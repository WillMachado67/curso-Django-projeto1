
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', status=201, context={
        'name': 'Willian Machado'
    })
