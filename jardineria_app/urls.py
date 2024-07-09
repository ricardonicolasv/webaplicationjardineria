from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    detalle_pedido, flores, base, maceteros, listar_usuarios, detalles_usuario, modificar_usuario, suculentas, sustratos, tierra, home, seguimiento_pedido,
    crearcuenta, salir, producto, crearproducto, detalles_producto, modificarproducto, agregar_a_pedido, pedidoscli, actualizar_cantidad, eliminar_pedido, listar_usuarios_con_pedidos, detalles_pedidos_usuario, agregar_pedido_usuario
)

urlpatterns = [
    # Home
    path('', home, name='home'),
    path('base/', base, name='base'),

    # Usuarios
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/<int:user_id>/', detalles_usuario, name='detalles_usuario'),
    path('usuarios/<int:user_id>/modificar/', modificar_usuario, name='modificar_usuario'),
    path('crearcuenta/', crearcuenta, name='crearcuenta'),
    path('salir/', salir, name='salir'),
    
    # Usuarios con pedidos
    path('usuarios_con_pedidos/', listar_usuarios_con_pedidos, name='listar_usuarios_con_pedidos'),
    path('usuarios_con_pedidos/<int:user_id>/', detalles_pedidos_usuario, name='detalles_pedidos_usuario'),
    path('usuarios_con_pedidos/<int:user_id>/agregar_pedido/', agregar_pedido_usuario, name='agregar_pedido_usuario'),

    # Pedidos
    path('pedidoscli/', pedidoscli, name='pedidoscli'),
    path('detalle_pedido/', detalle_pedido, name='detalle_pedido'),
    path('agregar_a_pedido/<str:producto_id>/', agregar_a_pedido, name='agregar_a_pedido'),
    path('actualizar_cantidad/<int:pedido_id>/', actualizar_cantidad, name='actualizar_cantidad'),
    path('eliminar_pedido/<int:pedido_id>/', eliminar_pedido, name='eliminar_pedido'),
    path('seguimiento_pedido/', seguimiento_pedido, name='seguimiento_pedido'),

    # Productos
    path('productos/', producto, name='productos'),
    path('detalles_producto/<id>', detalles_producto, name='detalles_producto'),
    path('modificarproducto/<id>', modificarproducto, name='modificarproducto'),
    path('crearproducto/', crearproducto, name='crearproducto'),

    # Otros
    path('flores/', flores, name='flores'),
    path('maceteros/', maceteros, name='maceteros'),
    path('suculentas/', suculentas, name='suculentas'),
    path('sustratos/', sustratos, name='sustratos'),
    path('tierra/', tierra, name='tierra'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
