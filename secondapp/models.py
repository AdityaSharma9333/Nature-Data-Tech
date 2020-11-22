from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

	user = models.OneToOneField(User,on_delete=models.PROTECT)

	# additional 
    
    
	Company_Address=models.CharField(max_length=128,blank=True)
	Company_Name=models.CharField(max_length=128,blank=True)
	portfolio_site=models.URLField(blank=True)
	

	def __str__ (self):
		return self.user.username