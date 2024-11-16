from typing import Iterable
from django.db import models
from django.core.exceptions import ValidationError

from users.models import Employee



class Regulator(models.Model):
    client = models.CharField(max_length=200, null=True, blank=True)
    performance = models.CharField(max_length=200, blank=True, null=True)

    is_sold = models.BooleanField(default=False)
    sold_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        if self.is_sold or self.sold_at:
            if not self.is_sold or not self.sold_at:
                raise ValidationError("You should provide both values for (\"is_sold\": boolean field) and (\"sold_at\": datetime field) ")
            
        return super().save(*args, **kwargs)


class Damage(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.id}"    
    

class Repair(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    regulator = models.ForeignKey(Regulator, on_delete=models.CASCADE)
    damage = models.ForeignKey(Damage, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        if self.name:
            return f"{self.name}"
        return super().__str__()



