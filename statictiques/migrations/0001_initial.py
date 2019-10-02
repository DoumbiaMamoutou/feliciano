# Generated by Django 2.2.5 on 2019-10-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('pays', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('continent', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('reseau', models.CharField(max_length=50)),
            ],
        ),
    ]
