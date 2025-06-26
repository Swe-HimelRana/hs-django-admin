from django.apps import AppConfig


class HsDjangoAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hs_django_admin'
    
    def ready(self):
        """Register default models when the app is ready"""
        try:
            from .admin import register_default_models, enable_default_admin_compatibility
            
            # Register default models (only TestModel, not User/Group)
            register_default_models()
            
            # Enable compatibility with default admin.site.register()
            enable_default_admin_compatibility()
            
        except ImportError:
            pass  # Models might not exist in other projects
        except Exception:
            # If there are any other errors, just continue
            pass
