from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Vendor  # Assuming Vendor is your model for vendors


@login_required
def vendors(request):
    vendors = Vendor.objects.all()  # Fetch all vendors from the database
    return render(request, 'vendor/vendors.html', {'vendors': vendors})