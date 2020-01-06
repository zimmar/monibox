from django.db import models
from django.utils.translation import ugettext_lazy as _

from application.pytsm import conf, const
from base.models import CfgTsmBaseMixin, CfgTsmAlertMixin

from application.pytsm.utils.camelcase import snake_to_camel


# Create your models here.


class CfgPytsmColors(models.Model):
    """
    Class with which the colors of the status messages are defined.

    """
    cfg_pytsm_colors_id = models.SmallAutoField(primary_key=True)
    cfg_pytsm_colors_name = models.CharField(max_length=35, verbose_name=_('Name'), help_text=const.H_CFG_PYTSM_COLOR_NAME)
    cfg_pytsm_colors_value = models.CharField(max_length=7, verbose_name=_('Value'), help_text=const.H_CFG_PYTSM_COLOR_VALUE)

    class Meta:
        db_table = 'cfg_pytsm_colors'
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def display_list(self):
        return ['cfg_pytsm_colors_name', 'cfg_pytsm_colors_value']


class CfgPytsmConfig(models.Model):
    """
    Class with the dynamic configuration data to be set.
    The following entries must exist.

    """
    cfg_pytsm_config_id = models.SmallAutoField(primary_key=True)
    cfg_pytsm_config_confkey = models.CharField(max_length=35, verbose_name=_('Config Key'),
                                                help_text=const.H_CFG_CONFIG_KEY)
    cfg_pytsm_config_confval = models.CharField(max_length=255, verbose_name=_('Config Value'),
                                                help_text=const.H_CFG_CONFIG_VALUE)
    cfg_pytsm_config_description = models.CharField(max_length=255, verbose_name=_('Description'),
                                                    help_text=const.H_CFG_CONFIG_DESCRIPTION)

    class Meta:
        managed = True
        db_table = 'cfg_pytsm_config'
        verbose_name = 'Config'
        verbose_name_plural = 'Configs'

    def display_list(self):
        return ['cfg_pytsm_config_confkey', 'cfg_pytsm_config_confval', 'cfg_pytsm_config_description']


class CfgPytsmServer(models.Model):
    """
    Description of a server. Will only be here until cmdb has been developed.
    """

    class Meta:
        db_table = 'cfg_pytsm_server'
        verbose_name = 'Server'
        verbose_name_plural = 'Servers'
        unique_together = ('cfg_pytsm_server_servername', 'cfg_pytsm_server_instanzname', 'cfg_pytsm_server_port')

    cfg_pytsm_server_id = models.SmallAutoField(primary_key=True)
    cfg_pytsm_server_servername = models.CharField(max_length=35, null=False, help_text=const.H_CFG_PYTSM_SRV_SERVERNAME,
                                                   verbose_name=_('Servername'), db_index=True)
    cfg_pytsm_server_instanzname = models.CharField(max_length=35, null=False, default='tsminst1',
                                                    help_text=const.H_CFG_PYTSM_SRV_INSTANZNAME,
                                                    verbose_name=_('Instanzname'))
    cfg_pytsm_server_description = models.CharField(max_length=35, null=True, help_text=const.H_CFG_PYTSM_SRV_DESCRIPTION,
                                                    verbose_name=_('Description'))
    cfg_pytsm_server_ip = models.CharField(max_length=15, null=False, help_text=const.H_CFG_PYTSM_SRV_TCPIP,
                                           verbose_name=_('IP'))
    cfg_pytsm_server_port = models.PositiveSmallIntegerField(null=False, default=1500, help_text=const.H_CFG_PYTSM_SRV_PORT,
                                                             verbose_name=_('Port'))
    cfg_pytsm_server_username = models.CharField(max_length=35, null=False, help_text=const.H_CFG_PYTSM_SRV_USERNAME,
                                                 verbose_name=_('Username'))
    cfg_pytsm_server_password = models.CharField(max_length=35, null=False, help_text=const.H_CFG_PYTSM_SRV_PASSWORD,
                                                 verbose_name=_('Password'))
    cfg_pytsm_server_libraryclient = models.BooleanField(null=False, default=False,
                                                         help_text=const.H_CFG_PYTSM_SRV_LIBRARYCLIENT,
                                                         verbose_name=_('Libraryclient'))
    cfg_pytsm_server_default = models.BooleanField(null=False, default=False, help_text=const.H_CFG_PYTSM_SRV_DEFAULT,
                                                   verbose_name=_('Default'))
    cfg_pytsm_server_checks = models.BooleanField(null=False, default=True, help_text=const.H_CFG_PYTSM_SRV_CHECK,
                                                  verbose_name=_('Run Queries'))
    cfg_pytsm_server_url_name = conf.CFGSERVER_DETAIL_URL_NAME

    def __str__(self):
        return self.cfg_pytsm_server_servername

    def cfg_pytsm_server_tabelle(self, overview=False, cl=False):

        _name = ( self.cfg_pytsm_server_servername).replace("-", "_") + "_" + self.cfg_pytsm_server_instanzname
        if overview:
            _name = "res_overview_" + _name
        if cl:
            _name = snake_to_camel(_name)

        return _name

    @classmethod
    def display_list(cls):
        return ['cfg_pytsm_server_servername', 'cfg_pytsm_server_instanzname', 'cfg_pytsm_server_ip', 'cfg_pytsm_server_port', 'cfg_pytsm_server_default', 'cfg_pytsm_server_checks']


