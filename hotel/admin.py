from django.contrib import admin
from .models import Hotel, RoomCategory, Room, Booking

class RoomCategoryInline(admin.TabularInline):
    model = RoomCategory
    extra = 0
    list_filter = ['hotel']

class RoomInline(admin.TabularInline):
    model = Room
    list_filter = ['room_category', 'room_category.hotel']

class BookingInline(admin.TabularInline):
    model = Booking
    list_filter = ['room',  'room.room_category', 'room.room_category.hotel']
    
class HotelAdmin(admin.ModelAdmin):
    inlines = [RoomCategoryInline]

class RoomCategoryAdmin(admin.ModelAdmin):
    inlines = [RoomInline]
    list_filter = ['hotel']

class RoomAdmin(admin.ModelAdmin):
    inlines = [BookingInline]
    list_filter = ['room_category']

class BookingAdmin(admin.ModelAdmin):
    list_filter = ['room']
    def save_model(self, request, obj, form, change):
        if(not obj.is_valid()):
            raise ValueError("dates are invalid")
        super().save_model(request, obj, form, change)

admin.site.register(Hotel, HotelAdmin)
admin.site.register(RoomCategory, RoomCategoryAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
