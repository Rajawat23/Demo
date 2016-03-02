from django.db import models

# Create your models here.
class User_interest(models.Model):
	email = models.CharField(max_length=255)
	interest = models.TextField()
	timestamp = models.CharField(max_length=20)

class User_browsing_pattern(models.Model):
	email = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	timestamp = models.CharField(max_length=20)

class User_intent(models.Model):
	email = models.CharField(max_length=255)
	intent = models.TextField()
	timestamp = models.CharField(max_length=20)