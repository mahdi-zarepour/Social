# Generated by Django 3.2.8 on 2021-11-03 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211024_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.PositiveSmallIntegerField(blank=True, max_length=12, null=True),
        ),
    ]