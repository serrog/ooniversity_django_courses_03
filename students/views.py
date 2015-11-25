from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
from courses.models import Course

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