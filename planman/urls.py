from django.conf.urls import url

from . import views

# check out https://docs.djangoproject.com/en/1.8/ref/urlresolvers/
# #module-django.core.urlresolvers for more info
from .views import *

urlpatterns = [

    #UserPlan
    url(r'^$', UserPlanList.as_view(), name='userplan-list'),
    url(r'^plan/$', UserPlanList.as_view(), name='userplan-list'),
    url(r'^plan/new/$', UserPlanCreate.as_view(), name='userplan-create'),
    url(r'^plan/(?P<pk>\d+)/$', UserPlanDetail.as_view(), name='userplan-detail'),
    url(r'^plan/(?P<pk>\d+)/update$', UserPlanUpdate.as_view(), name='userplan-update'),
    url(r'^plan/(?P<pk>\d+)/delete$', UserPlanDelete.as_view(), name='userplan-delete'),

    #Provider
    url(r'^provider/$', PlanProviderList.as_view(), name='provider-list'),
    url(r'^provider/new$', PlanProviderCreate.as_view(), name='provider-create'),
    url(r'^provider/(?P<pk>\d+)/$', PlanProviderDetail.as_view(), name='provider-detail'),
    url(r'^provider/(?P<pk>\d+)/update', PlanProviderUpdate.as_view(), name='provider-update'),
    url(r'^provider/(?P<pk>\d+)/delete', PlanProviderDelete.as_view(), name='provider-delete'),

    ##events/payments
    url(r'^plan/(?P<plan_id>\d+)/newevent/$', views.createEvent, name='event-create'),
    url(r'^event/(?P<pk>\d+)/update', PlanEventUpdate.as_view(), name='event-update'),
    url(r'^event/(?P<pk>\d+)/delete', PlanEventDelete.as_view(), name='event-delete'),



]
