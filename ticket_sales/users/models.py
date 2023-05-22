from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name):

        if not email:
            raise ValueError('El email debe ser proporcionado.')

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email, password, first_name, last_name)
        user.is_staff = True
        user.is_superuser = True
        user.groups.add(Group.objects.get(name='Administradores'))
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return str(self.pk) + ' - ' + self.email

    @property
    def is_client(self):
        return self.groups.filter(name='Clientes').exists()

    @property
    def is_admin(self):
        return self.groups.filter(name='Administradores').exists()
