from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
import csv
import datetime

from django.http import HttpResponse
from django.contrib import admin
from post.models import *


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


class TextInLine(admin.StackedInline):
    model = Text

class VideoInLine(admin.StackedInline):
    model = Video

class FileInLine(admin.StackedInline):
    model = File

class ImageInLine(admin.StackedInline):
    model = Image

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'author', 'date_posted']
    list_filter = ['title', 'author']
    search_fields = ['title', 'author']
    # prepopulated_fields = {'slug': ('title',)}
    # inlines = [ModuleInline]
    actions = [export_to_csv]


    inlines = [TextInLine,VideoInLine,FileInLine,ImageInLine]



@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'created', 'updated']
    list_filter = ['created', 'title']
    search_fields = ['title', 'post']
    # prepopulated_fields = {'slug': ('title',)}
    # inlines = [ModuleInline]
    actions = [export_to_csv]



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'created', 'updated']
    list_filter = ['created', 'title']
    search_fields = ['title', 'post']
    # prepopulated_fields = {'slug': ('title',)}
    # inlines = [ModuleInline]
    actions = [export_to_csv]



@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'created', 'updated']
    list_filter = ['created', 'title']
    search_fields = ['title', 'post']
    # prepopulated_fields = {'slug': ('title',)}
    # inlines = [ModuleInline]
    actions = [export_to_csv]



@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'created', 'updated']
    list_filter = ['created', 'title']
    search_fields = ['title', 'post']
    # prepopulated_fields = {'slug': ('title',)}
    # inlines = [ModuleInline]
    actions = [export_to_csv]