from django.shortcuts import render, redirect
from . forms import *
from . models import *
# #social settings
# from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin

#my imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
title = "Africa Disability Alliance"



# class HomeView(LoginRequiredMixin, TemplateView):
#     template_name = "account/login.html" 
# Create your views here.

def home(request):
    
    return render(request,"account/index.html",{"title":title})

def about(request):
    title="About"
    return render(request,"account/about.html",{"title":title})

@login_required
def profile(request):

	
	if request.method == "POST":
		u_form = AccountUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f"Your account has been updated")
			return redirect("profile")
	
	else:
		u_form = AccountUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		"u_form": u_form,
		"p_form" : p_form,
		"title":"Profile"
	}
	return render(request,"account/profile.html",context)




@login_required
def dashboard(request):
	context = {"title":title}
	return render(request,"account/dashboard.html", context)




def logout_success(request):
    title="Logged Out"
	
    return render(request,"account/logout_successful.html",{"title":title})


# def login_view(request):
    
#     return render(request,"account/login.html",{"title":title})

def benefits(request):
    title="benefits"
    return render(request,"account/benefits.html",{"title":title})


def covid_view(request):
    title="Covid19"
    return render(request,"account/covid_19.html",{"title":title})


def test(request):
    return render(request,"account/test.html",{"title":title})


def reset(request):
    title="Password Reset"
    return render(request,"registration/password_reset.html",{"title":title})



def courses(request):
    title="Courses"
    return render(request,"tutor/courses.html",{"title":title})




def registration_view(request):
	context = {
		"title": "Register"
	}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			messages.success(request,f"Your registration was successful, You are now signed in to your account!")
			return redirect('home')
		else:
			# messages.error(request,f"Your registration was successful")
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)



# def register_view(request):
    
#     return render(request,"account/register.html",{"title":title})



def login_view(request):

	context = {
		'title': 'Log in'
	}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				messages.success(request,f"You are now logged in to your account!")
				return redirect("logout-success")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)



def logout_view(request):
	logout(request)
	messages.success(request,f"You are now logged out of your account!")
	return redirect('logout-success')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				messages.success(request,f"You are now logged in to your account!")
				return redirect("profile")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)


def account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)

	context['account_form'] = form

	blog_posts = BlogPost.objects.filter(author=request.user)
	context['blog_posts'] = blog_posts

	return render(request, "account/account.html", context)


def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html', {})


