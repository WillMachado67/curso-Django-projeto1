
from unittest import skip

from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


# @skip('A mensagem do porquê estou pulando esses testes')
class RecipeHomeViewTest(RecipeTestBase):

    def test_recipe_home_views_functions_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_returns_status_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    # @skip('WIP')
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipe found here 😢</h1>',
            response.content.decode('utf-8')
        )

        # Tenho que escrever mais coisas sobre o teste
        # self.fail('Para que eu termine de digitá-lo')

    def test_recipe_home_templates_loads_recipes(self):
        # Need a recipe for this test
        self.make_recipe()

        response = self.client.get(reverse('recipes:home'))
        response_content = response.content.decode('utf8')
        response_context_recipe = response.context['recipes']

        # Check if one recipe exists
        self.assertIn('Recipe Title', response_content)
        self.assertEqual(len(response_context_recipe), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_publisheded False dont show"""
        # Need a recipe for this test
        self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:home'))

        # Check if one recipe exists
        self.assertIn(
            '<h1>No recipe found here 😢</h1>',
            response.content.decode('utf-8')
        )
