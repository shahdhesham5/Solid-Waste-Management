from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import *

class AddGAdmin(LeafletGeoAdmin):
    pass
# Register your models here.
admin.site.register(Add)
admin.site.register(AddG,AddGAdmin)
