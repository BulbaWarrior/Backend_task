from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager, BookingManager


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_hotel(self):
        return self

class RoomCategory(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    min_price = models.IntegerField('minimal price')
    def __str__(self):
        return self.name
    def get_hotel(self):
        return self.hotel

class Room(models.Model):
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_hotel(self):
        return room_category.hotel

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = None
    hotel = models.ForeignKey(Hotel, null=True, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_check_in = models.DateTimeField()
    date_check_out = models.DateTimeField()
    objects = BookingManager()

    def get_hotel(self):
        return room.room_category.hotel

    def is_valid(self):
        if (self.date_check_in >= self.date_check_out):
            return False
        last_bookings = self.room.booking_set.filter(date_check_out__gt = self.date_check_in)
        for booking in last_bookings:
            if booking.date_check_in <= self.date_check_in <= booking.date_check_out:
                return False
            if booking.date_check_in <= self.date_check_out <= booking.date_check_out:
                return False
        return True

    @classmethod
    def create(cls, **kwargs):
        booking = cls(kwargs)
        if(not booking.is_valid()):
            raise ValueError("booking dates are invalid")
        return booking
