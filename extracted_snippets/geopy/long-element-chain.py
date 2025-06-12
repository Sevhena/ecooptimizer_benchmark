# long-element-chain snippets for geopy

# File: /root/ecooptimizer/geopy/geopy/geocoders/yandex.py
# Line: 190

places = doc['response']['GeoObjectCollection']['featureMember']

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/woosmap.py
# Occurrences: Lines 248-249 (2 instances)

latitude = address['geometry']['location']['lat']

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/bing.py
# Line: 234

resources = doc['resourceSets'][0]['resources']

# ==================================================
# Occurrences: Lines 255-256 (2 instances)

latitude = resource['point']['coordinates'][0] or None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/here.py
# Line: 351

resources = doc['Response']['View'][0]['Result']

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/mapquest.py
# Line: 89

features = json['results'][0]['locations']

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/google.py
# Occurrences: Lines 402-403 (2 instances)

latitude = place['geometry']['location']['lat']

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/arcgis.py
# Line: 237

if 'Unable to find' in response['error']['details'][0]:

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/mapbox.py
# Occurrences: Lines 89-90 (2 instances)

longitude = feature['geometry']['coordinates'][0]

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/geokeo.py
# Occurrences: Lines 180-181 (2 instances)

latitude = place['geometry']['location']['lat']

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/photon.py
# Occurrences: Lines 241-242 (2 instances)

latitude = resource['geometry']['coordinates'][1]

# ==================================================
