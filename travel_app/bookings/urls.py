from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search-hotels/', views.fetch_hotels, name='fetch_hotels'),
    path('search-flights/', views.fetch_flights, name='fetch_flights'),
    path('search-cabs/', views.fetch_cabs, name='fetch_cabs'),
    path('hotel-details/', views.hotel_details, name='hotel_details'),
    path('search-packages/', views.search_packages, name='search_packages'),
    path('book-train-tickets/', views.book_train_tickets, name='book_train_tickets'),
    path('book-bus-tickets/', views.book_bus_tickets, name='book_bus_tickets'),
    path('airport-cabs/', views.airport_cabs, name='airport_cabs'),
    path('homestays-villas/', views.homestays_villas, name='homestays_villas'),
    path('outstation-cabs/', views.outstation_cabs, name='outstation_cabs'),
    path('hourly-stays/', views.hourly_stays, name='hourly_stays'),
    path('nearby-staycations/', views.nearby_staycations, name='nearby_staycations'),
    path('holiday-packages/', views.holiday_packages, name='holiday_packages'),
    path('flight-status/', views.flight_status, name='flight_status'),
    path('train-bus/', views.train_bus, name='train_bus'),
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('fetch-flights/', views.flight_details, name='flight_details'),
#     path('fetch-hotels/', views.fetch_hotels, name='fetch_hotels'),
#     path('search_packages/', views.search_packages, name='search_packages'),
#     path('book-train-tickets/', views.book_train_tickets, name='book_train_tickets'),
#     path('book-bus-tickets/', views.book_bus_tickets, name='book_bus_tickets'),
#     path('airport-cabs/', views.airport_cabs, name='airport_cabs'),
#     path('homestays-villas/', views.homestays_villas, name='homestays_villas'),
#     path('outstation-cabs/', views.outstation_cabs, name='outstation_cabs'),
#     path('hourly-stays/', views.hourly_stays, name='hourly_stays'),
#     path('nearby-staycations/', views.nearby_staycations, name='nearby_staycations'),
#     path('flight-status/', views.flight_status, name='flight_status'),
# ]

