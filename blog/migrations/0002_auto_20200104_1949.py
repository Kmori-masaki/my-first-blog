# Generated by Django 3.0.1 on 2020-01-04 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tiile',
            new_name='title',
        ),
    ]
