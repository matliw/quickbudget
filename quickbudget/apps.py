from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "quickbudget"

    def ready(self):
        import quickbudget.receivers
