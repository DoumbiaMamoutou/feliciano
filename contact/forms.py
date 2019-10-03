from django import forms
from .models import Message,Newsletter
from restaurant.models import Reservation

class ContactForm(forms.ModelForm):
	class Meta:
		model= Message
		fields = ['name', 'email', 'sujet', 'message']


class NewsletterForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = ('email',)

class ReservationForm(forms.ModelForm):
     class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone','time' ,'date', 'person']

