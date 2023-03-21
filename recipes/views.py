
from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, render

from recipes.models import Recipe
from utils.recipes.factory import make_recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_publush=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     is_publush=True,
    #     category__id=category_id,
    # ).order_by('-id')

    # category_name = getattr(getattr(recipes.first(), 'category', None),
    #                         'name',
    #                         'Not found')

    # if not recipes:
    #     return HttpResponse(content='Not found', status=404)

    # if not recipes:
    #     raise Http404('Not found 😢')

    # recipes = get_list_or_404(Recipe, category__id=category_id, is_publush=True,)

    recipes = get_list_or_404(Recipe.objects.filter(
        is_publush=True,
        category__id=category_id,
    ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
