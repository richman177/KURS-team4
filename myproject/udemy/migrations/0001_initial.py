# Generated by Django 5.1.5 on 2025-01-19 13:10

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('status', models.CharField(choices=[('admin', 'admin'), ('student', 'student'), ('teacher', 'teacher')], max_length=16)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64)),
                ('category_name_en', models.CharField(max_length=64, null=True)),
                ('category_name_ru', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('student_image', models.ImageField(blank=True, null=True, upload_to='student_images/')),
                ('student_bio', models.TextField()),
                ('student_status', models.CharField(choices=[('admin', 'admin'), ('student', 'student'), ('teacher', 'teacher')], default='student', max_length=16)),
            ],
            options={
                'verbose_name': 'Students',
                'verbose_name_plural': 'Students_Profile',
            },
            bases=('udemy.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('teacher_image', models.ImageField(blank=True, null=True, upload_to='teacher_images/')),
                ('teacher_bio', models.TextField()),
                ('teacher_education', models.CharField(max_length=150)),
                ('teacher_status', models.CharField(choices=[('admin', 'admin'), ('student', 'student'), ('teacher', 'teacher')], default='teacher', max_length=16)),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers_Profile',
            },
            bases=('udemy.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=64)),
                ('course_name_en', models.CharField(max_length=64, null=True)),
                ('course_name_ru', models.CharField(max_length=64, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('level', models.CharField(choices=[('easy', 'easy'), ('middle', 'middle'), ('high', 'high')], default='student', max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('category', models.ManyToManyField(related_name='category', to='udemy.category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='udemy.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=64)),
                ('lesson_name_en', models.CharField(max_length=64, null=True)),
                ('lesson_name_ru', models.CharField(max_length=64, null=True)),
                ('video_url', models.FileField(blank=True, null=True, upload_to='')),
                ('content', models.TextField()),
                ('content_en', models.TextField(null=True)),
                ('content_ru', models.TextField(null=True)),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.course')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=60)),
                ('option_1', models.CharField(max_length=60)),
                ('option_2', models.CharField(max_length=60)),
                ('option_3', models.CharField(max_length=60)),
                ('option_4', models.CharField(max_length=60)),
                ('correct_option', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='udemy.course')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_title', models.CharField(max_length=64)),
                ('exam_title_en', models.CharField(max_length=64, null=True)),
                ('exam_title_ru', models.CharField(max_length=64, null=True)),
                ('passing_score', models.PositiveSmallIntegerField()),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.course')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.question')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_at', models.DateField(auto_now=True)),
                ('certificate', models.URLField()),
                ('is_verified', models.BooleanField(default=False)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='udemy.course')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='udemy.student')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.student')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.teacher')),
            ],
        ),
    ]
