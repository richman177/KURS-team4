# Generated by Django 5.1.5 on 2025-01-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udemy', '0005_alter_course_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(related_name='category', to='udemy.category'),
        ),
    ]
