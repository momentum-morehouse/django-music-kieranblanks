#This allows the admin to edit information for the Album model
from django.contrib import admin
from .models import Album

# Register your models here.

admin.site.register(Album)