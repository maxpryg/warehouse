from django.db import models

# Create your models here.
from django.core.validators import FileExtensionValidator

from django.db import models


class Truck(models.Model):
    """Base model for truck"""
    cw = models.IntegerField()
    truck_number = models.IntegerField()
    arrival_date = models.DateField()
    specification = models.FileField(null=True, blank=True,
        validators=[FileExtensionValidator(
            allowed_extensions=['xls', 'xlsx'],
            message='Supported file types are XLS and XLSX')])

    class Meta:
        ordering = ['-arrival_date']

    def __str__(self):
        return f'CW{self.cw} - Truck{self.truck_number}'


class Entry(models.Model):
    """Model for representing rows of specification.One instance for one row"""
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True,
        blank=True)
    material = models.CharField(max_length=20)
    material_description = models.CharField(max_length=30)
    quantity = models.IntegerField()
    weight = models.FloatField()
    handling_unit = models.IntegerField()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return (f'{self.material} - {self.material_description} - '
                f'{self.quantity} - {self.handling_unit}')
