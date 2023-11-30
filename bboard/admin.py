from django.contrib import admin
from .models import Bb, Rubric


# Register your models here.

class BbAdmin(admin.ModelAdmin):
    def get_kind_display_humanized(self, obj):
        return obj.get_kind_display()

    get_kind_display_humanized.short_description = 'Действие'
    # тайтл и прайс - метод модели, применил в админке
    list_display = ['title', 'content', 'price', 'published', 'rubric', 'get_kind_display_humanized', 'title_and_price']

    # list_display_links = ['title', 'content']
    # search_fields = ['content', 'title']


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
