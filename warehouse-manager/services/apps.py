from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def start_scheduler():
    if not scheduler.running:
        print("Starting scheduler...")
        scheduler.start()

class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
    
    
    def ready(self):
        import services.signals
        from services.jobs import sync_jobs_with_db
        start_scheduler()
        sync_jobs_with_db()