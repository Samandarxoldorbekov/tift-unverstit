# Generated by Django 5.1.1 on 2024-09-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_diriction'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='full_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
