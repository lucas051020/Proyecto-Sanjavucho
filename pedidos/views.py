from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from tienda_app.models import Pedido, PedidoItem
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

@login_required
def crear_pedido(request):
    cart = Cart(request)
    
    if len(cart) == 0:
        return redirect('tienda_app:lista_productos')

    pedido = Pedido.objects.create(usuario=request.user)

    for item in cart:
        PedidoItem.objects.create(
            pedido=pedido,
            producto=item['product'],
            precio=item['price'],     
            cantidad=item['quantity']
        )
    
    cart.clear()

    return redirect('pedidos:pedido_creado', pedido_id=pedido.id)

def pedido_creado(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedidos/creado.html', {'pedido': pedido})

@staff_member_required  
def admin_pedido_imprimir(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedidos/admin_imprimir.html', {'pedido': pedido})