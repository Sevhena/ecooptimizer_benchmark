# no-self-use snippets for pandas

# File: /root/ecooptimizer/pandas/doc/source/conf.py
# Line: 513

def format_signature(self) -> str:
    # this method gives an error/warning for the accessors, therefore
    # overriding it (accessor has no arguments)
    return ""



# ==================================================
# Line: 607

def _replace_pandas_items(self, display_name, sig, summary, real_name):
    # this a hack: ideally we should extract the signature from the
    # .__call__ method instead of hard coding this
    if display_name == "DataFrame.plot":
        sig = "([x, y, kind, ax, ....])"
        summary = "DataFrame plotting accessor and method"
    elif display_name == "Series.plot":
        sig = "([kind, ax, figsize, ....])"
        summary = "Series plotting accessor and method"
    return (display_name, sig, summary, real_name)


# ==================================================
# File: /root/ecooptimizer/pandas/doc/make.py
# Line: 72

def _process_single_doc(self, single_doc):
    """
    Make sure the provided value for --single is a path to an existing
    .rst/.ipynb file, or a pandas object that can be imported.

    For example, categorial.rst or pandas.DataFrame.head. For the latter,
    return the corresponding file path
    (e.g. reference/api/pandas.DataFrame.head.rst).
    """
    base_name, extension = os.path.splitext(single_doc)
    if extension in (".rst", ".ipynb"):
        if os.path.exists(os.path.join(SOURCE_PATH, single_doc)):
            return single_doc
        else:
            raise FileNotFoundError(f"File {single_doc} not found")

    elif single_doc.startswith("pandas."):
        try:
            obj = pandas  # noqa: F821
            for name in single_doc.split("."):
                obj = getattr(obj, name)
        except AttributeError as err:
            raise ImportError(f"Could not import {single_doc}") from err
        else:
            return single_doc[len("pandas.") :]
    else:
        raise ValueError(
            f"--single={single_doc} not understood. "
            "Value should be a valid path to a .rst or .ipynb file, "
            "or a valid pandas object "
            "(e.g. categorical.rst or pandas.DataFrame.head)"
        )


# ==================================================
# Line: 153

def _open_browser(self, single_doc_html) -> None:
    """
    Open a browser tab showing single
    """
    url = os.path.join("file://", DOC_PATH, "build", "html", single_doc_html)
    webbrowser.open(url, new=2)


# ==================================================
# Line: 160

def _get_page_title(self, page):
    """
    Open the rst file `page` and extract its title.
    """
    fname = os.path.join(SOURCE_PATH, f"{page}.rst")
    doc = docutils.utils.new_document(
        "<doc>",
        docutils.frontend.get_default_settings(docutils.parsers.rst.Parser),
    )
    with open(fname, encoding="utf-8") as f:
        data = f.read()

    parser = docutils.parsers.rst.Parser()
    # do not generate any warning when parsing the rst
    with open(os.devnull, "a", encoding="utf-8") as f:
        doc.reporter.stream = f
        parser.parse(data, doc)

    section = next(
        node for node in doc.children if isinstance(node, docutils.nodes.section)
    )
    title = next(
        node for node in section.children if isinstance(node, docutils.nodes.title)
    )

    return title.astext()


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/sql.py
# Line: 1415

def _get_dtype(self, sqltype):
    from sqlalchemy.types import (
        TIMESTAMP,
        Boolean,
        Date,
        DateTime,
        Float,
        Integer,
        String,
    )

    if isinstance(sqltype, Float):
        return float
    elif isinstance(sqltype, Integer):
        # TODO: Refine integer size.
        return np.dtype("int64")
    elif isinstance(sqltype, TIMESTAMP):
        # we have a timezone capable type
        if not sqltype.timezone:
            return datetime
        return DatetimeTZDtype
    elif isinstance(sqltype, DateTime):
        # Caution: np.datetime64 is also a subclass of np.number.
        return datetime
    elif isinstance(sqltype, Date):
        return date
    elif isinstance(sqltype, Boolean):
        return bool
    elif isinstance(sqltype, String):
        if using_string_dtype():
            return StringDtype(na_value=np.nan)

    return object



