# Generated by Django 5.0.3 on 2024-03-13 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='p_name',
        ),
    ]
