# Generated by Django 3.2.5 on 2021-08-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_usuario_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='monto',
            field=models.FloatField(blank=True),
        ),
    ]
