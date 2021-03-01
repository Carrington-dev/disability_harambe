from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import *
import csv
import datetime

from django.http import HttpResponse


from django.utils.translation import gettext_lazy as _

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



@admin.register(QuestionaireDData)
class QuestionaireDDataAdmin(admin.ModelAdmin):
    list_display = ['question_1',"question_2", "question_3","question_4",
    'question_5',"question_6", "question_7","question_8",
    'question_9',"question_10", "question_11","question_12",
    'question_13',"question_15", "question_15","question_16",
    'question_17',"question_18", "question_19","question_20",'question_21',"question_22", "question_23",]
    actions = [export_to_csv]
    ordering = ["-date_sent"]
    list_filter = ['question_1',"question_2", "question_3","question_4",
    'question_5',"question_6", "question_7","question_8",
    'question_9',"question_10", "question_11","question_12",
    'question_13',"question_15", "question_15","question_16",
    'question_17',"question_18", "question_19","question_20",'question_21',"question_22", "question_23",]
    search_fields = ['question_1',"question_2", "question_3","question_4",
    'question_5',"question_6", "question_7","question_8",
    'question_9',"question_10", "question_11","question_12",
    'question_13',"question_15", "question_15","question_16",
    'question_17',"question_18", "question_19","question_20",'question_21',"question_22", "question_23",]




@admin.register(QuestionaireStakeHolders)
class QuestionaireStakeHoldersAdmin(admin.ModelAdmin):
    list_display = ['question_1',"question_2", "question_3","question_4",
    'question_5',"question_6", "question_7","question_8",
    'question_9',"question_10", "question_11","question_12",
    'question_13',"question_15", "question_15","question_16",
    'question_17',"question_18", "question_19","question_20",'question_21',"question_22", "question_23",] #'report_pdf',
    actions = [export_to_csv]
    ordering = ["-date_sent"]
    list_filter = ['question_1',"question_2", "question_3","question_4",
    'question_5',"question_6", "question_7","question_8",
    'question_9',"question_10", "question_11","question_12",
    'question_13',"question_15", "question_15","question_16",
    'question_17',"question_18", "question_19","question_20",'question_21',"question_22", "question_23",]
    search_fields = ['question_1',"question_2", "question_3","question_4",
    'question_5',"question_6", "question_7","question_8",
    'question_9',"question_10", "question_11","question_12",
    'question_13',"question_15", "question_15","question_16",
    'question_17',"question_18", "question_19","question_20",'question_21',"question_22", "question_23",]
