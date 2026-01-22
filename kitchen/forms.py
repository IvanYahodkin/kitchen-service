from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Cook, Dish


class CookCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name","years_of_experience",)

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        if years_of_experience <= 0:
            raise ValidationError("Please enter a positive integer")
        return years_of_experience


class DishCreationForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    name = forms.CharField(max_length=100,
                           required=False,
                           label="",
                           widget=forms.TextInput(
                               attrs={"placeholder": "Search by name"}))
