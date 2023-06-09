from django.http import HttpResponse
from django.shortcuts import redirect, render
from polls.models import Feedback

def index(request):
    return render(request, 'polls/index.html', {})

def new(request):
    return render(request, 'polls/new.html', {})

def sale(request):
    return render(request, 'polls/sale.html', {})

def sale_item(request):
    return render(request, 'polls/sale_item.html', {})

def devices(request):
    return render(request, 'polls/devices.html', {})

def contact(request):
    return render(request, 'polls/contact.html', {})