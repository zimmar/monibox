from io import StringIO
from django.db import DEFAULT_DB_ALIAS, connections
from django.core.management import call_command
from base.utils.logger import log

def create_table(table_name, using=DEFAULT_DB_ALIAS):
    connection = connections[using]

    c = connection.cursor()
    try:
        sql = "CREATE TABLE IF NOT EXISTS {tablename} (id INTEGER PRIMARY KEY AUTOINCREMENT, time DATETIME, name CHARACTER(35) UNIQUE, results CHARACTER(255));".format(
            tablename=table_name)
        print(sql)
        c.execute(sql)
    except:
        log.error("Tabelle {} could not created.".format(table_name))
    finally:
        out = StringIO()
        call_command('inspectdb', table_name, stdout=out)
        with open('application/pytsm/models/{}.py'.format(table_name), 'w') as file:
            file.write(out.getvalue())
        print(out.getvalue())
        file.close()
        c.close()
        call_command('migrate')