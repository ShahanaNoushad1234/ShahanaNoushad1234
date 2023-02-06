from django.db import models

# Create your models here.

class Semester(models.Model):
    sem=models.CharField(max_length=500)
    def __str__(self):
        return self.sem
    

class batch(models.Model):
    batch=models.CharField(max_length=500)
    def __str__(self):
        return self.batch

class teacher(models.Model):
    name=models.CharField(max_length=500)
    def __str__(self):
        return self.name


class Student(models.Model):
    name=models.CharField(max_length=500)
    age=models.CharField(max_length=500)
    admission=models.IntegerField()
    sem=models.ForeignKey("Semester", on_delete=models.CASCADE,default=1)
    batch=models.ForeignKey("batch",  on_delete=models.CASCADE,default=1)
    teacher=models.ForeignKey("teacher", on_delete=models.CASCADE,default=1)
