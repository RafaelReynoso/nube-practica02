from rest_framework import routers
from usuarios import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuariosView,'usuarios')

urlpatterns = [
    path('api/v1/', include(router.urls))
]
