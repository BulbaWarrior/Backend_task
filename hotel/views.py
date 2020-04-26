from hotel import models
from rest_framework import viewsets
from rest_framework import permissions
from hotel import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class HotelViewSet(viewsets.ModelViewSet):
    # queryset = models.Hotel.objects.all()
    def get_queryset(self):
        user = self.request.user
        if(user.is_staff):
            return models.Hotel.objects.all()
        else:
            return user.hotel
    serializer_class = serializers.HotelSerializer
    permission_classes = [permissions.IsAuthenticated]

class RoomCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.RoomCategory.objects.all()
    serializer_class = serializers.RoomCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class RoomViewSet(viewsets.ModelViewSet):
    # queryset = models.Room.objects.all()
    def get_queryset(self):
        user = self.request.user
        if(user.is_staff):
            return models.Room.objects.all()
        else:
            return user.hotel.room_set.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
