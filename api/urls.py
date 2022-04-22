from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('register/', views.register_user),
    path('user/', views.get_user_info),
    path('user/balance/', views.get_user_balance_info),
    path('user/ref/', views.get_user_ref_info),
    path('user/plans/', views.get_user_plans_info),
    path('user/withdraws/', views.get_withdraws),
    path('user/deposits/', views.get_deposits),
    # path('user/referal/list', views.get_referals),
    # path('user/referal/code', views.get_referal_code),
    # path('')
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('verify/<str:token>/',views.verify)
]