# Generated by Django 3.1.2 on 2020-10-31 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0011_auto_20201020_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine',
            name='category',
        ),
        migrations.AddField(
            model_name='magazine',
            name='thumbNail',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
