from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detail/<id_hotel>', views.detail_view),
]
