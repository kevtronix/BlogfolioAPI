# Generated by Django 4.2.3 on 2023-08-02 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tehnologies',
            new_name='technologies',
        ),
    ]