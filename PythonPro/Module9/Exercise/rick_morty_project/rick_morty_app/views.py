from django.shortcuts import render
from django.http import HttpResponse
from .models import Character
# Create your views here.

def character_list(request):
    characters = Character.objects.all()
    return render(request, 'rick_morty_app/home.html', {'characters': characters})
