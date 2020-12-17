from haversine import haversine
from operator import itemgetter

def haversine_coverage(locations, shoppers):
    shoppers_coverage = []

    for shopper in shoppers:
        if shopper['enabled'] == False: continue
        shopper_coordinates = (shopper['lat'], shopper['lng'])
        shopper_coverage = {'shopper_id': shopper['id'], 'coverage': calculate_locations_covered(locations, shopper_coordinates)}
        shoppers_coverage.append(shopper_coverage)
    
    return sorted(shoppers_coverage, key=itemgetter('coverage'), reverse=True)

def calculate_locations_covered(locations, shopper_coordinates):
    locations_covered = 0

    for location in locations:
        distance = haversine((location['lat'], location['lng']), (shopper_coordinates[0], shopper_coordinates[1]))
        if (distance < 10.0):
            locations_covered += 1

    return int(locations_covered / len(locations) * 100)
