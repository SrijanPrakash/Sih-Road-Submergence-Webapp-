from django.contrib import admin
from .models import Rain,DamWaterYear,DamWaterDay,RoadSubmergenceDay,RoadSubmergenceYear


# Register your models here.
admin.site.register(Rain)
admin.site.register(DamWaterYear)
admin.site.register(DamWaterDay)
admin.site.register(RoadSubmergenceDay)
admin.site.register(RoadSubmergenceYear)
