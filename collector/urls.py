from django.urls import path, include
from collector import views

urlpatterns = [
    path('parser/', views.parser, name='parser'),
]


