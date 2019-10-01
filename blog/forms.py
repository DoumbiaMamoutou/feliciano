from django.forms import ModelForm
from myapp.models import Reservation


class ReservationForm(ModelForm):
     class Meta:
         model = Reservation
         fields = ['name', 'email', 'phone', 'date', 'person']

# Creating a form to add an Reservation.
>>> form = ReservationForm()