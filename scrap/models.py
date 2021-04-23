from django.db import models


# Create your models here.
class ScrapModel(models.Model):
    name_hotel = models.CharField(max_length=255, blank=True, null=True)
    address_hotel = models.CharField(max_length=255, blank=True, null=True)
    photo_hotel = models.TextField(blank=True, null=True)
    review_score = models.CharField(max_length=255, blank=True, null=True)
    review_quantities = models.CharField(max_length=255, blank=True, null=True)


class ScrapModelRoom(models.Model):
    roomName = models.CharField(max_length=255, blank=True, null=True)
    photo_room = models.TextField(blank=True, null=True)
    bathroom = models.TextField(blank=True, null=True)
    room_view_title = models.TextField(blank=True, null=True)
    equipment_title = models.TextField(blank=True, null=True)
    hotel = models.ForeignKey(ScrapModel, on_delete=models.CASCADE)
