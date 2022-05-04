# Generated by Django 3.2.9 on 2022-04-18 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0005_orderlist_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='account',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
