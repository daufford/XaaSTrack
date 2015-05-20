from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'test': 'sup' }
    return render(request,'planman/index.html',context)