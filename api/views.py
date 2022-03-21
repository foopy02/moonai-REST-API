from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Deposit, Withdraw
from .serializers import WithdrawSerializer, DepositSerializer

@api_view(['GET'])
def index(request):
    data = {
        "hello": "hello"
    }
    return Response(data)

#TEST USER ID = ad474b75-2dd6-405f-85ab-e21495dd377e
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_withdraws(request):
    # headers = request.headers
    # uuid_of_user = headers.id
    return JsonResponse({"hello":2})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_deposits(request, uuid_of_user):
    deposits = Deposit.objects.filter(user_id = uuid_of_user)
    serializer = DepositSerializer(deposits, many=True)
    return Response(serializer.data)