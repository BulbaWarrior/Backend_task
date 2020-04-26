# Endpoints
[*] User login
[*] User logout
[] User change password
[*] List hotels (only for admin users)
[*] List RoomCategory (only for hotel related users) - non admin users can only get categories related to their hotel
[*] List Rooms (only for hotel related users) - non admin users get rooms of their hotel
[*] List Rooms of some RoomCategory (only for hotel related users) - only done in admin
[*] List Bookings (only for hotel related users) 
[*] List Bookings of some Room (only for hotel related users) - only in admin
[*] Create booking List Bookings (only for hotel related users), care about overlappings - currently setting invalid dates raises a value error in django admin
[*] Get for Room, Booking, RoomCategory, Hotel (only for hotel related users)
[*] User (only for admin users)

# Setup and run
$python -m pip install requirements.txt
$python manage.py runserver

API root is located at locahost:8000
GET request permissions should be properly handled (user can only see objects, related to their hotel),
however, other types of requests are not yet handled properly (user from one hotel can create a room for another hotel)
Listing


Created users:
admin@mail.com - admin
manager@mail.org - related to Sample Inn
silent@mail.com - related Silent Hills resort

all users have password '1234'