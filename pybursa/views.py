from django.shortcuts import render
from courses.models import Course


def index(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')