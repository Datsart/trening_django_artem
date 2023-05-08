from django.contrib import admin
from .models import Bb, Rubric


# Register your models here.

class BbAdmin(admin.ModelAdmin):
    list_display = ['title', 'rubric', 'price', 'published']


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)

