from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, role='user', password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        # Set unusable password so Django auth won’t break
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, role='admin', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, role=role, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    headline = models.CharField(max_length=1000, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=1000, blank=True)
    profile_photo_url = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # required by admin
    is_superuser = models.BooleanField(default=False)
     # Password field required by AbstractBaseUser
    password = models.CharField(max_length=128, blank=True, null=True)  # temporarily allow password

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # no password required

    objects = UserManager()

    def __str__(self):
        return self.email

class AuthProvider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auth_providers")
    provider = models.CharField(max_length=50)
    provider_user_id = models.CharField(max_length=255)

    class Meta:
        unique_together = ('provider', 'provider_user_id')

    def __str__(self):
        return f"{self.provider} - {self.user.email}"

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField(User, related_name='skills', blank=True)

    def __str__(self):
        return self.name
