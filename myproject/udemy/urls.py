from .views import *
from django.urls import path, include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'students', StudentViewSet, basename='students'),
router.register(r'teachers', TeacherViewSet, basename='teachers'),
router.register(r'questions', QuestionViewSet, basename='questions'),
router.register(r'exam', ExamViewSet, basename='exam'),
router.register(r'certificate', CertificateViewSet, basename='certificate'),
router.register(r'review', ReviewViewSet, basename='review'),
router.register(r'teacher_review', TeacherReviewViewSet, basename='teacher_review'),
router.register(r'teacher_rating', TeacherRatingViewSet, basename='teacher_rating'),

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('assignment/', AssignmentListAPIView.as_view(), name='assignment_list'),
    path('assignment/<int:pk>/', AssignmentDetailAPIView.as_view(), name='assignment_detail'),
]