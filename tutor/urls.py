from django.contrib import admin
from django.urls import path, include
from account import views
from contact import views
from django.conf import settings
from django.conf.urls.static import static
from tutor import views

urlpatterns = [
    path('tutor', views.tutor_view),
    path('', views.CoursesListView.as_view(), name="courses"),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name="course-detail"),
   
]