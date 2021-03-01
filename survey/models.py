from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django_countries.fields import CountryField
from . variables import *
# Create your models here.


class QuestionaireDData(models.Model):
	name_of_questionaire = "Descriptive Data"
	full_name = models.CharField(max_length=50,verbose_name="full name")
	gender = models.CharField(max_length=10, choices=GENDER,default=1)
	country = CountryField(default=1)
	date_sent	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	age = models.CharField(max_length=10, choices=AGE_OF_INTERVIEWEE, default=1)


	question_1 = models.CharField(max_length=400,verbose_name="question 1", choices=question_A, default=1)
	question_2 = models.CharField(max_length=400,verbose_name="question 2", choices=question_A, default=1)
	question_3 = models.CharField(max_length=400,verbose_name="question 3", choices=question_A, default=1)
	question_4 = models.CharField(max_length=400,verbose_name="question 4", choices=question_A, default=1)
	question_5 = models.CharField(max_length=400,verbose_name="question 5", choices=question_A, default=1)
	question_6 = models.CharField(max_length=400,verbose_name="question 6", choices=question_A, default=1)
	question_7 = models.CharField(max_length=400,verbose_name="question 7", choices=question_A, default=1)
	question_8 = models.CharField(max_length=400,verbose_name="question 8", choices=question_A, default=1)
	question_9 = models.CharField(max_length=400,verbose_name="question 9", choices=question_A, default=1)


	question_10 = models.CharField(max_length=400,verbose_name="question 10", choices=question_B, default=1)
	question_11 = models.CharField(max_length=400,verbose_name="question 11", choices=question_B, default=1)
	question_12 = models.CharField(max_length=400,verbose_name="question 12", choices=question_B, default=1)
	question_13 = models.CharField(max_length=400,verbose_name="question 13", choices=question_B, default=1)
	question_14 = models.CharField(max_length=400,verbose_name="question 14", choices=question_B, default=1)
	question_15 = models.CharField(max_length=400,verbose_name="question 15", choices=question_B, default=1)
	question_16 = models.CharField(max_length=400,verbose_name="question 16", choices=question_B, default=1)
	question_17 = models.CharField(max_length=400,verbose_name="question 17", choices=question_B, default=1)
	question_18 = models.CharField(max_length=400,verbose_name="question 18", choices=question_B, default=1)
	question_19 = models.CharField(max_length=400,verbose_name="question 19", choices=question_B, default=1)


	question_20 = models.CharField(max_length=400,verbose_name="question 20")#choice= question_C
	question_21 = models.CharField(max_length=400,verbose_name="question 21", choices=question_D, default=1)
	question_22 = models.CharField(max_length=400,verbose_name="question 22", choices=question_E, default=1)
	question_23 = models.CharField(max_length=400,verbose_name="question 23", choices=question_F, default=1)




	def __str__(self):
		return self.name_of_questionaire

	def __unicode__(self):
		return self.name_of_questionaire

	class Meta:
		verbose_name = "Descriptive Data Questionaire"
		verbose_name_plural = "Descriptive Data Questionaires"






class QuestionaireStakeHolders(models.Model):
	name_of_questionaire = "StakeHolders"
	date_sent	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	full_name = models.CharField(max_length=50,verbose_name="full name")
	gender = models.CharField(max_length=10, choices=GENDER,default=1)
	country = CountryField(default=1)
	age = models.CharField(max_length=10, choices=AGE_OF_INTERVIEWEE,default=1)
	stakeholder_class = models.CharField(max_length=300, choices=Stakeholder_classification)


	question_1 = models.CharField(max_length=400,verbose_name="question 1", choices=question_A, default=1)
	question_2 = models.CharField(max_length=400,verbose_name="question 2", choices=question_A, default=1)
	question_3 = models.CharField(max_length=400,verbose_name="question 3", choices=question_A, default=1)
	question_4 = models.CharField(max_length=400,verbose_name="question 4", choices=question_A, default=1)
	question_5 = models.CharField(max_length=400,verbose_name="question 5", choices=question_A, default=1)
	question_6 = models.CharField(max_length=400,verbose_name="question 6", choices=question_A, default=1)
	question_7 = models.CharField(max_length=400,verbose_name="question 7", choices=question_A, default=1)
	question_8 = models.CharField(max_length=400,verbose_name="question 8", choices=question_A, default=1)
	question_9 = models.CharField(max_length=400,verbose_name="question 9", choices=question_A, default=1)
	question_10 = models.CharField(max_length=400,verbose_name="question 10", choices=question_A, default=1)
	question_11 = models.CharField(max_length=400,verbose_name="question 11", choices=question_A, default=1)
	question_12 = models.CharField(max_length=400,verbose_name="question 12", choices=question_A, default=1)
	question_13 = models.CharField(max_length=400,verbose_name="question 13", choices=question_A, default=1)
	question_14 = models.CharField(max_length=400,verbose_name="question 14", choices=question_A, default=1)
	question_15 = models.CharField(max_length=400,verbose_name="question 15", choices=question_A, default=1)
	question_16 = models.CharField(max_length=400,verbose_name="question 16", choices=question_A, default=1)
	question_17 = models.CharField(max_length=400,verbose_name="question 17", choices=question_A, default=1)


	question_18 = models.CharField(max_length=400,verbose_name="question 18", choices=question_B, default=1)
	question_19 = models.CharField(max_length=400,verbose_name="question 19", choices=question_B, default=1)
	question_20 = models.CharField(max_length=400,verbose_name="question 20", choices=question_B, default=1)
	question_21 = models.CharField(max_length=400,verbose_name="question 21", choices=question_B, default=1)
	question_22 = models.CharField(max_length=400,verbose_name="question 22", choices=question_B, default=1)
	question_23 = models.CharField(max_length=400,verbose_name="question 23", choices=question_B, default=1)
	question_24 = models.CharField(max_length=400,verbose_name="question 24", choices=question_B, default=1)
	question_25 = models.CharField(max_length=400,verbose_name="question 25", choices=question_B, default=1)




	question_26 = models.CharField(max_length=400,verbose_name="question 26") #choices=question_C,
	question_27 = models.CharField(max_length=400,verbose_name="question 27", choices=question_D, default=1)
	question_28 = models.CharField(max_length=400,verbose_name="question 28", choices=question_F, default=1)
	# question_29 = models.CharField(max_length=400,verbose_name="question 23", choices=question_F, default=1)


	# def report_pdf(obj):
	# 	url = reverse('report:admin_order_report_pdf', args=[obj.id])
	# 	return mark_safe(f'<a href="{url}">PDF</a>')
	# 	report_pdf.short_description = 'Report Of Questionaire StakeHolders'

	def __str__(self):
		return self.name_of_questionaire

	def __unicode__(self):
		return self.name_of_questionaire

	class Meta:
		verbose_name = "StakeHolders Questionaire"
		verbose_name_plural = "StakeHolders Questionaires"
