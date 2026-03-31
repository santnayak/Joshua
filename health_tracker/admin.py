from django.contrib import admin
from .models import BloodPressure, SugarLevel, Weight


@admin.register(BloodPressure)
class BloodPressureAdmin(admin.ModelAdmin):
    list_display = ('user', 'systolic', 'diastolic', 'recorded_at')
    list_filter = ('user', 'recorded_at')
    search_fields = ('user__username',)
    date_hierarchy = 'recorded_at'


@admin.register(SugarLevel)
class SugarLevelAdmin(admin.ModelAdmin):
    list_display = ('user', 'glucose_level', 'meal_timing', 'recorded_at')
    list_filter = ('user', 'meal_timing', 'recorded_at')
    search_fields = ('user__username',)
    date_hierarchy = 'recorded_at'


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'recorded_at')
    list_filter = ('user', 'recorded_at')
    search_fields = ('user__username',)
    date_hierarchy = 'recorded_at'
