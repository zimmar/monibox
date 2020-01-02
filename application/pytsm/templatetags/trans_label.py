import datetime

from django import template
from base import const

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.filter
def trans(value):
    if str(value) in const.CFG_LABELS:
        return const.CFG_LABELS[str(value)]
    else:
        return value

@register.filter
def trans_cfg(value):
    value = value.replace('CFG_', 'LB_')
    if str(value) in const.CFG_LABELS:
        return const.CFG_LABELS[str(value)]
    else:
        return value