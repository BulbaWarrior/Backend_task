from rest_framework.permissions import BasePermission
from hotel.models import Hotel

class HotelRelated(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if(request.user.is_staff):
            return True
        return obj.get_hotel() == request.user.hotel
