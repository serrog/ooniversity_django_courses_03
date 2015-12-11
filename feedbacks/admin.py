from django.contrib import admin
from feedbacks.models import Feedback
from datetime import datetime


class FeedbackAdmin(admin.ModelAdmin):
    def create_time(self, obj):
        return obj.create_date.time()
        
    list_display = ('from_email', 'create_time')


admin.site.register(Feedback, FeedbackAdmin)