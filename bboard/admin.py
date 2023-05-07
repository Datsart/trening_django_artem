from django.contrib import admin
from .models import Bb
# Register your models here.

class BbAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','published']


admin.site.register(Bb, BbAdmin)