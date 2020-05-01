from django.conf import settings
from django.db import models
from django.urls import reverse

from users.models import Doctor, Patient


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class Comment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='comments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('doctor')


'''class Time(models.Model):
    available_time = models.TimeField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)'''
