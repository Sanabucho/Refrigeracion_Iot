from django.contrib import admin
from .models import *

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
admin.site.register(Device, DeviceAdmin)

class DataTagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', )
admin.site.register(DataTag, DataTagAdmin)

class DataTSAdmin(admin.ModelAdmin):
    list_display = ('tag', 'device', 'timestamp', 'value')
admin.site.register(DataTS, DataTSAdmin)