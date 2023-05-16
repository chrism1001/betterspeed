from django.shortcuts import render
from django.http import HttpResponse


def register_home(request):
    return HttpResponse('<h1>Register Home</h1>')
