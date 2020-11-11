# Generated by Django 3.1.1 on 2020-10-07 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0007_auto_20201006_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Sale Summary',
                'verbose_name_plural': 'Sales Summary',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('magazines.magazine',),
        ),
        migrations.AddField(
            model_name='magazine',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]