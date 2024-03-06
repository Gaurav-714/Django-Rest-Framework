from django.contrib import admin
from .models import Todo # Added..

# Register your models here.
admin.site.register(Todo)