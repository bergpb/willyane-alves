# Generated by Django 3.1.2 on 2020-12-09 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
        ('services', '0005_remove_service_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kititem',
            name='price',
        ),
        migrations.AlterField(
            model_name='kititem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock'),
        ),
    ]