# no-self-use snippets for gpiozero

# File: /root/ecooptimizer/gpiozero/gpiozero/pins/__init__.py
# Line: 134

def pin(self, name):
    """
    Creates an instance of a :class:`Pin` descendent representing the
    specified pin.

    .. warning::

        Descendents must ensure that pin instances representing the same
        hardware are identical; i.e. two separate invocations of
        :meth:`pin` for the same pin specification must return the same
        object.
    """
    raise PinUnsupported(  # pragma: no cover
        "Individual pins are not supported by this pin factory")


# ==================================================
# Line: 149

def spi(self, **spi_args):
    """
    Returns an instance of an :class:`SPI` interface, for the specified SPI
    *port* and *device*, or for the specified pins (*clock_pin*,
    *mosi_pin*, *miso_pin*, and *select_pin*).  Only one of the schemes can
    be used; attempting to mix *port* and *device* with pin numbers will
    raise :exc:`SPIBadArgs`.
    """
    raise PinSPIUnsupported(  # pragma: no cover
        'SPI not supported by this pin factory')


# ==================================================
# Line: 348

def _get_pull(self):
    return 'floating'  # pragma: no cover


# ==================================================
# Line: 369

def _get_frequency(self):
    return None  # pragma: no cover


# ==================================================
# Line: 390

def _get_bounce(self):
    return None  # pragma: no cover


# ==================================================
# Line: 432

def _get_edges(self):
    return 'none'  # pragma: no cover


# ==================================================
# Line: 462

def _get_when_changed(self):
    return None  # pragma: no cover


# ==================================================
# Line: 680

def _get_lsb_first(self):
    return False  # pragma: no cover


# ==================================================
# Line: 733

def _get_select_high(self):
    return False  # pragma: no cover


# ==================================================
# Line: 779

def _get_bits_per_word(self):
    return 8  # pragma: no cover


# ==================================================
# Line: 797

def _get_rate(self):
    return 100000  # pragma: no cover


# ==================================================
# Line: 964

def _pin_style(self, pin, style):
    if 'gpio' in pin.interfaces:
        return style('bold green')
    elif pin.name == '5V':
        return style('bold red')
    elif pin.name in {'3V3', '1V8'}:
        return style('bold cyan')
    elif pin.name in {'GND', 'NC'}:
        return style('bold black')
    else:
        return style('yellow')


# ==================================================
# File: /root/ecooptimizer/gpiozero/gpiozero/internal_devices.py
# Line: 556

def _validate_time(self, value):
    if isinstance(value, datetime):
        value = value.time()
    if not isinstance(value, time):
        raise ValueError(
            'start_time and end_time must be a datetime, or time instance')
    return value


# ==================================================
# File: /root/ecooptimizer/gpiozero/gpiozero/mixins.py
# Line: 165

def _wrap_callback(self, instance, fn):
    if not callable(fn):
        raise BadEventHandler('value must be None or a callable')
    # If fn is wrapped with partial (i.e. partial, partialmethod, or wraps
    # has been used to produce it) we need to dig out the "real" function
    # that's been wrapped along with all the mandatory positional args
    # used in the wrapper so we can test the binding
    args = ()
    wrapped_fn = fn
    while isinstance(wrapped_fn, partial):
        args = wrapped_fn.args + args
        wrapped_fn = wrapped_fn.func
    if inspect.isbuiltin(wrapped_fn):
        # We can't introspect the prototype of builtins. In this case we
        # assume that the builtin has no (mandatory) parameters; this is
        # the most reasonable assumption on the basis that pre-existing
        # builtins have no knowledge of gpiozero, and the sole parameter
        # we would pass is a gpiozero object
        return fn
    else:
        # Try binding ourselves to the argspec of the provided callable.
        # If this works, assume the function is capable of accepting no
        # parameters
        try:
            inspect.getcallargs(wrapped_fn, *args)
            return fn
        except TypeError:
            try:
                # If the above fails, try binding with a single parameter
                # (ourselves). If this works, wrap the specified callback
                inspect.getcallargs(wrapped_fn, *(args + (instance,)))
                @wraps(fn)
                def wrapper():
                    return fn(instance)
                return wrapper
            except TypeError:
                raise BadEventHandler(
                    'value must be a callable which accepts up to one '
                    'mandatory parameter')


# ==================================================
# File: /root/ecooptimizer/gpiozero/gpiozero/devices.py
# Line: 327

def _conflicts_with(self, other):
    """
    Called by :meth:`Factory.reserve_pins` to test whether the *other*
    :class:`Device` using a common pin conflicts with this device's intent
    to use it. The default is :data:`True` indicating that all devices
    conflict with common pins.  Sub-classes may override this to permit
    more nuanced replies.
    """
    return True


# ==================================================
