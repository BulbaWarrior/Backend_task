from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


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

    def get_hotel(self):
        return room.room_category.hotel

    def is_valid(self):
        if (self.date_check_in >= date_check_out):
            return False
        # TODO: check for overlaps and if booking in the past
