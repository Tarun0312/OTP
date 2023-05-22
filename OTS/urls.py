from django.urls import path
from .views import *
app_name='OTS'

urlpatterns = [
    path('',welcome),
    path('new-candidate/',candidateRegistrationForm,name='registrationForm'),
    path('store-candidate/',candidateRegistration,name='storeCandidate'),
    path('login/',loginView,name='login'),
    path('candidate-home/',candidateHome,name='home'),
    path('testpaper/',testpaper,name='testPaper'),
    path('calculate-result/',calculateTestResult,name='calculateTest'),
    path('test-history/',testResultHistory,name='testHistory'),
    path('show-result/',showTestResult,name='result'),
    path('logout/',logoutView,name='logout')
]
