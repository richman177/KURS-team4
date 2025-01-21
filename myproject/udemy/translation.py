from .models import Category, Course, Lesson, Exam, Teacher, Student
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('lesson_name', 'content')


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('exam_title',)

@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('teacher_bio',)

@register(Student)
class StudentTranslationOptions(TranslationOptions):
    fields = ('student_bio',)