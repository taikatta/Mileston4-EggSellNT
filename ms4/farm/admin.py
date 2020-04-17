from django.contrib import admin

from .models import Farm

class FarmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
    

admin.site.register(Farm, FarmAdmin)
