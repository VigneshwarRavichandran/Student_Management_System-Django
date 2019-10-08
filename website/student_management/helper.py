from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import *

def add_student(username, password, email, departmentid):
	user = User.objects.create_user(username, email, password)
	user.save()
	student = Student(user_id=user.id, department_id=departmentid)
	student.save()

def add_professor(username, password, email, subjectid):
	user = User.objects.create_user(username, email, password)
	user.save()
	professor = Professor(user_id=user.id, subject_id=subjectid)
	professor.save()

def is_professor(userid):
	user = Professor.objects.filter(user_id=userid)
	if user:
		return True
	return False

def is_superuser(userid):
	user = User.objects.get(id=userid)
	if user.is_superuser:
		return True
	return False

def list_students(userid):
	professor = Professor.objects.get(user_id=userid)
	department_id = professor.subject.department_id
	students = Student.objects.filter(department_id=department_id).values()
	return students

def list_subjects(userid):
	student = Student.objects.get(user_id=userid)
	department_id = student.department_id
	subjects = Subject.objects.filter(department_id=department_id).values()
	return subjects

def list_professors(userid):
	subjects = list_subjects(userid)
	professors = Professor.objects.all()
	student_professors = []
	subject_ids = []
	for subject in subjects:
		subject_ids.append(subject['id'])
	for professor in professors:
		if professor.subject_id in subject_ids:
			student_professors.append([professor.id, professor.user.username, professor.subject.name])
	return student_professors