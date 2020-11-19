from django import forms
from .models import Contact


class NewUser(forms.ModelForm):
	
	
	class Meta:
		model=Contact
		fields = '__all__'
