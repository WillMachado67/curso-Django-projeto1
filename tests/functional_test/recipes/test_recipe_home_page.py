from unittest.mock import patch

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import RecipeBaseFunctionalTest


@pytest.mark.functional_test
class RecipeHomeFuncionalTest(RecipeBaseFunctionalTest):
    def test_recipe_home_page_without_recipes_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertIn('No recipe found here 😢', body)

    @patch('recipes.views.PER_PAGE', new=3)
    def test_recipe_search_input_can_find_correct_recipes(self):
        recipes = self.make_recipe_in_batch()
        
        title_needed = 'This is what i need'
        recipes[0].title = title_needed
        recipes[0].save()

        # user open the page
        self.browser.get(self.live_server_url)

        # see a search input with the text "Search for a recipe"

        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Search for a recipe"]'
        )

        # Click in input e digit the term search
        # For search the recipe with title needed

        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)

        # The user see what is in the page
        
        self.assertIn(
            title_needed,
            self.browser.find_element(By.CLASS_NAME, 'main-content-list').text
        )

    @patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_home_page_pagination(self):
        self.make_recipe_in_batch()

        # User open the page
        self.browser.get(self.live_server_url)

        # See have a pagination and clic in the page 2
        page2 = self.browser.find_element(
            By.XPATH,
            '//a[@aria-label="Go to page 2"]'
        )
        page2.click()

        # See there are 2 more recipes on the page

        self.assertEqual(
            len(self.browser.find_elements(By.CLASS_NAME, 'recipe')),
            2
        )
