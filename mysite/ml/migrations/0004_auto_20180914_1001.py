# Generated by Django 2.1 on 2018-09-14 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0003_auto_20180912_0519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='last_name',
            new_name='state',
        ),
    ]
