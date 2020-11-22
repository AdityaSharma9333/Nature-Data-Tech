from django.shortcuts import render
from .forms import NewUser
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def index(request):
	return render(request,'myapp/index.html')

def aboutus(request):
	return render(request,'myapp/aboutus.html')

def services(request):
	return render(request,'myapp/services.html')

def team(request):
	return render(request,'myapp/team.html')

def clients(request):
	return render(request,'myapp/clients.html')

def users(request):
	form = NewUser()
	if request.method == "POST":
		form=NewUser(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
				print("ERROR FORM INVALID")	

			

	return render(request,'myapp/user.html',{'form':form})			


