from django_filters import FilterSet
from .models import Course


class CategoryFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'price': ['gt', 'lt']
        }