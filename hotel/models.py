from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class RoomCategory(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    min_price = models.IntegerField('minimal price')
    def __str__(self):
        return self.name

class Room(models.Model):
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class CustomUser(User):
    hotel = models.ForeignKey(Hotel, null=True, on_delete=models.CASCADE)

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_check_in = models.DateTimeField()
    date_check_out = models.DateTimeField()

    def is_valid(self):
        if (self.date_check_in >= date_check_out):
            return False
        # TODO: check for overlaps and if booking in the past
