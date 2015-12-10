from django.contrib import admin
from feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_email')


admin.site.register(Feedback, FeedbackAdmin)