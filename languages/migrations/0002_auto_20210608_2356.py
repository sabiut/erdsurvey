# Generated by Django 3.2 on 2021-06-08 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswer',
            name='checkanswer',
        ),
        migrations.RemoveField(
            model_name='questionanswer',
            name='textanswer',
        ),
    ]
