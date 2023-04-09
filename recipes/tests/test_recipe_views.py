
from unittest import skip

from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


# @skip('A mensagem do porquê estou pulando esses testes')
class RecipeViewTest(RecipeTestBase):

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

    def test_recipe_home_tenplate_dont_load_recipes_not_published(self):
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

    def test_recipe_category_views_functions_is_correct(self):
        view = resolve(reverse('recipes:category', args=(1,)))
        self.assertIs(view.func, views.category)

    def test_recipe_category_returns_404_if_no_recipe_found(self):
        response = self.client.get(reverse('recipes:category', args=(1000,)))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_templates_loads_recipes(self):
        needed_title = 'This is a category test'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        # Check if one recipe exists
        response = self.client.get(reverse('recipes:category', args=(1,)))
        response_content = response.content.decode('utf8')

        self.assertIn(needed_title, response_content)

    def test_recipe_category_tenplate_dont_load_recipes_not_published(self):
        """Test recipe is_publisheded False dont show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id})
        )

        self.assertEqual(response.status_code, 404)

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
