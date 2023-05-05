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
        userStatus=3  #Request method is not POST
    context={'userStatus':userStatus}
    return render(request,'registration.html',context)

def loginView(request):
    if request.method=='POST':
        clf=CandidateLoginForm(request.POST)
        valusername=request.POST['username']
        valpassword=request.POST['password']
        candidate=Candidate.objects.filter(username=valusername,password=valpassword)
        if len(candidate)==0:
            loginError="Invalid username or Password"
            return render(request,'login.html',{'loginError':loginError})
        else:
            #login success

            # session variable exists accross the pages and are stored in server
            request.session['username']=candidate[0].username
            request.session['name']=candidate[0].name
            res=HttpResponseRedirect('/OTS/candidate-home/')
    else:
      clf=CandidateLoginForm()
      res=render(request,'login.html',{'clf':clf})
    return res

def candidateHome(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect('/OTS/login/')
    else:
        res=render(request,'candidate_home.html')
    return res

def testpaper(request):
    pass

def calculateTestResult(request):
    pass

def testResultHistory(request):
    pass

def showTestResult(request):
    pass

def logoutView(request):
    return HttpResponseRedirect('/OTS/login/')