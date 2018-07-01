from django.conf.urls import url

from .views import AllHotels, Hotelincity #Reservationlist

urlpatterns = [
   url(r"allhotels", AllHotels),
   url(r"hotelincity", Hotelincity),
   #url(r"reservationlist", Reservationlist)
]