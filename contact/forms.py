from django import forms
from .models import *

class ContactForm(forms.ModelForm):
	class Meta:
		model= Message
		fields = ('name', 'email', 'sujet', 'message')


class NewsletterForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = ('email',)