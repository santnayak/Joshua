# Joshua - Health Data Tracker

A Django-based Progressive Web Application (PWA) for tracking health data including blood pressure, sugar levels, and weight.

## 🚀 Quick Start

The easiest way to get started is using the setup script:

```bash
./setup.sh
```

This will:
- Build and start Docker containers
- Run database migrations
- Create an admin user (username: `admin`, password: `admin123`)
- Start the application at http://localhost:8000

## 📋 Requirements

- Docker
- Docker Compose v2

## ✨ Features

- **Blood Pressure Tracking**: Log systolic and diastolic readings
- **Sugar Level Monitoring**: Track glucose levels with meal timing
- **Weight Management**: Monitor weight changes over time
- **Interactive Dashboard**: View all health data with charts and statistics
- **7-Day Averages**: See average readings for the last week
- **Progressive Web App**: Install on mobile devices for app-like experience
- **Secure Authentication**: Basic Django authentication
- **PostgreSQL Database**: Reliable data storage
- **Docker Support**: Easy deployment with Docker Compose

## 📚 Documentation

For detailed documentation, see [HEALTH_TRACKER_README.md](HEALTH_TRACKER_README.md)

## 🧪 Testing

Run tests inside the Docker container:

```bash
docker compose exec web python manage.py test
```

All 9 tests should pass.

## 🔒 Security

- ✅ No security vulnerabilities detected (CodeQL verified)
- ✅ Timezone-aware datetime handling
- ✅ CORS protection configured
- ✅ Secure password storage with Django's authentication system

## 📸 Screenshots

See the PR for application screenshots.

## 🛠️ Technology Stack

- **Backend**: Django 4.2, Python 3.12
- **Database**: PostgreSQL 15
- **Frontend**: Bootstrap 5, Chart.js
- **Deployment**: Docker, Docker Compose, Gunicorn
- **PWA**: Service Workers, Web App Manifest

## 📝 License

See LICENSE file for details.

