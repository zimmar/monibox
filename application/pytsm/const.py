from django.utils.translation import ugettext_lazy as _

H_CFG_PYTSM_SRV_SERVERNAME = _('Get the servername (Host Alias)')
H_CFG_PYTSM_SRV_INSTANZNAME = _('Get the server instanzname (Host Alias)')
H_CFG_PYTSM_SRV_DESCRIPTION = _('Normaly the instanz name')
H_CFG_PYTSM_SRV_TCPIP = _('Networkaddress')
H_CFG_PYTSM_SRV_PORT = _('Port normaly 1500')
H_CFG_PYTSM_SRV_USERNAME = _('Username with use to query the server')
H_CFG_PYTSM_SRV_PASSWORD = _('Password')
H_CFG_PYTSM_SRV_LIBRARYCLIENT = _('If the server a librarymanager then True')
H_CFG_PYTSM_SRV_DEFAULT = _('If no other server selected, than this server is the default server.')
H_CFG_PYTSM_SRV_CHECK = _('Bevor you make updates or other test on TSM Server stop the checks.')

# Tabelle CfgColor
H_CFG_PYTSM_COLOR_NAME = _('Name of the color')
H_CFG_PYTSM_COLOR_VALUE = _('RGB value of the color.')

# Taebelle CfgConfig
H_CFG_CONFIG_KEY = "Key that is stuck in the application."
H_CFG_CONFIG_VALUE = "key value"
H_CFG_CONFIG_DESCRIPTION = "Description of the key value."

# Table LogHash
H_CFG_PYTSM_LOGHASH_TABLENAME = _("Tablename")
H_CFG_PYTSM_LOGHASH_HASH = _("MD5 Summe from tablename")

# Table logPolldLog
H_CFG_PYTSM_LOGPOLLDLOG_TIMESTAMP = _("Timestamp create Tablename")
H_CFG_PYTSM_LOGPOLLDLOG_SERVERNAME = _("Servername")
H_CFG_PYTSM_LOGPOLLDLOG_UPDATED = _("Last update of the table.")
H_CFG_PYTSM_LOGPOLLDLOG_NOT_CHANGED = _("Time span for how long no change has taken place.")
H_CFG_PYTSM_LOGPOLLDLOG_POLLFREQ_NOT_REACHED = _("Repeat period has not yet been reached.")
H_CFG_PYTSM_LOGPOLLDLOG_TIMENEEDED = _("Time required for last job.")

# Table logPolldstat
H_CFG_PYTSM_LOGPOLLDSTAT_ENABLED = _("")
H_CFG_PYTSM_LOGPOLLDSTAT_STATUS = _("")
H_CFG_PYTSM_LOGPOLLDSTAT_LASTRUN = _("")
H_CFG_PYTSM_LOGPOLLDSTAT_NEXTRUN = _("")

# Table Joblist
H_CFG_PYTSM_JOBLIST_SERVERNAME = _("")
H_CFG_PYTSM_JOBLIST_PID = _("")
H_CFG_PYTSM_JOBLIST_STATUS = _("")
H_CFG_PYTSM_JOBLIST_NEXTRUN = _("")
H_CFG_PYTSM_JOBLIST_LASTRUN = _("")

# Table Overview
H_CFG_PYTSM_OVERVIEW_QUERY = _("")
H_CFG_PYTSM_OVERVIEW_UNIT = _("")
H_CFG_PYTSM_OVERVIEW_NOTFORLIBCLIENT = _("")
H_CFG_PYTSM_OVERVIEW_POLLFREQ = _("")
H_CFG_PYTSM_OVERVIEW_PARENT = _("")

# Table Queries
H_CFG_PYTSM_QURIES_TSMQUERY_V5 = _("")
H_CFG_PYTSM_QURIES_TSMQUERY_V6 = _("")
H_CFG_PYTSM_QURIES_QUERY_FIELDS = _("")
H_CFG_PYTSM_QURIES_TIMETABLE_FIELDS = _("")
H_CFG_PYTSM_QURIES_QUERY_INFO = _("")
H_CFG_PYTSM_QURIES_ORDERBY = _("")
H_CFG_PYTSM_QURIES_NOTFORLIBCLIENT = _("")
H_CFG_PYTSM_QURIES_POLLTYPE = _("")
H_CFG_PYTSM_QURIES_POLLFREQ = _("")
H_CFG_PYTSM_QURIES_PARENT = _("")
H_CFG_PYTSM_QURIES_SORTORDER = _("")

