from django.contrib import admin
from django.contrib.auth.models import User, Group
import platform
import django
from django.conf import settings



class HSDjangoAdmin(admin.AdminSite):
    site_header = getattr(settings, "ADMIN_SITE_HEADER", "Admin Panel")
    site_title = getattr(settings, "ADMIN_SITE_TITLE", "Admin Portal")
    index_title = getattr(settings, "ADMIN_INDEX_TITLE", "Welcome to Admin Panel")
    logo_url = getattr(settings, "ADMIN_LOGO_URL", "https://himosoft.com.bd/shortlogo.png")
    footer_enabled = getattr(settings, "ADMIN_FOOTER_ENABLED", True)
 

    def each_context(self, request):
        context = super().each_context(request)
        context['site_header'] = self.site_header
        context['site_title'] = self.site_title
        context['index_title'] = self.index_title
        context['logo_url'] = self.logo_url
        context['footer_enabled'] = self.footer_enabled
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
hs_admin= HSDjangoAdmin(name='hs_django_admin')

def register_default_models():
    """Register default models with the custom admin site"""
    pass 

def get_admin_site():
    """Get the custom admin site instance"""
    return hs_admin

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
            return hs_admin.register(model_or_iterable, admin_class, **options)
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
