# Generated by Django 2.2.20 on 2021-06-08 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describtion', models.CharField(max_length=255)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project_group', to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('project_code', models.CharField(max_length=255)),
                ('project_url', models.URLField(max_length=255)),
                ('project_cover', models.ImageField(null=True, upload_to='')),
                ('project_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='mainpage.Group_Team')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Project_tasks', to='mainpage.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='mainpage.Project_Country'),
        ),
        migrations.AddField(
            model_name='group_team',
            name='project_countries',
            field=models.ManyToManyField(related_name='project_groups', to='mainpage.Project_Country'),
        ),
    ]
