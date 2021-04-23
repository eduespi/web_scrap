from django import forms


class HotelForm(forms.Form):
    name_hotel = forms.CharField(label='Hotel Name', max_length=100)
