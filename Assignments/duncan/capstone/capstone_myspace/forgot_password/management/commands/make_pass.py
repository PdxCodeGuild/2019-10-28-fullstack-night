# blockbuster/users/management/commands/make_states.py

from django.core.management.base import BaseCommand, CommandError
from forgot_password.models import FakePass

class Command(BaseCommand):

    def handle(self, *args, **options):
        fake_pass_list = ['password', '123pass', '0000', '12345', 'qwert', 'duncan', 'abc123', '666']
        for fake_pass in fake_pass_list:
            FakePass.objects.get_or_create(text=fake_pass)