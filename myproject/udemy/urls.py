from .views import *
from django.urls import path, include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'students', StudentViewSet, basename='students'),
router.register(r'teachers', TeacherViewSet, basename='teachers'),
router.register(r'questions', QuestionViewSet, basename='questions'),
router.register(r'exam', ExamViewSet, basename='exam'),
router.register(r'option', OptionViewSet, basename='option'),
router.register(r'review', CourseReviewViewSet, basename='review'),
router.register(r'teacher_review', TeacherReviewViewSet, basename='teacher_review'),
router.register(r'teacher_rating', TeacherRatingViewSet, basename='teacher_rating'),

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),

    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('course/create/<int:pk>/', CourseEDITAPIView.as_view(), name='course_edit'),

    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/create/<int:pk>/', LessonEDITAPIView.as_view(), name='lesson_edit'),

    path('assignment/', AssignmentListAPIView.as_view(), name='assignment_list'),
    path('assignment/<int:pk>/', AssignmentDetailAPIView.as_view(), name='assignment_detail'),
    path('assignment/create/', LessonCreateAPIView.as_view(), name='assignment_create'),
    path('assignment/create/<int:pk>/', AssignmentEDITAPIView.as_view(), name='assignment_edit'),

    path('certificate/', CertificateListAPIView.as_view(), name='certificate_list'),
    path('certificate/<int:pk>/', CertificateDetailAPIView.as_view(), name='certificate_detail'),
    path('certificate/create/', CertificateCreateAPIView.as_view(), name='certificate_create'),
    path('certificate/create/<int:pk>/', CertificateEDITAPIView.as_view(), name='certificate_edit'),

    path('questions/create/', QuestionCreateAPIView.as_view(), name='questions_create'),
    path('questions/create/<int:pk>/', QuestionEDITAPIView.as_view(), name='questions_edit'),

    path('exam/create/', ExamCreateAPIView.as_view(), name='exam_create'),
    path('exam/create/<int:pk>/', ExamEDITAPIView.as_view(), name='exam_edit'),
]