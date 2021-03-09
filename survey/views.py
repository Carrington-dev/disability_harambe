from django.shortcuts import render
from . import variables
# pdf related
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

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
    context = {'title' : "Survey Main"}


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
    context = {'title' : "Stakeholders"}


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
    title = "Surveys"
    return render(request,"survey/surveys.html",{"title":title})






# @login_required
def sh_report(request):
    title = "Stakeholders Survey"

    # orders = Order.objects.all()
    # customers = Customer.objects.all()

    # total_customers = customers.count()

    # total_orders = orders.count()
    # delivered = orders.filter(status='Delivered').count()
    # pending = orders.filter(status='Pending').count()

    questionaires = QuestionaireStakeHolders.objects.all()
    number_of_participants = questionaires.count()


    qdd_age_1 = questionaires.filter(age=group_A).count()
    qdd_age_2 = questionaires.filter(age=group_B).count()
    qdd_age_3 = questionaires.filter(age=group_C).count()
    qdd_age_4 = questionaires.filter(age=group_D).count()
    qdd_age_5 = questionaires.filter(age=group_E).count()
    qdd_age_6 = questionaires.filter(age=group_F).count()
    qdd_age_7 = questionaires.filter(age=group_G).count()
    qdd_age_8 = questionaires.filter(age=group_H).count()
    qdd_age_9 = questionaires.filter(age=group_I).count()
    qdd_age_10 = questionaires.filter(age=group_J).count()
    qdd_age_11 = questionaires.filter(age=group_K).count()
    qdd_age_12 = questionaires.filter(age=group_L).count()
    qdd_age_13 = questionaires.filter(age=group_M).count()
    qdd_age_14 = questionaires.filter(age=group_N).count()
    qdd_age_15 = questionaires.filter(age=group_O).count()

    q1_sd = questionaires.filter(question_1="Strongly disagree").count()
    q1_d = questionaires.filter(question_1="Disagree").count()
    q1_n = questionaires.filter(question_1="Neutral").count()
    q1_a = questionaires.filter(question_1="Agree").count()
    q1_sa = questionaires.filter(question_1="Strongly agree").count()


    q2_sd = questionaires.filter(question_2="Strongly disagree").count()
    q2_d = questionaires.filter(question_2="Disagree").count()
    q2_n = questionaires.filter(question_2="Neutral").count()
    q2_a = questionaires.filter(question_2="Agree").count()
    q2_sa = questionaires.filter(question_2="Strongly agree").count()


    q3_sd = questionaires.filter(question_3="Strongly disagree").count()
    q3_d = questionaires.filter(question_3="Disagree").count()
    q3_n = questionaires.filter(question_3="Neutral").count()
    q3_a = questionaires.filter(question_3="Agree").count()
    q3_sa = questionaires.filter(question_3="Strongly agree").count()



    q4_sd = questionaires.filter(question_4="Strongly disagree").count()
    q4_d = questionaires.filter(question_4="Disagree").count()
    q4_n = questionaires.filter(question_4="Neutral").count()
    q4_a = questionaires.filter(question_4="Agree").count()
    q4_sa = questionaires.filter(question_4="Strongly agree").count()



    q5_sd = questionaires.filter(question_5="Strongly disagree").count()
    q5_d = questionaires.filter(question_5="Disagree").count()
    q5_n = questionaires.filter(question_5="Neutral").count()
    q5_a = questionaires.filter(question_5="Agree").count()
    q5_sa = questionaires.filter(question_5="Strongly agree").count()



    
    q6_sd = questionaires.filter(question_6="Strongly disagree").count()
    q6_d = questionaires.filter(question_6="Disagree").count()
    q6_n = questionaires.filter(question_6="Neutral").count()
    q6_a = questionaires.filter(question_6="Agree").count()
    q6_sa = questionaires.filter(question_6="Strongly agree").count()




    q7_sd = questionaires.filter(question_7="Strongly disagree").count()
    q7_d = questionaires.filter(question_7="Disagree").count()
    q7_n = questionaires.filter(question_7="Neutral").count()
    q7_a = questionaires.filter(question_7="Agree").count()
    q7_sa = questionaires.filter(question_7="Strongly agree").count()


    q8_sd = questionaires.filter(question_8="Strongly disagree").count()
    q8_d = questionaires.filter(question_8="Disagree").count()
    q8_n = questionaires.filter(question_8="Neutral").count()
    q8_a = questionaires.filter(question_8="Agree").count()
    q8_sa = questionaires.filter(question_8="Strongly agree").count()



    q9_sd = questionaires.filter(question_9="Strongly disagree").count()
    q9_d = questionaires.filter(question_9="Disagree").count()
    q9_n = questionaires.filter(question_9="Neutral").count()
    q9_a = questionaires.filter(question_9="Agree").count()
    q9_sa = questionaires.filter(question_9="Strongly agree").count()



    q10_sd = questionaires.filter(question_10="Strongly disagree").count()
    q10_d = questionaires.filter(question_10="Disagree").count()
    q10_n = questionaires.filter(question_10="Neutral").count()
    q10_a = questionaires.filter(question_10="Agree").count()
    q10_sa = questionaires.filter(question_10="Strongly agree").count()



    q11_sd = questionaires.filter(question_11="Strongly disagree").count()
    q11_d = questionaires.filter(question_11="Disagree").count()
    q11_n = questionaires.filter(question_11="Neutral").count()
    q11_a = questionaires.filter(question_11="Agree").count()
    q11_sa = questionaires.filter(question_11="Strongly agree").count()



    q12_sd = questionaires.filter(question_12="Strongly disagree").count()
    q12_d = questionaires.filter(question_12="Disagree").count()
    q12_n = questionaires.filter(question_12="Neutral").count()
    q12_a = questionaires.filter(question_12="Agree").count()
    q12_sa = questionaires.filter(question_12="Strongly agree").count()



    q13_sd = questionaires.filter(question_13="Strongly disagree").count()
    q13_d = questionaires.filter(question_13="Disagree").count()
    q13_n = questionaires.filter(question_13="Neutral").count()
    q13_a = questionaires.filter(question_13="Agree").count()
    q13_sa = questionaires.filter(question_13="Strongly agree").count()




    q14_sd = questionaires.filter(question_14="Strongly disagree").count()
    q14_d = questionaires.filter(question_14="Disagree").count()
    q14_n = questionaires.filter(question_14="Neutral").count()
    q14_a = questionaires.filter(question_14="Agree").count()
    q14_sa = questionaires.filter(question_14="Strongly agree").count()



    q15_sd = questionaires.filter(question_15="Strongly disagree").count()
    q15_d = questionaires.filter(question_15="Disagree").count()
    q15_n = questionaires.filter(question_15="Neutral").count()
    q15_a = questionaires.filter(question_15="Agree").count()
    q15_sa = questionaires.filter(question_15="Strongly agree").count()



    q16_sd = questionaires.filter(question_16="Strongly disagree").count()
    q16_d = questionaires.filter(question_16="Disagree").count()
    q16_n = questionaires.filter(question_16="Neutral").count()
    q16_a = questionaires.filter(question_16="Agree").count()
    q16_sa = questionaires.filter(question_16="Strongly agree").count()



    q17_sd = questionaires.filter(question_17="Strongly disagree").count()
    q17_d = questionaires.filter(question_17="Disagree").count()
    q17_n = questionaires.filter(question_17="Neutral").count()
    q17_a = questionaires.filter(question_17="Agree").count()
    q17_sa = questionaires.filter(question_17="Strongly agree").count()

    q18_no = questionaires.filter(question_18="No").count()
    q18_yes = questionaires.filter(question_18="Yes").count()
    q18_not_sure = questionaires.filter(question_18="Not sure").count()


    q19_no = questionaires.filter(question_19="No").count()
    q19_yes = questionaires.filter(question_19="Yes").count()
    q19_not_sure = questionaires.filter(question_19="Not sure").count()




    q20_no = questionaires.filter(question_20="No").count()
    q20_yes = questionaires.filter(question_20="Yes").count()
    q20_not_sure = questionaires.filter(question_20="Not sure").count()


    
    q21_no = questionaires.filter(question_21="No").count()
    q21_yes = questionaires.filter(question_21="Yes").count()
    q21_not_sure = questionaires.filter(question_21="Not sure").count()



    q22_no = questionaires.filter(question_22="No").count()
    q22_yes = questionaires.filter(question_22="Yes").count()
    q22_not_sure = questionaires.filter(question_22="Not sure").count()


    
    q23_no = questionaires.filter(question_23="No").count()
    q23_yes = questionaires.filter(question_23="Yes").count()
    q23_not_sure = questionaires.filter(question_23="Not sure").count()
    

    
    q24_no = questionaires.filter(question_24="No").count()
    q24_yes = questionaires.filter(question_24="Yes").count()
    q24_not_sure = questionaires.filter(question_24="Not sure").count()


    
    q25_no = questionaires.filter(question_25="No").count()
    q25_yes = questionaires.filter(question_25="Yes").count()
    q25_not_sure = questionaires.filter(question_25="Not sure").count()



    q26_sign = questionaires.filter(question_26="Sign Language").count()
    q26_easy = questionaires.filter(question_26="Easy Read or Plain Language").count()
    q26_audio = questionaires.filter(question_26="Audio formats").count()
    q26_multiple = questionaires.filter(question_26="Multiple languages").count()
    q26_websites = questionaires.filter(question_26="Websites are accessible for screen reader users ").count()
    q26_captioning = questionaires.filter(question_26="Captioning services").count()
    q26_other = questionaires.filter(question_26="Other (please specify)").count()
    q26_no_info = questionaires.filter(question_26="No information has been provided in any format").count()




    q27_not  = questionaires.filter(question_27="Not at all").count()
    q27_little  = questionaires.filter(question_27="Little support was given").count()
    q27_adequate  = questionaires.filter(question_27="Adequate support was given").count()



    q28_true  = questionaires.filter(question_28=True).count()
    q28_false  = questionaires.filter(question_28=False).count()
  
    context = {
        'questionaires': questionaires,
        'number_of_participants' : number_of_participants,

        "qdd_age_1" : qdd_age_1 ,
        "qdd_age_2" : qdd_age_2 ,
        "qdd_age_3" : qdd_age_3 ,
        "qdd_age_4" : qdd_age_4 ,
        "qdd_age_5" : qdd_age_5 ,
        "qdd_age_6" : qdd_age_6 ,
        "qdd_age_7" : qdd_age_7 ,
        "qdd_age_8" : qdd_age_8 ,
        "qdd_age_9" : qdd_age_9 ,
        "qdd_age_10" : qdd_age_10 ,
        "qdd_age_11" : qdd_age_11 ,
        "qdd_age_12" : qdd_age_12 ,
        "qdd_age_13" : qdd_age_13 ,
        "qdd_age_14" : qdd_age_14 ,
        "qdd_age_15" : qdd_age_15 ,


        # Question 1 answers

        'q1_sd' : q1_sd,
        'q1_d' : q1_d,
        'q1_n' : q1_n,
        'q1_a' : q1_a,
        'q1_sa' : q1_sa,


        # Question 2 answers

        'q2_sd' : q2_sd,
        'q2_d' : q2_d,
        'q2_n' : q2_n,
        'q2_a' : q2_a,
        'q2_sa' : q2_sa,

        # Question 3 answers

        'q3_sd' : q3_sd,
        'q3_d' : q3_d,
        'q3_n' : q3_n,
        'q3_a' : q3_a,
        'q3_sa' : q3_sa,


        # Question 4 answers

        'q4_sd' : q4_sd,
        'q4_d' : q4_d,
        'q4_n' : q4_n,
        'q4_a' : q4_a,
        'q4_sa' : q4_sa,


        # Question 5 answers

        'q5_sd' : q5_sd,
        'q5_d' : q5_d,
        'q5_n' : q5_n,
        'q5_a' : q5_a,
        'q5_sa' : q5_sa,


        # Question 6 answers

        'q6_sd' : q6_sd,
        'q6_d' : q6_d,
        'q6_n' : q6_n,
        'q6_a' : q6_a,
        'q6_sa' : q6_sa,


        # Question 7 answers

        'q7_sd' : q7_sd,
        'q7_d' : q7_d,
        'q7_n' : q7_n,
        'q7_a' : q7_a,
        'q7_sa' : q7_sa,

        # Question 8 answers

        'q8_sd' : q8_sd,
        'q8_d' : q8_d,
        'q8_n' : q8_n,
        'q8_a' : q8_a,
        'q8_sa' : q8_sa,

        # Question 9 answers

        'q9_sd' : q9_sd,
        'q9_d' : q9_d,
        'q9_n' : q9_n,
        'q9_a' : q9_a,
        'q9_sa' : q9_sa,

        # Question 10 answers

        'q10_sd' : q10_sd,
        'q10_d' : q10_d,
        'q10_n' : q10_n,
        'q10_a' : q10_a,
        'q10_sa' : q10_sa,

        # Question 11 answers

        'q11_sd' : q11_sd,
        'q11_d' : q11_d,
        'q11_n' : q11_n,
        'q11_a' : q11_a,
        'q11_sa' : q11_sa,

        # Question 12 answers

        'q12_sd' : q12_sd,
        'q12_d' : q12_d,
        'q12_n' : q12_n,
        'q12_a' : q12_a,
        'q12_sa' : q12_sa,

        # Question 13 answers

        'q13_sd' : q13_sd,
        'q13_d' : q13_d,
        'q13_n' : q13_n,
        'q13_a' : q13_a,
        'q13_sa' : q13_sa,

        # Question 14 answers

        'q14_sd' : q14_sd,
        'q14_d' : q14_d,
        'q14_n' : q14_n,
        'q14_a' : q14_a,
        'q14_sa' : q14_sa,

        # Question 15 answers

        'q15_sd' : q15_sd,
        'q15_d' : q15_d,
        'q15_n' : q15_n,
        'q15_a' : q15_a,
        'q15_sa' : q15_sa,

        # Question 16 answers

        'q16_sd' : q16_sd,
        'q16_d' : q16_d,
        'q16_n' : q16_n,
        'q16_a' : q16_a,
        'q16_sa' : q16_sa,

        # Question 16 answers

        'q16_sd' : q16_sd,
        'q16_d' : q16_d,
        'q16_n' : q16_n,
        'q16_a' : q16_a,
        'q16_sa' : q16_sa,



        # Question 17 answers

        'q17_sd' : q17_sd,
        'q17_d' : q17_d,
        'q17_n' : q17_n,
        'q17_a' : q17_a,
        'q17_sa' : q17_sa,


        # Question 18 answers
        "q18_no" : q18_no,
        'q18_yes'  :  q18_yes,
        'q18_not_sure' : q18_not_sure,

        # Question 19 answers
        "q19_no" : q19_no,
        'q19_yes'  :  q19_yes,
        'q19_not_sure' : q19_not_sure,


        # Question 20 answers
        "q20_no" : q20_no,
        'q20_yes'  :  q20_yes,
        'q20_not_sure' : q20_not_sure,


        # Question 21 answers
        "q21_no" : q21_no,
        'q21_yes'  :  q21_yes,
        'q21_not_sure' : q21_not_sure,


        # Question 22 answers
        "q22_no" : q22_no,
        'q22_yes'  :  q22_yes,
        'q22_not_sure' : q22_not_sure,


        # Question 23 answers
        "q23_no" : q23_no,
        'q23_yes'  :  q23_yes,
        'q23_not_sure' : q23_not_sure,


        # Question 24 answers
        "q24_no" : q24_no,
        'q24_yes'  :  q24_yes,
        'q24_not_sure' : q24_not_sure,



        # Question 25 answers
        "q25_no" : q25_no,
        'q25_yes'  :  q25_yes,
        'q25_not_sure' : q25_not_sure,


        # Questions 26

        "q26_sign" : q26_sign ,
        "q26_easy" : q26_easy,
        "q26_audio" : q26_audio,
        "q26_multiple" : q26_multiple,
        "q26_websites" : q26_websites ,
        "q26_captioning" : q26_captioning,
        "q26_other" : q26_other,
        "q26_no_info" : q26_no_info,



         # Question 27 answers
        "q27_not" : q27_not,
        'q27_little'  :  q27_little,
        'q27_adequate' : q27_adequate,


        "q28_true"  : q28_true ,
        "q28_false" : q28_false,






    }
    return render(request,"survey/sh_report.html",context)



