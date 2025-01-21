from django_filters import FilterSet
from .models import Course, Category


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'price': ['gt', 'lt'],
        }


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            'category_name': ['exact'],
        }