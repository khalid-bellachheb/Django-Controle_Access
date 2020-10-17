from django.urls import include, path

from . import views

urlpatterns = [
    path('redirect/',views.my_view, name='my_view' ),
    path('',views.FoliumVListView.as_view(), name='control_acces' ),
]