from django.db import models
from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.db.models import TextField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    STATUS_CHOICES = (
        ('admin', 'admin'),
        ('student', 'student'),
        ('teacher', 'teacher'),
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='student')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Student(UserProfile):
    student_image = models.ImageField(null=True, blank=True, upload_to='student_images/')
    student_bio = TextField()

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Teacher(UserProfile):
    teacher_image = models.ImageField(null=True, blank=True, upload_to='teacher_images/')
    teacher_bio = TextField()

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=64)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    course_name = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    LEVEL_CHOICES = (

        ('easy', 'easy'),
        ('middle', 'middle'),
        ('high', 'high'),
    )

    level = models.CharField(max_length=16, choices=LEVEL_CHOICES, default='student')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.course_name


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=64)
    video_url = models.FileField(null=True, blank=True)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Assignment(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return


class Option(models.Model):
    option = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)])


class Questions(models.Model):
    title = models.CharField(max_length=64)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)


class Exam(models.Model):
    exam_title = models.CharField(max_length=64)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    passing_score = models.PositiveSmallIntegerField()
    duration = models.DurationField(default=timedelta(minutes=60))


class Certificate(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now=True)
    certificate = models.URLField()

    def __str__(self):
        return f'{self.student}, {self.course}'


class Review(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)