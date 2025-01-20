# Generated by Django 5.1.5 on 2025-01-20 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udemy', '0006_alter_review_course_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherrating',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='udemy.teacher'),
        ),
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='udemy.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
