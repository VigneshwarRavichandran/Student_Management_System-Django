from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .helper import *

def login(request):
	context = {
		'error' : None,
	}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			return redirect(profile, user.id, user)
		context['error'] = 'Invalid credentials'
		return render(request, 'login.html', context)
	return render(request, 'login.html', context)

def profile(request, userid, username):
	context = {
		'username' : username,
		'userid' : userid,
	}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('password')
		response = None
		if 'add_student' in request.POST:
			departmentid = request.POST.get('departmentid')
			add_student(username, password, email, departmentid)
			response = 'Created Student Profile'
		elif 'add_professor' in request.POST:
			subjectid = request.POST.get('subjectid')
			add_professor(username, password, email, subjectid)
			response = 'Created Professor Profile'
		elif 'list_students' in request.POST:
			response = list_students(userid)
		elif 'list_subjects' in request.POST:
			response = list_subjects(userid)
		elif 'list_professors' in request.POST:
			reponse = list_professors(userid)
		return HttpResponse(response)
	if is_superuser(userid):
		context['user'] = 'superuser'
	elif is_professor(userid):
		context['user'] = 'professor'
	else:
		context['user'] = 'student'
	return render(request, 'profile.html', context)