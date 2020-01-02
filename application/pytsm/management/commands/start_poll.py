from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Start the poll service in foreground.'

    def add_arguments(self, parser):
        parser.add_argument('--start', action='store_true', help='Start the PollD Deamon in forground.')

    def handle(self, *args, **kwargs):
       if kwargs['start']:

           from application.pytsm.controller.polld import PollD
           x = PollD()
           x.poll()