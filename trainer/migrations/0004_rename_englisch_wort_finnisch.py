# Generated by Django 5.1.1 on 2024-10-07 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_alter_wort_kategorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wort',
            old_name='englisch',
            new_name='finnisch',
        ),
    ]
