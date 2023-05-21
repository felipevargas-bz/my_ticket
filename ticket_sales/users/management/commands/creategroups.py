from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Crea dos grupos de permisos"

    def handle(self, *args, **options):
        clientes = Group.objects.create(name="Clientes")
        administradores = Group.objects.create(name="Administradores")
