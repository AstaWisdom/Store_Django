# Generated by Django 3.1.5 on 2021-01-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Thoth_Gaming', '0003_auto_20210130_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]