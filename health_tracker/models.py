from django.db import models
from django.contrib.auth.models import User


class BloodPressure(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blood_pressure_readings')
    systolic = models.IntegerField(help_text='Systolic pressure (mmHg)')
    diastolic = models.IntegerField(help_text='Diastolic pressure (mmHg)')
    recorded_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-recorded_at']
        verbose_name_plural = 'Blood Pressure Readings'

    def __str__(self):
        return f"{self.user.username} - {self.systolic}/{self.diastolic} at {self.recorded_at}"


class SugarLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sugar_level_readings')
    glucose_level = models.DecimalField(max_digits=5, decimal_places=1, help_text='Blood glucose level (mg/dL)')
    recorded_at = models.DateTimeField(auto_now_add=True)
    meal_timing = models.CharField(max_length=20, choices=[
        ('fasting', 'Fasting'),
        ('before_meal', 'Before Meal'),
        ('after_meal', 'After Meal'),
        ('bedtime', 'Bedtime'),
    ], default='fasting')
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-recorded_at']
        verbose_name_plural = 'Sugar Level Readings'

    def __str__(self):
        return f"{self.user.username} - {self.glucose_level} mg/dL at {self.recorded_at}"


class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weight_readings')
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text='Weight (kg)')
    recorded_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-recorded_at']
        verbose_name_plural = 'Weight Readings'

    def __str__(self):
        return f"{self.user.username} - {self.weight} kg at {self.recorded_at}"
