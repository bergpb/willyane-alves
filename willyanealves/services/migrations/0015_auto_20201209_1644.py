# Generated by Django 3.1.2 on 2020-12-09 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
        ('services', '0014_auto_20201209_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kititem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock'),
        ),
    ]
