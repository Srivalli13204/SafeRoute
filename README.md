# SafeRoute 🚨

**SafeRoute** is an Emergency Assistance Platform built with Python and Django. It helps users quickly find relevant emergency facilities such as **hospitals, police stations, and fire stations** when every minute matters.

## 🌐 Live Application

**Production:** https://saferoute-3m1p.onrender.com/

---

## ✨ Features

- 👤 User registration and authentication
- 🏥 Emergency hospital directory
- 👮 Police station directory
- 🚒 Fire station directory
- 🔍 Emergency facility search and filtering
- 🚨 Emergency assistance workflows
- 🛠️ Django administration panel
- 🗄️ PostgreSQL database
- 📱 Responsive web interface
- ☁️ Production deployment on Render
- 📦 Static file management using WhiteNoise

---

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Backend | Python, Django |
| API Support | Django REST Framework |
| Database | PostgreSQL |
| Production Server | Gunicorn |
| Static Files | WhiteNoise |
| Database Configuration | dj-database-url |
| Deployment | Render |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```text
SafeRoute/
│
├── accounts/              # User and authentication functionality
├── config/                # Django project configuration
├── core/                  # Core application functionality
├── emergency/             # Emergency facilities and workflows
├── static/                # Static assets
├── templates/             # HTML templates
│
├── manage.py              # Django management entry point
├── requirements.txt       # Python dependencies
├── build.sh               # Render build script
├── startup.sh             # Application startup script
├── render.yaml            # Render configuration
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Srivalli13204/SafeRoute.git
cd SafeRoute
```

### 2. Create a Virtual Environment

#### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Seed Emergency Facilities

```bash
python manage.py seed_facilities
```

### 6. Create an Administrator Account

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Django Admin

The Django administration panel is available at:

**https://saferoute-3m1p.onrender.com/admin/**

The admin panel can be used to manage:

- Users
- Emergency facilities
- Hospitals
- Police stations
- Fire stations
- Application data

---

## 🏥 Emergency Facilities

SafeRoute maintains a centralized directory of emergency facilities, including:

### Hospitals

Medical facilities available for emergency assistance.

### Police Stations

Police facilities available for emergency support and assistance.

### Fire Stations

Fire and rescue facilities available through the platform.

Facilities can be managed through the Django administration panel.

The project also provides a management command to initialize the facility dataset:

```bash
python manage.py seed_facilities
```

---

## 🔄 Application Flow

```text
                    ┌──────────────────┐
                    │       User       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    SafeRoute     │
                    │   Web Platform   │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
        Authentication   Facilities    Emergency
                           Search       Assistance
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                    ┌──────────────────┐
                    │   PostgreSQL     │
                    │     Database     │
                    └──────────────────┘
```

---

## ☁️ Production Deployment

SafeRoute is deployed using **Render**.

The production environment consists of:

- **GitHub** — Source code repository
- **Render Web Service** — Application hosting
- **PostgreSQL** — Production database
- **Gunicorn** — WSGI application server
- **WhiteNoise** — Static file serving

### Production Build Process

```text
Install Dependencies
        ↓
Collect Static Files
        ↓
Run Database Migrations
        ↓
Seed Emergency Facilities
        ↓
Start Gunicorn
        ↓
Application Live
```

The application is started using:

```bash
python -m gunicorn config.wsgi:application
```

---

## 🗄️ Database

SafeRoute uses **PostgreSQL** for persistent production data.

Production database configuration is supplied through environment variables.

Typical environment variables include:

```text
SECRET_KEY
DATABASE_URL
WEB_CONCURRENCY
```

Sensitive credentials should never be committed to the GitHub repository.

---

## 🔒 Security

The application follows basic production security practices:

- Production `SECRET_KEY` is stored as an environment variable.
- Database credentials are not stored in source code.
- `.env` files are excluded from version control.
- HTTPS is used for the production application.
- Django production settings are configured for the deployed environment.

---

## 📊 Deployment Architecture

```text
                  Internet
                     │
                     │ HTTPS
                     ▼
             ┌─────────────────┐
             │     Render      │
             │   Web Service   │
             └────────┬────────┘
                      │
                      │ Gunicorn
                      ▼
             ┌─────────────────┐
             │     Django      │
             │   Application   │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │   PostgreSQL    │
             │    Database     │
             └─────────────────┘
```

---

## 🔮 Future Enhancements

Potential future improvements include:

- 📍 Real-time location-based emergency facility discovery
- 🗺️ Map integration and route visualization
- 📏 Distance and estimated travel-time calculations
- 🔔 Real-time emergency notifications
- 📱 Improved mobile experience
- 👥 Advanced role-based access control
- ⚡ Caching and performance optimization
- 🧪 Automated testing
- 🔄 CI/CD pipeline
- 📊 Application monitoring and logging

---

## 📌 Project Status

**Status: Deployed and Running**

Live application:

👉 **https://saferoute-3m1p.onrender.com/**

---

## 👨‍💻 Project

**SafeRoute — Emergency Assistance Platform**

Built using **Python, Django, PostgreSQL, and Render**.

> Helping users find relevant emergency services and suitable routes when every minute matters.
