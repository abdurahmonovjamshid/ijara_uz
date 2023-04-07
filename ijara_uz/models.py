from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        self.phone = phone
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        """Create and save a regular User with the given phone and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class CustomUser(AbstractUser):
    """User model."""

    username = None
    email = None
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17,
                             unique=True)  # validators should be a list
    city = models.CharField(max_length=50, blank=True, null=True)
    USERNAME_FIELD = 'phone'
    # REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'CustomUser'


class User(models.Model):
    phone = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='user_image', default="avatar.svg")
    full_name = models.CharField(max_length=200)
    city = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.full_name


class Apartment(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    size = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    for_men = models.BooleanField(default=True)
    contract = models.BooleanField(default=True)
    is_flat = models.BooleanField(default=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Jobs(models.Model):
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    salary = models.FloatField()
    skills = models.TextField(max_length=500)
    company = models.CharField(max_length=200, blank=False, null=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    list_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
