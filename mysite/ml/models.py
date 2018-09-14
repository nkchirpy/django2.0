from django.db import models
from django.urls import reverse
# Create your models here.


class School(models.Model):

    name = models.CharField(max_length=100)

    def get_absolute_url(self):

        return reverse('school', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Student(models.Model):

    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    school_id = models.ForeignKey(
        School, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):

        return reverse('student', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name

    # class Meta:
    #     ordering = ('student_id',)
