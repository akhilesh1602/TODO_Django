from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("akhil")
    


def remove(request,pk):
    pass

# Create your views here.
