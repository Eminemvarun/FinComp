from django.shortcuts import render
from .models import Posts

def home(request):
    context ={
        'posts' : Posts.objects.all()
    }
    return render(request,'home/home.html',context)
# Create your views here.

def about(request):
    return render(request,'home/about.html')

