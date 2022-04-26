from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserProfileManager(BaseUserManager):
    """ Manager para perfiles de usuario. """

    def create_user(self, name, email, password=None):
        """ Crear un nuevo perfil de usuario. """
        if not email:
            raise ValueError("Usuario debe tener un email")

        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo para los usuarios del sistema """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """ Obtener nombre completo """
        return self.name

    def get_short_name(self):
        """ Obtener nombre corto """
        return self.name

    def __str__(self):
        """ Return cadena representando el usuario """
        return self.email
