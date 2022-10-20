from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from DersTakip.form import *
from .filters import *


def index(request):
    return render(request, 'index.html')

@login_required(login_url='/account/login')
def indexadmin(request):
    return render(request, 'indexadmin.html')

@login_required(login_url='/account/login')
def bolumler(request):
    program = Program.objects.all()
    return render(request, 'dashbord/bolumler.html',{
        "program": program,
    })

@login_required(login_url='/account/login')
def dersler(request):
    courses = Course.objects.all()
    my_filter = CourseFilter(request.GET, queryset=courses)
    courses = my_filter.qs
    return render(request, 'dashbord/dersler.html',{
        "courses": courses,
        "my_filter": my_filter,
    })

@login_required(login_url='/account/login')
def acilandersler(request):
    open_courses = Open_course.objects.all()
    return render(request, 'dashbord/acilandersler.html',{
        "open_courses": open_courses,

    })


@login_required(login_url='/account/login')
def haftalikprogram(request):
    weekly_program = Weekly_program.objects.all()
    day = Day.objects.all()
    return render(request,'dashbord/haftalıkprogram.html',{
        "weekly_program" : weekly_program,
        "day" : day,
    })

def yerleske(request):
    building = Building.objects.all()
    return render(request,'dashbord/yerleske.html',{
        "building" : building,
    })

def sinif(request):
    classroom = Classroom.objects.all()
    return render(request,'dashbord/sınıf.html',{
        "classroom" : classroom,
    })

def hoca(request):
    instructor = Instructor.objects.all()
    return render(request,'dashbord/hoca.html',{
        "instructor" : instructor,
    })

def bolumadmin(request):
    program = Program.objects.all()
    return render(request, 'dashbord/bolumadmin.html', {
        "program": program,
    })

def dersadmin(request):
    courses = Course.objects.all()
    my_filter = CourseFilter(request.GET, queryset=courses)
    courses = my_filter.qs
    return render(request, 'dashbord/dersadmin.html',{
        "courses": courses,
        "my_filter": my_filter,
    })

def acilandersleradmin(request):
    open_courses = Open_course.objects.all()
    return render(request, 'dashbord/acilandersleradmin.html',{
        "open_courses": open_courses,

    })

def dersekle(request):
    form = CourseForm
    program = Program.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Ders başarıyla eklendi!")
            return redirect("dersler")
        else:
            form = CourseForm()

    return render(request, 'crud/dersekle.html', {
        "program" :program,
        "form" : form
    })

