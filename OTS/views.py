from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.

def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())

def candidateRegistrationForm(request):
    context={'fm':CandidateRegistrationForm()}
    return render(request,'registration_form.html',context)

def candidateRegistration(request):
    if request.method=='POST':
        username=request.POST['username']
        # check if user already exists
        if len(Candidate.objects.filter(username=username)):
            userStatus=1
        else:
            name1=request.POST['name']
            password1=request.POST['password']
            ob=Candidate(name=name1,username=username,password=password1)
            ob.save()
            userStatus=2
    else:
        userStatus=3
    context={'userStatus':userStatus}
    return render(request,'registration.html',context)

def loginView(request):
    pass

def candidateHome(request):
    pass

def testpaper(request):
    pass

def calculateTestResult(request):
    pass

def testResultHistory(request):
    pass

def showTestResult(request):
    pass

def logoutView(request):
    pass