from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0008_remove_producto_moneda'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntaFrecuente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=255)),
                ('respuesta', models.TextField()),
                ('orden', models.PositiveIntegerField(default=0, help_text='Para ordenar las preguntas (menor a mayor).')),
            ],
            options={
                'verbose_name': 'Pregunta Frecuente',
                'verbose_name_plural': 'Preguntas Frecuentes',
                'ordering': ['orden'],
            },
        ),
    ]
