# Generated by Django 3.0.5 on 2020-04-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]