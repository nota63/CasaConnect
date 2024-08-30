from django.apps import AppConfig


class BlgsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blgs'

    def ready(self):
        import blgs.signals

