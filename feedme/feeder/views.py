from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'index.html', context)

def result(request):
    context = {}
    return render(request, 'result.html', context)
