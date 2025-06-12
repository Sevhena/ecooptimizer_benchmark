# string-concat-loop snippets for pytest

# File: /root/ecooptimizer/pytest/src/_pytest/assertion/util.py
# Line: 518

for k in diff:
    explanation += [
        highlighter(saferepr({k: left[k]}))
        + " != "
        + highlighter(saferepr({k: right[k]}))
    ]

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/_code/code.py
# Line: 1209

while e is not None and id(e) not in seen:
    seen.add(id(e))

    if excinfo_:
        # Fall back to native traceback as a temporary workaround until
        # full support for exception groups added to ExceptionInfo.
        # See https://github.com/pytest-dev/pytest/issues/9159
        reprtraceback: ReprTraceback | ReprTracebackNative
        if isinstance(e, BaseExceptionGroup):
            # don't filter any sub-exceptions since they shouldn't have any internal frames
            traceback = filter_excinfo_traceback(self.tbfilter, excinfo)
            reprtraceback = ReprTracebackNative(
                format_exception(
                    type(excinfo.value),
                    excinfo.value,
                    traceback[0]._rawentry,
                )
            )
        else:
            reprtraceback = self.repr_traceback(excinfo_)
        reprcrash = excinfo_._getreprcrash()
    else:
        # Fallback to native repr if the exception doesn't have a traceback:
        # ExceptionInfo objects require a full traceback to work.
        reprtraceback = ReprTracebackNative(format_exception(type(e), e, None))
        reprcrash = None
    repr_chain += [(reprtraceback, reprcrash, descr)]

    if e.__cause__ is not None and self.chain:
        e = e.__cause__
        excinfo_ = ExceptionInfo.from_exception(e) if e.__traceback__ else None
        descr = "The above exception was the direct cause of the following exception:"
    elif (
        e.__context__ is not None and not e.__suppress_context__ and self.chain
    ):
        e = e.__context__
        excinfo_ = ExceptionInfo.from_exception(e) if e.__traceback__ else None
        descr = "During handling of the above exception, another exception occurred:"
    else:
        e = None

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/_py/path.py
# Line: 743

for arg in strargs:
    arg = arg.strip(sep)
    if iswin32:
        # allow unix style paths even on windows.
        arg = arg.strip("/")
        arg = arg.replace("/", sep)
    strpath = strpath + actual_sep + arg
    actual_sep = sep

# ==================================================
