import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0002_productoimagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AddField(
            model_name='categoria',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='tienda_app.categoria', verbose_name='Categoría Padre'),
        ),
        migrations.AddField(
            model_name='producto',
            name='moneda',
            field=models.CharField(choices=[('ARS', 'Pesos Argentinos (ARS)'), ('USD', 'Dólares (USD)')], default='ARS', max_length=3, verbose_name='Moneda'),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_x10',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio x10'),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_x5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio x5'),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_x50',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio x50'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
