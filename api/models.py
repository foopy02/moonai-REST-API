from multiprocessing.sharedctypes import Value
from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, name, surname, gender, date_of_birth, password=None):
        if not email:
            raise ValueError("Email is mandatory field")
        if not username:
            raise ValueError("Username is mandatory field")
        if not name:
            raise ValueError("Name is mandatory field")
        if not surname:
            raise ValueError("Surname is mandatory field")
        if not gender:
            raise ValueError("Gender is mandatory field")
        if not date_of_birth:
            raise ValueError("Date of birth is mandatory field")
        
        user=self.model(
            email=email,
            username=username,
            name=name,
            surname=surname,
            gender=gender,
            date_of_birth=date_of_birth
        )
        print(user.__dict__)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, name, surname, gender, date_of_birth, password=None):
        user=self.create_user(
            email=email,
            username=username,
            password=password,
            name=name,
            surname=surname,
            gender=gender,
            
            date_of_birth=date_of_birth
        )
        user.is_admin=True
        user.is_superuser=True
        print(user.__dict__)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    class Gender():
        MALE = 0
        FEMALE = 1
        genders = (
            (MALE, 'Male'),
            (FEMALE, 'Female')
        )
    
    class Apy():
        BASIC = "BASIC"
        SILVER = "SILVER"
        GOLD = "GOLD"
        plans = (
            (BASIC, 'BASIC'),
            (SILVER, 'SILVER'),
            (GOLD, 'GOLD')
        )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="ID")

    email=models.EmailField(verbose_name="Email", max_length=64)
    username=models.CharField(verbose_name="Username", max_length=30, unique=True)
    name=models.CharField(max_length=26, verbose_name="Name")
    surname=models.CharField(max_length=26, verbose_name="Surname")

    gender= models.IntegerField(choices=Gender.genders, verbose_name="Gender")
    date_of_birth=models.DateField(verbose_name="Date of Birth")
    
    balance_last_updated=models.FloatField(verbose_name="Balance last Updated", null=True, blank=True)
    balance_last_updated_time=models.FloatField(verbose_name="Balance last Updated Time", null=True, blank=True)
    balance_for_withdraw=models.FloatField(verbose_name="Balance available for withdraw", default=0)

    ref_balance_last_updated=models.FloatField(verbose_name="Referals balance last update", default=0)
    ref_balance_last_updated_time=models.FloatField(verbose_name="Referal balance last updated time", null=True, blank=True)
    ref_code=models.CharField(verbose_name="Referal code", max_length=30, unique=True, null=True, blank=True)
    ref_amount_available=models.IntegerField(default=0)
    ref_amount_filled=models.IntegerField(default=0)
    ref_by=models.UUIDField(default=None, null=True, blank=True)

    apy=models.IntegerField(default=2)
    plan=models.CharField(choices=Apy.plans, default=Apy.BASIC, max_length=10)

    date_joined = models.DateTimeField(auto_now_add=True, editable=True),
    last_login = models.DateTimeField(auto_now=True, verbose_name="Last login", editable=True),
    is_admin=models.BooleanField(default=False),
    is_active=models.BooleanField(default=True),
    is_staff=models.BooleanField(default=False),
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ['email', 'name', 'surname', 'gender', 'date_of_birth']

    objects=MyUserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Withdraw(models.Model):
    class CashFlowStatus():
        INITIATED = 'INITIATED'
        APPROVED = 'APPROVED'
        IN_PROGRESS = 'IN PROGRESS'
        SUCCEEDED = 'SUCCEEDED'
        FAILED = 'FAILED'
        statuses = (
            (INITIATED, 'Initiated'),
            (APPROVED, 'Approved'),
            (IN_PROGRESS, 'In progress'),
            (SUCCEEDED, 'Succeeded'),
            (FAILED, 'Failed')
        )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="ID")
    user_id = models.UUIDField(verbose_name="UUID of user")
    amount_kzt = models.FloatField(verbose_name="Amount of money in KZT")
    status = models.CharField(max_length=25, choices=CashFlowStatus.statuses, verbose_name="Status")
    datetime = models.DateTimeField(auto_now=True, verbose_name='Date and time of withdraw')

class Deposit(models.Model):
    class CashFlowStatus():
        INITIATED = 'INITIATED'
        APPROVED = 'APPROVED'
        IN_PROGRESS = 'IN PROGRESS'
        SUCCEEDED = 'SUCCEEDED'
        FAILED = 'FAILED'
        statuses = (
            (INITIATED, 'Initiated'),
            (APPROVED, 'Approved'),
            (IN_PROGRESS, 'In progress'),
            (SUCCEEDED, 'Succeeded'),
            (FAILED, 'Failed')
        )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="ID")
    user_id = models.UUIDField(verbose_name="UUID of user")
    amount_kzt = models.FloatField(verbose_name="Amount of money in KZT")
    status = models.CharField(max_length=25, choices=CashFlowStatus.statuses, verbose_name="Status")
    datetime = models.DateTimeField(auto_now=True, verbose_name='Date and time of withdraw')

