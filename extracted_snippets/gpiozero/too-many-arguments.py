# too-many-arguments snippets for gpiozero

# File: /root/ecooptimizer/gpiozero/gpiozero/pins/mock.py
# Line: 337

def __init__(self, clock_pin, mosi_pin=None, miso_pin=None,
             select_pin=None, *, clock_polarity=False, clock_phase=False,
             lsb_first=False, bits_per_word=8, select_high=False,
             pin_factory=None):
    if pin_factory is None:
        pin_factory = Device.pin_factory
        assert isinstance(pin_factory, MockFactory)
    self.clock_pin = pin_factory.pin(clock_pin, pin_class=MockSPIClockPin)
    self.mosi_pin = None if mosi_pin is None else pin_factory.pin(mosi_pin)
    self.miso_pin = None if miso_pin is None else pin_factory.pin(miso_pin)
    self.select_pin = None if select_pin is None else pin_factory.pin(select_pin, pin_class=MockSPISelectPin)
    self.clock_polarity = clock_polarity
    self.clock_phase = clock_phase
    self.lsb_first = lsb_first
    self.bits_per_word = bits_per_word
    self.select_high = select_high
    self.rx_bit = 0
    self.rx_buf = []
    self.tx_buf = []
    self.clock_pin.spi_devices.append(self)
    self.select_pin.spi_device = self


# ==================================================
# File: /root/ecooptimizer/gpiozero/gpiozero/boards.py
# Line: 215

def __init__(self, *pins, pull_up=True, active_state=None,
             bounce_time=None, hold_time=1, hold_repeat=False,
             _order=None, pin_factory=None, **named_pins):
    super().__init__(
        *(
            Button(pin, pull_up=pull_up, active_state=active_state,
                   bounce_time=bounce_time, hold_time=hold_time,
                   hold_repeat=hold_repeat, pin_factory=pin_factory)
            for pin in pins
        ),
        _order=_order,
        pin_factory=pin_factory,
        **{
            name: Button(pin, pull_up=pull_up, active_state=active_state,
                         bounce_time=bounce_time, hold_time=hold_time,
                         hold_repeat=hold_repeat, pin_factory=pin_factory)
            for name, pin in named_pins.items()
        }
    )
    if len(self) == 0:
        raise GPIOPinMissing('No pins given')
    def get_new_handler(device):
        def fire_both_events(ticks, state):
            device._fire_events(ticks, device._state_to_value(state))
            self._fire_events(ticks, self.is_active)
        return fire_both_events
    # _handlers only exists to ensure that we keep a reference to the
    # generated fire_both_events handler for each Button (remember that
    # pin.when_changed only keeps a weak reference to handlers)
    self._handlers = tuple(get_new_handler(device) for device in self)
    for button, handler in zip(self, self._handlers):
        button.pin.when_changed = handler
    self._when_changed = None
    self._last_value = None
    # Call _fire_events once to set initial state of events
    self._fire_events(self.pin_factory.ticks(), self.is_active)
    self.hold_time = hold_time
    self.hold_repeat = hold_repeat


# ==================================================
# Line: 498

def blink(
        self, on_time=1, off_time=1, fade_in_time=0, fade_out_time=0,
        n=None, background=True):
    """
    Make all the LEDs turn on and off repeatedly.

    :param float on_time:
        Number of seconds on. Defaults to 1 second.

    :param float off_time:
        Number of seconds off. Defaults to 1 second.

    :param float fade_in_time:
        Number of seconds to spend fading in. Defaults to 0. Must be 0 if
        ``pwm`` was :data:`False` when the class was constructed
        (:exc:`ValueError` will be raised if not).

    :param float fade_out_time:
        Number of seconds to spend fading out. Defaults to 0. Must be 0 if
        ``pwm`` was :data:`False` when the class was constructed
        (:exc:`ValueError` will be raised if not).

    :type n: int or None
    :param n:
        Number of times to blink; :data:`None` (the default) means forever.

    :param bool background:
        If :data:`True`, start a background thread to continue blinking and
        return immediately. If :data:`False`, only return when the blink is
        finished (warning: the default value of *n* will result in this
        method never returning).
    """
    for led in self.leds:
        if isinstance(led, LED):
            if fade_in_time:
                raise ValueError('fade_in_time must be 0 with non-PWM LEDs')
            if fade_out_time:
                raise ValueError('fade_out_time must be 0 with non-PWM LEDs')
    self._stop_blink()
    self._blink_thread = GPIOThread(
        self._blink_device,
        (on_time, off_time, fade_in_time, fade_out_time, n))
    self._blink_thread.start()
    if not background:
        self._blink_thread.join()
        self._blink_thread = None


