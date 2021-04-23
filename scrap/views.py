from scrap.scrap_hotel.scrap_hotel import ScrapHotel
from .models import ScrapModel, ScrapModelRoom
from django.shortcuts import render
from .forms import HotelForm


def index(request):
    hotels = ScrapModel.objects.all()

    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            scrap_view(request, request.POST['name_hotel'])
            print('++++++++++++SCRAP+++++++++++')
            return render(request, 'scrap/index.html', {'form': form,
                                                        'data': hotels})
    else:
        form = HotelForm()

    return render(request, 'scrap/index.html', {'form': form, 'data': hotels})


def detail_view(request, id_hotel):
    hotel = ScrapModel.objects.get(id=id_hotel)
    rooms = ScrapModelRoom.objects.filter(hotel=id_hotel)
    data = {'hotel': hotel, 'rooms': rooms}
    return render(request, 'scrap/detail.html', data)


def scrap_view(request, name_hotel):
    data = ScrapHotel(name_hotel)
    hotel_data = data.get_hotel_data()
    save_data(hotel_data)
    return render(request, "scrap/index.html")


def save_data(hotel_data):
    obj_hotel = ScrapModel()
    obj_hotel.name_hotel = hotel_data['hotel_description']['name_hotel']
    obj_hotel.address_hotel = hotel_data['hotel_description']['address_hotel']
    obj_hotel.photo_hotel = hotel_data['hotel_description']['photo_hotel']
    obj_hotel.review_score = hotel_data['hotel_description']['review_score']
    obj_hotel.review_quantities = hotel_data['hotel_description']['review_quantities']
    obj_hotel.save()

    for key, value in hotel_data.items():
        if key == 'rooms':
            for rooms in value:
                obj_room = ScrapModelRoom()
                obj_room.roomName = rooms['room_name']
                obj_room.photo_room = rooms['photo_room']
                obj_room.bathroom = rooms['bathroom']
                obj_room.room_view_title = rooms['room_view_title']
                obj_room.equipment_title = rooms['equipment_title']
                obj_room.hotel = obj_hotel
                obj_room.save()
