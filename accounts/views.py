from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()      
            login(request, user)    
            return redirect('tienda_app:lista_productos')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def editar_perfil(request):
    profile, created = Profile.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST) 
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:editar_perfil') 
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)

    return render(request, 
                  'accounts/editar_perfil.html', 
                  {'user_form': user_form, 'profile_form': profile_form})

@staff_member_required
def admin_perfil_imprimir(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    return render(request, 'accounts/admin_imprimir_perfil.html', {'usuario': usuario})