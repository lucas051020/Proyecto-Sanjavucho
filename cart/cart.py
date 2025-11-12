from decimal import Decimal
from django.conf import settings
from tienda_app.models import Producto
from .forms import CartAddProductForm

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.precio)}
        
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Producto.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            producto = item['product']
            cantidad = item['quantity']
            precio_unitario = Decimal(item['price']) 
            mejor_precio_volumen = producto.precios_volumen.filter(
                cantidad_minima__lte=cantidad
            ).last()

            if mejor_precio_volumen:
                precio_unitario = mejor_precio_volumen.precio

            item['price'] = precio_unitario
            item['total_price'] = precio_unitario * cantidad

            item['update_quantity_form'] = CartAddProductForm(initial={
                'quantity': cantidad,
                'override': True
            })

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        product_ids = self.cart.keys()
        products = Producto.objects.filter(id__in=product_ids)
        total = Decimal(0)

        for product in products:
            item = self.cart[str(product.id)]
            cantidad = item['quantity']
            precio_unitario = Decimal(item['price'])
            mejor_precio_volumen = product.precios_volumen.filter(
                cantidad_minima__lte=cantidad
            ).last()

            if mejor_precio_volumen:
                precio_unitario = mejor_precio_volumen.precio

            total += precio_unitario * cantidad

            return total

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()