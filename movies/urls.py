from django.urls import path
from movies.views import *

urlpatterns = [
    path('', index, name="index"),
    path('film_detay/<int:film_id>/', film_detay, name="film_detay"),
]