from django.conf.urls import url

from . import views
# check out https://docs.djangoproject.com/en/1.8/ref/urlresolvers/
# #module-django.core.urlresolvers for more info
from .views import *

urlpatterns = [

    #Creating Plaid Accounts
    url(r'^$', PlaidTokenList.as_view(), name='plaid-index'),
    url(r'^link$',views.plaidlink, name='plaid-link'),
    url(r'^link/submit$',views.plaidlink_submit, name='plaid-link-submit'),
    url(r'^token/list$',PlaidTokenList.as_view(),name='plaid-token-list'),
    url(r'^token/(?P<pk>\d+)/retrieve$',views.transactions_retrieve,name='plaid-token-retrieve'),
    #url(r'^token/(?P<pk>\d+)/transactions/$',PlaidTransactionList.as_view(),name='plaid-token-transactions'),

    #converting transactions
    url(r'^flag/$',PlaidTransactionList_Flag.as_view(),name='plaid-flag'),
    url(r'^flag/showall$',PlaidTransactionList.as_view(),name='plaid-transaction-list'),

    url(r'^flag/convert/(?P<pk>\w+)/$',views.transaction_convert,name='plaid-flag-convert'),
    #url(r'^flag/ignore/(?P<pk>\w+)/$',views.transaction_ignore,name='plaid-flag-ignore'),
    # url(r'^convert/$',views.transactions_convert,name='plaid-convert'),
    # url(r'^/flag/submit$',views.transactions_flag_submit,name='plaid-flag-submit'),
    # url(r'^/convert/submit$',views.transactions_convert_submit,name='plaid-convert-submit'),


]

    # url(r'^plan/$', UserPlanList.as_view(), name='userplan-list'),
    # url(r'^plan/new/$', UserPlanCreate.as_view(), name='userplan-create'),
    # url(r'^plan/(?P<pk>\d+)/$', UserPlanDetail.as_view(), name='userplan-detail'),
    # url(r'^plan/(?P<pk>\d+)/update$', UserPlanUpdate.as_view(), name='userplan-update'),
    # url(r'^plan/(?P<pk>\d+)/delete$', UserPlanDelete.as_view(), name='userplan-delete'),
    #
    # #Provider
    # url(r'^provider/$', PlanProviderList.as_view(), name='provider-list'),
    # url(r'^provider/new$', PlanProviderCreate.as_view(), name='provider-create'),
    # url(r'^provider/(?P<pk>\d+)/$', PlanProviderDetail.as_view(), name='provider-detail'),
    # url(r'^provider/(?P<pk>\d+)/update', PlanProviderUpdate.as_view(), name='provider-update'),
    # url(r'^provider/(?P<pk>\d+)/delete', PlanProviderDelete.as_view(), name='provider-delete'),
    #
    # ##events/payments
    # url(r'^plan/(?P<plan_id>\d+)/newevent/$', views.createEvent, name='event-create'),
    # url(r'^event/(?P<pk>\d+)/update', PlanEventUpdate.as_view(), name='event-update'),
    # url(r'^event/(?P<pk>\d+)/delete', PlanEventDelete.as_view(), name='event-delete'),


