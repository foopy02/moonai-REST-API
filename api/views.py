from django.http import JsonResponse
from django.shortcuts import render
from pydantic import Json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import CustomUser, Deposit, Withdraw
from .serializers import RegistrationSerializer, UserSerializer, WithdrawSerializer, DepositSerializer
from .helpers import *
import json


@api_view(['GET'])
def index(request):
    data = {
        "hello": "hello"
    }
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    token = get_token_from_request(request)
    user_id = get_user_id_from_token(token)
    user = CustomUser.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

#TEST USER ID = ad474b75-2dd6-405f-85ab-e21495dd377e
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
                'response': "Success",
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
