from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    phoneNumber = models.IntegerField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField('Event Date')
    imgURL = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    host = models.ForeignKey(Person)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey(Person)
    imgURL = models.CharField(max_length=100)
    event = models.ForeignKey(Event)
    lostFount = models.BooleanField() #false = lost, true = found

    def __str__(self):
        return self.title


class Tag(models.Model):
    tagText = models.CharField(max_length=100)
    item = models.ForeignKey(Item)

    def __str__(self):
        return self.tagText