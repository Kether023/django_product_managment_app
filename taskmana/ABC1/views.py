from django.shortcuts import render

def index(request):
    return render(request, 'ABC1/index.html')


def about(request):
    return render(request, 'ABC1/about.html')


def login(request):
    return render(request, 'ABC1/login.html')


def museumpermafrost(request):
    return render(request, 'ABC1/museumpermafrost.html')


