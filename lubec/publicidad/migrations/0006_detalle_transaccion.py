# Generated by Django 3.2.4 on 2021-07-14 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicidad', '0005_remove_detalle_transaccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='transaccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='publicidad.transacciones'),
        ),
    ]
