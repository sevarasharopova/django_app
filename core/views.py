from django.shortcuts import render

from frontend import *

def apple(request):
    return render(request,'apple.html')

def hp(request):
    return render(request,'hp.html')

def samsung(request):
    return render(request,'samsung.html')