# ==================================================
# Line: 579

def _blink_device(
        self, on_time, off_time, fade_in_time, fade_out_time, n, fps=25):
    sequence = []
    if fade_in_time > 0:
        sequence += [
            (i * (1 / fps) / fade_in_time, 1 / fps)
            for i in range(int(fps * fade_in_time))
        ]
    sequence.append((1, on_time))
    if fade_out_time > 0:
        sequence += [
            (1 - (i * (1 / fps) / fade_out_time), 1 / fps)
            for i in range(int(fps * fade_out_time))
        ]
    sequence.append((0, off_time))
    if n is None:
        sequence = cycle(sequence)
    else:
        sequence = chain.from_iterable(repeat(sequence, n))
    with self._blink_lock:
        self._blink_leds = list(self.leds)
        for led in self._blink_leds:
            if led._controller not in (None, self):
                led._controller._stop_blink(led)
            led._controller = self
    for value, delay in sequence:
        with self._blink_lock:
            if not self._blink_leds:
                break
            for led in self._blink_leds:
                led._write(value)
        if self._blink_thread.stopping.wait(delay):
            break



# ==================================================
# Line: 945

def __init__(self, *pins, dp=None, font=None, pwm=False, active_high=True,
             initial_value=" ", pin_factory=None):
    if not 1 < len(pins) <= 26:
        raise PinInvalidPin(
            'Must have between 2 and 26 LEDs in LEDCharDisplay')
    for pin in pins:
        if isinstance(pin, LEDCollection):
            raise PinInvalidPin(
                'Cannot use LEDCollection in LEDCharDisplay')

    if font is None:
        if len(pins) == 7:
            with resources.files('gpiozero.fonts').joinpath('7seg.txt').open() as f:
                font = load_font_7seg(f)
        elif len(pins) == 14:
            with resources.files('gpiozero.fonts').joinpath('14seg.txt').open() as f:
                font = load_font_14seg(f)
        else:
            # Construct a default dict containing a definition for " "
            font = {" ": (0,) * len(pins)}
    self._font = LEDCharFont(font)

    pins = {chr(ord('a') + i): pin for i, pin in enumerate(pins)}
    order = sorted(pins.keys())
    if dp is not None:
        pins['dp'] = dp
        order.append('dp')
    super().__init__(
        pwm=pwm, active_high=active_high, initial_value=None,
        _order=order, pin_factory=pin_factory, **pins)
    if initial_value is not None:
        self.value = initial_value


# ==================================================
# Line: 1515

def __init__(self, red=None, amber=None, green=None, *,
             pwm=False, initial_value=False, yellow=None,
             pin_factory=None):
    if amber is not None and yellow is not None:
        raise OutputDeviceBadValue(
            'Only one of amber or yellow can be specified')
    devices = OrderedDict((('red', red), ))
    self._display_yellow = amber is None and yellow is not None
    if self._display_yellow:
        devices['yellow'] = yellow
    else:
        devices['amber'] = amber
    devices['green'] = green
    if not all(p is not None for p in devices.values()):
        raise GPIOPinMissing(
            f'{", ".join(devices.keys())} pins must be provided')
    super().__init__(
        pwm=pwm, initial_value=initial_value,
        _order=devices.keys(), pin_factory=pin_factory,
        **devices)


# ==================================================
# File: /root/ecooptimizer/gpiozero/gpiozero/input_devices.py
# Line: 252

def __init__(
        self, pin=None, *, pull_up=False, active_state=None, threshold=0.5,
        queue_len=5, sample_wait=0.0, partial=False, average=median,
        ignore=None, pin_factory=None):
    self._queue = None
    super().__init__(
        pin, pull_up=pull_up, active_state=active_state,
        pin_factory=pin_factory)
    try:
        self._queue = GPIOQueue(self, queue_len, sample_wait, partial,
                                average, ignore)
        self.threshold = float(threshold)
    except:
        self.close()
        raise


