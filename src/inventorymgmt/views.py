from django.shortcuts import render, redirect
from .models import *
from .forms import StockCreateForm

# Create your views here.
def home(request):
    title = 'Welcome to the Main Page'
    form = 'this is form'
    context = {
    "title": title,
    "test1":form, 
    }
    return render(request, "start.html",context)

def list_inventory(request):
    title = 'Inventory List'
    queryset = Stock.objects.all()
    context = {
    "title": title,
    "queryset": queryset
    }
    return render(request, "list_inventory.html",context)

def add_inventory(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_inventory')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_inventory.html", context)