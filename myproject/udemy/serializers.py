from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учутные данные")


    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user':{
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CourseSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name']

class StudentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['last_name', 'first_name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CourseListSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer()
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
        fields = ['lesson_name', 'video_url', 'content', 'course', 'duration']


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


class ExamSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['exam_title']



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

class TeacherSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['last_name', 'first_name']


class TeacherReviewSerializer(serializers.ModelSerializer):
    student = StudentSimpleSerializer()
    teacher = TeacherSimpleSerializer()
    exam = ExamSimpleSerializer()
    class Meta:
        model = TeacherReview
        fields = ['teacher','student', 'exam', 'stars']


class TeacherRatingSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y'))
    student = StudentSimpleSerializer()
    teacher = TeacherSimpleSerializer()
    class Meta:
        model = TeacherRating
        fields = ['student', 'teacher', 'rating', 'comment', 'created_date']



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
    category = CategorySimpleSerializer()
    avg_rating = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format('%d-%m-%Y'))
    updated_at = serializers.DateTimeField(format('%d-%m-%Y'))
    lesson_course = LessonDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['course_name', 'category', 'level', 'description', 'price', 'created_by',
                  'created_at', 'updated_at', 'avg_rating','lesson_course']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_course = CourseDetailSerializer(many=True, read_only=True)


    class Meta:
        model = Category
        fields = ['category_name', 'category_course']