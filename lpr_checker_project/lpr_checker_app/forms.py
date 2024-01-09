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


class CarSearchForm(forms.Form):
    name = forms.CharField(required=False)
    license_plate = forms.CharField(required=False)
