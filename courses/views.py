from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    lessons = Lesson.objects.filter(course_id=course_id)
    context = {'course': course, 'lessons': lessons}
    return render(request, 'courses/detail.html', context)

def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            name = form.cleaned_data['name']
            message = 'Course %(name)s has been successfully added.' % {'name': name} 
            messages.success(request, message)
            return redirect("index")
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, "The changes have been saved.")
            return redirect("courses:detail", course.id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form':form})

def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    name = course.name
    if request.method == "POST":
        course.delete()
        message = "Course %(name)s has been deleted." % {'name': name} 
        messages.success(request, message)
        return redirect("index")
    return render(request, 'courses/remove.html', {'course': name})

def add_lesson(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            name = lesson.subject
            message = "Lesson %(name)s has been successfully added." % {'name': name}
            messages.success(request, message)
            return redirect("courses:detail", course.id)
    else:
        form = LessonModelForm(initial={'course': course})
    return render(request, "courses/add_lesson.html", {'form': form})
