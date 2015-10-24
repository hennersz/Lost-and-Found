from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

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
	#if both nul, then display login
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
		else:
			# Return a 'disabled account' error message
			login(request, user)
	else:
		# Return an 'invalid login' error message.
		login(request, user)