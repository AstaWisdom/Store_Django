# Generated by Django 3.1.5 on 2021-02-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_explain',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]