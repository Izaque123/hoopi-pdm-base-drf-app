from django.contrib import admin
from .models import Travel
# Register your models here.
class TravelAdmin(admin.ModelAdmin):
    list_display = ('start', 'end', 'start_date', 'time', 'places', 'price')
    search_fields = ('start', 'end', 'start_date', 'time', 'places', 'price')
    list_filter = ('start', 'end', 'start_date', 'time', 'places', 'price')
    ordering = ('start', 'end', 'start_date', 'time', 'places', 'price')
admin.site.register(Travel, TravelAdmin)