from django.urls import path

from kitchen.views import index, DishTypeListView, CookListView, DishListView, DishDetailView, CookDetailView, \
    DishTypeDetailView

urlpatterns = [
    path("", index, name="index"),
    path("dishtypes/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishtypes/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
]

app_name = "kitchen"
