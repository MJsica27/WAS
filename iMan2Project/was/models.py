from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    objects = models.Manager()

    CourseID = models.AutoField(primary_key=True)
    SubjectCode = models.CharField(max_length=255)
    SubjectDescription = models.CharField(max_length=255)
    Section = models.CharField(max_length=255)
    Professor = models.CharField(max_length=255)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)


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
    Score = models.DecimalField(max_digits=11, decimal_places=2)
    Status = models.CharField(max_length=255)
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)


class Grade(models.Model):
    objects = models.Manager()

    GradeID = models.AutoField(primary_key=True)
    MidtermGrade = models.DecimalField(max_digits=1, decimal_places=1)
    FinalGrade = models.DecimalField(max_digits=1, decimal_places=1)
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)
