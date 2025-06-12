# no-self-use snippets for django

# File: /root/ecooptimizer/django/django/apps/config.py
# Line: 62

def default_auto_field(self):
    from django.conf import settings

    return settings.DEFAULT_AUTO_FIELD


# ==================================================
# Line: 71

def _path_from_module(self, module):
    """Attempt to determine app's filesystem path from its module."""
    # See #21874 for extended discussion of the behavior of this method in
    # various cases.
    # Convert to list because __path__ may not support indexing.
    paths = list(getattr(module, "__path__", []))
    if len(paths) != 1:
        filename = getattr(module, "__file__", None)
        if filename is not None:
            paths = [os.path.dirname(filename)]
        else:
            # For unknown reasons, sometimes the list returned by __path__
            # contains duplicates that must be removed (#25246).
            paths = list(set(paths))
    if len(paths) > 1:
        raise ImproperlyConfigured(
            "The app module %r has multiple filesystem locations (%r); "
            "you must configure this app with an AppConfig subclass "
            "with a 'path' class attribute." % (module, paths)
        )
    elif not paths:
        raise ImproperlyConfigured(
            "The app module %r has no filesystem location, "
            "you must configure this app with an AppConfig subclass "
            "with a 'path' class attribute." % module
        )
    return paths[0]


# ==================================================
# File: /root/ecooptimizer/django/django/middleware/locale.py
# Line: 19

def process_request(self, request):
    urlconf = getattr(request, "urlconf", settings.ROOT_URLCONF)
    (
        i18n_patterns_used,
        prefixed_default_language,
    ) = is_language_prefix_patterns_used(urlconf)
    language = translation.get_language_from_request(
        request, check_path=i18n_patterns_used
    )
    language_from_path = translation.get_language_from_path(request.path_info)
    if (
        not language_from_path
        and i18n_patterns_used
        and not prefixed_default_language
    ):
        language = settings.LANGUAGE_CODE
    translation.activate(language)
    request.LANGUAGE_CODE = translation.get_language()


# ==================================================
# File: /root/ecooptimizer/django/django/middleware/cache.py
# Line: 82

def _should_update_cache(self, request, response):
    return hasattr(request, "_cache_update_cache") and request._cache_update_cache


# ==================================================
# File: /root/ecooptimizer/django/django/middleware/csrf.py
# Line: 175

def csrf_trusted_origins_hosts(self):
    return [
        urlsplit(origin).netloc.lstrip("*")
        for origin in settings.CSRF_TRUSTED_ORIGINS
    ]


# ==================================================
# Occurrences: Lines 182-186 (2 instances)

def allowed_origins_exact(self):
    return {origin for origin in settings.CSRF_TRUSTED_ORIGINS if "*" not in origin}


# ==================================================
# Line: 202

def _accept(self, request):
    # Avoid checking the request twice by adding a custom attribute to
    # request.  This will be relevant when both decorator and middleware
    # are used.
    request.csrf_processing_done = True
    return None


# ==================================================
# Line: 209

def _reject(self, request, reason):
    response = _get_failure_view()(request, reason=reason)
    log_response(
        "Forbidden (%s): %s",
        reason,
        request.path,
        response=response,
        request=request,
        logger=logger,
    )
    return response


# ==================================================
# Line: 221

def _get_secret(self, request):
    """
    Return the CSRF secret originally associated with the request, or None
    if it didn't have one.

    If the CSRF_USE_SESSIONS setting is false, raises InvalidTokenFormat if
    the request's secret has invalid characters or an invalid length.
    """
    if settings.CSRF_USE_SESSIONS:
        try:
            csrf_secret = request.session.get(CSRF_SESSION_KEY)
        except AttributeError:
            raise ImproperlyConfigured(
                "CSRF_USE_SESSIONS is enabled, but request.session is not "
                "set. SessionMiddleware must appear before CsrfViewMiddleware "
                "in MIDDLEWARE."
            )
    else:
        try:
            csrf_secret = request.COOKIES[settings.CSRF_COOKIE_NAME]
        except KeyError:
            csrf_secret = None
        else:
            # This can raise InvalidTokenFormat.
            _check_token_format(csrf_secret)
    if csrf_secret is None:
        return None
    # Django versions before 4.0 masked the secret before storing.
    if len(csrf_secret) == CSRF_TOKEN_LENGTH:
        csrf_secret = _unmask_cipher_token(csrf_secret)
    return csrf_secret


# ==================================================
# Line: 253

def _set_csrf_cookie(self, request, response):
    if settings.CSRF_USE_SESSIONS:
        if request.session.get(CSRF_SESSION_KEY) != request.META["CSRF_COOKIE"]:
            request.session[CSRF_SESSION_KEY] = request.META["CSRF_COOKIE"]
    else:
        response.set_cookie(
            settings.CSRF_COOKIE_NAME,
            request.META["CSRF_COOKIE"],
            max_age=settings.CSRF_COOKIE_AGE,
            domain=settings.CSRF_COOKIE_DOMAIN,
            path=settings.CSRF_COOKIE_PATH,
            secure=settings.CSRF_COOKIE_SECURE,
            httponly=settings.CSRF_COOKIE_HTTPONLY,
            samesite=settings.CSRF_COOKIE_SAMESITE,
        )
        # Set the Vary header since content varies with the CSRF cookie.
        patch_vary_headers(response, ("Cookie",))


# ==================================================
# Line: 342

def _bad_token_message(self, reason, token_source):
    if token_source != "POST":
        # Assume it is a settings.CSRF_HEADER_NAME value.
        header_name = HttpHeaders.parse_header_name(token_source)
        token_source = f"the {header_name!r} HTTP header"
    return f"CSRF token from {token_source} {reason}."


# ==================================================
# File: /root/ecooptimizer/django/django/middleware/http.py
# Line: 37

def needs_etag(self, response):
    """Return True if an ETag header should be added to response."""
    cache_control_headers = cc_delim_re.split(response.get("Cache-Control", ""))
    return all(header.lower() != "no-store" for header in cache_control_headers)

# ==================================================
# File: /root/ecooptimizer/django/django/middleware/clickjacking.py
# Line: 40

def get_xframe_options_value(self, request, response):
    """
    Get the value to set for the X_FRAME_OPTIONS header. Use the value from
    the X_FRAME_OPTIONS setting, or 'DENY' if not set.

    This method can be overridden if needed, allowing it to vary based on
    the request or response.
    """
    return getattr(settings, "X_FRAME_OPTIONS", "DENY").upper()

# ==================================================
# File: /root/ecooptimizer/django/django/middleware/common.py
# Line: 62

def should_redirect_with_slash(self, request):
    """
    Return True if settings.APPEND_SLASH is True and appending a slash to
    the request path turns an invalid path into a valid one.
    """
    if settings.APPEND_SLASH and not request.path_info.endswith("/"):
        urlconf = getattr(request, "urlconf", None)
        if not is_valid_path(request.path_info, urlconf):
            match = is_valid_path("%s/" % request.path_info, urlconf)
            if match:
                view = match.func
                return getattr(view, "should_append_slash", True)
    return False


# ==================================================
# Line: 76

def get_full_path_with_slash(self, request):
    """
    Return the full path of the request with a trailing slash appended.

    Raise a RuntimeError if settings.DEBUG is True and request.method is
    DELETE, POST, PUT, or PATCH.
    """
    new_path = request.get_full_path(force_append_slash=True)
    # Prevent construction of scheme relative urls.
    new_path = escape_leading_slashes(new_path)
    if settings.DEBUG and request.method in ("DELETE", "POST", "PUT", "PATCH"):
        raise RuntimeError(
            "You called this URL via %(method)s, but the URL doesn't end "
            "in a slash and you have APPEND_SLASH set. Django can't "
            "redirect to the slash URL while maintaining %(method)s data. "
            "Change your form to point to %(url)s (note the trailing "
            "slash), or set APPEND_SLASH=False in your Django settings."
            % {
                "method": request.method,
                "url": request.get_host() + new_path,
            }
        )
    return new_path


# ==================================================
# Line: 145

def is_internal_request(self, domain, referer):
    """
    Return True if the referring URL is the same domain as the current
    request.
    """
    # Different subdomains are treated as different domains.
    return bool(re.match("^https?://%s/" % re.escape(domain), referer))


# ==================================================
# File: /root/ecooptimizer/django/django/conf/__init__.py
# Line: 140

def _show_deprecation_warning(self, message, category):
    stack = traceback.extract_stack()
    # Show a warning if the setting is used outside of Django.
    # Stack index: -1 this line, -2 the property, -3 the
    # LazyObject __getattribute__(), -4 the caller.
    filename, _, _, _ = stack[-4]
    if not filename.startswith(os.path.dirname(django.__file__)):
        warnings.warn(message, category, stacklevel=2)



# ==================================================
# File: /root/ecooptimizer/django/django/template/backends/base.py
# Line: 26

def check(self, **kwargs):
    return []


# ==================================================
# File: /root/ecooptimizer/django/django/template/backends/django.py
# Line: 83

def get_templatetag_libraries(self, custom_libraries):
    """
    Return a collation of template tag libraries from installed
    applications and the supplied custom_libraries argument.
    """
    libraries = get_installed_libraries()
    libraries.update(custom_libraries)
    return libraries



# ==================================================
# File: /root/ecooptimizer/django/django/template/loaders/cached.py
# Line: 25

def get_contents(self, origin):
    return origin.loader.get_contents(origin)


# ==================================================
# Line: 95

def generate_hash(self, values):
    return hashlib.sha1("|".join(values).encode()).hexdigest()


# ==================================================
# File: /root/ecooptimizer/django/django/template/engine.py
# Occurrences: Lines 120-123 (2 instances)

def get_template_builtins(self, builtins):
    return [import_library(x) for x in builtins]


# ==================================================
# File: /root/ecooptimizer/django/django/template/response.py
# Line: 78

def resolve_context(self, context):
    return context


# ==================================================
# File: /root/ecooptimizer/django/django/template/base.py
# Line: 560

def error(self, token, e):
    """
    Return an exception annotated with the originating token. Since the
    parser can be called recursively, check if a token is already set. This
    ensures the innermost token is highlighted if an exception occurs,
    e.g. a compile error within the body of an if statement.
    """
    if not isinstance(e, Exception):
        e = TemplateSyntaxError(e)
    if not hasattr(e, "token"):
        e.token = token
    return e


# ==================================================
# File: /root/ecooptimizer/django/django/template/defaulttags.py
# Line: 290

def _get_context_stack_frame(self, context):
    # The Context object behaves like a stack where each template tag can
    # create a new scope. Find the place where to store the state to detect
    # changes.
    if "forloop" in context:
        # Ifchanged is bound to the local for loop.
        # When there is a loop-in-loop, the state is bound to the inner loop,
        # so it resets when the outer loop continues.
        return context["forloop"]
    else:
        # Using ifchanged outside loops. Effectively this is a no-op
        # because the state is associated with 'self'.
        return context.render_context



# ==================================================
# File: /root/ecooptimizer/django/django/template/smartif.py
# Line: 213

def create_var(self, value):
    return Literal(value)

# ==================================================
# File: /root/ecooptimizer/django/django/test/client.py
# Line: 438

def _encode_data(self, data, content_type):
    if content_type is MULTIPART_CONTENT:
        return encode_multipart(BOUNDARY, data)
    else:
        # Encode the content so that the byte representation is correct.
        match = CONTENT_TYPE_RE.match(content_type)
        if match:
            charset = match[1]
        else:
            charset = settings.DEFAULT_CHARSET
        return force_bytes(data, encoding=charset)


# ==================================================
# Line: 460

def _get_path(self, parsed):
    path = unquote_to_bytes(parsed.path)
    # Replace the behavior where non-ASCII values in the WSGI environ are
    # arbitrarily decoded with ISO-8859-1.
    # Refs comment in `get_bytes_from_wsgi()`.
    return path.decode("iso-8859-1")


# ==================================================
# Line: 863

def _get_backend(self):
    from django.contrib.auth import load_backend

    for backend_path in settings.AUTHENTICATION_BACKENDS:
        backend = load_backend(backend_path)
        if hasattr(backend, "get_user"):
            return backend_path


# ==================================================
# Line: 945

def _parse_json(self, response, **extra):
    if not hasattr(response, "_json"):
        if not JSON_CONTENT_TYPE_RE.match(response.get("Content-Type")):
            raise ValueError(
                'Content-Type header is "%s", not "application/json"'
                % response.get("Content-Type")
            )
        response._json = json.loads(response.text, **extra)
    return response._json


# ==================================================
# Line: 1012

def _ensure_redirects_not_cyclic(self, response):
    """
    Raise a RedirectCycleError if response contains too many redirects.
    """
    redirect_chain = response.redirect_chain
    if redirect_chain[-1] in redirect_chain[:-1]:
        # Check that we're not redirecting to somewhere we've already been
        # to, to prevent loops.
        raise RedirectCycleError("Redirect loop detected.", last_response=response)
    if len(redirect_chain) > 20:
        # Such a lengthy chain likely also means a loop, but one with a
        # growing path, changing view, or changing query argument. 20 is
        # the value of "network.http.redirection-limit" from Firefox.
        raise RedirectCycleError("Too many redirects.", last_response=response)



# ==================================================
# File: /root/ecooptimizer/django/django/test/utils.py
# Line: 965

def timed(self, name):
    yield


# ==================================================
# File: /root/ecooptimizer/django/django/test/runner.py
# Line: 179

def _confirm_picklable(self, obj):
    """
    Confirm that obj can be pickled and unpickled as multiprocessing will
    need to pickle the exception in the child process and unpickle it in
    the parent process. Let the exception rise, if not.
    """
    pickle.loads(pickle.dumps(obj))


# ==================================================
# Line: 187

