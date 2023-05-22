from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Crea dos grupos de permisos"

    def handle(self, *args, **options):
        clientes = Group.objects.create(name="Clientes")
        administradores = Group.objects.create(name="Administradores")

        admin_permissions = [
            "add_city",
            "change_city",
            "delete_city",
            "view_city",
            "add_country",
            "change_country",
            "delete_country",
            "view_country",
            "add_department",
            "change_department",
            "delete_department",
            "view_department",
            "add_location",
            "change_location",
            "delete_location",
            "view_location",
            "add_event",
            "change_event",
            "delete_event",
            "view_event",
            "add_ticket",
            "change_ticket",
            "delete_ticket",
            "view_ticket",
            "add_type",
            "change_type",
            "delete_type",
            "view_type",
            "add_session",
            "change_session",
            "delete_session",
            "view_session",
            "add_customuser",
            "change_customuser",
            "delete_customuser",
            "view_customuser",
        ]

        client_permissions = [
            "view_city",
            "view_country",
            "view_department",
            "view_location",
            "view_event",
            "add_ticket",
            "change_ticket",
            "delete_ticket",
            "view_ticket",
            "view_type",
            "add_session",
            "change_session",
            "delete_session",
            "view_session",
            "add_customuser",
            "change_customuser",
            "delete_customuser",
            "view_customuser",
        ]

        for permission in admin_permissions:
            perm = Permission.objects.get(codename=permission)
            administradores.permissions.add(perm)

        for permission in client_permissions:
            perm = Permission.objects.get(codename=permission)
            clientes.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS("Grupos creados exitosamente"))
