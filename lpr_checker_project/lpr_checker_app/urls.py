from django.urls import path
from . import views

urlpatterns = [
    path("my_endpoint/", views.hello_world),
    path("register_car/", views.car_and_owner_form_view, name="car_form"),
