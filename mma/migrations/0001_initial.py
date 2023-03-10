# Generated by Django 4.1.5 on 2023-01-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="mma",
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
                ("name", models.CharField(max_length=50, verbose_name="name")),
                ("nickname", models.CharField(max_length=50, verbose_name="nickname")),
                ("wins", models.IntegerField()),
                ("loses", models.IntegerField()),
                ("ties", models.IntegerField()),
            ],
        ),
    ]
