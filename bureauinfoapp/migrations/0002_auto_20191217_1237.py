# Generated by Django 2.2.7 on 2019-12-17 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bureauinfoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='create_profile',
            old_name='secondname',
            new_name='lastname',
        ),
    ]
