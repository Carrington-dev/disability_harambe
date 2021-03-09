from django import forms
from django.forms import ModelForm
from . models import *
from . import variables
from . variables import *
from django import forms
from django.forms import ModelForm


class DDForm(ModelForm):
    # gender = forms.SelectMultiple( choices=GENDER, help_text="")
    # age = forms.RadioSelect(choices=AGE_OF_INTERVIEWEE)

    class Meta:
        model = QuestionaireDData
        fields = ['full_name','gender','country','age','question_1',"question_2", "question_3","question_4",'question_5',"question_6", "question_7","question_8",'question_9',"question_10", "question_11","question_12",'question_13',"question_15", "question_15","question_16",'question_17',"question_18", "question_19","question_20",'question_21',"question_22", "question_23",]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}),
            'gender': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
             'age': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
              'question_1': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
               'question_2': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                'question_3': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                 'question_4': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                  'question_5': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                   'question_6': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                    'question_7': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                     'question_8': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                      'question_9': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                       'question_10': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                        'question_11': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                         'question_12': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_13': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_14': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_15': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_16': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_17': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_18': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_19': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_20': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_21': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_22': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_23': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),


                          }


        labels = {
            'full_name': "Unique identifier for the student",
            'full_name': "Unique identifier for the student",
            'question_1': "1. Access to essentials (food, shelter, medicines and other essentials) by people with disabilities has been hampered a lot during the pandemic",
            'question_2': "2. There has been equitable accessibility to ventilators by people with disabilities during COVID19 related sickness.",
            'question_3': "3. The price of medicines and other treatments has soared, and treatment for chronic and longterm health conditions has become difficult for people with disabilities during the period of the COVID-19 pandemic",
            'question_4': "4. Gender-based violence against women and girls with disabilities including rape, sexual assault, and harassment at the hands of enforcement authorities or family members rose during the pandemic periods?",
            'question_5': "5. People with disabilities in rural and remote settings have suffered both through the lack of availability of essential supplies and services, as well as the inability to access information during the time of the COVID-19 pandemic",
            'question_6': "6. COVID response measures have seen the exclusion of already marginalised population groups that include women, older persons and children with disabilities.",
            'question_7': "7. The behaviour of others (for example failure to socially distance) has jeopardised the lives of people with disabilities during the COVID-19 pandemic?",
            'question_8': "8. Organizations have helped in establishing conducive “work from home” environments for people with disabilities",
            'question_9': "9. People with disabilities have faced restriction or denial of basic and emergency healthcare, including for those who have contracted COVID-19",
            'question_10': "10. In your opinion, have government officials consulted with or involved persons with disabilities in the formulation of COVID19 response mechanisms in your country?",
            'question_11': "11. Have your rights to health and life been violated through government enforced lockdowns and other COVID-19 responses?",
            'question_12': "12. Do you feel you have been abused or you know a person with disability who has been ill-treated or exploited by persons (and even by systems) involved in enforcing the COVID-19 response measures?",
            'question_13': "13. Do you think the enforced periods of isolation had a severe impact on the mental health of people with disabilities in your country?",
            'question_14': "14. Were you provided with adequate information relating to the pandemic and how to keep yourself safe",
            'question_15': "15. Do you think adequate support was offered to families with disabled persons by government during the outbreak of the pandemic",
            'question_16': "16. During the outbreak of the pandemic, innovative online teaching environments were setup for children and young people. Did the measures in your area cater for children and young people with disabilities?",
            'question_17': "17. Did children and young people with disabilities have access to these online learning platforms?",
            'question_18': "18. Institutional admissions have gone up during the pandemic. ",
            'question_19': "19. There is need for disability-awareness training for police and law enforcement authorities, and accountability for disproportionate enforcement of public health-related restrictions. ",
            'question_20': "20. Information to people with disabilities can be provided in various ways. Which of the following ways have been used to disseminate information to people with disabilities in your country? (You may select more than 1)",
            'question_21': "21. Do you think adequate support was offered to families with disabled persons by government during the outbreak of the pandemic",
            'question_22': "22. Do you at times find yourself in settings where you cannot socially distance for example group quarantine shelters?",
            'question_23': "23. . People with disabilities have telephone numbers to telehealth services and emergency services that are critical during the time of the pandemic and beyond. Is this in your opinion true or false?",
        }

