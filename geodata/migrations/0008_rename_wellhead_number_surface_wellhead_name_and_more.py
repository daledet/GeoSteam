# Generated by Django 4.2.10 on 2024-03-15 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0007_alter_surface_pressure_bottom_hole_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surface',
            old_name='wellhead_number',
            new_name='wellhead_name',
        ),
        migrations.AlterField(
            model_name='surface',
            name='pressure_bottom_hole',
            field=models.FloatField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='surface',
            name='pressure_condensor',
            field=models.FloatField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='surface',
            name='pressure_seperator',
            field=models.FloatField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='surface',
            name='required_output',
            field=models.FloatField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='surface',
            name='temp_bottom_hole',
            field=models.FloatField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='surface',
            name='turbine_efficiency',
            field=models.FloatField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='surface',
            name='turbine_exit_pressure',
            field=models.FloatField(max_length=255, null=True),
        ),
    ]
