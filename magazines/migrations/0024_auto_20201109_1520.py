# Generated by Django 3.1.1 on 2020-11-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0023_auto_20201109_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine',
            name='tags',
        ),
        migrations.AddField(
            model_name='magazine',
            name='magazineGroup',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
