# Generated by Django 2.2.16 on 2021-01-01 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0015_auto_20210101_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct_answer',
            field=models.CharField(max_length=255),
        ),
    ]