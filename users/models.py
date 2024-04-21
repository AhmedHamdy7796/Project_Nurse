from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.db import models








class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ]

ROLE_CHOICES = (
    ('patient', 'Patient'),
    ('nurse', 'Nurse'),
)



class User(AbstractUser):
    username = models.CharField(max_length=11)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    national_id = models.CharField(max_length=14, blank=True)
    national_id_image = models.URLField(default='image')
    selfie = models.URLField(default='image')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')

    notification_token = models.CharField(max_length=255, null=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    is_active = models.BooleanField(default=True)



    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    date_of_birth = models.DateField(default="yyyy/mm/dd")



    

class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nurse')
    certificate_image = models.URLField(default='image')
    department = models.CharField(max_length=100)




















class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"OTP for {self.email}"
