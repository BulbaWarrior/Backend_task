from hotel import models
from rest_framework import viewsets, permissions
from rest_framework import permissions 
from hotel.permissions import HotelRelated
from hotel import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]

class HotelViewSet(viewsets.ModelViewSet):
    # queryset = models.Hotel.objects.all()
    def get_queryset(self):
        user = self.request.user
        if(user.is_staff):
            return models.Hotel.objects.all()
        else:
            return [user.hotel,]
    serializer_class = serializers.HotelSerializer
    permission_classes = [permissions.IsAuthenticated, HotelRelated]

class RoomCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.RoomCategory.objects.all()
    def get_queryset(self):
        user = self.request.user
        if(user.is_staff):
            return models.RoomCategory.objects.all()
        else:
            return user.hotel.roomcategory_set.all()
    serializer_class = serializers.RoomCategorySerializer
    permission_classes = [permissions.IsAuthenticated, HotelRelated]

class RoomViewSet(viewsets.ModelViewSet):
    # queryset = models.Room.objects.all()
    # def get_queryset(self):
    #     user = self.request.user
    #     if(user.is_staff):
    #         return models.Room.objects.all()
        
    #     # elif(self.request.room_category):
    #     #     return room_category.room_set.all()
    #     else:
    #         rooms = []
    #         for room_category in user.hotel.roomcategory_set.all():
    #             rooms += room_category.room_set.all()
    #         return rooms
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated, HotelRelated]

class BookingViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if(user.is_staff):
            return Booking.objects.all()
        else:
            bookings = []
            for category in user.hotel.roomcategory_set.all():
                for room in category.room_set.all():
                    bookings += room.booking_set.all()
            return bookings
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated, HotelRelated]
