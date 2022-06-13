# Generated by Django 3.1.5 on 2021-02-28 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20210222_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdashboard',
            name='invited_users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invited_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userdashboard',
            name='invite_link',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
