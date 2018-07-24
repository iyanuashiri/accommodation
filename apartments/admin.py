from django.contrib import admin

from .models import Apartment

# Register your models here.


class ApartmentAdmin(admin.ModelAdmin):

    list_display = ('title', 'location', 'number_of_rooms', 'duration')
    fields = ('title', 'picture', 'description', 'location', 'rent', 'number_of_rooms', 'house_type', 'duration', 'landlord_name', 'landlord_number')

    search_fields = ('title', 'description')


admin.site.register(Apartment, ApartmentAdmin)
admin.site.site_header = 'Lodgeme Administration'
admin.site.site_title = 'Lodgeme Admin'
admin.site.index_title = 'Lodgeme Administration'

