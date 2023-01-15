from django.contrib import admin

# Register your models here.

from jobs.models import JobDescription, Applicant

admin.site.register(JobDescription)
admin.site.register(Applicant)