from django.urls import path
from .views import *
app_name='OTS'

urlpatterns = [
    path('',welcome),
    path('new-candidate/',candidateRegistrationForm,name='registrationForm'),
    path('store-candidate/',candidateRegistration,name='storeCandidate'),
    path('login/',loginView,name='login'),
    path('candidate-home/',candidateHome),
    path('testpaper/',testpaper),
    path('calculate-result/',calculateTestResult),
    path('test-history/',testResultHistory),
    path('show-result/',showTestResult),
    path('logout/',logoutView)
]
