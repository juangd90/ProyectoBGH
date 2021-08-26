# Generated by Django 3.2.5 on 2021-08-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210826_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidonousuario',
            old_name='nombre',
            new_name='nombre_y_apellido',
        ),
        migrations.AddField(
            model_name='pedidonousuario',
            name='barrio',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='pedidonousuario',
            name='domicilio',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='pedidonousuario',
            name='comentarios',
            field=models.TextField(default='', max_length=300),
        ),
    ]