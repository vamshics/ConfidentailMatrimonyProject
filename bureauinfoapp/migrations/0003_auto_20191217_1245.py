# Generated by Django 2.2.7 on 2019-12-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bureauinfoapp', '0002_auto_20191217_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_profile',
            name='hobbies',
            field=models.CharField(max_length=30),
        ),
    ]
