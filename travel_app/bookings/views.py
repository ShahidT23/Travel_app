from django.shortcuts import render
from .forms import FlightSearchForm, HotelSearchForm, CabSearchForm
import requests

def home(request):
    return render(request, 'bookings/home.html')

def fetch_hotels(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        checkin_date = request.POST.get('checkin_date')
        checkout_date = request.POST.get('checkout_date')
        guests_number = request.POST.get('guests_number')

        api_key = "89e86c0141msh35287ab8f12a43fp1783f7jsn993ab1d2edbc"
        url = 'https://booking-com.p.rapidapi.com/v1/hotels/search'
        params = {
            'location': location,
            'checkin_date': checkin_date,
            'checkout_date': checkout_date,
            'adults_number': guests_number,
            'units': 'metric',
            'locale': 'en-gb',
            'currency': 'USD'
        }
        headers = {
            'x-rapidapi-host': 'booking-com.p.rapidapi.com',
            'x-rapidapi-key':"89e86c0141msh35287ab8f12a43fp1783f7jsn993ab1d2edbc",
        }

        response = requests.get(url, headers=headers, params=params)
        hotels_data = response.json()

        return render(request, 'bookings/hotels_results.html', {'hotels_data': hotels_data})
    return render(request, 'bookings/search_hotels.html')

def fetch_flights(request):
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            origin = form.cleaned_data['departure_city']
            destination = form.cleaned_data['arrival_city']
            departure_date = form.cleaned_data['departure_date']
            return_date = form.cleaned_data['return_date']
            travellers = form.cleaned_data['travellers']
            travel_class = form.cleaned_data['travel_class']

            api_key = "YOUR_FLIGHT_API_KEY"
            url = 'https://example-flights-api.com/v1/flights/search'
            params = {
                'origin': origin,
                'destination': destination,
                'departure_date': departure_date,
                'return_date': return_date,
                'adults': travellers,
                'travel_class': travel_class
            }
            headers = {
                'Authorization': f'Bearer {api_key}'
            }

            response = requests.get(url, headers=headers, params=params)
            flights_data = response.json()

            return render(request, 'bookings/flights_results.html', {'flights_data': flights_data})
    else:
        form = FlightSearchForm()
    return render(request, 'bookings/search_flights.html', {'form': form})

def fetch_cabs(request):
    if request.method == 'POST':
        pickup_location = request.POST.get('pickup_location')
        drop_location = request.POST.get('drop_location')
        pickup_time = request.POST.get('pickup_time')

        api_key = "YOUR_CAB_API_KEY"
        url = 'https://example-cabs-api.com/v1/cabs/estimate'
        params = {
            'pickup_location': pickup_location,
            'drop_location': drop_location,
            'pickup_time': pickup_time
        }
        headers = {
            'Authorization': f'Bearer {api_key}'
        }

        response = requests.get(url, headers=headers, params=params)
        cabs_data = response.json()

        return render(request, 'bookings/cabs_results.html', {'cabs_data': cabs_data})
    return render(request, 'bookings/search_cabs.html')

def hotel_details(request):
    if request.method == 'POST':
        form = HotelSearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            guests = form.cleaned_data['guests']
            
            hotels = [
                {'name': 'The Grand Hotel', 'city': city, 'price_per_night': 1500},
                {'name': 'City Inn', 'city': city, 'price_per_night': 1200},
            ]
            return render(request, 'bookings/search_results.html', {'hotels': hotels})
    else:
        form = HotelSearchForm()
    return render(request, 'bookings/search_hotels.html', {'form': form})

def search_packages(request):
    if request.method == 'POST':
        # Process form data here
        from_location = request.POST.get('from')
        to_location = request.POST.get('to')
        start_date = request.POST.get('start_date')
        room_guests = request.POST.get('room_guests')
        duration = request.POST.get('duration')
        include_flights = request.POST.get('flights')
        budget = request.POST.get('budget')
        hotel_category = request.POST.get('hotel_category')
        
        # Perform search logic or redirect to results page
        
    return render(request, 'bookings/search_packages.html')

def book_train_tickets(request):
    if request.method == 'POST':
        # Process form data here
        from_location = request.POST.get('from')
        to_location = request.POST.get('to')
        date = request.POST.get('date')
        
        # Perform search or booking logic
        
    return render(request, 'bookings/book_train_tickets.html')

def book_bus_tickets(request):
    if request.method == 'POST':
        # Process form data here
        from_location = request.POST.get('from')
        to_location = request.POST.get('to')
        date = request.POST.get('date')
        
        # Perform search or booking logic
        
    return render(request, 'bookings/book_bus_tickets.html')

def airport_cabs(request):
    if request.method == 'POST':
        form = CabSearchForm(request.POST)
        if form.is_valid():
            pickup_location = form.cleaned_data['pickup_location']
            drop_location = form.cleaned_data['drop_location']
            pickup_time = form.cleaned_data['pickup_time']

            api_key = "YOUR_CAB_API_KEY"
            url = 'https://example-cabs-api.com/v1/cabs/estimate'
            params = {
                'pickup_location': pickup_location,
                'drop_location': drop_location,
                'pickup_time': pickup_time
            }
            headers = {
                'Authorization': f'Bearer {api_key}'
            }

            try:
                response = requests.get(url, headers=headers, params=params)
                response.raise_for_status()
                cabs_data = response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error fetching airport cabs data: {e}")
                cabs_data = {'error': 'Error fetching airport cabs data. Please try again later.'}

            return render(request, 'bookings/cabs_results.html', {'cabs_data': cabs_data})
    else:
        form = CabSearchForm()

    return render(request, 'bookings/airport_cabs.html', {'form': form})


def homestays_villas(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        checkin_date = request.POST.get('checkin_date')
        checkout_date = request.POST.get('checkout_date')
        guests_number = request.POST.get('guests_number')

        api_key = "89e86c0141msh35287ab8f12a43fp1783f7jsn993ab1d2edbc"
        url = 'https://booking-com.p.rapidapi.com/v1/hotels/search'
        params = {
            'location': location,
            'checkin_date': checkin_date,
            'checkout_date': checkout_date,
            'adults_number': guests_number,
            'units': 'metric',
            'locale': 'en-gb',
            'currency': 'USD'
        }
        headers = {
            'x-rapidapi-host': 'booking-com.p.rapidapi.com',
            'x-rapidapi-key': api_key,
        }

        response = requests.get(url, headers=headers, params=params)
        hotels_data = response.json()

        return render(request, 'bookings/hotels_results.html', {'hotels_data': hotels_data})
    return render(request, 'bookings/homestays_villas.html')

def outstation_cabs(request):
    if request.method == 'POST':
        pickup_location = request.POST.get('pickup_location')
        drop_location = request.POST.get('drop_location')
        pickup_time = request.POST.get('pickup_time')

        api_key = "YOUR_CAB_API_KEY"
        url = 'https://example-cabs-api.com/v1/cabs/estimate'
        params = {
            'pickup_location': pickup_location,
            'drop_location': drop_location,
            'pickup_time': pickup_time
        }
        headers = {
            'Authorization': f'Bearer {api_key}'
        }

        response = requests.get(url, headers=headers, params=params)
        cabs_data = response.json()

        return render(request, 'bookings/cabs_results.html', {'cabs_data': cabs_data})
    return render(request, 'bookings/outstation_cabs.html')

def hourly_stays(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        checkin_date = request.POST.get('checkin_date')
        checkout_date = request.POST.get('checkout_date')
        guests_number = request.POST.get('guests_number')

        api_key = "89e86c0141msh35287ab8f12a43fp1783f7jsn993ab1d2edbc"
        url = 'https://booking-com.p.rapidapi.com/v1/hotels/search'
        params = {
            'location': location,
            'checkin_date': checkin_date,
            'checkout_date': checkout_date,
            'adults_number': guests_number,
            'units': 'metric',
            'locale': 'en-gb',
            'currency': 'USD'
        }
        headers = {
            'x-rapidapi-host': 'booking-com.p.rapidapi.com',
            'x-rapidapi-key': api_key,
        }

        response = requests.get(url, headers=headers, params=params)
        hotels_data = response.json()

        return render(request, 'bookings/hotels_results.html', {'hotels_data': hotels_data})
    return render(request, 'bookings/hourly_stays.html')

def nearby_staycations(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        checkin_date = request.POST.get('checkin_date')
        checkout_date = request.POST.get('checkout_date')
        guests_number = request.POST.get('guests_number')

        api_key = "89e86c0141msh35287ab8f12a43fp1783f7jsn993ab1d2edbc"
        url = 'https://booking-com.p.rapidapi.com/v1/hotels/search'
        params = {
            'location': location,
            'checkin_date': checkin_date,
            'checkout_date': checkout_date,
            'adults_number': guests_number,
            'units': 'metric',
            'locale': 'en-gb',
            'currency': 'USD'
        }
        headers = {
            'x-rapidapi-host': 'booking-com.p.rapidapi.com',
            'x-rapidapi-key': api_key,
        }

        response = requests.get(url, headers=headers, params=params)
        hotels_data = response.json()

        return render(request, 'bookings/hotels_results.html', {'hotels_data': hotels_data})
    return render(request, 'bookings/nearby_staycations.html')

def holiday_packages(request):
    # Your logic for handling holiday packages view
    return render(request, 'bookings/holiday_packages.html')

def flight_status(request):
    return render(request, 'bookings/flight_status.html')

def train_bus(request):
    # Your logic for handling train/bus view
    return render(request, 'bookings/train_bus.html')
