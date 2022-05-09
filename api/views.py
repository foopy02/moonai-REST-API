from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .utils import send_email_token,send_reset_password_mail, password_check
from .models import *
from .serializers import *
from .helpers import *
from rest_framework import serializers
from django.contrib.auth import get_user_model

import requests, time, json
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_full_infO(request):
    user = get_user(request)
    serializer = UserAllSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = get_user(request)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_balance_info(request):
    user = get_user(request)
    serializer = UserBalanceSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_ref_info(request):
    user = get_user(request)
    serializer = UserRefSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_referals(request):
    user = get_user(request)
    users = CustomUser.objects.filter(ref_by=user.username)
    serializer = UserRefUsernameSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_plans_info(request):
    user = get_user(request)
    serializer = UserPlansSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_balance_info(request):
    user = get_user(request)
    serializer = UserBalanceSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_withdraws(request):
    user_id = get_user_id(request)
    withdraws = Withdraw.objects.filter(user_id = user_id)
    serializer = WithdrawSerializer(withdraws, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_deposits(request):
    user_id = get_user_id(request)
    deposits = Deposit.objects.filter(user_id = user_id)
    serializer = DepositSerializer(deposits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_wallet_of_user(request):
    user = get_user(request)
    try:
        wallet = Wallet.objects.get(user=user)
    except Wallet.DoesNotExist:
        raise serializers.ValidationError({"status":500,"message":"There is no wallet of this user"})
    serializer = WalletSerializer(wallet, many=False)
    return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data = {
                'email': user.email,
                'username': user.username,
                'name': user.name,
                'surname': user.surname,
                'gender': user.gender,
                'date_of_birth': user.date_of_birth
            }
        else:
            data = serializer.errors
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    user = get_user(request)
    serializer = UserEditSerializer(data=request.data)
    if serializer.is_valid():
        user.name = serializer.data['name']
        user.surname = serializer.data['surname']
        user.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


def verify(request, token):
    try:
        user = CustomUser.objects.get(id=token)
        user.is_active = True
        user.save()
    except Exception as e:
        pass
    return render(request, 'confirm_template.html')


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    if request.method == "POST":

        try:
            email = request.data["email"]
            user = CustomUser.objects.get(email=email)

            id = user.id
            token = uuid.uuid4()
            username = user.username
            user.reset_password_token = token
            user.save()
            send_reset_password_mail(email=email, token=str(token), username=username, id=id)
            
            return Response({"status": "200"})
        except Exception as e:
            return Response({"status": "400"})
    else:
        return render(request, 'api/reset_password_done.html')


@permission_classes([AllowAny])
def password_reset_confirm(request, user, token):
    if request.method == "POST":
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2 and password_check(password1):
            user = CustomUser.objects.get(id=user)
            user.set_password(password1)
            user.save()
            return  render(request, 'api/password_reset_complete.html')
        else:
            return  render(request, 'api/password_reset_confirm.html', {"error": "We have error"})
    else:
        try:
            user = CustomUser.objects.get(id=user)
            if str(user.reset_password_token) == token:
                user.reset_password_token = None
                user.save()
                return  render(request, 'api/password_reset_confirm.html')
            else:
                return render(request, 'api/error_page.html', {'message': "Недействительный токен"})
        except Exception as e:
            print(e)
            return render(request, 'api/error_page.html', {'message': "Недействительный токен"})

def success_payment(request, addressFrom):
    #TODO implement check of address every n amount of time 

    return render(request, 'api/success_payment.html')