def _print_unpicklable_subtest(self, test, subtest, pickle_exc):
    print(
        """

# ==================================================
# Line: 564

def handle_event(self, result, tests, event):
    event_name = event[0]
    handler = getattr(result, event_name, None)
    if handler is None:
        return
    test_index = event[1]
    event_occurred_before_first_test = test_index == -1
    if (
        event_name == "addError"
        and event_occurred_before_first_test
        and len(event) >= 4
    ):
        test_id = event[2]
        test = unittest.suite._ErrorHolder(test_id)
        args = event[3:]
    else:
        test = tests[test_index]
        args = event[2:]
    handler(test, *args)


# ==================================================
# Occurrences: Lines 1035-1044 (3 instances)

def teardown_test_environment(self, **kwargs):
    unittest.removeHandler()
    teardown_test_environment()


# ==================================================
# File: /root/ecooptimizer/django/django/test/testcases.py
# Line: 382

def settings(self, **kwargs):
    """
    A context manager that temporarily sets a setting and reverts to the
    original value when exiting the context.
    """
    return override_settings(**kwargs)


# ==================================================
# Line: 389

def modify_settings(self, **kwargs):
    """
    A context manager that temporarily applies changes to a list setting
    and reverts back to the original value when exiting the context.
    """
    return modify_settings(**kwargs)


# ==================================================
# Line: 633

def _check_test_client_response(self, response, attribute, method_name):
    """
    Raise a ValueError if the given response doesn't have the required
    attribute.
    """
    if not hasattr(response, attribute):
        raise ValueError(
            f"{method_name}() is only usable on responses fetched using "
            "the Django test Client."
        )


# ==================================================
# Line: 1191

def _should_reload_connections(self):
    return True


# ==================================================
# Line: 1461

def _should_check_constraints(self, connection):
    return (
        connection.features.can_defer_constraint_checks
        and not connection.needs_rollback
        and connection.is_usable()
    )


# ==================================================
# Occurrences: Lines 1680-1683 (2 instances)

def get_base_dir(self):
    return settings.STATIC_ROOT


# ==================================================
# Occurrences: Lines 1693-1696 (2 instances)

def get_base_dir(self):
    return settings.MEDIA_ROOT


# ==================================================
# File: /root/ecooptimizer/django/django/utils/html.py
# Line: 403

def trim_url(self, x, *, limit):
    if limit is None or len(x) <= limit:
        return x
    return "%s…" % x[: max(0, limit - 1)]


# ==================================================
# File: /root/ecooptimizer/django/django/utils/feedgenerator.py
# Line: 216

def root_attributes(self):
    """
    Return extra attributes to place on the root (i.e. feed/channel) element.
    Called from write().
    """
    return {}


# ==================================================
# Line: 236

def item_attributes(self, item):
    """
    Return extra attributes to place on each item (i.e. item/entry) element.
    """
    return {}


# ==================================================
# Line: 342

def endChannelElement(self, handler):
    handler.endElement("channel")



# ==================================================
# File: /root/ecooptimizer/django/django/utils/autoreload.py
# Line: 310

def wait_for_apps_ready(self, app_reg, django_main_thread):
    """
    Wait until Django reports that the apps have been loaded. If the given
    thread has terminated before the apps are ready, then a SyntaxError or
    other non-recoverable error has been raised. In that case, stop waiting
    for the apps_ready event and continue processing.

    Return True if the thread is alive and the ready event has been
    triggered, or False if the thread is terminated while waiting for the
    event.
    """
    while django_main_thread.is_alive():
        if app_reg.ready_event.wait(timeout=0.1):
            return True
    else:
        logger.debug("Main Django thread has terminated before apps are ready.")
        return False


# ==================================================
# File: /root/ecooptimizer/django/django/utils/archive.py
# Line: 117

def split_leading_dir(self, path):
    path = str(path)
    path = path.lstrip("/").lstrip("\\")
    if "/" in path and (
        ("\\" in path and path.find("/") < path.find("\\")) or "\\" not in path
    ):
        return path.split("/", 1)
    elif "\\" in path:
        return path.split("\\", 1)
    else:
        return path, ""


# ==================================================
# Line: 145

def target_filename(self, to_path, name):
    target_path = os.path.abspath(to_path)
    filename = os.path.abspath(os.path.join(target_path, name))
    if not filename.startswith(target_path):
        raise SuspiciousOperation("Archive contains invalid path: '%s'" % name)
    return filename


# ==================================================
# File: /root/ecooptimizer/django/django/utils/translation/__init__.py
# Line: 126

def _get_number_value(self, values):
    try:
        return values[number]
    except KeyError:
        raise KeyError(
            "Your dictionary lacks key '%s'. Please provide "
            "it, because it is required to determine whether "
            "string is singular or plural." % number
        )


# ==================================================
# Line: 136

def _translate(self, number_value):
    kwargs["number"] = number_value
    return func(**kwargs)


# ==================================================
# File: /root/ecooptimizer/django/django/utils/text.py
# Line: 111

def void_elements(self):
    from django.utils.html import VOID_ELEMENTS

    return VOID_ELEMENTS


# ==================================================
# Line: 219

def _text_chars(self, length, truncate, text):
    """Truncate a string after a certain number of chars."""
    truncate_len = calculate_truncate_chars_length(length, truncate)
    s_len = 0
    end_index = None
    for i, char in enumerate(text):
        if unicodedata.combining(char):
            # Don't consider combining characters
            # as adding to the string length
            continue
        s_len += 1
        if end_index is None and s_len > truncate_len:
            end_index = i
        if s_len > length:
            # Return the truncated string
            return add_truncation_text(text[: end_index or 0], truncate)

    # Return the original string since no truncation was necessary
    return text


# ==================================================
# File: /root/ecooptimizer/django/django/utils/log.py
# Line: 145

def format_subject(self, subject):
    """
    Escape CR and LF characters.
    """
    return subject.replace("\n", "\\n").replace("\r", "\\r")



# ==================================================
# File: /root/ecooptimizer/django/django/templatetags/i18n.py
# Line: 40

def get_language_info(self, language):
    # ``language`` is either a language code string or a sequence
    # with the language code as its first item
    if len(language[0]) > 1:
        return translation.get_language_info(language[0])
    else:
        return translation.get_language_info(str(language))


# ==================================================
# File: /root/ecooptimizer/django/django/http/response.py
# Line: 44

def _convert_to_charset(self, value, charset, mime_encode=False):
    """
    Convert headers key/value to ascii/latin-1 native strings.
    `charset` must be 'ascii' or 'latin-1'. If `mime_encode` is True and
    `value` can't be represented in the given charset, apply MIME-encoding.
    """
    try:
        if isinstance(value, str):
            # Ensure string is valid in given charset
            value.encode(charset)
        elif isinstance(value, bytes):
            # Convert bytestring using given charset
            value = value.decode(charset)
        else:
            value = str(value)
            # Ensure string is valid in given charset.
            value.encode(charset)
        if "\n" in value or "\r" in value:
            raise BadHeaderError(
                f"Header values can't contain newlines (got {value!r})"
            )
    except UnicodeError as e:
        # Encoding to a string of the specified charset failed, but we
        # don't know what type that value was, or if it contains newlines,
        # which we may need to check for before sending it to be
        # encoded for multiple character sets.
        if (isinstance(value, bytes) and (b"\n" in value or b"\r" in value)) or (
            isinstance(value, str) and ("\n" in value or "\r" in value)
        ):
            raise BadHeaderError(
                f"Header values can't contain newlines (got {value!r})"
            ) from e
        if mime_encode:
            value = Header(value, "utf-8", maxlinelen=sys.maxsize).encode()
        else:
            e.reason += ", HTTP response headers must be in %s format" % charset
            raise
    return value


# ==================================================
# Occurrences: Lines 352-358 (3 instances)

def readable(self):
    return False


# ==================================================
# File: /root/ecooptimizer/django/django/http/multipartparser.py
# Line: 381

def sanitize_file_name(self, file_name):
    """
    Sanitize the filename of an upload.

    Remove all possible path separators, even though that might remove more
    than actually required by the target system. Filenames that could
    potentially cause problems (current/parent dir) are also discarded.

    It should be noted that this function could still return a "filepath"
    like "C:some_file.txt" which is handled later on by the storage layer.
    So while this function does sanitize filenames to some extent, the
    resulting filename should still be considered as untrusted user input.
    """
    file_name = html.unescape(file_name)
    file_name = file_name.rsplit("/")[-1]
    file_name = file_name.rsplit("\\")[-1]
    # Remove non-printable characters.
    file_name = "".join([char for char in file_name if char.isprintable()])

    if file_name in {"", ".", ".."}:
        return None
    return file_name


# ==================================================
# File: /root/ecooptimizer/django/django/http/request.py
# Line: 287

def _get_scheme(self):
    """
    Hook for subclasses like WSGIRequest to implement. Return 'http' by
    default.
    """
    return "http"


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/postgresql/schema.py
# Line: 145

def _is_changing_type_of_indexed_text_column(self, old_field, old_type, new_type):
    return (old_field.db_index or old_field.unique) and (
        (old_type.startswith("varchar") and not new_type.startswith("varchar"))
        or (old_type.startswith("text") and not new_type.startswith("text"))
        or (old_type.startswith("citext") and not new_type.startswith("citext"))
    )


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/postgresql/operations.py
# Line: 107

def _prepare_tzname_delta(self, tzname):
    tzname, sign, offset = split_tzname_delta(tzname)
    if offset:
        sign = "-" if sign == "+" else "+"
        return f"{tzname}{sign}{offset}"
    return tzname


# ==================================================
# Line: 158

def fetch_returned_insert_rows(self, cursor):
    """
    Given a cursor object that has just performed an INSERT...RETURNING
    statement into a table, return the tuple of returned data.
    """
    return cursor.fetchall()


# ==================================================
# Line: 282

def prep_for_iexact_query(self, x):
    return x


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/postgresql/creation.py
# Line: 33

def _database_exists(self, cursor, database_name):
    cursor.execute(
        "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s",
        [strip_quotes(database_name)],
    )
    return cursor.fetchone() is not None


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/postgresql/features.py
# Line: 134

def prohibits_null_characters_in_text_exception(self):
    if is_psycopg3:
        return DataError, "PostgreSQL text fields cannot contain NUL (0x00) bytes"
    else:
        return ValueError, "A string literal cannot contain NUL (0x00) characters."


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/oracle/operations.py
# Line: 134

def _prepare_tzname_delta(self, tzname):
    tzname, sign, offset = split_tzname_delta(tzname)
    return f"{sign}{offset}" if offset else tzname


# ==================================================
# Occurrences: Lines 251-261 (3 instances)

def convert_textfield_value(self, value, expression, connection):
    if isinstance(value, Database.LOB):
        value = value.read()
    return value


# ==================================================
# Occurrences: Lines 275-285 (3 instances)

def convert_datefield_value(self, value, expression, connection):
    if isinstance(value, Database.Timestamp):
        value = value.date()
    return value


# ==================================================
# Line: 366

def prep_for_iexact_query(self, x):
    return x


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/oracle/base.py
# Line: 400

def oracledb_version(self):
    return get_version_tuple(Database.__version__)



# ==================================================
# Line: 573

def _param_generator(self, params):
    # Try dict handling; if that fails, treat as sequence
    if hasattr(params, "items"):
        return {k: v.force_bytes for k, v in params.items()}
    else:
        return [p.force_bytes for p in params]


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/ddl_references.py
# Line: 12

def references_table(self, table):
    """
    Return whether or not this instance references the specified table.
    """
    return False


# ==================================================
# Line: 18

def references_column(self, table, column):
    """
    Return whether or not this instance references the specified column.
    """
    return False


# ==================================================
# Line: 24

def references_index(self, table, index):
    """
    Return whether or not this instance references the specified index.
    """
    return False


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/mysql/operations.py
# Line: 88

def _prepare_tzname_delta(self, tzname):
    tzname, sign, offset = split_tzname_delta(tzname)
    return f"{sign}{offset}" if offset else tzname


# ==================================================
# Line: 151

def fetch_returned_insert_rows(self, cursor):
    """
    Given a cursor object that has just performed an INSERT...RETURNING
    statement into a table, return the tuple of returned data.
    """
    return cursor.fetchall()


# ==================================================
# Line: 315

def convert_booleanfield_value(self, value, expression, connection):
    if value in (0, 1):
        value = bool(value)
    return value


# ==================================================
# Line: 325

def convert_uuidfield_value(self, value, expression, connection):
    if value is not None:
        value = uuid.UUID(value)
    return value


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/mysql/features.py
# Line: 71

def test_collations(self):
    return {
        "ci": "utf8mb4_general_ci",
        "non_default": "utf8mb4_esperanto_ci",
        "swedish_ci": "utf8mb4_swedish_ci",
        "virtual": "utf8mb4_esperanto_ci",
    }


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/base/schema.py
# Line: 404

def skip_default(self, field):
    """
    Some backends don't accept default values for certain columns types
    (i.e. MySQL longtext and longblob).
    """
    return False


# ==================================================
# Line: 411

def skip_default_on_alter(self, field):
    """
    Some backends don't accept default values for certain columns types
    (i.e. MySQL longtext and longblob) in the ALTER COLUMN statement.
    """
    return False


# ==================================================
# Line: 427

def _column_default_sql(self, field):
    """
    Return the SQL to use in a DEFAULT clause. The resulting string should
    contain a '%s' placeholder for a default value.
    """
    return "%s"


# ==================================================
# Line: 1533

def _index_condition_sql(self, condition):
    if condition:
        return " WHERE " + condition
    return ""


# ==================================================
# Occurrences: Lines 1694-1700 (3 instances)

def _field_should_be_indexed(self, model, field):
    return field.db_index and not field.unique


# ==================================================
# Line: 1752

def _deferrable_constraint_sql(self, deferrable):
    if deferrable is None:
        return ""
    if deferrable == Deferrable.DEFERRED:
        return " DEFERRABLE INITIALLY DEFERRED"
    if deferrable == Deferrable.IMMEDIATE:
        return " DEFERRABLE INITIALLY IMMEDIATE"


# ==================================================
# Line: 1760

def _unique_index_nulls_distinct_sql(self, nulls_distinct):
    if nulls_distinct is False:
        return " NULLS NOT DISTINCT"
    elif nulls_distinct is True:
        return " NULLS DISTINCT"
    return ""


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/base/operations.py
# Line: 65

def autoinc_sql(self, table, column):
    """
    Return any SQL needed to support auto-incrementing primary keys, or
    None if no SQL is necessary.

    This SQL is executed when a table is created.
    """
    return None


# ==================================================
# Line: 74

def bulk_batch_size(self, fields, objs):
    """
    Return the maximum allowed batch size for the backend. The fields
    are the fields going to be inserted in the batch, the objs contains
    all the objects to be inserted.
    """
    return len(objs)


# ==================================================
# Line: 99

def unification_cast_sql(self, output_field):
    """
    Given a field instance, return the SQL that casts the result of a union
    to that type. The resulting string should contain a '%s' placeholder
    for the expression being cast.
    """
    return "%s"


# ==================================================
# Line: 191

def deferrable_sql(self):
    """
    Return the SQL to make a constraint "initially deferred" during a
    CREATE TABLE statement.
    """
    return ""


# ==================================================
# Line: 198

def distinct_sql(self, fields, params):
    """
    Return an SQL DISTINCT clause which removes duplicate rows from the
    result set. If any fields are given, only check the given fields for
    duplicates.
    """
    if fields:
        raise NotSupportedError(
            "DISTINCT ON fields is not supported by this database backend"
        )
    else:
        return ["DISTINCT"], []


# ==================================================
# Line: 211

def fetch_returned_insert_columns(self, cursor, returning_params):
    """
    Given a cursor object that has just performed an INSERT...RETURNING
    statement into a table, return the newly created data.
    """
    return cursor.fetchone()


# ==================================================
# Line: 218

def force_group_by(self):
    """
    Return a GROUP BY clause to use with a HAVING clause when no grouping
    is specified.
    """
    return []


# ==================================================
# Line: 225

def force_no_ordering(self):
    """
    Return a list used in the "ORDER BY" clause to force no ordering at
    all. Return an empty list to include nothing in the ordering.
    """
    return []


# ==================================================
# Line: 232

def for_update_sql(self, nowait=False, skip_locked=False, of=(), no_key=False):
    """
    Return the FOR UPDATE SQL clause to lock rows for an update operation.
    """
    return "FOR%s UPDATE%s%s%s" % (
        " NO KEY" if no_key else "",
        " OF %s" % ", ".join(of) if of else "",
        " NOWAIT" if nowait else "",
        " SKIP LOCKED" if skip_locked else "",
    )


# ==================================================
# Occurrences: Lines 263-268 (2 instances)

def bulk_insert_sql(self, fields, placeholder_rows):
    placeholder_rows_sql = (", ".join(row) for row in placeholder_rows)
    values_sql = ", ".join([f"({sql})" for sql in placeholder_rows_sql])
    return f"VALUES {values_sql}"


# ==================================================
# Line: 292

def last_insert_id(self, cursor, table_name, pk_name):
    """
    Given a cursor object that has just performed an INSERT statement into
    a table that has an auto-incrementing ID, return the newly created ID.

    `pk_name` is the name of the primary-key column.
    """
    return cursor.lastrowid


# ==================================================
# Line: 301

def lookup_cast(self, lookup_type, internal_type=None):
    """
    Return the string to use in a query when performing lookups
    ("contains", "like", etc.). It should contain a '%s' placeholder for
    the column being searched against.
    """
    return "%s"


# ==================================================
# Line: 309

def max_in_list_size(self):
    """
    Return the maximum number of items that can be passed in a single 'IN'
    list condition, or None if the backend does not impose a limit.
    """
    return None


# ==================================================
# Line: 316

def max_name_length(self):
    """
    Return the maximum length of table and column names, or None if there
    is no limit.
    """
    return None


# ==================================================
# Line: 332

def pk_default_value(self):
    """
    Return the value to use during an INSERT statement to specify that
    the field should use its default value.
    """
    return "DEFAULT"


# ==================================================
# Line: 339

def prepare_sql_script(self, sql):
    """
    Take an SQL script that may contain multiple lines and return a list
    of statements to feed to successive cursor.execute() calls.

    Since few databases are able to process raw SQL scripts in a single
    cursor.execute() call and PEP 249 doesn't talk about this use case,
    the default implementation is conservative.
    """
    return [
        sqlparse.format(statement, strip_comments=True)
        for statement in sqlparse.split(sql)
        if statement
    ]


# ==================================================
# Line: 354

def process_clob(self, value):
    """
    Return the value of a CLOB column, for backends that return a locator
    object that requires additional processing.
    """
    return value


# ==================================================
# Line: 421

def set_time_zone_sql(self):
    """
    Return the SQL that will set the connection's time zone.

    Return '' if the backend doesn't support time zones.
    """
    return ""


# ==================================================
# Line: 459

def sequence_reset_by_name_sql(self, style, sequences):
    """
    Return a list of the SQL statements required to reset sequences
    passed in `sequences`.

    The `style` argument is a Style object as returned by either
    color_style() or no_style() in django.core.management.color.
    """
    return []


# ==================================================
# Line: 469

def sequence_reset_sql(self, style, model_list):
    """
    Return a list of the SQL statements required to reset sequences for
    the given models.

    The `style` argument is a Style object as returned by either
    color_style() or no_style() in django.core.management.color.
    """
    return []  # No sequence reset required by default.


# ==================================================
# Occurrences: Lines 479-483 (2 instances)

def start_transaction_sql(self):
    """Return the SQL statement required to start a transaction."""
    return "BEGIN;"


# ==================================================
# Line: 489

def tablespace_sql(self, tablespace, inline=False):
    """
    Return the SQL that will be used in a query to define the tablespace.

    Return '' if the backend doesn't support tablespaces.

    If `inline` is True, append the SQL to a row; otherwise append it to
    the entire CREATE TABLE or CREATE INDEX statement.
    """
    return ""


# ==================================================
# Line: 500

def prep_for_like_query(self, x):
    """Prepare a value for use in a LIKE query."""
    return str(x).replace("\\", "\\\\").replace("%", r"\%").replace("_", r"\_")


# ==================================================
# Line: 508

def validate_autopk_value(self, value):
    """
    Certain backends do not accept some values for "serial" fields
    (for example zero in MySQL). Raise a ValueError if the value is
    invalid, otherwise return the validated value.
    """
    return value


# ==================================================
# Occurrences: Lines 535-538 (2 instances)

def adapt_integerfield_value(self, value, internal_type):
    return value


# ==================================================
# Line: 547

def adapt_datetimefield_value(self, value):
    """
    Transform a datetime value to an object compatible with what is expected
    by the backend driver for datetime columns.
    """
    if value is None:
        return None
    return str(value)


# ==================================================
# Line: 556

def adapt_timefield_value(self, value):
    """
    Transform a time value to an object compatible with what is expected
    by the backend driver for time columns.
    """
    if value is None:
        return None
    if timezone.is_aware(value):
        raise ValueError("Django does not support timezone-aware times.")
    return str(value)


# ==================================================
# Line: 567

def adapt_decimalfield_value(self, value, max_digits=None, decimal_places=None):
    """
    Transform a decimal.Decimal value to an object compatible with what is
    expected by the backend driver for decimal (numeric) columns.
    """
    return value


# ==================================================
# Line: 574

def adapt_ipaddressfield_value(self, value):
    """
    Transform a string representation of an IP address into the expected
    type for the backend driver.
    """
    return value or None


# ==================================================
# Line: 581

def adapt_json_value(self, value, encoder):
    return json.dumps(value, cls=encoder)


# ==================================================
# Line: 630

def get_db_converters(self, expression):
    """
    Return a list of functions needed to convert field data.

    Some field types on some backends do not provide data in the correct
    format, this is the hook for converter functions.
    """
    return []


# ==================================================
# Line: 639

def convert_durationfield_value(self, value, expression, connection):
    if value is not None:
        return datetime.timedelta(0, 0, value)


# ==================================================
# Line: 654

def conditional_expression_supported_in_where_clause(self, expression):
    """
    Return True, if the conditional expression is supported in the WHERE
    clause.
    """
    return True


# ==================================================
# Line: 661

def combine_expression(self, connector, sub_expressions):
    """
    Combine a list of subexpressions into a single expression, using
    the provided connecting operator. This is required because operators
    can vary between backends (e.g., Oracle with %% and &) and between
    subexpression types (e.g., date expressions).
    """
    conn = " %s " % connector
    return conn.join(sub_expressions)


# ==================================================
# Line: 674

def binary_placeholder_sql(self, value):
    """
    Some backends require special syntax to insert binary content (MySQL
    for example uses '_binary %s').
    """
    return "%s"


# ==================================================
# Line: 681

def modify_insert_params(self, placeholder, params):
    """
    Allow modification of insert parameters. Needed for Oracle Spatial
    backend due to #10888.
    """
    return params


# ==================================================
# Occurrences: Lines 780-786 (3 instances)

def insert_statement(self, on_conflict=None):
    return "INSERT INTO"


# ==================================================
# Occurrences: Lines 792-796 (2 instances)

def format_debug_sql(self, sql):
    # Hook for backends (e.g. NoSQL) to customize formatting.
    return sqlparse.format(sql, reindent=True, keyword_case="upper")


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/base/base.py
# Line: 127

def ensure_timezone(self):
    """
    Ensure the connection's timezone is set to `self.timezone_name` and
    return whether it changed or not.
    """
    return False


# ==================================================
# Line: 540

def disable_constraint_checking(self):
    """
    Backends can implement as needed to temporarily disable foreign key
    constraint checking. Should return True if the constraints were
    disabled and will need to be reenabled.
    """
    return False


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/base/creation.py
# Line: 34

def log(self, msg):
    sys.stderr.write(msg + os.linesep)


# ==================================================
# Line: 206

def _execute_create_test_db(self, cursor, parameters, keepdb=False):
    cursor.execute("CREATE DATABASE %(dbname)s %(suffix)s" % parameters)


# ==================================================
# Line: 374

def sql_table_creation_suffix(self):
    """
    SQL to append to the end of the test table creation statements.
    """
    return ""


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/base/validation.py
# Line: 10

def check(self, **kwargs):
    return []


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/base/introspection.py
# Line: 35

def identifier_converter(self, name):
    """
    Apply a conversion to the identifier for the purposes of comparison.

    The default identifier converter is for case sensitive comparison.
    """
    return name


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/sqlite3/operations.py
# Line: 92

def fetch_returned_insert_rows(self, cursor):
    """
    Given a cursor object that has just performed an INSERT...RETURNING
    statement into a table, return the list of returned data.
    """
    return cursor.fetchall()


# ==================================================
# Line: 323

def convert_datefield_value(self, value, expression, connection):
    if value is not None:
        if not isinstance(value, datetime.date):
            value = parse_date(value)
    return value


# ==================================================
# Line: 329

def convert_timefield_value(self, value, expression, connection):
    if value is not None:
        if not isinstance(value, datetime.time):
            value = parse_time(value)
    return value


# ==================================================
# Line: 335

def get_decimalfield_converter(self, expression):
    # SQLite stores only 15 significant digits. Digits coming from
    # float inaccuracy must be removed.
    create_decimal = decimal.Context(prec=15).create_decimal_from_float
    if isinstance(expression, Col):
        quantize_value = decimal.Decimal(1).scaleb(
            -expression.output_field.decimal_places
        )

        def converter(value, expression, connection):
            if value is not None:
                return create_decimal(value).quantize(
                    quantize_value, context=expression.output_field.context
                )

    else:

        def converter(value, expression, connection):
            if value is not None:
                return create_decimal(value)

    return converter


# ==================================================
# Occurrences: Lines 358-363 (2 instances)

def convert_uuidfield_value(self, value, expression, connection):
    if value is not None:
        value = uuid.UUID(value)
    return value


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/sqlite3/base.py
# Line: 373

def convert_query(self, query, *, param_names=None):
    if param_names is None:
        # Convert from "format" style to "qmark" style.
        return FORMAT_QMARK_REGEX.sub("?", query).replace("%%", "%")
    else:
        # Convert from "pyformat" style to "named" style.
        return query % {name: f":{name}" for name in param_names}

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/sqlite3/features.py
# Line: 168

def can_return_columns_from_insert(self):
    return Database.sqlite_version_info >= (3, 35)


# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/sqlite3/introspection.py
# Line: 180

def _parse_column_or_constraint_definition(self, tokens, columns):
    token = None
    is_constraint_definition = None
    field_name = None
    constraint_name = None
    unique = False
    unique_columns = []
    check = False
    check_columns = []
    braces_deep = 0
    for token in tokens:
        if token.match(sqlparse.tokens.Punctuation, "("):
            braces_deep += 1
        elif token.match(sqlparse.tokens.Punctuation, ")"):
            braces_deep -= 1
            if braces_deep < 0:
                # End of columns and constraints for table definition.
                break
        elif braces_deep == 0 and token.match(sqlparse.tokens.Punctuation, ","):
            # End of current column or constraint definition.
            break
        # Detect column or constraint definition by first token.
        if is_constraint_definition is None:
            is_constraint_definition = token.match(
                sqlparse.tokens.Keyword, "CONSTRAINT"
            )
            if is_constraint_definition:
                continue
        if is_constraint_definition:
            # Detect constraint name by second token.
            if constraint_name is None:
                if token.ttype in (sqlparse.tokens.Name, sqlparse.tokens.Keyword):
                    constraint_name = token.value
                elif token.ttype == sqlparse.tokens.Literal.String.Symbol:
                    constraint_name = token.value[1:-1]
            # Start constraint columns parsing after UNIQUE keyword.
            if token.match(sqlparse.tokens.Keyword, "UNIQUE"):
                unique = True
                unique_braces_deep = braces_deep
            elif unique:
                if unique_braces_deep == braces_deep:
                    if unique_columns:
                        # Stop constraint parsing.
                        unique = False
                    continue
                if token.ttype in (sqlparse.tokens.Name, sqlparse.tokens.Keyword):
                    unique_columns.append(token.value)
                elif token.ttype == sqlparse.tokens.Literal.String.Symbol:
                    unique_columns.append(token.value[1:-1])
        else:
            # Detect field name by first token.
            if field_name is None:
                if token.ttype in (sqlparse.tokens.Name, sqlparse.tokens.Keyword):
                    field_name = token.value
                elif token.ttype == sqlparse.tokens.Literal.String.Symbol:
                    field_name = token.value[1:-1]
            if token.match(sqlparse.tokens.Keyword, "UNIQUE"):
                unique_columns = [field_name]
        # Start constraint columns parsing after CHECK keyword.
        if token.match(sqlparse.tokens.Keyword, "CHECK"):
            check = True
            check_braces_deep = braces_deep
        elif check:
            if check_braces_deep == braces_deep:
                if check_columns:
                    # Stop constraint parsing.
                    check = False
                continue
            if token.ttype in (sqlparse.tokens.Name, sqlparse.tokens.Keyword):
                if token.value in columns:
                    check_columns.append(token.value)
            elif token.ttype == sqlparse.tokens.Literal.String.Symbol:
                if token.value[1:-1] in columns:
                    check_columns.append(token.value[1:-1])
    unique_constraint = (
        {
            "unique": True,
            "columns": unique_columns,
            "primary_key": False,
            "foreign_key": None,
            "check": False,
            "index": False,
        }
        if unique_columns
        else None
    )
    check_constraint = (
        {
            "check": True,
            "columns": check_columns,
            "primary_key": False,
            "unique": False,
            "foreign_key": None,
            "index": False,
        }
        if check_columns
        else None
    )
    return constraint_name, unique_constraint, check_constraint, token


# ==================================================
# Line: 416

def _get_index_columns_orders(self, sql):
    tokens = sqlparse.parse(sql)[0]
    for token in tokens:
        if isinstance(token, sqlparse.sql.Parenthesis):
            columns = str(token).strip("()").split(", ")
            return ["DESC" if info.endswith("DESC") else "ASC" for info in columns]
    return None


# ==================================================
# Line: 424

def _get_column_collations(self, cursor, table_name):
    row = cursor.execute(
        """
        SELECT sql
        FROM sqlite_master
        WHERE type = 'table' AND name = %s
    """,
        [table_name],
    ).fetchone()
    if not row:
        return {}

    sql = row[0]
    columns = str(sqlparse.parse(sql)[0][-1]).strip("()").split(", ")
    collations = {}
    for column in columns:
        tokens = column[1:].split()
        column_name = tokens[0].strip('"')
        for index, token in enumerate(tokens):
            if token == "COLLATE":
                collation = tokens[index + 1]
                break
        else:
            collation = None
        collations[column_name] = collation
    return collations

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/sql/compiler.py
# Occurrences: Lines 1545-1550 (2 instances)

def has_composite_fields(self, expressions):
    # Check for composite fields before calling the relatively costly
    # composite_fields_to_tuples.
    return any(isinstance(expression, ColPairs) for expression in expressions)


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/sql/query.py
# Line: 1208

def check_alias(self, alias):
    if FORBIDDEN_ALIAS_PATTERN.search(alias):
        raise ValueError(
            "Column aliases cannot contain whitespace characters, quotation marks, "
            "semicolons, or SQL comments."
        )


# ==================================================
# Line: 1342

def check_query_object_type(self, value, opts, field):
    """
    Check whether the object passed while querying is of the correct type.
    If not, raise a ValueError specifying the wrong object.
    """
    if hasattr(value, "_meta"):
        if not check_rel_lookup_compatibility(value._meta.model, opts, field):
            raise ValueError(
                'Cannot query "%s": Must be "%s" instance.'
                % (value, opts.object_name)
            )


# ==================================================
# Line: 1436

def try_transform(self, lhs, name, lookups=None):
    """
    Helper method for build_lookup(). Try to fetch and initialize
    a transform for name parameter from lhs.
    """
    transform_class = lhs.get_transform(name)
    if transform_class:
        return transform_class(lhs)
    else:
        output_field = lhs.output_field.__class__
        suggested_lookups = difflib.get_close_matches(
            name, lhs.output_field.get_lookups()
        )
        if suggested_lookups:
            suggestion = ", perhaps you meant %s?" % " or ".join(suggested_lookups)
        else:
            suggestion = "."
        if lookups is not None:
            name_index = lookups.index(name)
            unsupported_lookup = LOOKUP_SEP.join(lookups[name_index:])
        else:
            unsupported_lookup = name
        raise FieldError(
            "Unsupported lookup '%s' for %s or join on the field not "
            "permitted%s" % (unsupported_lookup, output_field.__name__, suggestion)
        )


# ==================================================
# Line: 2677

def is_nullable(self, field):
    """
    Check if the given field should be treated as nullable.

    Some backends treat '' as null and Django treats such fields as
    nullable for those backends. In such situations field.null can be
    False even if we should treat the field as nullable.
    """
    # We need to use DEFAULT_DB_ALIAS here, as QuerySet does not have
    # (nor should it have) knowledge of which connection is going to be
    # used. The proper fix would be to defer all decisions where
    # is_nullable() is needed to the compiler stage, but that is not easy
    # to do currently.
    return field.null or (
        field.empty_strings_allowed
        and connections[DEFAULT_DB_ALIAS].features.interprets_empty_strings_as_nulls
    )



# ==================================================
# File: /root/ecooptimizer/django/django/db/models/sql/where.py
# Line: 293

def output_field(self):
    from django.db.models import BooleanField

    return BooleanField()


# ==================================================
# Line: 302

def select_format(self, compiler, sql, params):
    # Wrap filters with a CASE WHEN expression if a database backend
    # (e.g. Oracle) doesn't support boolean expression in SELECT or GROUP
    # BY list.
    if not compiler.connection.features.supports_boolean_expr_in_select_clause:
        sql = f"CASE WHEN {sql} THEN 1 ELSE 0 END"
    return sql, params


# ==================================================
# Line: 330

def as_sql(self, compiler=None, connection=None):
    raise EmptyResultSet



# ==================================================
# File: /root/ecooptimizer/django/django/db/models/signals.py
# Line: 15

def _lazy_method(self, method, apps, receiver, sender, **kwargs):
    from django.db.models.options import Options

    # This partial takes a single optional argument named "sender".
    partial_method = partial(method, receiver, **kwargs)
    if isinstance(sender, str):
        apps = apps or Options.default_apps
        apps.lazy_model_operation(partial_method, make_model_tuple(sender))
    else:
        return partial_method(sender)


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/constraints.py
# Occurrences: Lines 69-72 (2 instances)

def check(self, model, connection):
    return []


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/deletion.py
# Line: 180

def _has_signal_listeners(self, model):
    return signals.pre_delete.has_listeners(
        model
    ) or signals.post_delete.has_listeners(model)


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/query.py
# Line: 675

def _prepare_for_bulk_create(self, objs):
    objs_with_pk, objs_without_pk = [], []
    for obj in objs:
        if isinstance(obj.pk, DatabaseDefault):
            objs_without_pk.append(obj)
        elif obj._is_pk_set():
            objs_with_pk.append(obj)
        else:
            obj.pk = obj._meta.pk.get_pk_value_on_save(obj)
            if obj._is_pk_set():
                objs_with_pk.append(obj)
            else:
                objs_without_pk.append(obj)
        obj._prepare_related_fields_for_save(operation_name="bulk_create")
    return objs_with_pk, objs_without_pk


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/expressions.py
# Occurrences: Lines 209-215 (3 instances)

def get_source_expressions(self):
    return []


# ==================================================
# Line: 810

def compile(self, side, compiler, connection):
    try:
        output = side.output_field
    except FieldError:
        pass
    else:
        if output.get_internal_type() == "DurationField":
            sql, params = compiler.compile(side)
            return connection.ops.format_for_duration_arithmetic(sql), params
    return compiler.compile(side)


# ==================================================
# Line: 951

def as_sql(self, *args, **kwargs):
    raise ValueError(
        "This queryset contains a reference to an outer query and may "
        "only be used in a subquery."
    )


# ==================================================
# Line: 973

def get_group_by_cols(self):
    return []



# ==================================================
# Line: 1081

def _get_repr_options(self):
    """Return a dict of extra __init__() options to include in the repr."""
    return {}


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/manager.py
# Line: 79

def check(self, **kwargs):
    return []


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/fields/related.py
# Line: 848

def get_extra_descriptor_filter(self, instance):
    """
    Return an extra filter condition for related object fetching when
    user does 'instance.fieldname', that is the extra filter is used in
    the descriptor of the field.

    The filter should be either a dict usable in .filter(**kwargs) call or
    a Q-object. The condition will be ANDed together with the relation's
    joining columns.

    A parallel method is get_extra_restriction() which is used in
    JOIN and subquery conditions.
    """
    return {}


# ==================================================
# Line: 863

def get_extra_restriction(self, alias, related_alias):
    """
    Return a pair condition used for joining and subquery pushdown. The
    condition is something that responds to as_sql(compiler, connection)
    method.

    Note that currently referring both the 'alias' and 'related_alias'
    will not work in some conditions, like subquery pushdown.

    A parallel method is get_extra_descriptor_filter() which is used in
    instance.fieldname related object fetching.
    """
    return None


# ==================================================
# Line: 1235

def convert_empty_strings(self, value, expression, connection):
    if (not value) and isinstance(value, str):
        return None
    return value


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/fields/__init__.py
# Line: 562

def select_format(self, compiler, sql, params):
    """
    Custom format for select clauses. For example, GIS columns need to be
    selected as AsText(table.col) on MySQL as the table.col data can't be
    used by Django.
    """
    return sql, params


# ==================================================
# Line: 758

def to_python(self, value):
    """
    Convert the input value into the expected Python data type, raising
    django.core.exceptions.ValidationError if the data can't be converted.
    Return the converted value. Subclasses should override this.
    """
    return value


# ==================================================
# Line: 992

def get_prep_value(self, value):
    """Perform preliminary non-db specific value checks and conversions."""
    if isinstance(value, Promise):
        value = value._proxy____cast()
    return value


# ==================================================
# Line: 1154

def slice_expression(self, expression, start, length):
    """Return a slice of this field."""
    raise NotSupportedError("This field does not support slicing.")



# ==================================================
# Line: 1383

def _check_fix_default_value(self):
    return []


# ==================================================
# Line: 2702

def get_placeholder(self, value, compiler, connection):
    return connection.ops.binary_placeholder_sql(value)


# ==================================================
# Line: 2834

def formfield(self, **kwargs):
    return None



# ==================================================
# File: /root/ecooptimizer/django/django/db/models/fields/json.py
# Line: 184

def compile_json_path_final_key(self, connection, key_transform):
    # Compile the final key without interpreting ints as array elements.
    return ".%s" % json.dumps(key_transform)


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/lookups.py
# Line: 103

def get_db_prep_lookup(self, value, connection):
    return ("%s", [value])


# ==================================================
# Line: 163

def output_field(self):
    return BooleanField()


# ==================================================
# Line: 192

def select_format(self, compiler, sql, params):
    # Wrap filters with a CASE WHEN expression if a database backend
    # (e.g. Oracle) doesn't support boolean expression in SELECT or GROUP
    # BY list.
    if not compiler.connection.features.supports_boolean_expr_in_select_clause:
        sql = f"CASE WHEN {sql} THEN 1 ELSE 0 END"
    return sql, params


# ==================================================
# Line: 333

def resolve_expression_parameter(self, compiler, connection, sql, param):
    params = [param]
    if hasattr(param, "resolve_expression"):
        param = param.resolve_expression(compiler.query)
    if hasattr(param, "as_sql"):
        sql, params = compiler.compile(param)
    return sql, params


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/functions/json.py
# Line: 85

def join(self, args):
    pairs = zip(args[::2], args[1::2], strict=True)
    # Wrap 'key' in parentheses in case of postgres cast :: syntax.
    return ", ".join([f"({key}) VALUE {value}" for key, value in pairs])


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/functions/text.py
# Line: 310

def as_oracle(self, compiler, connection, **extra_context):
    raise NotSupportedError("SHA224 is not supported on Oracle.")



# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/questioner.py
# Occurrences: Lines 57-62 (2 instances)

def ask_not_null_addition(self, field_name, model_name):
    """Adding a NOT NULL field to a model."""
    # None means quit
    return None


# ==================================================
# Occurrences: Lines 79-84 (2 instances)

def ask_auto_now_add_addition(self, field_name, model_name):
    """Adding an auto_now_add field to a model."""
    # None means quit
    return None


# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/autodetector.py
# Line: 451

def check_dependency(self, operation, dependency):
    """
    Return True if the given operation depends on the given dependency,
    False otherwise.
    """
    # Created model
    if (
        dependency.field_name is None
        and dependency.type == OperationDependency.Type.CREATE
    ):
        return (
            isinstance(operation, operations.CreateModel)
            and operation.name_lower == dependency.model_name_lower
        )
    # Created field
    elif (
        dependency.field_name is not None
        and dependency.type == OperationDependency.Type.CREATE
    ):
        return (
            isinstance(operation, operations.CreateModel)
            and operation.name_lower == dependency.model_name_lower
            and any(dependency.field_name == x for x, y in operation.fields)
        ) or (
            isinstance(operation, operations.AddField)
            and operation.model_name_lower == dependency.model_name_lower
            and operation.name_lower == dependency.field_name_lower
        )
    # Removed field
    elif (
        dependency.field_name is not None
        and dependency.type == OperationDependency.Type.REMOVE
    ):
        return (
            isinstance(operation, operations.RemoveField)
            and operation.model_name_lower == dependency.model_name_lower
            and operation.name_lower == dependency.field_name_lower
        )
    # Removed model
    elif (
        dependency.field_name is None
        and dependency.type == OperationDependency.Type.REMOVE
    ):
        return (
            isinstance(operation, operations.DeleteModel)
            and operation.name_lower == dependency.model_name_lower
        )
    # Field being altered
    elif (
        dependency.field_name is not None
        and dependency.type == OperationDependency.Type.ALTER
    ):
        return (
            isinstance(operation, operations.AlterField)
            and operation.model_name_lower == dependency.model_name_lower
            and operation.name_lower == dependency.field_name_lower
        )
    # order_with_respect_to being unset for a field
    elif (
        dependency.field_name is not None
        and dependency.type == OperationDependency.Type.REMOVE_ORDER_WRT
    ):
        return (
            isinstance(operation, operations.AlterOrderWithRespectTo)
            and operation.name_lower == dependency.model_name_lower
            and (operation.order_with_respect_to or "").lower()
            != dependency.field_name_lower
        )
    # Field is removed and part of an index/unique_together
    elif (
        dependency.field_name is not None
        and dependency.type == OperationDependency.Type.ALTER_FOO_TOGETHER
    ):
        return (
            isinstance(
                operation,
                (operations.AlterUniqueTogether, operations.AlterIndexTogether),
            )
            and operation.name_lower == dependency.model_name_lower
        )
    # Unknown dependency. Raise an error.
    else:
        raise ValueError("Can't handle dependency %r" % (dependency,))


# ==================================================
# Line: 1452

def _constraint_should_be_dropped_and_recreated(
    self, old_constraint, new_constraint

# ==================================================
# Line: 1924

def _trim_to_apps(self, changes, app_labels):
    """
    Take changes from arrange_for_graph() and set of app labels, and return
    a modified set of changes which trims out as many migrations that are
    not in app_labels as possible. Note that some other migrations may
    still be present as they may be required dependencies.
    """
    # Gather other app dependencies in a first pass
    app_dependencies = {}
    for app_label, migrations in changes.items():
        for migration in migrations:
            for dep_app_label, name in migration.dependencies:
                app_dependencies.setdefault(app_label, set()).add(dep_app_label)
    required_apps = set(app_labels)
    # Keep resolving till there's no change
    old_required_apps = None
    while old_required_apps != required_apps:
        old_required_apps = set(required_apps)
        required_apps.update(
            *[app_dependencies.get(app_label, ()) for app_label in required_apps]
        )
    # Remove all migrations that aren't needed
    for app_label in list(changes):
        if app_label not in required_apps:
            del changes[app_label]
    return changes


# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/graph.py
# Line: 220

def iterative_dfs(self, start, forwards=True):
    """Iterative depth-first search for finding dependencies."""
    visited = []
    visited_set = set()
    stack = [(start, False)]
    while stack:
        node, processed = stack.pop()
        if node in visited_set:
            pass
        elif processed:
            visited_set.add(node)
            visited.append(node.key)
        else:
            stack.append((node, True))
            stack += [
                (n, False)
                for n in sorted(node.parents if forwards else node.children)
            ]
    return visited


# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/optimizer.py
# Line: 40

def optimize_inner(self, operations, app_label):
    """Inner optimization loop."""
    new_operations = []
    for i, operation in enumerate(operations):
        right = True  # Should we reduce on the right or on the left.
        # Compare it to each operation after it
        for j, other in enumerate(operations[i + 1 :]):
            result = operation.reduce(other, app_label)
            if isinstance(result, list):
                in_between = operations[i + 1 : i + j + 1]
                if right:
                    new_operations.extend(in_between)
                    new_operations.extend(result)
                elif all(op.reduce(other, app_label) is True for op in in_between):
                    # Perform a left reduction if all of the in-between
                    # operations can optimize through other.
                    new_operations.extend(result)
                    new_operations.extend(in_between)
                else:
                    # Otherwise keep trying.
                    new_operations.append(operation)
                    break
                new_operations.extend(operations[i + j + 2 :])
                return new_operations
            elif not result:
                # Can't perform a right reduction.
                right = False
        else:
            new_operations.append(operation)
    return new_operations

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/operations/base.py
# Line: 127

def references_model(self, name, app_label):
    """
    Return True if there is a chance this operation references the given
    model name (as a string), with an app label for accuracy.

    Used for optimization. If in doubt, return True;
    returning a false positive will merely make the optimizer a little
    less efficient, while returning a false negative may result in an
    unusable optimized migration.
    """
    return True


# ==================================================
# Line: 148

def allow_migrate_model(self, connection_alias, model):
    """
    Return whether or not a model may be migrated.

    This is a thin wrapper around router.allow_migrate_model() that
    preemptively rejects any proxy, swapped out, or unmanaged model.
    """
    if not model._meta.can_migrate(connection_alias):
        return False

    return router.allow_migrate_model(connection_alias, model)


# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/operations/special.py
# Line: 121

def _run_sql(self, schema_editor, sqls):
    if isinstance(sqls, (list, tuple)):
        for sql in sqls:
            params = None
            if isinstance(sql, (list, tuple)):
                elements = len(sql)
                if elements == 2:
                    sql, params = sql
                else:
                    raise ValueError("Expected a 2-tuple but got %d" % elements)
            schema_editor.execute(sql, params=params)
    elif sqls != RunSQL.noop:
        statements = schema_editor.connection.ops.prepare_sql_script(sqls)
        for statement in statements:
            schema_editor.execute(statement, params=None)



# ==================================================
# File: /root/ecooptimizer/django/django/urls/resolvers.py
# Line: 149

def _compile(self, regex):
    try:
        return re.compile(regex)
    except re.error as e:
        raise ImproperlyConfigured(
            f'"{regex}" is not a valid regular expression: {e}'
        ) from e



# ==================================================
# Line: 410

def check(self):
    return []


# ==================================================
# File: /root/ecooptimizer/django/django/urls/converters.py
# Occurrences: Lines 8-11 (2 instances)

def to_python(self, value):
    return int(value)


# ==================================================
# Occurrences: Lines 18-21 (2 instances)

def to_python(self, value):
    return value


# ==================================================
# Occurrences: Lines 28-31 (2 instances)

def to_python(self, value):
    return uuid.UUID(value)


# ==================================================
# File: /root/ecooptimizer/django/django/forms/formsets.py
# Line: 375

def _should_delete_form(self, form):
    """Return whether or not the form was marked for deletion."""
    return form.cleaned_data.get(DELETION_FIELD_NAME, False)


# ==================================================
# File: /root/ecooptimizer/django/django/forms/widgets.py
# Line: 183

def absolute_path(self, path):
    """
    Given a relative or absolute path to a static asset, return an absolute
    path. An absolute path will be returned unchanged while a relative path
    will be passed to django.templatetags.static.static().
    """
    if path.startswith(("http://", "https://", "/")):
        return path
    return static(path)


# ==================================================
# Occurrences: Lines 332-341 (3 instances)

def _render(self, template_name, context, renderer=None):
    if renderer is None:
        renderer = get_default_renderer()
    return mark_safe(renderer.render(template_name, context))


# ==================================================
# Occurrences: Lines 348-351 (2 instances)

def value_omitted_from_data(self, data, files, name):
    return name not in data


# ==================================================
# Line: 533

def clear_checkbox_name(self, name):
    """
    Given the name of the file input, return the name of the clear checkbox
    input.
    """
    return name + "-clear"


# ==================================================
# Line: 540

def clear_checkbox_id(self, name):
    """
    Given the name of the clear checkbox input, return the HTML id for it.
    """
    return name + "_id"


# ==================================================
# Line: 546

def is_initial(self, value):
    """
    Return whether value is considered to be initial value.
    """
    return bool(value and getattr(value, "url", False))


# ==================================================
# File: /root/ecooptimizer/django/django/forms/renderers.py
# Line: 64

def backend(self):
    from django.template.backends.jinja2 import Jinja2

    return Jinja2



# ==================================================
# File: /root/ecooptimizer/django/django/forms/models.py
# Line: 723

def _get_to_python(self, field):
    """
    If the field is a related field, fetch the concrete field's (that
    is, the ultimate pointed-to field's) to_python.
    """
    while field.remote_field is not None:
        field = field.remote_field.get_related_field()
    return field.to_python


# ==================================================
# Occurrences: Lines 785-793 (3 instances)

def save_new(self, form, commit=True):
    """Save and return a new model instance for the given form."""
    return form.save(commit=commit)


# ==================================================
# Line: 917

def get_unique_error_message(self, unique_check):
    if len(unique_check) == 1:
        return gettext("Please correct the duplicate data for %(field)s.") % {
            "field": unique_check[0],
        }
    else:
        return gettext(
            "Please correct the duplicate data for %(field)s, which must be unique."
        ) % {
            "field": get_text_list(unique_check, _("and")),
        }


# ==================================================
# Line: 929

def get_date_error_message(self, date_check):
    return gettext(
        "Please correct the duplicate data for %(field_name)s "
        "which must be unique for the %(lookup)s in %(date_field)s."
    ) % {
        "field_name": date_check[2],
        "date_field": date_check[3],
        "lookup": str(date_check[1]),
    }


# ==================================================
# Line: 939

def get_form_error(self):
    return gettext("Please correct the duplicate values below.")


# ==================================================
# Line: 1509

def validate_no_null_characters(self, value):
    non_null_character_validator = ProhibitNullCharactersValidator()
    return non_null_character_validator(value)


# ==================================================
# Line: 1541

def label_from_instance(self, obj):
    """
    Convert objects into strings and generate the labels for the choices
    presented by this object. Subclasses can override this method to
    customize the display of the choices.
    """
    return str(obj)


# ==================================================
# File: /root/ecooptimizer/django/django/forms/fields.py
# Occurrences: Lines 176-179 (2 instances)

def prepare_value(self, value):
    return value


# ==================================================
# Line: 223

def widget_attrs(self, widget):
    """
    Given a Widget instance (*not* a Widget class), return a dictionary of
    any HTML attributes that should be added to the Widget, based on this
    Field.
    """
    return {}


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/filters.py
# Line: 258

def field_admin_ordering(self, field, request, model_admin):
    """
    Return the model admin's ordering for related field, if provided.
    """
    try:
        related_admin = model_admin.admin_site.get_model_admin(
            field.remote_field.model
        )
    except NotRegistered:
        return ()
    else:
        return related_admin.get_ordering(request)


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/tests.py
# Line: 16

def process_response(self, request, response):
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response



# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/widgets.py
# Occurrences: Lines 237-242 (2 instances)

def value_from_datadict(self, data, files, name):
    value = data.get(name)
    if value:
        return value.split(",")


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/sites.py
# Line: 203

def has_permission(self, request):
    """
    Return True if the given HttpRequest has permission to view
    *at least one* page in the admin site.
    """
    return request.user.is_active and request.user.is_staff


# ==================================================
# Line: 382

def i18n_javascript(self, request, extra_context=None):
    """
    Display the i18n JavaScript that the Django admin requires.

    `extra_context` is unused but present for consistency with the other
    admin views.
    """
    return JavaScriptCatalog.as_view(packages=["django.contrib.admin"])(request)


# ==================================================
# Line: 456

def catch_all_view(self, request, url):
    if settings.APPEND_SLASH and not url.endswith("/"):
        urlconf = getattr(request, "urlconf", None)
        try:
            match = resolve("%s/" % request.path_info, urlconf)
        except Resolver404:
            pass
        else:
            if getattr(match.func, "should_append_slash", True):
                return HttpResponsePermanentRedirect(
                    request.get_full_path(force_append_slash=True)
                )
    raise Http404


# ==================================================
# Line: 603

def get_log_entries(self, request):
    from django.contrib.admin.models import LogEntry

    return LogEntry.objects.select_related("content_type", "user")



# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/views/autocomplete.py
# Line: 45

def serialize_result(self, obj, to_field_name):
    """
    Convert the provided model object to a dictionary that is added to the
    results list.
    """
    return {"id": str(getattr(obj, to_field_name)), "text": str(obj)}


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/options.py
# Line: 837

def get_changelist(self, request, **kwargs):
    """
    Return the ChangeList class for use on the changelist page.
    """
    from django.contrib.admin.views.main import ChangeList

    return ChangeList


# ==================================================
# Line: 935

def log_addition(self, request, obj, message):
    """
    Log that an object has been successfully added.

    The default implementation creates an admin LogEntry object.
    """
    from django.contrib.admin.models import ADDITION, LogEntry

    return LogEntry.objects.log_actions(
        user_id=request.user.pk,
        queryset=[obj],
        action_flag=ADDITION,
        change_message=message,
        single_object=True,
    )


# ==================================================
# Line: 951

def log_change(self, request, obj, message):
    """
    Log that an object has been successfully changed.

    The default implementation creates an admin LogEntry object.
    """
    from django.contrib.admin.models import CHANGE, LogEntry

    return LogEntry.objects.log_actions(
        user_id=request.user.pk,
        queryset=[obj],
        action_flag=CHANGE,
        change_message=message,
        single_object=True,
    )


# ==================================================
# Line: 967

def log_deletions(self, request, queryset):
    """
    Log that objects will be deleted. Note that this method must be called
    before the deletion.

    The default implementation creates admin LogEntry objects.
    """
    from django.contrib.admin.models import DELETION, LogEntry

    return LogEntry.objects.log_actions(
        user_id=request.user.pk,
        queryset=queryset,
        action_flag=DELETION,
    )


# ==================================================
# Line: 982

def action_checkbox(self, obj):
    """
    A list_display column containing a checkbox widget.
    """
    attrs = {
        "class": "action-select",
        "aria-label": format_html(
            _("Select this object for an action - {}"), str(obj)
        ),
    }
    checkbox = forms.CheckboxInput(attrs, lambda value: False)
    return checkbox.render(helpers.ACTION_CHECKBOX_NAME, str(obj.pk))


# ==================================================
# Line: 1227

def construct_change_message(self, request, form, formsets, add=False):
    """
    Construct a JSON structure describing changes from a changed object.
    """
    return construct_change_message(form, formsets, add)


# ==================================================
# Line: 1233

def message_user(
    self, request, message, level=messages.INFO, extra_tags="", fail_silently=False

# ==================================================
# Line: 1261

def save_form(self, request, form, change):
    """
    Given a ModelForm return an unsaved instance. ``change`` is True if
    the object is being changed, and False if it's being added.
    """
    return form.save(commit=False)


# ==================================================
# Line: 1268

def save_model(self, request, obj, form, change):
    """
    Given a model instance save it to the database.
    """
    obj.save()


# ==================================================
# Line: 1274

def delete_model(self, request, obj):
    """
    Given a model instance delete it from the database.
    """
    obj.delete()


# ==================================================
# Occurrences: Lines 1280-1284 (2 instances)

def delete_queryset(self, request, queryset):
    """Given a queryset, delete it from the database."""
    queryset.delete()


# ==================================================
# Line: 1366

def _get_preserved_qsl(self, request, preserved_filters):
    query_string = urlsplit(request.build_absolute_uri()).query
    return parse_qsl(query_string.replace(preserved_filters, ""))


# ==================================================
# Line: 2292

def get_formset_kwargs(self, request, obj, inline, prefix):
    formset_params = {
        "instance": obj,
        "prefix": prefix,
        "queryset": inline.get_queryset(request),
    }
    if request.method == "POST":
        formset_params.update(
            {
                "data": request.POST.copy(),
                "files": request.FILES,
                "save_as_new": "_saveasnew" in request.POST,
            }
        )
    return formset_params


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/checks.py
# Line: 218

def _check_autocomplete_fields_item(self, obj, field_name, label):
    """
    Check that an item in `autocomplete_fields` is a ForeignKey or a
    ManyToManyField and that the item has a related ModelAdmin with
    search_fields defined.
    """
    try:
        field = obj.model._meta.get_field(field_name)
    except FieldDoesNotExist:
        return refer_to_missing_field(
            field=field_name, option=label, obj=obj, id="admin.E037"
        )
    else:
        if not field.many_to_many and not isinstance(field, models.ForeignKey):
            return must_be(
                "a foreign key or a many-to-many field",
                option=label,
                obj=obj,
                id="admin.E038",
            )
        try:
            related_admin = obj.admin_site.get_model_admin(field.remote_field.model)
        except NotRegistered:
            return [
                checks.Error(
                    'An admin for model "%s" has to be registered '
                    "to be referenced by %s.autocomplete_fields."
                    % (
                        field.remote_field.model.__name__,
                        type(obj).__name__,
                    ),
                    obj=obj.__class__,
                    id="admin.E039",
                )
            ]
        else:
            if not related_admin.search_fields:
                return [
                    checks.Error(
                        '%s must define "search_fields", because it\'s '
                        "referenced by %s.autocomplete_fields."
                        % (
                            related_admin.__class__.__name__,
                            type(obj).__name__,
                        ),
                        obj=obj.__class__,
                        id="admin.E040",
                    )
                ]
        return []


# ==================================================
# Line: 287

def _check_raw_id_fields_item(self, obj, field_name, label):
    """Check an item of `raw_id_fields`, i.e. check that field named
    `field_name` exists in model `model` and is a ForeignKey or a
    ManyToManyField."""

    try:
        field = obj.model._meta.get_field(field_name)
    except FieldDoesNotExist:
        return refer_to_missing_field(
            field=field_name, option=label, obj=obj, id="admin.E002"
        )
    else:
        # Using attname is not supported.
        if field.name != field_name:
            return refer_to_missing_field(
                field=field_name,
                option=label,
                obj=obj,
                id="admin.E002",
            )
        if not field.many_to_many and not isinstance(field, models.ForeignKey):
            return must_be(
                "a foreign key or a many-to-many field",
                option=label,
                obj=obj,
                id="admin.E003",
            )
        else:
            return []


# ==================================================
# Line: 446

def _check_field_spec_item(self, obj, field_name, label):
    if field_name in obj.readonly_fields:
        # Stuff can be put in fields that isn't actually a model field if
        # it's in readonly_fields, readonly_fields will handle the
        # validation of such things.
        return []
    else:
        try:
            field = obj.model._meta.get_field(field_name)
        except FieldDoesNotExist:
            # If we can't find a field on the model that matches, it could
            # be an extra field on the form.
            return []
        else:
            if (
                isinstance(field, models.ManyToManyField)
                and not field.remote_field.through._meta.auto_created
            ):
                return [
                    checks.Error(
                        "The value of '%s' cannot include the ManyToManyField "
                        "'%s', because that field manually specifies a "
                        "relationship model." % (label, field_name),
                        obj=obj.__class__,
                        id="admin.E013",
                    )
                ]
            else:
                return []


# ==================================================
# Line: 476

def _check_exclude(self, obj):
    """Check that exclude is a sequence without duplicates."""

    if obj.exclude is None:  # default value is None
        return []
    elif not isinstance(obj.exclude, (list, tuple)):
        return must_be(
            "a list or tuple", option="exclude", obj=obj, id="admin.E014"
        )
    field_counts = collections.Counter(obj.exclude)
    if duplicate_fields := [
        field for field, count in field_counts.items() if count > 1
    ]:
        return [
            checks.Error(
                "The value of 'exclude' contains duplicate field(s).",
                hint="Remove duplicates of %s."
                % ", ".join(map(repr, duplicate_fields)),
                obj=obj.__class__,
                id="admin.E015",
            )
        ]
    else:
        return []


# ==================================================
# Line: 501

def _check_form(self, obj):
    """Check that form subclasses BaseModelForm."""
    if not _issubclass(obj.form, BaseModelForm):
        return must_inherit_from(
            parent="BaseModelForm", option="form", obj=obj, id="admin.E016"
        )
    else:
        return []


# ==================================================
# Line: 542

def _check_filter_item(self, obj, field_name, label):
    """Check one item of `filter_vertical` or `filter_horizontal`, i.e.
    check that given field exists and is a ManyToManyField."""

    try:
        field = obj.model._meta.get_field(field_name)
    except FieldDoesNotExist:
        return refer_to_missing_field(
            field=field_name, option=label, obj=obj, id="admin.E019"
        )
    else:
        if not field.many_to_many or isinstance(field, models.ManyToManyRel):
            return must_be(
                "a many-to-many field", option=label, obj=obj, id="admin.E020"
            )
        elif not field.remote_field.through._meta.auto_created:
            return [
                checks.Error(
                    f"The value of '{label}' cannot include the ManyToManyField "
                    f"'{field_name}', because that field manually specifies a "
                    f"relationship model.",
                    obj=obj.__class__,
                    id="admin.E013",
                )
            ]
        else:
            return []


# ==================================================
# Line: 587

def _check_radio_fields_key(self, obj, field_name, label):
    """Check that a key of `radio_fields` dictionary is name of existing
    field and that the field is a ForeignKey or has `choices` defined."""

    try:
        field = obj.model._meta.get_field(field_name)
    except FieldDoesNotExist:
        return refer_to_missing_field(
            field=field_name, option=label, obj=obj, id="admin.E022"
        )
    else:
        if not (isinstance(field, models.ForeignKey) or field.choices):
            return [
                checks.Error(
                    "The value of '%s' refers to '%s', which is not an "
                    "instance of ForeignKey, and does not have a 'choices' "
                    "definition." % (label, field_name),
                    obj=obj.__class__,
                    id="admin.E023",
                )
            ]
        else:
            return []


# ==================================================
# Line: 611

def _check_radio_fields_value(self, obj, val, label):
    """Check type of a value of `radio_fields` dictionary."""

    from django.contrib.admin.options import HORIZONTAL, VERTICAL

    if val not in (HORIZONTAL, VERTICAL):
        return [
            checks.Error(
                "The value of '%s' must be either admin.HORIZONTAL or "
                "admin.VERTICAL." % label,
                obj=obj.__class__,
                id="admin.E024",
            )
        ]
    else:
        return []


# ==================================================
# Line: 628

def _check_view_on_site_url(self, obj):
    if not callable(obj.view_on_site) and not isinstance(obj.view_on_site, bool):
        return [
            checks.Error(
                "The value of 'view_on_site' must be a callable or a boolean "
                "value.",
                obj=obj.__class__,
                id="admin.E025",
            )
        ]
    else:
        return []


# ==================================================
# Line: 661

def _check_prepopulated_fields_key(self, obj, field_name, label):
    """Check a key of `prepopulated_fields` dictionary, i.e. check that it
    is a name of existing field and the field is one of the allowed types.
    """

    try:
        field = obj.model._meta.get_field(field_name)
    except FieldDoesNotExist:
        return refer_to_missing_field(
            field=field_name, option=label, obj=obj, id="admin.E027"
        )
    else:
        if isinstance(
            field, (models.DateTimeField, models.ForeignKey, models.ManyToManyField)
        ):
            return [
                checks.Error(
                    "The value of '%s' refers to '%s', which must not be a "
                    "DateTimeField, a ForeignKey, a OneToOneField, or a "
                    "ManyToManyField." % (label, field_name),
                    obj=obj.__class__,
                    id="admin.E028",
                )
            ]
        else:
            return []


# ==================================================
# Line: 704

def _check_prepopulated_fields_value_item(self, obj, field_name, label):
    """For `prepopulated_fields` equal to {"slug": ("title",)},
    `field_name` is "title"."""

    try:
        obj.model._meta.get_field(field_name)
    except FieldDoesNotExist:
        return refer_to_missing_field(
            field=field_name, option=label, obj=obj, id="admin.E030"
        )
    else:
        return []


# ==================================================
# Line: 735

def _check_ordering_item(self, obj, field_name, label):
    """Check that `ordering` refers to existing fields."""
    if isinstance(field_name, (Combinable, models.OrderBy)):
        if not isinstance(field_name, models.OrderBy):
            field_name = field_name.asc()
        if isinstance(field_name.expression, models.F):
            field_name = field_name.expression.name
        else:
            return []
    if field_name == "?" and len(obj.ordering) != 1:
        return [
            checks.Error(
                "The value of 'ordering' has the random ordering marker '?', "
                "but contains other fields as well.",
                hint='Either remove the "?", or remove the other fields.',
                obj=obj.__class__,
                id="admin.E032",
            )
        ]
    elif field_name == "?":
        return []
    elif LOOKUP_SEP in field_name:
        # Skip ordering in the format field1__field2 (FIXME: checking
        # this format would be nice, but it's a little fiddly).
        return []
    else:
        field_name = field_name.removeprefix("-")
        if field_name == "pk":
            return []
        try:
            obj.model._meta.get_field(field_name)
        except FieldDoesNotExist:
            return refer_to_missing_field(
                field=field_name, option=label, obj=obj, id="admin.E033"
            )
        else:
            return []


# ==================================================
# Line: 792

def _check_readonly_fields_item(self, obj, field_name, label):
    if callable(field_name):
        return []
    elif hasattr(obj, field_name):
        return []
    elif hasattr(obj.model, field_name):
        return []
    else:
        try:
            obj.model._meta.get_field(field_name)
        except FieldDoesNotExist:
            return [
                checks.Error(
                    "The value of '%s' refers to '%s', which is not a callable, "
                    "an attribute of '%s', or an attribute of '%s'."
                    % (
                        label,
                        field_name,
                        obj.__class__.__name__,
                        obj.model._meta.label,
                    ),
                    obj=obj.__class__,
                    id="admin.E035",
                )
            ]
        else:
            return []



# ==================================================
# Line: 840

def _check_save_as(self, obj):
    """Check save_as is a boolean."""

    if not isinstance(obj.save_as, bool):
        return must_be("a boolean", option="save_as", obj=obj, id="admin.E101")
    else:
        return []


# ==================================================
# Line: 848

def _check_save_on_top(self, obj):
    """Check save_on_top is a boolean."""

    if not isinstance(obj.save_on_top, bool):
        return must_be("a boolean", option="save_on_top", obj=obj, id="admin.E102")
    else:
        return []


# ==================================================
# Line: 871

def _check_inlines_item(self, obj, inline, label):
    """Check one inline model admin."""
    try:
        inline_label = inline.__module__ + "." + inline.__name__
    except AttributeError:
        return [
            checks.Error(
                "'%s' must inherit from 'InlineModelAdmin'." % obj,
                obj=obj.__class__,
                id="admin.E104",
            )
        ]

    from django.contrib.admin.options import InlineModelAdmin

    if not _issubclass(inline, InlineModelAdmin):
        return [
            checks.Error(
                "'%s' must inherit from 'InlineModelAdmin'." % inline_label,
                obj=obj.__class__,
                id="admin.E104",
            )
        ]
    elif not inline.model:
        return [
            checks.Error(
                "'%s' must have a 'model' attribute." % inline_label,
                obj=obj.__class__,
                id="admin.E105",
            )
        ]
    elif not _issubclass(inline.model, models.Model):
        return must_be(
            "a Model", option="%s.model" % inline_label, obj=obj, id="admin.E106"
        )
    else:
        return inline(obj.model, obj.admin_site).check()


# ==================================================
# Line: 924

def _check_list_display_item(self, obj, item, label):
    if callable(item):
        return []
    elif hasattr(obj, item):
        return []
    try:
        field = obj.model._meta.get_field(item)
    except FieldDoesNotExist:
        try:
            field = getattr(obj.model, item)
        except AttributeError:
            try:
                field = get_fields_from_path(obj.model, item)[-1]
            except (FieldDoesNotExist, NotRelationField):
                return [
                    checks.Error(
                        f"The value of '{label}' refers to '{item}', which is not "
                        f"a callable or attribute of '{obj.__class__.__name__}', "
                        "or an attribute, method, or field on "
                        f"'{obj.model._meta.label}'.",
                        obj=obj.__class__,
                        id="admin.E108",
                    )
                ]
    if (
        getattr(field, "is_relation", False)
        and (field.many_to_many or field.one_to_many)
    ) or (getattr(field, "rel", None) and field.rel.field.many_to_one):
        return [
            checks.Error(
                f"The value of '{label}' must not be a many-to-many field or a "
                f"reverse foreign key.",
                obj=obj.__class__,
                id="admin.E109",
            )
        ]
    return []


# ==================================================
# Line: 987

def _check_list_display_links_item(self, obj, field_name, label):
    if field_name not in obj.list_display:
        return [
            checks.Error(
                "The value of '%s' refers to '%s', which is not defined in "
                "'list_display'." % (label, field_name),
                obj=obj.__class__,
                id="admin.E111",
            )
        ]
    else:
        return []


# ==================================================
# Line: 1013

def _check_list_filter_item(self, obj, item, label):
    """
    Check one item of `list_filter`, i.e. check if it is one of three options:
    1. 'field' -- a basic field filter, possibly w/ relationships (e.g.
       'field__rel')
    2. ('field', SomeFieldListFilter) - a field-based list filter class
    3. SomeListFilter - a non-field list filter class
    """
    from django.contrib.admin import FieldListFilter, ListFilter

    if callable(item) and not isinstance(item, models.Field):
        # If item is option 3, it should be a ListFilter...
        if not _issubclass(item, ListFilter):
            return must_inherit_from(
                parent="ListFilter", option=label, obj=obj, id="admin.E113"
            )
        # ...  but not a FieldListFilter.
        elif issubclass(item, FieldListFilter):
            return [
                checks.Error(
                    "The value of '%s' must not inherit from 'FieldListFilter'."
                    % label,
                    obj=obj.__class__,
                    id="admin.E114",
                )
            ]
        else:
            return []
    elif isinstance(item, (tuple, list)):
        # item is option #2
        field, list_filter_class = item
        if not _issubclass(list_filter_class, FieldListFilter):
            return must_inherit_from(
                parent="FieldListFilter",
                option="%s[1]" % label,
                obj=obj,
                id="admin.E115",
            )
        else:
            return []
    else:
        # item is option #1
        field = item

        # Validate the field string
        try:
            get_fields_from_path(obj.model, field)
        except (NotRelationField, FieldDoesNotExist):
            return [
                checks.Error(
                    "The value of '%s' refers to '%s', which does not refer to a "
                    "Field." % (label, field),
                    obj=obj.__class__,
                    id="admin.E116",
                )
            ]
        else:
            return []


# ==================================================
# Line: 1072

def _check_list_select_related(self, obj):
    """Check that list_select_related is a boolean, a list or a tuple."""

    if not isinstance(obj.list_select_related, (bool, list, tuple)):
        return must_be(
            "a boolean, tuple or list",
            option="list_select_related",
            obj=obj,
            id="admin.E117",
        )
    else:
        return []


# ==================================================
# Line: 1085

def _check_list_per_page(self, obj):
    """Check that list_per_page is an integer."""

    if not isinstance(obj.list_per_page, int):
        return must_be(
            "an integer", option="list_per_page", obj=obj, id="admin.E118"
        )
    else:
        return []


# ==================================================
# Line: 1095

def _check_list_max_show_all(self, obj):
    """Check that list_max_show_all is an integer."""

    if not isinstance(obj.list_max_show_all, int):
        return must_be(
            "an integer", option="list_max_show_all", obj=obj, id="admin.E119"
        )
    else:
        return []


# ==================================================
# Line: 1123

def _check_list_editable_item(self, obj, field_name, label):
    try:
        field = obj.model._meta.get_field(field_name)
    except FieldDoesNotExist:
        return refer_to_missing_field(
            field=field_name, option=label, obj=obj, id="admin.E121"
        )
    else:
        if field_name not in obj.list_display:
            return [
                checks.Error(
                    "The value of '%s' refers to '%s', which is not "
                    "contained in 'list_display'." % (label, field_name),
                    obj=obj.__class__,
                    id="admin.E122",
                )
            ]
        elif obj.list_display_links and field_name in obj.list_display_links:
            return [
                checks.Error(
                    "The value of '%s' cannot be in both 'list_editable' and "
                    "'list_display_links'." % field_name,
                    obj=obj.__class__,
                    id="admin.E123",
                )
            ]
        # If list_display[0] is in list_editable, check that
        # list_display_links is set. See #22792 and #26229 for use cases.
        elif (
            obj.list_display[0] == field_name
            and not obj.list_display_links
            and obj.list_display_links is not None
        ):
            return [
                checks.Error(
                    "The value of '%s' refers to the first field in 'list_display' "
                    "('%s'), which cannot be used unless 'list_display_links' is "
                    "set." % (label, obj.list_display[0]),
                    obj=obj.__class__,
                    id="admin.E124",
                )
            ]
        elif not field.editable or field.primary_key:
            return [
                checks.Error(
                    "The value of '%s' refers to '%s', which is not editable "
                    "through the admin." % (label, field_name),
                    obj=obj.__class__,
                    id="admin.E125",
                )
            ]
        else:
            return []


# ==================================================
# Line: 1177

def _check_search_fields(self, obj):
    """Check search_fields is a sequence."""

    if not isinstance(obj.search_fields, (list, tuple)):
        return must_be(
            "a list or tuple", option="search_fields", obj=obj, id="admin.E126"
        )
    else:
        return []


# ==================================================
# Line: 1187

def _check_date_hierarchy(self, obj):
    """Check that date_hierarchy refers to DateField or DateTimeField."""

    if obj.date_hierarchy is None:
        return []
    else:
        try:
            field = get_fields_from_path(obj.model, obj.date_hierarchy)[-1]
        except (NotRelationField, FieldDoesNotExist):
            return [
                checks.Error(
                    "The value of 'date_hierarchy' refers to '%s', which "
                    "does not refer to a Field." % obj.date_hierarchy,
                    obj=obj.__class__,
                    id="admin.E127",
                )
            ]
        else:
            if field.get_internal_type() not in {"DateField", "DateTimeField"}:
                return must_be(
                    "a DateField or DateTimeField",
                    option="date_hierarchy",
                    obj=obj,
                    id="admin.E128",
                )
            else:
                return []


# ==================================================
# Line: 1215

def _check_actions(self, obj):
    errors = []
    actions = obj._get_base_actions()

    # Actions with an allowed_permission attribute require the ModelAdmin
    # to implement a has_<perm>_permission() method for each permission.
    for func, name, _ in actions:
        if not hasattr(func, "allowed_permissions"):
            continue
        for permission in func.allowed_permissions:
            method_name = "has_%s_permission" % permission
            if not hasattr(obj, method_name):
                errors.append(
                    checks.Error(
                        "%s must define a %s() method for the %s action."
                        % (
                            obj.__class__.__name__,
                            method_name,
                            func.__name__,
                        ),
                        obj=obj.__class__,
                        id="admin.E129",
                    )
                )
    # Names need to be unique.
    names = collections.Counter(name for _, name, _ in actions)
    for name, count in names.items():
        if count > 1:
            errors.append(
                checks.Error(
                    "__name__ attributes of actions defined in %s must be "
                    "unique. Name %r is not unique."
                    % (
                        obj.__class__.__name__,
                        name,
                    ),
                    obj=obj.__class__,
                    id="admin.E130",
                )
            )
    return errors



# ==================================================
# Line: 1302

def _check_relation(self, obj, parent_model):
    try:
        _get_foreign_key(parent_model, obj.model, fk_name=obj.fk_name)
    except ValueError as e:
        return [checks.Error(e.args[0], obj=obj.__class__, id="admin.E202")]
    else:
        return []


# ==================================================
# Line: 1310

def _check_extra(self, obj):
    """Check that extra is an integer."""

    if not isinstance(obj.extra, int):
        return must_be("an integer", option="extra", obj=obj, id="admin.E203")
    else:
        return []


# ==================================================
# Line: 1318

def _check_max_num(self, obj):
    """Check that max_num is an integer."""

    if obj.max_num is None:
        return []
    elif not isinstance(obj.max_num, int):
        return must_be("an integer", option="max_num", obj=obj, id="admin.E204")
    else:
        return []


# ==================================================
# Line: 1328

def _check_min_num(self, obj):
    """Check that min_num is an integer."""

    if obj.min_num is None:
        return []
    elif not isinstance(obj.min_num, int):
        return must_be("an integer", option="min_num", obj=obj, id="admin.E205")
    else:
        return []


# ==================================================
# Line: 1338

def _check_formset(self, obj):
    """Check formset is a subclass of BaseModelFormSet."""

    if not _issubclass(obj.formset, BaseModelFormSet):
        return must_inherit_from(
            parent="BaseModelFormSet", option="formset", obj=obj, id="admin.E206"
        )
    else:
        return []



# ==================================================
# File: /root/ecooptimizer/django/django/contrib/staticfiles/handlers.py
# Line: 29

def get_base_url(self):
    utils.check_settings()
    return settings.STATIC_URL


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/staticfiles/storage.py
# Line: 125

def file_hash(self, name, content=None):
    """
    Return a hash of the file with the given name and optional content.
    """
    if content is None:
        return None
    hasher = md5(usedforsecurity=False)
    for chunk in content.chunks():
        hasher.update(chunk)
    return hasher.hexdigest()[:12]


# ==================================================
# Occurrences: Lines 413-416 (2 instances)

def clean_name(self, name):
    return name.replace("\\", "/")


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/staticfiles/finders.py
# Line: 172

def find_location(self, root, path, prefix=None):
    """
    Find a requested static file in a location and return the found
    absolute path (or ``None`` if no match).
    """
    if prefix:
        prefix = "%s%s" % (prefix, os.sep)
        if not path.startswith(prefix):
            return None
        path = path.removeprefix(prefix)
    path = safe_join(root, path)
    if os.path.exists(path):
        return path


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/staticfiles/management/commands/collectstatic.py
# Line: 39

def add_arguments(self, parser):
    parser.add_argument(
        "--noinput",
        "--no-input",
        action="store_false",
        dest="interactive",
        help="Do NOT prompt the user for input of any kind.",
    )
    parser.add_argument(
        "--no-post-process",
        action="store_false",
        dest="post_process",
        help="Do NOT post process collected files.",
    )
    parser.add_argument(
        "-i",
        "--ignore",
        action="append",
        default=[],
        dest="ignore_patterns",
        metavar="PATTERN",
        help="Ignore files or directories matching this glob-style "
        "pattern. Use multiple times to ignore more.",
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        help="Do everything except modify the filesystem.",
    )
    parser.add_argument(
        "-c",
        "--clear",
        action="store_true",
        help="Clear the existing files using the storage "
        "before trying to copy or link the original file.",
    )
    parser.add_argument(
        "-l",
        "--link",
        action="store_true",
        help="Create a symbolic link to each file instead of copying.",
    )
    parser.add_argument(
        "--no-default-ignore",
        action="store_false",
        dest="use_default_ignore_patterns",
        help=(
            "Don't ignore the common private glob-style patterns (defaults to "
            "'CVS', '.*' and '*~')."
        ),
    )


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/sessions/middleware.py
# Line: 22

def process_response(self, request, response):
    """
    If request.session was modified, or if the configuration is to save the
    session every time, save the changes and set a session cookie or delete
    the session cookie if the session has been emptied.
    """
    try:
        accessed = request.session.accessed
        modified = request.session.modified
        empty = request.session.is_empty()
    except AttributeError:
        return response
    # First check if we need to delete this cookie.
    # The session should be deleted only if the session is entirely empty.
    if settings.SESSION_COOKIE_NAME in request.COOKIES and empty:
        response.delete_cookie(
            settings.SESSION_COOKIE_NAME,
            path=settings.SESSION_COOKIE_PATH,
            domain=settings.SESSION_COOKIE_DOMAIN,
            samesite=settings.SESSION_COOKIE_SAMESITE,
        )
        patch_vary_headers(response, ("Cookie",))
    else:
        if accessed:
            patch_vary_headers(response, ("Cookie",))
        if (modified or settings.SESSION_SAVE_EVERY_REQUEST) and not empty:
            if request.session.get_expire_at_browser_close():
                max_age = None
                expires = None
            else:
                max_age = request.session.get_expiry_age()
                expires_time = time.time() + max_age
                expires = http_date(expires_time)
            # Save the session data and refresh the client cookie.
            # Skip session save for 5xx responses.
            if response.status_code < 500:
                try:
                    request.session.save()
                except UpdateError:
                    raise SessionInterrupted(
                        "The request's session was deleted before the "
                        "request completed. The user may have logged "
                        "out in a concurrent request, for example."
                    )
                response.set_cookie(
                    settings.SESSION_COOKIE_NAME,
                    request.session.session_key,
                    max_age=max_age,
                    expires=expires,
                    domain=settings.SESSION_COOKIE_DOMAIN,
                    path=settings.SESSION_COOKIE_PATH,
                    secure=settings.SESSION_COOKIE_SECURE or None,
                    httponly=settings.SESSION_COOKIE_HTTPONLY or None,
                    samesite=settings.SESSION_COOKIE_SAMESITE,
                )
    return response

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/sessions/backends/base.py
# Line: 215

def _validate_session_key(self, key):
    """
    Key must be truthy and at least 8 characters long. 8 characters is an
    arbitrary lower bound for some minimal key security.
    """
    return key and len(key) >= 8


# ==================================================
# Line: 265

def get_session_cookie_age(self):
    return settings.SESSION_COOKIE_AGE


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/middleware.py
# Line: 31

def process_request(self, request):
    if not hasattr(request, "session"):
        raise ImproperlyConfigured(
            "The Django authentication middleware requires session "
            "middleware to be installed. Edit your MIDDLEWARE setting to "
            "insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        )
    request.user = SimpleLazyObject(lambda: get_user(request))
    request.auser = partial(auser, request)



# ==================================================
# Line: 62

def get_login_url(self, view_func):
    login_url = getattr(view_func, "login_url", None) or settings.LOGIN_URL
    if not login_url:
        raise ImproperlyConfigured(
            "No login URL to redirect to. Define settings.LOGIN_URL or "
            "provide a login_url via the 'django.contrib.auth.decorators."
            "login_required' decorator."
        )
    return str(login_url)


# ==================================================
# Line: 234

def clean_username(self, username, request):
    """
    Allow the backend to clean the username, if the backend defines a
    clean_username method.
    """
    backend_str = request.session[auth.BACKEND_SESSION_KEY]
    backend = auth.load_backend(backend_str)
    try:
        username = backend.clean_username(username)
    except AttributeError:  # Backend has no clean_username method.
        pass
    return username


# ==================================================
# Line: 247

def _remove_invalid_user(self, request):
    """
    Remove the current authenticated user in the request which is invalid
    but only if the user is authenticated via the RemoteUserBackend.
    """
    try:
        stored_backend = load_backend(
            request.session.get(auth.BACKEND_SESSION_KEY, "")
        )
    except ImportError:
        # backend failed to load
        auth.logout(request)
    else:
        if isinstance(stored_backend, RemoteUserBackend):
            auth.logout(request)


# ==================================================
# Line: 263

async def _aremove_invalid_user(self, request):
    """
    Remove the current authenticated user in the request which is invalid
    but only if the user is authenticated via the RemoteUserBackend.
    """
    try:
        stored_backend = load_backend(
            await request.session.aget(auth.BACKEND_SESSION_KEY, "")
        )
    except ImportError:
        # Backend failed to load.
        await auth.alogout(request)
    else:
        if isinstance(stored_backend, RemoteUserBackend):
            await auth.alogout(request)



# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/forms.py
# Line: 391

def send_mail(
    self,
    subject_template_name,
    email_template_name,
    context,
    from_email,
    to_email,
    html_email_template_name=None,

# ==================================================
# Line: 420

def get_users(self, email):
    """Given an email, return matching user(s) who should receive a reset.

    This allows subclasses to more easily customize the default policies
    that prevent inactive users and users with unusable passwords from
    resetting their password.
    """
    email_field_name = UserModel.get_email_field_name()
    active_users = UserModel._default_manager.filter(
        **{
            "%s__iexact" % email_field_name: email,
            "is_active": True,
        }
    )
    return (
        u
        for u in active_users
        if u.has_usable_password()
        and _unicode_ci_compare(email, getattr(u, email_field_name))
    )


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/tokens.py
# Line: 98

def _make_hash_value(self, user, timestamp):
    """
    Hash the user's primary key, email (if available), and some user state
    that's sure to change after a password reset to produce a token that is
    invalidated when it's used:
    1. The password field will change upon a password reset (even if the
       same password is chosen, due to password salting).
    2. The last_login field will usually be updated very shortly after
       a password reset.
    Failing those things, settings.PASSWORD_RESET_TIMEOUT eventually
    invalidates the token.

    Running this data through salted_hmac() prevents password cracking
    attempts using the reset token, provided the secret isn't compromised.
    """
    # Truncate microseconds so that tokens are consistent even if the
    # database doesn't support microseconds.
    login_timestamp = (
        ""
        if user.last_login is None
        else user.last_login.replace(microsecond=0, tzinfo=None)
    )
    email_field = user.get_email_field_name()
    email = getattr(user, email_field, "") or ""
    return f"{user.pk}{user.password}{login_timestamp}{timestamp}{email}"


# ==================================================
# Occurrences: Lines 124-127 (2 instances)

def _num_seconds(self, dt):
    return int((dt - datetime(2001, 1, 1)).total_seconds())


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/views.py
# Line: 300

def get_user(self, uidb64):
    try:
        # urlsafe_base64_decode() decodes to bytestring
        uid = urlsafe_base64_decode(uidb64).decode()
        pk = UserModel._meta.pk.to_python(uid)
        user = UserModel._default_manager.get(pk=pk)
    except (
        TypeError,
        ValueError,
        OverflowError,
        UserModel.DoesNotExist,
        ValidationError,
    ):
        user = None
    return user


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/backends.py
# Line: 11

def authenticate(self, request, **kwargs):
    return None


# ==================================================
# Line: 17

def get_user(self, user_id):
    return None


# ==================================================
# Line: 23

def get_user_permissions(self, user_obj, obj=None):
    return set()


# ==================================================
# Line: 29

def get_group_permissions(self, user_obj, obj=None):
    return set()


# ==================================================
# Line: 91

def user_can_authenticate(self, user):
    """
    Reject users with is_active=False. Custom user models that don't have
    that attribute are allowed.
    """
    return getattr(user, "is_active", True)


# ==================================================
# Occurrences: Lines 98-101 (2 instances)

def _get_user_permissions(self, user_obj):
    return user_obj.user_permissions.all()


# ==================================================
# Line: 195

def with_perm(self, perm, is_active=True, include_superusers=True, obj=None):
    """
    Return users that have permission "perm". By default, filter out
    inactive users and include superusers.
    """
    if isinstance(perm, str):
        try:
            app_label, codename = perm.split(".")
        except ValueError:
            raise ValueError(
                "Permission name should be in the form "
                "app_label.permission_codename."
            )
    elif not isinstance(perm, Permission):
        raise TypeError(
            "The `perm` argument must be a string or a permission instance."
        )

    if obj is not None:
        return UserModel._default_manager.none()

    permission_q = Q(group__user=OuterRef("pk")) | Q(user=OuterRef("pk"))
    if isinstance(perm, Permission):
        permission_q &= Q(pk=perm.pk)
    else:
        permission_q &= Q(codename=codename, content_type__app_label=app_label)

    user_q = Exists(Permission.objects.filter(permission_q))
    if include_superusers:
        user_q |= Q(is_superuser=True)
    if is_active is not None:
        user_q &= Q(is_active=is_active)

    return UserModel._default_manager.filter(user_q)


# ==================================================
# Line: 318

def clean_username(self, username):
    """
    Perform any cleaning on the "username" prior to using it to get or
    create the user object.  Return the cleaned username.

    By default, return the username unchanged.
    """
    return username


# ==================================================
# Line: 327

def configure_user(self, request, user, created=True):
    """
    Configure a user and return the updated user.

    By default, return the user unmodified.
    """
    return user


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/hashers.py
# Line: 252

def _check_encode_args(self, password, salt):
    if password is None:
        raise TypeError("password must be provided.")
    if not salt or "$" in salt:
        raise ValueError("salt must be provided and cannot contain $.")


# ==================================================
# Occurrences: Lines 292-295 (2 instances)

def must_update(self, encoded):
    return False


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/management/commands/createsuperuser.py
# Line: 272

def _get_input_message(self, field, default=None):
    return "%s%s%s: " % (
        capfirst(field.verbose_name),
        " (leave blank to use '%s')" % default if default else "",
        (
            " (%s.%s)"
            % (
                field.remote_field.model._meta.object_name,
                (
                    field.m2m_target_field_name()
                    if field.many_to_many
                    else field.remote_field.field_name
                ),
            )
            if field.remote_field
            else ""
        ),
    )


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/management/commands/changepassword.py
# Line: 17

def _get_pass(self, prompt="Password: "):
    p = getpass.getpass(prompt=prompt)
    if not p:
        raise CommandError("aborted")
    return p


# ==================================================
# Line: 23

def add_arguments(self, parser):
    parser.add_argument(
        "username",
        nargs="?",
        help=(
            "Username to change password for; by default, it's the current "
            "username."
        ),
    )
    parser.add_argument(
        "--database",
        default=DEFAULT_DB_ALIAS,
        choices=tuple(connections),
        help='Specifies the database to use. Default is "default".',
    )


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/models.py
# Line: 588

def get_group_permissions(self, obj=None):
    return set()


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/password_validation.py
# Occurrences: Lines 215-218 (2 instances)

def get_error_message(self):
    return _("The password is too similar to the %(verbose_name)s.")


# ==================================================
# Line: 236

def DEFAULT_PASSWORD_LIST_PATH(self):
    return Path(__file__).resolve().parent / "common-passwords.txt.gz"


# ==================================================
# Occurrences: Lines 256-259 (2 instances)

def get_error_message(self):
    return _("This password is too common.")


# ==================================================
# Occurrences: Lines 275-278 (2 instances)

def get_error_message(self):
    return _("This password is entirely numeric.")


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/contenttypes/models.py
# Line: 26

def _get_opts(self, model, for_concrete_model):
    if for_concrete_model:
        model = model._meta.concrete_model
    return model._meta


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/geos/polygon.py
# Line: 95

def _clone(self, g):
    if isinstance(g, GEOM_PTR):
        return capi.geom_clone(g)
    else:
        return capi.geom_clone(g.ptr)


# ==================================================
# Line: 101

def _construct_ring(
    self,
    param,
    msg=(
        "Parameter must be a sequence of LinearRings or objects that can "
        "initialize to LinearRings"
    ),

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/geos/coordseq.py
# Line: 75

def _checkdim(self, dim):
    "Check the given dimension."
    if dim < 0 or dim > 2:
        raise GEOSException('invalid ordinate dimension "%d"' % dim)


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/geos/linestring.py
# Line: 137

def _checkdim(self, dim):
    if dim not in (2, 3):
        raise TypeError("Dimension mismatch.")


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/geos/geometry.py
# Line: 97

def _from_pickle_wkb(self, wkb):
    return wkb_r().read(memoryview(wkb))


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/utils/layermapping.py
# Line: 179

def check_fid_range(self, fid_range):
    "Check the `fid_range` keyword."
    if fid_range:
        if isinstance(fid_range, (tuple, list)):
            return slice(*fid_range)
        elif isinstance(fid_range, slice):
            return fid_range
        else:
            raise TypeError
    else:
        return None


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/backends/oracle/schema.py
# Line: 134

def _create_spatial_index_name(self, model, field):
    # Oracle doesn't allow object names > 30 characters. Use this scheme
    # instead of self._create_index_name() for backwards compatibility.
    return truncate_name(
        "%s_%s_id" % (strip_quotes(model._meta.db_table), field.column), 30
    )


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/backends/oracle/operations.py
# Line: 43

def check_relate_argument(self, arg):
    masks = (
        "TOUCH|OVERLAPBDYDISJOINT|OVERLAPBDYINTERSECT|EQUAL|INSIDE|COVEREDBY|"
        "CONTAINS|COVERS|ANYINTERACT|ON"
    )
    mask_regex = re.compile(r"^(%s)(\+(%s))*$" % (masks, masks), re.I)
    if not isinstance(arg, str) or not mask_regex.match(arg):
        raise ValueError('Invalid SDO_RELATE mask: "%s"' % arg)


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/backends/mysql/schema.py
# Line: 98

def _create_spatial_index_name(self, model, field):
    return "%s_%s_id" % (model._meta.db_table, field.column)


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/backends/base/operations.py
# Line: 94

def geo_quote_name(self, name):
    return "'%s'" % name


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/backends/postgis/operations.py
# Line: 172

def function_names(self):
    function_names = {
        "AsWKB": "ST_AsBinary",
        "AsWKT": "ST_AsText",
        "BoundingCircle": "ST_MinimumBoundingCircle",
        "FromWKB": "ST_GeomFromWKB",
        "FromWKT": "ST_GeomFromText",
        "NumPoints": "ST_NPoints",
    }
    return function_names


# ==================================================
# Line: 391

def parse_raster(self, value):
    """Convert a PostGIS HEX String into a dict readable by GDALRaster."""
    return from_pgraster(value)


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/backends/postgis/base.py
# Line: 38

def dump(self, obj):
    # Return bytes as hex for text formatting
    return obj.ewkb.hex().encode()


# ==================================================
# Line: 45

def dump(self, obj):
    return obj.ewkb


# ==================================================
# Line: 64

def get_key(self, obj, format):
    if obj.is_geometry:
        return GeographyType if obj.geography else GeometryType
    else:
        return RasterType


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/models/functions.py
# Line: 101

def _handle_param(self, value, param_name="", check_types=None):
    if not hasattr(value, "resolve_expression"):
        if check_types and not isinstance(value, check_types):
            raise TypeError(
                "The %s parameter has the wrong type: should be %s."
                % (param_name, check_types)
            )
    return value



# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/models/lookups.py
# Line: 56

def get_db_prep_lookup(self, value, connection):
    # get_db_prep_lookup is called by process_rhs from super class
    return ("%s", [connection.ops.Adapter(value)])


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/models/fields.py
# Line: 170

def get_raster_prep_value(self, value, is_candidate):
    """
    Return a GDALRaster if conversion is successful, otherwise return None.
    """
    if isinstance(value, gdal.GDALRaster):
        return value
    elif is_candidate:
        try:
            return gdal.GDALRaster(value)
        except GDALException:
            pass
    elif isinstance(value, dict):
        try:
            return gdal.GDALRaster(value)
        except GDALException:
            raise ValueError(
                "Couldn't create spatial object from lookup value '%s'." % value
            )


# ==================================================
# Line: 314

def select_format(self, compiler, sql, params):
    """
    Return the selection format string, depending on the requirements
    of the spatial backend. For example, Oracle and MySQL require custom
    selection formats in order to retrieve geometries in OGC WKB.
    """
    if not compiler.query.subquery:
        return compiler.connection.ops.select % sql, params
    return sql, params



# ==================================================
# Occurrences: Lines 380-383 (2 instances)

def get_internal_type(self):
    return "ExtentField"


# ==================================================
# Line: 397

def _check_connection(self, connection):
    # Make sure raster fields are used only on backends with raster support.
    if (
        not connection.features.gis_enabled
        or not connection.features.supports_raster
    ):
        raise ImproperlyConfigured(
            "Raster fields require backends with raster support."
        )


# ==================================================
# Line: 411

def from_db_value(self, value, expression, connection):
    return connection.ops.parse_raster(value)


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/forms/widgets.py
# Occurrences: Lines 33-36 (2 instances)

def serialize(self, value):
    return value.wkt if value else ""


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/sitemaps/kml.py
# Line: 20

def _build_kml_sources(self, sources):
    """
    Go through the given sources and return a 3-tuple of the application
    label, module name, and field name of every GeometryField encountered
    in the sources.

    If no sources are provided, then all models.
    """
    kml_sources = []
    if sources is None:
        sources = apps.get_models()
    for source in sources:
        if isinstance(source, models.base.ModelBase):
            for field in source._meta.fields:
                if isinstance(field, GeometryField):
                    kml_sources.append(
                        (
                            source._meta.app_label,
                            source._meta.model_name,
                            field.name,
                        )
                    )
        elif isinstance(source, (list, tuple)):
            if len(source) != 3:
                raise ValueError(
                    "Must specify a 3-tuple of (app_label, module_name, "
                    "field_name)."
                )
            kml_sources.append(source)
        else:
            raise TypeError("KML Sources must be a model or a 3-tuple.")
    return kml_sources


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/feeds.py
# Line: 11

def georss_coords(self, coords):
    """
    In GeoRSS coordinate pairs are ordered by lat/lon and separated by
    a single white space. Given a tuple of coordinates, return a string
    GeoRSS representation.
    """
    return " ".join("%f %f" % (coord[1], coord[0]) for coord in coords)


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/flatpages/middleware.py
# Line: 8

def process_response(self, request, response):
    if response.status_code != 404:
        return response  # No need to check for a flatpage for non-404 responses.
    try:
        return flatpage(request, request.path_info)
    # Return the original response if any errors happened. Because this
    # is a middleware, we can't assume the errors will be caught elsewhere.
    except Http404:
        return response
    except Exception:
        if settings.DEBUG:
            raise
        return response

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/flatpages/forms.py
# Line: 37

def _trailing_slash_required(self):
    return (
        settings.APPEND_SLASH
        and "django.middleware.common.CommonMiddleware" in settings.MIDDLEWARE
    )


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admindocs/middleware.py
# Line: 14

def process_view(self, request, view_func, view_args, view_kwargs):
    """
    If the request method is HEAD and either the IP is internal or the
    user is a logged-in staff member, return a response with an x-view
    header indicating the view function. This is used to lookup the view
    function for an arbitrary page.
    """
    if not hasattr(request, "user"):
        raise ImproperlyConfigured(
            "The XView middleware requires authentication middleware to "
            "be installed. Edit your MIDDLEWARE setting to insert "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        )
    if request.method == "HEAD" and (
        request.META.get("REMOTE_ADDR") in settings.INTERNAL_IPS
        or (request.user.is_active and request.user.is_staff)
    ):
        response = HttpResponse()
        response.headers["X-View"] = get_view_name(view_func)
        return response

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/sites/middleware.py
# Line: 11

def process_request(self, request):
    request.site = get_current_site(request)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/sites/models.py
# Line: 70

def clear_cache(self):
    """Clear the ``Site`` object cache."""
    global SITE_CACHE
    SITE_CACHE = {}


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/messages/middleware.py
# Occurrences: Lines 11-14 (2 instances)

def process_request(self, request):
    request._messages = default_storage(request)


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/messages/storage/cookie.py
# Line: 51

def dumps(self, obj):
    return [
        json.dumps(
            o,
            separators=(",", ":"),
            cls=MessageEncoder,
        )
        for o in obj
    ]



# ==================================================
# Line: 63

def dumps(self, obj):
    """
    The parameter is an already serialized list of Message objects. No need
    to serialize it again, only join the list together and encode it.
    """
    return ("[" + ",".join(obj) + "]").encode("latin-1")



# ==================================================
# Line: 72

def loads(self, data):
    return json.loads(data.decode("latin-1"), cls=MessageDecoder)



# ==================================================
# File: /root/ecooptimizer/django/django/contrib/messages/storage/base.py
# Line: 121

def _prepare_messages(self, messages):
    """
    Prepare a list of messages for storage.
    """
    for message in messages:
        message._prepare()


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/messages/storage/session.py
# Occurrences: Lines 45-49 (2 instances)

def serialize_messages(self, messages):
    encoder = MessageEncoder()
    return encoder.encode(messages)


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/sitemaps/__init__.py
# Occurrences: Lines 75-78 (2 instances)

def items(self):
    return []


# ==================================================
# Line: 85

def get_domain(self, site=None):
    # Determine domain
    if site is None:
        if django_apps.is_installed("django.contrib.sites"):
            Site = django_apps.get_model("sites.Site")
            try:
                site = Site.objects.get_current()
            except Site.DoesNotExist:
                pass
        if site is None:
            raise ImproperlyConfigured(
                "To use sitemaps, either enable the sites framework or pass "
                "a Site/RequestSite object in your view."
            )
    return site.domain


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/postgres/operations.py
# Line: 55

def extension_exists(self, schema_editor, extension):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(
            "SELECT 1 FROM pg_extension WHERE extname = %s",
            [extension],
        )
        return bool(cursor.fetchone())


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/postgres/fields/array.py
# Line: 233

def slice_expression(self, expression, start, length):
    # If length is not provided, don't specify an end to slice to the end
    # of the array.
    end = None if length is None else start + length - 1
    return SliceTransform(start, end, expression)



# ==================================================
# File: /root/ecooptimizer/django/django/contrib/postgres/fields/ranges.py
# Line: 172

def db_type(self, connection):
    return "int4range"



# ==================================================
# Line: 181

def db_type(self, connection):
    return "int8range"



# ==================================================
# Line: 190

def db_type(self, connection):
    return "numrange"



# ==================================================
# Line: 199

def db_type(self, connection):
    return "tstzrange"



# ==================================================
# Line: 208

def db_type(self, connection):
    return "daterange"



# ==================================================
# File: /root/ecooptimizer/django/django/contrib/postgres/forms/array.py
# Line: 140

def id_for_label(self, id_):
    # See the comment for RadioSelect.id_for_label()
    if id_:
        id_ += "_0"
    return id_


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/postgres/indexes.py
# Line: 40

def get_with_params(self):
    return []



# ==================================================
# File: /root/ecooptimizer/django/django/contrib/syndication/views.py
# Occurrences: Lines 51-58 (3 instances)

def item_title(self, item):
    # Titles should be double escaped by default (see #6533)
    return escape(str(item))


# ==================================================
# Line: 108

def feed_extra_kwargs(self, obj):
    """
    Return an extra keyword arguments dictionary that is used when
    initializing the feed generator.
    """
    return {}


# ==================================================
# Line: 115

def item_extra_kwargs(self, item):
    """
    Return an extra keyword arguments dictionary that is used with
    the `add_item` call of the feed generator.
    """
    return {}


# ==================================================
# Occurrences: Lines 122-125 (2 instances)

def get_object(self, request, *args, **kwargs):
    return None


# ==================================================
# File: /root/ecooptimizer/django/django/dispatch/dispatcher.py
# Line: 276

def _log_robust_failure(self, receiver, err):
    logger.error(
        "Error calling %s in Signal.send_robust() (%s)",
        receiver.__qualname__,
        err,
        exc_info=err,
    )


# ==================================================
# File: /root/ecooptimizer/django/django/core/files/storage/filesystem.py
# Line: 213

def _datetime_from_timestamp(self, ts):
    """
    If timezone support is enabled, make an aware datetime object in UTC;
    otherwise make a naive one in the local timezone.
    """
    tz = UTC if settings.USE_TZ else None
    return datetime.fromtimestamp(ts, tz=tz)


# ==================================================
# File: /root/ecooptimizer/django/django/core/files/storage/base.py
# Line: 60

def get_valid_name(self, name):
    """
    Return a filename, based on the provided filename, that's suitable for
    use in the target storage system.
    """
    return get_valid_filename(name)


# ==================================================
# Line: 67

def get_alternative_name(self, file_root, file_ext):
    """
    Return an alternative filename, by adding an underscore and a random 7
    character alphanumeric string (before the file extension, if one
    exists) to the filename.
    """
    return "%s_%s%s" % (file_root, get_random_string(7), file_ext)


# ==================================================
# File: /root/ecooptimizer/django/django/core/files/storage/mixins.py
# Line: 14

def _value_or_setting(self, value, setting):
    return setting if value is None else value

# ==================================================
# File: /root/ecooptimizer/django/django/core/files/storage/handler.py
# Line: 38

def create_storage(self, params):
    params = params.copy()
    backend = params.pop("BACKEND")
    options = params.pop("OPTIONS", {})
    try:
        storage_cls = import_string(backend)
    except ImportError as e:
        raise InvalidStorageError(f"Could not find backend {backend!r}: {e}") from e
    return storage_cls(**options)

# ==================================================
# File: /root/ecooptimizer/django/django/core/signing.py
# Occurrences: Lines 124-127 (2 instances)

def dumps(self, obj):
    return json.dumps(obj, separators=(",", ":")).encode("latin-1")


# ==================================================
# Line: 255

def timestamp(self):
    return b62_encode(int(time.time()))


# ==================================================
# File: /root/ecooptimizer/django/django/core/cache/backends/base.py
# Line: 112

def validate_key(self, key):
    """
    Warn about keys that would not be portable to the memcached
    backend. This encourages (but does not force) writing backend-portable
    cache code.
    """
    for warning in memcache_key_warnings(key):
        warnings.warn(warning, CacheKeyWarning)


# ==================================================
# File: /root/ecooptimizer/django/django/core/cache/backends/redis.py
# Line: 24

def loads(self, data):
    try:
        return int(data)
    except ValueError:
        return pickle.loads(data)



# ==================================================
# File: /root/ecooptimizer/django/django/core/cache/backends/memcached.py
# Line: 139

def validate_key(self, key):
    for warning in memcache_key_warnings(key):
        raise InvalidCacheKey(warning)



# ==================================================
# File: /root/ecooptimizer/django/django/core/serializers/xml_serializer.py
# Line: 206

def _make_parser(self):
    """Create a hardened XML parser (no custom/external entities)."""
    return DefusedExpatParser()


# ==================================================
# Line: 375

def _get_model_from_node(self, node, attr):
    """
    Look up a model from a <object model=...> or a <field rel=... to=...>
    node.
    """
    model_identifier = node.getAttribute(attr)
    if not model_identifier:
        raise base.DeserializationError(
            "<%s> node is missing the required '%s' attribute"
            % (node.nodeName, attr)
        )
    try:
        return apps.get_model(model_identifier)
    except (LookupError, TypeError):
        raise base.DeserializationError(
            "<%s> node has invalid model identifier: '%s'"
            % (node.nodeName, model_identifier)
        )



# ==================================================
# Line: 430

def entity_decl(
    self, name, is_parameter_entity, value, base, sysid, pubid, notation_name

# ==================================================
# Line: 439

def external_entity_ref_handler(self, context, base, sysid, pubid):
    raise ExternalReferenceForbidden(context, base, sysid, pubid)


# ==================================================
# File: /root/ecooptimizer/django/django/core/handlers/base.py
# Line: 104

def adapt_method_mode(
    self,
    is_async,
    method,
    method_is_async=None,
    debug=False,
    name=None,

# ==================================================
# Line: 300

def resolve_request(self, request):
    """
    Retrieve/set the urlconf for the request. Return the view resolved,
    with its args and kwargs.
    """
    # Work out the resolver.
    if hasattr(request, "urlconf"):
        urlconf = request.urlconf
        set_urlconf(urlconf)
        resolver = get_resolver(urlconf)
    else:
        resolver = get_resolver()
    # Resolve the view, and assign the match object back to the request.
    resolver_match = resolver.resolve(request.path_info)
    request.resolver_match = resolver_match
    return resolver_match


# ==================================================
# Line: 317

def check_response(self, response, callback, name=None):
    """
    Raise an error if the view returned None or an uncalled coroutine.
    """
    if not (response is None or asyncio.iscoroutine(response)):
        return
    if not name:
        if isinstance(callback, types.FunctionType):  # FBV
            name = "The view %s.%s" % (callback.__module__, callback.__name__)
        else:  # CBV
            name = "The view %s.%s.__call__" % (
                callback.__module__,
                callback.__class__.__name__,
            )
    if response is None:
        raise ValueError(
            "%s didn't return an HttpResponse object. It returned None "
            "instead." % name
        )
    elif asyncio.iscoroutine(response):
        raise ValueError(
            "%s didn't return an HttpResponse object. It returned an "
            "unawaited coroutine instead. You may need to add an 'await' "
            "into your view." % name
        )


# ==================================================
# Line: 345

def make_view_atomic(self, view):
    non_atomic_requests = getattr(view, "_non_atomic_requests", set())
    for alias, settings_dict in connections.settings.items():
        if settings_dict["ATOMIC_REQUESTS"] and alias not in non_atomic_requests:
            if iscoroutinefunction(view):
                raise RuntimeError(
                    "You cannot use ATOMIC_REQUESTS with async views."
                )
            view = transaction.atomic(using=alias)(view)
    return view


# ==================================================
# File: /root/ecooptimizer/django/django/core/handlers/asgi.py
# Line: 233

async def listen_for_disconnect(self, receive):
    """Listen for disconnect from the client."""
    message = await receive()
    if message["type"] == "http.disconnect":
        raise RequestAborted()
    # This should never happen.
    assert False, "Invalid ASGI message after request body: %s" % message["type"]


# ==================================================
# Line: 252

async def read_body(self, receive):
    """Reads an HTTP body from an ASGI connection."""
    # Use the tempfile that auto rolls-over to a disk file as it fills up.
    body_file = tempfile.SpooledTemporaryFile(
        max_size=settings.FILE_UPLOAD_MAX_MEMORY_SIZE, mode="w+b"
    )
    while True:
        message = await receive()
        if message["type"] == "http.disconnect":
            body_file.close()
            # Early client disconnect.
            raise RequestAborted()
        # Add a body chunk from the message, if provided.
        if "body" in message:
            on_disk = getattr(body_file, "_rolled", False)
            if on_disk:
                async_write = sync_to_async(
                    body_file.write,
                    thread_sensitive=False,
                )
                await async_write(message["body"])
            else:
                body_file.write(message["body"])

        # Quit out if that's the end.
        if not message.get("more_body", False):
            break
    body_file.seek(0)
    return body_file


# ==================================================
# File: /root/ecooptimizer/django/django/core/paginator.py
# Line: 130

def _get_page(self, *args, **kwargs):
    """
    Return an instance of a single page.

    This hook can be used by subclasses to use an alternative to the
    standard :cls:`Page` object.
    """
    return Page(*args, **kwargs)


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/showmigrations.py
# Line: 13

def add_arguments(self, parser):
    parser.add_argument(
        "app_label",
        nargs="*",
        help="App labels of applications to limit the output to.",
    )
    parser.add_argument(
        "--database",
        default=DEFAULT_DB_ALIAS,
        choices=tuple(connections),
        help=(
            "Nominates a database to show migrations for. Defaults to the "
            '"default" database.'
        ),
    )

    formats = parser.add_mutually_exclusive_group()
    formats.add_argument(
        "--list",
        "-l",
        action="store_const",
        dest="format",
        const="list",
        help=(
            "Shows a list of all migrations and which are applied. "
            "With a verbosity level of 2 or above, the applied datetimes "
            "will be included."
        ),
    )
    formats.add_argument(
        "--plan",
        "-p",
        action="store_const",
        dest="format",
        const="plan",
        help=(
            "Shows all migrations in the order they will be applied. With a "
            "verbosity level of 2 or above all direct migration dependencies and "
            "reverse dependencies (run_before) will be included."
        ),
    )

    parser.set_defaults(format="list")


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/diffsettings.py
# Line: 15

def add_arguments(self, parser):
    parser.add_argument(
        "--all",
        action="store_true",
        help=(
            'Display all settings, regardless of their value. In "hash" '
            'mode, default values are prefixed by "###".'
        ),
    )
    parser.add_argument(
        "--default",
        metavar="MODULE",
        help=(
            "The settings module to compare the current settings against. Leave "
            "empty to compare against Django's default settings."
        ),
    )
    parser.add_argument(
        "--output",
        default="hash",
        choices=("hash", "unified"),
        help=(
            "Selects the output format. 'hash' mode displays each changed "
            "setting, with the settings that don't appear in the defaults "
            "followed by ###. 'unified' mode prefixes the default setting "
            "with a minus sign, followed by the changed setting prefixed "
            "with a plus sign."
        ),
    )


# ==================================================
# Line: 63

def output_hash(self, user_settings, default_settings, **options):
    # Inspired by Postfix's "postconf -n".
    output = []
    for key in sorted(user_settings):
        if key not in default_settings:
            output.append("%s = %s  ###" % (key, user_settings[key]))
        elif user_settings[key] != default_settings[key]:
            output.append("%s = %s" % (key, user_settings[key]))
        elif options["all"]:
            output.append("### %s = %s" % (key, user_settings[key]))
    return output


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/makemessages.py
# Line: 466

def gettext_version(self):
    # Gettext tools will output system-encoded bytestrings instead of UTF-8,
    # when looking up the version. It's especially a problem on Windows.
    out, err, status = popen_wrapper(
        ["xgettext", "--version"],
        stdout_encoding=DEFAULT_LOCALE_ENCODING,
    )
    m = re.search(r"(\d+)\.(\d+)\.?(\d+)?", out)
    if m:
        return tuple(int(d) for d in m.groups() if d is not None)
    else:
        raise CommandError("Unable to get gettext version. Is it installed?")


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/testserver.py
# Line: 11

def add_arguments(self, parser):
    parser.add_argument(
        "args",
        metavar="fixture",
        nargs="*",
        help="Path(s) to fixtures to load before running the server.",
    )
    parser.add_argument(
        "--noinput",
        "--no-input",
        action="store_false",
        dest="interactive",
        help="Tells Django to NOT prompt the user for input of any kind.",
    )
    parser.add_argument(
        "--addrport",
        default="",
        help="Port number or ipaddr:port to run the server on.",
    )
    parser.add_argument(
        "--ipv6",
        "-6",
        action="store_true",
        dest="use_ipv6",
        help="Tells Django to use an IPv6 address.",
    )


# ==================================================
# Line: 38

def handle(self, *fixture_labels, **options):
    verbosity = options["verbosity"]
    interactive = options["interactive"]

    # Create a test database.
    db_name = connection.creation.create_test_db(
        verbosity=verbosity, autoclobber=not interactive
    )

    # Import the fixture data into the test database.
    call_command("loaddata", *fixture_labels, verbosity=verbosity)

    # Run the development server. Turn off auto-reloading because it causes
    # a strange error -- it causes this handle() method to be called
    # multiple times.
    shutdown_message = (
        "\nServer stopped.\nNote that the test database, %r, has not been "
        "deleted. You can explore it on your own." % db_name
    )
    use_threading = connection.features.test_db_allows_multiple_connections
    call_command(
        "runserver",
        addrport=options["addrport"],
        shutdown_message=shutdown_message,
        use_reloader=False,
        use_ipv6=options["use_ipv6"],
        use_threading=use_threading,
    )

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/runserver.py
# Line: 39

def add_arguments(self, parser):
    parser.add_argument(
        "addrport", nargs="?", help="Optional port number, or ipaddr:port"
    )
    parser.add_argument(
        "--ipv6",
        "-6",
        action="store_true",
        dest="use_ipv6",
        help="Tells Django to use an IPv6 address.",
    )
    parser.add_argument(
        "--nothreading",
        action="store_false",
        dest="use_threading",
        help="Tells Django to NOT use threading.",
    )
    parser.add_argument(
        "--noreload",
        action="store_false",
        dest="use_reloader",
        help="Tells Django to NOT use the auto-reloader.",
    )


# ==================================================
# Occurrences: Lines 71-75 (2 instances)

def get_handler(self, *args, **options):
    """Return the default WSGI handler for the runner."""
    return get_internal_wsgi_application()


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/sendtestemail.py
# Line: 15

def add_arguments(self, parser):
    parser.add_argument(
        "email",
        nargs="*",
        help="One or more email addresses to send a test email to.",
    )
    parser.add_argument(
        "--managers",
        action="store_true",
        help="Send a test email to the addresses specified in settings.MANAGERS.",
    )
    parser.add_argument(
        "--admins",
        action="store_true",
        help="Send a test email to the addresses specified in settings.ADMINS.",
    )


# ==================================================
# Line: 32

def handle(self, *args, **kwargs):
    subject = "Test email from %s on %s" % (socket.gethostname(), timezone.now())

    send_mail(
        subject=subject,
        message="If you're reading this, it was successful.",
        from_email=None,
        recipient_list=kwargs["email"],
    )

    if kwargs["managers"]:
        mail_managers(subject, "This email was sent to the site managers.")

    if kwargs["admins"]:
        mail_admins(subject, "This email was sent to the site admins.")

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/squashmigrations.py
# Line: 21

def add_arguments(self, parser):
    parser.add_argument(
        "app_label",
        help="App label of the application to squash migrations for.",
    )
    parser.add_argument(
        "start_migration_name",
        nargs="?",
        help=(
            "Migrations will be squashed starting from and including this "
            "migration."
        ),
    )
    parser.add_argument(
        "migration_name",
        help="Migrations will be squashed until and including this migration.",
    )
    parser.add_argument(
        "--no-optimize",
        action="store_true",
        help="Do not try to optimize the squashed operations.",
    )
    parser.add_argument(
        "--noinput",
        "--no-input",
        action="store_false",
        dest="interactive",
        help="Tells Django to NOT prompt the user for input of any kind.",
    )
    parser.add_argument(
        "--squashed-name",
        help="Sets the name of the new squashed migration.",
    )
    parser.add_argument(
        "--no-header",
        action="store_false",
        dest="include_header",
        help="Do not add a header comment to the new squashed migration.",
    )


# ==================================================
# Line: 241

def find_migration(self, loader, app_label, name):
    try:
        return loader.get_migration_by_prefix(app_label, name)
    except AmbiguityError:
        raise CommandError(
            "More than one migration matches '%s' in app '%s'. Please be "
            "more specific." % (name, app_label)
        )
    except KeyError:
        raise CommandError(
            "Cannot find a migration matching '%s' from app '%s'."
            % (name, app_label)
        )

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/migrate.py
# Line: 23

def add_arguments(self, parser):
    parser.add_argument(
        "app_label",
        nargs="?",
        help="App label of an application to synchronize the state.",
    )
    parser.add_argument(
        "migration_name",
        nargs="?",
        help="Database state will be brought to the state after that "
        'migration. Use the name "zero" to unapply all migrations.',
    )
    parser.add_argument(
        "--noinput",
        "--no-input",
        action="store_false",
        dest="interactive",
        help="Tells Django to NOT prompt the user for input of any kind.",
    )
    parser.add_argument(
        "--database",
        default=DEFAULT_DB_ALIAS,
        choices=tuple(connections),
        help=(
            'Nominates a database to synchronize. Defaults to the "default" '
            "database."
        ),
    )
    parser.add_argument(
        "--fake",
        action="store_true",
        help="Mark migrations as run without actually running them.",
    )
    parser.add_argument(
        "--fake-initial",
        action="store_true",
        help=(
            "Detect if tables already exist and fake-apply initial migrations if "
            "so. Make sure that the current database schema matches your initial "
            "migration before using this flag. Django will only check for an "
            "existing table name."
        ),
    )
    parser.add_argument(
        "--plan",
        action="store_true",
        help="Shows a list of the migration actions that will be performed.",
    )
    parser.add_argument(
        "--run-syncdb",
        action="store_true",
        help="Creates tables for apps without migrations.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        dest="check_unapplied",
        help=(
            "Exits with a non-zero status if unapplied migrations exist and does "
            "not actually apply migrations."
        ),
    )
    parser.add_argument(
        "--prune",
        action="store_true",
        dest="prune",
        help="Delete nonexistent migrations from the django_migrations table.",
    )


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/createcachetable.py
# Line: 20

def add_arguments(self, parser):
    parser.add_argument(
        "args",
        metavar="table_name",
        nargs="*",
        help=(
            "Optional table names. Otherwise, settings.CACHES is used to find "
            "cache tables."
        ),
    )
    parser.add_argument(
        "--database",
        default=DEFAULT_DB_ALIAS,
        choices=tuple(connections),
        help="Nominates a database onto which the cache tables will be "
        'installed. Defaults to the "default" database.',
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Does not create the table, just prints the SQL that would be run.",
    )


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/optimizemigration.py
# Line: 18

def add_arguments(self, parser):
    parser.add_argument(
        "app_label",
        help="App label of the application to optimize the migration for.",
    )
    parser.add_argument(
        "migration_name", help="Migration name to optimize the operations for."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit with a non-zero status if the migration can be optimized.",
    )


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/loaddata.py
# Line: 51

def add_arguments(self, parser):
    parser.add_argument(
        "args", metavar="fixture", nargs="+", help="Fixture labels."
    )
    parser.add_argument(
        "--database",
        default=DEFAULT_DB_ALIAS,
        choices=tuple(connections),
        help=(
            "Nominates a specific database to load fixtures into. Defaults to the "
            '"default" database.'
        ),
    )
    parser.add_argument(
        "--app",
        dest="app_label",
        help="Only look for fixtures in the specified app.",
    )
    parser.add_argument(
        "--ignorenonexistent",
        "-i",
        action="store_true",
        dest="ignore",
        help="Ignores entries in the serialized data for fields that do not "
        "currently exist on the model.",
    )
    parser.add_argument(
        "-e",
        "--exclude",
        action="append",
        default=[],
        help=(
            "An app_label or app_label.ModelName to exclude. Can be used multiple "
            "times."
        ),
    )
    parser.add_argument(
        "--format",
        help="Format of serialized data when reading from stdin.",
    )


# ==================================================
# Line: 113

def compression_formats(self):
    """A dict mapping format names to (open function, mode arg) tuples."""
    # Forcing binary mode may be revisited after dropping Python 2 support
    # (see #22399).
    compression_formats = {
        None: (open, "rb"),
        "gz": (gzip.GzipFile, "rb"),
        "zip": (SingleZipReader, "r"),
        "stdin": (lambda *args: sys.stdin, None),
    }
    if has_bz2:
        compression_formats["bz2"] = (bz2.BZ2File, "r")
    if has_lzma:
        compression_formats["lzma"] = (lzma.LZMAFile, "r")
        compression_formats["xz"] = (lzma.LZMAFile, "r")
    return compression_formats


# ==================================================
# Line: 305

def find_fixture_files_in_dir(self, fixture_dir, fixture_name, targets):
    fixture_files_in_dir = []
    path = os.path.join(fixture_dir, fixture_name)
    for candidate in glob.iglob(glob.escape(path) + "*"):
        if os.path.basename(candidate) in targets:
            # Save the fixture_dir and fixture_name for future error
            # messages.
            fixture_files_in_dir.append((candidate, fixture_dir, fixture_name))
    return fixture_files_in_dir


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/test.py
# Line: 54

def handle(self, *test_labels, **options):
    TestRunner = get_runner(settings, options["testrunner"])

    time_keeper = TimeKeeper() if options.get("timing", False) else NullTimeKeeper()
    parallel = options.get("parallel")
    if parallel == "auto":
        options["parallel"] = get_max_test_processes()
    test_runner = TestRunner(**options)
    with time_keeper.timed("Total run"):
        failures = test_runner.run_tests(test_labels)
    time_keeper.print_results()
    if failures:
        sys.exit(1)

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/inspectdb.py
# Line: 18

def add_arguments(self, parser):
    parser.add_argument(
        "table",
        nargs="*",
        type=str,
        help="Selects what tables or views should be introspected.",
    )
    parser.add_argument(
        "--database",
        default=DEFAULT_DB_ALIAS,
        choices=tuple(connections),
        help=(
            'Nominates a database to introspect. Defaults to using the "default" '
            "database."
        ),
    )
    parser.add_argument(
        "--include-partitions",
        action="store_true",
        help="Also output models for partition tables.",
    )
    parser.add_argument(
        "--include-views",
        action="store_true",
        help="Also output models for database views.",
    )


# ==================================================
# Line: 265

def normalize_col_name(self, col_name, used_column_names, is_relation):
    """
    Modify the column name to make it Python-compatible as a field name
    """
    field_params = {}
    field_notes = []

    new_name = col_name.lower()
    if new_name != col_name:
        field_notes.append("Field name made lowercase.")

    if is_relation:
        if new_name.endswith("_id"):
            new_name = new_name.removesuffix("_id")
        else:
            field_params["db_column"] = col_name

    new_name, num_repl = re.subn(r"\W", "_", new_name)
    if num_repl > 0:
        field_notes.append("Field renamed to remove unsuitable characters.")

    if new_name.find(LOOKUP_SEP) >= 0:
        while new_name.find(LOOKUP_SEP) >= 0:
            new_name = new_name.replace(LOOKUP_SEP, "_")
        if col_name.lower().find(LOOKUP_SEP) >= 0:
            # Only add the comment if the double underscore was in the original name
            field_notes.append(
                "Field renamed because it contained more than one '_' in a row."
            )

    if new_name.startswith("_"):
        new_name = "field%s" % new_name
        field_notes.append("Field renamed because it started with '_'.")

    if new_name.endswith("_"):
        new_name = "%sfield" % new_name
        field_notes.append("Field renamed because it ended with '_'.")

    if keyword.iskeyword(new_name):
        new_name += "_field"
        field_notes.append("Field renamed because it was a Python reserved word.")

    if new_name[0].isdigit():
        new_name = "number_%s" % new_name
        field_notes.append(
            "Field renamed because it wasn't a valid Python identifier."
        )

    if new_name in used_column_names:
        num = 0
        while "%s_%d" % (new_name, num) in used_column_names:
            num += 1
        new_name = "%s_%d" % (new_name, num)
        field_notes.append("Field renamed because of name conflict.")

    if col_name != new_name and field_notes:
        field_params["db_column"] = col_name

    return new_name, field_params, field_notes


# ==================================================
# Occurrences: Lines 325-329 (2 instances)

def normalize_table_name(self, table_name):
    """Translate the table name to a Python-compatible model name."""
    return re.sub(r"[^a-zA-Z0-9]", "", table_name.title())


# ==================================================
# Line: 370

def get_meta(
    self,
    table_name,
    constraints,
    column_to_field_name,
    is_view,
    is_partition,
    comment,

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/makemigrations.py
# Line: 30

def add_arguments(self, parser):
    parser.add_argument(
        "args",
        metavar="app_label",
        nargs="*",
        help="Specify the app label(s) to create migrations for.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Just show what migrations would be made; don't actually write them.",
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="Enable fixing of migration conflicts.",
    )
    parser.add_argument(
        "--empty",
        action="store_true",
        help="Create an empty migration.",
    )
    parser.add_argument(
        "--noinput",
        "--no-input",
        action="store_false",
        dest="interactive",
        help="Tells Django to NOT prompt the user for input of any kind.",
    )
    parser.add_argument(
        "-n",
        "--name",
        help="Use this name for migration file(s).",
    )
    parser.add_argument(
        "--no-header",
        action="store_false",
        dest="include_header",
        help="Do not add header comments to new migration file(s).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        dest="check_changes",
        help=(
            "Exit with a non-zero status if model changes are missing migrations "
            "and don't actually write them. Implies --dry-run."
        ),
    )
    parser.add_argument(
        "--scriptable",
        action="store_true",
        dest="scriptable",
        help=(
            "Divert log output and input prompts to stderr, writing only "
            "paths of generated migration files to stdout."
        ),
    )
    parser.add_argument(
        "--update",
        action="store_true",
        dest="update",
        help=(
            "Merge model changes into the latest migration and optimize the "
            "resulting operations."
        ),
    )


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/flush.py
# Line: 17

def add_arguments(self, parser):
    parser.add_argument(
        "--noinput",
        "--no-input",
        action="store_false",
        dest="interactive",
        help="Tells Django to NOT prompt the user for input of any kind.",
    )
    parser.add_argument(
        "--database",
        default=DEFAULT_DB_ALIAS,
        choices=tuple(connections),
        help='Nominates a database to flush. Defaults to the "default" database.',
    )


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/check.py
# Line: 13

def add_arguments(self, parser):
    parser.add_argument("args", metavar="app_label", nargs="*")
    parser.add_argument(
        "--tag",
        "-t",
        action="append",
        dest="tags",
        help="Run only checks labeled with given tag.",
    )
    parser.add_argument(
        "--list-tags",
        action="store_true",
        help=(
            "List available tags. Specify --deploy to include available deployment "
            "tags."
        ),
    )
    parser.add_argument(
        "--deploy",
        action="store_true",
        help="Check deployment settings.",
    )
    parser.add_argument(
        "--fail-level",
        default="ERROR",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"],
        help=(
            "Message level that will cause the command to exit with a "
            "non-zero status. Default is ERROR."
        ),
    )
    parser.add_argument(
        "--database",
        action="append",
        choices=tuple(connections),
        dest="databases",
        help="Run database related checks against these aliases.",
    )


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/sqlmigrate.py
# Line: 12

def add_arguments(self, parser):
    parser.add_argument(
        "app_label", help="App label of the application containing the migration."
    )
    parser.add_argument(
        "migration_name", help="Migration name to print the SQL for."
    )
    parser.add_argument(
        "--database",
        default=DEFAULT_DB_ALIAS,
        choices=tuple(connections),
        help=(
            'Nominates a database to create SQL for. Defaults to the "default" '
            "database."
        ),
    )
    parser.add_argument(
        "--backwards",
        action="store_true",
        help="Creates SQL to unapply the migration, rather than to apply it",
    )


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/shell.py
# Line: 124

def get_auto_imports(self):
    """Return a sequence of import paths for objects to be auto-imported.

    By default, import paths for models in INSTALLED_APPS are included,
    with models from earlier apps taking precedence in case of a name
    collision.

    For example, for an unchanged INSTALLED_APPS, this method returns:

    [
        "django.contrib.sessions.models.Session",
        "django.contrib.contenttypes.models.ContentType",
        "django.contrib.auth.models.User",
        "django.contrib.auth.models.Group",
        "django.contrib.auth.models.Permission",
        "django.contrib.admin.models.LogEntry",
    ]

    """
    app_models_imports = [
        f"{model.__module__}.{model.__name__}"
        for model in reversed(apps.get_models())
        if model.__module__
    ]
    return app_models_imports


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/base.py
# Line: 290

def get_version(self):
    """
    Return the Django version, which should be correct for all built-in
    Django commands. User-supplied commands can override this method to
    return their own version.
    """
    return django.get_version()


# ==================================================
# File: /root/ecooptimizer/django/django/core/management/templates.py
# Line: 355

def splitext(self, the_path):
    """
    Like os.path.splitext, but takes off .tar, too
    """
    base, ext = posixpath.splitext(the_path)
    if base.lower().endswith(".tar"):
        ext = base[-4:] + ext
        base = base[:-4]
    return base, ext


# ==================================================
# Line: 390

def apply_umask(self, old_path, new_path):
    current_umask = os.umask(0)
    os.umask(current_umask)
    current_mode = stat.S_IMODE(os.stat(old_path).st_mode)
    os.chmod(new_path, current_mode & ~current_umask)


# ==================================================
# Line: 396

def make_writeable(self, filename):
    """
    Make sure that the file is writeable.
    Useful if our source is read-only.
    """
    if not os.access(filename, os.W_OK):
        st = os.stat(filename)
        new_permissions = stat.S_IMODE(st.st_mode) | stat.S_IWUSR
        os.chmod(filename, new_permissions)

# ==================================================
# File: /root/ecooptimizer/django/django/core/validators.py
# Occurrences: Lines 407-410 (2 instances)

def compare(self, a, b):
    return a is not b


# ==================================================
# File: /root/ecooptimizer/django/django/core/servers/basehttp.py
# Line: 105

def _close_connections(self):
    # Used for mocking in tests.
    connections.close_all()


# ==================================================
# File: /root/ecooptimizer/django/django/views/debug.py
# Line: 175

def is_active(self, request):
    """
    This filter is to add safety in production environments (i.e. DEBUG
    is False). If DEBUG is True then your site is not safe anyway.
    This hook is provided as a convenience to easily activate or
    deactivate the filter on a per request basis.
    """
    return settings.DEBUG is False


# ==================================================
# Line: 440

def _get_source(self, filename, loader, module_name):
    source = None
    if hasattr(loader, "get_source"):
        try:
            source = loader.get_source(module_name)
        except ImportError:
            pass
        if source is not None:
            source = source.splitlines()
    if source is None:
        try:
            with open(filename, "rb") as fp:
                source = fp.read().splitlines()
        except OSError:
            pass
    return source


# ==================================================
# Line: 493

def _get_explicit_or_implicit_cause(self, exc_value):
    explicit = getattr(exc_value, "__cause__", None)
    suppress_context = getattr(exc_value, "__suppress_context__", None)
    implicit = getattr(exc_value, "__context__", None)
    return explicit or (None if suppress_context else implicit)


# ==================================================
# File: /root/ecooptimizer/django/django/views/generic/dates.py
# Line: 55

def _get_next_year(self, date):
    """
    Return the start date of the next interval.

    The interval is defined by start date <= item date < next start date.
    """
    try:
        return date.replace(year=date.year + 1, month=1, day=1)
    except ValueError:
        raise Http404(_("Date out of range"))


# ==================================================
# Line: 66

def _get_current_year(self, date):
    """Return the start date of the current interval."""
    return date.replace(month=1, day=1)



# ==================================================
# Line: 105

def _get_next_month(self, date):
    """
    Return the start date of the next interval.

    The interval is defined by start date <= item date < next start date.
    """
    if date.month == 12:
        try:
            return date.replace(year=date.year + 1, month=1, day=1)
        except ValueError:
            raise Http404(_("Date out of range"))
    else:
        return date.replace(month=date.month + 1, day=1)


# ==================================================
# Line: 119

def _get_current_month(self, date):
    """Return the start date of the previous interval."""
    return date.replace(day=1)



# ==================================================
# Line: 158

def _get_next_day(self, date):
    """
    Return the start date of the next interval.

    The interval is defined by start date <= item date < next start date.
    """
    return date + datetime.timedelta(days=1)


# ==================================================
# Line: 166

def _get_current_day(self, date):
    """Return the start date of the current interval."""
    return date



# ==================================================
# File: /root/ecooptimizer/django/django/views/i18n.py
# Line: 126

def get_paths(self, packages):
    allowable_packages = {
        app_config.name: app_config for app_config in apps.get_app_configs()
    }
    app_configs = [
        allowable_packages[p] for p in packages if p in allowable_packages
    ]
    if len(app_configs) < len(packages):
        excluded = [p for p in packages if p not in allowable_packages]
        raise ValueError(
            "Invalid package(s) provided to JavaScriptCatalog: %s"
            % ",".join(excluded)
        )
    # paths of requested packages
    return [os.path.join(app.path, "locale") for app in app_configs]


# ==================================================
# Line: 212

def render_to_response(self, context, **response_kwargs):
    def indent(s):
        return s.replace("\n", "\n  ")

    with builtin_template_path("i18n_catalog.js").open(encoding="utf-8") as fh:
        template = Engine().from_string(fh.read())
    context["catalog_str"] = (
        indent(json.dumps(context["catalog"], sort_keys=True, indent=2))
        if context["catalog"]
        else None
    )
    context["formats_str"] = indent(
        json.dumps(context["formats"], sort_keys=True, indent=2)
    )

    return HttpResponse(
        template.render(Context(context)), 'text/javascript; charset="utf-8"'
    )



# ==================================================
