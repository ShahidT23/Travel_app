# bookings/views.py
import requests
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import PackageSearchForm ,TrainSearchForm , BusSearchForm
from bs4 import BeautifulSoup

def home(request):
    return render(request, 'bookings/home.html')

@csrf_exempt
def search_flights(request):
    if request.method == 'POST':
        source_airport_code = request.POST.get('from')
        destination_airport_code = request.POST.get('to')
        departure_date = request.POST.get('departure_date')
        num_adults = request.POST.get('adults')
        cabin_class = request.POST.get('class')
        print("from request : -----------",request.POST)

        url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchFlights"
        querystring = {
            "sourceAirportCode": f"{source_airport_code}",
            "destinationAirportCode": f"{destination_airport_code}",
            "pageNo": "1",
            "numAdults": num_adults,
            "numSeniors":"0",
            # "children": "0,17",  # Assuming no children for simplicity
            "sortOrder": "ML_BEST_VALUE",
            "date":departure_date,
            "itineraryType":"ONE_WAY",
            
            "classOfService": "ECONOMY",
            # "currency_code": "USD"
        }
        print("querystring:----------------------",querystring)
        headers = {
            "x-rapidapi-key": settings.TRIPADVISOR_API_KEY,
            "x-rapidapi-host": "tripadvisor16.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        flights_data = response.json()
        print("flights--------------------------------: 00-------------------",flights_data)

        # Extract the relevant data
        flights = flights_data.get('data', {}).get('flights', [])
        
        return render(request, 'bookings/flight_list.html', {'flights': flights})
    else:
        return render(request, 'bookings/flight_search.html')


@csrf_exempt
def search_hotels(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        room = request.POST.get('room')
        guests = request.POST.get('guests')
        selected_location_id = request.POST.get('selected_location_id')

        # First API call to get geoId based on the location
        geoIdURL = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchLocation"
        geoIdHeaders = {
            'x-rapidapi-key': "4063190622msh8cdb57c724687e9p1fce07jsne6e9bc785b5e",
            'x-rapidapi-host': "tripadvisor16.p.rapidapi.com"
        }
        geoIdParams = {
            "query": location,
        }

        try:
            geoIdResponse = requests.get(geoIdURL, headers=geoIdHeaders, params=geoIdParams)
            geoIdResponse.raise_for_status()
            geoIdData = geoIdResponse.json()
            locations = geoIdData.get('data', [])

            if not locations:
                return render(request, 'bookings/hotel_search.html', {'error_message': "No locations found for the given query."})

            # Strip HTML tags from titles
            for loc in locations:
                loc['title'] = BeautifulSoup(loc['title'], 'html.parser').get_text()

            if selected_location_id:
                # If the user has selected a location, proceed with the hotel search
                selected_location = next((loc for loc in locations if str(loc['geoId']) == selected_location_id), None)

                if not selected_location:
                    return render(request, 'bookings/hotel_search.html', {'error_message': "Invalid location selected."})
                print("selected_location:--------------------",selected_location['geoId'])
                # Second API call to get hotels based on the selected geoId
                url = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels"
                headers = {
                    'x-rapidapi-key': "4063190622msh8cdb57c724687e9p1fce07jsne6e9bc785b5e",
                    'x-rapidapi-host': "tripadvisor16.p.rapidapi.com"
                }
                params = {
                    "geoId": selected_location['geoId'],
                    "checkIn": check_in,
                    "checkOut": check_out,
                    "pageNumber": 1,
                    "currencyCode": "USD"
                }

                response = requests.get(url, headers=headers, params=params)
                response.raise_for_status()
                hotels_data = response.json()
                hotels = hotels_data['data']['data']
                print("hotels-------------------------------",hotels)

                return render(request, 'bookings/hotel_list.html', {'hotels': hotels, 'location': location, 'check_in': check_in, 'check_out': check_out, 'room': room, 'guests': guests})
            else:
                # If no location has been selected, show the location selection form
                return render(request, 'bookings/hotel_search.html', {'locations': locations, 'location': location, 'check_in': check_in, 'check_out': check_out, 'room': room, 'guests': guests})

        except requests.exceptions.RequestException as e:
            error_message = f"Error fetching hotel data: {e}"
            return render(request, 'bookings/hotel_search.html', {'error_message': error_message})
    else:
        return render(request, 'bookings/hotel_search.html')

def search_packages(request):
    if request.method == 'POST':
        form = PackageSearchForm(request.POST)
        if form.is_valid():
            starting_from = form.cleaned_data.get('starting_from')
            travelling_to = form.cleaned_data.get('travelling_to')
            starting_date = form.cleaned_data.get('starting_date')
            duration_nights = form.cleaned_data.get('duration_nights')
            rooms = form.cleaned_data.get('rooms')
            guests = form.cleaned_data.get('guests')
            
            # Make API call to fetch holiday packages based on form data
            api_url = "https://example.com/api/v1/packages/search"  # Replace with your API URL
            headers = {
                'Authorization': 'Bearer your_api_key_here',
                'Content-Type': 'application/json'
            }
            params = {
                'starting_from': starting_from,
                'travelling_to': travelling_to,
                'starting_date': starting_date,
                'duration_nights': duration_nights,
                'rooms': rooms,
                'guests': guests
            }
            
            try:
                response = requests.get(api_url, headers=headers, params=params)
                response.raise_for_status()  # Raise an exception for HTTP errors
                packages = response.json()
                print("packages --------------",packages)
                
                # Render the results within the same template
                return render(request, 'bookings/package_search.html', {'form': form, 'packages': packages})
            
            except requests.exceptions.RequestException as e:
                # Handle API request exceptions (e.g., connection error, timeout)
                error_message = f"Error fetching data from API: {str(e)}"
                return render(request, 'bookings/package_search.html', {'form': form, 'error_message': error_message})
    
    else:
        form = PackageSearchForm()
    
    return render(request, 'bookings/package_search.html', {'form': form})


def search_trains(request):
    if request.method == 'POST':
        form = TrainSearchForm(request.POST)
        if form.is_valid():
            from_station = form.cleaned_data.get('from_station')
            to_station = form.cleaned_data.get('to_station')
            departure_date = form.cleaned_data.get('departure_date')
            num_travellers = form.cleaned_data.get('num_travellers')
            travel_class = form.cleaned_data.get('travel_class')
            
            # Perform API call to fetch train data
            # Replace with your actual API endpoint and headers
            api_url = "https://api.example.com/train/search"
            headers = {
                'Authorization': 'Bearer your_api_key_here',
                'Content-Type': 'application/json'
            }
            params = {
                'from_station': from_station,
                'to_station': to_station,
                'departure_date': departure_date,
                'num_travellers': num_travellers,
                'travel_class': travel_class
            }
            
            try:
                response = requests.get(api_url, headers=headers, params=params)
                response.raise_for_status()  # Raise an exception for HTTP errors
                trains = response.json()  # Assuming API returns JSON data
                
                # Render the results in the template
                return render(request, 'bookings/train_search.html', {'form': form, 'trains': trains})
            
            except requests.exceptions.RequestException as e:
                error_message = f"Error fetching data from API: {str(e)}"
                return render(request, 'bookings/train_search.html', {'form': form, 'error_message': error_message})
    
    else:
        form = TrainSearchForm()
    
    return render(request, 'bookings/train_search.html', {'form': form})

def search_buses(request):
    if request.method == 'POST':
        form = BusSearchForm(request.POST)
        if form.is_valid():
            from_city = form.cleaned_data.get('from_city')
            to_city = form.cleaned_data.get('to_city')
            departure_date = form.cleaned_data.get('departure_date')
            num_passengers = form.cleaned_data.get('num_passengers')
            
            # Perform API call to fetch bus data
            # Replace with your actual API endpoint and headers
            api_url = "https://api.example.com/bus/search"
            headers = {
                'Authorization': 'Bearer your_api_key_here',
                'Content-Type': 'application/json'
            }
            params = {
                'from_city': from_city,
                'to_city': to_city,
                'departure_date': departure_date,
                'num_passengers': num_passengers
            }
            
            try:
                response = requests.get(api_url, headers=headers, params=params)
                response.raise_for_status()  # Raise an exception for HTTP errors
                buses = response.json()  # Assuming API returns JSON data
                
                # Render the results in the template
                return render(request, 'bookings/bus_search.html', {'form': form, 'buses': buses})
            
            except requests.exceptions.RequestException as e:
                error_message = f"Error fetching data from API: {str(e)}"
                return render(request, 'bookings/bus_search.html', {'form': form, 'error_message': error_message})
    
    else:
        form = BusSearchForm()
    
    return render(request, 'bookings/bus_search.html', {'form': form})