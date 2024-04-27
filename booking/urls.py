from django.urls import path
from .views import create_booking, list_bookings
from .views import NurseSearchAPIView
from .views import NurseListAPIView



urlpatterns = [
    path('api/bookings/create/', create_booking, name='create_booking'),
    path('api/bookings/list/', list_bookings, name='list_bookings'),
    path('search/nurses/', NurseSearchAPIView.as_view(), name='nurse-search'),
    path('nurses/', NurseListAPIView.as_view(), name='nurse-list'),
]