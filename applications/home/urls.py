#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(),
        name='index',
    ),  
    path(
        'register-suscripción', 
        views.SuscriberCreateView.as_view(),
        name='add-suscription',
    ),  
    path(
        'rcontact', 
        views.ContactCreateView.as_view(),
        name='add-contac',
    ),  
]