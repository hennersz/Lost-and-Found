from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from events.models import Event
from django.db.models import Q
import json

#Other functions
def logUserIn(request, username, password):
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
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
	return render(request, 'events/index.html', {'user': request.user})

def eventSearch(request, searchTerm):
	event_list = Event.objects.filter(Q(title__icontains = searchTerm) | Q(description__icontains = searchTerm))
	context = RequestContext(request, {
		'event_list': event_list,
	})
	template = loader.get_template('events/eventSearch.html')
	return HttpResponse(template.render(context))


def event(request):
	if request.user.is_authenticated():
		return HttpResponse("all events, logged in")
	else:
		return HttpResponse("all events, NOT logged in")

def eventDetail(request, eventID):
	return HttpResponse("viewing event %s" % eventID)

def logoutRequest(request):
	logout(request)
	return HttpResponse(json.dumps({'loggedOut':True}), content_type='application/json')

@csrf_exempt
def loginRequest(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		if username == "" or password == "":
			error_message = '{"authenticated": false, "message": "Username and password cannot be empty"}'
			return HttpResponse(error_message, content_type='application/json')

		return logUserIn(request, username, password)
	elif request.method == 'GET':
		return render(request, 'events/login.html')
