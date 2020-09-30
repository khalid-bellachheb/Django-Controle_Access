from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.FoliumView.as_view(), name='control_acces' ),
]