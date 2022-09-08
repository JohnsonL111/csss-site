import importlib
import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management import BaseCommand

from csss.models import CronJob
from csss.views.crons.Constants import CRON_JOB_MAPPING

logger = logging.getLogger('csss_site')


class Command(BaseCommand):

    def handle(self, **options):
        print("setting up cron service")
        scheduler = BlockingScheduler()
        cron_jobs = CronJob.objects.all()
        for cron_job in cron_jobs:
            logger.info(f"[csss/cron_service.py cron()] adding job {cron_job.job_name} to the scheduler")
            file_name = CRON_JOB_MAPPING[cron_job.job_name]['file_name']
            class_name = CRON_JOB_MAPPING[cron_job.job_name]['class_name']
            scheduler.add_job(
                getattr(
                    importlib.import_module(file_name),
                    class_name
                ).run_job,
                CronTrigger.from_crontab(cron_job.schedule)
            )
            logger.info(f"[csss/cron_service.py cron()] job {cron_job.job_name} added to the scheduler")
        # scheduler.add_job(
        #     func=the_class.theClass.cron_job_2, minutes=1, trigger='interval'
        # )
        print("starting cron service")
        scheduler.start()
