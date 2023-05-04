from django import forms
from .models import *

class CandidateRegistrationForm(forms.ModelForm):
    class Meta:
        models=Candidate
        fields=('name','username','password')
        widgets={
            'password':forms.PasswordInput(render_value=True)
        }
        