# bookings/forms.py
from django import forms

class PackageSearchForm(forms.Form):
    starting_from = forms.CharField(label='Starting From', max_length=100)
    travelling_to = forms.CharField(label='Travelling To', max_length=100)
    starting_date = forms.DateField(label='Starting Date', widget=forms.DateInput(attrs={'type': 'date'}))
    duration_nights = forms.IntegerField(label='Duration Nights')
    rooms = forms.IntegerField(label='Rooms')
    guests = forms.IntegerField(label='Guests')

class TrainSearchForm(forms.Form):
    from_station = forms.CharField(label='From Station', max_length=100)
    to_station = forms.CharField(label='To Station', max_length=100)
    departure_date = forms.DateField(label='Departure Date', widget=forms.DateInput(attrs={'type': 'date'}))
    num_travellers = forms.IntegerField(label='Number of Travellers', min_value=1)
    class_choices = [
        ('economy', 'Economy'),
        ('premium_economy', 'Premium Economy'),
        ('business', 'Business'),
        ('first_class', 'First Class'),
    ]
    travel_class = forms.ChoiceField(label='Class', choices=class_choices)

class BusSearchForm(forms.Form):
    from_city = forms.CharField(label='From City', max_length=100)
    to_city = forms.CharField(label='To City', max_length=100)
    departure_date = forms.DateField(label='Departure Date', widget=forms.DateInput(attrs={'type': 'date'}))
    num_passengers = forms.IntegerField(label='Number of Passengers', min_value=1)