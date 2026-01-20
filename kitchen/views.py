from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm
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
    paginate_by = 3


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "kitchen/dish_type_detail.html"
    context_object_name = "dish_type"
    queryset = DishType.objects.prefetch_related("dishes")


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"
    fields = "__all__"

class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    fields = "__all__"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_confirm_delete.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 3


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 3


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish

class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    fields = "__all__"

class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    fields = "__all__"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
