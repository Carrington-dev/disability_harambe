# from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account, Profile

# # Register your models here.
# from . models import UserProfile

# # Register your models here.
# @admin.register(UserProfile)
# class UserAdmin(admin.ModelAdmin):
#     # pass
#     list_per_page = 2
#     # date_hierarchy = 'phone'
#     list_display = ("id","email", "username","first_name","last_name", "phone", "is_active","is_staff","is_superuser")

#     #This hides other fields to the admin such that they become uneditable
#     fields = ["email",'username', 'first_name',"last_name", "phone","password", "is_active","is_staff","is_superuser"]




class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff','is_student','is_teacher')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

    


admin.site.register(Account, AccountAdmin)


@admin.register(Profile)
class ProfileControler(admin.ModelAdmin):
	list_per_page = 15
	list_display = ('id','user','image')
