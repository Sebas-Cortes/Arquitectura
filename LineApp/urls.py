from django.urls import path
from .views import CustomLoginView, inicio, registro, estacionamiento, arrendar
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',inicio,name="inicio"),
    path('InicioSesion/', CustomLoginView.as_view(), name='InicioSesion'),
    path('logout/', LogoutView.as_view(template_name='LineApp/inicio.html'), name='logout'),
    path('registro/',registro,name="registro"),
    path('estacionamiento/', login_required(estacionamiento), name='estacionamiento'),
    path('arrendar/<int:idEstacionamiento>', login_required(arrendar), name='arrendar')
]