class SHForm(ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER)
    stakeholder_class = forms.ChoiceField(widget=forms.RadioSelect, choices=Stakeholder_classification)
    # if
    # question_26 = forms.MultipleChoiceField(choices=question_C),

    class Meta:
        model = QuestionaireStakeHolders
        fields = ['full_name','gender','country','age','stakeholder_class','question_1',"question_2", "question_3",
        "question_4",'question_5',"question_6", "question_7","question_8",'question_9',
        "question_10", "question_11","question_12",'question_13',"question_15", "question_15","question_16",
        'question_17',"question_18", "question_19","question_20",'question_21',"question_22",
        "question_23",'question_24','question_25','question_26', 'question_27','question_21']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}),
            'gender': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
             'age': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
              'question_1': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
               'question_2': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                'question_3': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                 'question_4': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                  'question_5': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                   'question_6': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                    'question_7': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                     'question_8': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                      'question_9': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                       'question_10': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                        'question_11': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                         'question_12': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_13': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_14': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_15': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_16': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_17': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_18': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_19': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_20': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_21': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_22': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_23': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_24': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_25': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_26': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_27': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),
                          'question_28': forms.RadioSelect(attrs={'class': 'form-select form-select-lg mb-3'}),

                          }


        labels = {
            'full_name': "Full Name",
            'gender': "Choose your gender!",
            "stakeholder_class": "Stakeholder classification",
            'question_1': "1. Government officials consulted with or involved persons with disabilities in the formulation of COVID19 response mechanisms in my country.",
            'question_2': "2. The government and care organizations have made sure that persons with disabilities have Access to essentials (food, shelter, medicines, physiotherapy and other essentials) during the pandemic",
            'question_3': "3. The government together with healthcare organizations have made sure that there is equitableaccessibility to ventilators by persons with disabilities during COVID19 related sickness.",
            'question_4': "4. The government created a database of vulnerable people who would require emergency help during the COVID19 pandemic",
            'question_5': "5. The government has strategically prioritised access to services for vulnerable people that include persons with disabilities.",
            'question_6': "6. The government has strategically prioritised access to services for vulnerable people that include persons with disabilities.",
            'question_7': "7. Vulnerable groups and persons with disabilities have received data deals and cheap internet access as a basic service during the pandemic.",
            'question_8': "8. Home carers have been trained and registered as essential services",
            'question_9': "9. There have been follow ups on persons with disabilities and other vulnerable groups to check on their well-being during the outbreak of the pandemic",
            'question_10': "10. Networks of persons with disabilities have been created to constantly offer support.",
            'question_11': "11. Transport to deliver basic needs to persons with disabilities has been arranged each time there is need. ",
            'question_12': "12. Responsible persons have been tasked with monitoring potential abusive situations, both abuser and victim during the COVID19 outbreak",
            'question_13': "13. Counselling services have been provided in abusive situations for persons with disabilities during the pandemic",
            'question_14': "14.  Support has been offered to persons with disabilities who are undergoing isolation or quarantine",
            'question_15': "15. The government and care organizations have made sure that persons with disabilities in rural and remote settings have access to essential supplies and services, as well as access information during the time of the COVID-19 pandemic",
            'question_16': "16. COVID-19 response measures have catered for already marginalised population groups thatinclude older persons with disabilities and children with disabilities.",
            'question_17': "17. The government and responsible organizations have encouraged and enforced the establishing of conducive “work from home” environments for persons with disabilities",
            'question_18': "18. Do you think there are certain instances where the rights to health and life of persons with disabilities have been violated through government enforced lockdowns and other COVID-19 responses?",
            'question_19': "19. Do you think the enforced periods of isolation had a severe impact on the mental health of persons with disability in your country?",
            'question_20': "20. The government and care organizations provided adequate information relating to the pandemic and how to keep safe to personswith disabilities",
            'question_21': "21. Do you think adequate support was offered to families with persons with disabilities by government during the outbreak of the pandemic",
            'question_22': "22. During the outbreak of the pandemic, innovative online teaching environments were setup for children and young people. In your opinion did the measures carried out in your area cater for children and young people with disabilities?",
            'question_23': "23. Did children and young people with disability have access to these online learning platforms?",
            'question_24': "24. The government and responsible organizations had control on the challenge of Institutional admissions during the pandemic. ",
            'question_25': "25. The government made sure that disability-awareness training for police and law enforcement authorities was offered, and accountability for disproportionate enforcement of public health-related restrictions was in place. ",
            'question_26': "26. Information to persons with disabilities can be conveyed in various ways. Which of the following ways have been used to disseminate information by authorities to persons with disability in your country? (You may select more than 1)",
            'question_27': "27. Do you think adequate support (by government and care organizations) was offered to families with disabled persons by government during the outbreak of the pandemic",
            'question_28': "28. Persons with disabilities have telephone numbers to telehealth services and emergency services that are critical during the time of the pandemic and beyond. Is this in your opinion true or false?",

        }

        # labels = {
        #     'contact_name': 'What is your name',
        # }
