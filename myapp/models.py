from django.db import models

# Create your models here.
class Contact(models.Model):
	first_Name=models.CharField(max_length=28)
	last_Name=models.CharField(max_length=28)
	email=models.EmailField(max_length=62,unique=True)
	Leave_an_comment=models.TextField(max_length=262,blank=True,default="")
