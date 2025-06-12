# no-self-use snippets for pytest

# File: /root/ecooptimizer/pytest/src/_pytest/logging.py
# Line: 495

def _force_enable_logging(
    self, level: int | str, logger_obj: logging.Logger

# ==================================================
# Line: 711

def _disable_loggers(self, loggers_to_disable: list[str]) -> None:
    if not loggers_to_disable:
        return

    for name in loggers_to_disable:
        logger = logging.getLogger(name)
        logger.disabled = True


# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/fixtures.py
# Line: 1135

def cache_key(self, request: SubRequest) -> object:
    return getattr(request, "param", None)


# ==================================================
# Line: 1220

def __post_init__(self, _ispytest: bool) -> None:
    check_ispytest(_ispytest)


# ==================================================
# Line: 1613

def _getusefixturesnames(self, node: nodes.Item) -> Iterator[str]:
    """Return the names of usefixtures fixtures applicable to node."""
    for marker_node, mark in node.iter_markers_with_node(name="usefixtures"):
        if not mark.args:
            marker_node.warn(
                PytestWarning(
                    f"usefixtures() in {node.nodeid} without arguments has no effect"
                )
            )
        yield from mark.args


# ==================================================
# Line: 1666

def pytest_generate_tests(self, metafunc: Metafunc) -> None:
    """Generate new tests based on parametrized fixtures used by the given metafunc"""

    def get_parametrize_mark_argnames(mark: Mark) -> Sequence[str]:
        args, _ = ParameterSet._parse_parametrize_args(*mark.args, **mark.kwargs)
        return args

    for argname in metafunc.fixturenames:
        # Get the FixtureDefs for the argname.
        fixture_defs = metafunc._arg2fixturedefs.get(argname)
        if not fixture_defs:
            # Will raise FixtureLookupError at setup time if not parametrized somewhere
            # else (e.g @pytest.mark.parametrize)
            continue

        # If the test itself parametrizes using this argname, give it
        # precedence.
        if any(
            argname in get_parametrize_mark_argnames(mark)
            for mark in metafunc.definition.iter_markers("parametrize")
        ):
            continue

        # In the common case we only look at the fixture def with the
        # closest scope (last in the list). But if the fixture overrides
        # another fixture, while requesting the super fixture, keep going
        # in case the super fixture is parametrized (#1953).
        for fixturedef in reversed(fixture_defs):
            # Fixture is parametrized, apply it and stop.
            if fixturedef.params is not None:
                metafunc.parametrize(
                    argname,
                    fixturedef.params,
                    indirect=True,
                    scope=fixturedef.scope,
                    ids=fixturedef.ids,
                )
                break

            # Not requesting the overridden super fixture, stop.
            if argname not in fixturedef.argnames:
                break

            # Try next super fixture, if any.


# ==================================================
# Line: 1711

def pytest_collection_modifyitems(self, items: list[nodes.Item]) -> None:
    # Separate parametrized setups.
    items[:] = reorder_items(items)


# ==================================================
# Line: 1872

def _matchfactories(
    self, fixturedefs: Iterable[FixtureDef[Any]], node: nodes.Node

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/assertion/rewrite.py
# Line: 289

def get_data(self, pathname: str | bytes) -> bytes:
    """Optional PEP302 get_data API."""
    with open(pathname, "rb") as f:
        return f.read()


# ==================================================
# Line: 805

def helper(self, name: str, *args: ast.expr) -> ast.expr:
    """Call a helper in this module."""
    py_name = ast.Name("@pytest_ar", ast.Load())
    attr = ast.Attribute(py_name, name, ast.Load())
    return ast.Call(attr, list(args), [])


# ==================================================
# Line: 811

def builtin(self, name: str) -> ast.Attribute:
    """Return the builtin called *name*."""
    builtin_name = ast.Name("@py_builtins", ast.Load())
    return ast.Attribute(builtin_name, name, ast.Load())


# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/_code/code.py
# Line: 173

def repr(self, object: object) -> str:
    """Return a 'safe' (non-recursive, one-line) string repr for 'object'."""
    return saferepr(object)


# ==================================================
# Line: 887

def _getindent(self, source: Source) -> int:
    # Figure out indent for the given source.
    try:
        s = str(source.getstatement(len(source) - 1))
    except KeyboardInterrupt:
        raise
    except BaseException:
        try:
            s = str(source[-1])
        except KeyboardInterrupt:
            raise
        except BaseException:
            return 0
    return 4 + (len(s) - len(s.lstrip()))


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
# Line: 1140

def _truncate_recursive_traceback(
    self, traceback: Traceback

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/nodes.py
# Line: 405

def _traceback_filter(self, excinfo: ExceptionInfo[BaseException]) -> Traceback:
    return excinfo.traceback


# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/debugging.py
# Line: 288

def pytest_exception_interact(
    self, node: Node, call: CallInfo[Any], report: BaseReport

# ==================================================
# Line: 302

def pytest_internalerror(self, excinfo: ExceptionInfo[BaseException]) -> None:
    exc_or_tb = _postmortem_exc_or_tb(excinfo)
    post_mortem(exc_or_tb)



# ==================================================
# Line: 309

def pytest_pyfunc_call(self, pyfuncitem) -> Generator[None, object, object]:
    wrap_pytest_function_for_tracing(pyfuncitem)
    return (yield)



# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/mark/expression.py
# Line: 89

def lex(self, input: str) -> Iterator[Token]:
    pos = 0
    while pos < len(input):
        if input[pos] in (" ", "\t"):
            pos += 1
        elif input[pos] == "(":
            yield Token(TokenType.LPAREN, "(", pos)
            pos += 1
        elif input[pos] == ")":
            yield Token(TokenType.RPAREN, ")", pos)
            pos += 1
        elif input[pos] == "=":
            yield Token(TokenType.EQUAL, "=", pos)
            pos += 1
        elif input[pos] == ",":
            yield Token(TokenType.COMMA, ",", pos)
            pos += 1
        elif (quote_char := input[pos]) in ("'", '"'):
            end_quote_pos = input.find(quote_char, pos + 1)
            if end_quote_pos == -1:
                raise ParseError(
                    pos + 1,
                    f'closing quote "{quote_char}" is missing',
                )
            value = input[pos : end_quote_pos + 1]
            if (backslash_pos := input.find("\\")) != -1:
                raise ParseError(
                    backslash_pos + 1,
                    r'escaping with "\" not supported in marker expression',
                )
            yield Token(TokenType.STRING, value, pos)
            pos += len(value)
        else:
            match = re.match(r"(:?\w|:|\+|-|\.|\[|\]|\\|/)+", input[pos:])
            if match:
                value = match.group(0)
                if value == "or":
                    yield Token(TokenType.OR, value, pos)
                elif value == "and":
                    yield Token(TokenType.AND, value, pos)
                elif value == "not":
                    yield Token(TokenType.NOT, value, pos)
                else:
                    yield Token(TokenType.IDENT, value, pos)
                pos += len(value)
            else:
                raise ParseError(
                    pos + 1,
                    f'unexpected character "{input[pos]}"',
                )
    yield Token(TokenType.EOF, "", pos)


# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/config/__init__.py
# Line: 1625

def _getini_unknown_type(self, name: str, type: str, value: object):
    msg = (
        f"Option {name} has unknown configuration type {type} with value {value!r}"
    )
    raise ValueError(msg)  # pragma: no cover


# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/cacheprovider.py
# Line: 463

def _get_increasing_order(self, items: Iterable[nodes.Item]) -> list[nodes.Item]:
    return sorted(items, key=lambda item: item.path.stat().st_mtime, reverse=True)


# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/pytester.py
# Line: 122

def get_open_files(self) -> list[tuple[str, str]]:
    if sys.version_info >= (3, 11):
        # New in Python 3.11, ignores utf-8 mode
        encoding = locale.getencoding()
    else:
        encoding = locale.getpreferredencoding(False)
    out = subprocess.run(
        ("lsof", "-Ffn0", "-p", str(os.getpid())),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=True,
        text=True,
        encoding=encoding,
    ).stdout

    def isopen(line: str) -> bool:
        return line.startswith("f") and (
            "deleted" not in line
            and "mem" not in line
            and "txt" not in line
            and "cwd" not in line
        )

    open_files = []

    for line in out.split("\n"):
        if isopen(line):
            fields = line.split("\0")
            fd = fields[0][1:]
            filename = fields[1][1:]
            if filename in IGNORE_PAM:
                continue
            if filename.startswith("/"):
                open_files.append((fd, filename))

    return open_files


# ==================================================
# Line: 159

def matching_platform(self) -> bool:
    try:
        subprocess.run(("lsof", "-v"), check=True)
    except (OSError, subprocess.CalledProcessError):
        return False
    else:
        return True


# ==================================================
# Line: 728

def __take_sys_modules_snapshot(self) -> SysModulesSnapshot:
    # Some zope modules used by twisted-related tests keep internal state
    # and can't be deleted; we had some trouble in the past with
    # `zope.interface` for example.
    #
    # Preserve readline due to https://bugs.python.org/issue41033.
    # pexpect issues a SIGWINCH.
    def preserve_module(name):
        return name.startswith(("zope", "readline"))

    return SysModulesSnapshot(preserve=preserve_module)


# ==================================================
# Line: 977

def getnode(self, config: Config, arg: str | os.PathLike[str]) -> Collector | Item:
    """Get the collection node of a file.

    :param config:
       A pytest config.
       See :py:meth:`parseconfig` and :py:meth:`parseconfigure` for creating it.
    :param arg:
        Path to the file.
    :returns:
        The node.
    """
    session = Session.from_config(config)
    assert "::" not in str(arg)
    p = Path(os.path.abspath(arg))
    config.hook.pytest_sessionstart(session=session)
    res = session.perform_collect([str(p)], genitems=False)[0]
    config.hook.pytest_sessionfinish(session=session, exitstatus=ExitCode.OK)
    return res


# ==================================================
# Line: 1016

def genitems(self, colitems: Sequence[Item | Collector]) -> list[Item]:
    """Generate all test items from a collection node.

    This recurses into the collection node and returns a list of all the
    test items contained within.

    :param colitems:
        The collection nodes.
    :returns:
        The collected items.
    """
    session = colitems[0].session
    result: list[Item] = []
    for colitem in colitems:
        result.extend(session.genitems(colitem))
    return result


# ==================================================
# Line: 1451

def _dump_lines(self, lines, fp):
    try:
        for line in lines:
            print(line, file=fp)
    except UnicodeEncodeError:
        print(f"couldn't print to {fp} because of encoding")


# ==================================================
# Line: 1458

def _getpytestargs(self) -> tuple[str, ...]:
    return sys.executable, "-mpytest"


# ==================================================
# Line: 1568

def _getlines(self, lines2: str | Sequence[str] | Source) -> Sequence[str]:
    if isinstance(lines2, str):
        lines2 = Source(lines2)
    if isinstance(lines2, Source):
        lines2 = lines2.strip().lines
    return lines2


# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/capture.py
# Line: 228

def read(self, size: int = -1) -> str:
    raise OSError(
        "pytest: reading from stdin while output is captured!  Consider using `-s`."
    )


# ==================================================
# Line: 238

def readlines(self, hint: int | None = -1) -> list[str]:
    raise OSError(
        "pytest: reading from stdin while output is captured!  Consider using `-s`."
    )


# ==================================================
# Occurrences: Lines 246-252 (3 instances)

def fileno(self) -> int:
    raise UnsupportedOperation("redirected stdin is pseudofile, has no fileno()")


# ==================================================
# Occurrences: Lines 258-279 (8 instances)

def readable(self) -> bool:
    return False


# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/_io/terminalwriter.py
# Line: 204

def _get_pygments_lexer(self, lexer: Literal["python", "diff"]) -> Lexer:
    if lexer == "python":
        return PythonLexer()
    elif lexer == "diff":
        return DiffLexer()
    else:
        assert_never(lexer)


# ==================================================
# Line: 212

def _get_pygments_formatter(self) -> TerminalFormatter:
    from _pytest.config.exceptions import UsageError

    theme = os.getenv("PYTEST_THEME")
    theme_mode = os.getenv("PYTEST_THEME_MODE", "dark")

    try:
        return TerminalFormatter(bg=theme_mode, style=theme)
    except pygments.util.ClassNotFound as e:
        raise UsageError(
            f"PYTEST_THEME environment variable has an invalid value: '{theme}'. "
            "Hint: See available pygments styles with `pygmentize -L styles`."
        ) from e
    except pygments.util.OptionError as e:
        raise UsageError(
            f"PYTEST_THEME_MODE environment variable has an invalid value: '{theme_mode}'. "
            "The allowed values are 'dark' (default) and 'light'."
        ) from e


# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/_py/path.py
# Line: 540

def _sortlist(self, res, sort):
    if sort:
        if hasattr(sort, "__call__"):
            warnings.warn(
                DeprecationWarning(
                    "listdir(sort=callable) is deprecated and breaks on python3"
                ),
                stacklevel=3,
            )
            res.sort(sort)
        else:
            res.sort()


# ==================================================
# Line: 1060

def _ensuresyspath(self, ensuremode, path):
    if ensuremode:
        s = str(path)
        if ensuremode == "append":
            if s not in sys.path:
                sys.path.append(s)
        else:
            if s != sys.path[0]:
                sys.path.insert(0, s)


# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/terminal.py
# Line: 861

def pytest_report_header(self, config: Config) -> list[str]:
    result = [f"rootdir: {config.rootpath}"]

    if config.inipath:
        result.append("configfile: " + bestrelpath(config.rootpath, config.inipath))

    if config.args_source == Config.ArgsSource.TESTPATHS:
        testpaths: list[str] = config.getini("testpaths")
        result.append("testpaths: {}".format(", ".join(testpaths)))

    plugininfo = config.pluginmanager.list_plugin_distinfo()
    if plugininfo:
        result.append(
            "plugins: {}".format(", ".join(_plugin_nameversions(plugininfo)))
        )
    return result


# ==================================================
# Line: 1018

def _getfailureheadline(self, rep):
    head_line = rep.head_line
    if head_line:
        return head_line
    return "test session"  # XXX?


# ==================================================
# Line: 1024

def _getcrashline(self, rep):
    try:
        return str(rep.longrepr.reprcrash)
    except AttributeError:
        try:
            return str(rep.longrepr)[:50]
        except AttributeError:
            return ""


# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/python.py
# Line: 346

def isnosetest(self, obj: object) -> bool:
    """Look for the __test__ attribute, which is applied by the
    @nose.tools.istest decorator.
    """
    # We explicitly check for "is True" here to not mistakenly treat
    # classes with a custom __getattr__ returning something truthy (like a
    # function) as test classes.
    return safe_getattr(obj, "__test__", False) is True


# ==================================================
# Line: 1394

def _validate_ids(
    self,
    ids: Iterable[object | None],
    parametersets: Sequence[ParameterSet],
    func_name: str,

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/junitxml.py
# Line: 182

def _prepare_content(self, content: str, header: str) -> str:
    return "\n".join([header.center(80, "-"), content, ""])


# ==================================================
