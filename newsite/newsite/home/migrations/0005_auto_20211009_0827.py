# Generated by Django 3.2.8 on 2021-10-09 08:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_entry_entries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entries',
            name='text',
        ),
        migrations.AddField(
            model_name='entries',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]