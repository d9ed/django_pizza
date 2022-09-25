from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'This commands prints "that commands is working"'

    def handle(self, *args, **kwargs):
        print('that command is working')