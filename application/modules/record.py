from itertools import combinations
import geocoder
import googlemaps
from bingmaps.apiservices import LocationByQuery

class Record:
    'Class for a line in a csv file'

    def __init__(self, row_dict, spreadsheet):
        self.fields = row_dict
        self.spreadsheet = {'cache': spreadsheet.cache, 'api_keys': spreadsheet.api_keys, 'id_field': spreadsheet.id_field,
                            'location_fields': spreadsheet.location_fields}
        self.num_queries = 0
        self.location = None

    def fetch_geocoded_data(self):
        self.gen_location_arrays(self.spreadsheet['location_fields'])
        for location_array in self.location_arrays:
            query_string = ",".join(location_array)
            if self.has_non_whitespace_chars(query_string):
                if query_string in self.spreadsheet['cache']:
                    self.location = self.spreadsheet['cache'][query_string]
                else:
                    self.query_api(query_string)
                if self.location:
                    self.spreadsheet['cache'][query_string] = self.location
                    break
                self.num_queries += 1
                if self.num_queries > 20:
                    break

    def has_non_whitespace_chars(self, query_string):
        return len(query_string.strip().replace(',', ''))

    def query_api(self, query_string):
        self.query_google(query_string)

    def gen_location_arrays(self, location_fields):
        locations = [self.fields[location_field] for location_field in location_fields]
        location_arrays = [locations]
        for s in [1, 2]:
            if len(locations) > s:
                location_arrays.extend([location_list for location_list in combinations(locations, len(locations) - s)])
        self.location_arrays = location_arrays

    def query_google(self, query):
        gmaps = googlemaps.Client(self.spreadsheet['api_keys']['google'])
        result = gmaps.geocode(query)
        if len(result) > 0:
            self.location = Location(result, 'google', query)

class Location:
    def __init__(self, result, api, query):
        if api == 'google':
            self.google_init(result)
            self.src = 'google'
            self.query = query

    def google_init(self, result):
        [setattr(self, key, result[0]['geometry']['location'][key]) for key in ['lat', 'lng']]
        components = result[0]['address_components']
        print(components)
        self.address_components = [(component['long_name'], component['types'][0]) for component in components]
        [self.__setattr__(component['types'][0], component['long_name']) for component in components]
        print(self.address_components)