class CfgPytsmOverviewbox(CfgTsmBaseMixin):
    """

    """

    cfg_pytsm_overviewbox_id = models.SmallAutoField(primary_key=True)
    cfg_pytsm_overviewbox_icon = models.CharField(max_length=35, null=True, blank=True)

    class Meta:
        db_table = 'cfg_pytsm_overviewbox'
        verbose_name = 'Overviewbox'
        verbose_name_plural = 'Overviewboxes'


class CfgPytsmOverview(CfgTsmBaseMixin, CfgTsmAlertMixin):
    """
    Overview dashboard as a health check.
    Query is always done directly on the server. No intermediate values in a table.
    Queries that should be recorded in tables must be entered in CfgQuery.
    """

    class Meta:
        db_table = 'cfg_pytsm_overview'
        verbose_name = 'Overviewquery'
        verbose_name_plural = 'Overviewqueries'

    cfg_pytsm_overview_id = models.SmallAutoField(primary_key=True)
    cfg_pytsm_overview_query = models.CharField(max_length=255, null=False, help_text=const.H_CFG_PYTSM_OVERVIEW_QUERY,
                                                verbose_name=_('Overvie Query'))
    cfg_pytsm_overview_unit = models.CharField(max_length=10, null=True, help_text=const.H_CFG_PYTSM_OVERVIEW_UNIT,
                                               verbose_name=_('Unit'))
    cfg_pytsm_overview_notforlibclient = models.BooleanField(default=False,
                                                             help_text=const.H_CFG_PYTSM_OVERVIEW_NOTFORLIBCLIENT,
                                                             verbose_name=_('Not for libclient.'))
    cfg_pytsm_overview_pollfreq = models.PositiveSmallIntegerField(null=False, default=200,
                                                                   help_text=const.H_CFG_PYTSM_OVERVIEW_POLLFREQ,
                                                                   verbose_name=_('poll freq.'))
    cfg_pytsm_overview_parent = models.ForeignKey(to=CfgPytsmOverviewbox, on_delete=models.CASCADE,
                                                  help_text=const.H_CFG_PYTSM_OVERVIEW_PARENT,
                                                  verbose_name=_('Parent'))

    @classmethod
    def display_list(cls):
        return ['cfg_pytsm_base_label', 'cfg_pytsm_overview_unit', 'cfg_pytsm_overview_notforlibclient', 'cfg_pytsm_overview_pollfreq']


