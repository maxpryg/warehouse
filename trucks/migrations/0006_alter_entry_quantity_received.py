# Generated by Django 4.0.2 on 2022-02-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0005_alter_entry_options_alter_entry_material_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='quantity_received',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]