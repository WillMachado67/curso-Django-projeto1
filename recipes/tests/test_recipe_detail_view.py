
from unittest import skip

from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


# @skip('A mensagem do porquê estou pulando esses testes')
class RecipeDetailViewTest(RecipeTestBase):

    def test_recipe_detail_views_functions_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 2}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_returns_404_if_no_recipe_found(self):
        response = self.client.get(reverse('recipes:recipe', args=(1000,)))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_templates_loads_the_correct_recipes(self):
        needed_title = 'This is a detail page - It load one recipe'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1}))
        response_content = response.content.decode('utf8')

        self.assertIn(needed_title, response_content)

    def test_recipe_detail_tenplate_dont_load_recipe_not_published(self):
        """Test recipe is_publisheded False dont show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.id}))

        self.assertEqual(response.status_code, 404)
