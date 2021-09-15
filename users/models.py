import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from stdimage import StdImageField


def get_file_path(_instance, filename) -> str:
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return f'users/{filename}'


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email is required'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    image = StdImageField(_('image'), upload_to=get_file_path, variations={'thumb': (480, 480)})
    email = models.EmailField('email', max_length=50, unique=True)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'cpf')

    def __str__(self):
        return self.email

    objects = UserManager()


class Address(models.Model):
    zip_code = models.CharField(_('zip code'), max_length=15, blank=False)
    address = models.CharField(_('address'), max_length=50, blank=False)
    house_number = models.CharField(_('house number'), max_length=10, blank=False)
    complement = models.CharField(_('complement'), max_length=150, blank=True)
    neighborhood = models.CharField(_('neighborhood'), max_length=100, blank=False)
    city = models.CharField(_('city'), max_length=100, blank=False)
    state = models.CharField(_('state'), max_length=100, blank=False)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
