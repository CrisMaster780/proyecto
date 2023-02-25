from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('padron/', views.index, name='Padron'),
    path('desembolso/', views.desembolso, name='Desembolso'),
    path('buscarPago/', views.buscarPago, name='Pago'),
    path('registrar/', views.registrar, name='Registrar'),
    
    

]
