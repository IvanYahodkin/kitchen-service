from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Cook, DishType, Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "dish_type", "price"]
    list_filter = ["price"]
    search_fields = ["name"]


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Experience", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            'fields': ('years_of_experience',),
        }),
    )


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
