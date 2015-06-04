from datetime import timezone
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
    user_description = models.CharField(max_length=200,verbose_name="Description")
    user = models.ForeignKey(User,verbose_name='*useraccount')
    planprovider_text = models.CharField(max_length=200,verbose_name='Service Provider')
    planprovider_key = models.ForeignKey(PlanProvider,verbose_name='*service provider _ key',blank=True,null=True,on_delete=models.SET_NULL)
    notes=models.TextField(blank=True,verbose_name="Notes")

    #plan start/end/renewal
    start_date = models.DateField(null=True,blank=True)
    next_renewal_date = models.DateField(null=True,blank=True)
    expiration_date = models.DateField(null=True,blank=True)

    #payments
    last_payment_date = models.DateField(null=True,blank=True)
    next_payment_date = models.DateField(null=True,blank=True)
    has_recurring_payment = models.BooleanField(default=False,verbose_name ="Has Recurring Payments?")
    recurring_payment_amount = models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2,verbose_name="Recurring Payment Amount")
    recurring_payment_months = models.PositiveSmallIntegerField(null=True,blank=True,verbose_name="Recurring Payment Occurs every X Months")

    def __str__(self):
        return self.user_description
    def get_absolute_url(self):
        return reverse('userplan-detail', kwargs={'pk':self.pk})

class PlanEvent(models.Model):
    userplan = models.ForeignKey(UserPlan)
    user_description = models.CharField(max_length=200)
    def __str__(self):
        return self.user_description

class PlanPayments(models.Model):
    user_description = models.CharField(max_length=200)
    planevent = models.ForeignKey(PlanEvent)
    def __str__(self):
       return self.user_description
