
# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class PlaidUserToken(models.Model):  #really a plaid useraccount
    user=models.ForeignKey(User)
    access_token=models.CharField(verbose_name='token used to access account from plaid',max_length=200)
    last_sync=models.DateTimeField(blank=True,null=True)
    STATUS_TYPES = (('ok','Ok'),('connecting','In Process'),('failed','Needs Attention'),('new','New'))
    status = models.CharField(max_length=10,choices=STATUS_TYPES)
    status_text=models.CharField(max_length=128,blank=True)

class PlaidAccount(models.Model):
    usertoken = models.ForeignKey(PlaidUserToken)
    _id = models.CharField(max_length=50)
    _item = models.CharField(max_length=50)
    _user = models.CharField(max_length=50)
    name = models.CharField(verbose_name='Account Name',max_length=50,blank=True,null=True)
    type = models.CharField(verbose_name='Account Type', max_length=10)
    institution_type = models.CharField(max_length=10)
# [{'_id': 'aV4qOmw5YDTe8KR1vmJoUX1QEJq676fbnyxrm',
#   '_item': 'R0LwXJyoYbcAga61M3bYIXVbyj04AktovKanX',
#   '_user': 'OkdapOqoYBUmej765Q0YHQjzQ8Er7Mce6ZjbL',
#   'balance': {'available': 5192.12, 'current': 788.13},
#   'institution_type': 'chase',
#   'meta': {'limit': 6000, 'name': 'Amazon Credit Card', 'number': '3407'},
#   'type': 'credit'}]

class PlaidTransaction(models.Model):
    json_raw=models.TextField(blank=True)

    usertoken = models.ForeignKey(PlaidUserToken)
    account = models.ForeignKey(PlaidAccount)

    _account = models.CharField(max_length=50)
    _id = models.CharField(primary_key=True,max_length=50)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField(blank=True,null=True)
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=50,blank=True)
    type=models.CharField(max_length=50)
    meta=models.CharField(max_length=200,blank=True)
    meta_score=models.CharField(max_length=200,blank=True)
    STATE_NEW = 0
    STATE_FLAGGED = 1
    STATE_CONVERTED = 2
    STATE_CANCELLED = 3
    STATES = ((STATE_NEW,'new'),(STATE_FLAGGED,'flagged'),
              (STATE_CONVERTED,'converted'),(STATE_CANCELLED,'ignored'))
    state = models.SmallIntegerField(choices=STATES)

# {'_account': 'aV4qOmw5YDTe8KR1vmJoUX1QEJq676fbnyxrm',
#   '_id': 'Bn7ZXV9pa3Sabn51v0m3CQ88ezm4AMcNmaRqX',
#   'amount': -2780.52,
#   'category': ['Payment', 'Credit Card'],
#   'category_id': '16001000',
#   'date': '2015-03-05',
#   'meta': {'location': {}},
#   'name': 'Credit Card Payment',
#   'pending': False,
#   'score': {'location': {}, 'name': 1},
#   'type': {'primary': 'special'}},
#  {'_account': 'aV4qOmw5YDTe8KR1vmJoUX1QEJq676fbnyxrm',
#   '_id': 'AQg7XNaV4KceboMKngLJUwxxZ8dqyDTjmJgYr',
#   'amount': 1.5,
#   'date': '2015-03-04',
#   'meta': {'location': {'city': 'Chicago', 'state': 'IL', 'zip': '60651'}},
#   'name': 'COCA COLA CHICAGO IL',
#   'pending': False,
#   'score': {'location': {'city': 1, 'state': 1, 'zip': 1}, 'name': 0.2},
#   'type': {'primary': 'place'}}]



# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     lastsync = models.DateTimeField('Last time user loaded transactions',blank=True,null=True)
#     def __str__(self):
#         return self.user.username
#
# class PlanProvider(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name
#     def get_absolute_url(self):
#         return reverse('provider-detail', kwargs={'pk':self.pk})
#
# class UserPlan(models.Model):
#
#     #description
#     user_description = models.CharField(max_length=200,verbose_name="Description",blank=True,help_text="form help text")
#     user = models.ForeignKey(User,verbose_name='*useraccount')
#     planprovider_text = models.CharField(max_length=200,verbose_name='Service Provider')
#     planprovider_key = models.ForeignKey(PlanProvider,verbose_name='*service provider _ key',blank=True,null=True,on_delete=models.SET_NULL)
#     notes=models.TextField(blank=True,verbose_name="Notes")
#
#     #plan start/end/renewal
#     start_date = models.DateField(null=True,blank=True)
#     next_renewal_date = models.DateField(null=True,blank=True)
#     expiration_date = models.DateField(null=True,blank=True)
#
#
#     #payment schedule
#     last_payment_date = models.DateField(null=True,blank=True)
#     next_payment_date = models.DateField(null=True,blank=True)
#     has_recurring_payment = models.BooleanField(default=False,verbose_name ="Has Recurring Payments?")
#     recurring_payment_amount = models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name="Recurring Payment Amount")
#     recurring_payment_months = models.PositiveSmallIntegerField(default=1,null=True,blank=True,verbose_name="Recurring Payment Occurs every X Months")
#
#     def get_amount_last_month(self):
#         amount = sum( (0 if not e.amount else e.amount) for e in self.planevent_set.filter(event_type='pay'))
#         if amount>0: return amount
#         if(self.recurring_payment_amount):
#             return self.recurring_payment_amount
#         return Decimal(0.0)
#
#
#     def get_year_to_date(self):
#         amount = sum((0 if not e.amount else e.amount) for e in self.planevent_set.filter(event_type='pay'))
#         if amount>0: return amount
#         return Decimal(0.0)
#
#     def __str__(self):
#         if len(self.user_description)>0:
#             return self.planprovider_text + " (" + self.user_description + ")"
#         else:
#             return self.planprovider_text
#
#     def get_absolute_url(self):
#         return reverse('userplan-detail', kwargs={'pk':self.pk})
#
# class PlanEvent(models.Model):
#     PLANEVENT_TYPES = (('pay','pay'),('start','start'),('stop','stop'),('renew','renew'))
#     userplan = models.ForeignKey(UserPlan)
#     event_type = models.CharField(max_length=8,choices=PLANEVENT_TYPES)
#     event_date = models.DateField()
#
#     amount = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
#     user_description = models.CharField(max_length=200,blank=True)
#
#     def __str__(self):
#         return self.userplan.__str__() + ":" + self.event_type +":" + self.user_description