# no-self-use snippets for geopy

# File: /root/ecooptimizer/geopy/geopy/extra/rate_limiter.py
# Line: 92

def _clock(self):  # pragma: no cover
    return default_timer()


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/adapters.py
# Line: 351

def _decode_page(self, page):
    encoding = page.headers.get_content_charset() or "utf-8"
    try:
        body_bytes = page.read()
    except Exception:
        raise GeocoderServiceError("Unable to read the response")

    try:
        return str(body_bytes, encoding=encoding)
    except ValueError:
        raise GeocoderParseError("Unable to decode the response bytes")



# ==================================================
# Line: 584

async def _raise_for_status(self, resp):
    if resp.status >= 400:
        raise AdapterHTTPError(
            "Non-successful status code %s" % resp.status,
            status_code=resp.status,
            headers=resp.headers,
            text=await resp.text(),
        )


# ==================================================
# Line: 610

def _normalize_exceptions(self):
    try:
        yield
    except (GeopyError, AdapterHTTPError, AssertionError):
        raise
    except Exception as error:
        message = str(error)
        if isinstance(error, asyncio.TimeoutError):
            raise GeocoderTimedOut("Service timed out")
        elif isinstance(error, SSLError):
            if "timed out" in message:
                raise GeocoderTimedOut("Service timed out")
        elif isinstance(error, aiohttp.ClientConnectionError):
            raise GeocoderUnavailable(message)
        raise GeocoderServiceError(message)



# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/geocodio.py
# Line: 190

def _parse_json(self, page, exactly_one=True):
    """Returns location, (latitude, longitude) from json feed."""

    places = page.get('results', [])
    if not places:
        return None

    def parse_place(place):
        """Get the location, lat, lng from a single json place."""
        location = place.get('formatted_address')
        latitude = place['location']['lat']
        longitude = place['location']['lng']
        return Location(location, (latitude, longitude), place)

    if exactly_one:
        return parse_place(places[0])
    else:
        return [parse_place(place) for place in places]


# ==================================================
# Line: 236

def _get_error_message(self, error):
    """Try to extract an error message from the 'error' property of a JSON response.
    """
    try:
        error_message = json.loads(error.text).get('error')
    except ValueError:
        error_message = None
    return error_message or error.text

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/smartystreets.py
# Line: 115

def _geocoder_exception_handler(self, error):
    search = "no active subscriptions found"
    if isinstance(error, AdapterHTTPError):
        if search in str(error).lower():
            raise GeocoderQuotaExceeded(str(error)) from error
        if search in (error.text or "").lower():
            raise GeocoderQuotaExceeded(error.text) from error


# ==================================================
# Line: 134

def _format_structured_address(self, address):
    """
    Pretty-print address and return lat, lon tuple.
    """
    latitude = address['metadata'].get('latitude')
    longitude = address['metadata'].get('longitude')
    return Location(
        ", ".join((address['delivery_line_1'], address['last_line'])),
        (latitude, longitude) if latitude and longitude else None,
        address
    )

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/yandex.py
# Line: 182

def _parse_json(self, doc, exactly_one):
    """
    Parse JSON response body.
    """
    if doc.get('error'):
        raise GeocoderServiceError(doc['error']['message'])

    try:
        places = doc['response']['GeoObjectCollection']['featureMember']
    except KeyError:
        raise GeocoderParseError('Failed to parse server response')

    def parse_code(place):
        """
        Parse each record.
        """
        try:
            place = place['GeoObject']
        except KeyError:
            raise GeocoderParseError('Failed to parse server response')

        longitude, latitude = (
            float(_) for _ in place['Point']['pos'].split(' ')
        )

        name_elements = ['name', 'description']
        location = ', '.join([place[k] for k in name_elements if place.get(k)])

        return Location(location, (latitude, longitude), place)

    if exactly_one:
        try:
            return parse_code(places[0])
        except IndexError:
            return None
    else:
        return [parse_code(place) for place in places]

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/woosmap.py
# Line: 80

