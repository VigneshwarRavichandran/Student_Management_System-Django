from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
	id = models.CharField(max_length=200,  primary_key=True)
	name = models.CharField(max_length=200)

class Subject(models.Model):
	id = models.CharField(max_length=200,  primary_key=True)
	name = models.CharField(max_length=200)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Professor(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Student(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)