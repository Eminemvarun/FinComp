from django import forms
from django.forms import ModelForm
from vendor.models import Vendor


class VendorRegistrationForm(ModelForm):
    class Meta:
        model = Vendor
        fields = [
        'ref_no',
        'company_name',
        'software_name',
        'company_website',
        'type_of_software',
        'description',
        'company_established',
        'countries',
        'cities',
        'contact_no',
        'address',
        'employees',
        'professional_services',
        'last_demo_date',
        'last_reviewed_date',
        ]     
