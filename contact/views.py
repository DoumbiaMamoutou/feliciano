from django.shortcuts import render

# Create your views here.

def contact(request):
	if request.method == 'POST':
		 
    return render(request, 'pages/contact.html')

def newsletter(request):
	return render(request,'pages/index.html')