from django.db import models

class Student(models.Model):
	admno    = models.AutoField(primary_key=True)
	sname    = models.CharField(max_length=100)
	category = models.CharField(max_length=5)
	gender   = models.CharField(max_length=6,default="NULL")
	house    = models.CharField(max_length=10,null=True)
	sclass   = models.IntegerField()
	ssec     = models.CharField(max_length=10,default="NULL")
	event1   = models.CharField(max_length=20,default="NULL")
	event2   = models.CharField(max_length=20,default="NULL")
	event3   = models.CharField(max_length=20,null=True)
class Eventlst(models.Model):
	eventname  = models.CharField(max_length=20)
	status     = models.BooleanField(default=False)
class Pointstable(models.Model):
	admno   = models.IntegerField()
	event   = models.CharField(max_length=20)
	points  = models.IntegerField()
	

