from django.contrib import admin
from django.contrib.auth.models import User, Group
import platform
import django

class HSDjangoAdmin(admin.AdminSite):
    site_header = "Admin Panel"
    site_title = "Himosoft Application Admin Portal"
    index_title = "Welcome to Admin Panel"
    

    def each_context(self, request):
        context = super().each_context(request)
        context['site_header'] = self.site_header
        context['site_title'] = self.site_title
        context['index_title'] = self.index_title
        context['os'] = platform.system()
        context['python_version'] = platform.python_version()
        context['django_version'] = django.get_version()
        context['database_engine'] = str(django.db.connection.settings_dict['ENGINE']).split('.')[-1]
        context['has_ssl'] = request.is_secure()
        context['panel_version'] = '1.0.0'
        return context

class HSDjangoAdminMixin:
    """
    Mixin to add Himosoft admin functionality to existing ModelAdmin classes.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['os'] = platform.system()
        context['python_version'] = platform.python_version()
        context['django_version'] = django.get_version()
        context['database_engine'] = str(django.db.connection.settings_dict['ENGINE']).split('.')[-1]
        context['panel_version'] = '1.0.0'
        return context

# Create a default admin site instance
admin_site = HSDjangoAdmin(name='hs_django_admin')

def register_default_models():
    """Register default models with the custom admin site"""
    pass 

def get_admin_site():
    """Get the custom admin site instance"""
    return admin_site

def enable_default_admin_compatibility():
    """
    Enable compatibility with default Django admin.site.register() calls.
    This redirects all admin.site.register() calls to the custom admin site.
    """
    # Store the original register method
    original_register = admin.site.register
    
    def custom_register(model_or_iterable, admin_class=None, **options):
        """Redirect registration to custom admin site"""
        try:
            return admin_site.register(model_or_iterable, admin_class, **options)
        except admin.sites.AlreadyRegistered:
            # If already registered, just return without error
            return None
    
    # Replace the default admin site's register method
    admin.site.register = custom_register
    
    return original_register

def disable_default_admin_compatibility(original_register=None):
    """
    Disable compatibility mode and restore original admin.site.register().
    """
    if original_register:
        admin.site.register = original_register