CFG_LABELS = {
    # Table CfgOverviewboxes
    "LB_PYTSM_SCHEDULE_STATUS": _("Schedule Status"),
    "LB_PYTSM_TOTALDATA": _("Total Data"),
    "LB_PYTSM_DATABASE": _("Database"),
    "LB_PYTSM_HEALTH_STATUS": _("Health Status"),
    "LB_PYTSM_HEALTH_DATA": _("Health Status"),

    # Tabelle CfgOverview
    "LB_PYTSM_TOTAL_DATA_STORED": _("Total data stored"),
    "LB_PYTSM_TOTAL_DATA_BACKUPED": _("Totel data backuped"),
    "LB_PYTSM_TOTAL_DATA_COPY_BACKUPED": _("Totel data copy backuped"),

    "LB_PYTSM_TOTAL_DATA_ARCHIVED": _("Total data archived"),
    "LB_PYTSM_TOTAL_DATA_COPY_ARCHIVED": _("Total data copy archived"),

    'LB_PYTSM_HEALTH_DATA_SCRATCH_TAPES': _("Scratch Tapes"),
    'LB_PYTSM_HEALTH_DATA_VOLUMES_WITH_ERRORS': _("Volumes with errors"),
    'LB_PYTSM_HEALTH_DATA_UNAVAILABLE_VOLUMES': _("Unavailable Volumes"),
    'LB_PYTSM_HEALTH_DATA_DRIVES_OFFLINE': _("Drives Offline"),
    'LB_PYTSM_HEALTH_DATA_PATHS_OFFLINE': _("Paths Offline"),
    'LB_PYTSM_DATABASE_CHACHE_HIT': _("Cache Hit"),
    'LB_PYTSM_DATABASE_USAGE': _("Database usage"),
    'LB_PYTSM_DATABASE_LOG_USAGE': _("Log Usage"),
    'LB_PYTSM_DATABASE_DB_FRAGMENTATION': _("DB Fragmentation"),
    'LB_PYTSM_DB_VOLUMES_NOT_SYNCED': _("DB Volumes not synced"),
    'LB_PYTSM_DATABASE_LOG_NOT_SYNCED': _("DB Logs Not Synced"),
    'LB_PYTSM_DB_BACKUP': _("Last DB Backup"),
    'LB_PYTSM_SCHEDULES_FAILED_ADMIN': _("Failed Admin Schedules"),
    'LB_PYTSM_SCHEDULES_FAILED_CLIENT': _("Failed Client Schedules"),
    'LB_PYTSM_SCHEDULES_RUNNING_CLIENT': _("Running Client Schedules"),
    'LB_PYTSM_SCHEDULES_RUNNING_ADMIN': _("Running Admin Schedules"),

    # Tabelle CfgMainmenu

    # Tabelle Queries
    "LB_PYTSM_QUERIES_ALL_NODES": _("All Nodes"),
    "LB_PYTSM_QUERIES_INACTIVE_NODES": _("Inactive Nodes"),
    "LB_PYTSM_QUERIES_FILESPACES": _("Filespaces"),
    "LB_PYTSM_QUERIES_STALLED_FILESPACES": _("Stalled Filespaces"),
    "LB_PYTSM_QUERIES_SPACE_USAGE_/_NODE": _("Space Usage je Node"),
    "LB_PYTSM_QUERIES_DATA_AND_TAPES_/_NODE": _("Data and Tapes je Node"),
    "LB_PYTSM_QUERIES_TAPES_USED_BY_NODE": _("Tape used by Node"),
    "LB_PYTSM_QUERIES_SERVER_OVERVIEW": _("Serveroverview"),
    "LB_PYTSM_QUERIES_OTHER_SERVERS": _("Other Servers"),
    "LB_PYTSM_QUERIES_DATABASE": _("Database"),
    "LB_PYTSM_QUERIES_MANAGEMENT_CLASSES": _("Managemenet Classes"),
    "LB_PYTSM_QUERIES_POLICY_SETS": _("Policy Set"),
    "LB_PYTSM_QUERIES_DOMAINS": _("Domains"),
    "LB_PYTSM_QUERIES_BACKUP_COPYGROUPS": _("Backup Copygroups"),
    "LB_PYTSM_QUERIES_ARCHIVE_COPYGROUPS": _("Archive Copygroups"),
    "LB_PYTSM_QUERIES_DRIVES": _("Drives"),
    "LB_PYTSM_QUERIES_PATHS": _("Pahts"),
    "LB_PYTSM_QUERIES_DISASTER_RECOVERY_MEDIA": _("Desaster Revocery Media"),
    "LB_PYTSM_QUERIES_BACKUP_STATUS_/_24H": _("Backup Status last 24 h"),
    "LB_PYTSM_QUERIES_BACKUP_TIMES": _("Backup Times"),
    "LB_PYTSM_QUERIES_BACKUP_TIMES_/_24H": _("Backup Times last 2"),
    "LB_PYTSM_QUERIES_ARCHIVE_STATUS_/_24H": _("Archive Status last 24h"),
    "LB_PYTSM_QUERIES_ARCHIVE_TIMES": _("Archive Times"),
    "LB_PYTSM_QUERIES_ARCHIVE_TIMES_/_24H": _("Archive Times last 24h"),
    "LB_PYTSM_QUERIES_CLIENT_SCHEDULES_DEFINITIONS": _("Client Schedule definitions"),
    "LB_PYTSM_QUERIES_CLIENT_SCHEDULES_RESULTS": _("Client Schedult results"),
    "LB_PYTSM_QUERIES_ADMIN_SCHEDULES_DEFINITIONS": _("Admin Schedule definitions"),
    "LB_PYTSM_QUERIES_ADMIN_SCHEDULES_RESULTS": _("Amdin Schedules Results"),
    "LB_PYTSM_QUERIES_ASSOSSIATIONS": _("Assossiations"),
    "LB_PYTSM_QUERIES_MIGRATION": _("Migration"),
    "LB_PYTSM_QUERIES_RUNNING_PROCESSES": _("Running Processes"),
    "LB_PYTSM_QUERIES_ACTIVE_SESSIONS": _("Active Sessions"),
    "LB_PYTSM_QUERIES_MOUNT_STATUS": _("Mount Status"),
    "LB_PYTSM_QUERIES_MOUNT_HISTORY": _("Mount History"),
    "LB_PYTSM_QUERIES_WARNINGS": _("Warnings"),
    "LB_PYTSM_QUERIES_ERRORS": _("Errors"),
    "LB_PYTSM_QUERIES_FREE_TAPES": _("Free Tapes"),
    "LB_PYTSM_QUERIES_FREE_TAPES_/_POOL": _("Free Tapes je Pool"),
    "LB_PYTSM_QUERIES_STORAGEPOOLS": _("Storagepools"),
    "LB_PYTSM_QUERIES_SPACE_RECLAMATION": _("Space Reclamation"),
    "LB_PYTSM_QUERIES_ERROR_TAPES": _("Error Tapes"),
    "LB_PYTSM_QUERIES_VOLUMES": _("Volumes"),
    "LB_PYTSM_QUERIES_LIBRARY_VOLUMES": _("Library Volumes"),
    "LB_PYTSM_QUERIES_BACKUPSETS": _("Backupsets"),
    "LB_PYTSM_QUERIES_EXPORTS": _("Exports"),
    "LB_PYTSM_QUERIES_OFFSITE_TAPES": _("Offsite Tapes"),

    "LB_PYTSM_HEALTH_NODES": _("Nodes Health"),
    "LB_PYTSM_TOTAL_NODES": _("Total Nodes"),
    "LB_PYTSM_TOTAL_NODES_LOCKED": _("Total Nodes Locked"),
}

CFG_NAMES = {
    'TEST': _('TEST')

}
