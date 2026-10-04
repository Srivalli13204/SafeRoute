SafeRoute

SafeRoute is an Emergency Assistance Platform built with Python and Django. It helps users find relevant emergency facilities such as hospitals, police stations, and fire stations, with the goal of making emergency-service discovery faster and easier when time matters.

Live Application

Production: https://saferoute-3m1p.onrender.com/

Key Features

User registration and authentication

Emergency facility directory

Hospitals, police stations, and fire stations

Facility search and filtering

Emergency assistance workflows

Django administration panel for managing facilities and users

PostgreSQL database for persistent production data

Responsive web interface

Production deployment on Render

Static-file handling with WhiteNoise

Technology Stack

Layer

Technology

Backend

Python, Django

API/Framework Support

Django REST Framework

Database

PostgreSQL

Production Server

Gunicorn

Static Files

WhiteNoise

Database Configuration

dj-database-url

Deployment

Render

Version Control

Git & GitHub

Project Structure

SafeRoute/
├── accounts/              # User/account functionality
├── config/                # Django project configuration
├── core/                  # Core application functionality
├── emergency/             # Emergency facilities and emergency workflows
├── static/                # Static assets
├── templates/             # HTML templates
├── manage.py               # Django management entry point
├── requirements.txt        # Python dependencies
├── build.sh                # Render build script
├── startup.sh              # Application startup script
├── render.yaml             # Render configuration
└── .gitignore

Local Development

1. Clone the repository

git clone https://github.com/Srivalli13204/SafeRoute.git
cd SafeRoute

2. Create a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

macOS/Linux:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Apply migrations

python manage.py migrate

5. Seed emergency facilities

python manage.py seed_facilities

6. Create an admin user

python manage.py createsuperuser

7. Start the development server

python manage.py runserver

The application will normally be available at:

http://127.0.0.1:8000/

Django Admin

The administration interface is available at:

https://saferoute-3m1p.onrender.com/admin/

The admin panel can be used to manage application data, including emergency facilities and users.

Production Deployment

SafeRoute is deployed on Render.

The production deployment uses:

GitHub as the source repository

Render Web Service for hosting

PostgreSQL for the production database

Gunicorn as the WSGI application server

WhiteNoise for static files

Environment variables for production configuration

Build Process

The production build performs the following steps:

Install dependencies
        ↓
Collect static files
        ↓
Run database migrations
        ↓
Seed emergency facilities
        ↓
Start Gunicorn

The production application is started with:

python -m gunicorn config.wsgi:application

Database

The application uses PostgreSQL in production. Database configuration is supplied through environment variables rather than hard-coding production database credentials in the source code.

Typical production configuration includes:

SECRET_KEY
DATABASE_URL
WEB_CONCURRENCY

Sensitive values should never be committed to GitHub.

Security Considerations

For production deployments:

Keep SECRET_KEY in environment variables.

Never commit .env files or database credentials.

Keep production secrets outside the source repository.

Use HTTPS in production.

Keep dependencies updated.

Review Django ALLOWED_HOSTS and CSRF settings before production changes.

Emergency Facilities

SafeRoute maintains an emergency-facility directory that can include:

Hospitals

Police stations

Fire stations

Facilities can be managed through the Django administration panel. The project also includes a management command for initializing the facility dataset:

python manage.py seed_facilities

Application Flow

User
  │
  ▼
SafeRoute Web Application
  │
  ├── Authentication
  │
  ├── Emergency Facility Search
  │       ├── Hospitals
  │       ├── Police Stations
  │       └── Fire Stations
  │
  └── Emergency Assistance
          │
          ▼
      PostgreSQL Database

Deployment Architecture

                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │ HTTPS
                               ▼
                    ┌─────────────────────┐
                    │       Render        │
                    │     Web Service     │
                    └──────────┬──────────┘
                               │
                         Gunicorn/Django
                               │
                               ▼
                    ┌─────────────────────┐
                    │     PostgreSQL      │
                    │      Database       │
                    └─────────────────────┘

Future Enhancements

Potential improvements include:

Real-time location-based facility discovery

Map integration and route visualization

Distance and estimated travel-time calculations

Real-time emergency-service availability

Notifications and alerts

Improved role-based access control

Monitoring and application logging

Automated testing and CI/CD

Caching and performance optimization

Containerized deployment

Project Status

Status: Deployed and running on Render.

The production application is available at:

https://saferoute-3m1p.onrender.com/

SafeRoute — Emergency Assistance Platform
