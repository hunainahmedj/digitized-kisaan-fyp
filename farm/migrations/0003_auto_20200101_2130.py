# Generated by Django 3.0.1 on 2020-01-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0002_auto_20200101_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='farm_lookup',
            field=models.CharField(auto_created=True, default='8HYnnJAy', max_length=120),
        ),
    ]
