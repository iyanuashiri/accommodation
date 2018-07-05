from django.contrib import admin

from .models import Apartment

# Register your models here.


class ApartmentAdmin(admin.ModelAdmin):

    list_display = ('title', 'location', 'number_of_rooms', 'duration')
    fields = ('title', 'picture', 'description', 'location', 'rent', 'number_of_rooms', 'house_type', 'duration')

    search_fields = ('title', 'description')


admin.site.register(Apartment, ApartmentAdmin)
