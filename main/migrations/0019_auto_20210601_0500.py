# Generated by Django 2.2.20 on 2021-06-01 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210601_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_country',
            name='Project_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_locations', to='main.Project_Team'),
        ),
    ]
