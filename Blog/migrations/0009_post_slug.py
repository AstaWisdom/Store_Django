# Generated by Django 3.1.5 on 2021-02-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug', max_length=255),
            preserve_default=False,
        ),
    ]
