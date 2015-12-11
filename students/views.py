from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

import logging
logger = logging.getLogger(__name__)

class StudentDeleteView(DeleteView):
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        full_name = student.name + ' ' + student.surname
        message = 'Info on %(name)s has been sucessfully deleted.' % {'name': full_name} 
        messages.success(self.request, message)
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)

    model = Student
    success_url = reverse_lazy("students:list_view")


class StudentCreateView(CreateView):
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        full_name = form.cleaned_data['name'] + ' ' + form.cleaned_data['surname']
        message = 'Student %(name)s has been successfully added.' % {'name': full_name} 
        messages.success(self.request, message)
        return super(StudentCreateView, self).form_valid(form)

    model = Student
    success_url = reverse_lazy("students:list_view")


class StudentUpdateView(UpdateView):
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Info on the student has been sucessfully changed.")
        self.student_id = self.request.GET.get('pk', None)
        return super(StudentUpdateView, self).form_valid(form)

    def get_success_url(self):
        student_id = self.kwargs['pk']
        return reverse('students:edit', kwargs={'pk': student_id})

    student_id = 1
    model = Student
    #success_url = reverse_lazy("students:edit", kwargs={'pk': student_id})


class StudentDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        logger.debug("Students detail view has been debugged")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        return context
        
    model = Student


class StudentListView(ListView):
    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs

    model = Student
    paginate_by = 2
