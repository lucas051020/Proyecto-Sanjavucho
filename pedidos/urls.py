from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('crear/', views.crear_pedido, name='crear_pedido'),
    path('creado/<int:pedido_id>/', views.pedido_creado, name='pedido_creado'),
    path('admin/imprimir/<int:pedido_id>/', views.admin_pedido_imprimir, name='admin_pedido_imprimir'),
]