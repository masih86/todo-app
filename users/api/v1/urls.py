from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
...

app_name = "api-v1"

urlpatterns = [
    path('registration/', CreateCustomUserView.as_view(), name='registration'),
    path('profile/', RetrieveUserView.as_view(), name='profile'),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('resend-verification-email/', ResendVerificationEmailView.as_view(), name='resend-verification-email'),
]

# http://localhost:8001/users/api/v1/verify-email/?token=3D6NOWK77xATOhE2Aoinvq=oac-JDgN1GO9ucEFBg09yx8

# http://localhost:8001/users/api/v1/verify-email/?token=3DfDcAPCFUWqgIV_A-rauW=Qh5hcLL00drTUvwR_Pueoso