# Generated by Django 3.1.2 on 2021-01-08 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0012_auto_20210108_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kit',
            name='items',
        ),
        migrations.AddField(
            model_name='stock',
            name='kit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.kit'),
        ),
    ]
