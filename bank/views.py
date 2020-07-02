from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from .filters import *

# Create your views here.
def home(request):
    return render(request,'bank/home.html')

def search(request):
    q=request.GET.get('search')
    srch=Bank.objects.filter(IFSCCode__contains=q)
    return render(request,'bank/search.html',{'s':srch})

def search1(request):
    q=request.GET.get('city')
    q1=request.GET.get('bank')
    srch=Bank.objects.filter(city__contains=q,name_of_bank__contains=q1)
    return render(request,'bank/search1.html',{'s':srch})

