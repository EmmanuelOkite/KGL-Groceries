from django import forms
from .models import *

#importing all models
class ProduceForm(forms.ModelForm):
    class Meta:
        model = Produce
        fields = '__all__'

