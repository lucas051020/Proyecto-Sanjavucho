from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0005_pedido_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Código (SKU)'),
        ),
    ]
