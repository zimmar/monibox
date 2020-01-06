from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from pytsm.controller.polld import PollD

class Command(BaseCommand):
    help = 'Display current time'

    def handle(self, *args, **options):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)

