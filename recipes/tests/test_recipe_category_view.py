
from unittest import skip

from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


# @skip('A mensagem do porquê estou pulando esses testes')
class RecipeCategoryViewTest(RecipeTestBase):

    def test_recipe_category_views_functions_is_correct(self):
        view = resolve(reverse('recipes:category', args=(1,)))
        self.assertIs(view.func.view_class, views.RecipeListViewCategory)

    def test_recipe_category_returns_404_if_no_recipe_found(self):
        response = self.client.get(reverse('recipes:category', args=(1000,)))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_templates_loads_recipes(self):
        needed_title = 'This is a category test'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        # Check if one recipe exists
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf8')

        self.assertIn(needed_title, content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        """Test recipe is_publisheded False dont show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'pk': recipe.category.id})
        )

        self.assertEqual(response.status_code, 404)
