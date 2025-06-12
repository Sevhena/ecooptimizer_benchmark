# too-many-arguments snippets for pandas

# File: /root/ecooptimizer/pandas/doc/make.py
# Line: 41

def __init__(
    self,
    num_jobs="auto",
    include_api=True,
    whatsnew=False,
    single_doc=None,
    verbosity=0,
    warnings_are_errors=False,
    no_browser=False,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/tseries/holiday.py
# Line: 161

def __init__(
    self,
    name: str,
    year=None,
    month=None,
    day=None,
    offset: BaseOffset | list[BaseOffset] | None = None,
    observance: Callable | None = None,
    start_date=None,
    end_date=None,
    days_of_week: tuple | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/sql.py
# Line: 191

def _wrap_result(
    data,
    columns,
    index_col=None,
    coerce_float: bool = True,
    parse_dates=None,
    dtype: DtypeArg | None = None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 239

def read_sql_table(  # pyright: ignore[reportOverlappingOverload]
    table_name: str,
    con,
    schema=...,
    index_col: str | list[str] | None = ...,
    coerce_float=...,
    parse_dates: list[str] | dict[str, str] | dict[str, dict[str, Any]] | None = ...,
    columns: list[str] | None = ...,
    chunksize: None = ...,
    dtype_backend: DtypeBackend | lib.NoDefault = ...,

# ==================================================
# Line: 253

def read_sql_table(
    table_name: str,
    con,
    schema=...,
    index_col: str | list[str] | None = ...,
    coerce_float=...,
    parse_dates: list[str] | dict[str, str] | dict[str, dict[str, Any]] | None = ...,
    columns: list[str] | None = ...,
    chunksize: int = ...,
    dtype_backend: DtypeBackend | lib.NoDefault = ...,

# ==================================================
# Line: 266

def read_sql_table(
    table_name: str,
    con,
    schema: str | None = None,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    parse_dates: list[str] | dict[str, str] | dict[str, dict[str, Any]] | None = None,
    columns: list[str] | None = None,
    chunksize: int | None = None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,

# ==================================================
# Line: 370

def read_sql_query(  # pyright: ignore[reportOverlappingOverload]
    sql,
    con,
    index_col: str | list[str] | None = ...,
    coerce_float=...,
    params: list[Any] | Mapping[str, Any] | None = ...,
    parse_dates: list[str] | dict[str, str] | dict[str, dict[str, Any]] | None = ...,
    chunksize: None = ...,
    dtype: DtypeArg | None = ...,
    dtype_backend: DtypeBackend | lib.NoDefault = ...,

# ==================================================
# Line: 384

def read_sql_query(
    sql,
    con,
    index_col: str | list[str] | None = ...,
    coerce_float=...,
    params: list[Any] | Mapping[str, Any] | None = ...,
    parse_dates: list[str] | dict[str, str] | dict[str, dict[str, Any]] | None = ...,
    chunksize: int = ...,
    dtype: DtypeArg | None = ...,
    dtype_backend: DtypeBackend | lib.NoDefault = ...,

# ==================================================
# Line: 397

def read_sql_query(
    sql,
    con,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    params: list[Any] | Mapping[str, Any] | None = None,
    parse_dates: list[str] | dict[str, str] | dict[str, dict[str, Any]] | None = None,
    chunksize: int | None = None,
    dtype: DtypeArg | None = None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,

# ==================================================
# Line: 506

def read_sql(  # pyright: ignore[reportOverlappingOverload]
    sql,
    con,
    index_col: str | list[str] | None = ...,
    coerce_float=...,
    params=...,
    parse_dates=...,
    columns: list[str] = ...,
    chunksize: None = ...,
    dtype_backend: DtypeBackend | lib.NoDefault = ...,
    dtype: DtypeArg | None = None,

# ==================================================
# Line: 521

def read_sql(
    sql,
    con,
    index_col: str | list[str] | None = ...,
    coerce_float=...,
    params=...,
    parse_dates=...,
    columns: list[str] = ...,
    chunksize: int = ...,
    dtype_backend: DtypeBackend | lib.NoDefault = ...,
    dtype: DtypeArg | None = None,

# ==================================================
# Line: 535

def read_sql(
    sql,
    con,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    params=None,
    parse_dates=None,
    columns: list[str] | None = None,
    chunksize: int | None = None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,
    dtype: DtypeArg | None = None,

# ==================================================
# Line: 737

def to_sql(
    frame,
    name: str,
    con,
    schema: str | None = None,
    if_exists: Literal["fail", "replace", "append", "delete_rows"] = "fail",
    index: bool = True,
    index_label: IndexLabel | None = None,
    chunksize: int | None = None,
    dtype: DtypeArg | None = None,
    method: Literal["multi"] | Callable | None = None,
    engine: str = "auto",
    **engine_kwargs,

# ==================================================
# Line: 931

def __init__(
    self,
    name: str,
    pandas_sql_engine,
    frame=None,
    index: bool | str | list[str] | None = True,
    if_exists: Literal["fail", "replace", "append", "delete_rows"] = "fail",
    prefix: str = "pandas",
    index_label=None,
    schema=None,
    keys=None,
    dtype: DtypeArg | None = None,

# ==================================================
# Line: 1125

def _query_iterator(
    self,
    result,
    exit_stack: ExitStack,
    chunksize: int | None,
    columns,
    coerce_float: bool = True,
    parse_dates=None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 1161

def read(
    self,
    exit_stack: ExitStack,
    coerce_float: bool = True,
    parse_dates=None,
    columns=None,
    chunksize: int | None = None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 1461

def read_table(
    self,
    table_name: str,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    parse_dates=None,
    columns=None,
    schema: str | None = None,
    chunksize: int | None = None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 1475

def read_query(
    self,
    sql: str,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    parse_dates=None,
    params=None,
    chunksize: int | None = None,
    dtype: DtypeArg | None = None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 1489

def to_sql(
    self,
    frame,
    name: str,
    if_exists: Literal["fail", "replace", "append", "delete_rows"] = "fail",
    index: bool = True,
    index_label=None,
    schema=None,
    chunksize: int | None = None,
    dtype: DtypeArg | None = None,
    method: Literal["multi"] | Callable | None = None,
    engine: str = "auto",
    **engine_kwargs,

# ==================================================
# Line: 1526

def insert_records(
    self,
    table: SQLTable,
    con,
    frame,
    name: str,
    index: bool | str | list[str] | None = True,
    schema=None,
    chunksize: int | None = None,
    method=None,
    **engine_kwargs,

# ==================================================
# Line: 1550

def insert_records(
    self,
    table: SQLTable,
    con,
    frame,
    name: str,
    index: bool | str | list[str] | None = True,
    schema=None,
    chunksize: int | None = None,
    method=None,
    **engine_kwargs,

# ==================================================
# Line: 1677

def read_table(
    self,
    table_name: str,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    parse_dates=None,
    columns=None,
    schema: str | None = None,
    chunksize: int | None = None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 1755

def _query_iterator(
    result,
    exit_stack: ExitStack,
    chunksize: int,
    columns,
    index_col=None,
    coerce_float: bool = True,
    parse_dates=None,
    dtype: DtypeArg | None = None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 1795

def read_query(
    self,
    sql: str,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    parse_dates=None,
    params=None,
    chunksize: int | None = None,
    dtype: DtypeArg | None = None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 1883

def prep_table(
    self,
    frame,
    name: str,
    if_exists: Literal["fail", "replace", "append", "delete_rows"] = "fail",
    index: bool | str | list[str] | None = True,
    index_label=None,
    schema=None,
    dtype: DtypeArg | None = None,

# ==================================================
# Line: 1960

def to_sql(
    self,
    frame,
    name: str,
    if_exists: Literal["fail", "replace", "append", "delete_rows"] = "fail",
    index: bool = True,
    index_label=None,
    schema: str | None = None,
    chunksize: int | None = None,
    dtype: DtypeArg | None = None,
    method: Literal["multi"] | Callable | None = None,
    engine: str = "auto",
    **engine_kwargs,

# ==================================================
# Line: 2161

def read_table(
    self,
    table_name: str,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    parse_dates=None,
    columns=None,
    schema: str | None = None,
    chunksize: int | None = None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 2251

def read_query(
    self,
    sql: str,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    parse_dates=None,
    params=None,
    chunksize: int | None = None,
    dtype: DtypeArg | None = None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 2324

def to_sql(
    self,
    frame,
    name: str,
    if_exists: Literal["fail", "replace", "append", "delete_rows"] = "fail",
    index: bool = True,
    index_label=None,
    schema: str | None = None,
    chunksize: int | None = None,
    dtype: DtypeArg | None = None,
    method: Literal["multi"] | Callable | None = None,
    engine: str = "auto",
    **engine_kwargs,

# ==================================================
# Line: 2717

def _query_iterator(
    cursor,
    chunksize: int,
    columns,
    index_col=None,
    coerce_float: bool = True,
    parse_dates=None,
    dtype: DtypeArg | None = None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 2755

def read_query(
    self,
    sql,
    index_col=None,
    coerce_float: bool = True,
    parse_dates=None,
    params=None,
    chunksize: int | None = None,
    dtype: DtypeArg | None = None,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",

# ==================================================
# Line: 2801

def to_sql(
    self,
    frame,
    name: str,
    if_exists: str = "fail",
    index: bool = True,
    index_label=None,
    schema=None,
    chunksize: int | None = None,
    dtype: DtypeArg | None = None,
    method: Literal["multi"] | Callable | None = None,
    engine: str = "auto",
    **engine_kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/html.py
# Line: 216

def __init__(
    self,
    io: FilePath | ReadBuffer[str] | ReadBuffer[bytes],
    match: str | Pattern,
    attrs: dict[str, str] | None,
    encoding: str,
    displayed_only: bool,
    extract_links: Literal[None, "header", "footer", "body", "all"],
    storage_options: StorageOptions = None,

# ==================================================
# Line: 956

def _parse(
    flavor,
    io,
    match,
    attrs,
    encoding,
    displayed_only,
    extract_links,
    storage_options,
    **kwargs,

# ==================================================
# Line: 1028

def read_html(
    io: FilePath | ReadBuffer[str],
    *,
    match: str | Pattern = ".+",
    flavor: HTMLFlavors | Sequence[HTMLFlavors] | None = None,
    header: int | Sequence[int] | None = None,
    index_col: int | Sequence[int] | None = None,
    skiprows: int | Sequence[int] | slice | None = None,
    attrs: dict[str, str] | None = None,
    parse_dates: bool = False,
    thousands: str | None = ",",
    encoding: str | None = None,
    decimal: str = ".",
    converters: dict | None = None,
    na_values: Iterable[object] | None = None,
    keep_default_na: bool = True,
    displayed_only: bool = True,
    extract_links: Literal[None, "header", "footer", "body", "all"] = None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,
    storage_options: StorageOptions = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/parsers/readers.py
# Line: 778

def read_csv(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None | lib.NoDefault = lib.no_default,
    delimiter: str | None | lib.NoDefault = None,
    # Column and Index Locations and Names
    header: int | Sequence[int] | None | Literal["infer"] = "infer",
    names: Sequence[Hashable] | None | lib.NoDefault = lib.no_default,
    index_col: IndexLabel | Literal[False] | None = None,
    usecols: UsecolsArgType = None,
    # General Parsing Configuration
    dtype: DtypeArg | None = None,
    engine: CSVEngine | None = None,
    converters: Mapping[HashableT, Callable] | None = None,
    true_values: list | None = None,
    false_values: list | None = None,
    skipinitialspace: bool = False,
    skiprows: list[int] | int | Callable[[Hashable], bool] | None = None,
    skipfooter: int = 0,
    nrows: int | None = None,
    # NA and Missing Data Handling
    na_values: Hashable
    | Iterable[Hashable]
    | Mapping[Hashable, Iterable[Hashable]]
    | None = None,
    keep_default_na: bool = True,
    na_filter: bool = True,
    skip_blank_lines: bool = True,
    # Datetime Handling
    parse_dates: bool | Sequence[Hashable] | None = None,
    date_format: str | dict[Hashable, str] | None = None,
    dayfirst: bool = False,
    cache_dates: bool = True,
    # Iteration
    iterator: bool = False,
    chunksize: int | None = None,
    # Quoting, Compression, and File Format
    compression: CompressionOptions = "infer",
    thousands: str | None = None,
    decimal: str = ".",
    lineterminator: str | None = None,
    quotechar: str = '"',
    quoting: int = csv.QUOTE_MINIMAL,
    doublequote: bool = True,
    escapechar: str | None = None,
    comment: str | None = None,
    encoding: str | None = None,
    encoding_errors: str | None = "strict",
    dialect: str | csv.Dialect | None = None,
    # Error Handling
    on_bad_lines: str = "error",
    # Internal
    low_memory: bool = _c_parser_defaults["low_memory"],
    memory_map: bool = False,
    float_precision: Literal["high", "legacy", "round_trip"] | None = None,
    storage_options: StorageOptions | None = None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,

# ==================================================
# Line: 914

def read_table(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None | lib.NoDefault = lib.no_default,
    delimiter: str | None | lib.NoDefault = None,
    # Column and Index Locations and Names
    header: int | Sequence[int] | None | Literal["infer"] = "infer",
    names: Sequence[Hashable] | None | lib.NoDefault = lib.no_default,
    index_col: IndexLabel | Literal[False] | None = None,
    usecols: UsecolsArgType = None,
    # General Parsing Configuration
    dtype: DtypeArg | None = None,
    engine: CSVEngine | None = None,
    converters: Mapping[HashableT, Callable] | None = None,
    true_values: list | None = None,
    false_values: list | None = None,
    skipinitialspace: bool = False,
    skiprows: list[int] | int | Callable[[Hashable], bool] | None = None,
    skipfooter: int = 0,
    nrows: int | None = None,
    # NA and Missing Data Handling
    na_values: Hashable
    | Iterable[Hashable]
    | Mapping[Hashable, Iterable[Hashable]]
    | None = None,
    keep_default_na: bool = True,
    na_filter: bool = True,
    skip_blank_lines: bool = True,
    # Datetime Handling
    parse_dates: bool | Sequence[Hashable] | None = None,
    date_format: str | dict[Hashable, str] | None = None,
    dayfirst: bool = False,
    cache_dates: bool = True,
    # Iteration
    iterator: bool = False,
    chunksize: int | None = None,
    # Quoting, Compression, and File Format
    compression: CompressionOptions = "infer",
    thousands: str | None = None,
    decimal: str = ".",
    lineterminator: str | None = None,
    quotechar: str = '"',
    quoting: int = csv.QUOTE_MINIMAL,
    doublequote: bool = True,
    escapechar: str | None = None,
    comment: str | None = None,
    encoding: str | None = None,
    encoding_errors: str | None = "strict",
    dialect: str | csv.Dialect | None = None,
    # Error Handling
    on_bad_lines: str = "error",
    # Internal
    low_memory: bool = _c_parser_defaults["low_memory"],
    memory_map: bool = False,
    float_precision: Literal["high", "legacy", "round_trip"] | None = None,
    storage_options: StorageOptions | None = None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,

# ==================================================
# Line: 1709

def _refine_defaults_read(
    dialect: str | csv.Dialect | None,
    delimiter: str | None | lib.NoDefault,
    engine: CSVEngine | None,
    sep: str | None | lib.NoDefault,
    on_bad_lines: str | Callable,
    names: Sequence[Hashable] | None | lib.NoDefault,
    defaults: dict[str, Any],
    dtype_backend: DtypeBackend | lib.NoDefault,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/parsers/python_parser.py
# Line: 1375

def __init__(
    self,
    f: IO[str] | ReadCsvBuffer[str],
    colspecs: list[tuple[int, int]] | Literal["infer"],
    delimiter: str | None,
    comment: str | None,
    skiprows: set[int] | None = None,
    infer_nrows: int = 100,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/xml.py
# Line: 148

def __init__(
    self,
    path_or_buffer: FilePath | ReadBuffer[bytes] | ReadBuffer[str],
    xpath: str,
    namespaces: dict[str, str] | None,
    elems_only: bool,
    attrs_only: bool,
    names: Sequence[str] | None,
    dtype: DtypeArg | None,
    converters: ConvertersArg | None,
    parse_dates: ParseDatesArg | None,
    encoding: str | None,
    stylesheet: FilePath | ReadBuffer[bytes] | ReadBuffer[str] | None,
    iterparse: dict[str, list[str]] | None,
    compression: CompressionOptions,
    storage_options: StorageOptions,

# ==================================================
# Line: 737

def _parse(
    path_or_buffer: FilePath | ReadBuffer[bytes] | ReadBuffer[str],
    xpath: str,
    namespaces: dict[str, str] | None,
    elems_only: bool,
    attrs_only: bool,
    names: Sequence[str] | None,
    dtype: DtypeArg | None,
    converters: ConvertersArg | None,
    parse_dates: ParseDatesArg | None,
    encoding: str | None,
    parser: XMLParsers,
    stylesheet: FilePath | ReadBuffer[bytes] | ReadBuffer[str] | None,
    iterparse: dict[str, list[str]] | None,
    compression: CompressionOptions,
    storage_options: StorageOptions,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,
    **kwargs,

# ==================================================
# Line: 832

def read_xml(
    path_or_buffer: FilePath | ReadBuffer[bytes] | ReadBuffer[str],
    *,
    xpath: str = "./*",
    namespaces: dict[str, str] | None = None,
    elems_only: bool = False,
    attrs_only: bool = False,
    names: Sequence[str] | None = None,
    dtype: DtypeArg | None = None,
    converters: ConvertersArg | None = None,
    parse_dates: ParseDatesArg | None = None,
    # encoding can not be None for lxml and StringIO input
    encoding: str | None = "utf-8",
    parser: XMLParsers = "lxml",
    stylesheet: FilePath | ReadBuffer[bytes] | ReadBuffer[str] | None = None,
    iterparse: dict[str, list[str]] | None = None,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/pytables.py
# Line: 256

def to_hdf(
    path_or_buf: FilePath | HDFStore,
    key: str,
    value: DataFrame | Series,
    mode: str = "a",
    complevel: int | None = None,
    complib: str | None = None,
    append: bool = False,
    format: str | None = None,
    index: bool = True,
    min_itemsize: int | dict[str, int] | None = None,
    nan_rep=None,
    dropna: bool | None = None,
    data_columns: Literal[True] | list[str] | None = None,
    errors: str = "strict",
    encoding: str = "UTF-8",

# ==================================================
# Line: 312

def read_hdf(
    path_or_buf: FilePath | HDFStore,
    key=None,
    mode: str = "r",
    errors: str = "strict",
    where: str | list | None = None,
    start: int | None = None,
    stop: int | None = None,
    columns: list[str] | None = None,
    iterator: bool = False,
    chunksize: int | None = None,
    **kwargs,

# ==================================================
# Line: 830

def select(
    self,
    key: str,
    where=None,
    start=None,
    stop=None,
    columns=None,
    iterator: bool = False,
    chunksize: int | None = None,
    auto_close: bool = False,

# ==================================================
# Line: 1001

def select_as_multiple(
    self,
    keys,
    where=None,
    selector=None,
    columns=None,
    start=None,
    stop=None,
    iterator: bool = False,
    chunksize: int | None = None,
    auto_close: bool = False,

# ==================================================
# Line: 1122

def put(
    self,
    key: str,
    value: DataFrame | Series,
    format=None,
    index: bool = True,
    append: bool = False,
    complib=None,
    complevel: int | None = None,
    min_itemsize: int | dict[str, int] | None = None,
    nan_rep=None,
    data_columns: Literal[True] | list[str] | None = None,
    encoding=None,
    errors: str = "strict",
    track_times: bool = True,
    dropna: bool = False,

# ==================================================
# Line: 1281

def append(
    self,
    key: str,
    value: DataFrame | Series,
    format=None,
    axes=None,
    index: bool | list[str] = True,
    append: bool = True,
    complib=None,
    complevel: int | None = None,
    columns=None,
    min_itemsize: int | dict[str, int] | None = None,
    nan_rep=None,
    chunksize: int | None = None,
    expectedrows=None,
    dropna: bool | None = None,
    data_columns: Literal[True] | list[str] | None = None,
    encoding=None,
    errors: str = "strict",

# ==================================================
# Line: 1409

def append_to_multiple(
    self,
    d: dict,
    value,
    selector,
    data_columns=None,
    axes=None,
    dropna: bool = False,
    **kwargs,

# ==================================================
# Line: 1679

def copy(
    self,
    file,
    mode: str = "w",
    propindexes: bool = True,
    keys=None,
    complib=None,
    complevel: int | None = None,
    fletcher32: bool = False,
    overwrite: bool = True,

# ==================================================
# Line: 1905

def _write_to_group(
    self,
    key: str,
    value: DataFrame | Series,
    format,
    axes=None,
    index: bool | list[str] = True,
    append: bool = False,
    complib=None,
    complevel: int | None = None,
    fletcher32=None,
    min_itemsize: int | dict[str, int] | None = None,
    chunksize: int | None = None,
    expectedrows=None,
    dropna: bool = False,
    nan_rep=None,
    data_columns=None,
    encoding=None,
    errors: str = "strict",
    track_times: bool = True,

# ==================================================
# Line: 2036

def __init__(
    self,
    store: HDFStore,
    s: GenericFixed | Table,
    func,
    where,
    nrows,
    start=None,
    stop=None,
    iterator: bool = False,
    chunksize: int | None = None,
    auto_close: bool = False,

# ==================================================
# Line: 2142

def __init__(
    self,
    name: str,
    values=None,
    kind=None,
    typ=None,
    cname: str | None = None,
    axis=None,
    pos=None,
    freq=None,
    tz=None,
    index_name=None,
    ordered=None,
    table=None,
    meta=None,
    metadata=None,

# ==================================================
# Line: 2483

def __init__(
    self,
    name: str,
    values=None,
    kind=None,
    typ=None,
    cname: str | None = None,
    pos=None,
    tz=None,
    ordered=None,
    table=None,
    meta=None,
    metadata=None,
    dtype: DtypeArg | None = None,
    data=None,

# ==================================================
# Line: 3511

def __init__(
    self,
    parent: HDFStore,
    group: Node,
    encoding: str | None = None,
    errors: str = "strict",
    index_axes: list[IndexCol] | None = None,
    non_index_axes: list[tuple[AxisInt, Any]] | None = None,
    values_axes: list[DataCol] | None = None,
    data_columns: list | None = None,
    info: dict | None = None,
    nan_rep=None,

# ==================================================
# Line: 4020

def _create_axes(
    self,
    axes,
    obj: DataFrame,
    validate: bool = True,
    nan_rep=None,
    data_columns=None,
    min_itemsize=None,

# ==================================================
# Line: 4516

def write(  # type: ignore[override]
    self,
    obj,
    axes=None,
    append: bool = False,
    complib=None,
    complevel=None,
    fletcher32=None,
    min_itemsize=None,
    chunksize: int | None = None,
    expectedrows=None,
    dropna: bool = False,
    nan_rep=None,
    data_columns=None,
    track_times: bool = True,

# ==================================================
# Line: 5184

def _maybe_convert_for_string_atom(
    name: str,
    bvalues: ArrayLike,
    existing_col,
    min_itemsize,
    nan_rep,
    encoding,
    errors,
    columns: list[str],

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/parquet.py
# Line: 171

def write(
    self,
    df: DataFrame,
    path: FilePath | WriteBuffer[bytes],
    compression: str | None = "snappy",
    index: bool | None = None,
    storage_options: StorageOptions | None = None,
    partition_cols: list[str] | None = None,
    filesystem=None,
    **kwargs,

# ==================================================
# Line: 237

def read(
    self,
    path,
    columns=None,
    filters=None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,
    storage_options: StorageOptions | None = None,
    filesystem=None,
    to_pandas_kwargs: dict[str, Any] | None = None,
    **kwargs,

# ==================================================
# Line: 295

def write(
    self,
    df: DataFrame,
    path,
    compression: Literal["snappy", "gzip", "brotli"] | None = "snappy",
    index=None,
    partition_cols=None,
    storage_options: StorageOptions | None = None,
    filesystem=None,
    **kwargs,

# ==================================================
# Line: 348

def read(
    self,
    path,
    columns=None,
    filters=None,
    storage_options: StorageOptions | None = None,
    filesystem=None,
    to_pandas_kwargs: dict | None = None,
    **kwargs,

# ==================================================
# Line: 407

def to_parquet(
    df: DataFrame,
    path: FilePath | WriteBuffer[bytes] | None = None,
    engine: str = "auto",
    compression: str | None = "snappy",
    index: bool | None = None,
    storage_options: StorageOptions | None = None,
    partition_cols: list[str] | None = None,
    filesystem: Any = None,
    **kwargs,

# ==================================================
# Line: 496

def read_parquet(
    path: FilePath | ReadBuffer[bytes],
    engine: str = "auto",
    columns: list[str] | None = None,
    storage_options: StorageOptions | None = None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,
    filesystem: Any = None,
    filters: list[tuple] | list[list[tuple]] | None = None,
    to_pandas_kwargs: dict | None = None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/iceberg.py
# Line: 10

def read_iceberg(
    table_identifier: str,
    catalog_name: str | None = None,
    *,
    catalog_properties: dict[str, Any] | None = None,
    row_filter: str | None = None,
    selected_fields: tuple[str] | None = None,
    case_sensitive: bool = True,
    snapshot_id: int | None = None,
    limit: int | None = None,
    scan_properties: dict[str, Any] | None = None,

# ==================================================
# Line: 98

def to_iceberg(
    df: DataFrame,
    table_identifier: str,
    catalog_name: str | None = None,
    *,
    catalog_properties: dict[str, Any] | None = None,
    location: str | None = None,
    append: bool = False,
    snapshot_properties: dict[str, str] | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/stata.py
# Line: 1096

def __init__(
    self,
    path_or_buf: FilePath | ReadBuffer[bytes],
    convert_dates: bool = True,
    convert_categoricals: bool = True,
    index_col: str | None = None,
    convert_missing: bool = False,
    preserve_dtypes: bool = True,
    columns: Sequence[str] | None = None,
    order_categoricals: bool = True,
    chunksize: int | None = None,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,

# ==================================================
# Line: 1671

def read(
    self,
    nrows: int | None = None,
    convert_dates: bool | None = None,
    convert_categoricals: bool | None = None,
    index_col: str | None = None,
    convert_missing: bool | None = None,
    preserve_dtypes: bool | None = None,
    columns: Sequence[str] | None = None,
    order_categoricals: bool | None = None,

# ==================================================
# Line: 2128

def read_stata(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    convert_dates: bool = True,
    convert_categoricals: bool = True,
    index_col: str | None = None,
    convert_missing: bool = False,
    preserve_dtypes: bool = True,
    columns: Sequence[str] | None = None,
    order_categoricals: bool = True,
    chunksize: int | None = None,
    iterator: bool = False,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,

# ==================================================
# Line: 2388

def __init__(
    self,
    fname: FilePath | WriteBuffer[bytes],
    data: DataFrame,
    convert_dates: dict[Hashable, str] | None = None,
    write_index: bool = True,
    byteorder: str | None = None,
    time_stamp: datetime | None = None,
    data_label: str | None = None,
    variable_labels: dict[Hashable, str] | None = None,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,
    *,
    value_labels: dict[Hashable, dict[float, str]] | None = None,

# ==================================================
# Line: 3367

def __init__(
    self,
    fname: FilePath | WriteBuffer[bytes],
    data: DataFrame,
    convert_dates: dict[Hashable, str] | None = None,
    write_index: bool = True,
    byteorder: str | None = None,
    time_stamp: datetime | None = None,
    data_label: str | None = None,
    variable_labels: dict[Hashable, str] | None = None,
    convert_strl: Sequence[Hashable] | None = None,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,
    *,
    value_labels: dict[Hashable, dict[float, str]] | None = None,

# ==================================================
# Line: 3762

def __init__(
    self,
    fname: FilePath | WriteBuffer[bytes],
    data: DataFrame,
    convert_dates: dict[Hashable, str] | None = None,
    write_index: bool = True,
    byteorder: str | None = None,
    time_stamp: datetime | None = None,
    data_label: str | None = None,
    variable_labels: dict[Hashable, str] | None = None,
    convert_strl: Sequence[Hashable] | None = None,
    version: int | None = None,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,
    *,
    value_labels: dict[Hashable, dict[float, str]] | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/sas/sasreader.py
# Line: 61

def read_sas(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    format: str | None = ...,
    index: Hashable | None = ...,
    encoding: str | None = ...,
    chunksize: int = ...,
    iterator: bool = ...,
    compression: CompressionOptions = ...,

# ==================================================
# Line: 74

def read_sas(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    format: str | None = ...,
    index: Hashable | None = ...,
    encoding: str | None = ...,
    chunksize: None = ...,
    iterator: bool = ...,
    compression: CompressionOptions = ...,

# ==================================================
# Line: 87

def read_sas(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    format: str | None = None,
    index: Hashable | None = None,
    encoding: str | None = None,
    chunksize: int | None = None,
    iterator: bool = False,
    compression: CompressionOptions = "infer",

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/sas/sas7bdat.py
# Line: 101

def __init__(
    self,
    col_id: int,
    # These can be bytes when convert_header_text is False
    name: str | bytes,
    label: str | bytes,
    format: str | bytes,
    ctype: bytes,
    length: int,

# ==================================================
# Line: 154

def __init__(
    self,
    path_or_buf: FilePath | ReadBuffer[bytes],
    index=None,
    convert_dates: bool = True,
    blank_missing: bool = True,
    chunksize: int | None = None,
    encoding: str | None = None,
    convert_text: bool = True,
    convert_header_text: bool = True,
    compression: CompressionOptions = "infer",

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/html.py
# Line: 210

def write_tr(
    self,
    line: Iterable,
    indent: int = 0,
    indent_delta: int = 0,
    header: bool = False,
    align: str | None = None,
    tags: dict[int, str] | None = None,
    nindex_levels: int = 0,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/xml.py
# Line: 105

def __init__(
    self,
    frame: DataFrame,
    path_or_buffer: FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None = None,
    index: bool = True,
    root_name: str | None = "data",
    row_name: str | None = "row",
    na_rep: str | None = None,
    attr_cols: list[str] | None = None,
    elem_cols: list[str] | None = None,
    namespaces: dict[str | None, str] | None = None,
    prefix: str | None = None,
    encoding: str = "utf-8",
    xml_declaration: bool | None = True,
    pretty_print: bool | None = True,
    stylesheet: FilePath | ReadBuffer[str] | ReadBuffer[bytes] | None = None,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/excel.py
# Line: 69

def __init__(
    self,
    row: int,
    col: int,
    val,
    style=None,
    mergestart: int | None = None,
    mergeend: int | None = None,

# ==================================================
# Line: 87

def __init__(
    self,
    row: int,
    col: int,
    val,
    style: dict | None,
    css_styles: dict[tuple[int, int], list[tuple[str, Any]]] | None,
    css_row: int,
    css_col: int,
    css_converter: Callable | None,
    **kwargs,

# ==================================================
# Line: 545

def __init__(
    self,
    df,
    na_rep: str = "",
    float_format: str | None = None,
    cols: Sequence[Hashable] | None = None,
    header: Sequence[Hashable] | bool = True,
    index: bool = True,
    index_label: IndexLabel | None = None,
    merge_cells: ExcelWriterMergeCells = False,
    inf_rep: str = "inf",
    style_converter: Callable | None = None,

# ==================================================
# Line: 879

def write(
    self,
    writer: FilePath | WriteExcelBuffer | ExcelWriter,
    sheet_name: str = "Sheet1",
    startrow: int = 0,
    startcol: int = 0,
    freeze_panes: tuple[int, int] | None = None,
    engine: str | None = None,
    storage_options: StorageOptions | None = None,
    engine_kwargs: dict | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/csvs.py
# Line: 59

def __init__(
    self,
    formatter: DataFrameFormatter,
    path_or_buf: FilePath | WriteBuffer[str] | WriteBuffer[bytes] = "",
    sep: str = ",",
    cols: Sequence[Hashable] | None = None,
    index_label: IndexLabel | None = None,
    mode: str = "w",
    encoding: str | None = None,
    errors: str = "strict",
    compression: CompressionOptions = "infer",
    quoting: int | None = None,
    lineterminator: str | None = "\n",
    chunksize: int | None = None,
    quotechar: str | None = '"',
    date_format: str | None = None,
    doublequote: bool = True,
    escapechar: str | None = None,
    storage_options: StorageOptions | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/style_render.py
# Line: 83

def __init__(
    self,
    data: DataFrame | Series,
    uuid: str | None = None,
    uuid_len: int = 5,
    table_styles: CSSStyles | None = None,
    table_attributes: str | None = None,
    caption: str | tuple | list | None = None,
    cell_ids: bool = True,
    precision: int | None = None,

# ==================================================
# Line: 283

def _translate(
    self,
    sparse_index: bool,
    sparse_cols: bool,
    max_rows: int | None = None,
    max_cols: int | None = None,
    blank: str = "&nbsp;",
    dxs: list[dict] | None = None,

# ==================================================
# Line: 669

def _check_trim(
    self,
    count: int,
    max: int,
    obj: list,
    element: str,
    css: str | None = None,
    value: str = "...",

# ==================================================
# Line: 976

def format(
    self,
    formatter: ExtFormatter | None = None,
    subset: Subset | None = None,
    na_rep: str | None = None,
    precision: int | None = None,
    decimal: str = ".",
    thousands: str | None = None,
    escape: str | None = None,
    hyperlinks: str | None = None,

# ==================================================
# Line: 1247

def format_index(
    self,
    formatter: ExtFormatter | None = None,
    axis: Axis = 0,
    level: Level | list[Level] | None = None,
    na_rep: str | None = None,
    precision: int | None = None,
    decimal: str = ".",
    thousands: str | None = None,
    escape: str | None = None,
    hyperlinks: str | None = None,

# ==================================================
# Line: 1598

def format_index_names(
    self,
    formatter: ExtFormatter | None = None,
    axis: Axis = 0,
    level: Level | list[Level] | None = None,
    na_rep: str | None = None,
    precision: int | None = None,
    decimal: str = ".",
    thousands: str | None = None,
    escape: str | None = None,
    hyperlinks: str | None = None,

# ==================================================
# Line: 1984

def _maybe_wrap_formatter(
    formatter: BaseFormatter | None = None,
    na_rep: str | None = None,
    precision: int | None = None,
    decimal: str = ".",
    thousands: str | None = None,
    escape: str | None = None,
    hyperlinks: str | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/style.py
# Line: 259

def __init__(
    self,
    data: DataFrame | Series,
    precision: int | None = None,
    table_styles: CSSStyles | None = None,
    uuid: str | None = None,
    caption: str | tuple | list | None = None,
    table_attributes: str | None = None,
    cell_ids: bool = True,
    na_rep: str | None = None,
    uuid_len: int = 5,
    decimal: str | None = None,
    thousands: str | None = None,
    escape: str | None = None,
    formatter: ExtFormatter | None = None,

# ==================================================
# Line: 579

def to_excel(
    self,
    excel_writer: FilePath | WriteExcelBuffer | ExcelWriter,
    sheet_name: str = "Sheet1",
    na_rep: str = "",
    float_format: str | None = None,
    columns: Sequence[Hashable] | None = None,
    header: Sequence[Hashable] | bool = True,
    index: bool = True,
    index_label: IndexLabel | None = None,
    startrow: int = 0,
    startcol: int = 0,
    engine: str | None = None,
    merge_cells: ExcelWriterMergeCells = True,
    encoding: str | None = None,
    inf_rep: str = "inf",
    verbose: bool = True,
    freeze_panes: tuple[int, int] | None = None,
    storage_options: StorageOptions | None = None,

# ==================================================
# Line: 623

def to_latex(
    self,
    buf: FilePath | WriteBuffer[str],
    *,
    column_format: str | None = ...,
    position: str | None = ...,
    position_float: str | None = ...,
    hrules: bool | None = ...,
    clines: str | None = ...,
    label: str | None = ...,
    caption: str | tuple | None = ...,
    sparse_index: bool | None = ...,
    sparse_columns: bool | None = ...,
    multirow_align: str | None = ...,
    multicol_align: str | None = ...,
    siunitx: bool = ...,
    environment: str | None = ...,
    encoding: str | None = ...,
    convert_css: bool = ...,

# ==================================================
# Line: 645

def to_latex(
    self,
    buf: None = ...,
    *,
    column_format: str | None = ...,
    position: str | None = ...,
    position_float: str | None = ...,
    hrules: bool | None = ...,
    clines: str | None = ...,
    label: str | None = ...,
    caption: str | tuple | None = ...,
    sparse_index: bool | None = ...,
    sparse_columns: bool | None = ...,
    multirow_align: str | None = ...,
    multicol_align: str | None = ...,
    siunitx: bool = ...,
    environment: str | None = ...,
    encoding: str | None = ...,
    convert_css: bool = ...,

# ==================================================
# Line: 666

def to_latex(
    self,
    buf: FilePath | WriteBuffer[str] | None = None,
    *,
    column_format: str | None = None,
    position: str | None = None,
    position_float: str | None = None,
    hrules: bool | None = None,
    clines: str | None = None,
    label: str | None = None,
    caption: str | tuple | None = None,
    sparse_index: bool | None = None,
    sparse_columns: bool | None = None,
    multirow_align: str | None = None,
    multicol_align: str | None = None,
    siunitx: bool = False,
    environment: str | None = None,
    encoding: str | None = None,
    convert_css: bool = False,

# ==================================================
# Line: 1240

def to_typst(
    self,
    buf: FilePath | WriteBuffer[str],
    *,
    encoding: str | None = ...,
    sparse_index: bool | None = ...,
    sparse_columns: bool | None = ...,
    max_rows: int | None = ...,
    max_columns: int | None = ...,

# ==================================================
# Line: 1252

def to_typst(
    self,
    buf: None = ...,
    *,
    encoding: str | None = ...,
    sparse_index: bool | None = ...,
    sparse_columns: bool | None = ...,
    max_rows: int | None = ...,
    max_columns: int | None = ...,

# ==================================================
# Line: 1264

def to_typst(
    self,
    buf: FilePath | WriteBuffer[str] | None = None,
    *,
    encoding: str | None = None,
    sparse_index: bool | None = None,
    sparse_columns: bool | None = None,
    max_rows: int | None = None,
    max_columns: int | None = None,

# ==================================================
# Line: 1345

def to_html(
    self,
    buf: FilePath | WriteBuffer[str],
    *,
    table_uuid: str | None = ...,
    table_attributes: str | None = ...,
    sparse_index: bool | None = ...,
    sparse_columns: bool | None = ...,
    bold_headers: bool = ...,
    caption: str | None = ...,
    max_rows: int | None = ...,
    max_columns: int | None = ...,
    encoding: str | None = ...,
    doctype_html: bool = ...,
    exclude_styles: bool = ...,
    **kwargs,

# ==================================================
# Line: 1364

def to_html(
    self,
    buf: None = ...,
    *,
    table_uuid: str | None = ...,
    table_attributes: str | None = ...,
    sparse_index: bool | None = ...,
    sparse_columns: bool | None = ...,
    bold_headers: bool = ...,
    caption: str | None = ...,
    max_rows: int | None = ...,
    max_columns: int | None = ...,
    encoding: str | None = ...,
    doctype_html: bool = ...,
    exclude_styles: bool = ...,
    **kwargs,

# ==================================================
# Line: 1383

def to_html(
    self,
    buf: FilePath | WriteBuffer[str] | None = None,
    *,
    table_uuid: str | None = None,
    table_attributes: str | None = None,
    sparse_index: bool | None = None,
    sparse_columns: bool | None = None,
    bold_headers: bool = False,
    caption: str | None = None,
    max_rows: int | None = None,
    max_columns: int | None = None,
    encoding: str | None = None,
    doctype_html: bool = False,
    exclude_styles: bool = False,
    **kwargs,

# ==================================================
# Line: 1529

def to_string(
    self,
    buf: FilePath | WriteBuffer[str],
    *,
    encoding: str | None = ...,
    sparse_index: bool | None = ...,
    sparse_columns: bool | None = ...,
    max_rows: int | None = ...,
    max_columns: int | None = ...,
    delimiter: str = ...,

# ==================================================
# Line: 1542

def to_string(
    self,
    buf: None = ...,
    *,
    encoding: str | None = ...,
    sparse_index: bool | None = ...,
    sparse_columns: bool | None = ...,
    max_rows: int | None = ...,
    max_columns: int | None = ...,
    delimiter: str = ...,

# ==================================================
# Line: 1555

def to_string(
    self,
    buf: FilePath | WriteBuffer[str] | None = None,
    *,
    encoding: str | None = None,
    sparse_index: bool | None = None,
    sparse_columns: bool | None = None,
    max_rows: int | None = None,
    max_columns: int | None = None,
    delimiter: str = " ",

# ==================================================
# Line: 3004

def background_gradient(
    self,
    cmap: str | Colormap = "PuBu",
    low: float = 0,
    high: float = 0,
    axis: Axis | None = 0,
    subset: Subset | None = None,
    text_color_threshold: float = 0.408,
    vmin: float | None = None,
    vmax: float | None = None,
    gmap: Sequence | None = None,

# ==================================================
# Line: 3158

def text_gradient(
    self,
    cmap: str | Colormap = "PuBu",
    low: float = 0,
    high: float = 0,
    axis: Axis | None = 0,
    subset: Subset | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    gmap: Sequence | None = None,

# ==================================================
# Line: 3225

def bar(
    self,
    subset: Subset | None = None,
    axis: Axis | None = 0,
    *,
    color: str | list | tuple | None = None,
    cmap: Any | None = None,
    width: float = 100,
    height: float = 100,
    align: str | float | Callable = "mid",
    vmin: float | None = None,
    vmax: float | None = None,
    props: str = "width: 10em;",

# ==================================================
# Line: 3532

def highlight_between(
    self,
    subset: Subset | None = None,
    color: str = "yellow",
    axis: Axis | None = 0,
    left: Scalar | Sequence | None = None,
    right: Scalar | Sequence | None = None,
    inclusive: IntervalClosedType = "both",
    props: str | None = None,

# ==================================================
# Line: 3649

def highlight_quantile(
    self,
    subset: Subset | None = None,
    color: str = "yellow",
    axis: Axis | None = 0,
    q_left: float = 0.0,
    q_right: float = 1.0,
    interpolation: QuantileInterpolation = "linear",
    inclusive: IntervalClosedType = "both",
    props: str | None = None,

# ==================================================
# Line: 4017

def _background_gradient(
    data,
    cmap: str | Colormap = "PuBu",
    low: float = 0,
    high: float = 0,
    text_color_threshold: float = 0.408,
    vmin: float | None = None,
    vmax: float | None = None,
    gmap: Sequence | np.ndarray | DataFrame | Series | None = None,
    text_only: bool = False,

# ==================================================
# Line: 4161

def _bar(
    data: NDFrame,
    align: str | float | Callable,
    colors: str | list | tuple,
    cmap: Any,
    width: float,
    height: float,
    vmin: float | None,
    vmax: float | None,
    base_css: str,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/format.py
# Line: 194

def __init__(
    self,
    series: Series,
    *,
    length: bool | str = True,
    header: bool = True,
    index: bool = True,
    na_rep: str = "NaN",
    name: bool = False,
    float_format: str | None = None,
    dtype: bool = True,
    max_rows: int | None = None,
    min_rows: int | None = None,

# ==================================================
# Line: 428

def __init__(
    self,
    frame: DataFrame,
    columns: Axes | None = None,
    col_space: ColspaceArgType | None = None,
    header: bool | SequenceNotStr[str] = True,
    index: bool = True,
    na_rep: str = "NaN",
    formatters: FormattersType | None = None,
    justify: str | None = None,
    float_format: FloatFormatType | None = None,
    sparsify: bool | None = None,
    index_names: bool = True,
    max_rows: int | None = None,
    min_rows: int | None = None,
    max_cols: int | None = None,
    show_dimensions: bool | str = False,
    decimal: str = ".",
    bold_rows: bool = False,
    escape: bool = True,

# ==================================================
# Line: 873

def to_html(
    self,
    buf: FilePath | WriteBuffer[str] | None = None,
    encoding: str | None = None,
    classes: str | list | tuple | None = None,
    notebook: bool = False,
    border: int | bool | None = None,
    table_id: str | None = None,
    render_links: bool = False,

# ==================================================
# Line: 954

def to_csv(
    self,
    path_or_buf: FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None = None,
    encoding: str | None = None,
    sep: str = ",",
    columns: Sequence[Hashable] | None = None,
    index_label: IndexLabel | None = None,
    mode: str = "w",
    compression: CompressionOptions = "infer",
    quoting: int | None = None,
    quotechar: str = '"',
    lineterminator: str | None = None,
    chunksize: int | None = None,
    date_format: str | None = None,
    doublequote: bool = True,
    escapechar: str | None = None,
    errors: str = "strict",
    storage_options: StorageOptions | None = None,

# ==================================================
# Line: 1068

def format_array(
    values: ArrayLike,
    formatter: Callable | None,
    float_format: FloatFormatType | None = None,
    na_rep: str = "NaN",
    digits: int | None = None,
    space: str | int | None = None,
    justify: str = "right",
    decimal: str = ".",
    leading_space: bool | None = True,
    quoting: int | None = None,
    fallback_formatter: Callable | None = None,

# ==================================================
# Line: 1154

def __init__(
    self,
    values: ArrayLike,
    digits: int = 7,
    formatter: Callable | None = None,
    na_rep: str = "NaN",
    space: str | int = 12,
    float_format: FloatFormatType | None = None,
    justify: str = "right",
    decimal: str = ".",
    quoting: int | None = None,
    fixed_width: bool = True,
    leading_space: bool | None = True,
    fallback_formatter: Callable | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/common.py
# Line: 628

def get_handle(
    path_or_buf: FilePath | BaseBuffer,
    mode: str,
    *,
    encoding: str | None = ...,
    compression: CompressionOptions = ...,
    memory_map: bool = ...,
    is_text: Literal[False],
    errors: str | None = ...,
    storage_options: StorageOptions = ...,

# ==================================================
# Line: 642

def get_handle(
    path_or_buf: FilePath | BaseBuffer,
    mode: str,
    *,
    encoding: str | None = ...,
    compression: CompressionOptions = ...,
    memory_map: bool = ...,
    is_text: Literal[True] = ...,
    errors: str | None = ...,
    storage_options: StorageOptions = ...,

# ==================================================
# Line: 656

def get_handle(
    path_or_buf: FilePath | BaseBuffer,
    mode: str,
    *,
    encoding: str | None = ...,
    compression: CompressionOptions = ...,
    memory_map: bool = ...,
    is_text: bool = ...,
    errors: str | None = ...,
    storage_options: StorageOptions = ...,

# ==================================================
# Line: 670

def get_handle(
    path_or_buf: FilePath | BaseBuffer,
    mode: str,
    *,
    encoding: str | None = None,
    compression: CompressionOptions | None = None,
    memory_map: bool = False,
    is_text: bool = True,
    errors: str | None = None,
    storage_options: StorageOptions | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/generic.py
# Line: 964

def _rename(
    self,
    mapper: Renamer | None = ...,
    *,
    index: Renamer | None = ...,
    columns: Renamer | None = ...,
    axis: Axis | None = ...,
    inplace: Literal[False] = ...,
    level: Level | None = ...,
    errors: str = ...,

# ==================================================
# Line: 977

def _rename(
    self,
    mapper: Renamer | None = ...,
    *,
    index: Renamer | None = ...,
    columns: Renamer | None = ...,
    axis: Axis | None = ...,
    inplace: Literal[True],
    level: Level | None = ...,
    errors: str = ...,

# ==================================================
# Line: 990

def _rename(
    self,
    mapper: Renamer | None = ...,
    *,
    index: Renamer | None = ...,
    columns: Renamer | None = ...,
    axis: Axis | None = ...,
    inplace: bool,
    level: Level | None = ...,
    errors: str = ...,

# ==================================================
# Line: 1003

def _rename(
    self,
    mapper: Renamer | None = None,
    *,
    index: Renamer | None = None,
    columns: Renamer | None = None,
    axis: Axis | None = None,
    inplace: bool = False,
    level: Level | None = None,
    errors: str = "ignore",

# ==================================================
# Line: 1073

def rename_axis(
    self,
    mapper: IndexLabel | lib.NoDefault = ...,
    *,
    index=...,
    columns=...,
    axis: Axis = ...,
    copy: bool | lib.NoDefault = lib.no_default,
    inplace: Literal[False] = ...,

# ==================================================
# Line: 1085

def rename_axis(
    self,
    mapper: IndexLabel | lib.NoDefault = ...,
    *,
    index=...,
    columns=...,
    axis: Axis = ...,
    copy: bool | lib.NoDefault = lib.no_default,
    inplace: Literal[True],

# ==================================================
# Line: 1097

def rename_axis(
    self,
    mapper: IndexLabel | lib.NoDefault = ...,
    *,
    index=...,
    columns=...,
    axis: Axis = ...,
    copy: bool | lib.NoDefault = lib.no_default,
    inplace: bool = ...,

# ==================================================
# Line: 1108

def rename_axis(
    self,
    mapper: IndexLabel | lib.NoDefault = lib.no_default,
    *,
    index=lib.no_default,
    columns=lib.no_default,
    axis: Axis = 0,
    copy: bool | lib.NoDefault = lib.no_default,
    inplace: bool = False,

# ==================================================
# Line: 2151

def to_excel(
    self,
    excel_writer: FilePath | WriteExcelBuffer | ExcelWriter,
    *,
    sheet_name: str = "Sheet1",
    na_rep: str = "",
    float_format: str | None = None,
    columns: Sequence[Hashable] | None = None,
    header: Sequence[Hashable] | bool = True,
    index: bool = True,
    index_label: IndexLabel | None = None,
    startrow: int = 0,
    startcol: int = 0,
    engine: Literal["openpyxl", "xlsxwriter"] | None = None,
    merge_cells: bool = True,
    inf_rep: str = "inf",
    freeze_panes: tuple[int, int] | None = None,
    storage_options: StorageOptions | None = None,
    engine_kwargs: dict[str, Any] | None = None,

# ==================================================
# Line: 2319

def to_json(
    self,
    path_or_buf: FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None = None,
    *,
    orient: Literal["split", "records", "index", "table", "columns", "values"]
    | None = None,
    date_format: str | None = None,
    double_precision: int = 10,
    force_ascii: bool = True,
    date_unit: TimeUnit = "ms",
    default_handler: Callable[[Any], JSONSerializable] | None = None,
    lines: bool = False,
    compression: CompressionOptions = "infer",
    index: bool | None = None,
    indent: int | None = None,
    storage_options: StorageOptions | None = None,
    mode: Literal["a", "w"] = "w",

# ==================================================
# Line: 2626

def to_hdf(
    self,
    path_or_buf: FilePath | HDFStore,
    *,
    key: str,
    mode: Literal["a", "w", "r+"] = "a",
    complevel: int | None = None,
    complib: Literal["zlib", "lzo", "bzip2", "blosc"] | None = None,
    append: bool = False,
    format: Literal["fixed", "table"] | None = None,
    index: bool = True,
    min_itemsize: int | dict[str, int] | None = None,
    nan_rep=None,
    dropna: bool | None = None,
    data_columns: Literal[True] | list[str] | None = None,
    errors: OpenFileErrors = "strict",
    encoding: str = "UTF-8",

# ==================================================
# Line: 2780

def to_sql(
    self,
    name: str,
    con,
    *,
    schema: str | None = None,
    if_exists: Literal["fail", "replace", "append", "delete_rows"] = "fail",
    index: bool = True,
    index_label: IndexLabel | None = None,
    chunksize: int | None = None,
    dtype: DtypeArg | None = None,
    method: Literal["multi"] | Callable | None = None,

# ==================================================
# Line: 3279

def to_latex(
    self,
    buf: None = ...,
    *,
    columns: Sequence[Hashable] | None = ...,
    header: bool | SequenceNotStr[str] = ...,
    index: bool = ...,
    na_rep: str = ...,
    formatters: FormattersType | None = ...,
    float_format: FloatFormatType | None = ...,
    sparsify: bool | None = ...,
    index_names: bool = ...,
    bold_rows: bool = ...,
    column_format: str | None = ...,
    longtable: bool | None = ...,
    escape: bool | None = ...,
    encoding: str | None = ...,
    decimal: str = ...,
    multicolumn: bool | None = ...,
    multicolumn_format: str | None = ...,
    multirow: bool | None = ...,
    caption: str | tuple[str, str] | None = ...,
    label: str | None = ...,
    position: str | None = ...,

# ==================================================
# Line: 3306

def to_latex(
    self,
    buf: FilePath | WriteBuffer[str],
    *,
    columns: Sequence[Hashable] | None = ...,
    header: bool | SequenceNotStr[str] = ...,
    index: bool = ...,
    na_rep: str = ...,
    formatters: FormattersType | None = ...,
    float_format: FloatFormatType | None = ...,
    sparsify: bool | None = ...,
    index_names: bool = ...,
    bold_rows: bool = ...,
    column_format: str | None = ...,
    longtable: bool | None = ...,
    escape: bool | None = ...,
    encoding: str | None = ...,
    decimal: str = ...,
    multicolumn: bool | None = ...,
    multicolumn_format: str | None = ...,
    multirow: bool | None = ...,
    caption: str | tuple[str, str] | None = ...,
    label: str | None = ...,
    position: str | None = ...,

# ==================================================
# Line: 3333

def to_latex(
    self,
    buf: FilePath | WriteBuffer[str] | None = None,
    *,
    columns: Sequence[Hashable] | None = None,
    header: bool | SequenceNotStr[str] = True,
    index: bool = True,
    na_rep: str = "NaN",
    formatters: FormattersType | None = None,
    float_format: FloatFormatType | None = None,
    sparsify: bool | None = None,
    index_names: bool = True,
    bold_rows: bool = False,
    column_format: str | None = None,
    longtable: bool | None = None,
    escape: bool | None = None,
    encoding: str | None = None,
    decimal: str = ".",
    multicolumn: bool | None = None,
    multicolumn_format: str | None = None,
    multirow: bool | None = None,
    caption: str | tuple[str, str] | None = None,
    label: str | None = None,
    position: str | None = None,

# ==================================================
# Line: 3621

def _to_latex_via_styler(
    self,
    buf=None,
    *,
    hide: dict | list[dict] | None = None,
    relabel_index: dict | list[dict] | None = None,
    format: dict | list[dict] | None = None,
    format_index: dict | list[dict] | None = None,
    format_index_names: dict | list[dict] | None = None,
    render_kwargs: dict | None = None,

# ==================================================
# Line: 3696

def to_csv(
    self,
    path_or_buf: None = ...,
    *,
    sep: str = ...,
    na_rep: str = ...,
    float_format: str | Callable | None = ...,
    columns: Sequence[Hashable] | None = ...,
    header: bool | list[str] = ...,
    index: bool = ...,
    index_label: IndexLabel | None = ...,
    mode: str = ...,
    encoding: str | None = ...,
    compression: CompressionOptions = ...,
    quoting: int | None = ...,
    quotechar: str = ...,
    lineterminator: str | None = ...,
    chunksize: int | None = ...,
    date_format: str | None = ...,
    doublequote: bool = ...,
    escapechar: str | None = ...,
    decimal: str = ...,
    errors: OpenFileErrors = ...,
    storage_options: StorageOptions = ...,

# ==================================================
# Line: 3723

def to_csv(
    self,
    path_or_buf: FilePath | WriteBuffer[bytes] | WriteBuffer[str],
    *,
    sep: str = ...,
    na_rep: str = ...,
    float_format: str | Callable | None = ...,
    columns: Sequence[Hashable] | None = ...,
    header: bool | list[str] = ...,
    index: bool = ...,
    index_label: IndexLabel | None = ...,
    mode: str = ...,
    encoding: str | None = ...,
    compression: CompressionOptions = ...,
    quoting: int | None = ...,
    quotechar: str = ...,
    lineterminator: str | None = ...,
    chunksize: int | None = ...,
    date_format: str | None = ...,
    doublequote: bool = ...,
    escapechar: str | None = ...,
    decimal: str = ...,
    errors: OpenFileErrors = ...,
    storage_options: StorageOptions = ...,

# ==================================================
# Line: 3754

def to_csv(
    self,
    path_or_buf: FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None = None,
    *,
    sep: str = ",",
    na_rep: str = "",
    float_format: str | Callable | None = None,
    columns: Sequence[Hashable] | None = None,
    header: bool | list[str] = True,
    index: bool = True,
    index_label: IndexLabel | None = None,
    mode: str = "w",
    encoding: str | None = None,
    compression: CompressionOptions = "infer",
    quoting: int | None = None,
    quotechar: str = '"',
    lineterminator: str | None = None,
    chunksize: int | None = None,
    date_format: str | None = None,
    doublequote: bool = True,
    escapechar: str | None = None,
    decimal: str = ".",
    errors: OpenFileErrors = "strict",
    storage_options: StorageOptions | None = None,

# ==================================================
# Line: 4516

def drop(
    self,
    labels: IndexLabel | ListLike = ...,
    *,
    axis: Axis = ...,
    index: IndexLabel | ListLike = ...,
    columns: IndexLabel | ListLike = ...,
    level: Level | None = ...,
    inplace: Literal[True],
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 4529

def drop(
    self,
    labels: IndexLabel | ListLike = ...,
    *,
    axis: Axis = ...,
    index: IndexLabel | ListLike = ...,
    columns: IndexLabel | ListLike = ...,
    level: Level | None = ...,
    inplace: Literal[False] = ...,
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 4542

def drop(
    self,
    labels: IndexLabel | ListLike = ...,
    *,
    axis: Axis = ...,
    index: IndexLabel | ListLike = ...,
    columns: IndexLabel | ListLike = ...,
    level: Level | None = ...,
    inplace: bool = ...,
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 4554

def drop(
    self,
    labels: IndexLabel | ListLike = None,
    *,
    axis: Axis = 0,
    index: IndexLabel | ListLike = None,
    columns: IndexLabel | ListLike = None,
    level: Level | None = None,
    inplace: bool = False,
    errors: IgnoreRaise = "raise",

# ==================================================
# Line: 4836

def sort_values(
    self,
    *,
    axis: Axis = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: Literal[False] = ...,
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    ignore_index: bool = ...,
    key: ValueKeyFunc = ...,

# ==================================================
# Line: 4849

def sort_values(
    self,
    *,
    axis: Axis = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: Literal[True],
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    ignore_index: bool = ...,
    key: ValueKeyFunc = ...,

# ==================================================
# Line: 4862

def sort_values(
    self,
    *,
    axis: Axis = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: bool = ...,
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    ignore_index: bool = ...,
    key: ValueKeyFunc = ...,

# ==================================================
# Line: 4874

def sort_values(
    self,
    *,
    axis: Axis = 0,
    ascending: bool | Sequence[bool] = True,
    inplace: bool = False,
    kind: SortKind = "quicksort",
    na_position: NaPosition = "last",
    ignore_index: bool = False,
    key: ValueKeyFunc | None = None,

# ==================================================
# Line: 5031

def sort_index(
    self,
    *,
    axis: Axis = ...,
    level: IndexLabel = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: Literal[True],
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    sort_remaining: bool = ...,
    ignore_index: bool = ...,
    key: IndexKeyFunc = ...,

# ==================================================
# Line: 5046

def sort_index(
    self,
    *,
    axis: Axis = ...,
    level: IndexLabel = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: Literal[False] = ...,
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    sort_remaining: bool = ...,
    ignore_index: bool = ...,
    key: IndexKeyFunc = ...,

# ==================================================
# Line: 5061

def sort_index(
    self,
    *,
    axis: Axis = ...,
    level: IndexLabel = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: bool = ...,
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    sort_remaining: bool = ...,
    ignore_index: bool = ...,
    key: IndexKeyFunc = ...,

# ==================================================
# Line: 5075

def sort_index(
    self,
    *,
    axis: Axis = 0,
    level: IndexLabel | None = None,
    ascending: bool | Sequence[bool] = True,
    inplace: bool = False,
    kind: SortKind = "quicksort",
    na_position: NaPosition = "last",
    sort_remaining: bool = True,
    ignore_index: bool = False,
    key: IndexKeyFunc | None = None,

# ==================================================
# Line: 5135

def reindex(
    self,
    labels=None,
    *,
    index=None,
    columns=None,
    axis: Axis | None = None,
    method: ReindexMethod | None = None,
    copy: bool | lib.NoDefault = lib.no_default,
    level: Level | None = None,
    fill_value: Scalar | None = np.nan,
    limit: int | None = None,
    tolerance=None,

# ==================================================
# Line: 5408

def _reindex_axes(
    self,
    axes,
    level: Level | None,
    limit: int | None,
    tolerance,
    method,
    fill_value: Scalar | None,

# ==================================================
# Line: 5781

def sample(
    self,
    n: int | None = None,
    frac: float | None = None,
    replace: bool = False,
    weights=None,
    random_state: RandomState | None = None,
    axis: Axis | None = None,
    ignore_index: bool = False,

# ==================================================
# Line: 6706

def convert_dtypes(
    self,
    infer_objects: bool = True,
    convert_string: bool = True,
    convert_integer: bool = True,
    convert_boolean: bool = True,
    convert_floating: bool = True,
    dtype_backend: DtypeBackend = "numpy_nullable",

# ==================================================
# Line: 7650

def interpolate(
    self,
    method: InterpolateOptions = ...,
    *,
    axis: Axis = ...,
    limit: int | None = ...,
    inplace: Literal[False] = ...,
    limit_direction: Literal["forward", "backward", "both"] | None = ...,
    limit_area: Literal["inside", "outside"] | None = ...,
    **kwargs,

# ==================================================
# Line: 7663

def interpolate(
    self,
    method: InterpolateOptions = ...,
    *,
    axis: Axis = ...,
    limit: int | None = ...,
    inplace: Literal[True],
    limit_direction: Literal["forward", "backward", "both"] | None = ...,
    limit_area: Literal["inside", "outside"] | None = ...,
    **kwargs,

# ==================================================
# Line: 7676

def interpolate(
    self,
    method: InterpolateOptions = ...,
    *,
    axis: Axis = ...,
    limit: int | None = ...,
    inplace: bool = ...,
    limit_direction: Literal["forward", "backward", "both"] | None = ...,
    limit_area: Literal["inside", "outside"] | None = ...,
    **kwargs,

# ==================================================
# Line: 7689

def interpolate(
    self,
    method: InterpolateOptions = "linear",
    *,
    axis: Axis = 0,
    limit: int | None = None,
    inplace: bool = False,
    limit_direction: Literal["forward", "backward", "both"] | None = None,
    limit_area: Literal["inside", "outside"] | None = None,
    **kwargs,

# ==================================================
# Line: 8774

def resample(
    self,
    rule,
    closed: Literal["right", "left"] | None = None,
    label: Literal["right", "left"] | None = None,
    convention: Literal["start", "end", "s", "e"] | lib.NoDefault = lib.no_default,
    on: Level | None = None,
    level: Level | None = None,
    origin: str | TimestampConvertibleTypes = "start_day",
    offset: TimedeltaConvertibleTypes | None = None,
    group_keys: bool = False,

# ==================================================
# Line: 9129

def rank(
    self,
    axis: Axis = 0,
    method: Literal["average", "min", "max", "first", "dense"] = "average",
    numeric_only: bool = False,
    na_option: Literal["keep", "top", "bottom"] = "keep",
    ascending: bool = True,
    pct: bool = False,

# ==================================================
# Line: 9375

def align(
    self,
    other: NDFrameT,
    join: AlignJoin = "outer",
    axis: Axis | None = None,
    level: Level | None = None,
    copy: bool | lib.NoDefault = lib.no_default,
    fill_value: Hashable | None = None,

# ==================================================
# Line: 10588

def tz_localize(
    self,
    tz,
    axis: Axis = 0,
    level=None,
    copy: bool | lib.NoDefault = lib.no_default,
    ambiguous: TimeAmbiguous = "raise",
    nonexistent: TimeNonexistent = "raise",

# ==================================================
# Line: 11342

def _stat_function_ddof(
    self,
    name: str,
    func,
    axis: Axis | None = 0,
    skipna: bool = True,
    ddof: int = 1,
    numeric_only: bool = False,
    **kwargs,

# ==================================================
# Line: 11502

def _min_count_stat_function(
    self,
    name: str,
    func,
    axis: Axis | None = 0,
    skipna: bool = True,
    numeric_only: bool = False,
    min_count: int = 0,
    **kwargs,

# ==================================================
# Line: 11562

def rolling(
    self,
    window: int | dt.timedelta | str | BaseOffset | BaseIndexer,
    min_periods: int | None = None,
    center: bool = False,
    win_type: str | None = None,
    on: str | None = None,
    closed: IntervalClosedType | None = None,
    step: int | None = None,
    method: str = "single",

# ==================================================
# Line: 11609

def ewm(
    self,
    com: float | None = None,
    span: float | None = None,
    halflife: float | TimedeltaConvertibleTypes | None = None,
    alpha: float | None = None,
    min_periods: int | None = 0,
    adjust: bool = True,
    ignore_na: bool = False,
    times: np.ndarray | DataFrame | Series | None = None,
    method: Literal["single", "table"] = "single",

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/missing.py
# Line: 347

def interpolate_2d_inplace(
    data: np.ndarray,  # floating dtype
    index: Index,
    axis: AxisInt,
    method: str = "linear",
    limit: int | None = None,
    limit_direction: str = "forward",
    limit_area: str | None = None,
    fill_value: Any | None = None,
    mask=None,
    **kwargs,

# ==================================================
# Line: 433

def _interpolate_1d(
    indices: np.ndarray,
    yvalues: np.ndarray,
    method: str = "linear",
    limit: int | None = None,
    limit_direction: str = "forward",
    limit_area: Literal["inside", "outside"] | None = None,
    fill_value: Any | None = None,
    bounds_error: bool = False,
    order: int | None = None,
    mask=None,
    **kwargs,

# ==================================================
# Line: 545

def _interpolate_scipy_wrapper(
    x: np.ndarray,
    y: np.ndarray,
    new_x: np.ndarray,
    method: str,
    fill_value=None,
    bounds_error: bool = False,
    order=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/generic.py
# Line: 1563

def hist(
    self,
    by=None,
    ax=None,
    grid: bool = True,
    xlabelsize: int | None = None,
    xrot: float | None = None,
    ylabelsize: int | None = None,
    yrot: float | None = None,
    figsize: tuple[float, float] | None = None,
    bins: int | Sequence[int] = 10,
    backend: str | None = None,
    legend: bool = False,
    **kwargs,

# ==================================================
# Line: 3134

def hist(
    self,
    column: IndexLabel | None = None,
    by=None,
    grid: bool = True,
    xlabelsize: int | None = None,
    xrot: float | None = None,
    ylabelsize: int | None = None,
    yrot: float | None = None,
    ax=None,
    sharex: bool = False,
    sharey: bool = False,
    figsize: tuple[float, float] | None = None,
    layout: tuple[int, int] | None = None,
    bins: int | Sequence[int] = 10,
    backend: str | None = None,
    legend: bool = False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/grouper.py
# Line: 444

def __init__(
    self,
    index: Index,
    grouper=None,
    obj: NDFrame | None = None,
    level=None,
    sort: bool = True,
    observed: bool = False,
    in_axis: bool = False,
    dropna: bool = True,
    uniques: ArrayLike | None = None,

# ==================================================
# Line: 711

def get_grouper(
    obj: NDFrameT,
    key=None,
    level=None,
    sort: bool = True,
    observed: bool = False,
    validate: bool = True,
    dropna: bool = True,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/ops.py
# Line: 313

def _cython_op_ndim_compat(
    self,
    values: np.ndarray,
    *,
    min_count: int,
    ngroups: int,
    comp_ids: np.ndarray,
    mask: npt.NDArray[np.bool_] | None = None,
    result_mask: npt.NDArray[np.bool_] | None = None,
    **kwargs,

# ==================================================
# Line: 357

def _call_cython_op(
    self,
    values: np.ndarray,  # np.ndarray[ndim=2]
    *,
    min_count: int,
    ngroups: int,
    comp_ids: np.ndarray,
    mask: npt.NDArray[np.bool_] | None,
    result_mask: npt.NDArray[np.bool_] | None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/groupby.py
# Line: 1044

def __init__(
    self,
    obj: NDFrameT,
    keys: _KeysArgType | None = None,
    level: IndexLabel | None = None,
    grouper: ops.BaseGrouper | None = None,
    exclusions: frozenset[Hashable] | None = None,
    selection: IndexLabel | None = None,
    as_index: bool = True,
    sort: bool = True,
    group_keys: bool = True,
    observed: bool = False,
    dropna: bool = True,

# ==================================================
# Line: 3654

def rolling(
    self,
    window: int | datetime.timedelta | str | BaseOffset | BaseIndexer,
    min_periods: int | None = None,
    center: bool = False,
    win_type: str | None = None,
    on: str | None = None,
    closed: IntervalClosedType | None = None,
    method: str = "single",

# ==================================================
# Line: 3883

def ewm(
    self,
    com: float | None = None,
    span: float | None = None,
    halflife: float | str | Timedelta | None = None,
    alpha: float | None = None,
    min_periods: int | None = 0,
    adjust: bool = True,
    ignore_na: bool = False,
    times: np.ndarray | Series | None = None,
    method: str = "single",

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/tools/datetimes.py
# Line: 318

def _convert_listlike_datetimes(
    arg,
    format: str | None,
    name: Hashable | None = None,
    utc: bool = False,
    unit: str | None = None,
    errors: DateTimeErrorChoices = "raise",
    dayfirst: bool | None = None,
    yearfirst: bool | None = None,
    exact: bool = True,

# ==================================================
# Line: 624

def to_datetime(
    arg: DatetimeScalar,
    errors: DateTimeErrorChoices = ...,
    dayfirst: bool = ...,
    yearfirst: bool = ...,
    utc: bool = ...,
    format: str | None = ...,
    exact: bool = ...,
    unit: str | None = ...,
    origin=...,
    cache: bool = ...,

# ==================================================
# Line: 639

def to_datetime(
    arg: Series | DictConvertible,
    errors: DateTimeErrorChoices = ...,
    dayfirst: bool = ...,
    yearfirst: bool = ...,
    utc: bool = ...,
    format: str | None = ...,
    exact: bool = ...,
    unit: str | None = ...,
    origin=...,
    cache: bool = ...,

# ==================================================
# Line: 654

def to_datetime(
    arg: list | tuple | Index | ArrayLike,
    errors: DateTimeErrorChoices = ...,
    dayfirst: bool = ...,
    yearfirst: bool = ...,
    utc: bool = ...,
    format: str | None = ...,
    exact: bool = ...,
    unit: str | None = ...,
    origin=...,
    cache: bool = ...,

# ==================================================
# Line: 668

def to_datetime(
    arg: DatetimeScalarOrArrayConvertible | DictConvertible,
    errors: DateTimeErrorChoices = "raise",
    dayfirst: bool = False,
    yearfirst: bool = False,
    utc: bool = False,
    format: str | None = None,
    exact: bool | lib.NoDefault = lib.no_default,
    unit: str | None = None,
    origin: str = "unix",
    cache: bool = True,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/apply.py
# Line: 181

def frame_apply(
    obj: DataFrame,
    func: AggFuncType,
    axis: Axis = 0,
    raw: bool = False,
    result_type: str | None = None,
    by_row: Literal[False, "compat"] = "compat",
    engine: str = "python",
    engine_kwargs: dict[str, bool] | None = None,
    args=None,
    kwargs=None,

# ==================================================
# Line: 223

def __init__(
    self,
    obj: AggObjType,
    func: AggFuncType,
    raw: bool,
    result_type: str | None,
    *,
    by_row: Literal[False, "compat", "_compat"] = "compat",
    engine: str = "python",
    engine_kwargs: dict[str, bool] | None = None,
    args,
    kwargs,

# ==================================================
# Line: 864

def __init__(
    self,
    obj: AggObjType,
    func: AggFuncType,
    raw: bool,
    result_type: str | None,
    *,
    by_row: Literal[False, "compat"] = False,
    engine: str = "python",
    engine_kwargs: dict[str, bool] | None = None,
    args,
    kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/window/rolling.py
# Line: 139

def __init__(
    self,
    obj: NDFrame,
    window=None,
    min_periods: int | None = None,
    center: bool | None = False,
    win_type: str | None = None,
    on: str | Index | None = None,
    closed: str | None = None,
    step: int | None = None,
    method: str = "single",
    *,
    selection=None,

# ==================================================
# Line: 1481

def apply(
    self,
    func: Callable[..., Any],
    raw: bool = False,
    engine: Literal["cython", "numba"] | None = None,
    engine_kwargs: dict[str, bool] | None = None,
    args: tuple[Any, ...] | None = None,
    kwargs: dict[str, Any] | None = None,

# ==================================================
# Line: 2098

def apply(
    self,
    func: Callable[..., Any],
    raw: bool = False,
    engine: Literal["cython", "numba"] | None = None,
    engine_kwargs: dict[str, bool] | None = None,
    args: tuple[Any, ...] | None = None,
    kwargs: dict[str, Any] | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/window/numba_.py
# Line: 82

def generate_numba_ewm_func(
    nopython: bool,
    nogil: bool,
    parallel: bool,
    com: float,
    adjust: bool,
    ignore_na: bool,
    deltas: tuple,
    normalize: bool,

# ==================================================
# Line: 266

def generate_numba_ewm_table_func(
    nopython: bool,
    nogil: bool,
    parallel: bool,
    com: float,
    adjust: bool,
    ignore_na: bool,
    deltas: tuple,
    normalize: bool,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/window/ewm.py
# Line: 331

def __init__(
    self,
    obj: NDFrame,
    com: float | None = None,
    span: float | None = None,
    halflife: float | TimedeltaConvertibleTypes | None = None,
    alpha: float | None = None,
    min_periods: int | None = 0,
    adjust: bool = True,
    ignore_na: bool = False,
    times: np.ndarray | NDFrame | None = None,
    method: str = "single",
    *,
    selection=None,

# ==================================================
# Line: 939

def __init__(
    self,
    obj: NDFrame,
    com: float | None = None,
    span: float | None = None,
    halflife: float | TimedeltaConvertibleTypes | None = None,
    alpha: float | None = None,
    min_periods: int | None = 0,
    adjust: bool = True,
    ignore_na: bool = False,
    times: np.ndarray | NDFrame | None = None,
    engine: str = "numba",
    engine_kwargs: dict[str, bool] | None = None,
    *,
    selection=None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/window/online.py
# Line: 38

def online_ewma(
    values: np.ndarray,
    deltas: np.ndarray,
    minimum_periods: int,
    old_wt_factor: float,
    new_wt: float,
    old_wt: np.ndarray,
    adjust: bool,
    ignore_na: bool,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/window/expanding.py
# Line: 237

def apply(
    self,
    func: Callable[..., Any],
    raw: bool = False,
    engine: Literal["cython", "numba"] | None = None,
    engine_kwargs: dict[str, bool] | None = None,
    args: tuple[Any, ...] | None = None,
    kwargs: dict[str, Any] | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/sorting.py
# Line: 58

def get_indexer_indexer(
    target: Index,
    level: Level | list[Level] | None,
    ascending: list[bool] | bool,
    kind: SortKind,
    na_position: NaPosition,
    sort_remaining: bool,
    key: IndexKeyFunc,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/strings/base.py
# Line: 75

def _str_replace(
    self,
    pat: str | re.Pattern,
    repl: str | Callable,
    n: int = -1,
    case: bool = True,
    flags: int = 0,
    regex: bool = True,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/strings/object_array.py
# Line: 191

def _str_replace(
    self,
    pat: str | re.Pattern,
    repl: str | Callable,
    n: int = -1,
    case: bool = True,
    flags: int = 0,
    regex: bool = True,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/strings/accessor.py
# Line: 274

def _wrap_result(
    self,
    result,
    name=None,
    expand: bool | None = None,
    fill_value=np.nan,
    returns_string: bool = True,
    dtype=None,

# ==================================================
# Line: 1478

def replace(
    self,
    pat: str | re.Pattern | dict,
    repl: str | Callable | None = None,
    n: int = -1,
    case: bool | None = None,
    flags: int = 0,
    regex: bool = False,

# ==================================================
# Line: 2369

def wrap(
    self,
    width: int,
    expand_tabs: bool = True,
    tabsize: int = 8,
    replace_whitespace: bool = True,
    drop_whitespace: bool = True,
    initial_indent: str = "",
    subsequent_indent: str = "",
    fix_sentence_endings: bool = False,
    break_long_words: bool = True,
    break_on_hyphens: bool = True,
    max_lines: int | None = None,
    placeholder: str = " [...]",

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/range.py
# Line: 152

def __new__(
    cls,
    start=None,
    stop=None,
    step=None,
    dtype: Dtype | None = None,
    copy: bool = False,
    name: Hashable | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/category.py
# Line: 205

def __new__(
    cls,
    data=None,
    categories=None,
    ordered=None,
    dtype: Dtype | None = None,
    copy: bool = False,
    name: Hashable | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/timedeltas.py
# Line: 241

def timedelta_range(
    start=None,
    end=None,
    periods: int | None = None,
    freq=None,
    name=None,
    closed=None,
    *,
    unit: str | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/interval.py
# Line: 226

def __new__(
    cls,
    data,
    closed: IntervalClosedType | None = None,
    dtype: Dtype | None = None,
    copy: bool = False,
    name: Hashable | None = None,
    verify_integrity: bool = True,

# ==================================================
# Line: 304

def from_arrays(
    cls,
    left,
    right,
    closed: IntervalClosedType = "right",
    name: Hashable | None = None,
    copy: bool = False,
    dtype: Dtype | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/datetimes.py
# Line: 309

def __new__(
    cls,
    data=None,
    freq: Frequency | lib.NoDefault = lib.no_default,
    tz=lib.no_default,
    ambiguous: TimeAmbiguous = "raise",
    dayfirst: bool = False,
    yearfirst: bool = False,
    dtype: Dtype | None = None,
    copy: bool = False,
    name: Hashable | None = None,

# ==================================================
# Line: 820

def date_range(
    start=None,
    end=None,
    periods=None,
    freq=None,
    tz=None,
    normalize: bool = False,
    name: Hashable | None = None,
    inclusive: IntervalClosedType = "both",
    *,
    unit: str | None = None,
    **kwargs,

# ==================================================
# Line: 1025

def bdate_range(
    start=None,
    end=None,
    periods: int | None = None,
    freq: Frequency | dt.timedelta = "B",
    tz=None,
    normalize: bool = True,
    name: Hashable | None = None,
    weekmask=None,
    holidays=None,
    inclusive: IntervalClosedType = "both",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/period.py
# Line: 248

def from_fields(
    cls,
    *,
    year=None,
    quarter=None,
    month=None,
    day=None,
    hour=None,
    minute=None,
    second=None,
    freq=None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/multi.py
# Line: 301

def __new__(
    cls,
    levels=None,
    codes=None,
    sortorder=None,
    names=None,
    copy: bool = False,
    name=None,
    verify_integrity: bool = True,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/dtypes/cast.py
# Line: 984

def convert_dtypes(
    input_array: ArrayLike,
    convert_string: bool = True,
    convert_integer: bool = True,
    convert_boolean: bool = True,
    convert_floating: bool = True,
    infer_objects: bool = False,
    dtype_backend: Literal["numpy_nullable", "pyarrow"] = "numpy_nullable",

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/series.py
# Line: 1443

def to_string(
    self,
    buf: None = ...,
    *,
    na_rep: str = ...,
    float_format: str | None = ...,
    header: bool = ...,
    index: bool = ...,
    length: bool = ...,
    dtype=...,
    name=...,
    max_rows: int | None = ...,
    min_rows: int | None = ...,

# ==================================================
# Line: 1459

def to_string(
    self,
    buf: FilePath | WriteBuffer[str],
    *,
    na_rep: str = ...,
    float_format: str | None = ...,
    header: bool = ...,
    index: bool = ...,
    length: bool = ...,
    dtype=...,
    name=...,
    max_rows: int | None = ...,
    min_rows: int | None = ...,

# ==================================================
# Line: 1477

def to_string(
    self,
    buf: FilePath | WriteBuffer[str] | None = None,
    na_rep: str = "NaN",
    float_format: str | None = None,
    header: bool = True,
    index: bool = True,
    length: bool = False,
    dtype: bool = False,
    name: bool = False,
    max_rows: int | None = None,
    min_rows: int | None = None,

# ==================================================
# Line: 1967

def groupby(
    self,
    by=None,
    level: IndexLabel | None = None,
    as_index: bool = True,
    sort: bool = True,
    group_keys: bool = True,
    observed: bool = False,
    dropna: bool = True,

# ==================================================
# Line: 3360

def sort_values(
    self,
    *,
    axis: Axis = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: Literal[False] = ...,
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    ignore_index: bool = ...,
    key: ValueKeyFunc = ...,

# ==================================================
# Line: 3373

def sort_values(
    self,
    *,
    axis: Axis = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: Literal[True],
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    ignore_index: bool = ...,
    key: ValueKeyFunc = ...,

# ==================================================
# Line: 3386

def sort_values(
    self,
    *,
    axis: Axis = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: bool = ...,
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    ignore_index: bool = ...,
    key: ValueKeyFunc = ...,

# ==================================================
# Line: 3398

def sort_values(
    self,
    *,
    axis: Axis = 0,
    ascending: bool | Sequence[bool] = True,
    inplace: bool = False,
    kind: SortKind = "quicksort",
    na_position: NaPosition = "last",
    ignore_index: bool = False,
    key: ValueKeyFunc | None = None,

# ==================================================
# Line: 3593

def sort_index(
    self,
    *,
    axis: Axis = ...,
    level: IndexLabel = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: Literal[True],
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    sort_remaining: bool = ...,
    ignore_index: bool = ...,
    key: IndexKeyFunc = ...,

# ==================================================
# Line: 3608

def sort_index(
    self,
    *,
    axis: Axis = ...,
    level: IndexLabel = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: Literal[False] = ...,
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    sort_remaining: bool = ...,
    ignore_index: bool = ...,
    key: IndexKeyFunc = ...,

# ==================================================
# Line: 3623

def sort_index(
    self,
    *,
    axis: Axis = ...,
    level: IndexLabel = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: bool = ...,
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    sort_remaining: bool = ...,
    ignore_index: bool = ...,
    key: IndexKeyFunc = ...,

# ==================================================
# Line: 3637

def sort_index(
    self,
    *,
    axis: Axis = 0,
    level: IndexLabel | None = None,
    ascending: bool | Sequence[bool] = True,
    inplace: bool = False,
    kind: SortKind = "quicksort",
    na_position: NaPosition = "last",
    sort_remaining: bool = True,
    ignore_index: bool = False,
    key: IndexKeyFunc | None = None,

# ==================================================
# Line: 4703

def rename(
    self,
    index: Renamer | Hashable | None = ...,
    *,
    axis: Axis | None = ...,
    copy: bool | lib.NoDefault = ...,
    inplace: Literal[True],
    level: Level | None = ...,
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 4715

def rename(
    self,
    index: Renamer | Hashable | None = ...,
    *,
    axis: Axis | None = ...,
    copy: bool | lib.NoDefault = ...,
    inplace: Literal[False] = ...,
    level: Level | None = ...,
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 4726

def rename(
    self,
    index: Renamer | Hashable | None = None,
    *,
    axis: Axis | None = None,
    copy: bool | lib.NoDefault = lib.no_default,
    inplace: bool = False,
    level: Level | None = None,
    errors: IgnoreRaise = "ignore",

# ==================================================
# Line: 4876

def reindex(  # type: ignore[override]
    self,
    index=None,
    *,
    axis: Axis | None = None,
    method: ReindexMethod | None = None,
    copy: bool | lib.NoDefault = lib.no_default,
    level: Level | None = None,
    fill_value: Scalar | None = None,
    limit: int | None = None,
    tolerance=None,

# ==================================================
# Line: 5010

def drop(
    self,
    labels: IndexLabel | ListLike = ...,
    *,
    axis: Axis = ...,
    index: IndexLabel | ListLike = ...,
    columns: IndexLabel | ListLike = ...,
    level: Level | None = ...,
    inplace: Literal[True],
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 5023

def drop(
    self,
    labels: IndexLabel | ListLike = ...,
    *,
    axis: Axis = ...,
    index: IndexLabel | ListLike = ...,
    columns: IndexLabel | ListLike = ...,
    level: Level | None = ...,
    inplace: Literal[False] = ...,
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 5036

def drop(
    self,
    labels: IndexLabel | ListLike = ...,
    *,
    axis: Axis = ...,
    index: IndexLabel | ListLike = ...,
    columns: IndexLabel | ListLike = ...,
    level: Level | None = ...,
    inplace: bool = ...,
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 5048

def drop(
    self,
    labels: IndexLabel | ListLike = None,
    *,
    axis: Axis = 0,
    index: IndexLabel | ListLike = None,
    columns: IndexLabel | ListLike = None,
    level: Level | None = None,
    inplace: bool = False,
    errors: IgnoreRaise = "raise",

# ==================================================
# Line: 6625

def _reduce(
    self,
    op,
    # error: Variable "pandas.core.series.Series.str" is not valid as a type
    name: str,  # type: ignore[valid-type]
    *,
    axis: Axis = 0,
    skipna: bool = True,
    numeric_only: bool = False,
    filter_type=None,
    **kwds,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/resample.py
# Line: 158

def __init__(
    self,
    obj: NDFrame,
    timegrouper: TimeGrouper,
    *,
    gpr_index: Index,
    group_keys: bool = False,
    selection=None,
    include_groups: bool = False,

# ==================================================
# Line: 765

def interpolate(
    self,
    method: InterpolateOptions = "linear",
    *,
    axis: Axis = 0,
    limit: int | None = None,
    inplace: bool = False,
    limit_direction: Literal["forward", "backward", "both"] = "forward",
    limit_area=None,
    downcast=lib.no_default,
    **kwargs,

# ==================================================
# Line: 2151

def __init__(
    self,
    obj: Grouper | None = None,
    freq: Frequency = "Min",
    key: str | None = None,
    closed: Literal["left", "right"] | None = None,
    label: Literal["left", "right"] | None = None,
    how: str = "mean",
    fill_method=None,
    limit: int | None = None,
    convention: Literal["start", "end", "e", "s"] | None = None,
    origin: Literal["epoch", "start", "start_day", "end", "end_day"]
    | TimestampConvertibleTypes = "start_day",
    offset: TimedeltaConvertibleTypes | None = None,
    group_keys: bool = False,
    **kwargs,

# ==================================================
# Line: 2594

def _get_timestamp_range_edges(
    first: Timestamp,
    last: Timestamp,
    freq: BaseOffset,
    unit: str,
    closed: Literal["right", "left"] = "left",
    origin: TimeGrouperOrigin = "start_day",
    offset: Timedelta | None = None,

# ==================================================
# Line: 2747

def _adjust_dates_anchored(
    first: Timestamp,
    last: Timestamp,
    freq: Tick,
    closed: Literal["right", "left"] = "right",
    origin: TimeGrouperOrigin = "start_day",
    offset: Timedelta | None = None,
    unit: str = "ns",

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/computation/expr.py
# Line: 497

def _maybe_evaluate_binop(
    self,
    op,
    op_class,
    lhs,
    rhs,
    eval_in_python=("in", "not in"),
    maybe_eval_in_python=("==", "!=", "<", ">", "<=", ">="),

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/computation/eval.py
# Line: 177

def eval(
    expr: str | BinOp,  # we leave BinOp out of the docstr bc it isn't for users
    parser: str = "pandas",
    engine: str | None = None,
    local_dict=None,
    global_dict=None,
    resolvers=(),
    level: int = 0,
    target=None,
    inplace: bool = False,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/pivot.py
# Line: 53

def pivot_table(
    data: DataFrame,
    values=None,
    index=None,
    columns=None,
    aggfunc: AggFuncType = "mean",
    fill_value=None,
    margins: bool = False,
    dropna: bool = True,
    margins_name: Hashable = "All",
    observed: bool = True,
    sort: bool = True,
    **kwargs,

# ==================================================
# Line: 284

def __internal_pivot_table(
    data: DataFrame,
    values,
    index,
    columns,
    aggfunc: AggFuncTypeBase | AggFuncTypeDict,
    fill_value,
    margins: bool,
    dropna: bool,
    margins_name: Hashable,
    observed: bool,
    sort: bool,
    kwargs,

# ==================================================
# Line: 414

def _add_margins(
    table: DataFrame | Series,
    data: DataFrame,
    values,
    rows,
    cols,
    aggfunc,
    kwargs,
    observed: bool,
    margins_name: Hashable = "All",
    fill_value=None,

# ==================================================
# Line: 531

def _generate_marginal_results(
    table,
    data: DataFrame,
    values,
    rows,
    cols,
    aggfunc,
    kwargs,
    observed: bool,
    margins_name: Hashable = "All",

# ==================================================
# Line: 627

def _generate_marginal_results_without_values(
    table: DataFrame,
    data: DataFrame,
    rows,
    cols,
    aggfunc,
    kwargs,
    observed: bool,
    margins_name: Hashable = "All",

# ==================================================
# Line: 909

def crosstab(
    index,
    columns,
    values=None,
    rownames=None,
    colnames=None,
    aggfunc=None,
    margins: bool = False,
    margins_name: Hashable = "All",
    dropna: bool = True,
    normalize: bool | Literal[0, 1, "all", "index", "columns"] = False,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/tile.py
# Line: 54

def cut(
    x,
    bins,
    right: bool = True,
    labels=None,
    retbins: bool = False,
    precision: int = 3,
    include_lowest: bool = False,
    duplicates: str = "raise",
    ordered: bool = True,

# ==================================================
# Line: 447

def _bins_to_cuts(
    x_idx: Index,
    bins: Index,
    right: bool = True,
    labels=None,
    precision: int = 3,
    include_lowest: bool = False,
    duplicates: str = "raise",
    ordered: bool = True,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/encoding.py
# Line: 41

def get_dummies(
    data,
    prefix=None,
    prefix_sep: str | Iterable[str] | dict[str, str] = "_",
    dummy_na: bool = False,
    columns=None,
    sparse: bool = False,
    drop_first: bool = False,
    dtype: NpDtype | None = None,

# ==================================================
# Line: 238

def _get_dummies_1d(
    data,
    prefix,
    prefix_sep: str | Iterable[str] | dict[str, str] = "_",
    dummy_na: bool = False,
    sparse: bool = False,
    drop_first: bool = False,
    dtype: NpDtype | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/merge.py
# Line: 145

def merge(
    left: DataFrame | Series,
    right: DataFrame | Series,
    how: MergeHow = "inner",
    on: IndexLabel | AnyArrayLike | None = None,
    left_on: IndexLabel | AnyArrayLike | None = None,
    right_on: IndexLabel | AnyArrayLike | None = None,
    left_index: bool = False,
    right_index: bool = False,
    sort: bool = False,
    suffixes: Suffixes = ("_x", "_y"),
    copy: bool | lib.NoDefault = lib.no_default,
    indicator: str | bool = False,
    validate: str | None = None,

# ==================================================
# Line: 404

def _cross_merge(
    left: DataFrame,
    right: DataFrame,
    on: IndexLabel | AnyArrayLike | None = None,
    left_on: IndexLabel | AnyArrayLike | None = None,
    right_on: IndexLabel | AnyArrayLike | None = None,
    left_index: bool = False,
    right_index: bool = False,
    sort: bool = False,
    suffixes: Suffixes = ("_x", "_y"),
    indicator: str | bool = False,
    validate: str | None = None,

# ==================================================
# Line: 515

def merge_ordered(
    left: DataFrame | Series,
    right: DataFrame | Series,
    on: IndexLabel | None = None,
    left_on: IndexLabel | None = None,
    right_on: IndexLabel | None = None,
    left_by=None,
    right_by=None,
    fill_method: str | None = None,
    suffixes: Suffixes = ("_x", "_y"),
    how: JoinHow = "outer",

# ==================================================
# Line: 659

def merge_asof(
    left: DataFrame | Series,
    right: DataFrame | Series,
    on: IndexLabel | None = None,
    left_on: IndexLabel | None = None,
    right_on: IndexLabel | None = None,
    left_index: bool = False,
    right_index: bool = False,
    by=None,
    left_by=None,
    right_by=None,
    suffixes: Suffixes = ("_x", "_y"),
    tolerance: int | datetime.timedelta | None = None,
    allow_exact_matches: bool = True,
    direction: str = "backward",

# ==================================================
# Line: 957

def __init__(
    self,
    left: DataFrame | Series,
    right: DataFrame | Series,
    how: JoinHow | Literal["left_anti", "right_anti", "asof"] = "inner",
    on: IndexLabel | AnyArrayLike | None = None,
    left_on: IndexLabel | AnyArrayLike | None = None,
    right_on: IndexLabel | AnyArrayLike | None = None,
    left_index: bool = False,
    right_index: bool = False,
    sort: bool = True,
    suffixes: Suffixes = ("_x", "_y"),
    indicator: str | bool = False,
    validate: str | None = None,

# ==================================================
# Line: 2193

def __init__(
    self,
    left: DataFrame | Series,
    right: DataFrame | Series,
    on: IndexLabel | None = None,
    left_on: IndexLabel | None = None,
    right_on: IndexLabel | None = None,
    left_index: bool = False,
    right_index: bool = False,
    suffixes: Suffixes = ("_x", "_y"),
    fill_method: str | None = None,
    how: JoinHow | Literal["asof"] = "outer",

# ==================================================
# Line: 2258

def __init__(
    self,
    left: DataFrame | Series,
    right: DataFrame | Series,
    on: IndexLabel | None = None,
    left_on: IndexLabel | None = None,
    right_on: IndexLabel | None = None,
    left_index: bool = False,
    right_index: bool = False,
    by=None,
    left_by=None,
    right_by=None,
    suffixes: Suffixes = ("_x", "_y"),
    how: Literal["asof"] = "asof",
    tolerance=None,
    allow_exact_matches: bool = True,
    direction: str = "backward",

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/concat.py
# Line: 74

def concat(
    objs: Iterable[DataFrame] | Mapping[HashableT, DataFrame],
    *,
    axis: Literal[0, "index"] = ...,
    join: str = ...,
    ignore_index: bool = ...,
    keys: Iterable[Hashable] | None = ...,
    levels=...,
    names: list[HashableT] | None = ...,
    verify_integrity: bool = ...,
    sort: bool = ...,
    copy: bool | lib.NoDefault = ...,

# ==================================================
# Line: 90

def concat(
    objs: Iterable[Series] | Mapping[HashableT, Series],
    *,
    axis: Literal[0, "index"] = ...,
    join: str = ...,
    ignore_index: bool = ...,
    keys: Iterable[Hashable] | None = ...,
    levels=...,
    names: list[HashableT] | None = ...,
    verify_integrity: bool = ...,
    sort: bool = ...,
    copy: bool | lib.NoDefault = ...,

# ==================================================
# Line: 106

def concat(
    objs: Iterable[Series | DataFrame] | Mapping[HashableT, Series | DataFrame],
    *,
    axis: Literal[0, "index"] = ...,
    join: str = ...,
    ignore_index: bool = ...,
    keys: Iterable[Hashable] | None = ...,
    levels=...,
    names: list[HashableT] | None = ...,
    verify_integrity: bool = ...,
    sort: bool = ...,
    copy: bool | lib.NoDefault = ...,

# ==================================================
# Line: 122

def concat(
    objs: Iterable[Series | DataFrame] | Mapping[HashableT, Series | DataFrame],
    *,
    axis: Literal[1, "columns"],
    join: str = ...,
    ignore_index: bool = ...,
    keys: Iterable[Hashable] | None = ...,
    levels=...,
    names: list[HashableT] | None = ...,
    verify_integrity: bool = ...,
    sort: bool = ...,
    copy: bool | lib.NoDefault = ...,

# ==================================================
# Line: 138

def concat(
    objs: Iterable[Series | DataFrame] | Mapping[HashableT, Series | DataFrame],
    *,
    axis: Axis = ...,
    join: str = ...,
    ignore_index: bool = ...,
    keys: Iterable[Hashable] | None = ...,
    levels=...,
    names: list[HashableT] | None = ...,
    verify_integrity: bool = ...,
    sort: bool = ...,
    copy: bool | lib.NoDefault = ...,

# ==================================================
# Line: 154

def concat(
    objs: Iterable[Series | DataFrame] | Mapping[HashableT, Series | DataFrame],
    *,
    axis: Axis = 0,
    join: str = "outer",
    ignore_index: bool = False,
    keys: Iterable[Hashable] | None = None,
    levels=None,
    names: list[HashableT] | None = None,
    verify_integrity: bool = False,
    sort: bool = False,
    copy: bool | lib.NoDefault = lib.no_default,

# ==================================================
# Line: 506

def _get_result(
    objs: list[Series | DataFrame],
    is_series: bool,
    bm_axis: AxisInt,
    ignore_index: bool,
    intersect: bool,
    sort: bool,
    keys: Iterable[Hashable] | None,
    levels,
    verify_integrity: bool,
    names: list[HashableT] | None,
    axis: AxisInt,

# ==================================================
# Line: 616

def new_axes(
    objs: list[Series | DataFrame],
    bm_axis: AxisInt,
    intersect: bool,
    sort: bool,
    keys: Iterable[Hashable] | None,
    names: list[HashableT] | None,
    axis: AxisInt,
    levels,
    verify_integrity: bool,
    ignore_index: bool,

# ==================================================
# Line: 650

def _get_concat_axis_series(
    objs: list[Series | DataFrame],
    ignore_index: bool,
    bm_axis: AxisInt,
    keys: Iterable[Hashable] | None,
    levels,
    verify_integrity: bool,
    names: list[HashableT] | None,

# ==================================================
# Line: 698

def _get_concat_axis_dataframe(
    objs: list[Series | DataFrame],
    axis: AxisInt,
    ignore_index: bool,
    keys: Iterable[Hashable] | None,
    names: list[HashableT] | None,
    levels,
    verify_integrity: bool,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/melt.py
# Line: 42

def melt(
    frame: DataFrame,
    id_vars=None,
    value_vars=None,
    var_name=None,
    value_name: Hashable = "value",
    col_level=None,
    ignore_index: bool = True,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/accessor.py
# Line: 74

def _add_delegate_accessors(
    cls,
    delegate,
    accessors: list[str],
    typ: str,
    overwrite: bool = False,
    accessor_mapping: Callable[[str], str] = lambda x: x,
    raise_on_missing: bool = True,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/sparse/array.py
# Line: 375

def __init__(
    self,
    data,
    sparse_index=None,
    fill_value=None,
    kind: SparseIndexKind = "integer",
    dtype: Dtype | None = None,
    copy: bool = False,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/datetimelike.py
# Line: 2346

def interpolate(
    self,
    *,
    method: InterpolateOptions,
    axis: int,
    index: Index,
    limit,
    limit_direction,
    limit_area,
    copy: bool,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/numpy_.py
# Line: 282

def interpolate(
    self,
    *,
    method: InterpolateOptions,
    axis: int,
    index: Index,
    limit,
    limit_direction,
    limit_area,
    copy: bool,
    **kwargs,

# ==================================================
# Line: 422

def std(
    self,
    *,
    axis: AxisInt | None = None,
    dtype: NpDtype | None = None,
    out=None,
    ddof: int = 1,
    keepdims: bool = False,
    skipna: bool = True,

# ==================================================
# Line: 438

def var(
    self,
    *,
    axis: AxisInt | None = None,
    dtype: NpDtype | None = None,
    out=None,
    ddof: int = 1,
    keepdims: bool = False,
    skipna: bool = True,

# ==================================================
# Line: 454

def sem(
    self,
    *,
    axis: AxisInt | None = None,
    dtype: NpDtype | None = None,
    out=None,
    ddof: int = 1,
    keepdims: bool = False,
    skipna: bool = True,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/masked.py
# Line: 1507

def interpolate(
    self,
    *,
    method: InterpolateOptions,
    axis: int,
    index,
    limit,
    limit_direction,
    limit_area,
    copy: bool,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/arrow/array.py
# Line: 2213

def interpolate(
    self,
    *,
    method: InterpolateOptions,
    axis: int,
    index,
    limit,
    limit_direction,
    limit_area,
    copy: bool,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/base.py
# Line: 989

def interpolate(
    self,
    *,
    method: InterpolateOptions,
    axis: int,
    index: Index,
    limit,
    limit_direction,
    limit_area,
    copy: bool,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/timedeltas.py
# Line: 275

def _generate_range(
    cls, start, end, periods, freq, closed=None, *, unit: str | None = None

# ==================================================
# Line: 388

def sum(
    self,
    *,
    axis: AxisInt | None = None,
    dtype: NpDtype | None = None,
    out=None,
    keepdims: bool = False,
    initial=None,
    skipna: bool = True,
    min_count: int = 0,

# ==================================================
# Line: 408

def std(
    self,
    *,
    axis: AxisInt | None = None,
    dtype: NpDtype | None = None,
    out=None,
    ddof: int = 1,
    keepdims: bool = False,
    skipna: bool = True,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/string_arrow.py
# Line: 355

def _str_replace(
    self,
    pat: str | re.Pattern,
    repl: str | Callable,
    n: int = -1,
    case: bool = True,
    flags: int = 0,
    regex: bool = True,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/datetimes.py
# Line: 345

def _from_sequence_not_strict(
    cls,
    data,
    *,
    dtype=None,
    copy: bool = False,
    tz=lib.no_default,
    freq: str | BaseOffset | lib.NoDefault | None = lib.no_default,
    dayfirst: bool = False,
    yearfirst: bool = False,
    ambiguous: TimeAmbiguous = "raise",

# ==================================================
# Line: 413

def _generate_range(
    cls,
    start,
    end,
    periods: int | None,
    freq,
    tz=None,
    normalize: bool = False,
    ambiguous: TimeAmbiguous = "raise",
    nonexistent: TimeNonexistent = "raise",
    inclusive: IntervalClosedType = "both",
    *,
    unit: str | None = None,

# ==================================================
# Line: 2300

def std(
    self,
    axis=None,
    dtype=None,
    out=None,
    ddof: int = 1,
    keepdims: bool = False,
    skipna: bool = True,

# ==================================================
# Line: 2382

def _sequence_to_dt64(
    data: ArrayLike,
    *,
    copy: bool = False,
    tz: tzinfo | None = None,
    dayfirst: bool = False,
    yearfirst: bool = False,
    ambiguous: TimeAmbiguous = "raise",
    out_unit: str | None = None,

# ==================================================
# Line: 2552

def objects_to_datetime64(
    data: np.ndarray,
    dayfirst,
    yearfirst,
    utc: bool = False,
    errors: DateTimeErrorChoices = "raise",
    allow_object: bool = False,
    out_unit: str | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/boolean.py
# Line: 331

def _from_sequence_of_strings(
    cls,
    strings: list[str],
    *,
    dtype: ExtensionDtype,
    copy: bool = False,
    true_values: list[str] | None = None,
    false_values: list[str] | None = None,
    none_values: list[str] | None = None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/period.py
# Line: 1398

def _range_from_fields(
    year=None,
    month=None,
    quarter=None,
    day=None,
    hour=None,
    minute=None,
    second=None,
    freq=None,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/frame.py
# Line: 1235

def to_string(
    self,
    buf: None = ...,
    *,
    columns: Axes | None = ...,
    col_space: int | list[int] | dict[Hashable, int] | None = ...,
    header: bool | SequenceNotStr[str] = ...,
    index: bool = ...,
    na_rep: str = ...,
    formatters: fmt.FormattersType | None = ...,
    float_format: fmt.FloatFormatType | None = ...,
    sparsify: bool | None = ...,
    index_names: bool = ...,
    justify: str | None = ...,
    max_rows: int | None = ...,
    max_cols: int | None = ...,
    show_dimensions: bool = ...,
    decimal: str = ...,
    line_width: int | None = ...,
    min_rows: int | None = ...,
    max_colwidth: int | None = ...,
    encoding: str | None = ...,

# ==================================================
# Line: 1260

def to_string(
    self,
    buf: FilePath | WriteBuffer[str],
    *,
    columns: Axes | None = ...,
    col_space: int | list[int] | dict[Hashable, int] | None = ...,
    header: bool | SequenceNotStr[str] = ...,
    index: bool = ...,
    na_rep: str = ...,
    formatters: fmt.FormattersType | None = ...,
    float_format: fmt.FloatFormatType | None = ...,
    sparsify: bool | None = ...,
    index_names: bool = ...,
    justify: str | None = ...,
    max_rows: int | None = ...,
    max_cols: int | None = ...,
    show_dimensions: bool = ...,
    decimal: str = ...,
    line_width: int | None = ...,
    min_rows: int | None = ...,
    max_colwidth: int | None = ...,
    encoding: str | None = ...,

# ==================================================
# Line: 1295

def to_string(
    self,
    buf: FilePath | WriteBuffer[str] | None = None,
    *,
    columns: Axes | None = None,
    col_space: int | list[int] | dict[Hashable, int] | None = None,
    header: bool | SequenceNotStr[str] = True,
    index: bool = True,
    na_rep: str = "NaN",
    formatters: fmt.FormattersType | None = None,
    float_format: fmt.FloatFormatType | None = None,
    sparsify: bool | None = None,
    index_names: bool = True,
    justify: str | None = None,
    max_rows: int | None = None,
    max_cols: int | None = None,
    show_dimensions: bool = False,
    decimal: str = ".",
    line_width: int | None = None,
    min_rows: int | None = None,
    max_colwidth: int | None = None,
    encoding: str | None = None,

# ==================================================
# Line: 2119

def from_records(
    cls,
    data,
    index=None,
    exclude=None,
    columns=None,
    coerce_float: bool = False,
    nrows: int | None = None,

# ==================================================
# Line: 2549

def to_stata(
    self,
    path: FilePath | WriteBuffer[bytes],
    *,
    convert_dates: dict[Hashable, str] | None = None,
    write_index: bool = True,
    byteorder: ToStataByteorder | None = None,
    time_stamp: datetime.datetime | None = None,
    data_label: str | None = None,
    variable_labels: dict[Hashable, str] | None = None,
    version: int | None = 114,
    convert_strl: Sequence[Hashable] | None = None,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,
    value_labels: dict[Hashable, dict[float, str]] | None = None,

# ==================================================
# Line: 2858

def to_parquet(
    self,
    path: None = ...,
    *,
    engine: Literal["auto", "pyarrow", "fastparquet"] = ...,
    compression: str | None = ...,
    index: bool | None = ...,
    partition_cols: list[str] | None = ...,
    storage_options: StorageOptions = ...,
    **kwargs,

# ==================================================
# Line: 2871

def to_parquet(
    self,
    path: FilePath | WriteBuffer[bytes],
    *,
    engine: Literal["auto", "pyarrow", "fastparquet"] = ...,
    compression: str | None = ...,
    index: bool | None = ...,
    partition_cols: list[str] | None = ...,
    storage_options: StorageOptions = ...,
    **kwargs,

# ==================================================
# Line: 2884

def to_parquet(
    self,
    path: FilePath | WriteBuffer[bytes] | None = None,
    *,
    engine: Literal["auto", "pyarrow", "fastparquet"] = "auto",
    compression: str | None = "snappy",
    index: bool | None = None,
    partition_cols: list[str] | None = None,
    storage_options: StorageOptions | None = None,
    **kwargs,

# ==================================================
# Line: 3118

def to_html(
    self,
    buf: FilePath | WriteBuffer[str],
    *,
    columns: Axes | None = ...,
    col_space: ColspaceArgType | None = ...,
    header: bool = ...,
    index: bool = ...,
    na_rep: str = ...,
    formatters: FormattersType | None = ...,
    float_format: FloatFormatType | None = ...,
    sparsify: bool | None = ...,
    index_names: bool = ...,
    justify: str | None = ...,
    max_rows: int | None = ...,
    max_cols: int | None = ...,
    show_dimensions: bool | str = ...,
    decimal: str = ...,
    bold_rows: bool = ...,
    classes: str | list | tuple | None = ...,
    escape: bool = ...,
    notebook: bool = ...,
    border: int | bool | None = ...,
    table_id: str | None = ...,
    render_links: bool = ...,
    encoding: str | None = ...,

# ==================================================
# Line: 3147

def to_html(
    self,
    buf: None = ...,
    *,
    columns: Axes | None = ...,
    col_space: ColspaceArgType | None = ...,
    header: bool = ...,
    index: bool = ...,
    na_rep: str = ...,
    formatters: FormattersType | None = ...,
    float_format: FloatFormatType | None = ...,
    sparsify: bool | None = ...,
    index_names: bool = ...,
    justify: str | None = ...,
    max_rows: int | None = ...,
    max_cols: int | None = ...,
    show_dimensions: bool | str = ...,
    decimal: str = ...,
    bold_rows: bool = ...,
    classes: str | list | tuple | None = ...,
    escape: bool = ...,
    notebook: bool = ...,
    border: int | bool | None = ...,
    table_id: str | None = ...,
    render_links: bool = ...,
    encoding: str | None = ...,

# ==================================================
# Line: 3183

def to_html(
    self,
    buf: FilePath | WriteBuffer[str] | None = None,
    *,
    columns: Axes | None = None,
    col_space: ColspaceArgType | None = None,
    header: bool = True,
    index: bool = True,
    na_rep: str = "NaN",
    formatters: FormattersType | None = None,
    float_format: FloatFormatType | None = None,
    sparsify: bool | None = None,
    index_names: bool = True,
    justify: str | None = None,
    max_rows: int | None = None,
    max_cols: int | None = None,
    show_dimensions: bool | str = False,
    decimal: str = ".",
    bold_rows: bool = True,
    classes: str | list | tuple | None = None,
    escape: bool = True,
    notebook: bool = False,
    border: int | bool | None = None,
    table_id: str | None = None,
    render_links: bool = False,
    encoding: str | None = None,

# ==================================================
# Line: 3299

def to_xml(
    self,
    path_or_buffer: None = ...,
    *,
    index: bool = ...,
    root_name: str | None = ...,
    row_name: str | None = ...,
    na_rep: str | None = ...,
    attr_cols: list[str] | None = ...,
    elem_cols: list[str] | None = ...,
    namespaces: dict[str | None, str] | None = ...,
    prefix: str | None = ...,
    encoding: str = ...,
    xml_declaration: bool | None = ...,
    pretty_print: bool | None = ...,
    parser: XMLParsers | None = ...,
    stylesheet: FilePath | ReadBuffer[str] | ReadBuffer[bytes] | None = ...,
    compression: CompressionOptions = ...,
    storage_options: StorageOptions | None = ...,

# ==================================================
# Line: 3321

def to_xml(
    self,
    path_or_buffer: FilePath | WriteBuffer[bytes] | WriteBuffer[str],
    *,
    index: bool = ...,
    root_name: str | None = ...,
    row_name: str | None = ...,
    na_rep: str | None = ...,
    attr_cols: list[str] | None = ...,
    elem_cols: list[str] | None = ...,
    namespaces: dict[str | None, str] | None = ...,
    prefix: str | None = ...,
    encoding: str = ...,
    xml_declaration: bool | None = ...,
    pretty_print: bool | None = ...,
    parser: XMLParsers | None = ...,
    stylesheet: FilePath | ReadBuffer[str] | ReadBuffer[bytes] | None = ...,
    compression: CompressionOptions = ...,
    storage_options: StorageOptions | None = ...,

# ==================================================
# Line: 3346

def to_xml(
    self,
    path_or_buffer: FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None = None,
    *,
    index: bool = True,
    root_name: str | None = "data",
    row_name: str | None = "row",
    na_rep: str | None = None,
    attr_cols: list[str] | None = None,
    elem_cols: list[str] | None = None,
    namespaces: dict[str | None, str] | None = None,
    prefix: str | None = None,
    encoding: str = "utf-8",
    xml_declaration: bool | None = True,
    pretty_print: bool | None = True,
    parser: XMLParsers | None = "lxml",
    stylesheet: FilePath | ReadBuffer[str] | ReadBuffer[bytes] | None = None,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,

# ==================================================
# Line: 3550

def to_iceberg(
    self,
    table_identifier: str,
    catalog_name: str | None = None,
    *,
    catalog_properties: dict[str, Any] | None = None,
    location: str | None = None,
    append: bool = False,
    snapshot_properties: dict[str, str] | None = None,

# ==================================================
# Line: 4539

def query(
    self,
    expr: str,
    *,
    parser: Literal["pandas", "python"] = ...,
    engine: Literal["python", "numexpr"] | None = ...,
    local_dict: dict[str, Any] | None = ...,
    global_dict: dict[str, Any] | None = ...,
    resolvers: list[Mapping] | None = ...,
    level: int = ...,
    inplace: Literal[False] = ...,

# ==================================================
# Line: 4553

def query(
    self,
    expr: str,
    *,
    parser: Literal["pandas", "python"] = ...,
    engine: Literal["python", "numexpr"] | None = ...,
    local_dict: dict[str, Any] | None = ...,
    global_dict: dict[str, Any] | None = ...,
    resolvers: list[Mapping] | None = ...,
    level: int = ...,
    inplace: Literal[True],

# ==================================================
# Line: 4567

def query(
    self,
    expr: str,
    *,
    parser: Literal["pandas", "python"] = ...,
    engine: Literal["python", "numexpr"] | None = ...,
    local_dict: dict[str, Any] | None = ...,
    global_dict: dict[str, Any] | None = ...,
    resolvers: list[Mapping] | None = ...,
    level: int = ...,
    inplace: bool = ...,

# ==================================================
# Line: 4580

def query(
    self,
    expr: str,
    *,
    parser: Literal["pandas", "python"] = "pandas",
    engine: Literal["python", "numexpr"] | None = None,
    local_dict: dict[str, Any] | None = None,
    global_dict: dict[str, Any] | None = None,
    resolvers: list[Mapping] | None = None,
    level: int = 0,
    inplace: bool = False,

# ==================================================
# Line: 5345

def reindex(
    self,
    labels=None,
    *,
    index=None,
    columns=None,
    axis: Axis | None = None,
    method: ReindexMethod | None = None,
    copy: bool | lib.NoDefault = lib.no_default,
    level: Level | None = None,
    fill_value: Scalar | None = np.nan,
    limit: int | None = None,
    tolerance=None,

# ==================================================
# Line: 5373

def drop(
    self,
    labels: IndexLabel | ListLike = ...,
    *,
    axis: Axis = ...,
    index: IndexLabel | ListLike = ...,
    columns: IndexLabel | ListLike = ...,
    level: Level = ...,
    inplace: Literal[True],
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 5386

def drop(
    self,
    labels: IndexLabel | ListLike = ...,
    *,
    axis: Axis = ...,
    index: IndexLabel | ListLike = ...,
    columns: IndexLabel | ListLike = ...,
    level: Level = ...,
    inplace: Literal[False] = ...,
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 5399

def drop(
    self,
    labels: IndexLabel | ListLike = ...,
    *,
    axis: Axis = ...,
    index: IndexLabel | ListLike = ...,
    columns: IndexLabel | ListLike = ...,
    level: Level = ...,
    inplace: bool = ...,
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 5411

def drop(
    self,
    labels: IndexLabel | ListLike = None,
    *,
    axis: Axis = 0,
    index: IndexLabel | ListLike = None,
    columns: IndexLabel | ListLike = None,
    level: Level | None = None,
    inplace: bool = False,
    errors: IgnoreRaise = "raise",

# ==================================================
# Line: 5580

def rename(
    self,
    mapper: Renamer | None = ...,
    *,
    index: Renamer | None = ...,
    columns: Renamer | None = ...,
    axis: Axis | None = ...,
    copy: bool | lib.NoDefault = lib.no_default,
    inplace: Literal[True],
    level: Level = ...,
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 5594

def rename(
    self,
    mapper: Renamer | None = ...,
    *,
    index: Renamer | None = ...,
    columns: Renamer | None = ...,
    axis: Axis | None = ...,
    copy: bool | lib.NoDefault = lib.no_default,
    inplace: Literal[False] = ...,
    level: Level = ...,
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 5608

def rename(
    self,
    mapper: Renamer | None = ...,
    *,
    index: Renamer | None = ...,
    columns: Renamer | None = ...,
    axis: Axis | None = ...,
    copy: bool | lib.NoDefault = lib.no_default,
    inplace: bool = ...,
    level: Level = ...,
    errors: IgnoreRaise = ...,

# ==================================================
# Line: 5621

def rename(
    self,
    mapper: Renamer | None = None,
    *,
    index: Renamer | None = None,
    columns: Renamer | None = None,
    axis: Axis | None = None,
    copy: bool | lib.NoDefault = lib.no_default,
    inplace: bool = False,
    level: Level | None = None,
    errors: IgnoreRaise = "ignore",

# ==================================================
# Line: 6221

def reset_index(
    self,
    level: IndexLabel = ...,
    *,
    drop: bool = ...,
    inplace: Literal[False] = ...,
    col_level: Hashable = ...,
    col_fill: Hashable = ...,
    allow_duplicates: bool | lib.NoDefault = ...,
    names: Hashable | Sequence[Hashable] | None = None,

# ==================================================
# Line: 6234

def reset_index(
    self,
    level: IndexLabel = ...,
    *,
    drop: bool = ...,
    inplace: Literal[True],
    col_level: Hashable = ...,
    col_fill: Hashable = ...,
    allow_duplicates: bool | lib.NoDefault = ...,
    names: Hashable | Sequence[Hashable] | None = None,

# ==================================================
# Line: 6247

def reset_index(
    self,
    level: IndexLabel = ...,
    *,
    drop: bool = ...,
    inplace: bool = ...,
    col_level: Hashable = ...,
    col_fill: Hashable = ...,
    allow_duplicates: bool | lib.NoDefault = ...,
    names: Hashable | Sequence[Hashable] | None = None,

# ==================================================
# Line: 6259

def reset_index(
    self,
    level: IndexLabel | None = None,
    *,
    drop: bool = False,
    inplace: bool = False,
    col_level: Hashable = 0,
    col_fill: Hashable = "",
    allow_duplicates: bool | lib.NoDefault = lib.no_default,
    names: Hashable | Sequence[Hashable] | None = None,

# ==================================================
# Line: 6535

def dropna(
    self,
    *,
    axis: Axis = ...,
    how: AnyAll | lib.NoDefault = ...,
    thresh: int | lib.NoDefault = ...,
    subset: IndexLabel = ...,
    inplace: Literal[False] = ...,
    ignore_index: bool = ...,

# ==================================================
# Line: 6547

def dropna(
    self,
    *,
    axis: Axis = ...,
    how: AnyAll | lib.NoDefault = ...,
    thresh: int | lib.NoDefault = ...,
    subset: IndexLabel = ...,
    inplace: Literal[True],
    ignore_index: bool = ...,

# ==================================================
# Line: 6558

def dropna(
    self,
    *,
    axis: Axis = 0,
    how: AnyAll | lib.NoDefault = lib.no_default,
    thresh: int | lib.NoDefault = lib.no_default,
    subset: IndexLabel | AnyArrayLike | None = None,
    inplace: bool = False,
    ignore_index: bool = False,

# ==================================================
# Line: 6993

def sort_values(
    self,
    by: IndexLabel,
    *,
    axis: Axis = ...,
    ascending=...,
    inplace: Literal[False] = ...,
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    ignore_index: bool = ...,
    key: ValueKeyFunc = ...,

# ==================================================
# Line: 7007

def sort_values(
    self,
    by: IndexLabel,
    *,
    axis: Axis = ...,
    ascending=...,
    inplace: Literal[True],
    kind: SortKind = ...,
    na_position: str = ...,
    ignore_index: bool = ...,
    key: ValueKeyFunc = ...,

# ==================================================
# Line: 7020

def sort_values(
    self,
    by: IndexLabel,
    *,
    axis: Axis = 0,
    ascending: bool | list[bool] | tuple[bool, ...] = True,
    inplace: bool = False,
    kind: SortKind = "quicksort",
    na_position: str = "last",
    ignore_index: bool = False,
    key: ValueKeyFunc | None = None,

# ==================================================
# Line: 7287

def sort_index(
    self,
    *,
    axis: Axis = ...,
    level: IndexLabel = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: Literal[True],
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    sort_remaining: bool = ...,
    ignore_index: bool = ...,
    key: IndexKeyFunc = ...,

# ==================================================
# Line: 7302

def sort_index(
    self,
    *,
    axis: Axis = ...,
    level: IndexLabel = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: Literal[False] = ...,
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    sort_remaining: bool = ...,
    ignore_index: bool = ...,
    key: IndexKeyFunc = ...,

# ==================================================
# Line: 7317

def sort_index(
    self,
    *,
    axis: Axis = ...,
    level: IndexLabel = ...,
    ascending: bool | Sequence[bool] = ...,
    inplace: bool = ...,
    kind: SortKind = ...,
    na_position: NaPosition = ...,
    sort_remaining: bool = ...,
    ignore_index: bool = ...,
    key: IndexKeyFunc = ...,

# ==================================================
# Line: 7331

def sort_index(
    self,
    *,
    axis: Axis = 0,
    level: IndexLabel | None = None,
    ascending: bool | Sequence[bool] = True,
    inplace: bool = False,
    kind: SortKind = "quicksort",
    na_position: NaPosition = "last",
    sort_remaining: bool = True,
    ignore_index: bool = False,
    key: IndexKeyFunc | None = None,

# ==================================================
# Line: 9280

def groupby(
    self,
    by=None,
    level: IndexLabel | None = None,
    as_index: bool = True,
    sort: bool = True,
    group_keys: bool = True,
    observed: bool = True,
    dropna: bool = True,

# ==================================================
# Line: 9609

def pivot_table(
    self,
    values=None,
    index=None,
    columns=None,
    aggfunc: AggFuncType = "mean",
    fill_value=None,
    margins: bool = False,
    dropna: bool = True,
    margins_name: Level = "All",
    observed: bool = True,
    sort: bool = True,
    **kwargs,

# ==================================================
# Line: 10052

def melt(
    self,
    id_vars=None,
    value_vars=None,
    var_name=None,
    value_name: Hashable = "value",
    col_level: Level | None = None,
    ignore_index: bool = True,

# ==================================================
# Line: 10410

def apply(
    self,
    func: AggFuncType,
    axis: Axis = 0,
    raw: bool = False,
    result_type: Literal["expand", "reduce", "broadcast"] | None = None,
    args=(),
    by_row: Literal[False, "compat"] = "compat",
    engine: Callable | None | Literal["python", "numba"] = None,
    engine_kwargs: dict[str, bool] | None = None,
    **kwargs,

# ==================================================
# Line: 10847

def join(
    self,
    other: DataFrame | Series | Iterable[DataFrame | Series],
    on: IndexLabel | None = None,
    how: MergeHow = "left",
    lsuffix: str = "",
    rsuffix: str = "",
    sort: bool = False,
    validate: JoinValidate | None = None,

# ==================================================
# Line: 11094

def merge(
    self,
    right: DataFrame | Series,
    how: MergeHow = "inner",
    on: IndexLabel | AnyArrayLike | None = None,
    left_on: IndexLabel | AnyArrayLike | None = None,
    right_on: IndexLabel | AnyArrayLike | None = None,
    left_index: bool = False,
    right_index: bool = False,
    sort: bool = False,
    suffixes: Suffixes = ("_x", "_y"),
    copy: bool | lib.NoDefault = lib.no_default,
    indicator: str | bool = False,
    validate: MergeValidate | None = None,

# ==================================================
# Line: 11516

def corrwith(
    self,
    other: DataFrame | Series,
    axis: Axis = 0,
    drop: bool = False,
    method: CorrelationMethod = "pearson",
    numeric_only: bool = False,
    min_periods: int | None = None,

# ==================================================
# Line: 11746

def _reduce(
    self,
    op,
    name: str,
    *,
    axis: Axis = 0,
    skipna: bool = True,
    numeric_only: bool = False,
    filter_type=None,
    **kwds,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/internals/blocks.py
# Line: 524

def convert_dtypes(
    self,
    infer_objects: bool = True,
    convert_string: bool = True,
    convert_integer: bool = True,
    convert_boolean: bool = True,
    convert_floating: bool = True,
    dtype_backend: DtypeBackend = "numpy_nullable",

# ==================================================
# Line: 1372

def interpolate(
    self,
    *,
    method: InterpolateOptions,
    index: Index,
    inplace: bool = False,
    limit: int | None = None,
    limit_direction: Literal["forward", "backward", "both"] = "forward",
    limit_area: Literal["inside", "outside"] | None = None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/internals/managers.py
# Line: 775

def reindex_indexer(
    self,
    new_axis: Index,
    indexer: npt.NDArray[np.intp] | None,
    axis: AxisInt,
    fill_value=None,
    allow_dups: bool = False,
    only_slice: bool = False,
    *,
    use_na_proxy: bool = False,

# ==================================================
# Line: 1404

def _iset_single(
    self,
    loc: int,
    value: ArrayLike,
    inplace: bool,
    blkno: int,
    blk: Block,
    refs: BlockValuesRefs | None = None,

# ==================================================
