from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from kitchen.models import DishType, Dish, Cook


def index(request: HttpRequest) -> HttpResponse:
    num_dish_type = DishType.objects.all().count()
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()

    context = {
        "num_dish_type": num_dish_type,
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
    }
    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    ordering = ["name"]
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class CookListView(generic.ListView):
    model = Cook


class DishListView(generic.ListView):
    model = Dish
