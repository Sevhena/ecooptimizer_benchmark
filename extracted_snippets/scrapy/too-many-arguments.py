# too-many-arguments snippets for scrapy

# File: /root/ecooptimizer/scrapy/scrapy/spiders/crawl.py
# Line: 61

def __init__(
    self,
    link_extractor: LinkExtractor | None = None,
    callback: CallbackT | str | None = None,
    cb_kwargs: dict[str, Any] | None = None,
    follow: bool | None = None,
    process_links: ProcessLinksT | str | None = None,
    process_request: ProcessRequestT | str | None = None,
    errback: Callable[[Failure], Any] | str | None = None,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/utils/ftp.py
# Line: 21

def ftp_store_file(
    *,
    path: str,
    file: IO[bytes],
    host: str,
    port: int,
    username: str,
    password: str,
    use_active_mode: bool = False,
    overwrite: bool = True,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/utils/deprecate.py
# Line: 22

def create_deprecated_class(
    name: str,
    new_class: type,
    clsdict: dict[str, Any] | None = None,
    warn_category: type[Warning] = ScrapyDeprecationWarning,
    warn_once: bool = True,
    old_class_path: str | None = None,
    new_class_path: str | None = None,
    subclass_warn_message: str = "{cls} inherits from deprecated class {old}, please inherit from {new}.",
    instance_warn_message: str = "{cls} is deprecated, instantiate {new} instead.",

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/http/response/__init__.py
# Line: 59

def __init__(
    self,
    url: str,
    status: int = 200,
    headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
    body: bytes = b"",
    flags: list[str] | None = None,
    request: Request | None = None,
    certificate: Certificate | None = None,
    ip_address: IPv4Address | IPv6Address | None = None,
    protocol: str | None = None,

# ==================================================
# Line: 183

def follow(
    self,
    url: str | Link,
    callback: CallbackT | None = None,
    method: str = "GET",
    headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
    body: bytes | str | None = None,
    cookies: CookiesT | None = None,
    meta: dict[str, Any] | None = None,
    encoding: str | None = "utf-8",
    priority: int = 0,
    dont_filter: bool = False,
    errback: Callable[[Failure], Any] | None = None,
    cb_kwargs: dict[str, Any] | None = None,
    flags: list[str] | None = None,

# ==================================================
# Line: 236

def follow_all(
    self,
    urls: Iterable[str | Link],
    callback: CallbackT | None = None,
    method: str = "GET",
    headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
    body: bytes | str | None = None,
    cookies: CookiesT | None = None,
    meta: dict[str, Any] | None = None,
    encoding: str | None = "utf-8",
    priority: int = 0,
    dont_filter: bool = False,
    errback: Callable[[Failure], Any] | None = None,
    cb_kwargs: dict[str, Any] | None = None,
    flags: list[str] | None = None,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/http/response/text.py
# Line: 170

def follow(
    self,
    url: str | Link | parsel.Selector,
    callback: CallbackT | None = None,
    method: str = "GET",
    headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
    body: bytes | str | None = None,
    cookies: CookiesT | None = None,
    meta: dict[str, Any] | None = None,
    encoding: str | None = None,
    priority: int = 0,
    dont_filter: bool = False,
    errback: Callable[[Failure], Any] | None = None,
    cb_kwargs: dict[str, Any] | None = None,
    flags: list[str] | None = None,

# ==================================================
# Line: 223

def follow_all(
    self,
    urls: Iterable[str | Link] | parsel.SelectorList | None = None,
    callback: CallbackT | None = None,
    method: str = "GET",
    headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
    body: bytes | str | None = None,
    cookies: CookiesT | None = None,
    meta: dict[str, Any] | None = None,
    encoding: str | None = None,
    priority: int = 0,
    dont_filter: bool = False,
    errback: Callable[[Failure], Any] | None = None,
    cb_kwargs: dict[str, Any] | None = None,
    flags: list[str] | None = None,
    css: str | None = None,
    xpath: str | None = None,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/http/request/__init__.py
# Line: 111

def __init__(
    self,
    url: str,
    callback: CallbackT | None = None,
    method: str = "GET",
    headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
    body: bytes | str | None = None,
    cookies: CookiesT | None = None,
    meta: dict[str, Any] | None = None,
    encoding: str = "utf-8",
    priority: int = 0,
    dont_filter: bool = False,
    errback: Callable[[Failure], Any] | None = None,
    flags: list[str] | None = None,
    cb_kwargs: dict[str, Any] | None = None,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/http/request/form.py
# Line: 63

def from_response(
    cls,
    response: TextResponse,
    formname: str | None = None,
    formid: str | None = None,
    formnumber: int = 0,
    formdata: FormdataType = None,
    clickdata: dict[str, str | int] | None = None,
    dont_click: bool = False,
    formxpath: str | None = None,
    formcss: str | None = None,
    **kwargs: Any,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/mail.py
# Line: 56

def __init__(
    self,
    smtphost: str = "localhost",
    mailfrom: str = "scrapy@localhost",
    smtpuser: str | None = None,
    smtppass: str | None = None,
    smtpport: int = 25,
    smtptls: bool = False,
    smtpssl: bool = False,
    debug: bool = False,

# ==================================================
# Line: 101

def send(
    self,
    to: str | list[str],
    subject: str,
    body: str,
    cc: str | list[str] | None = None,
    attachs: Sequence[tuple[str, str, IO[Any]]] = (),
    mimetype: str = "text/plain",
    charset: str | None = None,
    _callback: Callable[..., None] | None = None,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/extensions/feedexport.py
# Line: 206

def __init__(
    self,
    uri: str,
    access_key: str | None = None,
    secret_key: str | None = None,
    acl: str | None = None,
    endpoint_url: str | None = None,
    *,
    feed_options: dict[str, Any] | None = None,
    session_token: str | None = None,
    region_name: str | None = None,

# ==================================================
# Line: 373

def __init__(
    self,
    storage: FeedStorageProtocol,
    uri: str,
    format: str,
    store_empty: bool,
    batch_id: int,
    uri_template: str,
    filter: ItemFilter,
    feed_options: dict[str, Any],
    spider: Spider,
    exporters: dict[str, type[BaseItemExporter]],
    settings: BaseSettings,
    crawler: Crawler,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/http2/agent.py
# Line: 162

def __init__(
    self,
    reactor: ReactorBase,
    proxy_uri: URI,
    pool: H2ConnectionPool,
    context_factory: BrowserLikePolicyForHTTPS = BrowserLikePolicyForHTTPS(),
    connect_timeout: float | None = None,
    bind_address: bytes | None = None,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/scheduler.py
# Line: 238

def __init__(
    self,
    dupefilter: BaseDupeFilter,
    jobdir: str | None = None,
    dqclass: type[BaseQueue] | None = None,
    mqclass: type[BaseQueue] | None = None,
    logunser: bool = False,
    stats: StatsCollector | None = None,
    pqclass: type[ScrapyPriorityQueue] | None = None,
    crawler: Crawler | None = None,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/downloader/handlers/s3.py
# Line: 24

def __init__(
    self,
    settings: BaseSettings,
    *,
    crawler: Crawler,
    aws_access_key_id: str | None = None,
    aws_secret_access_key: str | None = None,
    aws_session_token: str | None = None,
    httpdownloadhandler: type[HTTPDownloadHandler] = HTTPDownloadHandler,
    **kw: Any,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/core/downloader/handlers/http11.py
# Line: 147

def __init__(
    self,
    reactor: ReactorBase,
    host: str,
    port: int,
    proxyConf: tuple[str, int, bytes | None],
    contextFactory: IPolicyForHTTPS,
    timeout: float = 30,
    bindAddress: tuple[str, int] | None = None,

# ==================================================
# Line: 259

def __init__(
    self,
    *,
    reactor: ReactorBase,
    proxyConf: tuple[str, int, bytes | None],
    contextFactory: IPolicyForHTTPS,
    connectTimeout: float | None = None,
    bindAddress: bytes | None = None,
    pool: HTTPConnectionPool | None = None,

# ==================================================
# Line: 284

def _requestWithEndpoint(
    self,
    key: Any,
    endpoint: TCP4ClientEndpoint,
    method: bytes,
    parsedURI: URI,
    headers: TxHeaders | None,
    bodyProducer: IBodyProducer | None,
    requestPath: bytes,

# ==================================================
# Line: 354

def __init__(
    self,
    *,
    contextFactory: IPolicyForHTTPS,
    connectTimeout: float = 10,
    bindAddress: bytes | None = None,
    pool: HTTPConnectionPool | None = None,
    maxsize: int = 0,
    warnsize: int = 0,
    fail_on_dataloss: bool = True,
    crawler: Crawler,

# ==================================================
# Line: 602

def __init__(
    self,
    finished: Deferred[_ResultT],
    txresponse: TxResponse,
    request: Request,
    maxsize: int,
    warnsize: int,
    fail_on_dataloss: bool,
    crawler: Crawler,

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/downloadermiddlewares/retry.py
# Line: 37

def get_retry_request(
    request: Request,
    *,
    spider: Spider,
    reason: str | Exception | type[Exception] = "unspecified",
    max_retry_times: int | None = None,
    priority_adjust: int | None = None,
    logger: Logger = retry_logger,
    stats_base_key: str = "retry",

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/linkextractors/lxmlhtml.py
# Line: 61

def __init__(
    self,
    tag: str | Callable[[str], bool] = "a",
    attr: str | Callable[[str], bool] = "href",
    process: Callable[[Any], Any] | None = None,
    unique: bool = False,
    strip: bool = True,
    canonicalized: bool = False,

# ==================================================
# Line: 167

def __init__(
    self,
    allow: _RegexOrSeveralT = (),
    deny: _RegexOrSeveralT = (),
    allow_domains: str | Iterable[str] = (),
    deny_domains: str | Iterable[str] = (),
    restrict_xpaths: str | Iterable[str] = (),
    tags: str | Iterable[str] = ("a", "area"),
    attrs: str | Iterable[str] = ("href",),
    canonicalize: bool = False,
    unique: bool = True,
    process_value: Callable[[Any], Any] | None = None,
    deny_extensions: str | Iterable[str] | None = None,
    restrict_css: str | Iterable[str] = (),
    strip: bool = True,
    restrict_text: _RegexOrSeveralT | None = None,

# ==================================================
