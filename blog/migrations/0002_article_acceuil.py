# Generated by Django 2.2.5 on 2019-10-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='acceuil',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
