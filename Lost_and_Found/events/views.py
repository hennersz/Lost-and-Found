from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("hello, world!")

def event(request):
	return HttpResponse("all events")

def eventDetail(request, eventID):
	return HttpResponse("viewing event %s" % eventID)