def dersduzenle(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            messages.success(request, "Ders başarıyla düzenlendi!")
            return redirect("dersler")

    else:
        form = CourseForm(instance=course)

    return render(request, "crud/dersduzenle.html", {
        "form": form
    })

def derssil(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        course.delete()
        messages.success(request, "Ders başarıyla silindi!")
        return redirect("dersler")

    return render(request, "crud/derssil.html", {
        "course": course
    })

def dersadminekle(request):
    form = CourseForm
    program = Program.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Ders başarıyla eklendi!")
            return redirect("dersadmin")
        else:
            form = CourseForm()

    return render(request, 'crud/dersadminekle.html', {
        "program" :program,
        "form" : form
    })

def dersadminduzenle(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            messages.success(request, "Ders başarıyla düzenlendi!")
            return redirect("dersadmin")

    else:
        form = CourseForm(instance=course)

    return render(request, "crud/dersadminduzenle.html", {
        "form": form
    })

def dersadminsil(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        course.delete()
        messages.success(request, "Ders başarıyla silindi!")
        return redirect("dersadmin")

    return render(request, "crud/dersadminsil.html", {
        "course": course
    })

def bolumekle(request):
    form = ProgramForm
    if request.method == 'POST':
        form = ProgramForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Bölüm başarıyla eklendi!")
            return redirect("bolumler")
        else:
            form = ProgramForm()

    return render(request, 'crud/bolumekle.html', {

        "form" : form
    })

def bolumduzenle(request, id):
    program = get_object_or_404(Program, pk=id)

    if request.method == "POST":
        form = ProgramForm(request.POST, instance=program)

        if form.is_valid():
            form.save()
            messages.success(request, "Bölüm başarıyla düzenlendi!")
            return redirect("bolumler")

    else:
        form = ProgramForm(instance=program)

    return render(request, "crud/bolumduzenle.html", {
        "form": form
    })

def bolumsil(request, id):
    program = get_object_or_404(Program, pk=id)

    if request.method == "POST":
        program.delete()
        messages.success(request, "Bölüm başarıyla silindi!")
        return redirect("bolumler")

    return render(request, "crud/bolumsil.html", {
        "program": program
    })

def bolumadminekle(request):
    form = ProgramForm
    if request.method == 'POST':
        form = ProgramForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Bölüm başarıyla eklendi!")
            return redirect("bolumadmin")
        else:
            form = ProgramForm()

    return render(request, 'crud/bolumadminekle.html', {

        "form" : form
    })

def bolumadminduzenle(request, id):
    program = get_object_or_404(Program, pk=id)

    if request.method == "POST":
        form = ProgramForm(request.POST, instance=program)

        if form.is_valid():
            form.save()
            messages.success(request, "Bölüm başarıyla düzenlendi!")
            return redirect("bolumadmin")

    else:
        form = ProgramForm(instance=program)

    return render(request, "crud/bolumadminduzenle.html", {
        "form": form
    })

def bolumadminsil(request, id):
    program = get_object_or_404(Program, pk=id)

    if request.method == "POST":
        program.delete()
        messages.success(request, "Bölüm başarıyla silindi!")
        return redirect("bolumadmin")

    return render(request, "crud/bolumadminsil.html", {
        "program": program
    })

def acilandersekle(request):
    form = OpenCourseForm
    if request.method == 'POST':
        form = OpenCourseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Ders başarıyla eklendi!")
            return redirect("acilandersler")
        else:
            form = OpenCourseForm()

    return render(request, 'crud/acilandersekle.html', {
        "form" : form
    })

def acilandersduzenle(request, id):
    open_course = get_object_or_404(Open_course, pk=id)

    if request.method == "POST":
        form = OpenCourseForm(request.POST, instance=open_course)

        if form.is_valid():
            form.save()
            messages.success(request, "Ders başarıyla düzenlendi!")
            return redirect("acilandersler")

    else:
        form = OpenCourseForm(instance=open_course)

    return render(request, "crud/acilandersduzenle.html", {
        "form": form
    })

def acilanderssil(request, id):
    open_course = get_object_or_404(Open_course, pk=id)

    if request.method == "POST":
        open_course.delete()
        messages.success(request, "Ders başarıyla silindi!")
        return redirect("acilandersler")

    return render(request, "crud/acilanderssil.html", {
        "open_course": open_course
    })

def acilandersadminekle(request):
    form = OpenCourseForm
    if request.method == 'POST':
        form = OpenCourseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Ders başarıyla eklendi!")
            return redirect("acilandersleradmin")
        else:
            form = OpenCourseForm()

    return render(request, 'crud/acilandersadminekle.html', {
        "form" : form
    })

def acilandersadminduzenle(request, id):
    open_course = get_object_or_404(Open_course, pk=id)

    if request.method == "POST":
        form = OpenCourseForm(request.POST, instance=open_course)

        if form.is_valid():
            form.save()
            messages.success(request, "Ders başarıyla düzenlendi!")
            return redirect("acilandersleradmin")

    else:
        form = OpenCourseForm(instance=open_course)

    return render(request, "crud/acilandersadminduzenle.html", {
        "form": form
    })

def acilandersadminsil(request, id):
    open_course = get_object_or_404(Open_course, pk=id)

    if request.method == "POST":
        open_course.delete()
        messages.success(request, "Ders başarıyla silindi!")
        return redirect("acilandersleradmin")

    return render(request, "crud/acilandersadminsil.html", {
        "open_course": open_course
    })

def haftalikprogramekle(request):
    form = WeeklyProgramForm
    weekly_program = Weekly_program.objects.all()
    if request.method == 'POST':
        form = WeeklyProgramForm(request.POST)


        if form.is_valid():
            form.save()
            messages.success(request, "Haftalık program başarıyla eklendi!")
            return redirect("haftalıkprogram")
        else:
            form = WeeklyProgramForm()

    return render(request, 'crud/haftalikprogramekle.html', {
        "weekly_program" : weekly_program,
        "form" : form
    })

def haftalikprogramduzenle(request, id):
    weekly_program = get_object_or_404(Weekly_program, pk=id)

    if request.method == "POST":
        form = WeeklyProgramForm(request.POST, instance=weekly_program)

        if form.is_valid():
            form.save()
            messages.success(request, "Haftalık program başarıyla düzenlendi!")
            return redirect("haftalıkprogram")

    else:
        form = WeeklyProgramForm(instance=weekly_program)

    return render(request, "crud/haftalikprogramduzenle.html", {
        "form": form
    })

def haftalikprogramsil(request, id):
    weekly_program = get_object_or_404(Weekly_program, pk=id)

    if request.method == "POST":
        weekly_program.delete()
        messages.success(request, "Haftalık program başarıyla silindi!")
        return redirect("haftalıkprogram")

    return render(request, "crud/haftalikprogramsil.html", {
        "weekly_program": weekly_program
    })

def yerleskeekle(request):
    form = BuildingForm
    if request.method == 'POST':
        form = BuildingForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Yerleske başarıyla eklendi!")
            return redirect("yerleske")
        else:
            form = CourseForm()

    return render(request, 'crud/yerleskeekle.html', {
        "form" : form
    })

def yerleskeduzenle(request, id):
    building = get_object_or_404(Building, pk=id)

    if request.method == "POST":
        form = BuildingForm(request.POST, instance=building)

        if form.is_valid():
            form.save()
            messages.success(request, "Yerleşke başarıyla düzenlendi!")
            return redirect("yerleske")

    else:
        form = BuildingForm(instance=building)

    return render(request, "crud/yerleskeduzenle.html", {
        "form": form
    })

def yerleskesil(request, id):
    building = get_object_or_404(Building, pk=id)

    if request.method == "POST":
        building.delete()
        messages.success(request, "Yerleşke başarıyla silindi!")
        return redirect("yerleske")

    return render(request, "crud/yerleskesil.html", {
        "building": building
    })

def sinifekle(request):
    form = ClassroomForm
    if request.method == 'POST':
        form = ClassroomForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Sınıf bilgisi başarıyla eklendi!")
            return redirect("sinif")
        else:
            form = ClassroomForm()

    return render(request, 'crud/sınıfekle.html', {
        "form" : form
    })

def sinifduzenle(request, id):
    classroom = get_object_or_404(Classroom, pk=id)

    if request.method == "POST":
        form = ClassroomForm(request.POST, instance=classroom)

        if form.is_valid():
            form.save()
            messages.success(request, "Sınıf bilgisi başarıyla düzenlendi!")
            return redirect("sinif")

    else:
        form = ClassroomForm(instance=classroom)

    return render(request, "crud/sınıfduzenle.html", {
        "form": form
    })

def sinifsil(request, id):
    classroom = get_object_or_404(Classroom, pk=id)

    if request.method == "POST":
        classroom.delete()
        messages.success(request, "Sınıf bilgisi başarıyla silindi!")
        return redirect("sinif")

    return render(request, "crud/sinifsil.html", {
        "classroom": classroom
    })

def hocaekle(request):
    form = InstructorForm
    if request.method == 'POST':
        form = InstructorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Hoca bilgisi başarıyla eklendi!")
            return redirect("hoca")
        else:
            form = InstructorForm()

    return render(request, 'crud/hocaekle.html', {
        "form" : form
    })

def hocaduzenle(request, id):
    instructor = get_object_or_404(Instructor, pk=id)

    if request.method == "POST":
        form = InstructorForm(request.POST, instance=instructor)

        if form.is_valid():
            form.save()
            messages.success(request, "Hoca bilgisi başarıyla düzenlendi!")
            return redirect("hoca")

    else:
        form = InstructorForm(instance=instructor)

    return render(request, "crud/hocaduzenle.html", {
        "form": form
    })

def hocasil(request, id):
    instructor = get_object_or_404(Instructor, pk=id)

    if request.method == "POST":
        instructor.delete()
        messages.success(request, "Hoca bilgisi başarıyla silindi!")
        return redirect("hoca")

    return render(request, "crud/hocasil.html", {
        "instructor": instructor
    })