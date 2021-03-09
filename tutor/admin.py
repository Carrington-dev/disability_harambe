from django.contrib import admin

# Register your models here.
import csv
import datetime

from django.http import HttpResponse
from django.contrib import admin
from tutor.models import Subject
from tutor.models import Course
from tutor.models import Module
from tutor.models import Review
from tutor.models import Video
from tutor.models import Text
from tutor.models import File
from tutor.models import Image

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


class CourseInLine(admin.StackedInline):
    model = Course
    

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    actions = [export_to_csv]
    inlines = [CourseInLine]


class ModuleInline(admin.StackedInline):
    model = Module
    



class TextInLine(admin.StackedInline):
    model = Text
    


class VideoInLine(admin.StackedInline):
    model = Video
    


class FileInLine(admin.StackedInline):
    model = File
   


class ImageInLine(admin.StackedInline):
    model = Image



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'created', 'document', 'updated']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'created', 'document', 'updated']


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'created', 'content', 'updated']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'created', 'url', 'updated']



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'date_created', 'image', 'author']
    list_filter = ['date_created', 'subject']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
    actions = [export_to_csv]




    
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'numbering', 'course']
    # list_filter = ['course',]
    # search_fields = ['title',]
    # prepopulated_fields = {'slug': ('title',)}
    prepopulated_fields = {'slug': ('title',)}
    actions = [export_to_csv]
    ordering = ['numbering']

    inlines = [TextInLine,VideoInLine,FileInLine,ImageInLine]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'rating', 'user_name', 'comment', 'pub_date']
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
    actions = [export_to_csv]


# @admin.register(Cluster)
# class ClusterAdmin(admin.ModelAdmin):
#     list_display = ['name', 'get_members']


# admin.site.register(BadgeAward)