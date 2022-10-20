from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
UserAdmin.list_display = ("username","first_name","last_name","email","is_staff","is_active",)
UserAdmin.list_display_links = ("username","first_name","last_name","email",)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","title",)
    list_display_links = ("first_name","last_name","email","title",)


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("building","name_tr","name_en","capacity","exam_capacity","obs_code")


class DayAdmin(admin.ModelAdmin):
    list_display = ("day_tr","day_en")
    list_display_links = ("day_tr","day_en")

class TitleAdmin(admin.ModelAdmin):
    list_display = ("title_tr","title_en")


class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name_tr","name_en")




class SemesterAdmin(admin.ModelAdmin):
    list_display = ("year","semesters","semester","start_date","end_date","is_active")


class UnitAdmin(admin.ModelAdmin):
    list_display = ("title_tr","short_title_tr","title_en","short_title_en")

class ProgramAdmin(admin.ModelAdmin):
    list_display = ("unit_id","title_tr","short_title_tr","title_en","short_title_en")

class CourseAdmin(admin.ModelAdmin):
    list_display = ("program_id","course_code","course_name_tr","course_name_en","credit_t","credit_u","credit_ects","semester")

class Open_courseAdmin(admin.ModelAdmin):
    list_display = ("course_id","semester_id","instructor_id","num_students","division")

class RoleAdmin(admin.ModelAdmin):
    list_display = ("role_tr","role_en")

class User_roleAdmin(admin.ModelAdmin):
    list_display = ("user_id","role_id","unit_id","selectedprogram_id")

    def selectedprogram_id (self, obj):
        html = ""

        for program in obj.programs_id.all():
            html += program.title_tr + ", "

        return html



class Weekly_programAdmin(admin.ModelAdmin):
    list_display = ("open_course_id","day_id","start","end","classroom_id")



admin.site.register(Building,BuildingAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Title,TitleAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Unit,UnitAdmin)
admin.site.register(Program,ProgramAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Open_course,Open_courseAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(User_role, User_roleAdmin)
admin.site.register(Weekly_program, Weekly_programAdmin)


