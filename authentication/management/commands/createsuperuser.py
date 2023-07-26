from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os 


class Command(BaseCommand): 
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            User.objects.create_superuser(
                username=os.environ.get('ADMIN_USERNAME'),
                email=os.environ.get('ADMIN_EMAIL'),
                password=os.environ.get('ADMIN_PASSWORD')
            )
            self.stdout.write(self.style.SUCCESS('Successfully created new Admin'))
        else:
            self.stdout.write(self.style.SUCCESS('Admin already exists'))