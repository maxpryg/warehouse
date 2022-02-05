from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Truck, Entry


class EntryInline(admin.TabularInline):
    model = Entry
    extra = 1


class TruckAdmin(admin.ModelAdmin):
    inlines = [EntryInline]
    list_display = ['cw', 'truck_number', 'arrival_date', 'id']
    list_filter = ['cw', 'truck_number', 'arrival_date']


class EntryAdmin(admin.ModelAdmin):
    list_display = ['truck', 'material', 'material_description', 'quantity',
        'handling_unit']
    list_filter = ['truck']
    search_fields = ['material', 'handling_unit']


admin.site.register(Truck, TruckAdmin)
admin.site.register(Entry, EntryAdmin)
