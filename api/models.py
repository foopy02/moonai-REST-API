from django.db import models
import uuid
# Create your models here.

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
