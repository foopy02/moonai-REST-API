from django.urls import path
from . import views

urlpatterns = [
    # path('user/register', views.register, name='register user'),
    # path('user/login', views.login, name='login user'),
    # path('user/register', views.register, name='register user'),
    # path('user/login', views.login, name='login user'),
    path('user/<str:uuid_of_user>/withdraws', views.get_withdraws),
    path('user/<str:uuid_of_user>/deposits', views.get_deposits),

]