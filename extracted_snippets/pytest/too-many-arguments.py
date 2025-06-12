# too-many-arguments snippets for pytest

# File: /root/ecooptimizer/pytest/src/_pytest/fixtures.py
# Line: 982

def __init__(
    self,
    config: Config,
    baseid: str | None,
    argname: str,
    func: _FixtureFunc[FixtureValue],
    scope: Scope | _ScopeName | Callable[[str, Config], _ScopeName] | None,
    params: Sequence[object] | None,
    ids: tuple[object | None, ...] | Callable[[Any], object | None] | None = None,
    *,
    _ispytest: bool = False,
    # only used in a deprecationwarning msg, can be removed in pytest9
    _autouse: bool = False,

# ==================================================
# Line: 1715

def _register_fixture(
    self,
    *,
    name: str,
    func: _FixtureFunc[object],
    nodeid: str | None,
    scope: Scope | _ScopeName | Callable[[str, Config], _ScopeName] = "function",
    params: Sequence[object] | None = None,
    ids: tuple[object | None, ...] | Callable[[Any], object | None] | None = None,
    autouse: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/_code/code.py
# Line: 695

def getrepr(
    self,
    showlocals: bool = False,
    style: TracebackStyle = "long",
    abspath: bool = False,
    tbfilter: bool | Callable[[ExceptionInfo[BaseException]], Traceback] = True,
    funcargs: bool = False,
    truncate_locals: bool = True,
    truncate_args: bool = True,
    chain: bool = True,

# ==================================================
# Line: 920

def get_source(
    self,
    source: Source | None,
    line_index: int = -1,
    excinfo: ExceptionInfo[BaseException] | None = None,
    short: bool = False,
    end_line_index: int | None = None,
    colno: int | None = None,
    end_colno: int | None = None,

# ==================================================
# Line: 973

def get_highlight_arrows_for_line(
    self,
    line: str,
    raw_line: str,
    lineno: int | None,
    end_lineno: int | None,
    colno: int | None,
    end_colno: int | None,

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/runner.py
# Line: 291

def __init__(
    self,
    result: TResult | None,
    excinfo: ExceptionInfo[BaseException] | None,
    start: float,
    stop: float,
    duration: float,
    when: Literal["collect", "setup", "call", "teardown"],
    *,
    _ispytest: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/reports.py
# Line: 268

def __init__(
    self,
    nodeid: str,
    location: tuple[str, int | None, str],
    keywords: Mapping[str, Any],
    outcome: Literal["passed", "failed", "skipped"],
    longrepr: None
    | ExceptionInfo[BaseException]
    | tuple[str, int, str]
    | str
    | TerminalRepr,
    when: Literal["setup", "call", "teardown"],
    sections: Iterable[tuple[str, str]] = (),
    duration: float = 0,
    start: float = 0,
    stop: float = 0,
    user_properties: Iterable[tuple[str, object]] | None = None,
    **extra,

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/nodes.py
# Line: 156

def __init__(
    self,
    name: str,
    parent: Node | None = None,
    config: Config | None = None,
    session: Session | None = None,
    fspath: LEGACY_PATH | None = None,
    path: Path | None = None,
    nodeid: str | None = None,

# ==================================================
# Line: 563

def __init__(
    self,
    fspath: LEGACY_PATH | None = None,
    path_or_parent: Path | Node | None = None,
    path: Path | None = None,
    name: str | None = None,
    parent: Node | None = None,
    config: Config | None = None,
    session: Session | None = None,
    nodeid: str | None = None,

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/config/__init__.py
# Line: 547

def _set_initial_conftests(
    self,
    args: Sequence[str | pathlib.Path],
    pyargs: bool,
    noconftest: bool,
    rootpath: pathlib.Path,
    confcutdir: pathlib.Path | None,
    invocation_dir: pathlib.Path,
    importmode: ImportMode | str,
    *,
    consider_namespace_packages: bool,

# ==================================================
# Line: 1340

def _decide_args(
    self,
    *,
    args: list[str],
    pyargs: bool,
    testpaths: list[str],
    invocation_dir: pathlib.Path,
    rootpath: pathlib.Path,
    warn: bool,

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/doctest.py
# Line: 535

def _find(
    self, tests, obj, name, module, source_lines, globs, seen

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/pytester.py
# Line: 592

def assert_outcomes(
    self,
    passed: int = 0,
    skipped: int = 0,
    failed: int = 0,
    errors: int = 0,
    xpassed: int = 0,
    xfailed: int = 0,
    warnings: int | None = None,
    deselected: int | None = None,

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/_io/pprint.py
# Line: 94

def _format(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 130

def _pprint_dataclass(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 154

def _pprint_dict(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 171

def _pprint_ordered_dict(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 190

def _pprint_list(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 205

def _pprint_tuple(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 220

def _pprint_set(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 246

def _pprint_str(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 305

def _pprint_bytes(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 334

def _pprint_bytearray(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 352

def _pprint_mappingproxy(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 367

def _pprint_simplenamespace(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 389

def _format_dict_items(
    self,
    items: list[tuple[Any, Any]],
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 413

def _format_namespace_items(
    self,
    items: list[tuple[Any, Any]],
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 450

def _format_items(
    self,
    items: list[Any],
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 476

def _pprint_default_dict(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 492

def _pprint_counter(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 513

def _pprint_chain_map(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 532

def _pprint_deque(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 551

def _pprint_user_dict(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 564

def _pprint_user_list(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# Line: 577

def _pprint_user_string(
    self,
    object: Any,
    stream: IO[str],
    indent: int,
    allowance: int,
    context: set[int],
    level: int,

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/pytester_assertions.py
# Line: 37

def assert_outcomes(
    outcomes: dict[str, int],
    passed: int = 0,
    skipped: int = 0,
    failed: int = 0,
    errors: int = 0,
    xpassed: int = 0,
    xfailed: int = 0,
    warnings: int | None = None,
    deselected: int | None = None,

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/python.py
# Line: 644

def __init__(
    self,
    fspath: LEGACY_PATH | None,
    parent: nodes.Collector,
    # NOTE: following args are unused:
    config=None,
    session=None,
    nodeid=None,
    path: Path | None = None,

# ==================================================
# Line: 1067

def setmulti(
    self,
    *,
    argnames: Iterable[str],
    valset: Iterable[object],
    id: str | _HiddenParam,
    marks: Iterable[Mark | MarkDecorator],
    scope: Scope,
    param_index: int,
    nodeid: str,

# ==================================================
# Line: 1569

def __init__(
    self,
    name: str,
    parent,
    config: Config | None = None,
    callspec: CallSpec2 | None = None,
    callobj=NOTSET,
    keywords: Mapping[str, Any] | None = None,
    session: Session | None = None,
    fixtureinfo: FuncFixtureInfo | None = None,
    originalname: str | None = None,

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/junitxml.py
# Line: 459

def __init__(
    self,
    logfile,
    prefix: str | None,
    suite_name: str = "pytest",
    logging: str = "no",
    report_duration: str = "total",
    family="xunit1",
    log_passing_tests: bool = True,

# ==================================================
