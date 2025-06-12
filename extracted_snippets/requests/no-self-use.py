# no-self-use snippets for requests

# File: /root/ecooptimizer/requests/src/requests/cookies.py
# Line: 69

def is_unverifiable(self):
    return True


# ==================================================
# File: /root/ecooptimizer/requests/src/requests/sessions.py
# Line: 107

def get_redirect_target(self, resp):
    """Receives a Response. Returns a redirect URI or ``None``"""
    # Due to the nature of how requests processes redirects this method will
    # be called at least once upon the original response and at least twice
    # on each subsequent redirect response (if any).
    # If a custom mixin is used to handle this logic, it may be advantageous
    # to cache the redirect location onto the response object as a private
    # attribute.
    if resp.is_redirect:
        location = resp.headers["location"]
        # Currently the underlying http module on py3 decode headers
        # in latin1, but empirical evidence suggests that latin1 is very
        # rarely used with non-ASCII characters in HTTP headers.
        # It is more likely to get UTF8 header rather than latin1.
        # This causes incorrect handling of UTF8 encoded location headers.
        # To solve this, we re-encode the location in latin1.
        location = location.encode("latin1")
        return to_native_string(location, "utf8")
    return None


# ==================================================
# Line: 127

def should_strip_auth(self, old_url, new_url):
    """Decide whether Authorization header should be removed when redirecting"""
    old_parsed = urlparse(old_url)
    new_parsed = urlparse(new_url)
    if old_parsed.hostname != new_parsed.hostname:
        return True
    # Special case: allow http -> https redirect when using the standard
    # ports. This isn't specified by RFC 7235, but is kept to avoid
    # breaking backwards compatibility with older versions of requests
    # that allowed any redirects on the same host.
    if (
        old_parsed.scheme == "http"
        and old_parsed.port in (80, None)
        and new_parsed.scheme == "https"
        and new_parsed.port in (443, None)
    ):
        return False

    # Handle default port usage corresponding to scheme.
    changed_port = old_parsed.port != new_parsed.port
    changed_scheme = old_parsed.scheme != new_parsed.scheme
    default_port = (DEFAULT_PORTS.get(old_parsed.scheme, None), None)
    if (
        not changed_scheme
        and old_parsed.port in default_port
        and new_parsed.port in default_port
    ):
        return False

    # Standard case: root URI must match
    return changed_port or changed_scheme


# ==================================================
# Line: 333

def rebuild_method(self, prepared_request, response):
    """When being redirected we may want to change the method of the request
    based on certain specs or browser behavior.
    """
    method = prepared_request.method

    # https://tools.ietf.org/html/rfc7231#section-6.4.4
    if response.status_code == codes.see_other and method != "HEAD":
        method = "GET"

    # Do what the browsers do, despite standards...
    # First, turn 302s into GETs.
    if response.status_code == codes.found and method != "HEAD":
        method = "GET"

    # Second, if a POST is responded to with a 301, turn it into a GET.
    # This bizarre behaviour is explained in Issue 1704.
    if response.status_code == codes.moved and method == "POST":
        method = "GET"

    prepared_request.method = method



# ==================================================
# File: /root/ecooptimizer/requests/src/requests/adapters.py
# Line: 304

def cert_verify(self, conn, url, verify, cert):
    """Verify a SSL certificate. This method should not be called from user
    code, and is only exposed for use when subclassing the
    :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

    :param conn: The urllib3 connection object associated with the cert.
    :param url: The requested URL.
    :param verify: Either a boolean, in which case it controls whether we verify
        the server's TLS certificate, or a string, in which case it must be a path
        to a CA bundle to use
    :param cert: The SSL certificate to verify.
    """
    if url.lower().startswith("https") and verify:
        conn.cert_reqs = "CERT_REQUIRED"

        # Only load the CA certificates if 'verify' is a string indicating the CA bundle to use.
        # Otherwise, if verify is a boolean, we don't load anything since
        # the connection will be using a context with the default certificates already loaded,
        # and this avoids a call to the slow load_verify_locations()
        if verify is not True:
            # `verify` must be a str with a path then
            cert_loc = verify

            if not os.path.exists(cert_loc):
                raise OSError(
                    f"Could not find a suitable TLS CA certificate bundle, "
                    f"invalid path: {cert_loc}"
                )

            if not os.path.isdir(cert_loc):
                conn.ca_certs = cert_loc
            else:
                conn.ca_cert_dir = cert_loc
    else:
        conn.cert_reqs = "CERT_NONE"
        conn.ca_certs = None
        conn.ca_cert_dir = None

    if cert:
        if not isinstance(cert, basestring):
            conn.cert_file = cert[0]
            conn.key_file = cert[1]
        else:
            conn.cert_file = cert
            conn.key_file = None
        if conn.cert_file and not os.path.exists(conn.cert_file):
            raise OSError(
                f"Could not find the TLS certificate file, "
                f"invalid path: {conn.cert_file}"
            )
        if conn.key_file and not os.path.exists(conn.key_file):
            raise OSError(
                f"Could not find the TLS key file, invalid path: {conn.key_file}"
            )


# ==================================================
# Line: 546

def request_url(self, request, proxies):
    """Obtain the url to use when making the final request.

    If the message is being sent through a HTTP proxy, the full URL has to
    be used. Otherwise, we should only use the path portion of the URL.

    This should not be called from user code, and is only exposed for use
    when subclassing the
    :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

    :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs.
    :rtype: str
    """
    proxy = select_proxy(request.url, proxies)
    scheme = urlparse(request.url).scheme

    is_proxied_http_request = proxy and scheme != "https"
    using_socks_proxy = False
    if proxy:
        proxy_scheme = urlparse(proxy).scheme.lower()
        using_socks_proxy = proxy_scheme.startswith("socks")

    url = request.path_url
    if url.startswith("//"):  # Don't confuse urllib3
        url = f"/{url.lstrip('/')}"

    if is_proxied_http_request and not using_socks_proxy:
        url = urldefragauth(request.url)

    return url


# ==================================================
# Line: 592

def proxy_headers(self, proxy):
    """Returns a dictionary of the headers to add to any request sent
    through a proxy. This works with urllib3 magic to ensure that they are
    correctly sent to the proxy, rather than in a tunnelled request if
    CONNECT is being used.

    This should not be called from user code, and is only exposed for use
    when subclassing the
    :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

    :param proxy: The url of the proxy being used for this request.
    :rtype: dict
    """
    headers = {}
    username, password = get_auth_from_url(proxy)

    if username:
        headers["Proxy-Authorization"] = _basic_auth_str(username, password)

    return headers


# ==================================================
