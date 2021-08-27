from django.contrib import admin

from .models import Ressource
from .models import Booking

admin.site.register(Ressource)
admin.site.register(Booking)