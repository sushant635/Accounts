# Generated by Django 3.2.2 on 2021-05-11 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210511_1742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={},
        ),
        migrations.AlterModelOptions(
            name='estimate',
            options={},
        ),
        migrations.AlterModelOptions(
            name='expenseclaim',
            options={},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='bill',
            unique_together={('organization',)},
        ),
        migrations.AlterUniqueTogether(
            name='estimate',
            unique_together={('organization',)},
        ),
        migrations.AlterUniqueTogether(
            name='expenseclaim',
            unique_together={('organization',)},
        ),
        migrations.AlterUniqueTogether(
            name='invoice',
            unique_together={('organization',)},
        ),
    ]
