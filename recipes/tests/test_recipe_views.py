from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views
from recipes.models import Category, Recipe, User


class RecipeViewTest(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(
            author=author,
            category=category,
            title='Recipe Title',
            description='Recipe Descripition',
            slug='recipe-slug',
            preparation_time=10,
            peparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            peparation_steps='Recipe Pretarion Steps',
            peparation_steps_is_html=False,
            is_publush=True,
        )
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_recipe_home_views_functions_is_correct(self):
        view = resolve(reverse('recipes:home'))
        # print(view)
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        # print(response)
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_returns_status_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        # print(response)
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse('recipes:home'))
        # print(response.content.decode('utf-8'))
        self.assertIn(
            '<h1>No recipe found here 😢</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_templates_loads_recipes(self):

        response = self.client.get(reverse('recipes:home'))
        response_context_recipe = response.context['recipes']
        # print(response_context_recipe.first().title)

        response_content = response.content.decode('utf8')
        # print(response_content)
        self.assertIn('Recipe Title', response_content)
        self.assertIn('10 Minutos', response_content)
        self.assertIn('5 Porções', response_content)
        self.assertEqual(len(response_context_recipe), 1)

    def test_recipe_category_views_functions_is_correct(self):
        view = resolve(reverse('recipes:category', args=(1,)))
        # print(view)
        self.assertIs(view.func, views.category)

    def test_recipe_category_returns_404_if_no_recipe_found(self):
        response = self.client.get(reverse('recipes:category', args=(1000,)))
        # print(response.content)
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_views_functions_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 2}))
        # print(view)
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_returns_404_if_no_recipe_found(self):
        response = self.client.get(reverse('recipes:recipe', args=(1000,)))
        # print(response)
        self.assertEqual(response.status_code, 404)
