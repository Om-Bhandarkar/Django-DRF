# Generated by Django 4.2.13 on 2025-05-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_app', '0002_interviewexperience_interview_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewexperience',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='interviewexperience',
            name='position',
            field=models.CharField(max_length=50),
        ),
    ]
