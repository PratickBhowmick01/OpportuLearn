# Generated by Django 4.2.7 on 2023-12-11 03:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("education", "0007_paymentuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentConfirmation",
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
                ("confirmation_code", models.CharField(max_length=255)),
                ("username", models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name="PaymentUser",
        ),
    ]
