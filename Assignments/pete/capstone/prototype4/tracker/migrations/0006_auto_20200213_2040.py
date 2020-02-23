# Generated by Django 2.2.9 on 2020-02-14 04:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0005_auto_20200213_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='user',
        ),
        migrations.AddField(
            model_name='meal',
            name='user',
            field=models.ManyToManyField(related_name='meal', to=settings.AUTH_USER_MODEL),
        ),
    ]