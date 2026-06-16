from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings

def home_view(request):
    return render(request, 'index.html')

def google_verify(request):
    return HttpResponse("google-site-verification: google48007e848d1f13dc.html", content_type="text/html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('google48007e848d1f13dc.html', google_verify),
    path('', home_view, name='home'),
]