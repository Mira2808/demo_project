from django.apps import AppConfig
# from django.contrib.auth.models import User

class DemoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demoapp'

    def ready(self):
        import demoapp.signals

