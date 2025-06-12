# no-self-use snippets for scrapy

# File: /root/ecooptimizer/scrapy/scrapy/settings/__init__.py
# Line: 580

def _get_key(self, key_value: Any) -> _SettingsKeyT:
    return (
        key_value
        if isinstance(key_value, (bool, float, int, str, type(None)))
        else str(key_value)
    )


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/list.py
# Line: 17

def short_desc(self) -> str:
    return "List available spiders"


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/runspider.py
# Occurrences: Lines 35-41 (3 instances)

def syntax(self) -> str:
    return "[options] <spider_file>"


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/__init__.py
# Line: 43

def syntax(self) -> str:
    """
    Command syntax (preferably one-line). Do not include command name.
    """
    return ""


# ==================================================
# Line: 49

def short_desc(self) -> str:
    """
    A short description of the command
    """
    return ""


# ==================================================
# Line: 210

def format_part_strings(self, part_strings: list[str]) -> list[str]:
    """
    Underline and title case command line help message headers.
    """
    if part_strings and part_strings[0].startswith("usage: "):
        part_strings[0] = "Usage\n=====\n  " + part_strings[0][len("usage: ") :]
    headings = [
        i for i in range(len(part_strings)) if part_strings[i].endswith(":\n")
    ]
    for index in headings[::-1]:
        char = "-" if "Global Options" in part_strings[index] else "="
        part_strings[index] = part_strings[index][:-2].title()
        underline = "".join(["\n", (char * len(part_strings[index])), "\n"])
        part_strings.insert(index + 1, underline)
    return part_strings

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/genspider.py
# Occurrences: Lines 52-55 (2 instances)

def syntax(self) -> str:
    return "[options] <name> <domain>"


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/version.py
# Occurrences: Lines 12-15 (2 instances)

def syntax(self) -> str:
    return "[-v]"


# ==================================================
# Line: 28

def run(self, args: list[str], opts: argparse.Namespace) -> None:
    if opts.verbose:
        versions = get_versions()
        width = max(len(n) for (n, _) in versions)
        for name, version in versions:
            print(f"{name:<{width}} : {version}")
    else:
        print(f"Scrapy {scrapy.__version__}")

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/bench.py
# Line: 26

def short_desc(self) -> str:
    return "Run quick benchmark test"


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/startproject.py
# Occurrences: Lines 39-45 (3 instances)

def syntax(self) -> str:
    return "<project_name> [project_dir]"


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/fetch.py
# Occurrences: Lines 22-28 (3 instances)

def syntax(self) -> str:
    return "[options] <url>"


# ==================================================
# Line: 65

def _print_bytes(self, bytes_: bytes) -> None:
    sys.stdout.buffer.write(bytes_ + b"\n")


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/parse.py
# Occurrences: Lines 48-51 (2 instances)

def syntax(self) -> str:
    return "[options] <url>"


# ==================================================
# Line: 132

def handle_exception(self, _failure: Failure) -> None:
    logger.error(
        "An error is caught while iterating the async iterable",
        exc_info=failure_to_exc_info(_failure),
    )


# ==================================================
# Line: 204

