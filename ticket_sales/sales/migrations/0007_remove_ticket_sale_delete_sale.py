# Generated by Django 4.2.1 on 2023-05-22 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_sale_client_alter_sale_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='sale',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
    ]
