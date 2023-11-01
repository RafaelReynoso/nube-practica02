from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *

class UsuariosView(viewsets.ModelViewSet):
    serializer_class = UsuariosSerializer
    queryset = Usuarios.objects.all()

