from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

#Other functions
def logUserIn(username, password):
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			error_message = '{"authenticated": true}'
			return HttpResponse(error_message, content_type='application/json')
		else:
			error_message = '{"authenticated": false, "message": "The password is valid, but the account has been disabled!"}'
			return HttpResponse(error_message, content_type='application/json')
	else:
		error_message = '{"authenticated": false, "message": "The password is not correct, try again"}'
		return HttpResponse(error_message, content_type='application/json')

# Create your views here.
#--------------------------------------------
def index(request):
	return render(request, 'events/index.html')

def event(request):
	return HttpResponse("all events")

def eventDetail(request, eventID):
	return HttpResponse("viewing event %s" % eventID)

@csrf_exempt
def loginRequest(request):
	username = request.POST['username']
	password = request.POST['password']
<<<<<<< Updated upstream
	if username == "" or password == "":
		error_message = '{"authenticated": false, "message": "Username and password cannot be empty"}'
		return HttpResponse(error_message, content_type='application/json')

	return logUserIn(username, password)
=======
	
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
>>>>>>> Stashed changes
