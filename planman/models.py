from _decimal import Decimal
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    lastsync = models.DateTimeField('Last time user loaded transactions',blank=True,null=True)
    def __str__(self):
        return self.user.username

class PlanProvider(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('provider-detail', kwargs={'pk':self.pk})

class UserPlan(models.Model):

    #description
    user_description = models.CharField(max_length=200,verbose_name="Description",blank=True,help_text="form help text")
    user = models.ForeignKey(User,verbose_name='*useraccount')
    planprovider_text = models.CharField(max_length=200,verbose_name='Service Provider')
    planprovider_key = models.ForeignKey(PlanProvider,verbose_name='*service provider _ key',blank=True,null=True,on_delete=models.SET_NULL)
    notes=models.TextField(blank=True,verbose_name="Notes")

    #plan start/end/renewal
    start_date = models.DateField(null=True,blank=True)
    next_renewal_date = models.DateField(null=True,blank=True)
    expiration_date = models.DateField(null=True,blank=True)


    #payment schedule
    last_payment_date = models.DateField(null=True,blank=True)
    next_payment_date = models.DateField(null=True,blank=True)
    has_recurring_payment = models.BooleanField(default=False,verbose_name ="Has Recurring Payments?")
    recurring_payment_amount = models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name="Recurring Payment Amount")
    recurring_payment_months = models.PositiveSmallIntegerField(default=1,null=True,blank=True,verbose_name="Recurring Payment Occurs every X Months")

    def get_amount_last_month(self):
        amount = sum( (0 if not e.amount else e.amount) for e in self.planevent_set.filter(event_type='pay'))
        if amount>0: return amount
        if(self.recurring_payment_amount):
            return self.recurring_payment_amount
        return Decimal(0.0)


    def get_year_to_date(self):
        amount = sum((0 if not e.amount else e.amount) for e in self.planevent_set.filter(event_type='pay'))
        if amount>0: return amount
        return Decimal(0.0)

    def __str__(self):
        if len(self.user_description)>0:
            return self.planprovider_text + " (" + self.user_description + ")"
        else:
            return self.planprovider_text

    def get_absolute_url(self):
        return reverse('userplan-detail', kwargs={'pk':self.pk})

class PlanEvent(models.Model):
    PLANEVENT_TYPES = (('pay','pay'),('start','start'),('stop','stop'),('renew','renew'))
    userplan = models.ForeignKey(UserPlan)
    event_type = models.CharField(max_length=8,choices=PLANEVENT_TYPES)
    event_date = models.DateField()

    amount = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    user_description = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.userplan.__str__() + ":" + self.event_type +":" + self.user_description