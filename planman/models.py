from django.db import models
from django.core.urlresolvers import reverse

class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class PlanProvider(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class UserPlan(models.Model):
    user_description = models.CharField(max_length=200)
    userprofile = models.ForeignKey(UserProfile)
    provider = models.ForeignKey(PlanProvider)
    start_date = models.DateField()
    next_renewal_date = models.DateField()
    expiration_date = models.DateField()
    #@todo:  fix these fields
    #type = models.  @type field, how to do this?
    #recurring_amount = models.DecimalField()  #:  check syntax
    #notes = models.TextField()   #
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

# # Create your models here.
# class Question(models.Model):
#   #list model attributes below, as subclasses of with models.<type>
#   question_text = models.CharField(max_length=200)
#   pub_date = models.DateTimeField('date published')
#
#   #default string description of the model object
#   def __str__(self):
#     return self.question_text
#   #create a custom attribute that returns a calculation
#   def was_published_recently(self):
#     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#   #some customizations to how the field is displayed in admin.  See Django list display
#   was_published_recently.admin_order_field = 'pub_date'
#   was_published_recently.boolean = True
#   was_published_recently.short_description='Published Recently?'
#
#
# class Choice(models.Model):
#   question = models.ForeignKey(Question)
#   choice_text = models.CharField(max_length=200)
#   votes = models.IntegerField(default=0)
#
#   def __str__(self):
#     return "%s (%d votes)" % (self.choice_text, self.votes)
