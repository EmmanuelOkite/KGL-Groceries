from django import forms
from .models import *

#importing all models
class ProduceForm(forms.ModelForm):
    type = forms.CharField(disabled=False, required=True, label="Type")
    class Meta:
        model = Produce
        fields = '__all__'







