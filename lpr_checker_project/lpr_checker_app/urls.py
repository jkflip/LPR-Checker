from django.urls import path
from . import views

urlpatterns = [
    path("", views.status, name="status"),
    path("car_register/", views.car_and_owner_form_view, name="car_form"),
    path("car_search/", views.car_search_view, name="car_search"),
    # path("predict/", views.predict, name="predict"),
]
