# Generated by Django 3.0.1 on 2020-01-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coordinates',
            options={'verbose_name': 'Coordinate', 'verbose_name_plural': 'Coordinates'},
        ),
        migrations.AlterField(
            model_name='farm',
            name='coordinates',
            field=models.ManyToManyField(to='farm.Coordinates'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='farm_lookup',
            field=models.CharField(auto_created=True, default='ujslDjWF', max_length=120),
        ),
    ]
