# Generated by Django 3.1.1 on 2020-11-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0017_magazine_description2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='involvedEditor',
            field=models.TextField(blank=True),
        ),
    ]