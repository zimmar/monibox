import datetime

from django import template
from base import const

from application.pytsm.utils.import_mod import _import_module
from application.pytsm.utils.cfg_queries import get_servers, get_overview_queries, get_alarm_colors
register = template.Library()

DEVICE_ALARM = """
<td align="right" style="color: {fcolor}; background-color: {bgcolor}">{value} {unit}</td>
"""

DEVICE_NORMAL = """
<td align="right">{value} {unit}</td>
"""

@register.simple_tag
def overview_value(value, srv):

    servers = get_servers()
    server = servers[srv]

    overviews = get_overview_queries()

    tabelle_name = server.cfg_pytsm_server_tabelle(overview=True, cl=False)
    tabelle_class = server.cfg_pytsm_server_tabelle(overview=True, cl=True)

    db_module = _import_module("application.pytsm.models.{}".format(tabelle_name))
    tabclass = getattr(db_module, tabelle_class)

    val = tabclass.objects.filter(name=value).first()


    if val != None:
        overview = overviews[value]

        if overview.cfg_pytsm_overview_unit == '#': # Only number value without sign
            res_unit = ""

        else:
            res_unit = overview.cfg_pytsm_overview_unit

        res = DEVICE_NORMAL.format(value=val.results, unit=res_unit) # Default erow

        if overview.cfg_pytsm_base_alert_val != None or overview.cfg_pytsm_base_alert_val != '--empty--' :
            # can we change to float
            try:
                result = float((val.results).replace(",","."))
                compare = float((overview.cfg_pytsm_base_alert_val).replace(",","."))
            except:
            # change to float is not possible (datetime)
                result = val.results
                compare = overview.cfg_pytsm_base_alert_val

            if overview.cfg_pytsm_base_alert_cmp == 'less':
                if result < compare:
                    res = DEVICE_ALARM.format(fcolor="red", bgcolor="yellow", value=val.results, unit=res_unit)

            elif overview.cfg_pytsm_base_alert_cmp == 'notequal':
                if result != compare:
                    res = DEVICE_ALARM.format(fcolor="red", bgcolor="yellow", value=val.results, unit=res_unit)

            elif overview.cfg_pytsm_base_alert_cmp == 'equal':
                if result == compare:
                    res = DEVICE_ALARM.format(fcolor="red", bgcolor="yellow", value=val.results, unit=res_unit)

            elif overview.cfg_pytsm_base_alert_cmp == 'more':
                if result > compare:
                    res = DEVICE_ALARM.format(fcolor="red", bgcolor="yellow", value=val.results, unit=res_unit)

        return res
