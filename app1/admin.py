from django.contrib import admin
from .models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'citizens', )
    list_display_links = ('id', 'city', 'citizens', )
    ordering = ('city', )


admin.site.register(City, CityAdmin)
