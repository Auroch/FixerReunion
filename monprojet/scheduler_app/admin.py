from django.contrib import admin
from .models import Lieu, Presence, Demande

admin.site.register(Lieu)
admin.site.register(Presence)
admin.site.register(Demande)
