# Generated by Django 2.1.2 on 2019-01-22 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20190121_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.CharField(max_length=200)),
                ('fecha', models.CharField(max_length=50)),
                ('urlPartido', models.URLField()),
                ('urlEquipo', models.URLField()),
                ('referencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Equipo')),
            ],
        ),
    ]
