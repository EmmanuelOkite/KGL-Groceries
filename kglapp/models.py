from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MinLengthValidator
from django.utils.timezone import now

class Produce(models.Model):
    PRODUCE_CHOICES = [
        ('maize', 'Maize'),
        ('beans', 'Beans'),
        ('rice', 'Rice'),
        ('cowpeas', 'Cowpeas'),
        ('g-nuts', 'Groundnuts'),
    ]

    TYPE_MAPPING = {
        'maize': 'Cereal',
        'beans': 'Grain',
        'rice': 'Cereal',
        'cowpeas': 'Legume',
        'g-nuts': 'Legume',
    }

    name = models.CharField(
        max_length=255,
        choices=PRODUCE_CHOICES,
    )
    type = models.CharField(
        max_length=100,
        editable=False
    )
    date = models.DateField(auto_now_add=True)
    time_of_produce = models.TimeField(auto_now_add=True)
    tonnage_in_kgs = models.PositiveIntegerField(validators=[MinValueValidator(100)])
    cost_per_kg = models.PositiveIntegerField(validators=[MinValueValidator(5)])
    total_cost = models.PositiveIntegerField(editable=False)
    dealer_name = models.CharField(
        max_length=255,
        validators=[
            MinLengthValidator(2),
            RegexValidator(r'^[a-zA-Z0-9 ]+$', 'Only alphanumeric characters allowed.')
        ],
    )
    contact = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?\d{9,15}$', 'Enter a valid phone number.')],
    )
    price_to_sell = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.type = self.TYPE_MAPPING.get(self.name, 'Unknown')
        self.total_cost = self.tonnage_in_kgs * self.cost_per_kg
        super().save(*args, **kwargs)
    
    def _str_(self):
        return f"{self.get_name_display()} ({self.type})"
    

class Selling(models.Model):
    produce = models.ForeignKey('Produce', on_delete=models.CASCADE)
    tonnage_in_kgs = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    amount_paid = models.PositiveIntegerField(validators=[MinValueValidator(5)])
    buyer_name = models.CharField(max_length=255, validators=[MinValueValidator(2)])
    sales_agent_name = models.CharField(max_length=255, validators=[MinValueValidator(2)])
    date_time = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        if self.produce.tonnage_in_kgs < self.tonnage_in_kgs:
            raise ValueError("Not enough stock available.")
        self.produce.tonnage_in_kgs -= self.tonnage_in_kgs
        self.produce.save()
        super().save(*args, **kwargs)