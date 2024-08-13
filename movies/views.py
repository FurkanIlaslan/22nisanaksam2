from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def index(request):
    filmler = Movie.objects.all()
    context = {
        'filmler':filmler
    }

    return render(request, "index.html", context)


def film_detay(request, film_id):
    film = get_object_or_404(Movie, id = film_id)

    context = {
        'film':film
    }

    return render(request, "film_detay.html", context)



        