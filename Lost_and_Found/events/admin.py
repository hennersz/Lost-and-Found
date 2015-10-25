from django.contrib import admin

from events.models import Tag, Event, Item

admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(Item)
