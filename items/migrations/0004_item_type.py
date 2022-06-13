# Generated by Django 3.1.5 on 2021-02-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20210127_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('SteamGiftCard', 'SteamGiftCard'), ('Game', 'Game'), ('CardWoW', 'CardWoW'), ('CardRiotPoints', 'CardRiotPoints'), ('DotaItem', 'DotaItem')], default=0, max_length=255),
            preserve_default=False,
        ),
    ]
