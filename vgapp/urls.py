from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home',views.index,name="home"),
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
    path('accounts/login_up/',views.log,name="login"),
    path('accounts/logout/',views.logout,name="logout")


]