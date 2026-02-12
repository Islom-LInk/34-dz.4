from django.shortcuts import render
from apps.bolot.models import MyInfo
# Create your views here.


def homepage_view(request):
    return render(request, "homepage.html",locals())


def base_view(request):
    info = MyInfo.objects.first()
    return render(request, "base.html",locals())


def urmat_view(request):
    return render(request, "urmat.html",locals())


def sierra_view(request):
    return render(request, "sierra.html",locals())

















def base(request):
    return render(request,'base.html',locals())

def homepage(request):
    return render(request, "homepage.html",locals())

def sierra(request):
    info = MyInfo.objects.latest("id")
    return render(request, "sierra.html",locals())

def urmat(request):
    return render(request, "urmat.html",locals())