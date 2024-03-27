from django.db import models

# Create your models here.
class adminlog(models.Model):
	
	username=models.CharField(max_length=25)
	password=models.CharField(max_length=25)
	
	class Meta:
		db_table="admin"

class accessories(models.Model):
	name=models.CharField(max_length=10)
	brand=models.CharField(max_length=20)
	style=models.CharField(max_length=20)
	liquid=models.CharField(max_length=20)
	photo=models.FileField(max_length=300, upload_to='',blank=True,null=True)
	

	class Meta:
		db_table="accessories"

class appointmentdet(models.Model):
	cname=models.CharField(max_length=10)
	place=models.CharField(max_length=20)
	email=models.CharField(max_length=50)
	phone=models.CharField(max_length=10)
	
	class Meta:
		db_table="dbappointment"

class dblfeed1(models.Model):
	cname=models.CharField(max_length=30)
	feed=models.CharField(max_length=50)
	rating=models.CharField(max_length=100)
	replay=models.CharField(max_length=300)
	
	
	class Meta:
		db_table="dblfeed"

