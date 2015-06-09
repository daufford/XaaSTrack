from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

# Create your views here.
from trans.plaidapi import PlaidAPI
from trans.models import PlaidUserToken, PlaidTransaction


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

@login_required
def index(request):
    return HttpResponse("Index page")


# https://github.com/plaid/link
@login_required
def plaidlink(request):
    public_key='test_key'
    client_id = 'test_id'
    context = {'client_id': PlaidAPI.client_id,
               'product': 'connect',
               'public_key': PlaidAPI.public_key,
               'env': PlaidAPI.env
               }
    return render(request, 'trans/plaidlink.html', context)

@login_required
def plaidlink_submit(request):
    print('request')
    print(request.GET)
    if request.GET: public_token = request.GET.get('public_token',None)
    if not public_token:
        return HttpResponse("you didn't get it")
    print('Token:')
    print(public_token)

    ##Exchange token and create account
    plaidaccount = PlaidAPI().exchangeLinkTokenForAccount(request.user,public_token)
    context={'plaidaccount':plaidaccount}
    return render(request, 'trans/plaidlinksubmit.html', context)

@login_required
def transactions_retrieve(request, pk):
    plaidaccount = get_object_or_404(PlaidUserToken,pk=pk)
    print('Retrieving transactions')
    PlaidAPI().getTransactions(plaidaccount)
    return HttpResponse("Got the transactions")

    #return render(request, 'trans/plaidlink.html', context)

@login_required
def transactions_flag(request):
    return HttpResponse("Flagging any transactions as relvent")

@login_required
def transactions_flag_submit(request):
    return HttpResponse("Flagging was submitted")

@login_required
def transactions_convert(request):
    return HttpResponse("Converting flagged transactions into payment entries ")

@login_required
def transactions_convert_submit(request):
    return HttpResponse("Flagging was submitted")


###generic views
class PlaidTokenList(LoginRequiredMixin, ListView):
    model = PlaidUserToken


class PlaidTokenUpdate(LoginRequiredMixin, UpdateView):
    model = PlaidUserToken
    template = 'trans/plaidaccount_update.html'


class PlaidTransactionUpdate(LoginRequiredMixin, UpdateView):
    model = PlaidTransaction


class PlaidTransactionList(LoginRequiredMixin, ListView):
    model = PlaidTransaction
