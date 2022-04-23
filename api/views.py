from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import CustomUser, Deposit, Withdraw
from .serializers import RegistrationSerializer, UserBalanceSerializer, UserPlansSerializer, UserRefSerializer, UserSerializer, WithdrawSerializer, DepositSerializer
from .helpers import *
import json
from django.contrib.auth import get_user_model


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
    print(user.is_active)
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


def verify(request, token):
    try:
        user = CustomUser.objects.get(id=token)
        user.is_active = True
        user.save()
    except Exception as e:
        print(e)
        pass
    return render(request, 'confirm_template.html')