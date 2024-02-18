from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . import forms
from . import models

# from lpr_model_app.views import predict


def status(request):
    return HttpResponse("Server is online")


# def image_file_upload_view(request):
#     """
#     Method to handle uploading an image file to the server.
#     """
#     if request.method == "POST":
#         form = forms.ImageFileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             image_file = form.cleaned_data.get("image_file")
#             image_file_name = form.cleaned_data.get("image_file_name")
#             image_file_path = form.cleaned_data.get("image_file_path")
#             image_file_size = form.cleaned_data.get("image_file_size")
#             image_file_type = form.cleaned_data.get("image_file_type")
#             image_file_url = form.cleaned_data.get("image_file_url")
#             image_file.save()
#             return HttpResponse("Image upload success")
#     return render(request, "image_file_upload_form.html", {"form": forms.ImageFileUploadForm()})


def image_file_upload_view(request):
    """
    Method to handle saving car information to the database.
    """
    if request.method == "POST":
        form = forms.ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Image upload success")
    else:
        form = forms.ImageUploadForm()
    return render(request, "car_form.html", {"form": form})


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
