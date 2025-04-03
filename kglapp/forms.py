from django import forms
from .models import *

#importing all models
class ProduceForm(forms.ModelForm):
    type = forms.CharField(disabled=False, required=True, label="Type")
    class Meta:
        model = Produce
        fields = '__all__'

class SellingForm(forms.ModelForm):
    class Meta:
        model = Selling
        fields = ['produce', 'tonnage_in_kgs', 'amount_paid', 'buyer_name', 'sales_agent_name', 'date_time']





