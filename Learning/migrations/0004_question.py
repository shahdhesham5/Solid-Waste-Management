# Generated by Django 2.2.16 on 2020-12-27 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0003_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Learning.Exam', verbose_name='question')),
            ],
        ),
    ]
