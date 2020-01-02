from django.utils.translation import ugettext_lazy as _
from application.pytsm.const import CFG_LABELS as PY_LABELS

H_CFG_BASIS_NAME = _("Name that is used internally.")
H_CFG_BASIS_LABEL = _("Label for the visible HTML page.")
H_CFG_BASIS_SORT = _("Sort order of the output.")

# Tabelle CfgAlert
H_CFG_ALERT_VALUE = _('Set alarm value.')
H_CFG_ALERT_CMP = _('Set alarm compare.')
H_CFG_ALERT_COLUMN = _('Comparison field for the alarm')
H_CFG_ALERT_FIELD = _('Selection of the data field from the query that is to be monitored.')


CFG_LABELS = {
    'LB_PYTSM_BASE_NODES': _("Nodes"),
    'LB_PYTSM_BASE_SERVER': _("Server"),
    'LB_PYTSM_BASE_BACKUP_ARCHIVE': _('Backup / Archive'),
    'LB_PYTSM_BASE_SCHEDULES' :_('Schedules'),
    'LB_PYTSM_BASE_ACTIVITY': _('Activity'),
    'LB_PYTSM_BASE_SERVER_STORAGE': _('Server Storage'),
    'LB_PYTSM_BASE_OFFSITE_MANAGEMENT': _('Offsite Management'),
}

CFG_LABELS.update(PY_LABELS)





