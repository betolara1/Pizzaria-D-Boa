# Generated by Django 5.0.7 on 2024-08-10 04:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0010_remove_pedidos_preco_pedidos_preco'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos',
            name='preco',
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='preco',
            field=models.FloatField(null=True),
        ),
    ]