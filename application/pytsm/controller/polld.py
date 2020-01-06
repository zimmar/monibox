import os
from datetime import datetime
from datetime import timedelta
from time import sleep
from django.utils.timezone import get_current_timezone

from application.pytsm.models import CfgPytsmOverview, LogPytsmPolldstat, LogPytsmPolldlog
from application.pytsm.utils.cfg_queries import get_configs, get_overview_queries, get_servers
from application.pytsm.controller.core import dsmadmc
from base.utils.logger import log

from application.pytsm.const import CFG_LABELS
from .create_table import create_table, run_sql
from application.pytsm.utils.import_mod import _import_module

LOGLEVEL = {
    "NOTSET": 0,
    "ERROR": 40,
    "WARN": 30,
    "INFO": 20,
    "DEBUG": 10,
    "CRITICAL": 50
}


class PollD(object):
    """
    polld.py PyTSM Monitor

    This file is the TSM Monitor Polling Daemon. It executes queries against TSM
    and inserts them into TSM Monitor's MySQL Database

    @author Martin Zimmermann
    @version 1.0
    @package pytsm
    """

    # Privat variable
    _servers = {}
    _queries = {}
    _lastrun = 0
    _os = ""

    _overviewqueries = {}
    _configs = {}
    _dsmadmc = ""

    # _debuglevel = 0  ## VERBOSE = 4, INFO = 3, WARN = 2, ERROR = 1, OFF = 0
    # _loghandle = 0

    _log_timeneeded = 0
    _log_unchangedresult = 0
    _log_pollfreqreached = 0
    _log_updated = 0

    def __init__(self):
        # Debuglevel
        log.setLevel("INFO")
        self._configs = get_configs()
        log.info("Configuration was loaded successfully.")
        # self.write_msg(, "INFO")

        log.setLevel(self._configs['loglevel_polld'])
        # self.set_debug_level(loglevel)

        log.name = self._configs['path_polldlog']
        # log.
        #if logfile != "":
        #    try:
        #        self._loghandle = open("{}".format(logfile), 'a+t')
        #    except Exception as e:
        #        self.write_msg(
        #            "Can not open logfile: {} for writing. Failing back to STDOUT. {}".format(logfile, str(e)), "ERROR")

        tsmclient = self._configs['path_dsmadmc']
        if tsmclient != "":
            if (os.path.isfile(tsmclient)) and os.access(tsmclient, os.X_OK):
                self._dsmadmc = tsmclient
            else:
                log.error("dsmadmc is not executable. %s", tsmclient)
                # self.write_msg("dsamdmc is not executable.", "ERROR")
                exit(4)
        else:
            log.error("Module PyTSM from Monibox has not been installed correctly, path to dsmadmc could not be found.")
            # self.write_msg(
            #    "Module PyTSM from Monibox has not been installed correctly, path to dsmadmc could not be found.",
            #    "ERROR")
            exit(2)

        self.init_queries() # Table load

    def __del__(self):
        pass

    def init_queries(self):
        self._servers = get_servers()
        log.info("Servers was loaded sucessfully")

        # Todo: Queries are not implemented
        # self._queries = get_queries()
        # self.write_msg("Queries was loaded successfully.", 'INFO')

        self._overviewqueries = get_overview_queries()
        log.info("Overviewqueries was loaded successfully.")

    def getServerVersion(self, server, logfile="dsmerror.log"):
        print("------Serverversion from {}".format(server.cfg_pytsm_server_servername))
        dsm = self._configs['path_dsmadmc']
        dsm.open(server.cfg_pytsm_server_servername, server.cfg_pytsm_server_username, server.cfg_pytsm_server_password, logfile)
        dsm.execute("select version from status")

    @staticmethod
    def setPollDStatus(status="", lastrun="", nextrun=""):
        """

        """
        qs_x = LogPytsmPolldstat.objects.filter(log_pytsm_polldstat_id=1)
        if (status != ""):
            qs_x.update(log_pytsm_polldstat_status=status)
        if (lastrun != ""):
            qs_x.update(log_pytsm_polldstat_lastrun=lastrun)
        if (nextrun != ""):
            qs_x.update(log_pytsm_polldstat_nextrun=nextrun)

    @staticmethod
    def isEnabled():
        qs_rc = LogPytsmPolldstat.objects.values('log_pytsm_polldstat_enabled').filter(log_pytsm_polldstat_id=1)
        rc = qs_rc[0]
        return rc['log_pytsm_polldstat_enabled']

    @staticmethod
    def controlPollD(switch=""):
        if switch == 'on':
            val = 1
        elif switch == 'off':
            val = 0
        else:
            return ""
        qs_x = LogPytsmPolldstat.objects.filter(log_pytsm_polldstat_id=1)
        qs_x.update(log_pytsm_polldstat_enabled=val)

    @staticmethod
    def getStatus():
        qs_x = LogPytsmPolldlog.objects.values('log_pytsm_polldstat_status').filter(log_pytsm_polldlog_id=1)
        rc = qs_x[0]
        return rc['log_pytsm_polldstat_status']

    @staticmethod
    def getSleepTime():

        minoverview = CfgPytsmOverview.objects.aggregate(min, "cfg_pytsm_overview_pollfreq")
        return minoverview * 60

    def poll_query(self, query, server, ignore_pollfreq, timestamp):
        pass

    def poll_drop_table(self, server):

        # result = execute
        tabelle_name = server.cfg_pytsm_server_tabelle(overview=True, cl=False)
        tabelle_class = server.cfg_pytsm_server_tabelle(overview=True, cl=True)

        db_module = _import_module("application.pytsm.models.{}".format(tabelle_name))
        tabclass = getattr(db_module, tabelle_class)

        tabclass.truncate()


    def poll_overview_query(self, query, server, timestamp):
        startquery = datetime.now()
        querytime = 0
        srv = server.cfg_pytsm_server_servername.replace("-","_")
        tablename = "res_overview_{servername}_{instanz}".format(servername=srv,
                                                                 instanz=server.cfg_pytsm_server_instanzname)
        log.info("---------{} - {}".format(query.cfg_pytsm_base_name, CFG_LABELS[query.cfg_pytsm_base_label]))
        create_table(tablename)

        # result = execute
        tabelle_name = server.cfg_pytsm_server_tabelle(overview=True, cl=False)
        tabelle_class = server.cfg_pytsm_server_tabelle(overview=True, cl=True)
        try:
            db_module = _import_module("application.pytsm.models.{}".format(tabelle_name))
            tabclass = getattr(db_module, tabelle_class)
        except:
            # create    table
            log.error("Tabelle {} could not create".format(tabelle_class))

        dsmdmc = dsmadmc()
        dsmdmc.open(server.cfg_pytsm_server_servername, server.cfg_pytsm_server_username, server.cfg_pytsm_server_password, "dsmerror.log")
        result = dsmdmc.execute(query.cfg_pytsm_overview_query)
        dsmdmc.close()

        if (result != ""):
            # insert
            for insertresult in result:
                save_value_with_unit = "{} [{}]".format(insertresult[0], query.cfg_pytsm_overview_unit)
                save_value = "{}".format(insertresult[0])
                try: # insert
                    log.info('Insert new value {} {}'.format(query.cfg_pytsm_overview_unit, insertresult[0]))
                    obj = tabclass(time=datetime.now(), name=query.cfg_pytsm_base_name, results=save_value)
                    obj.save()
                except:
                    log.info('Update value {} {}'.format(query.cfg_pytsm_overview_unit, insertresult[0]))
                    obj = tabclass.objects.get(name=query.cfg_pytsm_base_name)
                    obj.time = datetime.now()
                    obj.results = save_value
                    obj.save()

            querytime = datetime.now() - startquery
            log.info ("insert row {} sec".format(querytime))
        else:
            log.error("There was a problem querying the TSM Server {}".format(server.cfg_pytsm_server_servername))


    def poll(self):
        sleeptime = int(self._configs['timeout'])
        log.info("Sleeptime will be {} seconds".format(sleeptime))

        while True:
            # poller is enabled
            if self.isEnabled():
                timestamp = datetime.now(tz=get_current_timezone())
                log.info("R U N Start!\ntimestamp for this run is {}".format(timestamp))
                self.setPollDStatus(status="running", lastrun="", nextrun="")
                for srv in self._servers:

                    server = self._servers[srv]

                    if server.cfg_pytsm_server_checks == True: # Server should be checked. (Run Queries True)

                        self._log_timeneeded = datetime.now()
                        self._log_unchangedresult = 0
                        self._log_pollfreqreached = 0
                        self._log_updated = 0

                        log.info("---quering server {}.".format(server.cfg_pytsm_server_servername))
                        log.info("------quering normal queries")

                        for qry in self._queries:
                            query = self._queries[qry]
                            # if server.cfg_pytsm_server_libraryclient == query.cfg_pytsm_queries_notforlibclient: #
                            log.info("--------- query {}".format(CFG_LABELS[query.cfg_pytsm_overview_query]))
                            self.poll_query(query, server, False, timestamp)

                        log.info("------quering overview queries")

                        if len(self._overviewqueries) > 0:

                            for qry in self._overviewqueries:
                                query = self._overviewqueries[qry]
                                # if server.cfg_pytsm_server_libraryclient != query.cfg_pytsm_overview_notforlibclient:
                                # log.info("--------- overviewquery {}".format(CFG_LABELS[query.label]))

                                self.poll_overview_query(query, server, timestamp)
                                x = LogPytsmPolldlog(timestamp, server.cfg_pytsm_server_servername, self._log_updated)

                log.info("needed {} seconds for this run".format(datetime.now(tz=get_current_timezone()) - timestamp))
                tempsleeptime = (timedelta(seconds=300) - (datetime.now(tz=get_current_timezone()) - timestamp)).seconds
                if tempsleeptime < 0:
                    tempsleeptime = 0

                log.info("sleeping for {} seconds ...".format(tempsleeptime))
                log.info("next run will be at {}".format((datetime.now(tz=get_current_timezone()) + timedelta(seconds=tempsleeptime)).strftime("%H:%M:%S")))
                self.setPollDStatus("sleeping",timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                                    (datetime.now(tz=get_current_timezone()) + timedelta(seconds=tempsleeptime)).strftime("%Y-%m-%d %H:%M:%S"))
                sleep(tempsleeptime)

            else:
                log.warn('PollD is disabled. Sleeping for {seconds} seconds'.format(seconds=sleeptime))
                self.init_queries() # Table reload

                sleep(sleeptime)
