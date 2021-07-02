# Generated by Django 2.2.16 on 2020-12-27 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0004_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_choice', models.CharField(max_length=255)),
                ('second_choice', models.CharField(max_length=255)),
                ('third_choice', models.CharField(max_length=255)),
                ('fourth_choice', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(choices=[(models.CharField(max_length=255), models.CharField(max_length=255)), (models.CharField(max_length=255), models.CharField(max_length=255)), (models.CharField(max_length=255), models.CharField(max_length=255)), (models.CharField(max_length=255), models.CharField(max_length=255))], max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Learning.Question', verbose_name='answers')),
            ],
        ),
    ]
