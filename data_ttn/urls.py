from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.Data_ListView.as_view()),
]