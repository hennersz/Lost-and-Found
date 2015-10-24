from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^events/$', views.event, name='event'),
    url(r'^events/(?P<eventID>[0-9]+)/$', views.eventDetail, name='eventDetail'),
]
