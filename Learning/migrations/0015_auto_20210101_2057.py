# Generated by Django 2.2.16 on 2021-01-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0014_auto_20201229_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct_answer',
            field=models.CharField(choices=[(models.CharField(max_length=255), 'first_choice'), (models.CharField(max_length=255), 'second_choice'), (models.CharField(max_length=255), 'third_choice'), (models.CharField(max_length=255), 'fourth_choice')], max_length=255),
        ),
    ]
