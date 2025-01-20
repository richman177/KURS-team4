# Generated by Django 5.1.5 on 2025-01-20 12:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udemy', '0010_userprofile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
        migrations.AddField(
            model_name='student',
            name='student_age',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(65)]),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_age',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(65)]),
        ),
    ]
