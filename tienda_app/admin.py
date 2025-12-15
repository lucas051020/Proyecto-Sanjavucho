from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Categoria, Producto, ProductoImagen, Pedido, PedidoItem, PrecioPorVolumen, PreguntaFrecuente

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto
        fields = ('id', 'codigo', 'nombre', 'slug', 'categoria', 'descripcion', 
                  'precio', 'stock', 'disponible', 'imagen')
        import_id_fields = ['id']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}


class ProductoImagenInline(admin.TabularInline):
    model = ProductoImagen
    extra = 1
    verbose_name = "Imagen de galería"
    verbose_name_plural = "Imágenes de galería"

class PrecioPorVolumenInline(admin.TabularInline):
    model = PrecioPorVolumen
    extra = 1
    verbose_name = "Precio por Volumen"
    verbose_name_plural = "Precios por Volumen"


@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):
    resource_class = ProductoResource
    list_display = ['nombre', 'codigo', 'slug', 'precio', 'stock', 'disponible']
    list_filter = ['disponible', 'categoria']
    list_editable = ['precio', 'stock', 'disponible'] 
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ['nombre', 'slug', 'codigo']
    readonly_fields = ('codigo',)
    inlines = [ProductoImagenInline, PrecioPorVolumenInline] 


class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    readonly_fields = ('producto', 'precio', 'cantidad')
    extra = 0
    can_delete = False

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha_creado', 'completado', 'enlace_imprimir')
    list_filter = ('completado', 'fecha_creado', 'usuario')
    inlines = [PedidoItemInline]
    readonly_fields = ('fecha_creado', 'enlace_imprimir', 'usuario',)
    
    def enlace_imprimir(self, obj):
        from django.utils.html import format_html
        from django.urls import reverse
        if obj.id:
            url = reverse('pedidos:admin_pedido_imprimir', args=[obj.id])
            return format_html(
                '<a href="{}" class="button" target="_blank">Imprimir Pedido</a>',
                url
            )
        return "N/A"
    
    enlace_imprimir.short_description = 'Imprimir'

@admin.register(PreguntaFrecuente)
class PreguntaFrecuenteAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'orden')
    list_editable = ('orden',)