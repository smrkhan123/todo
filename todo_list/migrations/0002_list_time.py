# Generated by Django 2.2.4 on 2019-08-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
