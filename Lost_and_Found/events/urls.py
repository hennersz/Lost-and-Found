from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^eventSearch/(?P<searchTerm>\w+)', views.eventSearch, name='eventSearch'),
    url(r'^events/$', views.event, name='event'),
    url(r'^events/(?P<eventID>[0-9]+)/$', views.eventDetail, name='eventDetail'),
    url(r'^login/$', views.loginRequest, name='login'),
]
