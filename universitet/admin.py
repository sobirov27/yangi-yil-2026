from django.contrib import admin
from universitet.models import Direktor, Universitet, Oqituvchi


class DirektorAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user']
    list_filter = ['user']

admin.site.register(Direktor, DirektorAdmin)





class UniversitetAdmin(admin.ModelAdmin):
    list_display = ['name', 'manzil', 'oquvchilar_soni', "ochilish_vaqti", 'created_at']
    list_filter = ['name']
    search_fields = ['name', 'manzil']

admin.site.register(Universitet, UniversitetAdmin)





class OqituvchiAdmin(admin.ModelAdmin):
    list_display = ['age', 'about', 'created_at']
    search_fields = ['about']
    list_filter = ['about']

admin.site.register(Oqituvchi, OqituvchiAdmin)