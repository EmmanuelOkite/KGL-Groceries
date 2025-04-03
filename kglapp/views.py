from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.db.models import Sum

from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')  # Ensure this template exists

def branches(request):
    return render(request, 'branches.html') 

def base(request):
    return render(request, 'base.html')

def director(request):
    return render(request, 'director.html')

def manager(request):
    return render(request, 'manager.html')

def attendant(request):
    return render(request, 'attendant.html')

def create_produce(request):
    if request.method == 'POST':
        form = ProduceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_produce')
    else:
        form = ProduceForm()
    produces = Produce.objects.all()
    return render(request, 'create_produce.html', {'form': form, 'produces': produces})

def produce_list(request):
    produces = Produce.objects.all()
    return render(request, 'produce_list.html', {'produces': produces})

def dashboard(request):
    produce_summary = (
        Produce.objects
        .values('name')
        .annotate(total_tonnage=Sum('tonnage_in_kgs'))
    )

    return render(request, 'dashboard.html', {'produce_summary': produce_summary})


def sell_produce(request):
    if request.method == 'POST':
        form = SellingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_dashboard')
    else:
        form = SellingForm()
    return render(request, 'sell_produce.html', {'form': form})

def sales_dashboard(request):
    sales = Selling.objects.all()
    return render(request, 'sales_dashboard.html', {'sales': sales})

def edit_sale(request, sale_id):
    sale = get_object_or_404(Selling, id=sale_id)
    if request.method == 'POST':
        form = SellingForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sales_dashboard')
    else:
        form = SellingForm(instance=sale)
    return render(request, 'edit_sale.html', {'form': form})

def delete_sale(request, sale_id):
    sale = get_object_or_404(Selling, id=sale_id)
    sale.delete()
    return redirect('sales_dashboard')

def sales_table(request):
    sales = Selling.objects.all()
    return render(request, 'sales_table.html', {'sales': sales})


    

# def selling_produce(request):
#     if request.method == 'POST':
#         form = SellingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('sell_produce')
#     else:
#         form = SellingForm()
#     produces = Produce.objects.all()
#     return render(request, 'sell_produce.html', {'form': form, 'produces': produces})



# def deferring_produce(request):
#     if request.method == 'POST':
#         form = DeferringForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('defer_produce')
#     else:
#         form = DeferringForm()
#     produces = Produce.objects.all()
#     return render(request, 'deferring_produce.html', {'form': form, 'produces': produces})