# ==================================================
# Line: 409

def __init__(self, pin=None, *, pull_up=True, active_state=None,
             bounce_time=None, hold_time=1, hold_repeat=False,
             pin_factory=None):
    super().__init__(
        pin, pull_up=pull_up, active_state=active_state,
        bounce_time=bounce_time, pin_factory=pin_factory)
    self.hold_time = hold_time
    self.hold_repeat = hold_repeat


# ==================================================
# Line: 496

def __init__(self, pin=None, *, pull_up=False, active_state=None,
             queue_len=5, sample_rate=100, threshold=0.5, partial=False,
             pin_factory=None):
    super().__init__(
        pin, pull_up=pull_up, active_state=active_state,
        threshold=threshold, queue_len=queue_len,
        sample_wait=1 / sample_rate, partial=partial,
        pin_factory=pin_factory)
    self._queue.start()


# ==================================================
# Line: 585

def __init__(self, pin=None, *, pull_up=False, active_state=None,
             queue_len=1, sample_rate=10, threshold=0.5, partial=False,
             pin_factory=None):
    super().__init__(
        pin, pull_up=pull_up, active_state=active_state,
        threshold=threshold, queue_len=queue_len, sample_wait=1 /
        sample_rate, partial=partial, pin_factory=pin_factory, average=mean)
    self._queue.start()


# ==================================================
# Line: 665

def __init__(self, pin=None, *, queue_len=5, charge_time_limit=0.01,
             threshold=0.1, partial=False, pin_factory=None):
    super().__init__(
        pin, pull_up=False, threshold=threshold, queue_len=queue_len,
        sample_wait=0.0, partial=partial, pin_factory=pin_factory)
    try:
        self._charge_time_limit = charge_time_limit
        self._charge_time = None
        self._charged = Event()
        self.pin.edges = 'rising'
        self.pin.bounce = None
        self.pin.when_changed = self._cap_charged
        self._queue.start()
    except:
        self.close()
        raise


# ==================================================
# Line: 823

def __init__(self, echo=None, trigger=None, *, queue_len=9,
             max_distance=1, threshold_distance=0.3, partial=False,
             pin_factory=None):
    self._trigger = None
    super().__init__(
        echo, pull_up=False, queue_len=queue_len, sample_wait=0.06,
        partial=partial, ignore=frozenset({None}), pin_factory=pin_factory
    )
    try:
        if max_distance <= 0:
            raise ValueError('invalid maximum distance (must be positive)')
        self._max_distance = max_distance
        self.threshold = threshold_distance / max_distance
        self.speed_of_sound = 343.26 # m/s
        self._trigger = GPIODevice(trigger, pin_factory=pin_factory)
        self._echo = Event()
        self._echo_rise = None
        self._echo_fall = None
        self._trigger.pin.function = 'output'
        self._trigger.pin.state = False
        self.pin.edges = 'both'
        self.pin.bounce = None
        self.pin.when_changed = self._echo_changed
        self._queue.start()
    except:
        self.close()
        raise

    if PiGPIOFactory is None or not isinstance(self.pin_factory, PiGPIOFactory):
        warnings.warn(PWMSoftwareFallback(
            'For more accurate readings, use the pigpio pin factory.'
            'See https://gpiozero.readthedocs.io/en/stable/api_input.html#distancesensor-hc-sr04 for more info'
        ))


# ==================================================
# Line: 1129

