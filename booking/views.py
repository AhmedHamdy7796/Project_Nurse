from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Patient
from .serializers import NurseSerializer
from users.models import Nurse




@api_view(['POST'])
def create_booking(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)



# search
class NurseSearchAPIView(generics.ListAPIView):
    serializer_class = NurseSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        if query:
            return Nurse.objects.filter(full_name__icontains=query)
        return Nurse.objects.all()  # Return all nurses if no query is provided



# list of nurse
class NurseListAPIView(generics.ListAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer



