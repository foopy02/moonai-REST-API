from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Withdraw, Deposit, CustomUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'name', 'surname', 'gender', 'date_of_birth', 'password', 'number']

class UserBalanceSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['balance_last_updated', 'balance_last_updated_time', 'balance_for_withdraw']

class UserRefSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['ref_balance_last_updated', 'ref_balance_last_updated_time', 'ref_code','ref_amount_available','ref_amount_filled','ref_by']

class UserPlansSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['apy', 'usertype', 'plan']

class WithdrawSerializer(ModelSerializer):
    class Meta:
        model = Withdraw
        fields = '__all__'

class DepositSerializer(ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class RegistrationSerializer(ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'name', 'surname', 'gender', 'date_of_birth', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            name=self.data['name'],
            surname=self.data['surname'],
            gender=self.data['gender'],
            date_of_birth=self.data['date_of_birth']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':"Passwords must match."})
        user.set_password(password)
        user.save()
        return user
