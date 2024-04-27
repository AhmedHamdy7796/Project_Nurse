from rest_framework import serializers
from .models import Booking
from users.models import Patient
from .models import Nurse

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'patient', 'nurse', 'appointment', 'price']

# search
class NurseSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name')

    class Meta:
        model = Nurse
        fields = ['id', 'user', 'department_name']



#list 
class NurseSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department')

    class Meta:
        model = Nurse
        fields = ['id', 'user', 'department_name']