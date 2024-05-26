from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from configs import upload_dir

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, password):

        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            # last_name=last_name,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    sound = models.ForeignKey('AudioFile', on_delete=models.SET_NULL, null=True, blank=True, default=0)
    background_color = models.CharField(max_length=7, default='red')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email


class ToDo(models.Model):

    STATUS_CHOICES = [
        ('todo', 'ToDo'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='todos', default=None)

    def __str__(self):
        return self.title


class AudioFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(
        upload_to=upload_dir)

    def __str__(self):
        return self.name
