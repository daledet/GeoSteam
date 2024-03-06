# Generated by Django 4.2.10 on 2024-03-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wellhead_number', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('temp_bottom_hole', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('pressure_bottom_hole', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('pressure_seperator', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('pressure_condensor', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('turbine_efficiency', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('turbine_exit_pressure', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('required_output', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