# @login_required
def dd_report(request):
    title = "Africa Disability Alliance"

    # orders = Order.objects.all()
    # customers = Customer.objects.all()

    # total_customers = customers.count()

    # total_orders = orders.count()
    # delivered = orders.filter(status='Delivered').count()
    # pending = orders.filter(status='Pending').count()

    questionaires = QuestionaireDData.objects.all()
    number_of_participants = questionaires.count()


    qdd_age_1 = questionaires.filter(age=group_A).count()
    qdd_age_2 = questionaires.filter(age=group_B).count()
    qdd_age_3 = questionaires.filter(age=group_C).count()
    qdd_age_4 = questionaires.filter(age=group_D).count()
    qdd_age_5 = questionaires.filter(age=group_E).count()
    qdd_age_6 = questionaires.filter(age=group_F).count()
    qdd_age_7 = questionaires.filter(age=group_G).count()
    qdd_age_8 = questionaires.filter(age=group_H).count()
    qdd_age_9 = questionaires.filter(age=group_I).count()
    qdd_age_10 = questionaires.filter(age=group_J).count()
    qdd_age_11 = questionaires.filter(age=group_K).count()
    qdd_age_12 = questionaires.filter(age=group_L).count()
    qdd_age_13 = questionaires.filter(age=group_M).count()
    qdd_age_14 = questionaires.filter(age=group_N).count()
    qdd_age_15 = questionaires.filter(age=group_O).count()



    q1_sd = questionaires.filter(question_1="Strongly disagree").count()
    q1_d = questionaires.filter(question_1="Disagree").count()
    q1_n = questionaires.filter(question_1="Neutral").count()
    q1_a = questionaires.filter(question_1="Agree").count()
    q1_sa = questionaires.filter(question_1="Strongly agree").count()


    q2_sd = questionaires.filter(question_2="Strongly disagree").count()
    q2_d = questionaires.filter(question_2="Disagree").count()
    q2_n = questionaires.filter(question_2="Neutral").count()
    q2_a = questionaires.filter(question_2="Agree").count()
    q2_sa = questionaires.filter(question_2="Strongly agree").count()


    q3_sd = questionaires.filter(question_3="Strongly disagree").count()
    q3_d = questionaires.filter(question_3="Disagree").count()
    q3_n = questionaires.filter(question_3="Neutral").count()
    q3_a = questionaires.filter(question_3="Agree").count()
    q3_sa = questionaires.filter(question_3="Strongly agree").count()



    q4_sd = questionaires.filter(question_4="Strongly disagree").count()
    q4_d = questionaires.filter(question_4="Disagree").count()
    q4_n = questionaires.filter(question_4="Neutral").count()
    q4_a = questionaires.filter(question_4="Agree").count()
    q4_sa = questionaires.filter(question_4="Strongly agree").count()



    q5_sd = questionaires.filter(question_5="Strongly disagree").count()
    q5_d = questionaires.filter(question_5="Disagree").count()
    q5_n = questionaires.filter(question_5="Neutral").count()
    q5_a = questionaires.filter(question_5="Agree").count()
    q5_sa = questionaires.filter(question_5="Strongly agree").count()



    
    q6_sd = questionaires.filter(question_6="Strongly disagree").count()
    q6_d = questionaires.filter(question_6="Disagree").count()
    q6_n = questionaires.filter(question_6="Neutral").count()
    q6_a = questionaires.filter(question_6="Agree").count()
    q6_sa = questionaires.filter(question_6="Strongly agree").count()




    q7_sd = questionaires.filter(question_7="Strongly disagree").count()
    q7_d = questionaires.filter(question_7="Disagree").count()
    q7_n = questionaires.filter(question_7="Neutral").count()
    q7_a = questionaires.filter(question_7="Agree").count()
    q7_sa = questionaires.filter(question_7="Strongly agree").count()


    q8_sd = questionaires.filter(question_8="Strongly disagree").count()
    q8_d = questionaires.filter(question_8="Disagree").count()
    q8_n = questionaires.filter(question_8="Neutral").count()
    q8_a = questionaires.filter(question_8="Agree").count()
    q8_sa = questionaires.filter(question_8="Strongly agree").count()



    q9_sd = questionaires.filter(question_9="Strongly disagree").count()
    q9_d = questionaires.filter(question_9="Disagree").count()
    q9_n = questionaires.filter(question_9="Neutral").count()
    q9_a = questionaires.filter(question_9="Agree").count()
    q9_sa = questionaires.filter(question_9="Strongly agree").count()



   

    q10_no = questionaires.filter(question_10="No").count()
    q10_yes = questionaires.filter(question_10="Yes").count()
    q10_not_sure = questionaires.filter(question_10="Not sure").count()


    q11_no = questionaires.filter(question_11="No").count()
    q11_yes = questionaires.filter(question_11="Yes").count()
    q11_not_sure = questionaires.filter(question_11="Not sure").count()




    q12_no = questionaires.filter(question_12="No").count()
    q12_yes = questionaires.filter(question_12="Yes").count()
    q12_not_sure = questionaires.filter(question_12="Not sure").count()

    q13_no = questionaires.filter(question_13="No").count()
    q13_yes = questionaires.filter(question_13="Yes").count()
    q13_not_sure = questionaires.filter(question_13="Not sure").count()

    q14_no = questionaires.filter(question_14="No").count()
    q14_yes = questionaires.filter(question_14="Yes").count()
    q14_not_sure = questionaires.filter(question_14="Not sure").count()


    q15_no = questionaires.filter(question_15="No").count()
    q15_yes = questionaires.filter(question_15="Yes").count()
    q15_not_sure = questionaires.filter(question_15="Not sure").count()


    q16_no = questionaires.filter(question_16="No").count()
    q16_yes = questionaires.filter(question_16="Yes").count()
    q16_not_sure = questionaires.filter(question_16="Not sure").count()

    q17_no = questionaires.filter(question_17="No").count()
    q17_yes = questionaires.filter(question_17="Yes").count()
    q17_not_sure = questionaires.filter(question_17="Not sure").count()


    q18_no = questionaires.filter(question_18="No").count()
    q18_yes = questionaires.filter(question_18="Yes").count()
    q18_not_sure = questionaires.filter(question_18="Not sure").count()

    q19_no = questionaires.filter(question_19="No").count()
    q19_yes = questionaires.filter(question_19="Yes").count()
    q19_not_sure = questionaires.filter(question_19="Not sure").count()


    # q19_not_sure = questionaires.filter(question_19="Not sure").count()
    # q19_no = questionaires.filter(question_21="No").count()
    

    q20_sign = questionaires.filter(question_20="Sign Language").count()
    q20_easy = questionaires.filter(question_20="Easy Read or Plain Language").count()
    q20_audio = questionaires.filter(question_20="Audio formats").count()
    q20_multiple = questionaires.filter(question_20="Multiple languages").count()
    q20_websites = questionaires.filter(question_20="Websites are accessible for screen reader users ").count()
    q20_captioning = questionaires.filter(question_20="Captioning services").count()
    q20_other = questionaires.filter(question_20="Other (please specify)").count()
    q20_no_info = questionaires.filter(question_20="No information has been provided in any format").count()




    q21_not  = questionaires.filter(question_21="Not at all").count()
    q21_little  = questionaires.filter(question_21="Little support was given").count()
    q21_adequate  = questionaires.filter(question_21="Adequate support was given").count()


    q22_not  = questionaires.filter(question_22="Not at all").count()
    q22_sometimes  = questionaires.filter(question_22="Sometimes").count()
    q22_all  = questionaires.filter(question_22="All the time").count()



    q23_true  = questionaires.filter(question_23=True).count()
    q23_false  = questionaires.filter(question_23=False).count()
  
    context = {
        'questionaires': questionaires,
        'number_of_participants' : number_of_participants,



        "qdd_age_1" : qdd_age_1 ,
        "qdd_age_2" : qdd_age_2 ,
        "qdd_age_3" : qdd_age_3 ,
        "qdd_age_4" : qdd_age_4 ,
        "qdd_age_5" : qdd_age_5 ,
        "qdd_age_6" : qdd_age_6 ,
        "qdd_age_7" : qdd_age_7 ,
        "qdd_age_8" : qdd_age_8 ,
        "qdd_age_9" : qdd_age_9 ,
        "qdd_age_10" : qdd_age_10 ,
        "qdd_age_11" : qdd_age_11 ,
        "qdd_age_12" : qdd_age_12 ,
        "qdd_age_13" : qdd_age_13 ,
        "qdd_age_14" : qdd_age_14 ,
        "qdd_age_15" : qdd_age_15 ,

        

        # Question 1 answers

        'q1_sd' : q1_sd,
        'q1_d' : q1_d,
        'q1_n' : q1_n,
        'q1_a' : q1_a,
        'q1_sa' : q1_sa,


        # Question 2 answers

        'q2_sd' : q2_sd,
        'q2_d' : q2_d,
        'q2_n' : q2_n,
        'q2_a' : q2_a,
        'q2_sa' : q2_sa,

        # Question 3 answers

        'q3_sd' : q3_sd,
        'q3_d' : q3_d,
        'q3_n' : q3_n,
        'q3_a' : q3_a,
        'q3_sa' : q3_sa,


        # Question 4 answers

        'q4_sd' : q4_sd,
        'q4_d' : q4_d,
        'q4_n' : q4_n,
        'q4_a' : q4_a,
        'q4_sa' : q4_sa,


        # Question 5 answers

        'q5_sd' : q5_sd,
        'q5_d' : q5_d,
        'q5_n' : q5_n,
        'q5_a' : q5_a,
        'q5_sa' : q5_sa,


        # Question 6 answers

        'q6_sd' : q6_sd,
        'q6_d' : q6_d,
        'q6_n' : q6_n,
        'q6_a' : q6_a,
        'q6_sa' : q6_sa,


        # Question 7 answers

        'q7_sd' : q7_sd,
        'q7_d' : q7_d,
        'q7_n' : q7_n,
        'q7_a' : q7_a,
        'q7_sa' : q7_sa,

        # Question 8 answers

        'q8_sd' : q8_sd,
        'q8_d' : q8_d,
        'q8_n' : q8_n,
        'q8_a' : q8_a,
        'q8_sa' : q8_sa,

        # Question 9 answers

        'q9_sd' : q9_sd,
        'q9_d' : q9_d,
        'q9_n' : q9_n,
        'q9_a' : q9_a,
        'q9_sa' : q9_sa,


        # Question 10 answers
        "q10_no" : q10_no,
        'q10_yes'  :  q10_yes,
        'q10_not_sure' : q10_not_sure,

        # Question 11 answers
        "q11_no" : q11_no,
        'q11_yes'  :  q11_yes,
        'q11_not_sure' : q11_not_sure,


        # Question 12 answers
        "q12_no" : q12_no,
        'q12_yes'  :  q12_yes,
        'q12_not_sure' : q12_not_sure,


        # Question 13 answers
        "q13_no" : q13_no,
        'q13_yes'  :  q13_yes,
        'q13_not_sure' : q13_not_sure,


        # Question 14 answers
        "q14_no" : q14_no,
        'q14_yes'  :  q14_yes,
        'q14_not_sure' : q14_not_sure,


        # Question 15 answers
        "q15_no" : q15_no,
        'q15_yes'  :  q15_yes,
        'q15_not_sure' : q15_not_sure,


        # Question 16 answers
        "q16_no" : q16_no,
        'q16_yes'  :  q16_yes,
        'q16_not_sure' : q16_not_sure,



        # Question 17 answers
        "q17_no" : q17_no,
        'q17_yes'  :  q17_yes,
        'q17_not_sure' : q17_not_sure,


         # Question 18 answers
        "q18_no" : q18_no,
        'q18_yes'  :  q18_yes,
        'q18_not_sure' : q18_not_sure,


         # Question 19 answers
        "q19_no" : q19_no,
        'q19_yes'  :  q19_yes,
        'q19_not_sure' : q19_not_sure,




        # Questions 20

        "q20_sign" : q20_sign ,
        "q20_easy" : q20_easy,
        "q20_audio" : q20_audio,
        "q20_multiple" : q20_multiple,
        "q20_websites" : q20_websites ,
        "q20_captioning" : q20_captioning,
        "q20_other" : q20_other,
        "q20_no_info" : q20_no_info,



         # Question 21 answers
        "q21_not" : q21_not,
        'q21_little'  :  q21_little,
        'q21_adequate' : q21_adequate,


         # Question 22 answers
        "q22_not" : q22_not,
        'q22_sometimes'  :  q22_sometimes,
        'q22_all' : q22_all,


        "q23_true"  : q23_true ,
        "q23_false" : q23_false,






    }
    return render(request,"survey/dd_report.html",context)





# def render_pdf_view(request):
#     template_path = 'survey/dd_report.html' #'user_printer.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="report-stakeholders.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)# link_callback=link_callback

#     # if error then show some funy view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response
