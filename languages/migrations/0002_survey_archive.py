# Generated by Django 3.2 on 2021-05-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='archive',
            field=models.CharField(default='', max_length=200),
        ),
    ]