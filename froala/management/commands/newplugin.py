from django.conf import settings
from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """A simple management command which clears the site-wide cache."""

    def add_arguments(self, parser):
        parser.add_argument('module', nargs='1')
        parser.add_argument('plugin', nargs='1')

    def handle(self, *args, **kwargs):
        modules = [
            'contents',

        ]
        if kwargs['module'] not in modules:
            raise CommandError('Wrong module {}'.format(",".join(modules)))


