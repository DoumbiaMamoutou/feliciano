from django.shortcuts import render,redirect
from . import models 
from .forms import ContactForm , NewsletterForm , ReservationForm
# Create your views here.

def contact(request):
	if request.method == 'POST':
		cont=ContactForm(request.POST)
		print('\r\n===============================\r\n',request.POST,'\r\n==================================\r\n')
		if cont.is_valid:
			cont.save()
			return redirect('home')
		else:
			return redirect('contact')
	return render(request,'pages/contact.html')

def newsletter(request):
	if request.method == 'POST':
		news=NewsletterForm(request.POST)
		if news.is_valid:
			news.save()
		else:
			redirect('newsletter')
	return redirect('home')

def reservation(request):
	if request.method == 'POST':
		res=ReservationForm(request.POST)
		if res.is_valid:
			res.save()
		else:
			redirect('reservation')
	return redirect('home')