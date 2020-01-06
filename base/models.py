from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import const
from application.pytsm.const import CFG_LABELS, CFG_NAMES


# Create your models here.

class CfgTsmBaseMixin(models.Model):
    """
    Basisklasse (abstract):
    """
    COLORS = {}

    class Meta:
        abstract = True

    cfg_pytsm_base_name = models.CharField(max_length=45, null=False, unique=True, help_text=const.H_CFG_BASIS_NAME,
                                           verbose_name=_('Name'), default="CFG_")
    cfg_pytsm_base_label = models.CharField(max_length=45, null=False, help_text=const.H_CFG_BASIS_LABEL,
                                            verbose_name=_('Label'), default='label')
    cfg_pytsm_base_sortorder = models.SmallIntegerField(null=False, default=10, help_text=const.H_CFG_BASIS_SORT,
                                                        verbose_name=_('Sort'))

    def display_list(self):
        pass

    def __str__(self):
        return self.cfg_pytsm_base_label

    def cfg_pytsm_base_label_trans(self):
        rc = self.cfg_pytsm_base_label
        if self.cfg_pytsm_base_label in CFG_LABELS:
            rc = CFG_LABELS[self.cfg_pytsm_base_label]
        return rc

    def cfg_pytsm_base_trans_name(self):
        rc = self.cfg_pytsm_base_name
        if self.cfg_pytsm_base_name in CFG_NAMES:
            rc = CFG_NAMES[self.cfg_pytsm_base_name]
        return rc




class CfgTsmAlertMixin(models.Model):
    """
    Basisklasse Alarmierung (abstract)
    """
    ALERT_COMP = [
        ('equal', _('equal')),
        ('notequal', _('not equal')),
        ('less', _('less')),
        ('more', _('more')),
    ]


    class Meta:
        abstract = True

    cfg_pytsm_base_alert_cmp = models.CharField(max_length=35, choices=ALERT_COMP, null=True, blank=True, help_text=const.H_CFG_ALERT_CMP,
                                                verbose_name=_('Alert Compare'))
    cfg_pytsm_base_alert_val = models.CharField(max_length=35, null=True, blank=True, help_text=const.H_CFG_ALERT_VALUE,
                                                verbose_name=_('Alert Value'))
    cfg_pytsm_base_alert_col = models.CharField(max_length=35, null=True, blank=True,
                                                help_text=const.H_CFG_ALERT_COLUMN,
                                                verbose_name=_('Alert Column'))
    cfg_pytsm_base_alert_field = models.CharField(max_length=35, blank=True, null=True,
                                                  help_text=const.H_CFG_ALERT_FIELD,
                                                  verbose_name=_('Alert Field'))
    def __str__(self):
        return self.cfg_pytsm_base_alert_cmp
