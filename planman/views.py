from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView, FormView
from .models import *
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from planman.forms import UserPlanForm,SignUpForm, UserProfileForm, PlanEventForm

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
    def get_context_data(self, **kwargs):  ##adding additional context data
        context = super(UserPlanList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['total_month'] = sum(object.get_amount_last_month() for object in context['object_list'])
        context['total_ytd']= sum(object.get_year_to_date() for object in context['object_list'])
        return context

class UserPlanUpdate(LoginRequiredMixin, UpdateView):
    model = UserPlan
    form_class = UserPlanForm

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

class PlanEventUpdate(LoginRequiredMixin, UpdateView):
    model = PlanEvent
    form_class = PlanEventForm
    success_url = reverse_lazy('userplan-detail',kwargs={'pk':1})
    #@todo:  fix pk retrival

class PlanEventDelete(LoginRequiredMixin, DeleteView):
    model = PlanEvent
    success_url = reverse_lazy('userplan-detail',kwargs={'pk':1})
    #@todo: make ajax

class UserPlanDetail(LoginRequiredMixin, DetailView):
    model = UserPlan
    def get_context_data(self, **kwargs):  ##adding additional context data
        context = super(UserPlanDetail, self).get_context_data(**kwargs)
        context['stop_form'] = PlanEventForm(initial={'event_date': timezone.now()})
        return context

@login_required
def createEvent(request,plan_id):
    registered = False

    #process data if its a post method
    if request.method == 'POST':
        event_form = PlanEventForm(data=request.POST)#UserCreationForm(request.POST)
        if 'start' in request.POST:
            event_form.event_type = 'start'
        if 'stop' in request.POST:
            event_form.event_type = 'stop'
        if 'pay' in request.POST:
            event_form.event_type = 'pay'
        if 'renew' in request.POST:
            event_form.event_type = 'renew'

        if event_form.is_valid():
            print("creating event")

            event = event_form.save(commit=False)
            event.event_type = event_form.event_type
            event.userplan = get_object_or_404(UserPlan, pk=plan_id)
            event.save()
            registered=True
            messages.success(request,"{0} event added".format(event.event_type.title()))
            return HttpResponseRedirect(reverse('userplan-detail',kwargs={'pk':plan_id}))

        else:
            print('error')
            for error in event_form.non_field_errors():
                messages.error(request,error)
            for error in event_form.errors:
                if error=='__all__': continue
                messages.error(request,event_form.errors[error])

    else:    #new form
        event_form = PlanEventForm()
        print("new form")
    return HttpResponseRedirect(reverse('userplan-detail',kwargs={'pk':plan_id}))