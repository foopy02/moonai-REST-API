from attr import fields
from rest_framework.serializers import ModelSerializer
from .models import Withdraw, Deposit

class WithdrawSerializer(ModelSerializer):
    class Meta:
        model = Withdraw
        fields = '__all__'

class DepositSerializer(ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'