def __init__(self, a, b, *, bounce_time=None, max_steps=16,
             threshold_steps=(0, 0), wrap=False, pin_factory=None):
    min_thresh, max_thresh = threshold_steps
    if max_thresh < min_thresh:
        raise ValueError('maximum threshold cannot be less than minimum')
    self._steps = 0
    self._max_steps = int(max_steps)
    self._threshold = (int(min_thresh), int(max_thresh))
    self._wrap = bool(wrap)
    self._state = 'idle'
    self._edge = 0
    self._when_rotated = None
    self._when_rotated_cw = None
    self._when_rotated_ccw = None
    self._rotate_event = Event()
    self._rotate_cw_event = Event()
    self._rotate_ccw_event = Event()
    super().__init__(
        a=InputDevice(a, pull_up=True, pin_factory=pin_factory),
        b=InputDevice(b, pull_up=True, pin_factory=pin_factory),
        _order=('a', 'b'), pin_factory=pin_factory)
    self.a.pin.bounce_time = bounce_time
    self.b.pin.bounce_time = bounce_time
    self.a.pin.edges = 'both'
    self.b.pin.edges = 'both'
    self.a.pin.when_changed = self._a_changed
    self.b.pin.when_changed = self._b_changed
    # Call _fire_events once to set initial state of events
    self._fire_events(self.pin_factory.ticks(), self.is_active)


# ==================================================
# File: /root/ecooptimizer/gpiozero/gpiozero/internal_devices.py
# Line: 263

def __init__(self, sensor_file='/sys/class/thermal/thermal_zone0/temp', *,
        min_temp=0.0, max_temp=100.0, threshold=80.0, event_delay=5.0,
        pin_factory=None):
    self.sensor_file = sensor_file
    super().__init__(event_delay=event_delay, pin_factory=pin_factory)
    try:
        if min_temp >= max_temp:
            raise ValueError('max_temp must be greater than min_temp')
        self.min_temp = min_temp
        self.max_temp = max_temp
        if not min_temp <= threshold <= max_temp:
            warnings.warn(ThresholdOutOfRange(
                'threshold is outside of the range (min_temp, max_temp)'))
        self.threshold = threshold
        self._fire_events(self.pin_factory.ticks(), self.is_active)
    except:
        self.close()
        raise


# ==================================================
# Line: 396

def __init__(self, load_average_file='/proc/loadavg', *,
             min_load_average=0.0, max_load_average=1.0, threshold=0.8,
             minutes=5, event_delay=10.0, pin_factory=None):
    if min_load_average >= max_load_average:
        raise ValueError(
            'max_load_average must be greater than min_load_average')
    self.load_average_file = load_average_file
    self.min_load_average = min_load_average
    self.max_load_average = max_load_average
    if not min_load_average <= threshold <= max_load_average:
        warnings.warn(ThresholdOutOfRange(
            'threshold is outside of the range (min_load_average, '
            'max_load_average)'))
    self.threshold = threshold
    if minutes not in (1, 5, 15):
        raise ValueError('minutes must be 1, 5 or 15')
    self._load_average_file_column = {
        1: 0,
        5: 1,
        15: 2,
    }[minutes]
    super().__init__(event_delay=event_delay, pin_factory=pin_factory)
    self._fire_events(self.pin_factory.ticks(), None)


# ==================================================
# File: /root/ecooptimizer/gpiozero/gpiozero/mixins.py
# Line: 547

def __init__(
        self, parent, queue_len=5, sample_wait=0.0, partial=False,
        average=median, ignore=None):
    assert callable(average)
    if queue_len < 1:
        raise BadQueueLen('queue_len must be at least one')
    if sample_wait < 0:
        raise BadWaitTime('sample_wait must be 0 or greater')
    if ignore is None:
        ignore = set()
    super().__init__(target=self.fill)
    self.queue = deque(maxlen=queue_len)
    self.partial = bool(partial)
    self.sample_wait = float(sample_wait)
    self.full = Event()
    self.parent = weakref.proxy(parent)
    self.average = average
    self.ignore = ignore


# ==================================================
# File: /root/ecooptimizer/gpiozero/gpiozero/output_devices.py
# Line: 476

def blink(
        self, on_time=1, off_time=1, fade_in_time=0, fade_out_time=0,
        n=None, background=True):
    """
    Make the device turn on and off repeatedly.

    :param float on_time:
        Number of seconds on. Defaults to 1 second.

    :param float off_time:
        Number of seconds off. Defaults to 1 second.

    :param float fade_in_time:
        Number of seconds to spend fading in. Defaults to 0.

    :param float fade_out_time:
        Number of seconds to spend fading out. Defaults to 0.

    :type n: int or None
    :param n:
        Number of times to blink; :data:`None` (the default) means forever.

    :param bool background:
        If :data:`True` (the default), start a background thread to
        continue blinking and return immediately. If :data:`False`, only
        return when the blink is finished (warning: the default value of
        *n* will result in this method never returning).
    """
    self._stop_blink()
    self._blink_thread = GPIOThread(
        self._blink_device,
        (on_time, off_time, fade_in_time, fade_out_time, n)
    )
    self._blink_thread.start()
    if not background:
        self._blink_thread.join()
        self._blink_thread = None


