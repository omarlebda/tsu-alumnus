from django.contrib import admin
from .models import Alumni, Graduation, GraduationProject, Company, Job
# Register your models here.

admin.site.register(Alumni)
admin.site.register(Graduation)
admin.site.register(GraduationProject)
admin.site.register(Company)
admin.site.register(Job)
