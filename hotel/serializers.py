from hotel import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['url', 'username', 'email', 'hotel']

class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Hotel
        fields = '__all__'

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'

class RoomCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RoomCategory
        fields = '__all__'

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'
