from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('pedidos/', include('pedidos.urls', namespace='pedidos')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('tienda_app.urls')), # Incluir las URLs de la app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
