from django.contrib import admin
from .models import Desk, Category, Item, Requests
# Register your models here.

admin.site.register(Desk)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Requests)
