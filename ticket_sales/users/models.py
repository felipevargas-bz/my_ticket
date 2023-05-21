from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


# Create your models here.


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')

    @property
    def is_client(self):
        return self.groups.filter(name='Clientes').exists()

    @property
    def is_admin(self):
        return self.groups.filter(name='Administradores').exists()
