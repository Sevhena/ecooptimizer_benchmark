# too-many-arguments snippets for geopandas

# File: /root/ecooptimizer/geopandas/geopandas/base.py
# Line: 5412

def buffer(
    self,
    distance,
    resolution=16,
    cap_style="round",
    join_style="round",
    mitre_limit=5.0,
    single_sided=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/plotting.py
# Line: 117

def _plot_polygon_collection(
    ax,
    geoms,
    values=None,
    color=None,
    cmap=None,
    vmin=None,
    vmax=None,
    autolim=True,
    **kwargs,

# ==================================================
# Line: 188

def _plot_linestring_collection(
    ax,
    geoms,
    values=None,
    color=None,
    cmap=None,
    vmin=None,
    vmax=None,
    autolim=True,
    **kwargs,

# ==================================================
# Line: 253

def _plot_point_collection(
    ax,
    geoms,
    values=None,
    color=None,
    cmap=None,
    vmin=None,
    vmax=None,
    marker="o",
    markersize=None,
    **kwargs,

# ==================================================
# Line: 316

def plot_series(
    s,
    cmap=None,
    color=None,
    ax=None,
    figsize=None,
    aspect="auto",
    autolim=True,
    **style_kwds,

# ==================================================
# Line: 489

def plot_dataframe(
    df,
    column=None,
    cmap=None,
    color=None,
    ax=None,
    cax=None,
    categorical=False,
    legend=False,
    scheme=None,
    k=5,
    vmin=None,
    vmax=None,
    markersize=None,
    figsize=None,
    legend_kwds=None,
    categories=None,
    classification_kwds=None,
    missing_kwds=None,
    aspect="auto",
    autolim=True,
    **style_kwds,

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/explore.py
# Line: 34

def _explore(
    df,
    column=None,
    cmap=None,
    color=None,
    m=None,
    tiles="OpenStreetMap",
    attr=None,
    tooltip=True,
    popup=False,
    highlight=True,
    categorical=False,
    legend=True,
    scheme=None,
    k=5,
    vmin=None,
    vmax=None,
    width="100%",
    height="100%",
    categories=None,
    classification_kwds=None,
    control_scale=True,
    marker_type=None,
    marker_kwds={},
    style_kwds={},
    highlight_kwds={},
    missing_kwds={},
    tooltip_kwds={},
    popup_kwds={},
    legend_kwds={},
    map_kwds={},
    **kwargs,

# ==================================================
# Line: 903

def _explore_geoseries(
    s,
    color=None,
    m=None,
    tiles="OpenStreetMap",
    attr=None,
    highlight=True,
    width="100%",
    height="100%",
    control_scale=True,
    marker_type=None,
    marker_kwds={},
    style_kwds={},
    highlight_kwds={},
    map_kwds={},
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/testing.py
# Line: 123

def assert_geoseries_equal(
    left,
    right,
    check_dtype=True,
    check_index_type=False,
    check_series_type=True,
    check_less_precise=False,
    check_geom_type=False,
    check_crs=True,
    normalize=False,

# ==================================================
# Line: 241

def assert_geodataframe_equal(
    left,
    right,
    check_dtype=True,
    check_index_type="equiv",
    check_column_type="equiv",
    check_frame_type=True,
    check_like=False,
    check_less_precise=False,
    check_geom_type=False,
    check_crs=True,
    normalize=False,

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/geodataframe.py
# Line: 828

def from_postgis(
    cls,
    sql: str | sqlalchemy.text,
    con,
    geom_col: str = "geom",
    crs: Any | None = None,
    index_col: str | list[str] | None = None,
    coerce_float: bool = True,
    parse_dates: list | dict | None = None,
    params: list | tuple | dict | None = None,
    chunksize: int | None = None,

# ==================================================
# Line: 1406

def to_parquet(
    self,
    path: os.PathLike | typing.IO,
    index: bool | None = None,
    compression: str = "snappy",
    geometry_encoding: PARQUET_GEOMETRY_ENCODINGS = "WKB",
    write_covering_bbox: bool = False,
    schema_version: SUPPORTED_VERSIONS_LITERAL | None = None,
    **kwargs,

# ==================================================
# Line: 2143

def dissolve(
    self,
    by: str | None = None,
    aggfunc="first",
    as_index: bool = True,
    level=None,
    sort: bool = True,
    observed: bool = False,
    dropna: bool = True,
    method: Literal["unary", "coverage", "disjoint_subset"] = "unary",
    grid_size: float | None = None,
    **kwargs,

# ==================================================
# Line: 2412

def to_postgis(
    self,
    name: str,
    con,
    schema: str | None = None,
    if_exists: Literal["fail", "replace", "append"] = "fail",
    index: bool = False,
    index_label: Iterable[str] | str | None = None,
    chunksize: int | None = None,
    dtype=None,

# ==================================================
# Line: 2588

def sjoin_nearest(
    self,
    right: GeoDataFrame,
    how: Literal["left", "right", "inner"] = "inner",
    max_distance: float | None = None,
    lsuffix: str = "left",
    rsuffix: str = "right",
    distance_col: str | None = None,
    exclusive: bool = False,

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/io/sql.py
# Line: 124

def _read_postgis(
    sql,
    con,
    geom_col="geom",
    crs=None,
    index_col=None,
    coerce_float=True,
    parse_dates=None,
    params=None,
    chunksize=None,

# ==================================================
# Line: 344

def _write_postgis(
    gdf,
    name,
    con,
    schema=None,
    if_exists="fail",
    index=False,
    index_label=None,
    chunksize=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/io/arrow.py
# Line: 388

def _to_parquet(
    df,
    path,
    index=None,
    compression="snappy",
    geometry_encoding="WKB",
    schema_version=None,
    write_covering_bbox=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/io/file.py
# Line: 343

def _read_file_fiona(
    path_or_bytes,
    from_bytes,
    bbox=None,
    mask=None,
    columns=None,
    rows=None,
    where=None,
    **kwargs,

# ==================================================
# Line: 617

def _to_file(
    df,
    filename,
    driver=None,
    schema=None,
    index=None,
    mode="w",
    crs=None,
    engine=None,
    metadata=None,
    **kwargs,

# ==================================================
# Line: 742

def _to_file_fiona(df, filename, driver, schema, crs, mode, metadata, **kwargs):
    if not HAS_PYPROJ and crs:
        raise ImportError(
            "The 'pyproj' package is required to write a file with a CRS, but it is not"
            " installed or does not import correctly."
        )

    if schema is None:
        schema = infer_schema(df)

    if crs:
        from pyproj import CRS

        crs = CRS.from_user_input(crs)
    else:
        crs = df.crs

    with fiona_env():
        crs_wkt = None
        try:
            gdal_version = Version(
                fiona.env.get_gdal_release_name().strip("e")
            )  # GH3147
        except (AttributeError, ValueError):
            gdal_version = Version("2.0.0")  # just assume it is not the latest
        if gdal_version >= Version("3.0.0") and crs:
            crs_wkt = crs.to_wkt()
        elif crs:
            crs_wkt = crs.to_wkt("WKT1_GDAL")
        with fiona.open(
            filename, mode=mode, driver=driver, crs_wkt=crs_wkt, schema=schema, **kwargs
        ) as colxn:
            if metadata is not None:
                colxn.update_tags(metadata)
            colxn.writerecords(df.iterfeatures())



# ==================================================
# Line: 779

def _to_file_pyogrio(df, filename, driver, schema, crs, mode, metadata, **kwargs):
    import pyogrio

    if schema is not None:
        raise ValueError(
            "The 'schema' argument is not supported with the 'pyogrio' engine."
        )

    if mode == "a":
        kwargs["append"] = True

    if crs is not None:
        raise ValueError("Passing 'crs' is not supported with the 'pyogrio' engine.")

    # for the fiona engine, this check is done in gdf.iterfeatures()
    if not df.columns.is_unique:
        raise ValueError("GeoDataFrame cannot contain duplicated column names.")

    pyogrio.write_dataframe(df, filename, driver=driver, metadata=metadata, **kwargs)



# ==================================================
