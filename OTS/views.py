from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
import random

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
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    else:
        question_pool=Question.objects.all()
        n=int(request.GET['n'])
        random.shuffle(list(question_pool))
        question_list=question_pool[:n]
        context={'questions':question_list}
        res=render(request,'testpaper.html',context)
    return res


def calculateTestResult(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect('login')
    else:
        total_right=0
        total_wrong=0
        total_attempted=0
        question_list=[]
        for k in request.POST:
            if k.startswith('qno'):
                question_list.append(int(k))
        
        for n in question_list:
            question=Question.objects.get(qid=n)
            try:
                if question.ans==request.get['q'+str(n)]:
                    total_right+=1
                else:
                    total_wrong+=1
                total_attempted+=1
            except:
                pass
            total_points=((total_right-total_wrong)/len(question_list))*10

            # store it in result table
            result=Result()
            result.username=Candidate.objects.get(request.session['usename'])
            result.right=total_right
            result.wrong=total_wrong
            result.attempt=total_attempted
            result.points=total_points
            result.save()

            # update candidate table
            candidate=Candidate.objects.get(request.session['username'])
            candidate.test_attempted+=1
            candidate.points=(candidate.points*(candidate.test_attempted-1)+total_points)/candidate.test_attempted
            candidate.save()

            return HttpResponseRedirect('result')
            
            
                

def testResultHistory(request):
    pass

def showTestResult(request):
    if 'name' not in request.session['username']:
        HttpResponseRedirect('login')
    else:
        candidate=Candidate.objects.get(username=request.session['username'])
        result=Result.objects.get(username=candidate.username)
        context={'result':result,'candidate':candidate}
        return render(request,'result.html',context)

def logoutView(request):
    if 'name' in request.session.keys():
        res=HttpResponseRedirect('/OTS/login/')
    return res