class CfgPytsmMainmenu(CfgTsmBaseMixin):
    """

    """

    class Meta:
        managed = True
        db_table = 'cfg_pytsm_mainmenu'
        verbose_name = 'Mainmenu'
        verbose_name_plural = 'Mainmenues'

    cfg_pytsm_mainmenu_id = models.SmallAutoField(primary_key=True)


class CfgPytsmQueries(CfgTsmBaseMixin, CfgTsmAlertMixin):

    POLLING_TYPE = [
        ('a', 'append'),
        ('s', 'snapshot'),
        ('u', 'update'),
    ]



    cfg_pytsm_queries_id = models.BigAutoField(primary_key=True)
    cfg_pytsm_queries_tsmquery_v5 = models.CharField(max_length=500,
                                                     help_text=const.H_CFG_PYTSM_QURIES_TSMQUERY_V5,
                                                     verbose_name=_("TSM Query V5"))
    cfg_pytsm_queries_tsmquery_v6 = models.CharField(max_length=500,
                                                     help_text=const.H_CFG_PYTSM_QURIES_TSMQUERY_V6,
                                                     verbose_name=_("TSM Query V6"))
    cfg_pytsm_queries_fields = models.CharField(max_length=1000,
                                                help_text=const.H_CFG_PYTSM_QURIES_QUERY_FIELDS,
                                                verbose_name=_("Query Fields"))
    cfg_pytsm_queries_timetablefields = models.CharField(max_length=255, blank=True, null=True,
                                                         help_text=const.H_CFG_PYTSM_QURIES_TIMETABLE_FIELDS,
                                                         verbose_name=_("Timetable Fields"))
    cfg_pytsm_queries_info = models.CharField(max_length=500, blank=True, null=True,
                                              help_text=const.H_CFG_PYTSM_QURIES_QUERY_INFO,
                                              verbose_name=_("Info"))
    cfg_pytsm_queries_orderby = models.CharField(max_length=35, blank=True, null=True,
                                                 help_text=const.H_CFG_PYTSM_QURIES_ORDERBY,
                                                 verbose_name=_("Order By"))
    cfg_pytsm_queries_notforlibclient = models.IntegerField(blank=True, null=True,
                                                            help_text=const.H_CFG_PYTSM_QURIES_NOTFORLIBCLIENT,
                                                            verbose_name=_("Not for lib client"))
    cfg_pytsm_queries_polltype = models.CharField(max_length=1, choices = POLLING_TYPE,
                                                  help_text=const.H_CFG_PYTSM_QURIES_POLLTYPE,
                                                  verbose_name=_("Polltype"))
    cfg_pytsm_queries_pollfreq = models.IntegerField(help_text=const.H_CFG_PYTSM_QURIES_POLLFREQ,
                                                     verbose_name=_("Pollfrequenz"))
    cfg_pytsm_queries_parent = models.ForeignKey(CfgPytsmMainmenu, on_delete=models.CASCADE,
                                                help_text=const.H_CFG_PYTSM_QURIES_PARENT,
                                                verbose_name=_("Parent ID"))

    class Meta:
        db_table = 'cfg_pytsm_queries'
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'


class JobPytsmList(models.Model):
    """
    Table structure for table 'JobList'
    """

    class Meta:
        db_table = 'job_pytsm_list'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    job_pytsm_list_id = models.BigAutoField(primary_key=True)
    job_pytsm_list_servername = models.CharField(max_length=35, null=False, help_text=const.H_CFG_PYTSM_JOBLIST_SERVERNAME,
                                                 verbose_name=_('Servername'))
    job_pytsm_list_pid = models.IntegerField(null=True, help_text=const.H_CFG_PYTSM_JOBLIST_PID, verbose_name=_('Pid'))

    job_pytsm_list_status = models.CharField(max_length=35, null=True, blank=True, help_text=const.H_CFG_PYTSM_JOBLIST_STATUS,
                                             verbose_name=_('Status'))
    job_pytsm_list_lastrun = models.DateTimeField(null=False, help_text=const.H_CFG_PYTSM_JOBLIST_LASTRUN,
                                                  verbose_name=_('Lastrun'))
    job_pytsm_list_nextrun = models.DateTimeField(null=False, help_text=const.H_CFG_PYTSM_JOBLIST_NEXTRUN,
                                                  verbose_name=_('Nextrun'))


