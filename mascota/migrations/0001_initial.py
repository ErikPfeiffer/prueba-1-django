# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('raza', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=15)),
                ('sexo', models.BooleanField()),
                ('sector', models.CharField(max_length=50)),
                ('foto', models.CharField(max_length=70)),
                ('estado', models.BooleanField()),
                ('recompensa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('correo', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='Usuario',
            field=models.ForeignKey(to='mascota.Usuario'),
        ),
    ]
