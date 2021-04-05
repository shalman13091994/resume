from django.shortcuts import render
from django.http import HttpResponse

def homeview(request):
    return render(request,'home.html')

