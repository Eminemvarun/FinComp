from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="fincomp-home"),
    path("about/",views.about, name="fincomp-about"),
]