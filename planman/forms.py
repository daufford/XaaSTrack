from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput

from planman.models import UserPlan,UserProfile, PlanEvent


class UserPlanForm(forms.ModelForm):
    class Meta:
        model = UserPlan
        fields = ['planprovider_text','user_description',
                  'recurring_payment_amount',
                  'recurring_payment_months',
                  'next_payment_date',
                  'notes'
                  ]
    def clean(self):
        cleaned_data = super(UserPlanForm, self).clean()

class PlanEventForm(forms.ModelForm):
    event_type=None
    class Meta:
        model=PlanEvent
        fields = ['event_date','user_description','amount']
        widgets = {
            'event_date':DateInput(attrs={'size': 8, 'title': 'Event date',})
        }
    def clean(self):
        cleaned_data = super(PlanEventForm, self).clean()
        amount = cleaned_data.get('amount')
        if(self.event_type=='pay' and (not amount or amount<=0)):
            raise forms.ValidationError("Enter amount when adding a payment")

class PlanEvent_ConversionForm(forms.ModelForm):
    class Meta:
        model=PlanEvent
        fields = ['userplan']


##User registration
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username','email','password1','password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields = ()
