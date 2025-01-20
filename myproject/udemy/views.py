from .permissions import CheckCreateCourse,GiveCertificate,CreateCertificate, CheckUser
from .serializers import *
from .models import *
from rest_framework import viewsets, generics
from .filters import CourseFilter,CategoryFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [CheckUser]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CategoryFilter


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer



class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['course_name',]
    ordering_fields = ['updated_at',]


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [CheckCreateCourse]


class CourseEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [CheckCreateCourse]



class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer


class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [CheckCreateCourse]


class AssignmentListAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentListSerializer


class AssignmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer

class AssignmentCreateAPIView(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer



class AssignmentEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Assignment.objects.all()
    serializer_class =  AssignmentSerializer
    permission_classes = [CheckCreateCourse]



class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [CheckCreateCourse]


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamCreateAPIView(generics.CreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [CheckCreateCourse]


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class CertificateListAPIView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateListSerializer
    permission_classes = [GiveCertificate]


class CertificateDetailAPIView(generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateDetailSerializer

class CertificateCreateAPIView(generics.CreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [CreateCertificate]


class CertificateEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [CreateCertificate]

class CourseReviewViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer

class TeacherReviewViewSet(viewsets.ModelViewSet):
    queryset = TeacherReview.objects.all()
    serializer_class = TeacherReviewSerializer

class TeacherRatingViewSet(viewsets.ModelViewSet):
    queryset = TeacherRating.objects.all()
    serializer_class = TeacherRatingSerializer