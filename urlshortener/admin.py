# urlshortener/admin.py
from django.contrib import admin
from .models import URL, Click

admin.site.register(URL)
admin.site.register(Click)
from django.contrib import admin

# Register your models here.
