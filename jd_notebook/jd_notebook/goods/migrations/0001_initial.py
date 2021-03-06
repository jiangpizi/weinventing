# Generated by Django 2.1.3 on 2019-01-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('shop', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('img', models.CharField(blank=True, max_length=255, null=True)),
                ('commit_num', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'notebook',
            },
        ),
    ]
