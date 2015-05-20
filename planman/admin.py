from django.contrib import admin

#@todo: Register your models here.
from planman.models import UserProfile, UserPlan

admin.site.register(UserProfile)
admin.site.register(UserPlan)
