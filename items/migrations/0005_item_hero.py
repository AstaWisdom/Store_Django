# Generated by Django 3.1.5 on 2021-03-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='hero',
            field=models.CharField(default='Terror Blade', max_length=50),
            preserve_default=False,
        ),
    ]
