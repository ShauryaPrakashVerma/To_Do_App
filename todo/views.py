from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addTask(request):
    return HttpResponse('<h1>The form is submitted</h1>')