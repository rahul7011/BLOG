# Generated by Django 3.2 on 2021-04-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='fix_me'),
            preserve_default=False,
        ),
    ]
