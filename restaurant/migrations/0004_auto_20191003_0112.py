# Generated by Django 2.2.5 on 2019-10-03 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20191002_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
