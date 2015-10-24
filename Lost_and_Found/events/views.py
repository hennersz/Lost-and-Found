from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.conf import settings
from django.shortcuts import redirect

#Other functions
def logUserIn(username, password):
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect('events/index.html')
		else:
			error_message = "The password is valid, but the account has been disabled!"
			return render(request, 'events/login.html')
	else:
		error_message = "The password is not correct, try again"
		return render(request, 'events/login.html')

# Create your views here.
def index(request):
	return render(request, 'events/index.html')

def event(request):
	return HttpResponse("all events")

def eventDetail(request, eventID):
	return HttpResponse("viewing event %s" % eventID)

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	if username == "" and password == "":
		return render(request, 'events/login.html')

	return logUserIn(username, password)
