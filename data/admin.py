from django.contrib import admin
from .models import CorFeatures, Corporates, CorRisk
# Register your models here.

admin.site.register(CorRisk)
admin.site.register(CorFeatures)
admin.site.register(Corporates)
