# Generated by Django 3.1.2 on 2021-01-08 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0015_auto_20210108_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kititem', to='stock.stock')),
            ],
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('kititem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.kititem')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='kit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kit', to='stock.kit'),
        ),
    ]
