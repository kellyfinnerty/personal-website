# Generated by Django 3.0.5 on 2020-04-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='current',
            field=models.BooleanField(default=True),
        ),
    ]
