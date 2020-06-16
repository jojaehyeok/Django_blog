from django.contrib import admin
from .models import Rankingdata, Chartdata, GJ_risk, JN_risk

admin.site.register(JN_risk)
admin.site.register(GJ_risk)
admin.site.register(Rankingdata)
admin.site.register(Chartdata)

# Register your models here.
