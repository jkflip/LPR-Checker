from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . import forms
from . import models


def status(request):
    return HttpResponse("Server is online")


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


def car_search_view(request):
    """
    Method to handle getting car information from the database.
    """
    car = None
    form = forms.CarSearchForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        license_plate = form.cleaned_data.get("license_plate")
        if name:
            owner = models.Owner.objects.filter(name=name).first()
            if owner:
                car = models.Car.objects.filter(owner=owner).first()
        elif license_plate:
            car = models.Car.objects.filter(license_plate=license_plate).first()
    return render(request, "car_search_form.html", {"form": form, "car": car})
