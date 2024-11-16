from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
User = get_user_model()

from users.models import Admin

import logging
logging.basicConfig(level=logging.INFO)

class Command(BaseCommand):
    help = "creating admins"


    def handle(self, *args: Any, **options: Any) -> str | None:
        users = User.objects.all()
        if users.count() == 0:
            logging.info("There are no users to create admins objects.")
            logging.info("you could create users using this command: \"python manage.py create_users \"")

            return 

        for user in users:
            if user.employee:
                print(f"User: {user.username} is already Employee!")
                continue

            admin, created = Admin.objects.get_or_create(user=user)

            if created:
                print(f"New Admin: {admin.id}-{admin.user.username}")
                continue

            print(f"Admin: {user.username} already exists.")
            
        return 