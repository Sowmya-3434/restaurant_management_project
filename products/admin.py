from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'item_price', 'created_at']

admin.site.register(Menu, MenuAdmin)