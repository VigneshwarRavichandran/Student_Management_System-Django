from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate

def login(request):
	context = {
		'error' : None,
	}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			userid = user.id
			return redirect(profile, userid)
		context['error'] = 'Invalid credentials'
		return render(request, 'login.html', context)
	return render(request, 'login.html', context)

def profile(request, userid):
	return render(request, 'profile.html')