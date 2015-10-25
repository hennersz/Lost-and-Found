from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from events.models import Event, Item
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

def eventSearch(request):
	searchTerm = request.GET['searchTerm']
	events = Event.objects.filter(Q(title__icontains = searchTerm) | Q(description__icontains = searchTerm))
	for event in events:
		allItems = Item.objects.filter(event = event.id)
		print "found %d items under event %s" % (allItems.count(), event.title)
		event.lostItemCount = allItems.filter(lostFount = 0).count()
		event.foundItemCount = allItems.count() - event.lostItemCount
	return render(request, 'events/eventSearch.html', { 'events': events,})


def event(request):
	if request.user.is_authenticated():
		return HttpResponse("all events, logged in")
	else:
		return HttpResponse("all events, NOT logged in")

def eventDetail(request, eventID):
	allItems = Item.objects.filter(event = eventID)
	foundItems = allItems.filter(lostFount = True)
	lostItems = allItems.filter(lostFount = False)
	return render(request, 'events/eventDetail.html', {'event': Event.objects.get(id = eventID), 'lostItems': lostItems, 'foundItems': foundItems})

@csrf_exempt
def items(request):
	if request.method == 'POST' and request.user and request.user.is_authenticated:
		title = request.POST['title']
		description = request.POST['description']
		lostFount = (request.POST['lostFount'] == "1")
		imgURL = request.POST['imgURL']
		eventID = request.POST['eventID']
		Item(title=title, description=description, imgURL=imgURL, owner=User.objects.get(id=request.user.id), event=Event.objects.get(id=eventID), lostFount = lostFount).save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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
