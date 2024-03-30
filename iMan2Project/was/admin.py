from django.contrib import admin
from .models import Course, Task, Schedule, Grade

# Register your models here.
admin.site.register(Course)
admin.site.register(Task)
admin.site.register(Schedule)
admin.site.register(Grade)
