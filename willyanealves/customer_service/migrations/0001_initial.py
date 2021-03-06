# Generated by Django 3.1.2 on 2020-11-12 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0015_auto_20201112_1109'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Data')),
                ('start', models.TimeField(auto_now_add=True, verbose_name='Hora de início')),
                ('discount', models.IntegerField(verbose_name='Desconto')),
                ('payment', models.CharField(max_length=20, verbose_name='Pagamento')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
