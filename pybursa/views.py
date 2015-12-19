# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib import messages
from courses.models import Course


class PostingApplyForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    body = forms.CharField(
                widget=forms.Textarea,
                initial='Привет! Только до 26.12.2015 для тебя открыт доступ к сайту adbuild.com.ua'
            )


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

def posting(request):
    if request.method == 'POST':
        form = PostingApplyForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                send_mail(
                    'PyBursa теперь доступен!', 
                    form.cleaned_data['body'], 
                    'mail@adbuild.com.ua', 
                    settings.POSTING_ADDRESSES, 
                    fail_silently=False
                )
                message = "Mails was send successfully." 
                messages.success(request, message)
            else:
                message = "You have not admin permissions." 
                messages.success(request, message)
    else:
        form = PostingApplyForm()
    return render(request, 'posting.html', {'form': form})