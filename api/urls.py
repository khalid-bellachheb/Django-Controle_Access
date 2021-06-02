from django.urls import include, path
from . import views


urlpatterns = [
    path('up', views.save_data, name='api'),
]
