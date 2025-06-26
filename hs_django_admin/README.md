# Himosoft Django Admin

A customizable Django admin interface with enhanced styling and system information display.

## Features

- Custom admin site with Himosoft branding
- System information display (OS, Python version, Django version, database engine)
- SSL status indicator
- Custom CSS styling
- Responsive design
- **NEW: Full compatibility with default Django admin.site.register()**

## Installation

### Option 1: Copy the app to your project

1. Copy the `hs_django_admin` directory to your Django project
2. Add `'hs_django_admin'` to your `INSTALLED_APPS` in `settings.py`
3. Update your main `urls.py` to use the custom admin site

### Option 2: Use as a reusable app

1. Add `'hs_django_admin'` to your `INSTALLED_APPS` in `settings.py`
2. Import and use the custom admin site in your `urls.py`

## Usage

### Basic Integration

In your main `urls.py`:

```python
from django.urls import path
from hs_django_admin.admin import get_admin_site

urlpatterns = [
    path('admin/', get_admin_site().urls),
    # ... your other URL patterns
]
```

### Model Registration (Multiple Options)

#### Option 1: Use default Django admin.site.register() (Recommended)
```python
# your_app/admin.py
from django.contrib import admin
from .models import Product

# This automatically works with the custom admin site!
admin.site.register(Product)
```

#### Option 2: Use the custom admin site directly
```python
from hs_django_admin.admin import get_admin_site
from your_app.models import YourModel

admin_site = get_admin_site()
admin_site.register(YourModel)
```

#### Option 3: Import the admin site instance directly
```python
from hs_django_admin.admin import admin_site
from your_app.models import YourModel

admin_site.register(YourModel)
```

#### Option 4: Create your own admin site instance
```python
from hs_django_admin.admin import HSDjangoAdmin
from your_app.models import YourModel

custom_admin = HSDjangoAdmin(name='my_custom_admin')
custom_admin.site_header = "My Custom Admin"
custom_admin.site_title = "My Custom Admin Portal"
custom_admin.register(YourModel)
```

### Advanced ModelAdmin Usage

#### Using the Mixin
```python
from django.contrib import admin
from hs_django_admin.admin import HSDjangoAdminMixin
from .models import Product

class ProductAdmin(HSDjangoAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
```

#### Custom Admin Classes
```python
from hs_django_admin.admin import get_admin_site
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']

admin_site = get_admin_site()
admin_site.register(Product, ProductAdmin)
```

### Manual Compatibility Control

If you need to control when compatibility is enabled:

```python
from hs_django_admin.admin import enable_default_admin_compatibility, disable_default_admin_compatibility

# Enable compatibility
original_register = enable_default_admin_compatibility()

# Your admin registrations here
from django.contrib import admin
from .models import Product
admin.site.register(Product)

# Disable compatibility (optional)
disable_default_admin_compatibility(original_register)
```

## Configuration

The app automatically provides:
- System information in the admin context
- Custom styling via static files
- Enhanced admin templates
- **Automatic compatibility with default admin.site.register()**

No additional configuration is required for basic functionality.

## Dependencies

- Django 5.2+ (tested with Django 5.2.3)
- No additional Python packages required

## Notes

- The app includes a `TestModel` for demonstration purposes
- Custom admin templates override the default Django admin templates
- Static files are automatically collected when running `python manage.py collectstatic`
- **Default admin compatibility is automatically enabled when the app loads**
- All existing `admin.site.register()` calls will work without modification 