from django.shortcuts import render
from .import models

# Create your views here.

def at(request):
    form=models.at.objects.all()
    return render(request,'at.html',{"sub":form})