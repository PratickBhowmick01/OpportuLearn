# Generated by Django 4.2.7 on 2023-12-11 03:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("education", "0006_delete_answer"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentUser",
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
                ("username", models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
