from django.shortcuts import render
from . import models 
# Create your views here.

def contact(request):
	if request.method == 'POST':
		pass

	return render(request, 'pages/contact.html')

def newsletter(request):
	return render(request,'pages/index.html')