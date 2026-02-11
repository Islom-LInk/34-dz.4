from django.shortcuts import render
from apps.bolot.models import CompanyInfo
# Create your views here.

def base(request):
    return render(request,'base.html',locals())

def homepage(request):
    return render(request, "homepage.html",locals())

def sierra(request):
    info = CompanyInfo.objects.latest("id")
    return render(request, "sierra.html",locals())

def urmat(request):
    return render(request, "urmat.html",locals())