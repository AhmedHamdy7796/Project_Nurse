# from rest_framework import viewsets
# from .models import Nurse, Patient
# from .serializers import NurseSerializer, PatientSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import OTP
import random

#chossing_user


# class NurseViewSet(viewsets.ModelViewSet):
#     queryset = Nurse.objects.all()
#     serializer_class = NurseSerializer

# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer

#set_pass_OTP

@api_view(['POST'])
def generate_otp(request):
    email = request.data.get('email')
    if email:
        otp = ''.join(random.choices('0123456789', k=6))  # Generate OTP
        OTP.objects.create(email=email, otp=otp)  # Save OTP to database
        send_mail(
            'Password Reset OTP',
            f'Your OTP for password reset is: {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return Response({'message': 'OTP sent successfully'})
    else:
        return Response({'error': 'Email is required'}, status=400)



@api_view(['POST'])
def verify_otp(request):
    email = request.data.get('email')
    otp_entered = request.data.get('otp')
    if email and otp_entered:
        otp_obj = OTP.objects.filter(email=email, otp=otp_entered).first()
        if otp_obj:
            # If OTP is valid, allow password reset
            # Implement your password reset logic here
            otp_obj.delete()  # Delete OTP record from database
            return Response({'message': 'OTP verified successfully'})
        else:
            return Response({'error': 'Invalid OTP'}, status=400)
    else:
        return Response({'error': 'Email and OTP are required'}, status=400)



# views.py
# reset_password
# important

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
# from .models import OTP

# @api_view(['POST'])
# def set_password(request):
#     email = request.data.get('email')
#     password = request.data.get('password')
#     otp_entered = request.data.get('otp')

#     if email and password and otp_entered:
#         otp_obj = OTP.objects.filter(email=email, otp=otp_entered).first()
#         if otp_obj:
#             # If OTP is valid, allow password reset
#             user = User.objects.filter(email=email).first()
#             if user:
#                 user.set_password(password)
#                 user.save()
#                 otp_obj.delete()  # Delete OTP record from database
#                 return Response({'message': 'Password has been reset successfully'})
#             else:
#                 return Response({'error': 'User not found'}, status=404)
#         else:
#             return Response({'error': 'Invalid OTP'}, status=400)
#     else:
#         return Response({'error': 'Email, password, and OTP are required'}, status=400)




# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['POST'])
# def reset_password(request):
#     if request.method == 'POST':
#         email = request.data.get('email')
#         new_password = request.data.get('new_password')

#         # Retrieve the user by email
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=404)

#         # Update the user's password
#         user.password = make_password(new_password)
#         user.save()

#         return Response({'message': 'Password reset successfully'})
