from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . import forms
from . import models


def hello_world(request):
    return HttpResponse("Hello, World!")


#! Feature request: What if user can register multiple cars in one go?
def car_and_owner_form_view(request):
    """
    Method to register a car and its owner to the database.
    """
    if request.method == "POST":
        car_form = forms.CarForm(request.POST)
        owner_form = forms.OwnerForm(request.POST)
        if car_form.is_valid() and owner_form.is_valid():
            owner = owner_form.save()
            car = car_form.save(commit=False)
            car.owner = owner
            car.save()
            return HttpResponse("Car registration success")

    return render(
        request,
        "car_form.html",
        {"car_form": forms.CarForm(), "owner_form": forms.OwnerForm()},
    )


