from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.login, name='login'),
	path('profile<userid>/<username>', views.profile, name='profile')
]