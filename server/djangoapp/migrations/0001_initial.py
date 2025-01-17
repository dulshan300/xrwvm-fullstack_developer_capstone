# Generated by Django 5.1.4 on 2025-01-01 16:16

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarMake",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="CarModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "type",
                    models.CharField(
                        choices=[
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
                        ],
                        default="Sedan",
                        max_length=100,
                    ),
                ),
                (
                    "year",
                    models.IntegerField(
                        default=2024,
                        validators=[
                            django.core.validators.MinValueValidator(2015),
                            django.core.validators.MaxValueValidator(2024),
                        ],
                    ),
                ),
                (
                    "car_make",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djangoapp.carmake",
                    ),
                ),
            ],
        ),
    ]
