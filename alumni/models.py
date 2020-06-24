from django.db import models
from django.conf import settings
import random
import os
User = settings.AUTH_USER_MODEL
# Create your models here.
class Alumni(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='Alumni', blank=True)
	def __str__(self):
		return str(self.user)

class Graduation(models.Model):
	faculty = models.CharField(max_length=120)
	degree = models.CharField(max_length=120)
	yearOfGraduation = models.CharField(max_length=120)
	groupNumber = models.CharField(max_length=120)
	alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name='graduation')
	
	def __str__(self):
		return str(self.faculty)

class GraduationProject(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	mark = models.IntegerField(blank=True, null=True)
	gitLink = models.CharField(max_length=120)
	graduation = models.OneToOneField(
        Graduation,
        on_delete=models.CASCADE,
        primary_key=True, related_name='projects')
	def __str__(self):
		return str(self.title)
class Company(models.Model):
	name = models.CharField(max_length=120)
	address = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	information = models.TextField()
	alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name='company')

	def __str__(self):
		return str(self.name)

class Job(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job')
	position = models.CharField(max_length=120)
	startDate = models.DateField(blank=True, null=True)
	endDate = models.DateField(blank=True, null=True)
	def __str__(self):
		return str(self.position)