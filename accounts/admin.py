from django.contrib import admin

from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.site_header = 'Lodgeme Administration'
admin.site.site_title = 'Lodgeme Admin'
admin.site.index_title = 'Lodgeme Administration'

