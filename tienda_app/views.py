from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto, PreguntaFrecuente
from cart.forms import CartAddProductForm
from django.db.models import Q

def lista_productos(request, categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.filter(parent=None)
    productos = Producto.objects.filter(disponible=True)
    preguntas = PreguntaFrecuente.objects.all() 
    categoria_activa_slug = None
    categoria_padre_slug = None
    
    query = request.GET.get('q')
    if query:
        search_filter = (
            Q(nombre__icontains=query) | 
            Q(descripcion__icontains=query) |
            Q(codigo__icontains=query)
        )
        
        if query.isdigit():
            search_filter |= Q(id=int(query))
            
        productos = productos.filter(search_filter)

    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        
        if categoria.parent:
            categoria_activa_slug = categoria.slug
            categoria_padre_slug = categoria.parent.slug
        else:
            categoria_activa_slug = None
            categoria_padre_slug = categoria.slug

        subcategorias = categoria.subcategorias.all()
        ids_categorias = [categoria.id] + [sub.id for sub in subcategorias]
        productos = productos.filter(categoria_id__in=ids_categorias)
        
    return render(request, 'tienda/lista_productos.html', {
        'categoria': categoria,
        'categorias': categorias,
        'productos': productos,
        'query': query,
        'categoria_activa_slug': categoria_activa_slug,
        'categoria_padre_slug': categoria_padre_slug,
        'preguntas_frecuentes': preguntas,
    })


def detalle_producto(request, id, slug):
    producto = get_object_or_404(Producto, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria, 
        disponible=True
    ).exclude(id=producto.id)[:4]

    return render(request, 
                  'tienda/detalle_producto.html', 
                  {'producto': producto, 
                   'cart_product_form': cart_product_form,
                   'productos_relacionados': productos_relacionados
                  })


def pagina_faq(request):
    preguntas = PreguntaFrecuente.objects.all().order_by('orden')
    return render(request, 'tienda/faq.html', {'preguntas': preguntas})