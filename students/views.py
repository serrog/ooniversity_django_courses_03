from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

def detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {'student': student}
    return render(request, 'students/detail.html', context)

def list_view(request):
    course_id = request.GET.get('course_id', None)
    if course_id:
        students = Course.objects.get(pk=course_id).student_set.all()
    else:
        students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/list.html', context)

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            full_name = form.cleaned_data['name'] + ' ' + form.cleaned_data['surname']
            message = 'Student %(name)s has been successfully added.' % {'name': full_name} 
            messages.success(request, message)
            return redirect("students:list_view")
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Info on the student has been sucessfully changed.")
            return redirect("students:edit", student.id)
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form':form})

def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    full_name = student.name + ' ' + student.surname
    if request.method == "POST":
        student.delete()
        message = "Info on %(name)s has been sucessfully deleted." % {'name': full_name} 
        messages.success(request, message)
        return redirect("students:list_view")
    return render(request, 'students/remove.html', {'student': full_name})