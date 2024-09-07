# Generated by Django 5.1.1 on 2024-09-07 18:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='chais/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('types', models.CharField(choices=[('ML', 'MASLA'), ('GR', 'GINGER'), ('KL', 'KIWI'), ('PL', 'PLAIN'), ('EL', 'ELAICHI')], max_length=2)),
            ],
        ),
    ]
