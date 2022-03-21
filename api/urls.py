from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    # path('user/register', views.register, name='register user'),
    # path('user/login', views.login, name='login user'),
    # path('user/register', views.register, name='register user'),
    # path('user/login', views.login, name='login user'),
    path('user/withdraws', views.get_withdraws),
    path('user/deposits', views.get_deposits),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),


]

