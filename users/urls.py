from django.urls import path, include
# from .views import PasswordResetRequestAPIView, PasswordResetConfirmAPIView
from django.utils import timezone
from django.db import models
from .views import *
#generate_otp, verify_otp
# set_password


# from .views import CustomPasswordResetView, CustomPasswordResetConfirmView



urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    # path('registration/', CustomRegisterView.as_view()),
    path('registration/', include('dj_rest_auth.registration.urls')),
    
    # path('delete/', delete_account),
    # path('reset-password/', reset_password),


    # path('api/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    # path('api/password_reset_confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   


   #RESET_PASSWORD
    # path('api/password_reset/', PasswordResetRequestAPIView.as_view(), name='password_reset_request'),
    # path('api/password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),



    #OTP
    path('generate-otp/', generate_otp, name='generate_otp'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    # path('set_password/', set_password, name='set_password'),
    #path('api/reset-password/', reset_password, name='reset_password_with_otp'),
    #path('api/update-password/', make_password, name='update_password_after_otp_verification'),

]



