# Generated by Django 2.1.2 on 2019-01-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('victorias', models.CharField(max_length=10)),
                ('derrotas', models.CharField(max_length=10)),
                ('porcentaje', models.CharField(max_length=10)),
                ('diferencia', models.CharField(max_length=10)),
                ('puntosFuera', models.CharField(max_length=10)),
                ('puntosContra', models.CharField(max_length=10)),
                ('conf', models.CharField(max_length=10)),
                ('division', models.CharField(max_length=10)),
                ('casa', models.CharField(max_length=10)),
                ('fuera', models.CharField(max_length=10)),
                ('ultimo10', models.CharField(max_length=10)),
            ],
        ),
    ]
