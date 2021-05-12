# Generated by Django 3.2.2 on 2021-05-11 10:29

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('payroll_tax_rate', models.DecimalField(decimal_places=5, max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('0')), django.core.validators.MaxValueValidator(Decimal('1'))])),
                ('salary_follows_profits', models.BooleanField(default=False)),
                ('shares_percentage', models.DecimalField(decimal_places=5, max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('0')), django.core.validators.MaxValueValidator(Decimal('1'))])),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='app.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address_line_1', models.CharField(max_length=128)),
                ('address_line_2', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(max_length=64)),
                ('postal_code', models.CharField(max_length=7)),
                ('country', models.CharField(max_length=50)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='app.organization')),
            ],
        ),
    ]
