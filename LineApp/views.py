from django.shortcuts import render
from .forms import LoginForm, UserForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect



def AcercaDe(request):
    return render(request,'LineApp/AcercaDe.html')


def inicio(request):
    return render(request,'LineApp/inicio.html')


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