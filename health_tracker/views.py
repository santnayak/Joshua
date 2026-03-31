from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Avg
from django.utils import timezone
from datetime import timedelta
from .models import BloodPressure, SugarLevel, Weight
from .forms import BloodPressureForm, SugarLevelForm, WeightForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'health_tracker/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    # Get recent readings for the current user
    blood_pressure_readings = BloodPressure.objects.filter(user=request.user)[:30]
    sugar_level_readings = SugarLevel.objects.filter(user=request.user)[:30]
    weight_readings = Weight.objects.filter(user=request.user)[:30]
    
    # Calculate averages for the last 7 days
    seven_days_ago = timezone.now() - timedelta(days=7)
    
    avg_systolic = BloodPressure.objects.filter(
        user=request.user, 
        recorded_at__gte=seven_days_ago
    ).aggregate(Avg('systolic'))['systolic__avg']
    
    avg_diastolic = BloodPressure.objects.filter(
        user=request.user,
        recorded_at__gte=seven_days_ago
    ).aggregate(Avg('diastolic'))['diastolic__avg']
    
    avg_glucose = SugarLevel.objects.filter(
        user=request.user,
        recorded_at__gte=seven_days_ago
    ).aggregate(Avg('glucose_level'))['glucose_level__avg']
    
    avg_weight = Weight.objects.filter(
        user=request.user,
        recorded_at__gte=seven_days_ago
    ).aggregate(Avg('weight'))['weight__avg']
    
    context = {
        'blood_pressure_readings': blood_pressure_readings,
        'sugar_level_readings': sugar_level_readings,
        'weight_readings': weight_readings,
        'avg_systolic': round(avg_systolic, 1) if avg_systolic else None,
        'avg_diastolic': round(avg_diastolic, 1) if avg_diastolic else None,
        'avg_glucose': round(avg_glucose, 1) if avg_glucose else None,
        'avg_weight': round(avg_weight, 2) if avg_weight else None,
    }
    
    return render(request, 'health_tracker/dashboard.html', context)


@login_required
def add_blood_pressure(request):
    if request.method == 'POST':
        form = BloodPressureForm(request.POST)
        if form.is_valid():
            blood_pressure = form.save(commit=False)
            blood_pressure.user = request.user
            blood_pressure.save()
            messages.success(request, 'Blood pressure reading added successfully!')
            return redirect('dashboard')
    else:
        form = BloodPressureForm()
    
    return render(request, 'health_tracker/add_blood_pressure.html', {'form': form})


@login_required
def add_sugar_level(request):
    if request.method == 'POST':
        form = SugarLevelForm(request.POST)
        if form.is_valid():
            sugar_level = form.save(commit=False)
            sugar_level.user = request.user
            sugar_level.save()
            messages.success(request, 'Sugar level reading added successfully!')
            return redirect('dashboard')
    else:
        form = SugarLevelForm()
    
    return render(request, 'health_tracker/add_sugar_level.html', {'form': form})


@login_required
def add_weight(request):
    if request.method == 'POST':
        form = WeightForm(request.POST)
        if form.is_valid():
            weight = form.save(commit=False)
            weight.user = request.user
            weight.save()
            messages.success(request, 'Weight reading added successfully!')
            return redirect('dashboard')
    else:
        form = WeightForm()
    
    return render(request, 'health_tracker/add_weight.html', {'form': form})
