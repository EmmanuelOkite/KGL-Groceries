from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator

class Produce(models.Model):
    name = models.CharField(max_length=255, validators=[
        RegexValidator(r'^[a-zA-Z0-9 ]+$', 'Only alphanumeric characters allowed.')
    ])
    type = models.CharField(max_length=100, validators=[
        MinLengthValidator(2),
        RegexValidator(r'^[a-zA-Z ]+$', 'Only alphabets allowed.')
    ])
    date = models.DateField()
    time_of_produce = models.TimeField()
    tonnage_in_kgs = models.PositiveIntegerField(validators=[MinValueValidator(100)])
    cost_per_kg = models.PositiveIntegerField(validators=[MinValueValidator(5)])
    total_cost = models.PositiveIntegerField(editable=False)
    dealer_name = models.CharField(max_length=255, validators=[
        MinLengthValidator(2),
        RegexValidator(r'^[a-zA-Z0-9 ]+$', 'Only alphanumeric characters allowed.')
    ])
    contact = models.CharField(max_length=15, validators=[
        RegexValidator(r'^\+?\d{9,15}$', 'Enter a valid phone number.')
    ])
    price_to_sell = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.total_cost = self.tonnage_in_kgs * self.cost_per_kg
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

