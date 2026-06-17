from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
import os
import datetime
from django.conf import settings

def home_view(request):
    return render(request, 'index.html')

def google_verify(request):
    return HttpResponse("google-site-verification: google48007e848d1f13dc.html", content_type="text/html")

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: https://mchlbrns-portfolio.vercel.app/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def sitemap_xml(request):
    today = datetime.date.today().isoformat()
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += '  <url>\n'
    xml += '    <loc>https://mchlbrns-portfolio.vercel.app/</loc>\n'
    xml += '    <lastmod>' + today + '</lastmod>\n'
    xml += '    <changefreq>monthly</changefreq>\n'
    xml += '    <priority>1.0</priority>\n'
    xml += '  </url>\n'
    xml += '</urlset>'
    return HttpResponse(xml, content_type="application/xml")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap_xml),
    path('google48007e848d1f13dc.html', google_verify),
]
