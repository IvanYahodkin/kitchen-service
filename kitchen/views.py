from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from kitchen.models import DishType, Dish, Cook


@login_required
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


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    ordering = ["name"]
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "kitchen/dish_type_detail.html"
    context_object_name = "dish_type"
    queryset = DishType.objects.prefetch_related("dishes")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
