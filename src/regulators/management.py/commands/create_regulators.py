from typing import Any
from django.core.management.base import BaseCommand

from regulators.models import Regulator

class Command(BaseCommand):
    help = "creating regulators"


    def handle(self, *args: Any, **options: Any) -> str | None:
        
        for _ in range(10):
            Regulator.objects.create()

        return 