# Generated by Django 3.1.1 on 2020-11-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0020_auto_20201107_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='tags',
            field=models.ManyToManyField(to='magazines.Tag'),
        ),
    ]
