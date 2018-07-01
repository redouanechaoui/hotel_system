# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel #Reservation, Customer

def AllHotels(request):
    all_hotels = "<ul>"
    for hotel in Hotel.objects.all():
        all_hotels =all_hotels + "<li>" + hotel.hotel_name + "</li>"
    all_hotels += "</ul>"

    return HttpResponse(all_hotels)

def Hotelincity(request):
    all_hotelincity = "<ul>"
    for hotel in Hotel.objects.all():
        all_hotelincity +="<li>" + hotel.hotel_city + " =>    " + hotel.hotel_name + "</li>"
    all_hotelincity += "</ul>"

    return HttpResponse(all_hotelincity)

#def Reservationlist(request):
#    all_reservationlist = "<ul>"
#    for r in Reservation.objects.all():
#        all_reservationlist += "<li>" + r.customer.name + ' - ' + r.hotel.hotel_name + str(name.start_time)[:-6] + " " + str(name.end_time)[:-6] + "</li>"
#    all_reservationlist += '</ul>'
#    return HttpResponse(all_reservationlist)