from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# === INSTRUCTION FOR CREATING USERS === # 
class MyAccountManager(BaseUserManager):
    
    # === CREATING NORMAL USER === #
    def create_user(self, first_name, last_name, username, email, password=None):
        
        if not email:
            raise ValueError('User must have an email address')
        elif not username:
            raise ValueError('User must have an username')
    
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        
        user.save(using=self._db)
        return user
    
    # === CREATING SUPER USER === #
    def create_superuser(self, first_name, last_name, username, email, password):
        
        user = self.create_user(
            first_name=first_name, 
            last_name=last_name, 
            username=username, 
            email=self.normalize_email(email),
            password=password 
        )
        # === SET PERMISSIONS FOR SUPER USER === #
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user


# === CREATE CUSTOM USER MODEL === #
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    username = models.CharField(max_length=55, unique=True)
    email = models.EmailField(max_length=55, unique=True)
    phone_number = models.CharField(max_length=55, unique=True)
    # ==== REQUIRED FIELDS === #
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # === DEFAULT DJANGO HAS 'username' FIELD FOR LOGIN | CHANGE FOR 'email' === #
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # === SPECIFY THAT WE USE OUR OWN USER MANAGER === #
    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, object=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    # === SPECIFY THIS CUSTOM MODEL IN settings.py == #
    # === AND REGISTER MODEL INSIDE APP admin.py === #