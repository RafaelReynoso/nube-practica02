from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import *
from .serializer import *

class UsuariosView(viewsets.ModelViewSet):
    serializer_class = UsuariosSerializer
    queryset = Usuarios.objects.all()


def home(request):
    usuariosListado = Usuarios.objects.all()
    return render(request, "gestionUsuarios.html", {"usuarios": usuariosListado})

def registrarUsuarios(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    telefono = request.POST['numTelefono']
    email = request.POST['txtEmail']

    usuarios = Usuarios.objects.create(codigo = codigo, nombre = nombre, telefono = telefono, email = email)
    return redirect('usuarios/')
