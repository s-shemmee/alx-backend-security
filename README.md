# ALX Backend Security: IP Tracking Project

## Overview
This Django project tracks and analyzes incoming IP addresses for security and analytics purposes. It features request logging, IP blocking, suspicious activity detection, rate limiting, and public API documentation.

## Features
- IP logging and analytics
- Blacklist/block suspicious IPs
- Rate limiting (via django_ratelimit)
- Geolocation lookup
- Suspicious activity detection
- Admin interface
- Public API documentation (Swagger)
- Ready for deployment on PythonAnywhere

## Deployment
Live site: [https://shemmee.pythonanywhere.com/](https://shemmee.pythonanywhere.com/)

## API Documentation
Swagger UI is available at: [https://shemmee.pythonanywhere.com/swagger/](https://shemmee.pythonanywhere.com/swagger/)

## Environment Variables
Set sensitive values (API keys, DB credentials) as environment variables on your server. Do not hardcode secrets in `settings.py`.

## Celery & RabbitMQ
- Celery and RabbitMQ are required for background tasks.
- PythonAnywhere free tier does not support RabbitMQ/Celery workers. For full support, use a paid plan or another host (Render, Heroku, AWS).

## Setup Instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/s-shemmee/alx-backend-security.git
   cd alx-backend-security
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install django_ratelimit drf-yasg
   ```
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run the server:
   ```bash
   python manage.py runserver
   ```

## Manual QA Review
- All features are deployed and tested.
- See `/swagger/` for API docs.
- See `/login/` and `/` for main endpoints.

## License
MIT
