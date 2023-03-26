
from django.http import Http404, HttpResponse  # noqa: F401
from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe
from utils.recipes.factory import make_recipe  # noqa: F401


def home(request):
    recipes = Recipe.objects.filter(
        is_publush=True
    ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):

    recipes = get_list_or_404(Recipe.objects.filter(
        is_publush=True,
        category__id=category_id,
    ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '  # type: ignore
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_publush=True,)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
