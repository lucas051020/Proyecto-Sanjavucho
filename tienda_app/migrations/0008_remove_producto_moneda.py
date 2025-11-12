from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0007_remove_producto_precio_x10_remove_producto_precio_x5_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='moneda',
        ),
    ]
