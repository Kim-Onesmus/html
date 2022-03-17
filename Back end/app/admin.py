from django.contrib import admin
# from . import models
from .models import Client
from .models import Shop
# Register your models here.

admin.site.register(Client)
admin.site.register(Shop)