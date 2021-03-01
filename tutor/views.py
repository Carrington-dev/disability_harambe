from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
from . models import *


from django.views.generic import DetailView, ListView, View
# from django.views.generic.list import ListView, DetailView
from .models import Course




def tutor_view(request):
    return render(request, "tutor/tutor.html")

class CoursesListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name='tutor/course_list.html'
    ordering = ["-date_created"]
    paginate_by = 3



class CourseDetailView(DetailView):
    model = Course
    modules = Module.objects.all()
    context_object_name = 'course'
    template_name='tutor/course_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        context['modules'] = Module.objects.all()
        context['texts'] = Text.objects.all()
        context['files'] = File.objects.all()
        context['images'] = Image.objects.all()
        return context

class CourseView(View):

    pass

# class ManageCourseListView(ListView):
#     model = Course
#     template_name = 'courses/manage/course/list.html'

#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(owner=self.request.user)
