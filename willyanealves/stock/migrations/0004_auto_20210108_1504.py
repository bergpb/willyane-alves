# Generated by Django 3.1.2 on 2021-01-08 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20201209_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Quantidade'),
        ),
    ]
