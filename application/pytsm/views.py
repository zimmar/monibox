from django.shortcuts import render
from django.views.decorators.cache import never_cache

from .models.cfg_models import CfgPytsmOverviewbox, CfgPytsmOverview, LogPytsmPolldstat
from .utils.camelcase import snake_to_camel
from .utils.cfg_queries import get_servers
from .utils.import_mod import _import_module


# Create your views here.
@never_cache
def res_overview(server):

    temp = {}

    overviewbox_qs = CfgPytsmOverviewbox.objects.all()

    for box in overviewbox_qs:
        overview_qs = CfgPytsmOverview.objects.filter(cfg_pytsm_overview_parent__cfg_pytsm_base_label=box.cfg_pytsm_base_label).values('cfg_pytsm_base_label', 'cfg_pytsm_base_name', 'cfg_pytsm_base_name')
        for view in overview_qs:
            temp[box] = overview_qs
    return temp

@never_cache
def index(request):
    servers = get_servers()
    x = {}
    active_server = {}
    for server in servers:
        srv = servers[server]
        if srv.cfg_pytsm_server_checks:
            tabelle_name = srv.cfg_pytsm_server_tabelle(overview=True, cl=False)
            tabelle_class = srv.cfg_pytsm_server_tabelle(overview=True, cl=True)

            db_module = _import_module("application.pytsm.models.{}".format(tabelle_name))
            tabclass = getattr(db_module, tabelle_class)
            values  = tabclass.objects.all()

            x[server] = values
            active_server[server] = srv

    overviewbox_qs = CfgPytsmOverviewbox.objects.all()
    overview_qs = CfgPytsmOverview.objects.values(
        'cfg_pytsm_base_label', 'cfg_pytsm_base_name', 'cfg_pytsm_overview_parent__cfg_pytsm_base_label')

    log = LogPytsmPolldstat.objects.filter(log_pytsm_polldstat_id=1).first()
    print(log )
    return render(request, "pytsm/index.html", {'overviewbox': overviewbox_qs,
                                                'overview': overview_qs,
                                                'servers': active_server,
                                                'values': x,
                                                'log': log})


def overview(request, mainname, subname):
    servers = get_servers()
    x = {}
    temp = {}
    for server in servers:
        srv = servers[server]
        if srv.cfg_pytsm_server_checks:

            tabelle_name = srv.cfg_pytsm_server_tabelle(overview=True, cl=False)
            tabelle_class = srv.cfg_pytsm_server_tabelle(overview=True, cl=True)

            overviews = CfgPytsmOverview.objects.filter(cfg_pytsm_base_name=mainname).first()

            db_module = _import_module("application.pytsm.models.{}".format(tabelle_name))
            z = getattr(db_module, tabelle_class)
            w = z.objects.filter(name=subname).first()
            if w:
                x[server] = w.results
            else:
                x[server] = ""

    return render(request, "pytsm/tabelle.html", {'main': mainname, 'sub': subname,
                                                  'servers': servers, 'values': x})
