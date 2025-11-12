from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile
from django.utils.html import format_html
from django.urls import reverse

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'enlace_imprimir_perfil')
    readonly_fields = BaseUserAdmin.readonly_fields + ('enlace_imprimir_perfil',)

    def enlace_imprimir_perfil(self, obj):
        if obj.id:
            url = reverse('accounts:admin_perfil_imprimir', args=[obj.id])
            return format_html(
                '<a href="{}" class="button" target="_blank">Imprimir Perfil</a>',
                url
            )
        return "N/A"
    
    enlace_imprimir_perfil.short_description = 'Imprimir'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)