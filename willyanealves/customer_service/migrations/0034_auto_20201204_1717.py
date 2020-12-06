# Generated by Django 3.1.2 on 2020-12-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0033_auto_20201130_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerservice',
            name='discount',
            field=models.IntegerField(blank=True, choices=[(0, '0%'), (5, '5%'), (10, '10%'), (15, '15%'), (20, '20%')], max_length=2, verbose_name='Desconto'),
        ),
    ]