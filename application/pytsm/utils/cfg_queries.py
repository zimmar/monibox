from application.pytsm.models import CfgPytsmServer, CfgPytsmOverview, CfgPytsmQueries, CfgPytsmConfig, CfgPytsmColors

def get_alarm_colors():
    alarms = CfgPytsmColors.objects.all()
    return alarms

def get_servers():
    tmp_servers = {}
    servers = CfgPytsmServer.objects.all()
    for srv in servers:
        tmp_servers[srv.cfg_pytsm_server_servername] = srv
    return tmp_servers


def get_configs():
    tmp_config = {}
    configs = CfgPytsmConfig.objects.all()
    for obj in configs:
        tmp_config[obj.cfg_pytsm_config_confkey] = obj.cfg_pytsm_config_confval
    return tmp_config


def get_overview_queries():
    tmp_queries = {}
    ovv_qs = CfgPytsmOverview.objects.all()
    for ovv in ovv_qs:
        tmp_queries[ovv.cfg_pytsm_base_name] = ovv
    return tmp_queries


def get_queries():
    tmp_queries = {}
    q_qs = CfgPytsmQueries.objects.all()
    for qs in q_qs:
        tmp_queries[q_qs.cfg_pytsm_base_name] = qs
    return tmp_queries
