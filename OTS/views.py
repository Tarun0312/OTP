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
    pass

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