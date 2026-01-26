from django.test import TestCase
from kitchen.models import DishType, Cook, Dish


class TestModel(TestCase):
    def test_dishtype(self):
        dishtype = DishType.objects.create(name="Pizza")
        self.assertEqual(str(dishtype), "Pizza")

    def test_dishtype_str(self):
        dishtype = DishType.objects.create(name="Pizza")
        self.assertEqual(str(dishtype), dishtype.name)

    def test_cook(self):
        cook = Cook.objects.create(
            username="GRam",
            first_name="Gordon",
            last_name="Ramsay",
            years_of_experience=5
        )
        self.assertEqual(cook.first_name, "Gordon")
        self.assertEqual(cook.last_name, "Ramsay")
        self.assertEqual(cook.years_of_experience, 5)

    def test_dish(self):
        dish_type = DishType.objects.create(name="Pizza")
        dish = Dish.objects.create(
            name="Peperoni",
            dish_type=dish_type,
            description="Test description",
            price=4.50
        )
        self.assertEqual(dish.name, "Peperoni")
        self.assertEqual(dish.description, "Test description")
        self.assertEqual(dish.price, 4.50)

