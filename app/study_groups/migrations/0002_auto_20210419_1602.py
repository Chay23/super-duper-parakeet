# Generated by Django 3.1.7 on 2021-04-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
