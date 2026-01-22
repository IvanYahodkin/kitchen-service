from django.test import TestCase
from kitchen.forms import CookCreationForm, DishSearchForm


class CookAdminCreationFormTests(TestCase):
    def test_valid_data(self):
        form = CookCreationForm(
            data={
                "username": "testuser",
                "password1": "strongpassword123",
                "password2": "strongpassword123",
                "years_of_experience": 5,
            }
        )
        self.assertTrue(form.is_valid())

    def test_invalid_years_of_experience(self):
        form = CookCreationForm(
            data={
                "username": "user",
                "password1": "password123",
                "password2": "password123",
                "years_of_experience": 0,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("Please enter a positive integer", form.errors["years_of_experience"])


class DishSearchFormTests(TestCase):
    def test_search_form_with_data(self):
        form = DishSearchForm(data={"name": "Pizza"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "Pizza")

    def test_search_form_empty(self):
        form = DishSearchForm(data={"name": ""})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "")