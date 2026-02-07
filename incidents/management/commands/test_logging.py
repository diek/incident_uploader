# incidents/management/commands/test_logging.py
import logging

from django.core.management.base import BaseCommand

logger = logging.getLogger("incidents")


class Command(BaseCommand):
    help = "Test logging configuration"

    def handle(self, *args, **options):
        logger.debug("This is a DEBUG message")
        logger.info("This is an INFO message")
        logger.warning("This is a WARNING message")
        logger.error("This is an ERROR message")
        logger.critical("This is a CRITICAL message")

        self.stdout.write(
            self.style.SUCCESS("Check logs/django.log and logs/django_error.log")
        )
