# Generated by Django 3.0.7 on 2020-06-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0011_auto_20200106_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='resource_GRE',
            field=models.ImageField(upload_to='arial_shots/GRE'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='resource_NIR',
            field=models.ImageField(upload_to='arial_shots/NIR'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='resource_RED',
            field=models.ImageField(upload_to='arial_shots/RED'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='resource_REG',
            field=models.ImageField(upload_to='arial_shots/REG'),
        ),
    ]
