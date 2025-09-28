from django.contrib import admin

# Register your models here.
from .models import Catergory, Item

admin.site.register(Catergory)
admin.site.register(Item)