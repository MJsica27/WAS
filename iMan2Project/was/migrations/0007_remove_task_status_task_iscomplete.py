# Generated by Django 5.0.3 on 2024-04-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('was', '0006_schedule_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Status',
        ),
        migrations.AddField(
            model_name='task',
            name='isComplete',
            field=models.BooleanField(default=False),
        ),
    ]
