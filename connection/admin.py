from django.contrib import admin
from .models import UserLoginActivity,ConnectionUserProfile,Connections

# Register your models here.

class ConnectionUserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'country')

admin.site.register(UserLoginActivity)
admin.site.register(Connections)
admin.site.register(ConnectionUserProfile,ConnectionUserProfileAdmin)