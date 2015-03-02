from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Backer(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	email = models.EmailField()
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.firstname

class Event(models.Model):
	eventname = models.CharField(max_length=200)
	eventdesc = models.TextField()
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.eventname

class Sweep(models.Model):
	sweepname = models.CharField(max_length=200)
	sweepevent = models.ForeignKey('Event')
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.sweepname

class Player(models.Model):
	playername = models.CharField(max_length=200)
	playersweep = models.ForeignKey('Sweep')
	playerbacker = models.ForeignKey('Backer', null=True, blank=True, default = None)
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.playername