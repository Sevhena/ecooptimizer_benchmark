# too-many-arguments snippets for geopy

# File: /root/ecooptimizer/geopy/geopy/extra/rate_limiter.py
# Line: 209

def __init__(
    self,
    func,
    *,
    min_delay_seconds=0.0,
    max_retries=2,
    error_wait_seconds=5.0,
    swallow_exceptions=True,
    return_value_on_exception=None

# ==================================================
# Line: 332

def __init__(
    self,
    func,
    *,
    min_delay_seconds=0.0,
    max_retries=2,
    error_wait_seconds=5.0,
    swallow_exceptions=True,
    return_value_on_exception=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/adapters.py
# Line: 386

def __init__(
    self,
    *,
    proxies,
    ssl_context,
    pool_connections=10,
    pool_maxsize=10,
    max_retries=2,
    pool_block=False

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/geocodio.py
# Line: 39

def __init__(
    self,
    api_key,
    *,
    scheme=None,
    timeout=DEFAULT_SENTINEL,
    proxies=DEFAULT_SENTINEL,
    user_agent=None,
    ssl_context=DEFAULT_SENTINEL,
    adapter_factory=None,
    domain=None,

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/smartystreets.py
# Line: 22

def __init__(
        self,
        auth_id,
        auth_token,
        *,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/geocodeearth.py
# Line: 18

def __init__(
        self,
        api_key,
        *,
        domain='api.geocode.earth',
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        scheme=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/yandex.py
# Line: 21

def __init__(
        self,
        api_key,
        *,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        scheme=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        domain='geocode-maps.yandex.ru',

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/woosmap.py
# Line: 24

def __init__(
    self,
    api_key,
    *,
    domain='api.woosmap.com',
    scheme=None,
    timeout=DEFAULT_SENTINEL,
    proxies=DEFAULT_SENTINEL,
    user_agent=None,
    ssl_context=DEFAULT_SENTINEL,
    adapter_factory=None,

# ==================================================
# Line: 98

def geocode(
    self,
    query,
    *,
    limit=None,
    exactly_one=True,
    timeout=DEFAULT_SENTINEL,
    location=None,
    components=None,
    language=None,
    country_code_format=None,

# ==================================================
# Line: 178

def reverse(
    self,
    query,
    *,
    limit=None,
    exactly_one=True,
    timeout=DEFAULT_SENTINEL,
    language=None,
    country_code_format=None,

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/databc.py
# Line: 21

def __init__(
        self,
        *,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        domain='geocoder.api.gov.bc.ca',

# ==================================================
# Line: 69

def geocode(
        self,
        query,
        *,
        max_results=25,
        set_back=0,
        location_descriptor='any',
        exactly_one=True,
        timeout=DEFAULT_SENTINEL

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/pickpoint.py
# Line: 17

def __init__(
        self,
        api_key,
        *,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        domain='api.pickpoint.io',
        scheme=None,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/azure.py
# Line: 17

def __init__(
        self,
        subscription_key,
        *,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        domain='atlas.microsoft.com'

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/banfrance.py
# Line: 21

def __init__(
        self,
        *,
        domain='api-adresse.data.gouv.fr',
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/what3words.py
# Line: 40

def __init__(
        self,
        api_key,
        *,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        domain='api.what3words.com',

# ==================================================
# Line: 246

def __init__(
        self,
        api_key,
        *,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        domain='api.what3words.com',

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/geolake.py
# Line: 35

def __init__(
        self,
        api_key,
        *,
        domain='api.geolake.com',
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/base.py
# Line: 219

def __init__(
        self,
        *,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/bing.py
# Line: 37

def __init__(
        self,
        api_key,
        *,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        domain='dev.virtualearth.net',

# ==================================================
# Line: 91

def geocode(
        self,
        query,
        *,
        exactly_one=True,
        user_location=None,
        timeout=DEFAULT_SENTINEL,
        culture=None,
        include_neighborhood=None,
        include_country_code=False

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/here.py
# Line: 49

def __init__(
        self,
        *,
        app_id=None,
        app_code=None,
        apikey=None,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# Line: 146

def geocode(
        self,
        query,
        *,
        bbox=None,
        mapview=None,
        exactly_one=True,
        maxresults=None,
        pageinformation=None,
        language=None,
        additional_data=False,
        timeout=DEFAULT_SENTINEL

# ==================================================
# Line: 253

def reverse(
        self,
        query,
        *,
        radius=None,
        exactly_one=True,
        maxresults=None,
        pageinformation=None,
        language=None,
        mode='retrieveAddresses',
        timeout=DEFAULT_SENTINEL

# ==================================================
# Line: 412

def __init__(
        self,
        apikey,
        *,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        domain="search.hereapi.com",

# ==================================================
# Line: 468

def geocode(
    self,
    query=None,
    *,
    components=None,
    at=None,
    countries=None,
    language=None,
    limit=None,
    exactly_one=True,
    timeout=DEFAULT_SENTINEL

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/geonames.py
# Line: 38

def __init__(
        self,
        username,
        *,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        scheme='http',
        domain='api.geonames.org',

# ==================================================
# Line: 163

def reverse(
        self,
        query,
        *,
        exactly_one=True,
        timeout=DEFAULT_SENTINEL,
        feature_code=None,
        lang=None,
        find_nearby_type='findNearbyPlaceName'

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/opencage.py
# Line: 26

def __init__(
        self,
        api_key,
        *,
        domain='api.opencagedata.com',
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# Line: 81

def geocode(
        self,
        query,
        *,
        bounds=None,
        country=None,
        language=None,
        annotations=True,
        exactly_one=True,
        timeout=DEFAULT_SENTINEL

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/mapquest.py
# Line: 28

def __init__(
        self,
        api_key,
        *,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        domain='www.mapquestapi.com'

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/ignfrance.py
# Line: 39

def __init__(
        self,
        api_key=None,
        *,
        username=None,
        password=None,
        referer=None,
        domain='wxs.ign.fr',
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# Line: 127

def geocode(
        self,
        query,
        *,
        query_type='StreetAddress',
        maximum_responses=25,
        is_freeform=False,
        filtering=None,
        exactly_one=True,
        timeout=DEFAULT_SENTINEL

# ==================================================
# Line: 229

def reverse(
        self,
        query,
        *,
        reverse_geocode_preference=('StreetAddress', ),
        maximum_responses=25,
        filtering='',
        exactly_one=True,
        timeout=DEFAULT_SENTINEL

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/maptiler.py
# Line: 21

def __init__(
        self,
        api_key,
        *,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        domain='api.maptiler.com'

# ==================================================
# Line: 90

def geocode(
        self,
        query,
        *,
        exactly_one=True,
        timeout=DEFAULT_SENTINEL,
        proximity=None,
        language=None,
        bbox=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/tomtom.py
# Line: 23

def __init__(
        self,
        api_key,
        *,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        domain='api.tomtom.com'

# ==================================================
# Line: 74

def geocode(
        self,
        query,
        *,
        exactly_one=True,
        timeout=DEFAULT_SENTINEL,
        limit=None,
        typeahead=False,
        language=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/openmapquest.py
# Line: 24

def __init__(
        self,
        api_key,
        *,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        domain='open.mapquestapi.com',
        scheme=None,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/google.py
# Line: 38

def __init__(
        self,
        api_key=None,
        *,
        domain='maps.googleapis.com',
        scheme=None,
        client_id=None,
        secret_key=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        channel=''

# ==================================================
# Line: 174

def geocode(
        self,
        query=None,
        *,
        exactly_one=True,
        timeout=DEFAULT_SENTINEL,
        bounds=None,
        region=None,
        components=None,
        place_id=None,
        language=None,
        sensor=False

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/nominatim.py
# Line: 53

def __init__(
        self,
        *,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        domain=_DEFAULT_NOMINATIM_DOMAIN,
        scheme=None,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None
        # Make sure to synchronize the changes of this signature in the
        # inheriting classes (e.g. PickPoint).

# ==================================================
# Line: 135

def geocode(
        self,
        query,
        *,
        exactly_one=True,
        timeout=DEFAULT_SENTINEL,
        limit=None,
        addressdetails=False,
        language=False,
        geometry=None,
        extratags=False,
        country_codes=None,
        viewbox=None,
        bounded=False,
        featuretype=None,
        namedetails=False

# ==================================================
# Line: 299

def reverse(
        self,
        query,
        *,
        exactly_one=True,
        timeout=DEFAULT_SENTINEL,
        language=False,
        addressdetails=True,
        zoom=None,
        namedetails=False,

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/pelias.py
# Line: 25

def __init__(
        self,
        domain,
        api_key=None,
        *,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        scheme=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None
        # Make sure to synchronize the changes of this signature in the
        # inheriting classes (e.g. GeocodeEarth).

# ==================================================
# Line: 85

def geocode(
        self,
        query,
        *,
        exactly_one=True,
        timeout=DEFAULT_SENTINEL,
        boundary_rect=None,
        countries=None,
        country_bias=None,
        language=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/baidu.py
# Line: 32

def __init__(
        self,
        api_key,
        *,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        security_key=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/arcgis.py
# Line: 33

def __init__(
        self,
        username=None,
        password=None,
        *,
        referer=None,
        token_lifetime=60,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        auth_domain='www.arcgis.com',
        domain='geocode.arcgis.com'

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/mapbox.py
# Line: 21

def __init__(
        self,
        api_key,
        *,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None,
        domain='api.mapbox.com',
        referer=None

# ==================================================
# Line: 97

def geocode(
        self,
        query,
        *,
        exactly_one=True,
        timeout=DEFAULT_SENTINEL,
        proximity=None,
        country=None,
        language=None,
        bbox=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/geokeo.py
# Line: 30

def __init__(
        self,
        api_key,
        *,
        domain='geokeo.com',
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/photon.py
# Line: 30

def __init__(
        self,
        *,
        scheme=None,
        timeout=DEFAULT_SENTINEL,
        proxies=DEFAULT_SENTINEL,
        domain='photon.komoot.io',
        user_agent=None,
        ssl_context=DEFAULT_SENTINEL,
        adapter_factory=None

# ==================================================
# Line: 80

def geocode(
        self,
        query,
        *,
        exactly_one=True,
        timeout=DEFAULT_SENTINEL,
        location_bias=None,
        language=False,
        limit=None,
        osm_tag=None,
        bbox=None

# ==================================================
