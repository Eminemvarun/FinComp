from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Vendor


@login_required
def vendors(request):

    page = request.GET.get('page', 1)
    paginator = Paginator(Vendor.objects.all(), 3)
    page_obj = paginator.get_page(page)

    return render(request, 'vendor/vendors.html', {'page_obj': page_obj})
