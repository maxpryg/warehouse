# Generated by Django 4.0.2 on 2022-02-05 19:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cw', models.IntegerField()),
                ('truck_number', models.IntegerField()),
                ('arrival_date', models.DateField()),
                ('specification', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xls', 'xlsx'], message='Supported file types are XLS and XLSX')])),
            ],
            options={
                'ordering': ['-arrival_date'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=20)),
                ('material_description', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('weight', models.FloatField()),
                ('handling_unit', models.IntegerField()),
                ('truck', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trucks.truck')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
