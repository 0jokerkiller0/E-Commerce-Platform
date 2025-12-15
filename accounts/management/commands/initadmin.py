from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser if it does not exist'

    def handle(self, *args, **options):
        User = get_user_model()
        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',  # Change this password after first login!
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write(self.style.SUCCESS('Successfully created superuser: admin'))
        else:
            self.stdout.write(self.style.WARNING('Superuser "admin" already exists'))
