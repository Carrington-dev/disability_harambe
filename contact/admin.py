from django.contrib import admin
from contact.models import Contact

import csv
import datetime

from django.http import HttpResponse
from django.contrib import admin
from tutor.models import Subject


from django.utils.translation import gettext_lazy as _


def mark_as_viewed(self, request, queryset):
    queryset.update(viewed=True)


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
            filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'


# Register your models here.
@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject','message','viewed','date_sent']
    list_filter = ['name', 'subject','email']
    search_fields = ['name', 'email']
    # prepopulated_fields = {'slug': ('name',)}
    # inlines = [ModuleInline]
    actions = [export_to_csv, mark_as_viewed]