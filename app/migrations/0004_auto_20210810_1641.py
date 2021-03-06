# Generated by Django 3.2.5 on 2021-08-10 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210810_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_ingreso',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_salida',
            field=models.DateTimeField(blank=True),
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='usuario',
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
            preserve_default=False,
        ),
    ]
