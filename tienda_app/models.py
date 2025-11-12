from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategorias',
        verbose_name='Categoría Padre'
    )

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        full_path = [self.nombre]
        k = self.parent
        while k is not None:
            full_path.append(k.nombre)
            k = k.parent
        return ' -> '.join(reversed(full_path))

class Producto(models.Model):
    
    codigo = models.CharField(
        max_length=50, 
        unique=True,
        null=True,
        blank=True,
        verbose_name='Código (SKU)'
    )
    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    stock = models.IntegerField(default=0)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 
        if not self.codigo:
            self.codigo = str(self.id)
            super().save(update_fields=['codigo']) 

    def __str__(self):
        return self.nombre

class ProductoImagen(models.Model):
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, 
        related_name='galeria_imagenes'
    )
    imagen = models.ImageField(
        upload_to='productos/galeria/', 
        help_text="Imagen adicional para la galería del producto"
    )

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"

class Pedido(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pedidos'
    )
    fecha_creado = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-fecha_creado',)
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'Pedido #{self.id} - {self.fecha_creado.strftime("%d/%m/%Y %H:%M")}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido,
                               related_name='items',
                               on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,
                                 related_name='items_pedido',
                                 on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.precio * self.cantidad

class PrecioPorVolumen(models.Model):
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE,
        related_name='precios_volumen'
    )
    cantidad_minima = models.PositiveIntegerField(
        default=1,
        verbose_name='Cantidad Mínima'
    )
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name='Precio Unitario'
    )

    class Meta:
        ordering = ['cantidad_minima']
        unique_together = ('producto', 'cantidad_minima')
        verbose_name = 'Precio por Volumen'
        verbose_name_plural = 'Precios por Volumen'

    def __str__(self):
        return f'{self.producto.nombre} - x{self.cantidad_minima} @ ${self.precio}'

class PreguntaFrecuente(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()
    orden = models.PositiveIntegerField(default=0, help_text="Para ordenar las preguntas (menor a mayor).")

    class Meta:
        ordering = ['orden']
        verbose_name = 'Pregunta Frecuente'
        verbose_name_plural = 'Preguntas Frecuentes'

    def __str__(self):
        return self.pregunta