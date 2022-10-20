import django_filters
from .models import *
from django.forms import widgets

class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = ('program_id',)

        widgets = {
            "program_id": widgets.Select(attrs={"class": "form-control"}),
        }
