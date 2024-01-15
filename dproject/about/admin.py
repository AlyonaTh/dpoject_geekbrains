from django.contrib import admin
from .models import About


@admin.register(About)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
