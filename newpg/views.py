from django.shortcuts import render
from .models import Login


def home(request):

    return render(request, 'newpg/home.html', {'title': 'Langscape'})
