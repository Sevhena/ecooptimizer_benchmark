# no-self-use snippets for flask

# File: /root/ecooptimizer/flask/src/flask/sessions.py
# Line: 103

def _fail(self, *args: t.Any, **kwargs: t.Any) -> t.NoReturn:
    raise RuntimeError(
        "The session is unavailable because no secret "
        "key was set.  Set the secret_key on the "
        "application to something unique and secret."
    )


# ==================================================
# Occurrences: Lines 185-189 (2 instances)

def get_cookie_name(self, app: Flask) -> str:
    """The name of the session cookie. Uses``app.config["SESSION_COOKIE_NAME"]``."""
    return app.config["SESSION_COOKIE_NAME"]  # type: ignore[no-any-return]


# ==================================================
# Line: 201

def get_cookie_path(self, app: Flask) -> str:
    """Returns the path for which the cookie should be valid.  The
    default implementation uses the value from the ``SESSION_COOKIE_PATH``
    config var if it's set, and falls back to ``APPLICATION_ROOT`` or
    uses ``/`` if it's ``None``.
    """
    return app.config["SESSION_COOKIE_PATH"] or app.config["APPLICATION_ROOT"]  # type: ignore[no-any-return]


# ==================================================
# Line: 209

def get_cookie_httponly(self, app: Flask) -> bool:
    """Returns True if the session cookie should be httponly.  This
    currently just returns the value of the ``SESSION_COOKIE_HTTPONLY``
    config var.
    """
    return app.config["SESSION_COOKIE_HTTPONLY"]  # type: ignore[no-any-return]


# ==================================================
# Line: 216

def get_cookie_secure(self, app: Flask) -> bool:
    """Returns True if the cookie should be secure.  This currently
    just returns the value of the ``SESSION_COOKIE_SECURE`` setting.
    """
    return app.config["SESSION_COOKIE_SECURE"]  # type: ignore[no-any-return]


# ==================================================
# Line: 222

def get_cookie_samesite(self, app: Flask) -> str | None:
    """Return ``'Strict'`` or ``'Lax'`` if the cookie should use the
    ``SameSite`` attribute. This currently just returns the value of
    the :data:`SESSION_COOKIE_SAMESITE` setting.
    """
    return app.config["SESSION_COOKIE_SAMESITE"]  # type: ignore[no-any-return]


# ==================================================
# Line: 229

def get_cookie_partitioned(self, app: Flask) -> bool:
    """Returns True if the cookie should be partitioned. By default, uses
    the value of :data:`SESSION_COOKIE_PARTITIONED`.

    .. versionadded:: 3.1
    """
    return app.config["SESSION_COOKIE_PARTITIONED"]  # type: ignore[no-any-return]


# ==================================================
# Line: 237

def get_expiration_time(self, app: Flask, session: SessionMixin) -> datetime | None:
    """A helper method that returns an expiration date for the session
    or ``None`` if the session is linked to the browser session.  The
    default implementation returns now + the permanent session
    lifetime configured on the application.
    """
    if session.permanent:
        return datetime.now(timezone.utc) + app.permanent_session_lifetime
    return None


# ==================================================
# Line: 247

def should_set_cookie(self, app: Flask, session: SessionMixin) -> bool:
    """Used by session backends to determine if a ``Set-Cookie`` header
    should be set for this session cookie for this response. If the session
    has been modified, the cookie is set. If the session is permanent and
    the ``SESSION_REFRESH_EACH_REQUEST`` config is true, the cookie is
    always set.

    This check is usually skipped if the session was deleted.

    .. versionadded:: 0.11
    """

    return session.modified or (
        session.permanent and app.config["SESSION_REFRESH_EACH_REQUEST"]
    )


# ==================================================
# File: /root/ecooptimizer/flask/src/flask/blueprints.py
# Line: 55

def get_send_file_max_age(self, filename: str | None) -> int | None:
    """Used by :func:`send_file` to determine the ``max_age`` cache
    value for a given file path if it wasn't passed.

    By default, this returns :data:`SEND_FILE_MAX_AGE_DEFAULT` from
    the configuration of :data:`~flask.current_app`. This defaults
    to ``None``, which tells the browser to use conditional requests
    instead of a timed cache, which is usually preferable.

    Note this is a duplicate of the same method in the Flask
    class.

    .. versionchanged:: 2.0
        The default configuration is ``None`` instead of 12 hours.

    .. versionadded:: 0.9
    """
    value = current_app.config["SEND_FILE_MAX_AGE_DEFAULT"]

    if value is None:
        return None

    if isinstance(value, timedelta):
        return int(value.total_seconds())

    return value  # type: ignore[no-any-return]


# ==================================================
# File: /root/ecooptimizer/flask/src/flask/sansio/app.py
# Line: 536

def select_jinja_autoescape(self, filename: str) -> bool:
    """Returns ``True`` if autoescaping should be active for the given
    template name. If no template name is given, returns `True`.

    .. versionchanged:: 2.2
        Autoescaping is now enabled by default for ``.svg`` files.

    .. versionadded:: 0.5
    """
    if filename is None:
        return True
    return filename.endswith((".html", ".htm", ".xml", ".xhtml", ".svg"))


# ==================================================
# Line: 883

def should_ignore_error(self, error: BaseException | None) -> bool:
    """This is called to figure out if an error should be ignored
    or not as far as the teardown system is concerned.  If this
    function returns ``True`` then the teardown handlers will not be
    passed the error.

    .. versionadded:: 0.10
    """
    return False


# ==================================================
# File: /root/ecooptimizer/flask/src/flask/json/provider.py
# Line: 75

def _prepare_response_obj(
    self, args: tuple[t.Any, ...], kwargs: dict[str, t.Any]

# ==================================================
# File: /root/ecooptimizer/flask/src/flask/app.py
# Line: 281

def get_send_file_max_age(self, filename: str | None) -> int | None:
    """Used by :func:`send_file` to determine the ``max_age`` cache
    value for a given file path if it wasn't passed.

    By default, this returns :data:`SEND_FILE_MAX_AGE_DEFAULT` from
    the configuration of :data:`~flask.current_app`. This defaults
    to ``None``, which tells the browser to use conditional requests
    instead of a timed cache, which is usually preferable.

    Note this is a duplicate of the same method in the Flask
    class.

    .. versionchanged:: 2.0
        The default configuration is ``None`` instead of 12 hours.

    .. versionadded:: 0.9
    """
    value = current_app.config["SEND_FILE_MAX_AGE_DEFAULT"]

    if value is None:
        return None

    if isinstance(value, timedelta):
        return int(value.total_seconds())

    return value  # type: ignore[no-any-return]


# ==================================================
# Line: 980

def async_to_sync(
    self, func: t.Callable[..., t.Coroutine[t.Any, t.Any, t.Any]]

# ==================================================
