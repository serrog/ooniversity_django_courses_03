from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
    
    def first_name(self, obj):
        return obj.user.first_name
    first_name.short_description = "First name"

    def last_name(self, obj):
        return obj.user.last_name
    last_name.short_description = "Last name"

    def is_staff(self, obj):
        return obj.user.is_staff

    list_display = ('first_name', 'last_name', 'gender', 'skype', 'description', )
    list_filter = ['user__is_staff']
    search_fields = ['user__first_name', 'user__last_name', 'gender', 'skype', 'description']

admin.site.register(Coach, CoachAdmin)
