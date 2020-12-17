from haversine import haversine

def haversine_coverage(locations, shoppers):
    shoppers_list = []
    
    for shopper in shoppers:
        if shopper.get('enabled') == False: continue
        lat = shopper.get('lat')
        lng = shopper.get('lng')
        shopper_dict = {'shopper_id': shopper['id'], 'coverage': 0}

        for location in locations:
            if (haversine(location, (lat, lng)) < 10.0):
                shopper_dict['coverage'] += 1

        shoppers_list.append(shopper_dict)

    return shoppers_list


locations = [
    	  {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
    	  {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
    	  {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
          {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02},
]

shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True},
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': True},
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': True},
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': True},
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': True},
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': True},
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': True},
]

sorted = [
  {'shopper_id': 'S3', 'coverage': 72},
  {'shopper_id': 'S1', 'coverage': 43},
  {'shopper_id': 'S6', 'coverage': 12},
]
