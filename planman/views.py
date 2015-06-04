from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView, FormView
from .models import *
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
from planman.forms import UserPlanForm,SignUpForm, UserProfileForm
from django.contrib.auth.forms import UserCreationForm

##Registration
def register(request):  #http://www.tangowithdjango.com/book17/chapters/login.html#creating-a-user-registration-view-and-template
    registered = False

    #process data if its a post method
    if request.method == 'POST':
        user_form = SignUpForm(data=request.POST)#UserCreationForm(request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            #save user
            user = user_form.save()
            #save user profile
            profile = profile_form.save(commit=False)#delay committ until we have set all attributes
            profile.user=user
            profile.save()
            registered=True

        else:
            print(user_form.errors)#print to terminal
            print(profile_form.errors)

    else:    #new form
        user_form = SignUpForm()
        profile_form=UserProfileForm()

    return render (request,'registration/register.html',
                   {'user_form':user_form,'profile_form':profile_form,'registered':registered})

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls,**initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

###BASIC CRUD
class PlanProviderList(LoginRequiredMixin, ListView):
    model = PlanProvider

class PlanProviderCreate(LoginRequiredMixin, CreateView):
    model = PlanProvider
    fields = ['name']

class PlanProviderUpdate(LoginRequiredMixin, UpdateView):
    model = PlanProvider
    fields = ['name']

class PlanProviderDetail(LoginRequiredMixin, DetailView):
    model = PlanProvider

class PlanProviderDelete(LoginRequiredMixin, DeleteView):
    model = PlanProvider
    success_url = reverse_lazy('userplan-list')

class UserPlanList(LoginRequiredMixin, ListView):
    model = UserPlan

class UserPlanDetail(LoginRequiredMixin, DetailView):
    model = UserPlan

class UserPlanUpdate(LoginRequiredMixin, UpdateView):
    model = UserPlan
    fields = ['user_description']

# class UserPlanCreate(LoginRequiredMixin, CreateView):
#     model = UserPlan
#     fields = ['user_description','userprofile','planprovider','start_date',
#               'next_renewal_date','expiration_date'
#               ]


##This is an example for how to use a generic view with a model form.
class UserPlanCreate(LoginRequiredMixin, CreateView):
    model = UserPlan
    form_class = UserPlanForm
    def form_valid(self,form):  #store user during save
        form.instance.user = self.request.user
        return super(UserPlanCreate,self).form_valid(form)

class UserPlanDelete(LoginRequiredMixin, DeleteView):
    model = UserPlan
    success_url = reverse_lazy('userplan-list')
