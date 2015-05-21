from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import UserPlan
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class UserPlanList(ListView):
    model = UserPlan

class UserPlanDetail(DetailView):
    model = UserPlan


class UserPlanUpdate(UpdateView):
    model = UserPlan
    fields = ['user_description']

class UserPlanCreate(CreateView):
    model = UserPlan
    fields = ['user_description','userprofile','provider','start_date',
              'next_renewal_date','expiration_date'
              ]

class UserPlanDelete(DeleteView):
    model = UserPlan
    success_url = reverse_lazy('userplan-list')
