from django import forms
from .models import *

#importing all models
class ProduceForm(forms.ModelForm):
    name = forms.ChoiceField(
        choices=Produce.PRODUCE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "Select Produce"}),
        label=""
    )
    type = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "readonly": "readonly", "placeholder": "Auto-filled Type"}),
        label=""
    )
    date = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "readonly": "readonly", "placeholder": "Auto-filled Date"}),
        label=""
    )
    time_of_produce = forms.TimeField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "readonly": "readonly", "placeholder": "Auto-filled Time"}),
        label=""
    )
    tonnage_in_kgs = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Tonnage in KGs", "class": "form-control"}),
        label=""
    )
    cost_per_kg = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Cost per KG", "class": "form-control"}),
        label=""
    )
    total_cost = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "readonly": "readonly", "placeholder": "Auto-calculated Total Cost"}),
        label=""
    )
    dealer_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Dealer Name", "class": "form-control"}),
        label=""
    )
    contact = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Contact (+256...)", "class": "form-control"}),
        label=""
    )
    price_to_sell = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Selling Price", "class": "form-control"}),
        label=""
    )

    class Meta:
        model = Produce
        fields = '__all__'

class SellingForm(forms.ModelForm):
    produce = forms.ModelChoiceField(
        queryset=Selling._meta.get_field('produce').remote_field.model.objects.all(),
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "Select Produce"}),
        label=""
    )
    tonnage_in_kgs = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Tonnage in KGs", "class": "form-control"}),
        label=""
    )
    amount_paid = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Amount Paid", "class": "form-control"}),
        label=""
    )
    buyer_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Buyer's Name", "class": "form-control"}),
        label=""
    )
    sales_agent_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Sales Agent Name", "class": "form-control"}),
        label=""
    )
    date = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "readonly": "readonly", "placeholder": "Auto-filled Date"}),
        label=""
    )

    class Meta:
        model = Selling
        fields = '__all__'
   




