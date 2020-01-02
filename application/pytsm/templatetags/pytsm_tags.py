import datetime

from django import template
from base import const

from application.pytsm.utils.import_mod import _import_module
from application.pytsm.utils.cfg_queries import get_servers, get_overview_queries, get_alarm_colors
register = template.Library()

DEVICE_ALARM = """
<style="color: {{ fcolor }}; background-color: {{ bgcolor }}">{{ value }}</label>
"""

@register.simple_tag
def overview_value(value, srv):

    servers = get_servers()
    server = servers[srv]

    overviews = get_overview_queries()
    alarms = get_alarm_colors()

    tabelle_name = server.cfg_pytsm_server_tabelle(overview=True, cl=False)
    tabelle_class = server.cfg_pytsm_server_tabelle(overview=True, cl=True)

    db_module = _import_module("application.pytsm.models.{}".format(tabelle_name))
    tabclass = getattr(db_module, tabelle_class)
    val = tabclass.objects.filter(name=value).first()
    if val != None:
        overview = overviews[value]
        if overview.cfg_pytsm_base_alert_val != None:
            if val.results < overview.cfg_pytsm_base_alert_val:
                 res = " Alarm -- {}".format(val.results)

            else:
                res = "{}".format(val.results)
        else:
            res = "{}".format(val.results)
        return res
    return None