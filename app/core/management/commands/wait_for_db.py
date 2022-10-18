
"""
Django commands to wait for the database to be avalable.
"""
import time
from psycopg2 import OperationalError as PsyCopg2opError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""
    def handle(self, *args, **option):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (PsyCopg2opError, OperationalError):
                self.stdout.write('Database unavilable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
