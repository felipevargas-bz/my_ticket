# Generated by Django 4.2.1 on 2023-05-22 14:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_customuser_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="username",
        ),
    ]
