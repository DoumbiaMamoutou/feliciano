from django.shortcuts import render
from . import models 
from .forms import ContactForm , NewsletterForm , ReservationForm
# Create your views here.

def contact(request):
	if request.method == 'POST':
		cont=ContactForm(request.POST)
		if cont.is_valid:
			cont.save
		else:
			redirect('contact')
	return render(request, 'pages/contact.html')

def newsletter(request):
	if request.method == 'POST':
		news=NewsletterForm(request.POST)
		if news.is_valid:
			news.save
		else:
			redirect('newsletter')
	return render(request,'pages/index.html')

def reservation(request):
	if request.method == 'POST':
		res=ReservationForm(request.POST)
		if res.is_valid:
			res.save
		else:
			redirect('reservation')
	return render(request, 'pages/reservation.html')
