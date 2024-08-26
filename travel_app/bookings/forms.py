from django import forms
import datetime
class FlightSearchForm(forms.Form):
    departure_city = forms.CharField(max_length=50,label="Departure City",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search for cities..'})
    )
    arrival_city = forms.CharField(max_length=50, label="Arrival City",
           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search for cities..'})
    )
      # Set current date as initial value for departure_date
    departure_date = forms.DateField(
        widget=forms.SelectDateWidget(attrs={'class': 'form-control','type':'date'}), 
        label="Departure Date",
        initial=datetime.date.today  # This sets the current date as default
    )
    
    return_date = forms.DateField(
        widget=forms.SelectDateWidget(attrs={'class': 'form-control','type':'date'}), 
        label="Return Date", 
        required=False
    )
    travellers = forms.IntegerField(min_value=1, label="Traveller",
    widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1'})
    )
    travel_class = forms.ChoiceField(choices=[('economy', 'Economy'), ('business', 'Business'), ('first', 'First Class')],label="Class",widget=forms.Select(attrs={'class': 'form-control'})
   )


   

class HotelSearchForm(forms.Form):
    city = forms.CharField(max_length=100, label="City")
    check_in_date = forms.DateField(widget=forms.SelectDateWidget, label="Check-In Date")
    check_out_date = forms.DateField(widget=forms.SelectDateWidget, label="Check-Out Date")
    guests = forms.IntegerField(min_value=1, label="Number of Guests")


class HotelSearchForm(forms.Form):
    city = forms.CharField(label='City', max_length=100)
    check_in_date = forms.DateField(label='Check-in Date')
    check_out_date = forms.DateField(label='Check-out Date')
    guests = forms.IntegerField(label='Number of Guests')

class CabSearchForm(forms.Form):
    pickup_location = forms.CharField(label='Pickup Location', max_length=100)
    drop_location = forms.CharField(label='Drop Location', max_length=100)
    pickup_time = forms.DateTimeField(label='Pickup Time')