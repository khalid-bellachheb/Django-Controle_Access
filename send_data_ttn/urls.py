from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.Accueil, name='send_data_ttn'),
]