# Generated by Django 2.2.16 on 2021-01-02 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0020_auto_20210102_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Learning.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Learning.Student')),
            ],
        ),
    ]
