# Generated by Django 3.2.2 on 2021-05-10 10:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_rename_phone_no_registermodels_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegisterModels',
            new_name='RegisterModel',
        ),
    ]
