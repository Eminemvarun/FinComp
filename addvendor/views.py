from django.shortcuts import render,redirect
from vendor.models import Vendor
from .forms import VendorRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def AddVendor(request):
    if(request.method == "POST"):
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = VendorRegistrationForm()

    return render(request,'addvendor/add_vendor.html',{ "form" : form } )