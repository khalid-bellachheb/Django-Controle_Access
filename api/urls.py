from django.urls import include, path
from . import views


urlpatterns = [
    path('up', views.save_data, name='api'),
    path('matricule', views.save_maricule_data, name='api'),
    path('facialRecognition', views.save_faceRecognition_data, name='api'),
]
