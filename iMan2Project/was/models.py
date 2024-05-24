from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.conf import settings
from datetime import datetime, timezone
import os

class Course(models.Model):
    objects = models.Manager()

    CourseID = models.AutoField(primary_key=True)
    CourseImage = models.ImageField(upload_to='uploaded/', default='default/courseplaceholder.png')
    SubjectCode = models.CharField(max_length=255)
    SubjectDescription = models.CharField(max_length=255)
    Section = models.CharField(max_length=255)
    Professor = models.CharField(max_length=255)
    UserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# if course is delete, ma delete ang mga pics associated sa course :)
@receiver(post_delete, sender=Course)
def delete_course_image(sender, instance, **kwargs):
    if instance.CourseImage.name != 'default/courseplaceholder.png':
        if os.path.isfile(instance.CourseImage.path):
            os.remove(instance.CourseImage.path)


class Schedule(models.Model):
    objects = models.Manager()

    ScheduleID = models.AutoField(primary_key=True)
    DayOfWeek = models.CharField(max_length=255)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Room = models.CharField(max_length=255, null=True)
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)


class Task(models.Model):
    objects = models.Manager()

    TaskID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Deadline = models.DateTimeField()
    Type = models.CharField(max_length=255)
    Score = models.DecimalField(max_digits=11, decimal_places=2, default=-1)
    Score_over = models.DecimalField(max_digits=11, decimal_places=2, default=-1)
    isComplete = models.BooleanField(default=False)
    dateCompleted = models.DateTimeField(null=True)
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)

    # return the Date value of the deadline 
    @property
    def Deadline_date(self):
        return self.Deadline.date()
    
    # return the Time value of the deadline 
    @property
    def Deadline_time(self):
        return self.Deadline.time()

    # return the Deadline in a specific string format used for the datetime-local input tag
    @property
    def Deadline_fordatetimelocal(self):
        return self.Deadline.strftime('%Y-%m-%dT%H:%M')

    # boolean value of the task is already late
    @property
    def isLate(self):
        return datetime.today().replace(tzinfo=timezone.utc) > self.Deadline


class Grade(models.Model):
    objects = models.Manager()

    GradeID = models.AutoField(primary_key=True)
    MidtermGrade = models.DecimalField(max_digits=3, decimal_places=1, default=-1)
    FinalGrade = models.DecimalField(max_digits=3, decimal_places=1, default=-1)
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)

