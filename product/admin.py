from django.contrib import admin
from .models import Product, Units


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'unit']


admin.site.register(Product, ProductAdmin)
admin.site.register(Units)