# ==================================================
# Line: 2510

def _register_date_adapters(self) -> None:
    # GH 8341
    # register an adapter callable for datetime.time object
    import sqlite3

    # this will transform time(12,34,56,789) into '12:34:56.000789'
    # (this is what sqlalchemy does)
    def _adapt_time(t) -> str:
        # This is faster than strftime
        return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}.{t.microsecond:06d}"

    # Also register adapters for date/datetime and co
    # xref https://docs.python.org/3.12/library/sqlite3.html#adapter-and-converter-recipes
    # Python 3.12+ doesn't auto-register adapters for us anymore

    adapt_date_iso = lambda val: val.isoformat()
    adapt_datetime_iso = lambda val: val.isoformat(" ")

    sqlite3.register_adapter(time, _adapt_time)

    sqlite3.register_adapter(date, adapt_date_iso)
    sqlite3.register_adapter(datetime, adapt_datetime_iso)

    convert_date = lambda val: date.fromisoformat(val.decode())
    convert_timestamp = lambda val: datetime.fromisoformat(val.decode())

    sqlite3.register_converter("date", convert_date)
    sqlite3.register_converter("timestamp", convert_timestamp)


# ==================================================
# Line: 2795

def _fetchall_as_list(self, cur):
    result = cur.fetchall()
    if not isinstance(result, list):
        result = list(result)
    return result


# ==================================================
# Line: 2896

def get_table(self, table_name: str, schema: str | None = None) -> None:
    return None  # not supported in fallback mode


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/html.py
# Line: 245

def _attr_getter(self, obj, attr):
    """
    Return the attribute value of an individual DOM node.

    Parameters
    ----------
    obj : node-like
        A DOM node.

    attr : str or unicode
        The attribute, such as "colspan"

    Returns
    -------
    str or unicode
        The attribute value.
    """
    # Both lxml and BeautifulSoup have the same implementation:
    return obj.get(attr)


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/parsers/base_parser.py
# Line: 261

