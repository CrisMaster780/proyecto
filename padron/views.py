from django.shortcuts import render, redirect
import json
from padron.models import Persona
from padron.models import Padron
from django.db.models import Q
from django.contrib import messages



def index(request):
    usuario = request.user
    sucursal = request.session['0']
    persona = Persona.objects.all()

    if request.method == 'GET':
        padron = Padron.objects.all()
        _buscar = request.GET.get('buscar')

        if _buscar:
            padron = Padron.objects.filter(
                Q(persona__cedula__icontains=_buscar)
            ).distinct()

            return render(request, 'Padron/index.html', {
                'usuario': usuario,
                'lista': padron,
                'sucursal': sucursal
            })

        return render(request, 'Padron/index.html', {
            'usuario': usuario,
            'lista': padron,
            'sucursal': sucursal
        })
    else:
        return render(request, 'Padron/index.html', {
            'usuario': usuario,
            'lista': padron,
            'sucursal': sucursal
        })


def desembolso(request):
    usuario = request.user
    sucursal = request.session['0']
    persona = Persona.objects.all()
    padron = Padron.objects.all()
    if request.method == 'GET':
        return render(request, 'Padron/desembolso.html', {
            'usuario': usuario,
            'lista': padron,
            'sucursal': sucursal
        })
    else:
        return render(request, 'Padron/desembolso.html', {
            'usuario': usuario,
            'lista': padron,
            'sucursal': sucursal
        })


def buscarPago(request):
    _buscar_pago = request.GET.get('buscarpago')
    usuario = request.user
    persona = Persona.objects.all()
    sucursal = request.session['0']
    padron = Padron.objects.all()
    if _buscar_pago:
        persona = Persona.objects.filter(
            Q(cedula__icontains=_buscar_pago)
        ).distinct()
        return render(request, 'Padron/desembolso.html', {
            'usuario': usuario,
            'consulta': persona,
            'sucursal': sucursal,
        })
    else:
        return render(request, 'Padron/desembolso.html', {
            'usuario': usuario,
            'sucursal': sucursal,
        })


def registrar(request):
    usuario = request.user
    sucursal = request.session['0']
    padron = Padron.objects.all()
    persona = Persona.objects.all()

    if request.method == 'GET':
        print('entro en get')
        return render(request, 'Padron/desembolso.html', {
            'usuario': usuario,
            'sucursal': sucursal,

        })
    else:
        print('entro en post')
        _nombre = request.POST.get('nombre')
        _apellido = request.POST.get('apellido')
        _documento = request.POST.get('documento')
        _mesa = request.POST.get('mesa')
        _orden = request.POST.get('orden')
        _monto = request.POST.get('monto')
        print(request.POST)
        
        if padron.filter(persona__cedula=_documento):
          
            return render(request, 'Padron/desembolso.html', {
            'usuario': usuario,
            'sucursal': sucursal,
            
            'error': 'La persona ya tiene un Pago'

        })

    return redirect('/padron')
