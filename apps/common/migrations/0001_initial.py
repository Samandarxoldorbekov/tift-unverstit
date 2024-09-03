# Generated by Django 5.0.7 on 2024-09-03 02:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order_id', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['order_id', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('social', models.CharField(choices=[('telegram', 'Telegram'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('youtube', 'Youtube')], max_length=16)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order_id', models.IntegerField(unique=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.region')),
            ],
            options={
                'ordering': ['order_id', 'id'],
            },
        ),
    ]
