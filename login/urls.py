from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='Index'),
    path('principal/', login_required(views.principal), name='Principal'),
    path('salir/', login_required(views.salir), name='salir'),


]
