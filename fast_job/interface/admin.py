from django.contrib import admin
from .models import Record, OffreEmploi, UserProfile

# Register your models here.
admin.site.register(Record)
admin.site.register(OffreEmploi)
admin.site.register(UserProfile)