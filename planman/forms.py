from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from planman.models import PlanProvider,UserPlan,UserProfile



class UserPlanForm(forms.ModelForm):
    class Meta:
        model = UserPlan
        fields = ['user_description','planprovider_text',
                  'start_date',
                  'has_recurring_payment',
                  'next_payment_date',
                  'recurring_payment_amount',
                  'recurring_payment_months',
                  'notes'
                  ]


##User registration
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username','email','password1','password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields = ()
