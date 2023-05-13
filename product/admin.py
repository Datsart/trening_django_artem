from django.contrib import admin
from .models import Product, Units


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'unit']
    list_display_links = ['title', 'amount']
    # search_fields = ['title']


admin.site.register(Product, ProductAdmin)
admin.site.register(Units)
