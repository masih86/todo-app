from django.urls import path

from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = "api-v1"

urlpatterns = [
    path('registration/', CreateCustomUserView.as_view(), name='registration'),
    path('profile/', RetrieveUserView.as_view(), name='profile'),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout')
]