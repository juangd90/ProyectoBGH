# Generated by Django 3.2.5 on 2021-08-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210812_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='comentarios',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
