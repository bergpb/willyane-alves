# Generated by Django 3.1.2 on 2021-01-08 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kit', '0002_auto_20210108_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kit',
            name='kititem',
        ),
    ]