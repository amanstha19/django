from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=10)


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="classroom_students", null=True, blank=True)