class LogPytsmHash(models.Model):
    """
    Table structure for table 'log_hoshes'
    """

    class Meta:
        db_table = 'log_pytsm_hash'
        verbose_name = 'Hash'
        verbose_name_plural = 'Hashes'

    log_pytsm_hash_id = models.BigAutoField(primary_key=True)
    log_pytsm_hash_tablename = models.CharField(max_length=255, null=False, unique=True,
                                                help_text=const.H_CFG_PYTSM_LOGHASH_TABLENAME,
                                                verbose_name=_('Tablename'))
    log_pytsm_hash_hash = models.CharField(max_length=255, null=True, help_text=const.H_CFG_PYTSM_LOGHASH_HASH,
                                           verbose_name=_('HASH'))


class LogPytsmPolldlog(models.Model):
    """
    Table structure for table 'log_polldlog'
    """

    class Meta:
        db_table = 'log_pytsm_polldlog'
        verbose_name = 'PollDLog'
        verbose_name_plural = 'PollDLogs'

    log_pytsm_polldlog_id = models.BigAutoField(primary_key=True)
    log_pytsm_polldlog_timestamp = models.DateTimeField(null=False, help_text=const.H_CFG_PYTSM_LOGPOLLDLOG_TIMESTAMP,
                                                        verbose_name=_('Timestamp'))
    log_pytsm_polldlog_servername = models.CharField(max_length=30, null=False,
                                                     help_text=const.H_CFG_PYTSM_LOGPOLLDLOG_SERVERNAME,
                                                     verbose_name=_('Servername'))
    log_pytsm_polldlog_updated = models.DateTimeField(null=False, help_text=const.H_CFG_PYTSM_LOGPOLLDLOG_UPDATED,
                                                      verbose_name=_('Updated'))
    log_pytsm_polldlog_not_changed = models.DateTimeField(null=False, help_text=const.H_CFG_PYTSM_LOGPOLLDLOG_NOT_CHANGED,
                                                          verbose_name=_('Not Changed'))
    log_pytsm_polldlog_pollfreq_not_reached = models.DateTimeField(null=False,
                                                                   help_text=const.H_CFG_PYTSM_LOGPOLLDLOG_POLLFREQ_NOT_REACHED,
                                                                   verbose_name=_('Pollfrequenz not reached'))
    log_pytsm_polldlog_timeneeded = models.DateTimeField(null=False, help_text=const.H_CFG_PYTSM_LOGPOLLDLOG_TIMENEEDED,
                                                         verbose_name=_('Timeneeded'))


class LogPytsmPolldstat(models.Model):
    """
    Table structure for table 'log_polldstat'
    """

    class Meta:
        db_table = 'log_pytsm_polldstat'
        verbose_name = 'PollDStatus'
        verbose_name_plural = 'PollDStati'

    log_pytsm_polldstat_id = models.SmallAutoField(primary_key=True)
    log_pytsm_polldstat_enabled = models.BooleanField(null=False, default=True, help_text=const.H_CFG_PYTSM_LOGPOLLDSTAT_ENABLED,
                                                      verbose_name=_('Enabled'))
    log_pytsm_polldstat_status = models.CharField(max_length=35, null=True, blank=True,
                                                  help_text=const.H_CFG_PYTSM_LOGPOLLDSTAT_STATUS,
                                                  verbose_name=_('Status'))
    log_pytsm_polldstat_lastrun = models.DateTimeField(null=False, help_text=const.H_CFG_PYTSM_LOGPOLLDSTAT_LASTRUN,
                                                       verbose_name=_('Lastrun'))
    log_pytsm_polldstat_nextrun = models.DateTimeField(null=False, help_text=const.H_CFG_PYTSM_LOGPOLLDSTAT_NEXTRUN,
                                                       verbose_name=_('Nextrun'))

    def display_list(self):
        pass
