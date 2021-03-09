"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views as account_views

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', account_views.home, name='home'),
    path('about/', account_views.about, name='about'),

    path('profile/', account_views.profile, name='profile'),
    # path('surveys/', account_views.surveys, name='surveys'),
    path('register/', account_views.registration_view, name='register'),
    path('forgot-password/', account_views.registration_view, name='forgot'),
    path('logout-successful/', account_views.logout_success, name='logout-success'),
    path('reset/', account_views.reset, name="reset"),
    path('login/', account_views.login_view, name="login"),
    # path('admin/', admin.site.urls, name="admin"),

    #testing
    
    path('test/', account_views.test, name="test"),

    
    path('logout/', account_views.logout_view, name="logout"),
	path('must_authenticate/', account_views.must_authenticate_view, name="must_authenticate"),    
    path('benefits/', account_views.benefits, name='benefits'),
    path('covid/', account_views.covid_view, name='covid_19'),

    path('dashboard/', account_views.dashboard, name='dashboard'),


    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
    name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
      name='password_reset_complete'),
    
    # path('oauth/', include('social_django.urls', namespace='social')),  # <-- here

]