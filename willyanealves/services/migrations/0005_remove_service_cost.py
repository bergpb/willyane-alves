# Generated by Django 3.1.2 on 2020-12-09 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_kititem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='cost',
        ),
    ]