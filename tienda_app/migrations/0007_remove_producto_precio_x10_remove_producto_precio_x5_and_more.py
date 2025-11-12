import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0006_producto_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio_x10',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio_x5',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio_x50',
        ),
        migrations.CreateModel(
            name='PrecioPorVolumen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_minima', models.PositiveIntegerField(default=1, verbose_name='Cantidad Mínima')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Unitario')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='precios_volumen', to='tienda_app.producto')),
            ],
            options={
                'verbose_name': 'Precio por Volumen',
                'verbose_name_plural': 'Precios por Volumen',
                'ordering': ['cantidad_minima'],
                'unique_together': {('producto', 'cantidad_minima')},
            },
        ),
    ]
