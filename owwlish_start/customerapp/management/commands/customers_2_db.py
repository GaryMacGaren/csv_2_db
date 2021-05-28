import googlemaps
import os
from django.core.management.base import BaseCommand
from configparser import ConfigParser
from customerapp.models import Customer

import csv

class Geocode:
    def __init__(self, api_key):
        self._api_key = api_key
        self._gclient = googlemaps.Client(key=self._api_key)

    def get_coordenates(self, city, coordenate):
        return self._gclient.geocode(city)[0]['geometry']['location'][coordenate]


class Command(BaseCommand):
    help = 'Adds a user to django'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        ROOT = os.path.abspath(os.path.dirname(__name__))
        config = ConfigParser()
        config.read(ROOT + '/.ini')
        key = config.get('api', 'API_KEY')

        gmaps = Geocode(key)
        csv_file = options['file']
        customers_list = []
        with open(csv_file, newline='') as csv_file:
            dict_reader = csv.DictReader(csv_file)
            for row in dict_reader:
                try:
                    customers_list.append(Customer(first_name=row['first_name'],
                                                  last_name=row['last_name'],
                                                  email=row['email'],
                                                  gender=row['gender'],
                                                  company=row['company'],
                                                  city=row['city'],
                                                  title=row['title'],
                                                  latitude= gmaps.get_coordenates(row['city'], 'lat'),
                                                  longitude=gmaps.get_coordenates(row['city'], 'lng'))
                    )
                except:
                    print(f"Can't create the customer object with name: {row['first_name']}")
            customers = Customer.objects.bulk_create(customers_list)
            if customers:
                print('Customers created')
            else:
                print("Couldn't create the customers objects")