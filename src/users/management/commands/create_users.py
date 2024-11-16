from typing import Any
from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "creating users"

    def handle(self, *args: Any, **options: Any) -> str | None:
        """Creating super user"""
        if not User.objects.filter(username="osama").exists():
            User.objects.create_superuser(username='osama', password="admin")
            print("Superuser Created.")

        users = [
            {'username': 'ahmad'},
            {'username': 'zavier'},
            {'username': 'shafiq'},
            {'username': 'hadi'},
            {'username': 'salam'},
            {'username': 'omar'},
            {'username': 'amina'},
            {'username': 'sara'},
            {'username': 'tariq'},
            {'username': 'ibrahim'},
            {'username': 'rana'},
            {'username': 'khaled'},
            {'username': 'samira'},
            {'username': 'leila'},
            {'username': 'karim'},
            {'username': 'mansour'},
            {'username': 'rashid'},
            {'username': 'yusuf'},
            {'username': 'hamza'},
            {'username': 'amir'},
            {'username': 'layla'},
            {'username': 'hana'},
            {'username': 'tamer'},
            {'username': 'najwa'},
            {'username': 'jamil'},
            {'username': 'farida'},
            {'username': 'lina'},
            {'username': 'adil'},
            {'username': 'samih'},
            {'username': 'aziz'},
            {'username': 'hakim'},
        ]

        for user in users:
            new_user, created = User.objects.get_or_create(
                **user,
            )
            
            if created:
                new_user.set_password('test')
                new_user.save()
                print(f"New User :{new_user.id}-{new_user.username}.")
                continue

            print(f"User: {new_user.username} already exists.")



        return super().handle(*args, **options)