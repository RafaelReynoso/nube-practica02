from rest_framework import routers
from usuarios import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuariosView,'usuarios')

urlpatterns = [
    path('', views.home),
    path('registrarUsuarios/', views.registrarUsuarios, name='registrar_usuarios'),
    path('api/v1/', include(router.urls))
]
