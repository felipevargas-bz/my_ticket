# Generated by Django 4.2.1 on 2023-05-20 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("sales", "0001_initial"),
        ("users", "0001_initial"),
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.customuser"
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="sales.event"
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="sale",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="sales.ticketsale"
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="sales.type"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="locations.location"
            ),
        ),
    ]
