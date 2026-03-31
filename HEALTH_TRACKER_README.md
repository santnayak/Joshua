# Health Data Tracker

A Django-based Progressive Web Application (PWA) for logging and tracking health data including blood pressure, sugar levels, and weight.

## Features

- 📊 **Dashboard**: View all your health data with interactive charts
- 🩺 **Blood Pressure Tracking**: Log systolic and diastolic readings
- 🍬 **Sugar Level Monitoring**: Track glucose levels with meal timing
- ⚖️ **Weight Management**: Monitor weight changes over time
- 📱 **PWA Support**: Install on mobile devices for app-like experience
- 🔒 **Basic Authentication**: Secure user authentication
- 🐘 **PostgreSQL Database**: Reliable data storage
- 🐳 **Docker Support**: Easy deployment with Docker and Docker Compose

## Quick Start with Docker Compose

1. Clone the repository:
```bash
git clone <repository-url>
cd Joshua
```

2. Build and start the containers:
```bash
docker-compose up --build
```

3. The application will be available at http://localhost:8000

4. Create a superuser (in a new terminal):
```bash
docker-compose exec web python manage.py createsuperuser
```

5. Login with your credentials at http://localhost:8000/login

## Manual Installation

### Prerequisites

- Python 3.12+
- PostgreSQL 15+
- pip

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file (copy from `.env.example`):
```bash
cp .env.example .env
```

3. Update the `.env` file with your database credentials and secret key.

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Collect static files:
```bash
python manage.py collectstatic
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Access the application at http://localhost:8000

## Usage

### Adding Health Data

1. Login to your account
2. Use the "Add Data" dropdown menu or quick action buttons on the dashboard
3. Fill in the form with your health readings
4. View your data on the dashboard with interactive charts

### Dashboard Features

- **7-Day Averages**: Quick stats showing average readings for the last week
- **Interactive Charts**: Visualize trends in your health data
- **Recent Readings**: View your last 10 readings for each metric
- **Time-Based Data**: All readings are timestamped for accurate tracking

### PWA Installation

On supported browsers (Chrome, Edge, Safari):
1. Visit the website
2. Look for the "Install" prompt or button
3. Follow the installation steps
4. Access the app from your home screen

## API Endpoints

- `/` - Dashboard (requires authentication)
- `/login/` - User login
- `/logout/` - User logout
- `/add-blood-pressure/` - Add blood pressure reading
- `/add-sugar-level/` - Add sugar level reading
- `/add-weight/` - Add weight reading
- `/admin/` - Django admin panel

## Technology Stack

- **Backend**: Django 4.2
- **Database**: PostgreSQL 15
- **Frontend**: Bootstrap 5, Chart.js
- **PWA**: Service Workers, Web App Manifest
- **Deployment**: Docker, Docker Compose, Gunicorn

## Development

### Running Tests

```bash
python manage.py test
```

### Making Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating Admin User

```bash
python manage.py createsuperuser
```

## Docker Commands

### Build and start services
```bash
docker-compose up --build
```

### Start services (after initial build)
```bash
docker-compose up
```

### Stop services
```bash
docker-compose down
```

### View logs
```bash
docker-compose logs -f
```

### Run migrations in Docker
```bash
docker-compose exec web python manage.py migrate
```

### Create superuser in Docker
```bash
docker-compose exec web python manage.py createsuperuser
```

## Security Notes

- Change the `SECRET_KEY` in production
- Set `DEBUG=False` in production
- Use strong passwords for database and admin accounts
- Configure `ALLOWED_HOSTS` appropriately
- Use HTTPS in production
- Regularly update dependencies

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
