from django.contrib import admin
from .models import Profile, FeedBack, Issues 
from django.utils import timezone

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username', )
    list_display = ('user', 'gender', 'days_since_registered', 'is_online')
    list_per_page = 50
    radio_fields = {"gender": admin.HORIZONTAL}
    list_filter = ['gender', 'is_online', ]

    fieldsets = [
    	("User", {"fields": ["user"]}),
        ("Gender", {"fields":["gender"]}),
        ("ProfileImage", {"fields":["image"]}),
      	("Registration_Date", {"fields":["date_registered"]}),
    ]

    def days_since_registered(self, Profile):
        diff = timezone.now() - Profile.date_registered
        return diff.days
    days_since_registered.short_description = 'Active Days'

    # def get_queryset(self, request):
    # 	qs = super().get_queryset(request)
    # 	if request.user.is_superuser:
    # 		return qs
    # 	return qs.filter(department=request.user.profile.department)


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedBack', )
    list_filter = ('user', 'feedBack', )
    search_fields = ('feedBack', )
    list_per_page = 10


class IssuesAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'issue', )
    list_filter = ('type', 'issue', )
    search_fields = ('type', 'issue')
    list_per_page = 10


admin.site.register(Profile, ProfileAdmin)
admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(Issues, IssuesAdmin)
