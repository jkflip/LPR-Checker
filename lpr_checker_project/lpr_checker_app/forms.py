from django import forms
from django.forms.widgets import NumberInput
from . import models


class OwnerForm(forms.ModelForm):
    class Meta:
        model = models.Owner
        fields = ["name", "email", "phone_number", "address"]


class CarForm(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = ["license_plate", "car_model"]

