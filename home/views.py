from django.shortcuts import render
from vendor.models import Vendor

def home(request):
    vendors = Vendor.objects.all().filter()[:5]
    return render(request,'home/home.html',{'vendors': vendors})

# Create your views here.

def about(request):
    return render(request,'home/about.html')

