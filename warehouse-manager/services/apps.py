from django.apps import AppConfig
from .shedule_jobs import schedule_jobs


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'

    schedule_jobs()
