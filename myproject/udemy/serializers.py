from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CourseSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CourseListSerializer(serializers.ModelSerializer):
    category = CategoryDetailSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    good_grade = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'category', 'price', 'avg_rating', 'good_grade', 'count_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_rating(self, obj):
        return obj.get_count_rating()

    def get_good_grade(self, obj):
        return obj.get_good_grade()


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'lesson_name', 'video_url', 'course']


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['content', 'lesson_name', 'video_url', 'course', 'duration']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'course']


class AssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'course', 'student', 'due_date', 'description']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    course = CourseSimpleSerializer()

    class Meta:
        model = Question
        fields = ['text', 'option_1', 'option_2', 'option_3', 'option_4',
                  'correct_option', 'course']



class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class CertificateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'course', 'student', 'certificate', 'issued_at', 'is_verified']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'course', 'student', 'certificate', 'issued_at', 'is_verified']

class CertificateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'course', 'student', 'certificate', 'issued_at', 'is_verified']


class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TeacherReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherReview
        fields = '__all__'


class TeacherRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherRating
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    avg_teacher_rating = serializers.SerializerMethodField()
    good_grade = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'teacher_education', 'avg_teacher_rating', 'good_grade', 'count_rating']

    def get_avg_teacher_rating(self, obj):
        return obj.get_avg_teacher_rating()

    def get_count_rating(self, obj):
        return obj.get_count_rating()

    def get_good_grade(self, obj):
        return obj.get_good_grade()


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategoryDetailSerializer()
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['course_name', 'category', 'level', 'description', 'price', 'created_by',
                  'created_at', 'updated_at', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()