# Generated by Django 3.2 on 2021-05-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_survey_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_check',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
