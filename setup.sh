#!/bin/bash

# Health Tracker Setup Script

echo "=========================================="
echo "Health Data Tracker Setup"
echo "=========================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is available
if ! docker compose version &> /dev/null; then
    echo "Error: Docker Compose is not available. Please install Docker Compose v2."
    exit 1
fi

echo "✓ Docker and Docker Compose are installed"
echo ""

# Build and start containers
echo "Building and starting containers..."
docker compose up --build -d

# Wait for database to be ready
echo "Waiting for database to be ready..."
sleep 10

# Run migrations
echo "Running database migrations..."
docker compose exec -T web python manage.py migrate

# Create superuser
echo ""
echo "=========================================="
echo "Creating Admin User"
echo "=========================================="
echo ""
echo "Default credentials will be created:"
echo "  Username: admin"
echo "  Password: admin123"
echo ""
read -p "Press Enter to create admin user or Ctrl+C to cancel..."

echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | docker compose exec -T web python manage.py shell

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Your Health Tracker is now running!"
echo ""
echo "Access the application at: http://localhost:8000"
echo "Login with:"
echo "  Username: admin"
echo "  Password: admin123"
echo ""
echo "To view logs: docker compose logs -f"
echo "To stop: docker compose down"
echo ""
echo "IMPORTANT: Change the admin password after first login!"
echo ""
