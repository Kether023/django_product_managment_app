from django.shortcuts import render

def index(request):
    return render(request, 'ABC1/index.html')


def about(request):
    return render(request, 'ABC1/about.html')


def login(request):
    return render(request, 'ABC1/login.html')


def museumpermafrost(request):
    return render(request, 'ABC1/museumpermafrost.html')


def register(request):
    return render(request, 'ABC1/register.html')


def lena(request):
    return render(request, 'ABC1/lena.html')


def pricelist(request):
    return render(request, 'ABC1/pricelist.html')


def paypage(request):
    return render(request, 'ABC1/paypage.html')


