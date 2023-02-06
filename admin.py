from django.contrib import admin
from .models import Student,teacher,batch,Semester

# Register your models here.


class Batch_display(admin.ModelAdmin):
    list_display=['batch']
   


class sem_display(admin.ModelAdmin):
    list_display=['sem']

class teacher_display(admin.ModelAdmin):
    list_display=['name']


class Student_display(admin.ModelAdmin):
    list_display=['name','age','sem','batch','teacher']





admin.site.register(batch,Batch_display)
admin.site.register(Semester,sem_display)
admin.site.register(teacher,teacher_display)
admin.site.register(Student,Student_display)


