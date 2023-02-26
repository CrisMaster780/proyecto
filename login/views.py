from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.backends.db import SessionStore
from padron.models import Sucursal
import json


def index(request):
    sucursal = Sucursal.objects.all()
    if request.method == 'GET':
        sucursal = Sucursal.objects.all()

        return render(request, 'Login/index.html', {
            'sucursal': sucursal
        })
    else:
        sucursal = Sucursal.objects.all()
        _usu = request.POST['username']
        _pass = request.POST['password']
        user = authenticate(request, username=_usu, password=_pass)

        if user is None:
            return render(request, 'Login/index.html', {
                'error': 'USUARIO O CONTRASENA INCORRECTOS',
                'sucursal': sucursal
            })

        else:
            
            login(request, user)
            id_usu = request.user.id
            #estr = Sucursal.objects.filter(usuario__id__contains= id_usu).first()
            

            #print(estr)
           # request.session[0] = estr
            return redirect('/principal')


def principal(request):
    usuario = request.user.username
    #sucursal = request.session['0']
    id_usu = request.user.id
    estr = Sucursal.objects.filter(usuario__id__contains= id_usu).first()
    titulo = 'Principal'
    return render(request, 'Login/principal.html', {
        'usuario': usuario,
        'titulo': titulo,
        'sucursal': estr
    })


def salir(request):
    logout(request)
    return redirect("/")
