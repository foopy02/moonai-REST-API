import jwt
from django.conf import settings
from .models import CustomUser, Deposit, Withdraw

def get_user(request):
    token = get_token_from_request(request)
    user_id = get_user_id_from_token(token)
    user = CustomUser.objects.get(id=user_id)
    return user

def get_token_from_request(request):
    return request.META.get('HTTP_AUTHORIZATION').split('Bearer ')[1]

def get_user_id_from_token(token):
    token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    return token['user_id']

def get_user_id(request):
    token = get_token_from_request(request)
    return get_user_id_from_token(token)
