from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Withdraw, Deposit, CustomUser, Wallet
from .terra_network import TerraNetwork
from .utils import send_email_token

class UserAllSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'name', 'surname', 'gender', 'date_of_birth', 'number','balance_last_updated', 'balance_last_updated_time', 'balance_for_withdraw','ref_balance_last_updated', 'ref_balance_last_updated_time', 'ref_code','ref_amount_available','ref_amount_filled','ref_by','apy', 'usertype', 'plan']

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'name', 'surname', 'gender', 'date_of_birth', 'number']

class UserBalanceSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['balance_last_updated', 'balance_last_updated_time', 'balance_for_withdraw']

class UserRefSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['ref_balance_last_updated', 'ref_balance_last_updated_time', 'ref_code','ref_amount_available','ref_amount_filled','ref_by']

class UserRefUsernameSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']


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
        fields = ['email', 'username', 'name', 'surname', 'gender', 'date_of_birth', 'number', 'ref_by', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    

    def _generate_wallet_for_user(self,user):
        tn = TerraNetwork()
        terra_wallet = tn.create_wallet()
        wallet = Wallet(
                user=user,
                address=terra_wallet[0],
                mnemonic_key=terra_wallet[1]
        )
        wallet.save()

    def save(self):
        
        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            name=self.data['name'],
            surname=self.data['surname'],
            number=self.data['number'],
            gender=self.data['gender'],
            date_of_birth=self.data['date_of_birth']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':"Passwords must match."})

        if self.data['ref_by'] is not None:
            try:
                referer = CustomUser.objects.get(username=self.data['ref_by'])
                user.ref_by = referer.username
                referer.ref_amount_filled += 1
                referer.save()
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError({'ref_by':f"{self.data['ref_by']} doesn't found in database. Check referal username."})
            
        user.set_password(password)

        user.ref_code = user.username
        send_email_token(user.email, user.id, user.username)
        user.is_active = False
        user.save()
        self._generate_wallet_for_user(user)

        return user

class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['address', 'balance']