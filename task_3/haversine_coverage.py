from haversine import haversine
from operator import itemgetter

sort_test = sorted

def haversine_coverage(locations, shoppers):
    shoppers_list = []

    for shopper in shoppers:
        if shopper.get('enabled') == False: continue

        lat_shopper = shopper['lat']
        lng_shopper = shopper['lng']

        locations_covered = 0

        for location in locations:
            lat_location = location['lat']
            lng_location = location['lng']
            if (haversine((lat_location, lng_location), (lat_shopper, lng_shopper)) < 10.0):
                locations_covered += 1
        
        shopper_dict = {'shopper_id': shopper['id'], 'coverage': int(locations_covered/len(locations) * 100) }
        shoppers_list.append(shopper_dict)
    
    return sort_test(shoppers_list, key=itemgetter('coverage'), reverse=True)



