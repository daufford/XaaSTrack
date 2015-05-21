from django.contrib import admin

#@todo: Register your models here.
from .models import *

admin.site.register(UserProfile)
admin.site.register(UserPlan)
admin.site.register(PlanProvider)