def _maybe_make_multi_index_columns(
    self,
    columns: SequenceT,
    col_names: Sequence[Hashable] | None = None,

# ==================================================
# Line: 632

def _validate_usecols_names(self, usecols: SequenceT, names: Sequence) -> SequenceT:
    """
    Validates that all usecols are present in a given
    list of names. If not, raise a ValueError that
    shows what usecols are missing.

    Parameters
    ----------
    usecols : iterable of usecols
        The columns to validate are present in names.
    names : iterable of names
        The column names to check against.

    Returns
    -------
    usecols : iterable of usecols
        The `usecols` parameter if the validation succeeds.

    Raises
    ------
    ValueError : Columns were missing. Error message will list them.
    """
    missing = [c for c in usecols if c not in names]
    if len(missing) > 0:
        raise ValueError(
            f"Usecols do not match columns, columns expected but not found: "
            f"{missing}"
        )

    return usecols


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/parsers/python_parser.py
# Line: 871

def _is_line_empty(self, line: Sequence[Scalar]) -> bool:
    """
    Check if a line is empty or not.

    Parameters
    ----------
    line : str, array-like
        The line of data to check.

    Returns
    -------
    boolean : Whether or not the line is empty.
    """
    return not line or all(not x for x in line)


# ==================================================
# Line: 1033

def _remove_empty_lines(self, lines: list[list[T]]) -> list[list[T]]:
    """
    Iterate through the lines and remove any that are
    either empty or contain only one whitespace value

    Parameters
    ----------
    lines : list of list of Scalars
        The array of lines that we are to filter.

    Returns
    -------
    filtered_lines : list of list of Scalars
        The same array of lines with the "empty" ones removed.
    """
    # Remove empty lines and lines with only one whitespace value
    ret = [
        line
        for line in lines
        if (
            len(line) > 1
            or (
                len(line) == 1 and (not isinstance(line[0], str) or line[0].strip())
            )
        )
    ]
    return ret


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/parsers/arrow_parser_wrapper.py
# Line: 217

def _validate_usecols(self, usecols) -> None:
    if lib.is_list_like(usecols) and not all(isinstance(x, str) for x in usecols):
        raise ValueError(
            "The pyarrow engine does not allow 'usecols' to be integer "
            "column positions. Pass a list of string column names instead."
        )
    elif callable(usecols):
        raise ValueError(
            "The pyarrow engine does not allow 'usecols' to be a callable."
        )


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/pytables.py
# Line: 1804

def _validate_format(self, format: str) -> str:
    """validate / deprecate formats"""
    # validate
    try:
        format = _FORMAT_MAP[format.lower()]
    except KeyError as err:
        raise TypeError(f"invalid HDFStore format specified [{format}]") from err

    return format


# ==================================================
# Line: 2904

def validate(self, other) -> Literal[True] | None:
    """validate against an existing storable"""
    if other is None:
        return None
    return True


# ==================================================
# Line: 3013

def validate_read(self, columns, where) -> None:
    """
    raise if any keywords are passed which are not-None
    """
    if columns is not None:
        raise TypeError(
            "cannot pass a column specification when reading "
            "a Fixed format store. this store must be selected in its entirety"
        )
    if where is not None:
        raise TypeError(
            "cannot pass a where specification when reading "
            "from a Fixed format store. this store must be selected in its entirety"
        )


# ==================================================
# Line: 3605

def validate_multiindex(
    self, obj: DataFrame | Series

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/stata.py
# Line: 2533

def _validate_variable_name(self, name: str) -> str:
    """
    Validate variable names for Stata export.

    Parameters
    ----------
    name : str
        Variable name

    Returns
    -------
    str
        The validated name with invalid characters replaced with
        underscores.

    Notes
    -----
    Stata 114 and 117 support ascii characters in a-z, A-Z, 0-9
    and _.
    """
    for c in name:
        if (
            (c < "A" or c > "Z")
            and (c < "a" or c > "z")
            and (c < "0" or c > "9")
            and c != "_"
        ):
            name = name.replace(c, "_")
    return name


# ==================================================
# Line: 2986

def _convert_strls(self, data: DataFrame) -> DataFrame:
    """No-op, future compatibility"""
    return data


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/sas/sas_xport.py
# Line: 456

def _missing_double(self, vec):
    v = vec.view(dtype="u1,u1,u2,u4")
    miss = (v["f1"] == 0) & (v["f2"] == 0) & (v["f3"] == 0)
    miss1 = (
        ((v["f0"] >= 0x41) & (v["f0"] <= 0x5A))
        | (v["f0"] == 0x5F)
        | (v["f0"] == 0x2E)
    )
    miss &= miss1
    return miss


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/info.py
# Line: 647

def _initialize_max_cols(self, max_cols: int | None) -> int:
    if max_cols is None:
        return get_option("display.max_info_columns")
    return max_cols


# ==================================================
# Line: 714

def _initialize_show_counts(self, show_counts: bool | None) -> bool:
    if show_counts is None:
        return True
    else:
        return show_counts



# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/excel.py
# Line: 269

def _get_is_wrap_text(self, props: Mapping[str, str]) -> bool | None:
    if props.get("white-space") is None:
        return None
    return bool(props["white-space"] not in ("nowrap", "pre", "pre-line"))


# ==================================================
# Line: 361

def _pt_to_float(self, pt_string: str) -> float:
    assert pt_string.endswith("pt")
    return float(pt_string.rstrip("pt"))


# ==================================================
# Line: 372

def build_number_format(self, props: Mapping[str, str]) -> dict[str, str | None]:
    fc = props.get("number-format")
    fc = fc.replace("§", ";") if isinstance(fc, str) else fc
    return {"format_code": fc}


# ==================================================
# Line: 407

def _get_decoration(self, props: Mapping[str, str]) -> Sequence[str]:
    decoration = props.get("text-decoration")
    if decoration is not None:
        return decoration.split()
    else:
        return ()


# ==================================================
# Occurrences: Lines 414-424 (3 instances)

def _get_underline(self, decoration: Sequence[str]) -> str | None:
    if "underline" in decoration:
        return "single"
    return None


# ==================================================
# Line: 482

def _is_hex_color(self, color_string: str) -> bool:
    return bool(color_string.startswith("#"))


# ==================================================
# Line: 492

def _is_shorthand_color(self, color_string: str) -> bool:
    """Check if color code is shorthand.

    #FFF is a shorthand as opposed to full #FFFFFF.
    """
    code = color_string.lstrip("#")
    if len(code) == 3:
        return True
    elif len(code) == 6:
        return False
    else:
        raise ValueError(f"Unexpected color {color_string}")



# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/printing.py
# Occurrences: Lines 523-526 (2 instances)

def len(self, text: str) -> int:
    return len(text)


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/style_render.py
# Line: 2210

def _pseudo_css(
    self, uuid: str, name: str, row: int, col: int, text: str

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/format.py
# Line: 529

def _initialize_sparsify(self, sparsify: bool | None) -> bool:
    if sparsify is None:
        return get_option("display.multi_sparse")
    return sparsify


# ==================================================
# Line: 547

def _initialize_justify(self, justify: str | None) -> str:
    if justify is None:
        return get_option("display.colheader_justify")
    else:
        return justify


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/css.py
# Line: 276

def _update_initial(
    self,
    props: dict[str, str],
    inherited: dict[str, str],

# ==================================================
# Line: 318

def _get_float_font_size_from_pt(self, font_size_string: str) -> float:
    assert font_size_string.endswith("pt")
    return float(font_size_string.rstrip("pt"))


# ==================================================
# Line: 401

def parse(self, declarations_str: str) -> Iterator[tuple[str, str]]:
    """
    Generates (prop, value) pairs from declarations.

    In a future version may generate parsed tokens from tinycss/tinycss2

    Parameters
    ----------
    declarations_str : str
    """
    for decl in declarations_str.split(";"):
        if not decl.strip():
            continue
        prop, sep, val = decl.partition(":")
        prop = prop.strip().lower()
        # TODO: don't lowercase case sensitive parts of values (strings)
        val = val.strip().lower()
        if sep:
            yield prop, val
        else:
            warnings.warn(
                f"Ill-formatted attribute: expected a colon in {decl!r}",
                CSSWarning,
                stacklevel=find_stack_level(),
            )

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/interchange/column.py
# Line: 148

def _dtype_from_pandasdtype(self, dtype) -> tuple[DtypeKind, int, str, str]:
    """
    See `self.dtype` for details.
    """
    # Note: 'c' (complex) not handled yet (not in array spec v1).
    #       'b', 'B' (bytes), 'S', 'a', (old-style string) 'V' (void) not handled
    #       datetime and timedelta both map to datetime (is timedelta handled?)

    kind = _NP_KINDS.get(dtype.kind, None)
    if kind is None:
        # Not a NumPy dtype. Check if it's a categorical maybe
        raise ValueError(f"Data type {dtype} not supported by interchange protocol")
    if isinstance(dtype, ArrowDtype):
        byteorder = dtype.numpy_dtype.byteorder
    elif isinstance(dtype, DatetimeTZDtype):
        byteorder = dtype.base.byteorder  # type: ignore[union-attr]
    elif isinstance(dtype, BaseMaskedDtype):
        byteorder = dtype.numpy_dtype.byteorder
    else:
        byteorder = dtype.byteorder

    if dtype == "bool[pyarrow]":
        # return early to avoid the `* 8` below, as this is a bitmask
        # rather than a bytemask
        return (
            kind,
            dtype.itemsize,  # pyright: ignore[reportAttributeAccessIssue]
            ArrowCTypes.BOOL,
            byteorder,
        )

    return kind, dtype.itemsize * 8, dtype_to_arrow_c_fmt(dtype), byteorder


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/generic.py
# Line: 2289

def _define_paths(self, func, *args, **kwargs):
    if isinstance(func, str):
        fast_path = lambda group: getattr(group, func)(*args, **kwargs)
        slow_path = lambda group: group.apply(
            lambda x: getattr(x, func)(*args, **kwargs), axis=0
        )
    else:
        fast_path = lambda group: func(group, *args, **kwargs)
        slow_path = lambda group: group.apply(
            lambda x: func(x, *args, **kwargs), axis=0
        )
    return fast_path, slow_path


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/ops.py
# Line: 518

def _validate_axis(self, axis: AxisInt, values: ArrayLike) -> None:
    if values.ndim > 2:
        raise NotImplementedError("number of dimensions is currently limited to 2")
    if values.ndim == 2:
        assert axis == 1, axis
    elif not is_1d_only_ea_dtype(values.dtype):
        # Note: it is *not* the case that axis is always 0 for 1-dim values,
        #  as we can have 1D ExtensionArrays that we need to treat as 2D
        assert axis == 0


# ==================================================
# Line: 849

def _ob_index_and_ids(
    self,
    levels: list[Index],
    codes: list[npt.NDArray[np.intp]],
    names: list[Hashable],
    sorts: list[bool],

# ==================================================
# Line: 889

def _unob_index_and_ids(
    self,
    levels: list[Index],
    codes: list[npt.NDArray[np.intp]],
    names: list[Hashable],

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/apply.py
# Line: 726

def normalize_dictlike_arg(
    self, how: str, obj: DataFrame | Series, func: AggFuncTypeDict

# ==================================================
# Line: 772

def _apply_str(self, obj, func: str, *args, **kwargs):
    """
    if arg is a string, then try to operate on it:
    - try to find a function (or attribute) on obj
    - try to find a numpy function
    - raise
    """
    assert isinstance(func, str)

    if hasattr(obj, func):
        f = getattr(obj, func)
        if callable(f):
            return f(*args, **kwargs)

        # people may aggregate on a non-callable attribute
        # but don't let them think they can pass args to it
        assert len(args) == 0
        assert not any(kwarg == "axis" for kwarg in kwargs)
        return f
    elif hasattr(np, func) and hasattr(obj, "__array__"):
        # in particular exclude Window
        f = getattr(np, func)
        return f(obj, *args, **kwargs)
    else:
        msg = f"'{func}' is not a valid function for '{type(obj).__name__}' object"
        raise AttributeError(msg)



# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/window/rolling.py
# Line: 266

def _make_numeric_only(self, obj: NDFrameT) -> NDFrameT:
    """Subset DataFrame to numeric columns.

    Parameters
    ----------
    obj : DataFrame

    Returns
    -------
    obj subset to numeric-only columns.
    """
    result = obj.select_dtypes(include=["number"], exclude=["timedelta"])
    return result


# ==================================================
# Line: 1166

def _center_window(self, result: np.ndarray, offset: int) -> np.ndarray:
    """
    Center the result in the window for weighted rolling aggregations.
    """
    if offset > 0:
        lead_indexer = [slice(offset, None)]
        result = np.copy(result[tuple(lead_indexer)])
    return result


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/base.py
# Line: 255

def _infer_selection(self, key, subset: Series | DataFrame):
    """
    Infer the `selection` to pass to our constructor in _gotitem.
    """
    # Shared by Rolling and Resample
    selection = None
    if subset.ndim == 2 and (
        (lib.is_scalar(key) and key in subset) or lib.is_list_like(key)
    ):
        selection = key
    elif subset.ndim == 1 and lib.is_scalar(key) and key == subset.name:
        selection = key
    return selection


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexing.py
# Line: 1292

def _multi_take_opportunity(self, tup: tuple) -> bool:
    """
    Check whether there is the possibility to use ``_multi_take``.

    Currently the limit is that all axes being indexed, must be indexed with
    list-likes.

    Parameters
    ----------
    tup : tuple
        Tuple of indexers, one per axis.

    Returns
    -------
    bool
        Whether the current indexing,
        can be passed through `_multi_take`.
    """
    if not all(is_list_like_indexer(x) for x in tup):
        return False

    # just too complicated
    return not any(com.is_bool_indexer(x) for x in tup)


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/range.py
# Line: 782

def _extended_gcd(self, a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclidean algorithms to solve Bezout's identity:
       a*x + b*y = gcd(x, y)
    Finds one particular solution for x, y: s, t
    Returns: gcd, s, t
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/base.py
# Line: 2950

def _validate_sort_keyword(self, sort) -> None:
    if sort not in [None, False, True]:
        raise ValueError(
            "The 'sort' keyword only takes the values of "
            f"None, True, or False; {sort} was passed."
        )


# ==================================================
# Line: 3542

def _assert_can_do_setop(self, other) -> bool:
    if not is_list_like(other):
        raise TypeError("Input must be Index or array-like")
    return True


# ==================================================
# Line: 5338

def _concat(self, to_concat: list[Index], name: Hashable) -> Index:
    """
    Concatenate multiple Index objects.
    """
    to_concat_vals = [x._values for x in to_concat]

    result = concat_compat(to_concat_vals)

    return Index._with_infer(result, name=name)


# ==================================================
# Line: 5919

def _check_indexing_error(self, key) -> None:
    if not is_scalar(key):
        # if key is not a scalar, directly raise an error (the code below
        # would convert to numpy arrays and raise later any way) - GH29926
        raise InvalidIndexError(key)


# ==================================================
# Line: 6099

def _raise_if_missing(self, key, indexer, axis_name: str_t) -> None:
    """
    Check that indexer can be used to return a result.

    e.g. at least one element was found,
    unless the list of keys was actually empty.

    Parameters
    ----------
    key : list-like
        Targeted labels (only used to show correct error message).
    indexer: array-like of booleans
        Indices corresponding to the key,
        (with -1 indicating not found).
    axis_name : str

    Raises
    ------
    KeyError
        If at least one key was requested but none was found.
    """
    if len(key) == 0:
        return

    # Count missing values
    missing_mask = indexer < 0
    nmissing = missing_mask.sum()

    if nmissing:
        if nmissing == len(indexer):
            raise KeyError(f"None of [{key}] are in the [{axis_name}]")

        not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
        raise KeyError(f"{not_found} not in index")


# ==================================================
# Line: 6582

def _maybe_cast_indexer(self, key):
    """
    If we have a float key and are not a floating index, then try to cast
    to an int if equivalent.
    """
    return key


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/multi.py
# Line: 347

def _validate_codes(self, level: Index, code: np.ndarray) -> np.ndarray:
    """
    Reassign code values as -1 if their corresponding levels are NaN.

    Parameters
    ----------
    code : Index
        Code to reassign.
    level : np.ndarray
        Level to check for missing values (NaN, NaT, None).

    Returns
    -------
    new code where code value = -1 if it corresponds
    to a level with missing values (NaN, NaT, None).
    """
    null_mask = isna(level)
    if np.any(null_mask):
        code = np.where(null_mask[code], -1, code)
    return code


# ==================================================
# Line: 3076

def _get_loc_single_level_index(self, level_index: Index, key: Hashable) -> int:
    """
    If key is NA value, location of index unify as -1.

    Parameters
    ----------
    level_index: Index
    key : label

    Returns
    -------
    loc : int
        If key is NA value, loc is -1
        Else, location of key in index.

    See Also
    --------
    Index.get_loc : The get_loc method for (single-level) index.
    """
    if is_scalar(key) and isna(key):
        # TODO: need is_valid_na_for_dtype(key, level_index.dtype)
        return -1
    else:
        return level_index.get_loc(key)


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/dtypes/base.py
# Line: 416

def index_class(self) -> type_t[Index]:
    """
    The Index subclass to return from Index.__new__ when this dtype is
    encountered.
    """
    from pandas import Index

    return Index


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/series.py
# Line: 517

def _init_dict(
    self, data: Mapping, index: Index | None = None, dtype: DtypeObj | None = None

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/resample.py
# Line: 221

def _convert_obj(self, obj: NDFrameT) -> NDFrameT:
    """
    Provide any conversions for the object in order to correctly handle.

    Parameters
    ----------
    obj : Series or DataFrame

    Returns
    -------
    Series or DataFrame
    """
    return obj._consolidate()


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/computation/pytables.py
# Line: 167

def conform(self, rhs):
    """inplace conform rhs"""
    if not is_list_like(rhs):
        rhs = [rhs]
    if isinstance(rhs, np.ndarray):
        rhs = rhs.ravel()
    return rhs


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/computation/expr.py
# Line: 714

def translate_In(self, op):
    return op


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/merge.py
# Line: 1036

def _validate_how(
    self, how: JoinHow | Literal["left_anti", "right_anti", "asof"]

# ==================================================
# Line: 2471

def _convert_values_for_libjoin(
    self, values: AnyArrayLike, side: str

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/accessor.py
# Occurrences: Lines 64-70 (3 instances)

def _delegate_property_get(self, name: str, *args, **kwargs):
    raise TypeError(f"You cannot access the property {name}")


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/datetimelike.py
# Line: 1038

def _get_i8_values_and_mask(
    self, other

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/arrow/extension_types.py
# Line: 148

def __arrow_ext_serialize__(self) -> bytes:
    return b""


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/base.py
# Line: 1923

def _formatter(self, boxed: bool = False) -> Callable[[Any], str | None]:
    """
    Formatting function for scalar values.

    This is used in the default '__repr__'. The returned formatting
    function receives instances of your scalar type.

    Parameters
    ----------
    boxed : bool, default False
        An indicated for whether or not your array is being printed
        within a Series, DataFrame, or Index (True), or just by
        itself (False). This may be useful if you want scalar values
        to appear differently within a Series versus on its own (e.g.
        quoted or not).

    Returns
    -------
    Callable[[Any], str]
        A callable that gets instances of the scalar type and
        returns a string. By default, :func:`repr` is used
        when ``boxed=False`` and :func:`str` is used when
        ``boxed=True``.

    See Also
    --------
    api.extensions.ExtensionArray._concat_same_type : Concatenate multiple
        array of this dtype.
    api.extensions.ExtensionArray._explode : Transform each element of
        list-like to a row.
    api.extensions.ExtensionArray._from_factorized : Reconstruct an
        ExtensionArray after factorization.
    api.extensions.ExtensionArray._from_sequence : Construct a new
        ExtensionArray from a sequence of scalars.

    Examples
    --------
    >>> class MyExtensionArray(pd.arrays.NumpyExtensionArray):
    ...     def _formatter(self, boxed=False):
    ...         return lambda x: "*" + str(x) + "*"
    >>> MyExtensionArray(np.array([1, 2, 3, 4]))
    <MyExtensionArray>
    [*1*, *2*, *3*, *4*]
    Length: 4, dtype: int64
    """
    if boxed:
        return str
    return repr


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/datetimes.py
# Line: 633

def tz(self, value):
    # GH 3746: Prevent localizing or converting the index by setting tz
    raise AttributeError(
        "Cannot directly set timezone. Use tz_localize() "
        "or tz_convert() as appropriate"
    )


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/boolean.py
# Line: 110

def __from_arrow__(
    self, array: pyarrow.Array | pyarrow.ChunkedArray

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arraylike.py
# Line: 36

def _cmp_method(self, other, op):
    return NotImplemented


# ==================================================
# Line: 66

def _logical_method(self, other, op):
    return NotImplemented


# ==================================================
# Line: 96

def _arith_method(self, other, op):
    return NotImplemented


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/internals/blocks.py
# Line: 940

def _maybe_squeeze_arg(self, arg: np.ndarray) -> np.ndarray:
    """
    For compatibility with 1D-only ExtensionArrays.
    """
    return arg


# ==================================================
# Line: 946

def _unwrap_setitem_indexer(self, indexer):
    """
    For compatibility with 1D-only ExtensionArrays.
    """
    return indexer


# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/internals/managers.py
# Line: 732

def is_consolidated(self) -> bool:
    return True


# ==================================================
# Line: 751

def _consolidate_inplace(self) -> None:
    return


# ==================================================
# File: /root/ecooptimizer/pandas/setup.py
# Line: 257

def check_cython_extensions(self, extensions) -> None:
    for ext in extensions:
        for src in ext.sources:
            if not os.path.exists(src):
                print(f"{ext.name}: -> [{ext.sources}]")
                raise Exception(
                    f"""Cython-generated file '{src}' not found.
            Cython is required to compile pandas from a development branch.
            Please install Cython or download a release package of pandas.
            """
                )


# ==================================================
