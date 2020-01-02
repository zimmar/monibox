from django.shortcuts import render
from django.views.decorators.cache import never_cache

from .models.cfg_models import CfgPytsmOverviewbox, CfgPytsmOverview
from .utils.camelcase import snake_to_camel
from .utils.cfg_queries import get_servers
from .utils.import_mod import _import_module


# Create your views here.
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
    for server in servers:

        tabelle_name = servers[server].cfg_pytsm_server_tabelle(overview=True, cl=False)
        tabelle_class = servers[server].cfg_pytsm_server_tabelle(overview=True, cl=True)

        db_module = _import_module("application.pytsm.models.{}".format(tabelle_name))
        tabclass = getattr(db_module, tabelle_class)
        values  = tabclass.objects.all()
        x[server] = values

    overviewbox_qs = CfgPytsmOverviewbox.objects.all()
    overview_qs = CfgPytsmOverview.objects.values(
        'cfg_pytsm_base_label', 'cfg_pytsm_base_name', 'cfg_pytsm_overview_parent__cfg_pytsm_base_label')

    return render(request, "pytsm/index.html", {'overviewbox': overviewbox_qs,
                                                'overview': overview_qs,
                                                'servers': servers,
                                                'values': x })


def overview(request, mainname, subname):
    servers = get_servers()
    x = {}
    temp = {}
    for server in servers:

        tabelle_name = servers[server].cfg_pytsm_server_tabelle(overview=True, cl=False)
        tabelle_class = servers[server].cfg_pytsm_server_tabelle(overview=True, cl=True)

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
