"""
URL configuration for fincomp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from loginapp import views as login_views
from django.contrib.auth import views as auth_views
from vendor import views as vendor_views
from addvendor import views as addvendor_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", login_views.register,name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="loginapp/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="loginapp/logout.html"),name="logout"),
    path('vendors/', vendor_views.vendors, name='vendors'),
    path("", include("home.urls")),
    path('add-vendor/', addvendor_views.AddVendor, name="addvendor"),
    path("profile/", login_views.profile, name ="profile")
]
