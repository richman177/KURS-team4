# Generated by Django 5.1.5 on 2025-01-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udemy', '0002_remove_student_student_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(to='udemy.category'),
        ),
    ]
