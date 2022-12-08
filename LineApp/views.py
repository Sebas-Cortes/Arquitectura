from django.shortcuts import render
from .forms import LoginForm, UserForm, EstacionamientoForm
from .models import Estacionamiento, Arriendo
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect


def inicio(request):
    lista = Estacionamiento.objects.all().order_by('idEstacionamiento')
    data = {"lista" : lista}
    return render(request,'LineApp/inicio.html', data)

def InicioSesion(request):
    return render(request,'LineApp/InicioSesion.html')

class CustomLoginView(LoginView):
    template_name = 'LineApp/InicioSesion.html'
    form_class = LoginForm

def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            nick1 = form.cleaned_data['username']
            messages.success(request, f'Usuario {nick1} creado con exito')
            return redirect('inicio')
    else:
        form = UserForm()

    contexto = { 'form' : form }

    return render(request,'LineApp/registro.html', contexto)

def estacionamiento(request):
    if request.method == 'POST':
        form = EstacionamientoForm(request.POST)
        if form.is_valid():
            form.save()
            direccion = form.cleaned_data['direccion']
            messages.success(request, f'Estacionamiento {direccion} agregado con exito')
            return redirect('inicio')
        print('xd')
    else:
        form = EstacionamientoForm()
    
    contexto = { 'form' : form }
    
    return render(request, 'LineApp/estacionamiento.html', contexto)

def arrendar(request, idEstacionamiento):
    esta = Estacionamiento.objects.get(pk=idEstacionamiento)
    numero = esta.numero
    if numero > 0:
        Arriendo.objects.create(arrendatario = request.user, estacionamiento = esta, titular = esta.titular.id)
        esta.numero = esta.numero - 1 
        esta.save()
        messages.success(request, f'Estacionamiento {esta.direccion} agregado con exito')
        return redirect('inicio')
    else:
        messages.warning(request, 'No hay estacionamientos disponibles')
        return redirect('inicio')