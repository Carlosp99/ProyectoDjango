from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name="token_obtainer_pair"),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
    
]