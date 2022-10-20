from django import forms
from django.forms import widgets
from DersTakip.models import *



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('program_id', 'course_code', 'course_name_tr', 'course_name_en',
                   'credit_t', 'credit_u', 'credit_ects', 'semester')

        widgets = {
            "program_id": widgets.Select(attrs={"class":"form-control"}),
            "course_code": widgets.NumberInput(attrs={"class":"form-control"}),
            "course_name_tr": widgets.TextInput(attrs={"class":"form-control"}),
            "course_name_en": widgets.TextInput(attrs={"class": "form-control"}),
            "credit_t": widgets.NumberInput(attrs={"class": "form-control"}),
            "credit_u": widgets.NumberInput(attrs={"class": "form-control"}),
            "credit_ects": widgets.NumberInput(attrs={"class": "form-control"}),
            "semester": widgets.NumberInput(attrs={"class": "form-control"}),
        }

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('unit_id','title_tr','short_title_tr','title_en','short_title_en',)

        widgets = {
            "unit_id": widgets.Select(attrs={"class": "form-control"}),
            "title_tr": widgets.TextInput(attrs={"class": "form-control"}),
            "short_title_tr": widgets.TextInput(attrs={"class": "form-control"}),
            "title_en": widgets.TextInput(attrs={"class": "form-control"}),
            "short_title_en": widgets.TextInput(attrs={"class": "form-control"}),

        }

class OpenCourseForm(forms.ModelForm):
    class Meta:
        model = Open_course
        fields = ('course_id','semester_id','instructor_id','num_students','division')

        widgets = {
            "course_id": widgets.Select(attrs={"class": "form-control"}),
            "semester_id": widgets.Select(attrs={"class": "form-control"}),
            "instructor_id": widgets.Select(attrs={"class": "form-control"}),
            "num_students": widgets.NumberInput(attrs={"class": "form-control"}),
            "division": widgets.TextInput(attrs={"class": "form-control"}),

        }

class WeeklyProgramForm(forms.ModelForm):
    class Meta:
        model = Weekly_program
        fields = ("program_id","open_course_id","day_id","start","end","lesson_duration","lesson_break","building","classroom_id")

        widgets = {
            "program_id": widgets.Select(attrs={"class": "form-control"}),
            "open_course_id": widgets.Select(attrs={"class": "form-control"}),
            "day_id": widgets.Select(attrs={"class": "form-control"}),
            "start": widgets.TimeInput(format='%H:%M'),
            "end": widgets.TimeInput(format='%H:%M'),
            "lesson_duration": forms.TextInput(attrs={'min':1,'max': '5','type': 'number', 'placeholder': 'Ders Süresi'}),
            "lesson_break": forms.TextInput(attrs={'min':15,'max': '30','type': 'number', 'placeholder': 'Ders Arası'}),
            "building": widgets.Select(attrs={"class": "form-control"}),
            "classroom_id": widgets.Select(attrs={"class": "form-control"}),
        }

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ("name_tr","name_en",)

        widgets = {
            "name_tr":widgets.TextInput(attrs={"class": "form-control"}),
            "name_en": widgets.TextInput(attrs={"class": "form-control"}),
        }

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ("building", "name_tr","name_en","capacity","exam_capacity","obs_code",)

        widgets = {
            "building": widgets.Select(attrs={"class": "form-control"}),
            "name_tr": widgets.TextInput(attrs={"class": "form-control"}),
            "name_en": widgets.TextInput(attrs={"class": "form-control"}),
            "capacity": widgets.NumberInput(attrs={"class": "form-control"}),
            "exam_capacity": widgets.NumberInput(attrs={"class": "form-control"}),
            "obs_code": widgets.TextInput(attrs={"class": "form-control"}),
        }

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ("title","first_name", "last_name","email")

        widgets = {
            "title": widgets.Select(attrs={"class": "form-control"}),
            "first_name": widgets.TextInput(attrs={"class": "form-control"}),
            "last_name": widgets.TextInput(attrs={"class": "form-control"}),
            "email": widgets.EmailInput(attrs={"class": "form-control"}),

        }


class UserRoleForm(forms.ModelForm):
    class Meta:
        model = User_role
        fields = ("user_id","role_id","unit_id","programs_id",)

        widgets ={
            "user_id": widgets.Select(attrs={"class": "form-control"}),
            "role_id": widgets.Select(attrs={"class": "form-control"}),
            "unit_id": widgets.Select(attrs={"class": "form-control"}),
            "programs_id": widgets.Select(attrs={"class": "form-control"}),

        }


