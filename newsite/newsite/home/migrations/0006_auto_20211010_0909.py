# Generated by Django 3.2.8 on 2021-10-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211009_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entries',
            name='body',
        ),
        migrations.AddField(
            model_name='entries',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
