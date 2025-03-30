from apscheduler.schedulers.background import BackgroundScheduler
from .services_functions import test
scheduler = BackgroundScheduler()

def schedule_jobs():
    scheduler.add_job(test.test_1, 'cron', minute='*/1')
    scheduler.add_job(test.test_2, 'cron', minute='*/1', second='*/30')
    scheduler.start()
