# Generated by Django 5.1.7 on 2025-04-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_emaillist_first_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inquiry",
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
                ("email_of_sender", models.EmailField(max_length=100)),
                ("content", models.CharField(max_length=1000)),
            ],
        ),
    ]
