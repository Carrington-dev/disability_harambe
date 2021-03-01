from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import DetailView, ListView
from . models import *
from . forms import *
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
# from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render,redirect




# import weasyprint


# Create your views here.






@login_required
def survey_dd(request):
    context = {'title' : "Africa Disability Alliance"}


    form = DDForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DDForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # subject = form.cleaned_data['subject']
            # email = form.cleaned_data['email']
            # name = form.cleaned_data['name']
            # message = form.cleaned_data['message']
            form.save()



            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request,f"Your information has been submitted")
            return redirect('survey-dd')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DDForm()
        # context['form'] = ContactForm()

    # return render(request, 'name.html', {'form': form})

    return render(request,"survey/survey_dd.html",{'form': form})



@login_required
def survey_sh(request):
    context = {'title' : "Africa Disability Alliance"}


    form = SHForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SHForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # subject = form.cleaned_data['subject']
            # email = form.cleaned_data['email']
            # name = form.cleaned_data['name']
            # message = form.cleaned_data['message']
            form.save()



            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request,f"Your information has been submitted")
            return redirect('survey-sh')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SHForm()
        # context['form'] = ContactForm()

    # return render(request, 'name.html', {'form': form})

    return render(request,"survey/survey_sh.html",{'form': form})



# @login_required
def surveys(request):
    title = "Africa Disability Alliance"
    return render(request,"survey/surveys.html",{"title":title})
