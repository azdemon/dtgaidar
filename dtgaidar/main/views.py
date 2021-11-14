from django.shortcuts import render
from . import templates

def index(request):
    return render(request, 'main/index.html')
