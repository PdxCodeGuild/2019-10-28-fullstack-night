# Generated by Django 2.2.9 on 2020-02-13 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_meal_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='carbs',
            new_name='carb',
        ),
    ]