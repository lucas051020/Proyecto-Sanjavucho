from django.urls import path
from . import views

app_name = 'tienda_app'

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('categoria/<slug:categoria_slug>/', views.lista_productos, name='lista_productos_por_categoria'),
    path('producto/<int:id>/<slug:slug>/', views.detalle_producto, name='detalle_producto'),
    path('preguntas-frecuentes/', views.pagina_faq, name='faq'),
]