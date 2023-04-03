from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


class RecipeURLsTest(TestCase):

    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', args=(1,))
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 2})
        self.assertEqual(url, '/recipes/2/')


class RecipeViewTest(TestCase):
    def test_recipe_home_views_functions_is_correct(self):
        view = resolve(reverse('recipes:home'))
        print(view)
        print(self.assertIs(view.func, views.home))

    def test_recipe_category_views_functions_is_correct(self):
        view = resolve(reverse('recipes:category', args=(1,)))
        print(view)
        print(self.assertIs(view.func, views.category))

    def test_recipe_detail_views_functions_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 2}))
        print(view)
        print(self.assertIs(view.func, views.recipe))
