# Generated by Django 4.2.5 on 2023-09-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_remove_todo_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]