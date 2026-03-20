"""
Management command: python manage.py create_superuser_if_none

Creates a superuser from environment variables if no superuser exists yet.
Safe to run in release phase — will not duplicate or overwrite.

Set these in Railway → Variables:
    DJANGO_SUPERUSER_USERNAME  (default: admin)
    DJANGO_SUPERUSER_EMAIL     (default: admin@redneck.co)
    DJANGO_SUPERUSER_PASSWORD  (required — set this in Railway!)
"""
import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a superuser from env vars if no superuser exists'

    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write('  · Superuser already exists — skipping')
            return

        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@redneck.co')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')

        if not password:
            self.stdout.write(self.style.WARNING(
                '  ⚠ DJANGO_SUPERUSER_PASSWORD not set — skipping superuser creation.\n'
                '    Set it in Railway → Variables to auto-create the admin account.'
            ))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(
            f'  ✓ Superuser created: {username} / {email}'
        ))