def _format_components_param(self, components):
    component_items = []

    if isinstance(components, collections.abc.Mapping):
        component_items = components.items()
    elif (
        isinstance(components, collections.abc.Sequence)
        and not isinstance(components, (str, bytes))
    ):
        component_items = components
    else:
        raise ValueError(
            '`components` parameter must be of type `dict` or `list`')

    return "|".join(
        ":".join(item) for item in component_items
    )


# ==================================================
# Line: 257

def _check_status(self, response):
    # https://developers.woosmap.com/products/address-api/geocode/#status
    status = response.get('status')
    if status == 'OK':
        return
    if status == 'ZERO_RESULTS':
        return

    error_message = response.get('error_message')
    if status == 'INVALID_REQUEST':
        raise GeocoderQueryError(
            error_message or 'Invalid request or missing address or latlng')
    elif status == 'REQUEST_DENIED':
        raise GeocoderQueryError(
            error_message or 'Your request was denied. Please check your API Key')
    elif status == 'UNKNOWN_ERROR':
        raise GeocoderUnavailable(error_message or 'Server error')
    else:
        # Unknown (undocumented) status.
        raise GeocoderServiceError(error_message or 'Unknown error')

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/databc.py
# Line: 141

def _parse_feature(self, feature):
    properties = feature['properties']
    coordinates = feature['geometry']['coordinates']
    return Location(
        properties['fullAddress'], (coordinates[1], coordinates[0]),
        properties
    )

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/banfrance.py
# Line: 163

def _parse_feature(self, feature):
    # Parse each resource.
    latitude = feature.get('geometry', {}).get('coordinates', [])[1]
    longitude = feature.get('geometry', {}).get('coordinates', [])[0]
    placename = feature.get('properties', {}).get('label')

    return Location(placename, (latitude, longitude), feature)


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/what3words.py
# Line: 140

def _parse_json(self, resources, exactly_one=True):
    """
    Parse type, words, latitude, and longitude and language from a
    JSON response.
    """

    code = resources['status'].get('code')

    if code:
        # https://docs.what3words.com/api/v2/#errors
        exc_msg = "Error returned by What3Words: %s" % resources['status']['message']
        if code == 401:
            raise exc.GeocoderAuthenticationFailure(exc_msg)

        raise exc.GeocoderQueryError(exc_msg)

    def parse_resource(resource):
        """
        Parse record.
        """

        if 'geometry' in resource:
            words = resource['words']
            position = resource['geometry']
            latitude, longitude = position['lat'], position['lng']
            if latitude and longitude:
                latitude = float(latitude)
                longitude = float(longitude)

            return Location(words, (latitude, longitude), resource)
        else:
            raise exc.GeocoderParseError('Error parsing result.')

    location = parse_resource(resources)
    if exactly_one:
        return location
    else:
        return [location]


# ==================================================
# Line: 339

def _parse_json(self, resources, exactly_one=True):
    """
    Parse type, words, latitude, and longitude and language from a
    JSON response.
    """

    error = resources.get('error')

    if error is not None:
        # https://developer.what3words.com/public-api/docs#error-handling
        exc_msg = "Error returned by What3Words: %s" % resources["error"]["message"]
        exc_code = error.get('code')
        if exc_code in ['MissingKey', 'InvalidKey']:
            raise exc.GeocoderAuthenticationFailure(exc_msg)

        raise exc.GeocoderQueryError(exc_msg)

    def parse_resource(resource):
        """
        Parse record.
        """

        if 'coordinates' in resource:
            words = resource['words']
            position = resource['coordinates']
            latitude, longitude = position['lat'], position['lng']
            if latitude and longitude:
                latitude = float(latitude)
                longitude = float(longitude)

            return Location(words, (latitude, longitude), resource)
        else:
            raise exc.GeocoderParseError('Error parsing result.')

    location = parse_resource(resources)
    if exactly_one:
        return location
    else:
        return [location]


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/geolake.py
# Line: 173

def _get_address(self, page):
    """
    Returns address string from page dictionary
    :param page: dict
    :return: str
    """
    place = page.get('place')
    address_city = place.get('city')
    address_country_code = place.get('countryCode')
    address = join_filter(', ', [address_city, address_country_code])
    return address

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/base.py
# Line: 294

