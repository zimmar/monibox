import csv
from gettext import find

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.http import HttpResponse
from . import const

# Register your models here.

class PyTSMAdminSite(AdminSite):
    """
    Custom admin site
    """
    site_header = 'PyTSM Admin'
    index_title = 'PyTSM Admin Portal'
    site_title = 'Welcome to Python Tivoli Storage Manager (PyTSM) Admin Portal'
    # site_url = 'pytsm'

pytsm_admin_site = PyTSMAdminSite(name='pytsm_admin')

## Actions

def copy_set(self, request, queryset):
    """
    Admin action: copy the selected dataset.
    """
    for object in queryset:
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        for field in field_names:
            if field[-3:]=='_id':
                setattr(object, field, None)
            if field[-5:]=='_name':
                setattr(object, field,  getattr(object, field) + '_copy')
            if field[-11:]=='_servername':
                setattr(object, field, getattr(object, field) + '_copy')
        object.save()

copy_set.short_description = "Copy Dataset"

def export_as_csv(self, request, queryset):

    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response

export_as_csv.short_description = "Export Selected"


class CustomModelAdminMixin(object):

    def __init__(self, model, admin_site):
        # in the list don't show username, password or id
        include = model._meta.fields

        excludelist = ['_id', '_username', '_password']

        self.list_display = ['trans_label' for field in model._meta.fields if (field.name == 'cfg_pytsm_base_label')]
        if 'trans_label' in self.list_display:
            excludelist.insert(1,"_label")
            excludelist.insert(2,"_name")

        # self.list_display += ['trans_parent' for field in model._meta.fields if (field.name[-7:] == '_parent')]
        # if 'trans_parent' in self.list_display:
        #     excludelist.insert(1,'_parent')

        print (excludelist)
        fields = model._meta.fields

        self.list_display += [field.name for field in model._meta.fields if (((field.name)[(field.name).rfind("_"):]) not in excludelist)]
        super(CustomModelAdminMixin, self).__init__(model, pytsm_admin_site)

    actions = [copy_set, export_as_csv]
    empty_value_display = '-empty-'

    def trans_label(self, object):
        if object.cfg_pytsm_base_label in const.CFG_LABELS:
            return const.CFG_LABELS[object.cfg_pytsm_base_label]


