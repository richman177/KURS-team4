import rating
from django.db import models
from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.db.models import TextField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

STATUS_CHOICES = (
    ('admin', 'admin'),
    ('student', 'student'),
    ('teacher', 'teacher'),
)


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'



class Student(UserProfile):
    student_image = models.ImageField(null=True, blank=True, upload_to='student_images/')
    student_bio = TextField()
    student_age = models.PositiveSmallIntegerField(validators=[MinValueValidator(10), MaxValueValidator(65)], null=True, blank=True)


    class Meta:
        verbose_name = "Students"
        verbose_name_plural = "Students_Profile"

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Teacher(UserProfile):
    teacher_image = models.ImageField(null=True, blank=True, upload_to='teacher_images/')
    teacher_bio = models.TextField()
    teacher_education = models.CharField(max_length=150)
    teacher_age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(65)], null=True, blank=True)


    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers_Profile"

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    def get_avg_teacher_rating(self):
        teacher_rating = self.rating.all()
        if teacher_rating.exists():
            return round(sum([i.rating for i in teacher_rating if i.rating]) / teacher_rating.count(), 1)
        return 0

    def get_count_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            if ratings.count() > 3:
                return '3+'
            return ratings.count()
        return 0

    def get_good_grade(self):
        ratings = self.reviews.all()
        if ratings.exists():
            total_people = 0
            for i in ratings:
                if i.stars > 3:
                    total_people += 1
            return f'{(total_people * 100) / ratings.count()} %'
        return '0 %'


class TeacherRating(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='rating')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}, {self.teacher}'


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
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.course_name

    def get_avg_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum([i.rating for i in ratings if i.rating]) / ratings.count(), 1)
        return 0

    def get_count_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            if ratings.count() > 3:
                return '3+'
            return ratings.count()
        return 0

    def get_good_grade(self):
        ratings = self.reviews.all()
        if ratings.exists():
            total_people = 0
            for i in ratings:
                if i.rating > 3:
                    total_people += 1
            return f'{round((total_people * 100) / ratings.count(), 1)}%'
        return '0%'


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=64)
    video_url = models.FileField(null=True, blank=True)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.DurationField(default=timedelta(minutes=60))

    def __str__(self):
        return f'{self.lesson_name}'


class Assignment(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Question(models.Model):
    text = models.CharField(max_length=60)
    option_1 = models.CharField(max_length=60)
    option_2 = models.CharField(max_length=60)
    option_3 = models.CharField(max_length=60)
    option_4 = models.CharField(max_length=60)
    correct_option = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return f'{self.text}'

    def check_answer(self, answer_index):
        return answer_index == self.correct_option



class Exam(models.Model):
    exam_title = models.CharField(max_length=64)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    passing_score = models.PositiveSmallIntegerField()
    duration = models.DurationField(default=timedelta(minutes=60))

    def __str__(self):
        return f'{self.exam_title}, {self.course}'


class Option(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)

    def __str__(self):
        return f'{self.teacher}, {self.exam}'

class Certificate(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now=True)
    certificate = models.URLField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student}, {self.course}'


class CourseReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}'


class TeacherReview(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='reviews')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher}, {self.student}'