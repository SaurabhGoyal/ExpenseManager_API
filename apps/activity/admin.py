from django.contrib import admin

from apps.activity.models import ActivityCategory, Activity, UserActivity

admin.site.register(ActivityCategory)
admin.site.register(Activity)
admin.site.register(UserActivity)
