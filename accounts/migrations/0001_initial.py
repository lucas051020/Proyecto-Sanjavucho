import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(blank=True, max_length=20, null=True, verbose_name='DNI')),
                ('telefono', models.CharField(blank=True, max_length=50, null=True, verbose_name='Teléfono')),
                ('direccion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
                ('barrio', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=20, null=True, verbose_name='Código Postal')),
                ('provincia', models.CharField(blank=True, max_length=100, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
