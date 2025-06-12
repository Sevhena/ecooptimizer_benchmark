# cached-repeated-calls snippets for geopandas

# File: /root/ecooptimizer/geopandas/versioneer.py
# Occurrences: Lines 351-353 (3 instances)

setup_py = os.path.join(root, "setup.py")

# ==================================================
# Occurrences: Lines 361-363 (3 instances)

setup_py = os.path.join(root, "setup.py")

# ==================================================
# Occurrences: Lines 1217-1227 (12 instances)

mo = re.search(r'=\s*"(.*)"', line)

# ==================================================
# Occurrences: Lines 1277-1278 (2 instances)

print("likely tags: %s" % ",".join(sorted(tags)))

# ==================================================
# Occurrences: Lines 1987-1989 (3 instances)

root = get_root()

# ==================================================
# Line: 1998

target_versionfile = os.path.join(self.build_lib, cfg.versionfile_build)

# ==================================================
# Occurrences: Lines 2011-2013 (3 instances)

root = get_root()

# ==================================================
# Line: 2025

target_versionfile = os.path.join(self.build_lib, cfg.versionfile_build)

# ==================================================
# Occurrences: Lines 2050-2052 (3 instances)

root = get_root()

# ==================================================
# Occurrences: Lines 2083-2085 (3 instances)

root = get_root()

# ==================================================
# Occurrences: Lines 2120-2121 (2 instances)

root = get_root()

# ==================================================
# Line: 2155

versions = get_versions()

# ==================================================
# Occurrences: Lines 2163-2164 (2 instances)

root = get_root()

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/base.py
# Occurrences: Lines 6647-6656 (2 instances)

polygons = GeoSeries(polygons, crs=self.crs, name="polygons").explode(
    ignore_index=True
)

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/array.py
# Occurrences: Lines 1162-1163 (2 instances)

x_center = np.mean([minx, maxx])

# ==================================================
# Line: 1170

y_center = np.mean([miny, maxy])

# ==================================================
# Occurrences: Lines 1177-1181 (2 instances)

x_center = np.mean([minx, maxx])

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/plotting.py
# Line: 769

fmt = legend_kwds.pop("fmt")

# ==================================================
# Line: 895

legend_kwds.pop("fmt")

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/_version.py
# Occurrences: Lines 179-189 (12 instances)

mo = re.search(r'=\s*"(.*)"', line)

# ==================================================
# Occurrences: Lines 239-240 (2 instances)

print("likely tags: %s" % ",".join(sorted(tags)))

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/explore.py
# Occurrences: Lines 769-771 (2 instances)

fields = gdf.columns.drop(gdf.geometry.name).to_list()

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/io/sql.py
# Occurrences: Lines 185-206 (2 instances)

df = pd.read_sql(
    sql,
    con,
    index_col=index_col,
    coerce_float=coerce_float,
    parse_dates=parse_dates,
    params=params,
    chunksize=chunksize,
)

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/io/file.py
# Line: 509

crs = pyogrio.read_info(path_or_bytes, layer=kwargs.get("layer")).get("crs")

# ==================================================
# Line: 522

crs = pyogrio.read_info(path_or_bytes, layer=kwargs.get("layer")).get("crs")

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/io/_geoarrow.py
# Line: 333

field = pa.field(
    field_name,
    parr.type,
    nullable=True,
    metadata=extension_metadata,
)

# ==================================================
# Occurrences: Lines 344-354 (2 instances)

_parr = _convert_inner_coords(coords, interleaved, dims)

# ==================================================
# Occurrences: Lines 360-370 (4 instances)

_parr = _convert_inner_coords(coords, interleaved, dims)

# ==================================================
# Occurrences: Lines 376-386 (2 instances)

_parr = _convert_inner_coords(coords, interleaved, dims)

# ==================================================
# Occurrences: Lines 392-402 (4 instances)

_parr = _convert_inner_coords(coords, interleaved, dims)

# ==================================================
# Occurrences: Lines 408-419 (3 instances)

_parr = _convert_inner_coords(coords, interleaved, dims)

# ==================================================
# Occurrences: Lines 579-600 (10 instances)

coords = _get_inner_coords(arr.values)

# ==================================================
# Occurrences: Lines 608-609 (2 instances)

offsets3 = np.asarray(arr.offsets)

# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/sindex.py
# Occurrences: Lines 30-35 (2 instances)

non_empty = geometry.copy()

# ==================================================
