from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return str(self.name)


class CarModel(models.Model):
    """_summary_

    Returns:
        _type_: _description_
    """

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ("Sedan", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "WAGON"),
        ("HATCHBACK", "HATCHBACK"),
        ("TRUCK", "TRUCK"),
        ("VAN", "VAN"),
        ("COUPE", "COUPE"),
        ("CONVERTIBLE", "CONVERTIBLE"),
        ("SPORTS CAR", "SPORTS CAR"),
        ("HYBRID", "HYBRID"),
        ("ELECTRIC", "ELECTRIC"),
    ]

    type = models.CharField(max_length=100, choices=CAR_TYPES, default="Sedan")
    year = models.IntegerField(
        default=2024, validators=[MinValueValidator(2015), MaxValueValidator(2024)]
    )

    def __str__(self):
        return str(self.name)
