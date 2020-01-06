# -*- coding: utf-8 -*-
from django.contrib import admin

from base.admin import CustomModelAdminMixin, pytsm_admin_site
from .models import CfgPytsmColors, CfgPytsmConfig, CfgPytsmServer, CfgPytsmOverviewbox, CfgPytsmOverview, \
    CfgPytsmMainmenu, CfgPytsmQueries, LogPytsmPolldlog, LogPytsmHash, LogPytsmPolldstat

from . import const


## Actions

def enable_check(modeladmin, request, queryset):
    """
    Admin action: set check true
    """
    queryset.update(cfg_pytsm_server_checks=True)


enable_check.short_description = "Enable selected Server"


def disable_check(modeladmin, request, queryset):
    """
    Admin action: set check false
    """
    queryset.update(cfg_pytsm_server_checks=False)


disable_check.short_description = "Disable selected Server"


def enable_lib_client(modeladmin, request, queryset):
    """
    Admin action: set check true
    """
    queryset.update(cfg_pytsm_overview_notforlibclient=True)


enable_lib_client.short_description = "Enable lib client"


def disable_lib_client(modeladmin, request, queryset):
    """
    Admin action: set check false
    """
    queryset.update(cfg_pytsm_overview_notforlibclient=False)


disable_lib_client.short_description = "Disable lib client"




class CfgPytsmColorsAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    search_fields = ('cfg_pytsm_colors_name',)


class CfgPytsmConfigAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    search_fields = ('cfg_pytsm_config_name',)


class CfgPytsmServerAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    list_filter = ('cfg_pytsm_server_libraryclient', 'cfg_pytsm_server_default', 'cfg_pytsm_server_checks')
    search_fields = ('cfg_pytsm_server_servername', 'cfg_pytsm_server_instanzname')
    actions = CustomModelAdminMixin.actions + [disable_check, enable_check]
    list_display = CfgPytsmServer.display_list()


class CfgPytsmOverviewboxAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    search_fields = ('cfg_pytsm_overview_name',)


class CfgPytsmOverviewAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    list_filter = ('cfg_pytsm_overview_notforlibclient', 'cfg_pytsm_overview_parent')
    search_fields = ('cfg_pytsm_overview_name',)
    list_display = CfgPytsmOverview.display_list()
    actions = CustomModelAdminMixin.actions + [enable_lib_client, disable_lib_client]


class CfgPytsmMainmenuAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    search_fields = ('cfg_pytsm_mainmenu_name',)

class CfgPytsmQueriesAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    list_filter=('cfg_pytsm_queries_parent',)


class LogPytsmPolldstatAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    list_display = ('log_pytsm_polldstat_enabled', 'log_pytsm_polldstat_status', 'log_pytsm_polldstat_last run', 'log_pytsm_polldstat_snext run')



pytsm_admin_site.register(CfgPytsmColors, CfgPytsmColorsAdmin)
pytsm_admin_site.register(CfgPytsmConfig, CfgPytsmConfigAdmin)
pytsm_admin_site.register(CfgPytsmServer, CfgPytsmServerAdmin)
pytsm_admin_site.register(CfgPytsmOverviewbox, CfgPytsmOverviewboxAdmin)
pytsm_admin_site.register(CfgPytsmOverview, CfgPytsmOverviewAdmin)
pytsm_admin_site.register(CfgPytsmMainmenu, CfgPytsmMainmenuAdmin)
pytsm_admin_site.register(CfgPytsmQueries, CfgPytsmQueriesAdmin)
pytsm_admin_site.register(LogPytsmPolldstat, LogPytsmPolldstatAdmin)
