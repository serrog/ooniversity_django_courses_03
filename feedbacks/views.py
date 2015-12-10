from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from feedbacks.models import Feedback
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

class FeedbackView(CreateView):
    def form_valid(self, form):
        recipient_list = [el[1] for el in settings.ADMINS]
        send_mail(
            form.cleaned_data['subject'], 
            form.cleaned_data['message'], 
            form.cleaned_data['from_email'],
            recipient_list, 
            fail_silently=False
        )
        message =  "Thank you for your feedback! We will keep in touch with you very soon!" 
        messages.success(self.request, message)
        return super(FeedbackView, self).form_valid(form)

    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy("feedback")
