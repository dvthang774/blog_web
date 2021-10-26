# Generated by Django 3.2.8 on 2021-10-09 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_entry_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={},
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='entry_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='entry_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='entry_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='entry_title',
            new_name='title',
        ),
    ]