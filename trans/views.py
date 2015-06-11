from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from planman.models import UserPlan,PlanEvent


# Create your views here.
from trans.plaidapi import PlaidAPI
from trans.models import PlaidUserToken, PlaidTransaction
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from planman.forms import PlanEvent_ConversionForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

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
        return HttpResponse("Expected a GET request with token")
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
    new_transaction_list = PlaidAPI().getTransactions(plaidaccount)
    messages.success(request,"Successfully retrieved {0} new transactions".format(len(new_transaction_list)))
    return HttpResponseRedirect(reverse_lazy('plaid-index'))

    #return render(request, 'trans/plaidlink.html', context)

class PlaidTransactionList(LoginRequiredMixin, ListView):
    model = PlaidTransaction
    template_name='trans/transactions_flag.html'
    def get_context_data(self, **kwargs):  ##adding additional context data
        context = super(PlaidTransactionList, self).get_context_data(**kwargs)
        context['showing_all']=True
        return context
    def get_queryset(self):
        return PlaidTransaction.objects.order_by('date')

class PlaidTransactionList_Flag(LoginRequiredMixin, ListView):
    model = PlaidTransaction
    template_name='trans/transactions_flag.html'
    def get_queryset(self):
        return PlaidTransaction.objects.filter(state=PlaidTransaction.STATE_NEW,
                                               usertoken__user=self.request.user).order_by('date')
    def get_context_data(self, **kwargs):  ##adding additional context data
        context = super(PlaidTransactionList_Flag, self).get_context_data(**kwargs)
        form=PlanEvent_ConversionForm()
        form.fields['userplan'].queryset=UserPlan.objects.filter(user=self.request.user)
        context['form_convert_existing']=form
        return context


@login_required()
def transaction_convert(request,pk):
    transaction=get_object_or_404(PlaidTransaction,pk=pk)

    context = {'transaction':transaction}

    #process data if its a post method
    if request.method == 'POST':
        event_form = PlanEvent_ConversionForm(data=request.POST)
        userplan=None
        if 'ignore' in request.POST:
            ##process ignore
                transaction.state=PlaidTransaction.STATE_CANCELLED
                transaction.save()
                messages.warning(request,"Transaction '{0}/{1}' discarded".format(transaction.date,transaction.name) )
                return HttpResponseRedirect(reverse_lazy('plaid-flag'))
        if 'newplan' in request.POST:
            ##process the creation of a new plan
            userplan = UserPlan(user=request.user,
                                    planprovider_text=transaction.name,
                                    notes="Provider automatically created from {3} transaction labeled '{0}' on {1} for {2}".format(transaction.name,transaction.date,transaction.amount,transaction.account.name),
                                    recurring_payment_amount = transaction.amount)
            userplan.save()
            messages.success(request,"Created new plan: {0}".format(userplan))
        elif 'convert' in request.POST:
            ##process the conversion into an existing plan
            event_form=PlanEvent_ConversionForm(data=request.POST)
            if event_form.is_valid():
                userplan = get_object_or_404(UserPlan,pk=event_form.cleaned_data['userplan'].pk)
                #userplan=event_form.userplan
            else:
                for error in event_form.non_field_errors():
                    messages.error(request,error)
                for error in event_form.errors:
                    if error=='__all__': continue
                    messages.error(request,"{0}: {1}".format(error,event_form.errors[error]))
        else:
            messages.error(request,"Unknown form submission?")

        if userplan:
            ##add the transaction as a payment
            payment = PlanEvent(userplan=userplan,
                                event_type='pay',
                                event_date=transaction.date,
                                amount=transaction.amount,
                                user_description="{0} ({1})".format(transaction.name,transaction.account.name))
            payment.save()
            transaction.state=PlaidTransaction.STATE_CONVERTED
            transaction.save()
            messages.success(request,'Added payment: {0} [{1}]<br><a href="{2}">Process more transactions...</a>'.format(payment.user_description,payment.event_date,reverse_lazy('plaid-flag')))
            return HttpResponseRedirect(reverse_lazy('userplan-detail',kwargs={'pk':userplan.pk}) + "?highlight={0}".format(payment.id))
    #if not a post, or not a valid plan, go back
    return HttpResponseRedirect(reverse_lazy('plaid-flag'))

@login_required()
def transaction_ignore(request,pk):
    transaction=get_object_or_404(PlaidTransaction,pk=pk)
    transaction.state=PlaidTransaction.STATE_CANCELLED
    transaction.save()
    messages.warning(request,"Transaction '{0}/{1}' discarded".format(transaction.date,transaction.name) )
    return HttpResponseRedirect(reverse_lazy('plaid-flag'))


@login_required
def transactions_convert_submit(request):
    return HttpResponse("Flagging was submitted")

@login_required
def transactions_flag_submit(request):
    return HttpResponse("Flagging was submitted")


###generic views
class PlaidTokenList(LoginRequiredMixin, ListView):
    model = PlaidUserToken
    def get_queryset(self):
        return PlaidUserToken.objects.filter(user=self.request.user)


class PlaidTokenUpdate(LoginRequiredMixin, UpdateView):
    model = PlaidUserToken
    template = 'trans/plaidaccount_update.html'






