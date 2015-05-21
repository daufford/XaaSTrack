from django.conf.urls import url

from . import views

# check out https://docs.djangoproject.com/en/1.8/ref/urlresolvers/
# #module-django.core.urlresolvers for more info
from .views import *

urlpatterns = [

    url(r'^$', UserPlanList.as_view(), name='userplan-list'),
    url(r'^add/$', UserPlanCreate.as_view(), name='userplan-create'),
    url(r'^(?P<pk>\d+)/$', UserPlanDetail.as_view(), name='userplan-detail'),
    url(r'^(?P<pk>\d+)/update/$', UserPlanUpdate.as_view(), name='userplan-update'),
    url(r'^(?P<pk>\d+)/delete/$', UserPlanDelete.as_view(), name='userplan-delete'),
]
