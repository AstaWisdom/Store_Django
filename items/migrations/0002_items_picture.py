# Generated by Django 3.1.5 on 2021-01-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