# ==================================================
# Line: 547

def _blink_device(
        self, on_time, off_time, fade_in_time, fade_out_time, n, fps=25):
    sequence = []
    if fade_in_time > 0:
        sequence += [
            (i * (1 / fps) / fade_in_time, 1 / fps)
            for i in range(int(fps * fade_in_time))
            ]
    sequence.append((1, on_time))
    if fade_out_time > 0:
        sequence += [
            (1 - (i * (1 / fps) / fade_out_time), 1 / fps)
            for i in range(int(fps * fade_out_time))
            ]
    sequence.append((0, off_time))
    sequence = (
            cycle(sequence) if n is None else
            chain.from_iterable(repeat(sequence, n))
            )
    for value, delay in sequence:
        self._write(value)
        if self._blink_thread.stopping.wait(delay):
            break



# ==================================================
# Line: 869

def __init__(self, red=None, green=None, blue=None, *, active_high=True,
             initial_value=(0, 0, 0), pwm=True, pin_factory=None):
    self._leds = ()
    self._blink_thread = None
    if not all(p is not None for p in [red, green, blue]):
        raise GPIOPinMissing('red, green, and blue pins must be provided')
    LEDClass = PWMLED if pwm else LED
    super().__init__(pin_factory=pin_factory)
    self._leds = tuple(
        LEDClass(pin, active_high=active_high, pin_factory=pin_factory)
        for pin in (red, green, blue))
    self.value = initial_value


# ==================================================
# Line: 1008

def blink(
        self, on_time=1, off_time=1, fade_in_time=0, fade_out_time=0,
        on_color=(1, 1, 1), off_color=(0, 0, 0), n=None, background=True):
    """
    Make the device turn on and off repeatedly.

    :param float on_time:
        Number of seconds on. Defaults to 1 second.

    :param float off_time:
        Number of seconds off. Defaults to 1 second.

    :param float fade_in_time:
        Number of seconds to spend fading in. Defaults to 0. Must be 0 if
        *pwm* was :data:`False` when the class was constructed
        (:exc:`ValueError` will be raised if not).

    :param float fade_out_time:
        Number of seconds to spend fading out. Defaults to 0. Must be 0 if
        *pwm* was :data:`False` when the class was constructed
        (:exc:`ValueError` will be raised if not).

    :type on_color: ~colorzero.Color or tuple
    :param on_color:
        The color to use when the LED is "on". Defaults to white.

    :type off_color: ~colorzero.Color or tuple
    :param off_color:
        The color to use when the LED is "off". Defaults to black.

    :type n: int or None
    :param n:
        Number of times to blink; :data:`None` (the default) means forever.

    :param bool background:
        If :data:`True` (the default), start a background thread to
        continue blinking and return immediately. If :data:`False`, only
        return when the blink is finished (warning: the default value of
        *n* will result in this method never returning).
    """
    if isinstance(self._leds[0], LED):
        if fade_in_time:
            raise ValueError('fade_in_time must be 0 with non-PWM RGBLEDs')
        if fade_out_time:
            raise ValueError('fade_out_time must be 0 with non-PWM RGBLEDs')
    self._stop_blink()
    self._blink_thread = GPIOThread(
        self._blink_device,
        (
            on_time, off_time, fade_in_time, fade_out_time,
            on_color, off_color, n
        )
    )
    self._blink_thread.start()
    if not background:
        self._blink_thread.join()
        self._blink_thread = None


# ==================================================
# Line: 1066

