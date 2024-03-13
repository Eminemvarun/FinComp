from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):

    if(request.method == "POST"):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,"Account Created Successfully")
            return redirect("login")
    else:
        form = UserRegisterForm()

    
    return render(request,'loginapp/register.html',{"form":form})

def user_logout(request):
    logout(request)
    return render(request,"loginapp/logout.html", {})
