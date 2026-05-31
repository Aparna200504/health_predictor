# Health Prediction System

A Django-based health prediction system that manages patient health data and predicts health risks based on medical metrics.

## Features

- **Patient Management**: Create, read, update, and delete patient records
- **Health Metrics Tracking**: Monitor glucose, hemoglobin, and cholesterol levels
- **Risk Prediction**: Analyze patient data to predict potential health risks
- **Admin Interface**: Django admin panel for data management
- **Responsive Forms**: User-friendly forms for patient data entry

## Project Structure

```
health_prediction/
├── health_prediction/          # Main project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # URL routing
│   ├── asgi.py                # ASGI configuration
│   └── wsgi.py                # WSGI configuration
├── patients/                   # Patients app
│   ├── models.py              # Patient model definition
│   ├── views.py               # Views for patient management
│   ├── forms.py               # Forms for patient input
│   ├── urls.py                # App URL routing
│   ├── admin.py               # Admin configuration
│   ├── services.py            # Business logic services
│   ├── tests.py               # Unit tests
│   ├── migrations/            # Database migrations
│   └── templates/patients/    # HTML templates
├── health_api/                # Health risk prediction API
│   ├── risk_api.py            # Risk prediction logic
│   └── requirements.txt        # API-specific requirements
├── manage.py                  # Django management script
├── db.sqlite3                 # SQLite database
└── requirements.txt           # Project dependencies
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd health_prediction
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Environment Variables

Create a `.env` file in the project root if you need custom environment variables:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
```

The project uses `python-dotenv` to load environment variables automatically.

## Running the Application

1. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

2. **Create a superuser account for admin access**:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to enter:
   - Username
   - Email
   - Password

3. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

4. **Access the application**:
   - Main site: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Using the Admin Panel

1. Navigate to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Manage patients, view health metrics, and monitor records

## API & Services

### Patient Model

Each patient record contains:
- **full_name**: Patient's full name (max 100 characters)
- **date_of_birth**: Date of birth
- **email**: Unique email address (validated)
- **glucose**: Blood glucose level (mg/dL, min 0.1)
- **haemoglobin**: Hemoglobin level (g/dL, min 0.1)
- **cholesterol**: Cholesterol level (mg/dL, min 0.1)
- **remarks**: Additional notes (optional)

### Health Risk Prediction

The system uses the `health_api/risk_api.py` module to predict health risks based on patient metrics. Check the module documentation for prediction algorithms and methods.

## Database

- **Type**: SQLite 3
- **File**: `db.sqlite3`
- **No password required** for local development

To reset the database:
```bash
python manage.py migrate --fake-initial
# or delete db.sqlite3 and run: python manage.py migrate
```

## Development

### Running Tests

```bash
python manage.py test patients
```

### Creating New Migrations

After modifying models:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Management Commands

```bash
# Shell for interactive Python with Django context
python manage.py shell

# Create an admin user
python manage.py createsuperuser

# Check for issues
python manage.py check

# Collect static files (if needed)
python manage.py collectstatic
```

## Dependencies

- **Django 4.2.0**: Web framework
- **requests 2.31.0**: HTTP library for API calls
- **python-dotenv 1.0.0**: Environment variable management

See `requirements.txt` for full dependency list.

## Troubleshooting

**Issue: "No such table" error**
- Solution: Run `python manage.py migrate`

**Issue: Static files not loading**
- Solution: Run `python manage.py collectstatic --noinput`

**Issue: Can't connect to database**
- Solution: Ensure `db.sqlite3` exists and is readable; run migrations

**Issue: Port 8000 already in use**
- Solution: Use a different port: `python manage.py runserver 8001`

## Contributing

1. Create a new branch for features
2. Make changes and test thoroughly
3. Run tests before submitting changes
4. Update documentation as needed

## License

This project is for educational purposes.

## Support

For issues or questions, check the Django documentation: https://docs.djangoproject.com/
