from django.contrib import admin

# Register your models here.
from .models import Title, Description

admin.site.register(Title)
admin.site.register(Description)