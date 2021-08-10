# Generated by Django 3.2.5 on 2021-08-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='pedidos',
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ManyToManyField(blank=True, to='app.Usuario'),
        ),
    ]