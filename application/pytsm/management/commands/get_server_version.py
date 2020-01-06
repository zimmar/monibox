from django.core.management.base import BaseCommand

from pytsm.controller.polld import PollD

class Command(BaseCommand):
    help = 'TSM Server version'

    def add_arguments(self, parser):
        parser.add_argument('servername', nargs='+', type=str, help='Servername')

    def handle(self, *args, **kwargs):
        servernames = kwargs['servername']

        for server in servernames:
            try:
                x=PollD()
                y = x.get_server_version(server)
                self.stdout.write("Server {} has the version {}".format(server, y))
            except:
                self.stdout.write("Server {} are not reached.".format(server))