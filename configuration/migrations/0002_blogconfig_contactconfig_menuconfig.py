# Generated by Django 2.2.5 on 2019-09-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='home/contact')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'BlogConfig',
                'verbose_name_plural': 'BlogConfigs',
            },
        ),
        migrations.CreateModel(
            name='ContactConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='home/contact')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ContactConfig',
                'verbose_name_plural': 'ContactConfigs',
            },
        ),
        migrations.CreateModel(
            name='MenuConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='home/contact')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'MenuConfig',
                'verbose_name_plural': 'MenuConfigs',
            },
        ),
    ]
