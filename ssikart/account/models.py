from re import U 
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("User must have email address")
        if not username:
            raise ValueError("User must have username")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, first_name, last_name,  username, email, password):
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
            username = username,
            password = password,
            
            )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save()
        return user 


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    #required 
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return f"{self.id} - {self.email}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_lable):
        return True