from django.contrib import admin
from maktab.models import Maktab, Director


class MaktabAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', "opened_time", 'created_at']
    search_fields = ['name', 'location']
    list_filter = ['name']

admin.site.register(Maktab, MaktabAdmin)


class DirektorAdmin(admin.ModelAdmin):
    list_display = ['user', 'salary', 'created_at']
    search_fields = ['user']
    list_filter = ['user']

admin.site.register(Director, DirektorAdmin)
