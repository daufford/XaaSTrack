from django import forms
from planman.models import PlanProvider,UserPlan


class UserPlanForm(forms.ModelForm):
    class Meta:
        model = UserPlan
        fields = ['user_description','userprofile','planprovider','start_date',
                  'next_renewal_date','expiration_date'
                  ]



