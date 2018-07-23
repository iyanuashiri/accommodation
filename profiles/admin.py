from django.contrib import admin

from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.site_header = 'Lodgeme Administration'
admin.site.site_title = 'Lodgeme Admin'
admin.site.index_title = 'Lodgeme Administration'
