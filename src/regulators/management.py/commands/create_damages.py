from typing import Any
from django.core.management.base import BaseCommand

from regulators.models import Damage

class Command(BaseCommand):
    help = "creating damages"

    def handle(self, *args: Any, **options: Any) -> str | None:
        damages = [
            "Dead battery",
            "Dimming or flickering lights",
            "Voltage stabilizer failures",
            "Voltage spikes damaging electrical parts",
            "Stalling engine",
            "Bulbs in headlights or taillights burning out prematurely",
            "Battery warning lights",
            "Malfunctioning instrument cluster",

        ]


        for damage_name in damages:
            obj, created = Damage.objects.get_or_create(name=damage_name)
            if created:
                print(f"New Damage: {obj.pk}")
                continue
            print(f"Damage: '{damage_name}' already exists")

        return
    


    