def pulse(
        self, fade_in_time=1, fade_out_time=1,
        on_color=(1, 1, 1), off_color=(0, 0, 0), n=None, background=True):
    """
    Make the device fade in and out repeatedly.

    :param float fade_in_time:
        Number of seconds to spend fading in. Defaults to 1.

    :param float fade_out_time:
        Number of seconds to spend fading out. Defaults to 1.

    :type on_color: ~colorzero.Color or tuple
    :param on_color:
        The color to use when the LED is "on". Defaults to white.

    :type off_color: ~colorzero.Color or tuple
    :param off_color:
        The color to use when the LED is "off". Defaults to black.

    :type n: int or None
    :param n:
        Number of times to pulse; :data:`None` (the default) means forever.

    :param bool background:
        If :data:`True` (the default), start a background thread to
        continue pulsing and return immediately. If :data:`False`, only
        return when the pulse is finished (warning: the default value of
        *n* will result in this method never returning).
    """
    on_time = off_time = 0
    self.blink(
        on_time, off_time, fade_in_time, fade_out_time,
        on_color, off_color, n, background
    )


# ==================================================
# Line: 1108

def _blink_device(
        self, on_time, off_time, fade_in_time, fade_out_time, on_color,
        off_color, n, fps=25):
    # Define a simple lambda to perform linear interpolation between
    # off_color and on_color
    lerp = lambda t, fade_in: tuple(
        (1 - t) * off + t * on
        if fade_in else
        (1 - t) * on + t * off
        for off, on in zip(off_color, on_color)
        )
    sequence = []
    if fade_in_time > 0:
        sequence += [
            (lerp(i * (1 / fps) / fade_in_time, True), 1 / fps)
            for i in range(int(fps * fade_in_time))
            ]
    sequence.append((on_color, on_time))
    if fade_out_time > 0:
        sequence += [
            (lerp(i * (1 / fps) / fade_out_time, False), 1 / fps)
            for i in range(int(fps * fade_out_time))
            ]
    sequence.append((off_color, off_time))
    sequence = (
            cycle(sequence) if n is None else
            chain.from_iterable(repeat(sequence, n))
            )
    for l in self._leds:
        l._controller = self
    for value, delay in sequence:
        for l, v in zip(self._leds, value):
            l._write(v)
        if self._blink_thread.stopping.wait(delay):
            break



# ==================================================
# Line: 1490

def __init__(self, pin=None, *, initial_value=0.0, min_pulse_width=1/1000,
             max_pulse_width=2/1000, frame_width=20/1000,
             pin_factory=None):
    if min_pulse_width >= max_pulse_width:
        raise ValueError('min_pulse_width must be less than max_pulse_width')
    if max_pulse_width >= frame_width:
        raise ValueError('max_pulse_width must be less than frame_width')
    self._frame_width = frame_width
    self._min_dc = min_pulse_width / frame_width
    self._dc_range = (max_pulse_width - min_pulse_width) / frame_width
    self._min_value = -1
    self._value_range = 2
    super().__init__(
        pwm_device=PWMOutputDevice(
            pin, frequency=int(1 / frame_width), pin_factory=pin_factory),
        pin_factory=pin_factory
    )

    if PiGPIOFactory is None or not isinstance(self.pin_factory, PiGPIOFactory):
        warnings.warn(PWMSoftwareFallback(
            'To reduce servo jitter, use the pigpio pin factory.'
            'See https://gpiozero.readthedocs.io/en/stable/api_output.html#servo for more info'
        ))

    try:
        self.value = initial_value
    except:
        self.close()
        raise


# ==================================================
# Line: 1711

def __init__(self, pin=None, *, initial_angle=0.0, min_angle=-90,
             max_angle=90, min_pulse_width=1/1000, max_pulse_width=2/1000,
             frame_width=20/1000, pin_factory=None):
    self._min_angle = min_angle
    self._angular_range = max_angle - min_angle
    if initial_angle is None:
        initial_value = None
    elif ((min_angle <= initial_angle <= max_angle) or
        (max_angle <= initial_angle <= min_angle)):
        initial_value = 2 * ((initial_angle - min_angle) / self._angular_range) - 1
    else:
        raise OutputDeviceBadValue(
            f"AngularServo angle must be between {min_angle} and "
            f"{max_angle}, or None")
    super().__init__(pin, initial_value=initial_value,
                     min_pulse_width=min_pulse_width,
                     max_pulse_width=max_pulse_width,
                     frame_width=frame_width, pin_factory=pin_factory)


# ==================================================
