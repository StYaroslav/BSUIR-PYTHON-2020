from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import CustomUserManager


class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    patronymic = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(default=date.today)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.patronymic

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(blank=True, null=True)

    FIRST = "First category"
    SECOND = "Second category"
    HIGHEST = "Highest category"
    QUALIFICATION_CHOICES = [
        (FIRST, _("First category doctor")),
        (SECOND, _("Second category doctor")),
        (HIGHEST, _("Highest category doctor"))
    ]

    category = models.CharField(max_length=50, choices=QUALIFICATION_CHOICES, default=FIRST)

    SPECIALITY_CHOICES = [
        ("Neurologist", _("Neurologist")),
        ("Traumatologist", _("Traumatologist")),
        ("Infectious disease specialist", _("Infectious disease specialist")),
        ("Cardiologist", _("Cardiologist")),
        ("Pediatrician", _("Pediatrician")),
        ("Surgeon", _("Surgeon")),
        ("Therapist", _("Therapist")),
    ]

    speciality = models.CharField(max_length=50, choices=SPECIALITY_CHOICES, default="Therapist")

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ' + self.user.patronymic

    def save(self, *args, **kwargs):
        if not self.user.is_doctor:
            raise PermissionError('Only users with is_doctor permission can be doctors')
        else:
            super(Doctor, self).save(*args, **kwargs)


class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ' + self.user.patronymic
