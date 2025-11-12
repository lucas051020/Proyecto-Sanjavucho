import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoImagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(help_text='Imagen adicional para la galería del producto', upload_to='productos/galeria/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galeria_imagenes', to='tienda_app.producto')),
            ],
        ),
    ]
