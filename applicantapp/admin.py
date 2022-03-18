from django.contrib import admin

from applicantapp.models import StatusResume, Resume, Education, Experience


admin.site.register(StatusResume)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Experience)