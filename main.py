from django.contrib.auth.models import AbstractUser
from django.db import models

# Колдонуучунун кеңейтилген модели
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Instructor', 'Instructor'),
        ('Admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Student')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)  # Колдонуучу текшерилгенби?
    email_verified_at = models.DateTimeField(null=True, blank=True)  # Email текшерилген убакыт

    def __str__(self):
        return f"{self.username} ({self.role})"

# Категориялар (негизги категориялар)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Подкатегориялар
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category.name} -> {self.name}"

# Курс үчүн деңгээлдер
class CourseLevel(models.TextChoices):
    BEGINNER = 'Beginner', 'Beginner'
    INTERMEDIATE = 'Intermediate', 'Intermediate'
    ADVANCED = 'Advanced', 'Advanced'

# Курс модели
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, related_name='courses')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor_courses', limit_choices_to={'role': 'Instructor'})
    level = models.CharField(max_length=20, choices=CourseLevel.choices, default=CourseLevel.BEGINNER)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prerequisites = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def final_price(self):
        return self.discount_price if self.discount_price else self.price

    def publish(self):
        """Курсты жарыялоо"""
        self.published_at = models.DateTimeField(auto_now_add=True)
        self.save()

# Сабак модели
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField()
    duration = models.DurationField()  # Сабактын узактыгы

    def __str__(self):
        return f"{self.course.title} - {self.title}"

# Курстагы прогресс
class Progress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress', limit_choices_to={'role': 'Student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='progress')
    completed_lessons = models.ManyToManyField(Lesson, related_name='completed_by_students', blank=True)
    completion_percentage = models.FloatField(default=0.0)
    is_completed = models.BooleanField(default=False)

    def update_progress(self):
        total_lessons = self.course.lessons.count()
        if total_lessons > 0:
            completed = self.completed_lessons.count()
            self.completion_percentage = (completed / total_lessons) * 100
            if self.completion_percentage == 100:
                self.is_completed = True
            self.save()

    def __str__(self):
        return f"{self.student.username} - {self.course.title}: {self.completion_percentage}%"

# Комментарий жана баалоо модели
class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', limit_choices_to={'role': 'Student'})
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.title} ({self.rating})"

# Төлөм модели
class Payment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments', limit_choices_to={'role': 'Student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    is_successful = models.BooleanField(default=True)
    payment_method = models.CharField(max_length=100)  # Төлөм ыкмасы (мисалы, Credit Card, PayPal)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.title} (${self.amount})"

# Сертификат модели
class Certificate(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates', limit_choices_to={'role': 'Student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates')
    certificate_url = models.URLField()
    issued_date = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.course.title} Certificate"

# Колдонуучунун билдирүүлөрү
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=50, choices=[('Info', 'Info'), ('Alert', 'Alert')])

    def __str__(self):
        return f"{self.user.username} - {self.message[:50]}"

# FAQ (Часто задаваемые вопросы)
class FAQ(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return f"FAQ for {self.course.title}: {self.question[:50]}"

# Контактты жана керектүү жардам (Support)
class SupportTicket(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_tickets', limit_choices_to={'role': 'Student'})
    issue = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    is_resolved = models.BooleanField(default=False)
    resolution = models.TextField(blank=True, null=True)

    def resolve(self, resolution):
        """Тикетти чечүү жана акыркы жыйынтыгын жазуу."""
        self.is_resolved = True
        self.resolution = resolution
        self.resolved_at = models.DateTimeField(auto_now=True)
        self.save()

    def __str__(self):
        return f"Ticket by {self.student.username} - {'Resolved' if self.is_resolved else 'Pending'}"