from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/', views.editar_perfil, name='editar_perfil'),
    path('admin/imprimir_perfil/<int:user_id>/', views.admin_perfil_imprimir, name='admin_perfil_imprimir'),
]