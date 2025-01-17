from .views import *
from django.urls import path, include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'students', StudentViewSet, basename='students'),
router.register(r'teachers', TeacherViewSet, basename='teachers'),
router.register(r'category', CategoryViewSet, basename='category'),
router.register(r'course', CourseViewSet, basename='course'),
router.register(r'lessens', LessonViewSet, basename='lessens'),
router.register(r'assignment', AssignmentViewSet, basename='assignment'),
router.register(r'option', OptionViewSet, basename='option'),
router.register(r'questions', QuestionsViewSet, basename='questions'),
router.register(r'exam', ExamViewSet, basename='exam'),
router.register(r'certificate', CertificateViewSet, basename='certificate'),
router.register(r'review', ReviewViewSet, basename='review'),


urlpatterns = [
    path('', include(router.urls)),
]