# Generated by Django 3.2.5 on 2021-08-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_pedido_monto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='monto',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
