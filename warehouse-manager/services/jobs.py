from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.utils.timezone import now
from services.models import ServiceConfig, ServiceFunction

from services.apps import scheduler

def execute_service(service_id):
    """
    Execute a service dynamically by looking it up in the database.
    """
    try:
        service = ServiceConfig.objects.get(id=service_id, enabled=True)
        function_to_run = ServiceFunction.get_function(service.function)
        
        if function_to_run:
            function_to_run(**service.get_arguments())
            service.last_run = now()
            service.save()
    except ServiceConfig.DoesNotExist:
        pass  # If the service was deleted, ignore it

def sync_jobs_with_db():
    """
    Sync APScheduler jobs with the ServiceConfig database table.
    """
    existing_jobs = {job.id for job in scheduler.get_jobs()}
    db_jobs = {str(config.id): config for config in ServiceConfig.objects.filter(enabled=True)}

    # Remove jobs that no longer exist in DB
    for job_id in existing_jobs - db_jobs.keys():
        print(f"Removing job {job_id}")
        scheduler.remove_job(job_id)

    # Add or update jobs
    for service_id, config in db_jobs.items():
        trigger = CronTrigger.from_crontab(config.schedule)

        if service_id in existing_jobs:
            print(f"Rescheduling job {service_id}")
            scheduler.reschedule_job(service_id, trigger=trigger)
        else:
            print(f"Adding job {service_id}")
            scheduler.add_job(execute_service, trigger=trigger, id=service_id, args=[service_id])
