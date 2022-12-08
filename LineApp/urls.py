from django.urls import path
from .views import CustomLoginView, inicio,AcercaDe, registro
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio,name="inicio"),
    path('AcercaDe/',AcercaDe,name="AcercaDe"),
    path('InicioSesion/', CustomLoginView.as_view(), name='InicioSesion'),
    path('logout/', LogoutView.as_view(template_name='LineApp/inicio.html'), name='logout'),
    path('registro/',registro,name="registro"),
]