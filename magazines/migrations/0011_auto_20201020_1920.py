# Generated by Django 3.1.1 on 2020-10-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0010_auto_20201020_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine',
            name='tags',
        ),
        migrations.AddField(
            model_name='customer',
            name='tags',
            field=models.ManyToManyField(to='magazines.Tag'),
        ),
    ]
