from rest_framework import serializers
from .models import User
from django.utils import timezone
from django.db import models
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import Nurse, Patient


class UserRegisterSerializer(UserDetailsSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        exclude = ['is_superuser', 'is_staff', 'last_login', 'date_joined', 'is_active']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

        def save(self, request):
            user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            national_id=self.validated_data['national_id'],
            gender=self.validated_data['gender'],
            role=self.validated_data['role'],
            national_id_image=self.validated_data['national_id_image'],
            selfie=self.validated_data['selfie'],
            
        )

        optional_fields = ['notification_token']

        for field in optional_fields:
            if field in self.validated_data:
                setattr(user, field, self.validated_data[field])

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta:
        model = User
        exclude = ['is_superuser', 'is_staff', 'last_login', 'date_joined',
                   'is_active', 'password', 'groups', 'user_permissions']
        read_only_fields = ('id', )


# new serializers for patient and nurse

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'






# reset_password

# class PasswordResetSerializer(serializers.Serializer):
#     email = serializers.EmailField()

#     def validate_email(self, value):
#         """
#         Check if the email exists in the database.
#         """
#         if not User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("No user with that email address.")
#         return value


# class PasswordResetConfirmSerializer(serializers.Serializer):
#     new_password = serializers.CharField(min_length=8, max_length=128)
#     new_password_confirm = serializers.CharField(min_length=8, max_length=128)

#     def validate(self, data):
#         """
#         Check if the new passwords match.
#         """
#         new_password = data.get('new_password')
#         new_password_confirm = data.get('new_password_confirm')

#         if new_password != new_password_confirm:
#             raise serializers.ValidationError("The new passwords do not match.")
#         return data




# serializers.py


# class OTPSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     otp = serializers.CharField(max_length=6)
