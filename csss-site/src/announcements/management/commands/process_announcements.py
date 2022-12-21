from django.core.management.base import BaseCommand

from announcements.views.commands.process_announcements.process_announcements import run_job
from csss.setup_logger import Loggers

SERVICE_NAME = "process_announcements"


class Command(BaseCommand):
    help = "process the latest new emails and manual announcements and determines which to display"

    def add_arguments(self, parser):
        parser.add_argument(
            '--poll_email',
            action='store_true',
            default=False,
            help="pull the latest emails from gmail"
        )

    def handle(self, *args, **options):
        logger = Loggers.get_logger(logger_name=SERVICE_NAME)
        logger.info(options)
        run_job(poll_email=options['poll_email'], use_cron_logger=False)
        Loggers.remove_logger(logger_name=SERVICE_NAME)
