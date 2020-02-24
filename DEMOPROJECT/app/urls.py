from django.contrib import admin
from DEMOPROJECT.app import views

urlpatterns = [
    path('', views.hi),
    ]