def _get_items_and_requests(
    self,
    spider_output: Iterable[Any],
    opts: argparse.Namespace,
    depth: int,
    spider: Spider,
    callback: CallbackT,

# ==================================================
# Line: 231

def get_callback_from_rules(
    self, spider: Spider, response: Response

# ==================================================
# Line: 377

def process_request_meta(self, opts: argparse.Namespace) -> None:
    if opts.meta:
        try:
            opts.meta = json.loads(opts.meta)
        except ValueError:
            raise UsageError(
                "Invalid -m/--meta value, pass a valid json string to -m or --meta. "
                'Example: --meta=\'{"foo" : "bar"}\'',
                print_help=False,
            )


# ==================================================
# Line: 388

def process_request_cb_kwargs(self, opts: argparse.Namespace) -> None:
    if opts.cbkwargs:
        try:
            opts.cbkwargs = json.loads(opts.cbkwargs)
        except ValueError:
            raise UsageError(
                "Invalid --cbkwargs value, pass a valid json string to --cbkwargs. "
                'Example: --cbkwargs=\'{"foo" : "bar"}\'',
                print_help=False,
            )


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/check.py
# Occurrences: Lines 46-49 (2 instances)

def syntax(self) -> str:
    return "[options] <spider>"


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/shell.py
# Occurrences: Lines 31-37 (3 instances)

def syntax(self) -> str:
    return "[url|file]"


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/edit.py
# Occurrences: Lines 15-21 (3 instances)

def syntax(self) -> str:
    return "<spider>"


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/commands/view.py
# Occurrences: Lines 12-15 (2 instances)

def short_desc(self) -> str:
    return "Open URL in browser, as seen by Scrapy"


# ==================================================
# Line: 24

def _print_response(self, response: Response, opts: argparse.Namespace) -> None:
    if not isinstance(response, TextResponse):
        logger.error("Cannot view a non-text response.")
        return
    open_in_browser(response)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/spiders/crawl.py
# Occurrences: Lines 118-121 (2 instances)

def parse_start_url(self, response: Response, **kwargs: Any) -> Any:
    return []


# ==================================================
# Line: 200

def _handle_failure(
    self, failure: Failure, errback: Callable[[Failure], Any] | None

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/spiders/sitemap.py
# Line: 64

def sitemap_filter(
    self, entries: Iterable[dict[str, Any]]

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/spiders/feed.py
# Line: 37

def process_results(
    self, response: Response, results: Iterable[Any]

# ==================================================
# Line: 49

def adapt_response(self, response: Response) -> Response:
    """You can override this function in order to make any changes you want
    to into the feed before parsing it. This function must return a
    response.
    """
    return response


# ==================================================
# Line: 128

def process_results(
    self, response: Response, results: Iterable[Any]

# ==================================================
# Line: 134

def adapt_response(self, response: Response) -> Response:
    """This method has the same purpose as the one in XMLFeedSpider"""
    return response


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/utils/datatypes.py
# Occurrences: Lines 73-77 (2 instances)

def normkey(self, key: AnyStr) -> AnyStr:
    """Method to normalize dictionary key access"""
    return key.lower()


# ==================================================
# Occurrences: Lines 136-139 (2 instances)

def _normkey(self, key: AnyStr) -> AnyStr:
    return key


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/utils/benchserver.py
# Line: 15

def render(self, request: Request) -> bytes:
    total = _getarg(request, b"total", 100, int)
    show = _getarg(request, b"show", 10, int)
    nlist = [random.randint(1, total) for _ in range(show)]  # noqa: S311
    request.write(b"<html><head></head><body>")
    assert request.args is not None
    args = request.args.copy()
    for nl in nlist:
        args["n"] = nl
        argstr = urlencode(args, doseq=True)
        request.write(f"<a href='/follow?{argstr}'>follow {nl}</a><br>".encode())
    request.write(b"</body></html>")
    return b""



# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/utils/testproc.py
# Line: 49

def _process_finished(
    self, pp: TestProcessProtocol, cmd: list[str], check_code: bool

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/spidermiddlewares/base.py
# Line: 74

def get_processed_request(
    self, request: Request, response: Response | None

# ==================================================
# Line: 94

def get_processed_item(self, item: Any, response: Response | None) -> Any:
    """Return a processed item from the spider output.

    This method is called with a single item from the start seeds or the
    spider output. It should return the same or a different item, or
    ``None`` to ignore it.

    :param item: the input item
    :type item: item object

    :param response: the response being processed
    :type response: :class:`~scrapy.http.Response` object or ``None`` for
        start seeds

    :return: the processed item or ``None``
    """
    return item

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/spidermiddlewares/offsite.py
# Line: 82

def get_host_regex(self, spider: Spider) -> re.Pattern[str]:
    """Override this method to implement a different offsite policy"""
    allowed_domains = getattr(spider, "allowed_domains", None)
    if not allowed_domains:
        return re.compile("")  # allow all by default
    url_pattern = re.compile(r"^https?://.*$")
    port_pattern = re.compile(r":\d+$")
    domains = []
    for domain in allowed_domains:
        if domain is None:
            continue
        if url_pattern.match(domain):
            message = (
                "allowed_domains accepts only domains, not URLs. "
                f"Ignoring URL entry {domain} in allowed_domains."
            )
            warnings.warn(message, URLWarning)
        elif port_pattern.search(domain):
            message = (
                "allowed_domains accepts only domains without ports. "
                f"Ignoring entry {domain} in allowed_domains."
            )
            warnings.warn(message, PortWarning)
        else:
            domains.append(re.escape(domain))
    regex = rf"^(.*\.)?({'|'.join(domains)})$"
    return re.compile(regex)


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/spidermiddlewares/httperror.py
# Line: 66

def process_spider_exception(
    self, response: Response, exception: Exception, spider: Spider

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/spidermiddlewares/referer.py
# Line: 65

def strip_url(self, url: str, origin_only: bool = False) -> str | None:
    """
    https://www.w3.org/TR/referrer-policy/#strip-url

    If url is null, return no referrer.
    If url's scheme is a local scheme, then return no referrer.
    Set url's username to the empty string.
    Set url's password to null.
    Set url's fragment to null.
    If the origin-only flag is true, then:
        Set url's path to null.
        Set url's query to null.
    Return url.
    """
    if not url:
        return None
    return strip_url(
        url,
        strip_credentials=True,
        strip_fragment=True,
        strip_default_port=True,
        origin_only=origin_only,
    )


# ==================================================
# Line: 100

def tls_protected(self, url: str) -> bool:
    return urlparse(url).scheme in ("https", "ftps")



# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/spidermiddlewares/start.py
# Line: 26

def get_processed_request(
    self, request: Request, response: Response | None

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/crawler.py
# Line: 627

def _stop_reactor(self, _: Any = None) -> None:
    from twisted.internet import reactor

    # raised if already stopped or in shutdown stage
    with contextlib.suppress(RuntimeError):
        reactor.stop()



# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/exporters.py
# Line: 60

def serialize_field(
    self, field: Mapping[str, Any] | Field, name: str, value: Any

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/dupefilters.py
# Line: 46

def request_seen(self, request: Request) -> bool:
    return False


# ==================================================
# Line: 55

def log(self, request: Request, spider: Spider) -> None:
    """Log that a request has been filtered"""
    warn(
        "Calling BaseDupeFilter.log() is deprecated.",
        ScrapyDeprecationWarning,
        stacklevel=2,
    )



# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/http/response/__init__.py
# Line: 165

def css(self, *a: Any, **kw: Any) -> SelectorList:
    """Shortcut method implemented only by responses whose content
    is text (subclasses of TextResponse).
    """
    raise NotSupported("Response content isn't text")


# ==================================================
# Line: 171

def jmespath(self, *a: Any, **kw: Any) -> SelectorList:
    """Shortcut method implemented only by responses whose content
    is text (subclasses of TextResponse).
    """
    raise NotSupported("Response content isn't text")


# ==================================================
# Line: 177

def xpath(self, *a: Any, **kw: Any) -> SelectorList:
    """Shortcut method implemented only by responses whose content
    is text (subclasses of TextResponse).
    """
    raise NotSupported("Response content isn't text")


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/pqueues.py
# Line: 143

def priority(self, request: Request) -> int:
    return -request.priority


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/logformatter.py
# Line: 75

def crawled(
    self, request: Request, response: Response, spider: Spider

# ==================================================
# Line: 95

def scraped(
    self, item: Any, response: Response | Failure | None, spider: Spider

# ==================================================
# Line: 115

def dropped(
    self,
    item: Any,
    exception: BaseException,
    response: Response | Failure | None,
    spider: Spider,

# ==================================================
# Line: 136

def item_error(
    self,
    item: Any,
    exception: BaseException,
    response: Response | Failure | None,
    spider: Spider,

# ==================================================
# Line: 156

def spider_error(
    self,
    failure: Failure,
    request: Request,
    response: Response | Failure,
    spider: Spider,

# ==================================================
# Line: 176

def download_error(
    self,
    failure: Failure,
    request: Request,
    spider: Spider,
    errmsg: str | None = None,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/mail.py
# Line: 169

def _sent_ok(
    self, result: Any, to: list[str], cc: list[str], subject: str, nattachs: int

# ==================================================
# Line: 183

def _sent_failed(
    self,
    failure: Failure,
    to: list[str],
    cc: list[str],
    subject: str,
    nattachs: int,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/spiderloader.py
# Occurrences: Lines 142-148 (3 instances)

def load(self, spider_name: str) -> type[Spider]:
    raise KeyError("DummySpiderLoader doesn't load any spiders")


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/resolver.py
# Line: 68

def _cache_result(self, result: Any, name: str) -> Any:
    dnscache[name] = result
    return result



# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/extensions/debug.py
# Line: 61

def _thread_stacks(self) -> str:
    id2name = {th.ident: th.name for th in threading.enumerate()}
    dumps = ""
    for id_, frame in sys._current_frames().items():
        name = id2name.get(id_, "")
        dump = "".join(traceback.format_stack(frame))
        dumps += f"# Thread: {name}({id_})\n{dump}\n"
    return dumps



# ==================================================
# Line: 77

def _enter_debugger(self, signum: int, frame: FrameType | None) -> None:
    assert frame
    Pdb().set_trace(frame.f_back)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/extensions/telnet.py
# Line: 78

def protocol(self) -> telnet.TelnetTransport:
    # these import twisted.internet.reactor
    from twisted.conch import manhole, telnet
    from twisted.conch.insults import insults

    class Portal:
        """An implementation of IPortal"""

        @defers
        def login(self_, credentials, mind, *interfaces):  # pylint: disable=no-self-argument
            if not (
                credentials.username == self.username.encode("utf8")
                and credentials.checkPassword(self.password.encode("utf8"))
            ):
                raise ValueError("Invalid credentials")

            protocol = telnet.TelnetBootstrapProtocol(
                insults.ServerProtocol, manhole.Manhole, self._get_telnet_vars()
            )
            return (interfaces[0], protocol, lambda: None)

    return telnet.TelnetTransport(telnet.AuthenticatingTelnetProtocol, Portal())


# ==================================================
# Line: 87

def login(self_, credentials, mind, *interfaces):  # pylint: disable=no-self-argument
    if not (
        credentials.username == self.username.encode("utf8")
        and credentials.checkPassword(self.password.encode("utf8"))
    ):
        raise ValueError("Invalid credentials")

    protocol = telnet.TelnetBootstrapProtocol(
        insults.ServerProtocol, manhole.Manhole, self._get_telnet_vars()
    )
    return (interfaces[0], protocol, lambda: None)


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/extensions/httpcache.py
# Occurrences: Lines 51-56 (2 instances)

def is_cached_response_fresh(
    self, cachedresponse: Response, request: Request

# ==================================================
# Line: 178

def _set_conditional_validators(
    self, request: Request, cachedresponse: Response

# ==================================================
# Line: 189

def _get_max_age(self, cc: dict[bytes, bytes | None]) -> int | None:
    try:
        return max(0, int(cc[b"max-age"]))  # type: ignore[arg-type]
    except (KeyError, ValueError):
        return None


# ==================================================
# Line: 228

def _compute_current_age(
    self, response: Response, request: Request, now: float

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/extensions/postprocessing.py
# Line: 159

def _load_plugins(self, plugins: list[Any]) -> list[Any]:
    return [load_object(plugin) for plugin in plugins]


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/extensions/periodic_log.py
# Line: 148

def param_allowed(
    self, stat_name: str, include: list[str], exclude: list[str]

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/extensions/feedexport.py
# Line: 144

def open(self, spider: Spider) -> IO[bytes]:
    path = spider.crawler.settings["FEED_TEMPDIR"]
    if path and not Path(path).is_dir():
        raise OSError("Not a Directory: " + str(path))

    return NamedTemporaryFile(prefix="feed-", dir=path)


# ==================================================
# Line: 200

def store(self, file: IO[bytes]) -> Deferred[None] | None:
    file.close()
    return None



# ==================================================
# Line: 718

def _get_uri_params(
    self,
    spider: Spider,
    uri_params_function: str | UriParamsCallableT | None,
    slot: FeedSlot | None = None,

# ==================================================
# Line: 739

def _load_filter(self, feed_options: dict[str, Any]) -> ItemFilter:
    # load the item filter if declared else load the default filter class
    item_filter_class: type[ItemFilter] = load_object(
        feed_options.get("item_filter", ItemFilter)
    )
    return item_filter_class(feed_options)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/contracts/__init__.py
# Line: 88

def adjust_request_args(self, args: dict[str, Any]) -> dict[str, Any]:
    return args



# ==================================================
# Line: 99

def tested_methods_from_spidercls(self, spidercls: type[Spider]) -> list[str]:
    is_method = re.compile(r"^\s*@", re.MULTILINE).search
    methods = []
    for key, value in getmembers(spidercls):
        if callable(value) and value.__doc__ and is_method(value.__doc__):
            methods.append(key)

    return methods


# ==================================================
# Line: 172

def _clean_req(
    self, request: Request, method: Callable, results: TestResult

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/engine.py
# Line: 122

def _get_scheduler_class(self, settings: BaseSettings) -> type[BaseScheduler]:
    from scrapy.core.scheduler import BaseScheduler

    scheduler_cls: type[BaseScheduler] = load_object(settings["SCHEDULER"])
    if not issubclass(scheduler_cls, BaseScheduler):
        raise TypeError(
            f"The provided scheduler class ({settings['SCHEDULER']})"
            " does not fully implement the scheduler interface"
        )
    return scheduler_cls


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/http2/agent.py
# Line: 139

def get_key(self, uri: URI) -> ConnectionKeyT:
    """
    Arguments:
        uri - URI obtained directly from request URL
    """
    return uri.scheme, uri.host, uri.port


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/http2/protocol.py
# Line: 452

def acceptableProtocols(self) -> list[bytes]:
    return [PROTOCOL_NAME]

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/scheduler.py
# Line: 300

def _get_start_queue_cls(
    self, crawler: Crawler | None, queue: str

# ==================================================
# Line: 480

def _dqdir(self, jobdir: str | None) -> str | None:
    """Return a folder name to keep disk queue state at"""
    if jobdir:
        dqdir = Path(jobdir, "requests.queue")
        if not dqdir.exists():
            dqdir.mkdir(parents=True)
        return str(dqdir)
    return None


# ==================================================
# Line: 489

def _read_dqs_state(self, dqdir: str) -> list[int]:
    path = Path(dqdir, "active.json")
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return cast(list[int], json.load(f))


# ==================================================
# Line: 496

def _write_dqs_state(self, dqdir: str, state: list[int]) -> None:
    with Path(dqdir, "active.json").open("w", encoding="utf-8") as f:
        json.dump(state, f)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/downloader/handlers/datauri.py
# Line: 19

def download_request(self, request: Request, spider: Spider) -> Response:
    uri = parse_data_uri(request.url)
    respcls = responsetypes.from_mimetype(uri.media_type)

    resp_kwargs: dict[str, Any] = {}
    if issubclass(respcls, TextResponse) and uri.media_type.split("/")[0] == "text":
        charset = uri.media_type_parameters.get("charset")
        resp_kwargs["encoding"] = charset

    return respcls(url=request.url, body=uri.data, **resp_kwargs)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/downloader/handlers/http11.py
# Line: 456

def _cb_latency(self, result: _T, request: Request, start_time: float) -> _T:
    request.meta["download_latency"] = time() - start_time
    return result


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/downloader/handlers/file.py
# Line: 20

def download_request(self, request: Request, spider: Spider) -> Response:
    filepath = file_uri_to_path(request.url)
    body = Path(filepath).read_bytes()
    respcls = responsetypes.from_args(filename=filepath, body=body)
    return respcls(url=request.url, body=body)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/downloader/webclient.py
# Line: 185

def _cancelTimeout(self, result, timeoutCall):
    if timeoutCall.active():
        timeoutCall.cancel()
    return result


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/downloadermiddlewares/redirect.py
# Line: 127

def _redirect_request_using_get(
    self, request: Request, redirect_url: str

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/downloadermiddlewares/cookies.py
# Line: 52

def _process_cookies(
    self, cookies: Iterable[Cookie], *, jar: CookieJar, request: Request

# ==================================================
# Line: 125

def _format_cookie(self, cookie: VerboseCookie, request: Request) -> str | None:
    """
    Given a dict consisting of cookie components, return its string representation.
    Decode from bytes if necessary.
    """
    decoded = {}
    flags = set()
    for key in ("name", "value", "path", "domain"):
        value = cookie.get(key)
        if value is None:
            if key in ("name", "value"):
                msg = f"Invalid cookie found in request {request}: {cookie} ('{key}' is missing)"
                logger.warning(msg)
                return None
            continue
        if isinstance(value, (bool, float, int, str)):
            decoded[key] = str(value)
        else:
            assert isinstance(value, bytes)
            try:
                decoded[key] = value.decode("utf8")
            except UnicodeDecodeError:
                logger.warning(
                    "Non UTF-8 encoded cookie found in request %s: %s",
                    request,
                    cookie,
                )
                decoded[key] = value.decode("latin1", errors="replace")
    for flag in ("secure",):
        value = cookie.get(flag, _UNSET)
        if value is _UNSET or not value:
            continue
        flags.add(flag)
    cookie_str = f"{decoded.pop('name')}={decoded.pop('value')}"
    for key, value in decoded.items():  # path, domain
        cookie_str += f"; {key.capitalize()}={value}"
    for flag in flags:  # secure
        cookie_str += f"; {flag.capitalize()}"
    return cookie_str


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/downloadermiddlewares/httpcompression.py
# Line: 81

def process_request(
    self, request: Request, spider: Spider

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/downloadermiddlewares/httpproxy.py
# Line: 79

def _set_proxy_and_creds(
    self,
    request: Request,
    proxy_url: str | None,
    creds: bytes | None,
    scheme: str | None,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/downloadermiddlewares/offsite.py
# Line: 67

def get_host_regex(self, spider: Spider) -> re.Pattern[str]:
    """Override this method to implement a different offsite policy"""
    allowed_domains = getattr(spider, "allowed_domains", None)
    if not allowed_domains:
        return re.compile("")  # allow all by default
    url_pattern = re.compile(r"^https?://.*$")
    port_pattern = re.compile(r":\d+$")
    domains = []
    for domain in allowed_domains:
        if domain is None:
            continue
        if url_pattern.match(domain):
            message = (
                "allowed_domains accepts only domains, not URLs. "
                f"Ignoring URL entry {domain} in allowed_domains."
            )
            warnings.warn(message)
        elif port_pattern.search(domain):
            message = (
                "allowed_domains accepts only domains without ports. "
                f"Ignoring entry {domain} in allowed_domains."
            )
            warnings.warn(message)
        else:
            domains.append(re.escape(domain))
    regex = rf"^(.*\.)?({'|'.join(domains)})$"
    return re.compile(regex)

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/downloadermiddlewares/robotstxt.py
# Line: 128

def _logerror(self, failure: Failure, request: Request, spider: Spider) -> Failure:
    if failure.type is not IgnoreRequest:
        logger.error(
            "Error downloading %(request)s: %(f_exception)s",
            {"request": request, "f_exception": failure.value},
            exc_info=failure_to_exc_info(failure),
            extra={"spider": spider},
        )
    return failure


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/pipelines/images.py
# Line: 264

def thumb_path(
    self,
    request: Request,
    thumb_id: str,
    response: Response | None = None,
    info: MediaPipeline.SpiderInfo | None = None,
    *,
    item: Any = None,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/pipelines/media.py
# Line: 213

def _log_exception(self, result: Failure) -> Failure:
    logger.exception(result)
    return result


# ==================================================
# Line: 242

def _cache_result_and_execute_waiters(
    self, result: FileInfo | Failure, fp: bytes, info: SpiderInfo

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/pipelines/files.py
# Line: 235

def _headers_to_botocore_kwargs(self, headers: dict[str, Any]) -> dict[str, Any]:
    """Convert headers to botocore keyword arguments."""
    # This is required while we need to support both boto and botocore.
    mapping = CaseInsensitiveDict(
        {
            "Content-Type": "ContentType",
            "Cache-Control": "CacheControl",
            "Content-Disposition": "ContentDisposition",
            "Content-Encoding": "ContentEncoding",
            "Content-Language": "ContentLanguage",
            "Content-Length": "ContentLength",
            "Content-MD5": "ContentMD5",
            "Expires": "Expires",
            "X-Amz-Grant-Full-Control": "GrantFullControl",
            "X-Amz-Grant-Read": "GrantRead",
            "X-Amz-Grant-Read-ACP": "GrantReadACP",
            "X-Amz-Grant-Write-ACP": "GrantWriteACP",
            "X-Amz-Object-Lock-Legal-Hold": "ObjectLockLegalHoldStatus",
            "X-Amz-Object-Lock-Mode": "ObjectLockMode",
            "X-Amz-Object-Lock-Retain-Until-Date": "ObjectLockRetainUntilDate",
            "X-Amz-Request-Payer": "RequestPayer",
            "X-Amz-Server-Side-Encryption": "ServerSideEncryption",
            "X-Amz-Server-Side-Encryption-Aws-Kms-Key-Id": "SSEKMSKeyId",
            "X-Amz-Server-Side-Encryption-Context": "SSEKMSEncryptionContext",
            "X-Amz-Server-Side-Encryption-Customer-Algorithm": "SSECustomerAlgorithm",
            "X-Amz-Server-Side-Encryption-Customer-Key": "SSECustomerKey",
            "X-Amz-Server-Side-Encryption-Customer-Key-Md5": "SSECustomerKeyMD5",
            "X-Amz-Storage-Class": "StorageClass",
            "X-Amz-Tagging": "Tagging",
            "X-Amz-Website-Redirect-Location": "WebsiteRedirectLocation",
        }
    )
    extra: dict[str, Any] = {}
    for key, value in headers.items():
        try:
            kwarg = mapping[key]
        except KeyError:
            raise TypeError(f'Header "{key}" is not supported by botocore')
        extra[kwarg] = value
    return extra



# ==================================================
# Line: 324

def _get_content_type(self, headers: dict[str, str] | None) -> str:
    if headers and "Content-Type" in headers:
        return headers["Content-Type"]
    return "application/octet-stream"


# ==================================================
# Line: 695

def inc_stats(self, spider: Spider, status: str) -> None:
    assert spider.crawler.stats
    spider.crawler.stats.inc_value("file_count", spider=spider)
    spider.crawler.stats.inc_value(f"file_status_count/{status}", spider=spider)


# ==================================================
