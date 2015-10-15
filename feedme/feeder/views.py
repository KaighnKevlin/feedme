from django.shortcuts import render
from django.http import HttpResponse

from .models import Restaurant

def index(request):
    context = {}
    return render(request, 'index.html', context)

def result(request):
    restaurant = Restaurant.objects.all()[5]
    context = {'restaurant': restaurant}
    return render(request, 'result.html', context)