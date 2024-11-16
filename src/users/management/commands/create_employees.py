from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
User = get_user_model()

import logging
logging.basicConfig(level=logging.INFO)

from .create_users import Command as USERS_Command
from users.models import Employee


class Command(BaseCommand):
    help = "creating employees"


    def handle(self, *args: Any, **options: Any) -> str | None:
        users = User.objects.all()
        if users.count() == 0:
            logging.info("There are no users to create employees objects.")
            logging.info("you could create users using this command: \"python manage.py create_users \"")

            return

        for user in users:
            if user.admin:
                print(f"User: {user.username} is already Admin!")
                continue

            emp, created = Employee.objects.get_or_create(user=user)

            if created:
                print(f"New Employee: {emp.id}-{emp.user.username}")
                continue

            print(f"Employee: {user.username} already exists.")
            
        return







