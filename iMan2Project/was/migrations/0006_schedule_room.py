# Generated by Django 5.0.2 on 2024-03-30 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('was', '0005_alter_grade_finalgrade_alter_grade_midtermgrade'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='Room',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
