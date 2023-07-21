from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'barrios', BarrioSerializerViewSet)
router.register(r'personas', PersonaSerializerViewSet)
router.register(r'locales_repuestos', LocalesRepuestosSerializerViewSet)
router.register(r'locales_comidas', LocalesComidaViewSet)


urlpatterns = [
path('api/', include(router.urls)),
    path("LocalesRepuestoss", ListLocalesRepuestos.as_view(), name="list_LocalesRepuestoss"),

    path("create/LocalesRepuestos", LocalesRepuestos_create, name="LocalesRepuestos_create"),
    path("edit/LocalesRepuestos/<int:id>", LocalesRepuestos_edit, name="LocalesRepuestos_edit"),
    path('eliminar/LocalesRepuestos/<int:id>', eliminar_LocalesRepuestos,
         name='eliminar_local_repuestos'),

    path("", ListLocalesComida.as_view(), name="list_LocalesComidas"),

    path("create/LocalesComida", LocalesComida_create, name="LocalesComida_create"),
    path("edit/LocalesComida/<int:id>", LocalesComida_edit, name="LocalesComida_edit"),
    path('eliminar/LocalesComida/<int:id>', eliminar_LocalesComida,
         name='eliminar_local_comida'),
]
