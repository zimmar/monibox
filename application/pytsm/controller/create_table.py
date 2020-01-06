from io import StringIO
import os
import importlib
from django.db import DEFAULT_DB_ALIAS, connections
from django.core.management import call_command
from base.utils.logger import log


def run_sql(table_name, ovvname, ttstamp, result, using=DEFAULT_DB_ALIAS):
    connection = connections[using]

    c = connection
    try:
        sql = 'INSERT INTO "main.{tablename}" (timestamp, name, result) values ("{timestamp}", "{overviewname}", "{result}") ON DUPLICATE KEY update result="{result}", timestamp="{timestamp}";'.format(tablename=table_name, overviewname=ovvname, timestamp=ttstamp, result=result)
        print(sql)
        c.execute(sql)
    except:
        print("Can not insert in {tablename}, {overviewname}".format(tablename=table_name, overviewname=ovvname))


def create_table(table_name, using=DEFAULT_DB_ALIAS):
    connection = connections[using]

    c = connection.cursor()
    try:
        sql = "CREATE TABLE IF NOT EXISTS {tablename} (id INTEGER PRIMARY KEY AUTOINCREMENT, time DATETIME, name CHARACTER(35) UNIQUE, results CHARACTER(255));".format(
            tablename=table_name)
        c.execute(sql)
    except:
        log.error("Tabelle {} could not created.".format(table_name))
    finally:
        out = StringIO()
        call_command('inspectdb', table_name, stdout=out)

        with open('application/pytsm/models/{}.py'.format(table_name), 'w') as file:
           file.write(out.getvalue())

        # with open('application/pytsm/models/x{}.py'.format(table_name), "r") as input:
        #    with open('application/pytsm/models/{}.py'.format(table_name), "w") as output:
        ##        for line in input:
        #            if "managed" not in line:
        #                output.write(line)

        # if os.path.exists('application/pytsm/models/x{}.py'.format(table_name)):
        #    os.remove('application/pytsm/models/x{}.py'.format(table_name))

        # sql = "DROP TABLE IF EXISTS {tablename}".format(tablename=table_name)
        # c.execute(sql)

        # from application.pytsm.models import table_name

        # call_command('makemigrations')
        # call_command('migrate')


def truncate_table(table_name,using=DEFAULT_DB_ALIAS):

    connection = connections[using]

    c = connection.cursor()
    try:
        sql = "TRUNCATE TABLE {tablename}".format(tablename=table_name)
        c.execute(sql)
    except:
        log.error("Tabelle {} could not created.".format(table_name))