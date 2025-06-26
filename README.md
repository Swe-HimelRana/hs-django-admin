# HS Django Admin

A customizable Django admin interface with enhanced styling and system information display.

## Features

- Custom admin site with modern design
- System information display (OS, Python version, Django version, database engine)
- SSL status indicator
- Custom CSS styling with dark theme
- Responsive design
- Full compatibility with default Django admin.site.register()
- Grid background pattern
- Modern UI components

## Installation

### From PyPI

```bash
pip install hs-django-admin
```

### From source

```bash
git clone https://github.com/Swe-HimelRana/hs-django-admin.git
cd hs-django-admin
pip install -e .
```

## Quick Start

1. Add `'hs_django_admin'` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    'hs_django_admin', # it must be at top
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ... your other apps
]
```

2. Update your main `urls.py`:

```python
from django.urls import path
from hs_django_admin.admin import hs_admin

urlpatterns = [
    path('admin/', hs_admin.urls),
    # ... your other URL patterns
]
```

3. Run migrations and collect static files:

```bash
python manage.py migrate
python manage.py collectstatic
```

4. Start your development server:

```bash
python manage.py runserver
```

5. Visit `http://localhost:8000/admin/` to see your custom admin interface!

## Usage

### Model Registration

The package is fully compatible with Django's default admin registration:

```python
# your_app/admin.py
from django.contrib import admin
from .models import Product

# This automatically works with the custom admin site!
admin.site.register(Product)
```

### Advanced Configuration

For more advanced usage, see the [full documentation](https://github.com/Swe-HimelRana/hs-django-admin#readme).

## Requirements

- Python 3.8+
- Django 5.2+

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/Swe-HimelRana/hs-django-admin/issues) on GitHub. 