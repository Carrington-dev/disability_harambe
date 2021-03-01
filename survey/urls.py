from django.contrib import admin
from django.urls import path
from . import views as survey_views

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from survey import views as survey_views

urlpatterns = [
    # path('', survey_views.SurveyListView.as_view(), name="surveys"),
    # path('survey/<int:pk>', survey_views.SurveyDetailView.as_view(), name="survey"),
    path('dd',survey_views.survey_dd, name='survey-dd'),
    path('sh/',survey_views.survey_sh, name='survey-sh'),
    path('', survey_views.surveys, name='surveys'),
    # path('admin/report/pdf/',views.admin_sh_report_pdf, name='admin_sh_report_pdf'),

]