def _coerce_point_to_string(self, point, output_format="%(lat)s,%(lon)s"):
    """
    Do the right thing on "point" input. For geocoders with reverse
    methods.
    """
    if not isinstance(point, Point):
        point = Point(point)

    # Altitude is silently dropped.
    #
    # Geocoding services (almost?) always consider only lat and lon
    # in queries, so altitude doesn't affect the request.
    # A non-zero altitude should not raise an exception
    # though, because PoIs are assumed to span the whole
    # altitude axis (i.e. not just the 0km plane).
    return output_format % dict(lat=_format_coordinate(point.latitude),
                                lon=_format_coordinate(point.longitude))


# ==================================================
# Line: 312

def _format_bounding_box(
    self, bbox, output_format="%(lat1)s,%(lon1)s,%(lat2)s,%(lon2)s"

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/bing.py
# Line: 216

def _parse_json(self, doc, exactly_one=True):
    """
    Parse a location name, latitude, and longitude from an JSON response.
    """
    status_code = doc.get("statusCode", 200)
    if status_code != 200:
        err = doc.get("errorDetails", "")
        if status_code == 401:
            raise GeocoderAuthenticationFailure(err)
        elif status_code == 403:
            raise GeocoderInsufficientPrivileges(err)
        elif status_code == 429:
            raise GeocoderRateLimited(err)
        elif status_code == 503:
            raise GeocoderUnavailable(err)
        else:
            raise GeocoderServiceError(err)

    resources = doc['resourceSets'][0]['resources']
    if resources is None or not len(resources):
        return None

    def parse_resource(resource):
        """
        Parse each return object.
        """
        stripchars = ", \n"
        addr = resource['address']

        address = addr.get('addressLine', '').strip(stripchars)
        city = addr.get('locality', '').strip(stripchars)
        state = addr.get('adminDistrict', '').strip(stripchars)
        zipcode = addr.get('postalCode', '').strip(stripchars)
        country = addr.get('countryRegion', '').strip(stripchars)

        city_state = join_filter(", ", [city, state])
        place = join_filter(" ", [city_state, zipcode])
        location = join_filter(", ", [address, place, country])

        latitude = resource['point']['coordinates'][0] or None
        longitude = resource['point']['coordinates'][1] or None
        if latitude and longitude:
            latitude = float(latitude)
            longitude = float(longitude)

        return Location(location, (latitude, longitude), resource)

    if exactly_one:
        return parse_resource(resources[0])
    else:
        return [parse_resource(resource) for resource in resources]

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/here.py
# Line: 332

def _parse_json(self, doc, exactly_one=True):
    """
    Parse a location name, latitude, and longitude from an JSON response.
    """
    status_code = doc.get("statusCode", 200)
    if status_code != 200:
        err = doc.get("errorDetails", "")
        if status_code == 401:
            raise GeocoderAuthenticationFailure(err)
        elif status_code == 403:
            raise GeocoderInsufficientPrivileges(err)
        elif status_code == 429:
            raise GeocoderRateLimited(err)
        elif status_code == 503:
            raise GeocoderUnavailable(err)
        else:
            raise GeocoderServiceError(err)

    try:
        resources = doc['Response']['View'][0]['Result']
    except IndexError:
        resources = None
    if not resources:
        return None

    def parse_resource(resource):
        """
        Parse each return object.
        """
        stripchars = ", \n"
        addr = resource['Location']['Address']

        address = addr.get('Label', '').strip(stripchars)
        city = addr.get('City', '').strip(stripchars)
        state = addr.get('State', '').strip(stripchars)
        zipcode = addr.get('PostalCode', '').strip(stripchars)
        country = addr.get('Country', '').strip(stripchars)

        city_state = join_filter(", ", [city, state])
        place = join_filter(" ", [city_state, zipcode])
        location = join_filter(", ", [address, place, country])

        display_pos = resource['Location']['DisplayPosition']
        latitude = float(display_pos['Latitude'])
        longitude = float(display_pos['Longitude'])

        return Location(location, (latitude, longitude), resource)

    if exactly_one:
        return parse_resource(resources[0])
    else:
        return [parse_resource(resource) for resource in resources]



# ==================================================
# Line: 617

def _parse_json(self, doc, exactly_one=True):
    resources = doc['items']
    if not resources:
        return None

    def parse_resource(resource):
        """
        Parse each return object.
        """
        location = resource['title']
        position = resource['position']

        latitude, longitude = position['lat'], position['lng']

        return Location(location, (latitude, longitude), resource)

    if exactly_one:
        return parse_resource(resources[0])
    else:
        return [parse_resource(resource) for resource in resources]


# ==================================================
# Line: 638

def _geocoder_exception_handler(self, error):
    if not isinstance(error, AdapterHTTPError):
        return
    if error.status_code is None or error.text is None:
        return
    try:
        body = json.loads(error.text)
    except ValueError:
        message = error.text
    else:
        # `title`: https://developer.here.com/documentation/geocoding-search-api/api-reference-swagger.html  # noqa
        # `error_description`: returned for queries without apiKey.
        message = body.get('title') or body.get('error_description') or error.text
    exc_cls = ERROR_CODE_MAP.get(error.status_code, GeocoderServiceError)
    raise exc_cls(message) from error

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/geonames.py
# Line: 301

def _raise_for_error(self, body):
    err = body.get('status')
    if err:
        code = err['value']
        message = err['message']
        # http://www.geonames.org/export/webservice-exception.html
        if message.startswith("user account not enabled to use"):
            raise GeocoderInsufficientPrivileges(message)
        if code == 10:
            raise GeocoderAuthenticationFailure(message)
        if code in (18, 19, 20):
            raise GeocoderQuotaExceeded(message)
        raise GeocoderServiceError(message)


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/opencage.py
# Line: 225

def _check_status(self, status):
    status_code = status['code']
    message = status['message']
    if status_code == 200:
        return
    # https://opencagedata.com/api#codes
    exc_cls = ERROR_CODE_MAP.get(status_code, GeocoderServiceError)
    raise exc_cls(message)

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/mapquest.py
# Line: 87

def _parse_json(self, json, exactly_one=True):
    '''Returns location, (latitude, longitude) from json feed.'''
    features = json['results'][0]['locations']

    if features == []:
        return None

    def parse_location(feature):
        addr_keys = [
            'street',
            'adminArea6',
            'adminArea5',
            'adminArea4',
            'adminArea3',
            'adminArea2',
            'adminArea1',
            'postalCode'
        ]

        location = [feature[k] for k in addr_keys if feature.get(k)]
        return ", ".join(location)

    def parse_feature(feature):
        location = parse_location(feature)
        longitude = feature['latLng']['lng']
        latitude = feature['latLng']['lat']
        return Location(location, (latitude, longitude), feature)

    if exactly_one:
        return parse_feature(features[0])
    else:
        return [parse_feature(feature) for feature in features]


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/ignfrance.py
# Line: 361

def _xml_to_json_places(self, tree, is_reverse=False):
    """
    Transform the xml ElementTree due to XML webservice return to json
    """

    select_multi = (
        'GeocodedAddress'
        if not is_reverse
        else 'ReverseGeocodedLocation'
    )

    adresses = tree.findall('.//' + select_multi)
    places = []

    sel_pl = './/Address/Place[@type="{}"]'
    for adr in adresses:
        el = {}
        el['pos'] = adr.find('./Point/pos')
        el['street'] = adr.find('.//Address/StreetAddress/Street')
        el['freeformaddress'] = adr.find('.//Address/freeFormAddress')
        el['municipality'] = adr.find(sel_pl.format('Municipality'))
        el['numero'] = adr.find(sel_pl.format('Numero'))
        el['feuille'] = adr.find(sel_pl.format('Feuille'))
        el['section'] = adr.find(sel_pl.format('Section'))
        el['departement'] = adr.find(sel_pl.format('Departement'))
        el['commune_absorbee'] = adr.find(sel_pl.format('CommuneAbsorbee'))
        el['commune'] = adr.find(sel_pl.format('Commune'))
        el['insee'] = adr.find(sel_pl.format('INSEE'))
        el['qualite'] = adr.find(sel_pl.format('Qualite'))
        el['territoire'] = adr.find(sel_pl.format('Territoire'))
        el['id'] = adr.find(sel_pl.format('ID'))
        el['id_tr'] = adr.find(sel_pl.format('ID_TR'))
        el['bbox'] = adr.find(sel_pl.format('Bbox'))
        el['nature'] = adr.find(sel_pl.format('Nature'))
        el['postal_code'] = adr.find('.//Address/PostalCode')
        el['extended_geocode_match_code'] = adr.find(
            './/ExtendedGeocodeMatchCode'
        )

        place = {}

        def testContentAttrib(selector, key):
            """
            Helper to select by attribute and if not attribute,
            value set to empty string
            """
            return selector.attrib.get(
                key,
                None
            ) if selector is not None else None

        place['accuracy'] = testContentAttrib(
            adr.find('.//GeocodeMatchCode'), 'accuracy')

        place['match_type'] = testContentAttrib(
            adr.find('.//GeocodeMatchCode'), 'matchType')

        place['building'] = testContentAttrib(
            adr.find('.//Address/StreetAddress/Building'), 'number')

        place['search_centre_distance'] = testContentAttrib(
            adr.find('.//SearchCentreDistance'), 'value')

        for key, value in iter(el.items()):
            if value is not None:
                place[key] = value.text
            else:
                place[key] = None

        # We check if lat lng is not empty and unpack accordingly
        if place['pos']:
            lat, lng = place['pos'].split(' ')
            place['lat'] = lat.strip()
            place['lng'] = lng.strip()
        else:
            place['lat'] = place['lng'] = None

        # We removed the unused key
        place.pop("pos", None)
        places.append(place)

    return places


# ==================================================
# Line: 455

def _parse_place(self, place, is_freeform=None):
    """
    Get the location, lat, lng and place from a single json place.
    """
    # When freeform already so full address
    if is_freeform == 'true':
        location = place.get('freeformaddress')
    else:
        # For parcelle
        if place.get('numero'):
            location = place.get('street')
        else:
            # When classic geocoding
            # or when reverse geocoding
            location = "%s %s" % (
                place.get('postal_code', ''),
                place.get('commune', ''),
            )
            if place.get('street'):
                location = "%s, %s" % (
                    place.get('street', ''),
                    location,
                )
            if place.get('building'):
                location = "%s %s" % (
                    place.get('building', ''),
                    location,
                )

    return Location(location, (place.get('lat'), place.get('lng')), place)

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/maptiler.py
# Line: 73

def _parse_json(self, json, exactly_one=True):
    # Returns location, (latitude, longitude) from json feed.
    features = json['features']
    if not features:
        return None

    def parse_feature(feature):
        location = feature['place_name']
        longitude = feature['center'][0]
        latitude = feature['center'][1]

        return Location(location, (latitude, longitude), feature)
    if exactly_one:
        return parse_feature(features[0])
    else:
        return [parse_feature(feature) for feature in features]


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/tomtom.py
# Line: 177

def _boolean_value(self, bool_value):
    return 'true' if bool_value else 'false'


# ==================================================
# Line: 200

def _parse_search_result(self, result):
    latitude = result['position']['lat']
    longitude = result['position']['lon']
    return Location(result['address']['freeformAddress'],
                    (latitude, longitude), result)


# ==================================================
# Occurrences: Lines 216-221 (2 instances)

def _parse_reverse_result(self, result):
    latitude, longitude = result['position'].split(',')
    return Location(result['address']['freeformAddress'],
                    (latitude, longitude), result)


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/google.py
# Line: 156

def _format_components_param(self, components):
    component_items = []

    if isinstance(components, collections.abc.Mapping):
        component_items = components.items()
    elif (
        isinstance(components, collections.abc.Sequence)
        and not isinstance(components, (str, bytes))
    ):
        component_items = components
    else:
        raise ValueError(
            '`components` parameter must be of type `dict` or `list`')

    return "|".join(
        ":".join(item) for item in component_items
    )


# ==================================================
# Line: 380

def _normalize_timezone_at_time(self, at_time):
    if at_time is None:
        timestamp = timegm(datetime.utcnow().utctimetuple())
    elif isinstance(at_time, datetime):
        # Naive datetimes are silently treated as UTC.
        # Timezone-aware datetimes are handled correctly.
        timestamp = timegm(at_time.utctimetuple())
    else:
        raise GeocoderQueryError(
            "`at_time` must be an instance of `datetime.datetime`"
        )
    return timestamp


# ==================================================
# Line: 411

def _check_status(self, response):
    # https://developers.google.com/maps/documentation/geocoding/requests-geocoding#StatusCodes
    status = response.get('status')
    if status == 'OK':
        return
    if status == 'ZERO_RESULTS':
        return

    error_message = response.get('error_message')
    # https://developers.google.com/maps/documentation/geocoding/requests-geocoding#ErrorMessages
    #   When the geocoder returns a status code other than OK, there *may*
    #   be an additional error_message field within the Geocoding response
    #   object.

    if status in ('OVER_QUERY_LIMIT', 'OVER_DAILY_LIMIT'):
        raise GeocoderQuotaExceeded(
            error_message or
            'The given key has gone over the requests limit in the 24'
            ' hour period or has submitted too many requests in too'
            ' short a period of time'
        )
    elif status == 'REQUEST_DENIED':
        raise GeocoderQueryError(error_message or 'Your request was denied')
    elif status == 'INVALID_REQUEST':
        raise GeocoderQueryError(
            error_message or 'Probably missing address or latlng'
        )
    elif status == 'UNKNOWN_ERROR':
        raise GeocoderUnavailable(error_message or 'Server error')
    else:
        # Unknown (undocumented) status.
        raise GeocoderServiceError(error_message or 'Unknown error')

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/nominatim.py
# Line: 120

def _construct_url(self, base_api, params):
    """
    Construct geocoding request url.
    The method can be overridden in Nominatim-based geocoders in order
    to extend URL parameters.

    :param str base_api: Geocoding function base address - self.api
        or self.reverse_api.

    :param dict params: Geocoding params.

    :return: string URL.
    """
    return "?".join((base_api, urlencode(params)))


# ==================================================
# Line: 374

def _parse_code(self, place):
    # Parse each resource.
    latitude = place.get('lat', None)
    longitude = place.get('lon', None)
    placename = place.get('display_name', None)
    if latitude is not None and longitude is not None:
        latitude = float(latitude)
        longitude = float(longitude)
    return Location(placename, (latitude, longitude), place)


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/pelias.py
# Line: 230

def _parse_code(self, feature):
    # Parse each resource.
    latitude = feature.get('geometry', {}).get('coordinates', [])[1]
    longitude = feature.get('geometry', {}).get('coordinates', [])[0]
    placename = feature.get('properties', {}).get('name')
    return Location(placename, (latitude, longitude), feature)


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/baidu.py
# Line: 88

def _format_components_param(self, components):
    """
    Format the components dict to something Baidu understands.
    """
    return "|".join(
        (":".join(item) for item in components.items())
    )


# ==================================================
# Line: 210

def _check_status(self, status):
    """
    Validates error statuses.
    """
    if status == 0:
        # When there are no results, just return.
        return
    if status == 1:
        raise GeocoderServiceError(
            'Internal server error.'
        )
    elif status == 2:
        raise GeocoderQueryError(
            'Invalid request.'
        )
    elif status == 3:
        raise GeocoderAuthenticationFailure(
            'Authentication failure.'
        )
    elif status == 4:
        raise GeocoderQuotaExceeded(
            'Quota validate failure.'
        )
    elif status == 5:
        raise GeocoderQueryError(
            'AK Illegal or Not Exist.'
        )
    elif status == 101:
        raise GeocoderAuthenticationFailure(
            'No AK'
        )
    elif status == 102:
        raise GeocoderAuthenticationFailure(
            'MCODE Error'
        )
    elif status == 200:
        raise GeocoderAuthenticationFailure(
            'Invalid AK'
        )
    elif status == 211:
        raise GeocoderAuthenticationFailure(
            'Invalid SN'
        )
    elif 200 <= status < 300:
        raise GeocoderAuthenticationFailure(
            'Authentication Failure'
        )
    elif 300 <= status < 500:
        raise GeocoderQuotaExceeded(
            'Quota Error.'
        )
    else:
        raise GeocoderQueryError('Unknown error. Status: %r' % status)


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/arcgis.py
# Line: 175

def _parse_geocode(self, response, exactly_one):
    if 'error' in response:
        raise GeocoderServiceError(str(response['error']))

    # Success; convert from the ArcGIS JSON format.
    if not len(response['candidates']):
        return None
    geocoded = []
    for resource in response['candidates']:
        geometry = resource['location']
        geocoded.append(
            Location(
                resource['address'], (geometry['y'], geometry['x']), resource
            )
        )
    if exactly_one:
        return geocoded[0]
    return geocoded


# ==================================================
# Line: 229

def _parse_reverse(self, response, exactly_one):
    if not len(response):
        return None
    if 'error' in response:
        # https://developers.arcgis.com/rest/geocode/api-reference/geocoding-service-output.htm
        if response['error']['code'] == 400:
            # 'details': ['Unable to find address for the specified location.']}
            try:
                if 'Unable to find' in response['error']['details'][0]:
                    return None
            except (KeyError, IndexError):
                pass
        raise GeocoderServiceError(str(response['error']))

    if response['address'].get('Address'):
        address = (
            "%(Address)s, %(City)s, %(Region)s %(Postal)s,"
            " %(CountryCode)s" % response['address']
        )
    else:
        address = response['address']['LongLabel']

    location = Location(
        address,
        (response['location']['y'], response['location']['x']),
        response['address']
    )
    if exactly_one:
        return location
    else:
        return [location]


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/mapbox.py
# Line: 81

def _parse_json(self, json, exactly_one=True):
    '''Returns location, (latitude, longitude) from json feed.'''
    features = json['features']
    if features == []:
        return None

    def parse_feature(feature):
        location = feature['place_name']
        longitude = feature['geometry']['coordinates'][0]
        latitude = feature['geometry']['coordinates'][1]
        return Location(location, (latitude, longitude), feature)
    if exactly_one:
        return parse_feature(features[0])
    else:
        return [parse_feature(feature) for feature in features]


# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/geokeo.py
# Line: 189

def _check_status(self, page):
    status = (page.get("status") or "").upper()

    # https://geokeo.com/documentation.php#responsecodes
    if status == "OK":
        return
    if status == 'ZERO_RESULTS':
        return

    if status == 'INVALID_REQUEST':
        raise GeocoderQueryError('Invalid request parameters')
    elif status == "ACCESS_DENIED":
        raise GeocoderAuthenticationFailure('Access denied')
    elif status == "OVER_QUERY_LIMIT":
        raise GeocoderQuotaExceeded('Over query limit')
    elif status == "INTERNAL_SERVER_ERROR":  # not documented
        raise GeocoderUnavailable('Internal server error')
    else:
        # Unknown (undocumented) status.
        raise GeocoderServiceError('Unknown error')

# ==================================================
# File: /root/ecooptimizer/geopy/geopy/geocoders/photon.py
# Line: 232

def _parse_resource(self, resource):
    # Return location and coordinates tuple from dict.
    name_elements = ['name', 'housenumber', 'street',
                     'postcode', 'street', 'city',
                     'state', 'country']
    name = [resource['properties'].get(k) for k
            in name_elements if resource['properties'].get(k)]
    location = ', '.join(name)

    latitude = resource['geometry']['coordinates'][1]
    longitude = resource['geometry']['coordinates'][0]
    if latitude and longitude:
        latitude = float(latitude)
        longitude = float(longitude)

    return Location(location, (latitude, longitude), resource)

# ==================================================
