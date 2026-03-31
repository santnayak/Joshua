from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import BloodPressure, SugarLevel, Weight


class HealthTrackerModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
    
    def test_blood_pressure_creation(self):
        bp = BloodPressure.objects.create(
            user=self.user,
            systolic=120,
            diastolic=80,
            notes='Test reading'
        )
        self.assertEqual(bp.systolic, 120)
        self.assertEqual(bp.diastolic, 80)
        self.assertEqual(bp.user, self.user)
    
    def test_sugar_level_creation(self):
        sugar = SugarLevel.objects.create(
            user=self.user,
            glucose_level=100.5,
            meal_timing='fasting'
        )
        self.assertEqual(float(sugar.glucose_level), 100.5)
        self.assertEqual(sugar.meal_timing, 'fasting')
    
    def test_weight_creation(self):
        weight = Weight.objects.create(
            user=self.user,
            weight=70.5
        )
        self.assertEqual(float(weight.weight), 70.5)


class HealthTrackerViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
    
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')
    
    def test_login_required_for_dashboard(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_dashboard_with_authenticated_user(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')
    
    def test_add_blood_pressure_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('add_blood_pressure'), {
            'systolic': 120,
            'diastolic': 80,
            'notes': 'Test'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(BloodPressure.objects.count(), 1)
    
    def test_add_sugar_level_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('add_sugar_level'), {
            'glucose_level': 100,
            'meal_timing': 'fasting',
            'notes': 'Test'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(SugarLevel.objects.count(), 1)
    
    def test_add_weight_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('add_weight'), {
            'weight': 70.5,
            'notes': 'Test'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Weight.objects.count(), 1)
