from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Lesson

def detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    lessons = Lesson.objects.filter(course_id=course_id)
    context = {'course': course, 'lessons': lessons}
    return render(request, 'courses/detail.html', context)

