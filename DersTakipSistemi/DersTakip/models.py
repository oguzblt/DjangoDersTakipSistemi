from django.db import models
import datetime as dt
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, AbstractUser


class Building(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name_tr = models.CharField(max_length=255, null=True)
    name_en = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name_tr


class Classroom(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name_tr = models.CharField(max_length=255, null=True)
    name_en = models.CharField(max_length=255, null=True)
    capacity = models.IntegerField(null=True)
    exam_capacity = models.IntegerField(null=True)
    obs_code = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name_tr} "



class Day(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    day_tr = models.CharField(max_length=15, null=True)
    day_en = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.day_tr




class Title(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    title_tr = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)


    def __str__(self):
        return self.title_tr


class Instructor(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.title} {self.first_name} {self.last_name} "



class Semester(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    year = models.CharField(max_length=255, null=True)
    semesters = models.CharField(max_length=255, null=True)
    semester = models.IntegerField(null=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    is_active = models.BooleanField(null=True)

    def __str__(self):
        return f" {self.year} {self.semesters}"


class Unit(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    title_tr = models.CharField(max_length=255, null=False)
    short_title_tr = models.CharField(max_length=255, null=False)
    title_en = models.CharField(max_length=255, null=False)
    short_title_en = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.title_tr} "


class Program(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE, null=False)
    title_tr = models.CharField(max_length=255, null=False)
    short_title_tr = models.CharField(max_length=255, null=False)
    title_en = models.CharField(max_length=255, null=False)
    short_title_en = models.CharField(max_length=255, null=False)


    def __str__(self):
        return f"{self.title_tr} "


class Course(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=255, null=True)
    course_name_tr = models.CharField(max_length=255, null=True)
    course_name_en = models.CharField(max_length=255, null=True)
    credit_t = models.IntegerField(null=True)
    credit_u = models.IntegerField(null=True)
    credit_ects = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)


    def __str__(self):
        return f"{self.course_name_tr} "


class Open_course(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    num_students = models.IntegerField(null=True)
    division = models.CharField(max_length=255)

    def __str__(self):
        return str(self.course_id)


class Role(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    role_tr = models.CharField(max_length=255, null=True)
    role_en = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.role_tr


class User_role(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE)
    programs_id = models.ManyToManyField(Program)

class Weekly_program(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    open_course_id = models.ForeignKey(Open_course, on_delete=models.CASCADE)
    day_id = models.ForeignKey(Day, on_delete=models.CASCADE)
    start = models.TimeField(default=dt.time(00, 00))
    end = models.TimeField(default=dt.time(00, 00))
    lesson_duration = models.IntegerField(null=True)
    lesson_break = models.IntegerField(null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)



