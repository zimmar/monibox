from django.core.management.base import BaseCommand

from pytsm.controller.polld import PollD


class Command(BaseCommand):
    help = 'PollDaemon Start'

    def handle(self, *args, **kwargs):

        x = PollD()
        y = x.poll()
        self.stdout.write("Daemon start.")

