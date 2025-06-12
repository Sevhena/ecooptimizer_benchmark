# cached-repeated-calls snippets for pandas

# File: /root/ecooptimizer/pandas/doc/make.py
# Line: 309

joined = ", ".join(cmds)

# ==================================================
# Line: 363

joined = ", ".join(cmds)

# ==================================================
# File: /root/ecooptimizer/pandas/doc/sphinxext/contributors.py
# Occurrences: Lines 31-31 (2 instances)

return [nodes.paragraph(), nodes.bullet_list()]

# ==================================================
# Occurrences: Lines 42-48 (3 instances)

message = nodes.paragraph()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/tseries/frequencies.py
# Occurrences: Lines 431-432 (2 instances)

assert count == int(count)

# ==================================================
# Occurrences: Lines 520-524 (4 instances)

return get_rule_month(source) == get_rule_month(target)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/sql.py
# Occurrences: Lines 1330-1330 (2 instances)

self.frame[col_name] = df_col.astype(col_type)

# ==================================================
# Occurrences: Lines 1336-1340 (4 instances)

self.frame[col_name] = df_col.astype(col_type)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/parsers/c_parser_wrapper.py
# Occurrences: Lines 308-313 (3 instances)

names = _filter_usecols(self.usecols, names)

# ==================================================
# Line: 323

data_tups = sorted(data.items())

# ==================================================
# Occurrences: Lines 330-332 (2 instances)

names = dedup_names(names, is_potential_multi_index(names, self.index_col))

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/parsers/base_parser.py
# Line: 102

self.names = kwds.get("names")

# ==================================================
# Line: 142

if kwds.get("names"):

# ==================================================
# Occurrences: Lines 496-501 (2 instances)

na_count = parsers.sanitize_objects(values, na_values)

# ==================================================
# Line: 520

na_count = parsers.sanitize_objects(values, na_values)

# ==================================================
# Line: 531

bool_mask = np.zeros(result.shape, dtype=np.bool_)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/parsers/readers.py
# Occurrences: Lines 638-644 (3 instances)

if int(val) != val:

# ==================================================
# Line: 1212

value = kwds.get(argname, default)

# ==================================================
# Line: 1247

options[argname] = kwds.get(argname, default)

# ==================================================
# Occurrences: Lines 1692-1693 (4 instances)

if v == int(v):

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/parsers/python_parser.py
# Occurrences: Lines 224-228 (2 instances)

line = f.readline()

# ==================================================
# Line: 251

line = f.readline()

# ==================================================
# Occurrences: Lines 636-636 (2 instances)

for i in range(len(this_columns))

# ==================================================
# Occurrences: Lines 669-669 (2 instances)

lc = len(this_columns)

# ==================================================
# Occurrences: Lines 685-685 (2 instances)

num_original_columns = len(this_columns)

# ==================================================
# Occurrences: Lines 700-700 (2 instances)

if len(names) > len(columns[0]) and len(names) > len_first_data_row:

# ==================================================
# Occurrences: Lines 713-714 (2 instances)

num_original_columns = len(names)

# ==================================================
# Occurrences: Lines 731-734 (3 instances)

elif self.usecols is None or len(names) >= ncols:

# ==================================================
# Line: 903

ret = self._remove_empty_lines([line])

# ==================================================
# Line: 922

ret = self._remove_empty_lines([line])

# ==================================================
# Line: 1119

line = self._next_line()

# ==================================================
# Line: 1125

next_line = self._next_line()

# ==================================================
# Occurrences: Lines 1275-1279 (2 instances)

if self.pos > len(self.data):

# ==================================================
# Line: 1302

len_new_rows = len(new_rows)

# ==================================================
# Occurrences: Lines 1314-1317 (2 instances)

len_new_rows = len(new_rows)

# ==================================================
# Occurrences: Lines 1481-1483 (2 instances)

line = next(self.f)  # type: ignore[arg-type]

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/pytables.py
# Line: 722

tables = _tables()

# ==================================================
# Line: 743

self._filters = _tables().Filters(

# ==================================================
# Line: 1873

index = getattr(value, "index", None)

# ==================================================
# Line: 1880

index = getattr(value, "index", None)

# ==================================================
# Line: 2267

new_pd_index = factory(values, **kwargs)

# ==================================================
# Line: 2287

new_pd_index = factory(values, **kwargs)

# ==================================================
# Occurrences: Lines 3058-3062 (2 instances)

dtype = getattr(attrs, "value_type", None)

# ==================================================
# Occurrences: Lines 3291-3296 (3 instances)

vlarr = self._handle.create_vlarray(self.group, key, _tables().ObjectAtom())

# ==================================================
# Line: 3309

node = getattr(self.group, key)

# ==================================================
# Occurrences: Lines 3316-3321 (4 instances)

getattr(self.group, key)._v_attrs.value_type = "timedelta64"

# ==================================================
# Line: 3327

getattr(self.group, key)._v_attrs.transposed = transposed

# ==================================================
# Line: 3394

shape = getattr(node, "shape", None)

# ==================================================
# Line: 3400

shape = getattr(node, "shape", None)

# ==================================================
# Line: 4099

indexer = len(new_non_index_axes)  # i.e. 0

# ==================================================
# Line: 4141

assert len(new_non_index_axes) == 1

# ==================================================
# Line: 4276

blk_items: list[Index] = get_blk_items(mgr)

# ==================================================
# Line: 4288

blk_items = get_blk_items(mgr)

# ==================================================
# Line: 4295

blk_items.extend(get_blk_items(mgr))

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/stata.py
# Line: 432

d = parse_dates_safe(dates, delta=True)

# ==================================================
# Line: 441

d = parse_dates_safe(dates, delta=True)

# ==================================================
# Occurrences: Lines 447-456 (4 instances)

d = parse_dates_safe(dates, year=True)

# ==================================================
# Occurrences: Lines 563-563 (2 instances)

orig_missing = data[col].isna()

# ==================================================
# Occurrences: Lines 576-576 (2 instances)

data.loc[data[col].isna(), col] = None

# ==================================================
# Occurrences: Lines 582-587 (4 instances)

if empty_df or data[col].max() <= np.iinfo(c_data[1]).max:

# ==================================================
# Occurrences: Lines 595-607 (14 instances)

if data[col].max() > 100 or data[col].min() < -127:

# ==================================================
# Occurrences: Lines 615-617 (4 instances)

value = data[col].max()

# ==================================================
# Occurrences: Lines 670-672 (2 instances)

self.off = np.array([], dtype=np.int32)

# ==================================================
# Occurrences: Lines 1385-1388 (2 instances)

strlen = self._read_int8()

# ==================================================
# Occurrences: Lines 1427-1428 (2 instances)

self._byteorder = ">" if self._read_int8() == 0x1 else "<"

# ==================================================
# Occurrences: Lines 1441-1443 (2 instances)

typlist = [int(c) for c in self._path_or_buf.read(self._nvar)]

# ==================================================
# Occurrences: Lines 1455-1460 (2 instances)

invalid_types = ",".join([str(x) for x in typlist])

# ==================================================
# Occurrences: Lines 1560-1567 (8 instances)

n = self._read_uint32()

# ==================================================
# Line: 1714

data = self._do_select_columns(data, columns)

# ==================================================
# Line: 1762

data = self._do_select_columns(data, columns)

# ==================================================
# Occurrences: Lines 1835-1835 (2 instances)

fmt = cast(str, fmt)  # only strs in OLD_VALID_RANGE

# ==================================================
# Occurrences: Lines 1841-1841 (2 instances)

fmt = cast(str, fmt)  # only strs in VALID_RANGE

# ==================================================
# Occurrences: Lines 2497-2497 (2 instances)

if values.max() >= get_base_missing_value(dtype):

# ==================================================
# Occurrences: Lines 2507-2507 (2 instances)

values[values == -1] = get_base_missing_value(dtype)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/sas/sas_xport.py
# Line: 292

line1 = self._get_row()

# ==================================================
# Line: 302

line2 = self._get_row()

# ==================================================
# Occurrences: Lines 310-315 (3 instances)

line3 = self._get_row()

# ==================================================
# Occurrences: Lines 333-335 (4 instances)

member_info = _split_line(self._get_row(), mem)

# ==================================================
# Line: 342

fieldcount = int(self._get_row()[54:58])

# ==================================================
# Line: 379

header = self._get_row()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/sas/sas7bdat.py
# Occurrences: Lines 398-407 (8 instances)

subheader_offset = self._read_uint(total_offset, self._int_length)

# ==================================================
# Line: 498

buf = self._read_bytes(offset1, self._lcp)

# ==================================================
# Line: 505

buf = self._read_bytes(offset1, self._lcp)

# ==================================================
# Line: 511

buf = self._read_bytes(offset1, self._lcp)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/html.py
# Occurrences: Lines 485-488 (2 instances)

nrows = len(frame)

# ==================================================
# Line: 575

for i in range(len(frame)):

# ==================================================
# Line: 587

zip(*frame.index._format_multi(sparsify=False, include_names=False))

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/string.py
# Line: 165

n_cols = len(col_lens)

# ==================================================
# Line: 175

n_cols = len(col_lens)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/printing.py
# Occurrences: Lines 156-158 (2 instances)

nitems = len(seq)

# ==================================================
# Line: 168

if nitems < len(seq):

# ==================================================
# Line: 218

result = str(thing)

# ==================================================
# Line: 224

return str(thing)

# ==================================================
# Occurrences: Lines 243-245 (2 instances)

result = f"'{as_escaped_string(thing)}'"

# ==================================================
# Line: 340

name_len = len(name)

# ==================================================
# Line: 351

sep = ",\n " + " " * len(name)

# ==================================================
# Occurrences: Lines 382-385 (2 instances)

first = formatter(obj[0])

# ==================================================
# Line: 440

summary, line = _extend_line(summary, line, word, display_width, space2)

# ==================================================
# Line: 449

summary, line = _extend_line(summary, line, word, display_width, space2)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/style_render.py
# Line: 2616

ps = pattern.search(s, pos)

# ==================================================
# Line: 2622

ps = pattern.search(s, pos)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/style.py
# Occurrences: Lines 1831-1834 (2 instances)

setattr(styler, attr, getattr(self, attr))

# ==================================================
# Occurrences: Lines 2399-2400 (2 instances)

if styles.get("css"):

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/format.py
# Occurrences: Lines 1111-1114 (2 instances)

values = cast(DatetimeArray, values)

# ==================================================
# Line: 1418

float_format = partial(fmt_str.format, digits=self.digits)

# ==================================================
# Line: 1424

formatted_values = format_values_with(float_format)

# ==================================================
# Occurrences: Lines 1451-1452 (2 instances)

float_format = partial(fmt_str.format, digits=self.digits)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/common.py
# Line: 435

file_obj = fsspec.open(
    filepath_or_buffer, mode=fsspec_mode, **(storage_options or {})
).open()

# ==================================================
# Line: 446

file_obj = fsspec.open(
    filepath_or_buffer, mode=fsspec_mode, **(storage_options or {})
).open()

# ==================================================
# Line: 748

is_path = isinstance(handle, str)

# ==================================================
# Line: 767

if isinstance(handle, str):

# ==================================================
# Line: 822

if isinstance(handle, str):

# ==================================================
# Occurrences: Lines 879-882 (2 instances)

assert not isinstance(handle, str)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/generic.py
# Line: 5588

values = labels.map(f)

# ==================================================
# Line: 5596

values = labels.map(f)

# ==================================================
# Line: 7082

new_data = self._mgr.fillna(value=value, limit=limit, inplace=inplace)

# ==================================================
# Line: 7142

new_data = self._mgr.fillna(value=value, limit=limit, inplace=inplace)

# ==================================================
# Occurrences: Lines 8066-8069 (2 instances)

self = cast("DataFrame", self)

# ==================================================
# Line: 9627

right = other._reindex_indexer(join_index, ridx)

# ==================================================
# Line: 9645

right = other._reindex_indexer(join_index, ridx)

# ==================================================
# Line: 9705

axis = self._get_axis_number(axis)

# ==================================================
# Line: 9814

align = self._get_axis_number(axis) == 1

# ==================================================
# Line: 9821

result = self._constructor_from_mgr(new_data, axes=new_data.axes)

# ==================================================
# Line: 9830

result = self._constructor_from_mgr(new_data, axes=new_data.axes)

# ==================================================
# Line: 10236

axis = self._get_axis_number(axis)

# ==================================================
# Line: 10255

axis = self._get_axis_number(axis)

# ==================================================
# Occurrences: Lines 10281-10284 (2 instances)

is_period = isinstance(index, PeriodIndex)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/methods/to_dict.py
# Line: 212

("columns", df.columns.tolist()),

# ==================================================
# Line: 221

("columns", df.columns.tolist()),

# ==================================================
# Line: 235

columns = df.columns.tolist()

# ==================================================
# Line: 260

columns = df.columns.tolist()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/methods/selectn.py
# Line: 129

result.index = original_index.take(result.index)

# ==================================================
# Line: 163

narr = len(arr)

# ==================================================
# Line: 169

if len(arr) > 0:

# ==================================================
# Occurrences: Lines 180-183 (4 instances)

if len(inds) < nbase <= len(nan_index) + len(inds):

# ==================================================
# Line: 190

result.index = original_index.take(result.index)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/construction.py
# Line: 324

cls = dtype.construct_array_type()

# ==================================================
# Line: 361

cls = dtype.construct_array_type()

# ==================================================
# Line: 502

dtype = get_supported_dtype(arr.dtype)

# ==================================================
# Line: 508

dtype = get_supported_dtype(arr.dtype)

# ==================================================
# Line: 602

cls = dtype.construct_array_type()

# ==================================================
# Line: 620

subarr = dtype.construct_array_type()._from_sequence(data, dtype=dtype)

# ==================================================
# Line: 630

subarr = _try_cast(data, dtype, copy)

# ==================================================
# Line: 656

subarr = _try_cast(data, dtype, copy)

# ==================================================
# Occurrences: Lines 687-689 (2 instances)

arr = construct_1d_object_array_from_listlike(list(rng))

# ==================================================
# Line: 805

arr = cast(np.ndarray, arr)

# ==================================================
# Line: 817

arr = cast(np.ndarray, arr)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/missing.py
# Line: 593

new_y = terp(new_x)

# ==================================================
# Line: 601

new_y = terp(new_x)

# ==================================================
# Occurrences: Lines 1058-1059 (2 instances)

f_idx = np.array([], dtype=np.int64)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/interchange/column.py
# Line: 317

np_arr = self._col.to_numpy()

# ==================================================
# Line: 353

buf = self._col.to_numpy()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/generic.py
# Occurrences: Lines 619-620 (2 instances)

result = self._insert_inaxis_grouper(result)

# ==================================================
# Occurrences: Lines 628-629 (2 instances)

result = self._insert_inaxis_grouper(result)

# ==================================================
# Occurrences: Lines 1073-1075 (2 instances)

acc = rep(d)[mask]

# ==================================================
# Occurrences: Lines 1935-1937 (2 instances)

result = cast(DataFrame, result)

# ==================================================
# Line: 1985

result = cast(DataFrame, result)

# ==================================================
# Line: 2053

result = result.astype(data.dtypes)

# ==================================================
# Line: 2064

result = result.astype(data.dtypes)

# ==================================================
# Line: 2207

res = _wrap_transform_general_frame(self.obj, group, res)

# ==================================================
# Line: 2218

res = _wrap_transform_general_frame(self.obj, group, res)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/grouper.py
# Line: 626

ucodes = np.arange(len(categories))

# ==================================================
# Line: 635

na_code = len(categories)

# ==================================================
# Line: 756

if is_list_like(level) and len(level) == 1:

# ==================================================
# Line: 769

nlevels = len(level)

# ==================================================
# Line: 835

keys = [None] * len(level)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/categorical.py
# Line: 49

take_codes = unique1d(c.codes[c.codes != -1])  # type: ignore[no-untyped-call]

# ==================================================
# Line: 55

categories = c.categories.take(take_codes)

# ==================================================
# Line: 71

unique_notnan_codes = unique1d(c.codes[c.codes != -1])  # type: ignore[no-untyped-call]

# ==================================================
# Line: 83

return Categorical(c, c.categories.take(take_codes))

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/ops.py
# Line: 232

values = ensure_float64(values)

# ==================================================
# Line: 240

values = ensure_float64(values)

# ==================================================
# Line: 822

ids = ensure_platform_int(ids)

# ==================================================
# Line: 828

ids = ensure_platform_int(ids)

# ==================================================
# Line: 861

ob_ids = ensure_platform_int(ob_ids)

# ==================================================
# Line: 886

ob_ids = ensure_platform_int(ob_ids)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/numba_.py
# Occurrences: Lines 112-113 (4 instances)

assert len(begin) == len(end)

# ==================================================
# Occurrences: Lines 172-173 (4 instances)

assert len(begin) == len(end)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/groupby/groupby.py
# Occurrences: Lines 1153-1156 (2 instances)

result = concat(values, axis=0)

# ==================================================
# Line: 1179

result = concat(values, axis=0)

# ==================================================
# Line: 1204

result = result.set_axis(index, axis=0)

# ==================================================
# Line: 1215

result = result.set_axis(index, axis=0)

# ==================================================
# Occurrences: Lines 4441-4450 (6 instances)

out = vals.to_numpy(dtype=float, na_value=np.nan)

# ==================================================
# Occurrences: Lines 4465-4465 (2 instances)

out = vals.to_numpy(dtype=float, na_value=np.nan)

# ==================================================
# Occurrences: Lines 5795-5798 (2 instances)

codes = [np.repeat(x, nqs) for x in idx.codes] + [np.tile(lev_codes, len(idx))]

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/ops/array_ops.py
# Line: 158

mask = notna(xrav) & ymask.ravel()

# ==================================================
# Line: 172

mask = notna(xrav)

# ==================================================
# Occurrences: Lines 542-544 (3 instances)

new_dtype = get_supported_dtype(obj.dtype)

# ==================================================
# Occurrences: Lines 560-562 (3 instances)

new_dtype = get_supported_dtype(obj.dtype)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/tools/datetimes.py
# Line: 505

arg = arg.astype(object)

# ==================================================
# Line: 516

arg.astype(object), unit, name, utc, errors

# ==================================================
# Line: 591

(is_integer(arg) or is_float(arg)) or is_numeric_dtype(np.asarray(arg))

# ==================================================
# Line: 618

arg = np.asarray(arg)

# ==================================================
# Line: 1016

cache_array = _maybe_cache(arg, format, cache, convert_listlike)

# ==================================================
# Line: 1025

cache_array = _maybe_cache(arg, format, cache, convert_listlike)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/apply.py
# Line: 1054

r = self.func(
    Series([], dtype=np.float64), *self.args, **self.kwargs
)

# ==================================================
# Line: 1070

r = self.func(Series([], dtype=np.float64), *self.args, **self.kwargs)

# ==================================================
# Line: 1298

res = self.obj._constructor_sliced(results)

# ==================================================
# Line: 1307

res = self.obj._constructor_sliced(results)

# ==================================================
# Line: 1317

res = self.obj._constructor_sliced(results)

# ==================================================
# Line: 1443

result = self.infer_to_same_shape(results, res_index)

# ==================================================
# Line: 1452

result = self.infer_to_same_shape(results, res_index)

# ==================================================
# Occurrences: Lines 1544-1549 (2 instances)

return obj.apply(func, by_row=False)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/window/rolling.py
# Line: 785

len(group) == len(other) for group in self._grouper.indices.values()

# ==================================================
# Line: 795

for gb_indices in self._grouper.indices.values()

# ==================================================
# Line: 818

group_indices = self._grouper.indices.values()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/window/numba_.py
# Occurrences: Lines 318-318 (2 instances)

result[0] = np.where(nobs >= minimum_periods, weighted, np.nan)

# ==================================================
# Occurrences: Lines 353-353 (2 instances)

result[i] = np.where(nobs >= minimum_periods, weighted, np.nan)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/window/online.py
# Occurrences: Lines 57-57 (2 instances)

result[0] = np.where(nobs >= minimum_periods, weighted_avg, np.nan)

# ==================================================
# Occurrences: Lines 82-82 (2 instances)

result[i] = np.where(nobs >= minimum_periods, weighted_avg, np.nan)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/sorting.py
# Line: 533

sort_levels = range(index.nlevels)

# ==================================================
# Line: 539

for level in range(index.nlevels)

# ==================================================
# Line: 581

type_of_values = type(values)

# ==================================================
# Line: 587

which could not be converted to {type(values)}."

# ==================================================
# Line: 677

if len(group_index) and np.all(group_index[1:] >= group_index[:-1]):

# ==================================================
# Line: 686

size_hint = len(group_index)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/base.py
# Line: 690

values = np.asarray(values, dtype=dtype)

# ==================================================
# Line: 696

result = np.asarray(values, dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/strings/object_array.py
# Line: 381

new_pat = re.compile(pat)

# ==================================================
# Line: 389

new_pat = re.compile(pat)

# ==================================================
# Line: 523

m = regex.search(x)

# ==================================================
# Line: 533

m = regex.search(x)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/strings/accessor.py
# Occurrences: Lines 703-706 (2 instances)

result = cat_safe(all_cols, sep)

# ==================================================
# Line: 3016

result_list = self._data.array._str_extract(
    pat, flags=flags, expand=returns_df
)

# ==================================================
# Line: 3032

result = self._data.array._str_extract(pat, flags=flags, expand=returns_df)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/nanops.py
# Occurrences: Lines 145-149 (6 instances)

result = alt(values, axis=axis, skipna=skipna, **kwds)

# ==================================================
# Occurrences: Lines 699-705 (3 instances)

dtype_count = np.dtype(np.float64)

# ==================================================
# Line: 1068

nanvar(values, axis=axis, skipna=skipna, ddof=ddof, mask=mask)

# ==================================================
# Line: 1078

var = nanvar(values, axis=axis, skipna=skipna, ddof=ddof, mask=mask)

# ==================================================
# Line: 1685

x = x.astype(np.float64)

# ==================================================
# Line: 1695

x = x.astype(np.float64)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexing.py
# Line: 817

value = self.obj.iloc._align_series(indexer, value)

# ==================================================
# Line: 829

value = self.obj.iloc._align_series(indexer, value)

# ==================================================
# Line: 1409

key = slice(None)

# ==================================================
# Line: 1432

indexer: list[slice | npt.NDArray[np.intp]] = [slice(None)] * self.ndim

# ==================================================
# Line: 2460

val = df.copy()

# ==================================================
# Line: 2468

val = df.copy()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/range.py
# Occurrences: Lines 641-647 (4 instances)

start = len(self)

# ==================================================
# Occurrences: Lines 1010-1022 (6 instances)

ridx = other.get_indexer(join_index)

# ==================================================
# Occurrences: Lines 1126-1131 (6 instances)

values = np.tile(
    non_empty_indexes[0]._values, len(non_empty_indexes)
)

# ==================================================
# Occurrences: Lines 1141-1146 (6 instances)

values = np.tile(
    non_empty_indexes[0]._values, len(non_empty_indexes)
)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/base.py
# Line: 527

data = com.asarray_tuplesafe(data, dtype=_dtype_obj)

# ==================================================
# Line: 568

data = com.asarray_tuplesafe(data, dtype=_dtype_obj)

# ==================================================
# Line: 3264

dtype = self._find_common_type_compat(other)

# ==================================================
# Line: 3287

dtype = self._find_common_type_compat(other)

# ==================================================
# Occurrences: Lines 3352-3354 (2 instances)

result = left_unique.take(taker)

# ==================================================
# Line: 3414

result = self.unique().rename(result_name)

# ==================================================
# Line: 3421

result = self.unique().rename(result_name)

# ==================================================
# Occurrences: Lines 3707-3708 (2 instances)

loc = self.get_loc(np.nan)

# ==================================================
# Occurrences: Lines 3726-3727 (2 instances)

loc = self.get_loc(np.nan)

# ==================================================
# Line: 4261

length = np.arange(len(indexer), dtype=np.intp)

# ==================================================
# Line: 4281

new_indexer = np.arange(len(indexer), dtype=np.intp)

# ==================================================
# Line: 4497

rindexer = other.get_indexer_for(join_index)

# ==================================================
# Line: 4504

lindexer = self.get_indexer_for(join_index)

# ==================================================
# Occurrences: Lines 4527-4531 (2 instances)

lindexer = self.get_indexer_for(join_index)

# ==================================================
# Line: 4637

join_index = other.take(right_idx)

# ==================================================
# Line: 4644

right = other.take(right_idx)

# ==================================================
# Line: 4748

if not mask.all():

# ==================================================
# Line: 4766

mask_all = mask.all()

# ==================================================
# Line: 4829

join_index, lidx, ridx = self._wrap_join_result(
    join_array, other, lidx, ridx, how
)

# ==================================================
# Occurrences: Lines 4840-4852 (3 instances)

join_index, lidx, ridx = self._wrap_join_result(
    join_array, other, lidx, ridx, how
)

# ==================================================
# Line: 5231

return getitem(key)

# ==================================================
# Line: 5255

result = getitem(key)

# ==================================================
# Line: 6820

end_slice = len(self)

# ==================================================
# Occurrences: Lines 6843-6845 (2 instances)

end_slice -= len(self)

# ==================================================
# Line: 6930

dtype = self._find_common_type_compat(item)

# ==================================================
# Line: 6944

dtype = self._find_common_type_compat(item)

# ==================================================
# Occurrences: Lines 7139-7142 (2 instances)

result = op(self._values, other)

# ==================================================
# Occurrences: Lines 7763-7764 (2 instances)

result = values._format_native_types(na_rep=na_rep, date_format=date_format)

# ==================================================
# Line: 7773

results_converted.append(result.astype(object, copy=False))

# ==================================================
# Line: 7779

res = values._format_native_types(na_rep=na_rep, date_format=date_format)

# ==================================================
# Occurrences: Lines 7799-7807 (4 instances)

mask = isna(values)

# ==================================================
# Line: 7825

mask = isna(values)

# ==================================================
# Occurrences: Lines 7832-7844 (4 instances)

mask = isna(values)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/timedeltas.py
# Line: 166

data = data.copy()

# ==================================================
# Line: 176

return data.copy()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/interval.py
# Occurrences: Lines 792-797 (4 instances)

locs = np.array([-1])

# ==================================================
# Line: 1269

breaks = maybe_downcast_numeric(breaks, dtype)

# ==================================================
# Line: 1282

breaks = maybe_downcast_numeric(breaks, dtype)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/extension.py
# Line: 62

return getattr(self._data, name)

# ==================================================
# Line: 71

result = getattr(self._data, name)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/multi.py
# Line: 400

levels_to_verify = range(len(levels))

# ==================================================
# Line: 437

for i in range(len(levels)):

# ==================================================
# Line: 908

ensure_index(lev, copy=copy)._view() for lev in levels

# ==================================================
# Line: 915

new_levels_list[lev_num] = ensure_index(lev, copy=copy)._view()

# ==================================================
# Line: 1149

_coerce_indexer_frozen(level_codes, lev, copy=copy).view()

# ==================================================
# Line: 1158

new_codes_list[lev_num] = _coerce_indexer_frozen(
    level_codes, lev, copy=copy
)

# ==================================================
# Occurrences: Lines 3026-3032 (3 instances)

if len(tup) > self._lexsort_depth:

# ==================================================
# Occurrences: Lines 3154-3158 (2 instances)

loc = lib.maybe_indices_to_slice(loc, len(self))

# ==================================================
# Line: 3194

stop = len(self)

# ==================================================
# Line: 3321

mask = np.zeros(len(self), dtype=bool)

# ==================================================
# Line: 3345

indexer = self._get_level_indexer(key, level=level)

# ==================================================
# Line: 3365

ilevels = [i for i in range(len(key)) if key[i] != slice(None, None)]

# ==================================================
# Line: 3381

and key[i] != slice(None, None)

# ==================================================
# Line: 3401

k_index = np.zeros(len(self), dtype=bool)

# ==================================================
# Occurrences: Lines 3421-3425 (3 instances)

indexer = slice(None, None)

# ==================================================
# Line: 3486

start = len(level_index) - 1

# ==================================================
# Occurrences: Lines 3495-3497 (2 instances)

stop = len(level_index)

# ==================================================
# Occurrences: Lines 3636-3636 (2 instances)

lvl_indexer = self._get_level_indexer(k, level=i, indexer=indexer)

# ==================================================
# Occurrences: Lines 3673-3673 (2 instances)

lvl_indexer = self._get_level_indexer(k, level=i, indexer=indexer)

# ==================================================
# Line: 3723

k_codes = self.levels[i].get_indexer(k)

# ==================================================
# Line: 3761

level_indexer = self.levels[i].get_indexer(k)

# ==================================================
# Line: 4232

index = index._drop_level_numbers([0])

# ==================================================
# Line: 4238

index = index._drop_level_numbers([0])

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexers/objects.py
# Occurrences: Lines 270-272 (2 instances)

start = np.empty(num_values, dtype="int64")

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/util/hashing.py
# Occurrences: Lines 129-137 (2 instances)

h = hash_array(obj._values, encoding, hash_key, categorize).astype(
    "uint64", copy=False
)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/dtypes/cast.py
# Occurrences: Lines 308-312 (2 instances)

result = cast(np.ndarray, result)

# ==================================================
# Line: 363

return trans(result).astype(dtype)

# ==================================================
# Line: 377

new_result = trans(result).astype(dtype)

# ==================================================
# Line: 395

new_result = result.astype(dtype)

# ==================================================
# Line: 408

new_result = result.astype(dtype)

# ==================================================
# Line: 646

inferred, fv = infer_dtype_from_scalar(fill_value)

# ==================================================
# Line: 660

inferred, fv = infer_dtype_from_scalar(fill_value)

# ==================================================
# Line: 679

dtype = np.dtype(np.object_)

# ==================================================
# Line: 685

mst = np.min_scalar_type(fill_value)

# ==================================================
# Occurrences: Lines 691-720 (11 instances)

mst = np.min_scalar_type(fill_value)

# ==================================================
# Occurrences: Lines 726-730 (2 instances)

dtype = np.dtype(np.object_)

# ==================================================
# Line: 836

dtype = np.dtype(type(val))

# ==================================================
# Line: 847

dtype = np.dtype(type(val))

# ==================================================
# Line: 910

return arr.dtype, np.asarray(arr)

# ==================================================
# Line: 917

arr = np.asarray(arr)

# ==================================================
# Occurrences: Lines 1042-1045 (2 instances)

inferred_dtype = pandas_dtype_func("string")

# ==================================================
# Line: 1073

input_array.dtype, pandas_dtype_func("Float64")

# ==================================================
# Line: 1081

inferred_dtype = pandas_dtype_func("Int64")

# ==================================================
# Occurrences: Lines 1094-1100 (3 instances)

inferred_dtype = pandas_dtype_func("Float64")

# ==================================================
# Line: 1111

inferred_dtype = pandas_dtype_func("string")

# ==================================================
# Occurrences: Lines 1420-1423 (2 instances)

common_dtype = np.dtype("O")

# ==================================================
# Occurrences: Lines 1479-1481 (2 instances)

return np.dtype(max(types))

# ==================================================
# Line: 1805

return dtype.type(element)

# ==================================================
# Line: 1815

casted = element.astype(dtype)

# ==================================================
# Line: 1830

casted = element.astype(dtype)

# ==================================================
# Line: 1849

casted = element.astype(dtype)

# ==================================================
# Line: 1871

casted = dtype.type(element)

# ==================================================
# Line: 1891

casted = element.astype(dtype)

# ==================================================
# Occurrences: Lines 1904-1908 (2 instances)

return dtype.type(element)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/dtypes/missing.py
# Occurrences: Lines 206-209 (2 instances)

return _isna_array(obj._values)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/dtypes/astype.py
# Line: 86

res = arr.astype(dtype, copy=copy)

# ==================================================
# Line: 132

return arr.astype(dtype, copy=copy)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/dtypes/concat.py
# Occurrences: Lines 76-79 (3 instances)

to_concat_arrs = cast("Sequence[np.ndarray]", to_concat)

# ==================================================
# Line: 111

to_concat_eas = cast("Sequence[ExtensionArray]", to_concat)

# ==================================================
# Occurrences: Lines 124-125 (2 instances)

to_concat_arrs = cast("Sequence[np.ndarray]", to_concat)

# ==================================================
# Line: 307

categories = categories.sort_values()

# ==================================================
# Line: 318

categories = categories.sort_values()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/dtypes/common.py
# Line: 698

src = _get_dtype(source)

# ==================================================
# Line: 707

source = _get_dtype(source)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/array_algos/take.py
# Occurrences: Lines 238-243 (3 instances)

func = _take_1d_dict.get(tup, None)

# ==================================================
# Occurrences: Lines 252-257 (3 instances)

func = _take_1d_dict.get(tup, None)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/array_algos/replace.py
# Line: 99

result = op(a)

# ==================================================
# Line: 108

result = op(a)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/array_algos/quantile.py
# Occurrences: Lines 210-215 (2 instances)

and (result == result.astype(values.dtype, copy=False)).all()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/series.py
# Line: 393

data = data.copy(deep=False)

# ==================================================
# Occurrences: Lines 402-407 (2 instances)

data = data.copy()

# ==================================================
# Line: 508

data = data.copy()

# ==================================================
# Line: 949

return self._get_value(key)

# ==================================================
# Line: 960

result = self._get_value(key)

# ==================================================
# Line: 3171

new_values = np.empty(len(new_index), dtype=object)

# ==================================================
# Line: 3181

new_values = np.empty(len(new_index), dtype=object)

# ==================================================
# Occurrences: Lines 6045-6050 (2 instances)

return self._binop(other, op, level=level, fill_value=fill_value)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/resample.py
# Line: 475

result = grouped.apply(how, *args, **kwargs)

# ==================================================
# Line: 487

result = grouped.apply(how, *args, **kwargs)

# ==================================================
# Occurrences: Lines 2855-2859 (2 instances)

new_obj = obj.copy()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/computation/pytables.py
# Line: 223

conv_val = stringify(conv_val)

# ==================================================
# Occurrences: Lines 251-256 (2 instances)

float(conv_val)

# ==================================================
# Line: 276

return TermValue(conv_val, stringify(conv_val), "string")

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/computation/expr.py
# Occurrences: Lines 446-450 (2 instances)

right = self.term_type(name, self.env)

# ==================================================
# Line: 473

left = self.term_type(name, self.env)

# ==================================================
# Line: 482

right = self.term_type(name, self.env)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/computation/ops.py
# Occurrences: Lines 448-451 (2 instances)

v = stringify(v)

# ==================================================
# Occurrences: Lines 457-460 (2 instances)

v = stringify(v)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/computation/common.py
# Line: 28

return reduce(np.result_type, arrays_and_dtypes)

# ==================================================
# Line: 45

np_dtype = reduce(np.result_type, arrays_and_dtypes)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/computation/align.py
# Occurrences: Lines 214-216 (2 instances)

ret_value = res_t.type(obj)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/pivot.py
# Line: 561

all_key = _all_key(key)

# ==================================================
# Line: 578

all_key = _all_key(key)

# ==================================================
# Line: 651

all_key = _all_key()

# ==================================================
# Line: 658

all_key = _all_key()

# ==================================================
# Line: 858

cols = com.convert_to_list_like(index)

# ==================================================
# Line: 882

index_list = [data[idx] for idx in com.convert_to_list_like(index)]

# ==================================================
# Line: 1149

table = table.fillna(0)

# ==================================================
# Occurrences: Lines 1173-1180 (4 instances)

table = concat([table, column_margin], axis=1)

# ==================================================
# Occurrences: Lines 1187-1190 (3 instances)

table = concat([table, column_margin], axis=1)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/tile.py
# Line: 411

unit = dtype_to_unit(x_idx.dtype)  # type: ignore[arg-type]

# ==================================================
# Line: 423

bins = np.linspace(mn, mx, nbins + 1, endpoint=True)

# ==================================================
# Line: 430

unit = dtype_to_unit(x_idx.dtype)  # type: ignore[arg-type]

# ==================================================
# Line: 437

bins = np.linspace(mn, mx, nbins + 1, endpoint=True)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/encoding.py
# Occurrences: Lines 267-269 (2 instances)

dtype = np.dtype(bool)

# ==================================================
# Occurrences: Lines 281-297 (6 instances)

index = default_index(len(data))

# ==================================================
# Line: 314

elif dtype == np.dtype(bool):

# ==================================================
# Line: 320

N = len(data)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/merge.py
# Occurrences: Lines 1570-1570 (2 instances)

rk = cast(ArrayLike, rk)

# ==================================================
# Occurrences: Lines 1576-1576 (2 instances)

rk = cast(Hashable, rk)

# ==================================================
# Occurrences: Lines 1588-1588 (2 instances)

rk = cast(Hashable, rk)

# ==================================================
# Occurrences: Lines 1597-1597 (2 instances)

rk = cast(ArrayLike, rk)

# ==================================================
# Occurrences: Lines 1612-1613 (2 instances)

k = extract_array(k, extract_numpy=True)

# ==================================================
# Line: 1619

k = cast(Hashable, k)

# ==================================================
# Occurrences: Lines 1633-1635 (2 instances)

k = extract_array(k, extract_numpy=True)

# ==================================================
# Line: 1641

k = cast(Hashable, k)

# ==================================================
# Occurrences: Lines 1685-1686 (4 instances)

lk = cast(Categorical, lk)

# ==================================================
# Occurrences: Lines 1712-1721 (8 instances)

ct = find_common_type([lk.dtype, rk.dtype])

# ==================================================
# Occurrences: Lines 1768-1770 (4 instances)

if lib.infer_dtype(lk, skipna=False) == lib.infer_dtype(

# ==================================================
# Occurrences: Lines 1786-1787 (4 instances)

inferred_left = lib.infer_dtype(lk, skipna=False)

# ==================================================
# Occurrences: Lines 1839-1843 (4 instances)

typ = cast(Categorical, lk).categories.dtype if lk_is_cat else object

# ==================================================
# Occurrences: Lines 1897-1899 (2 instances)

n = len(left_on)

# ==================================================
# Occurrences: Lines 1912-1914 (2 instances)

n = len(right_on)

# ==================================================
# Occurrences: Lines 1920-1920 (2 instances)

if len(right_on) != len(left_on):

# ==================================================
# Line: 2573

func = _asof_by_function(self.direction)

# ==================================================
# Line: 2584

func = _asof_by_function(self.direction)

# ==================================================
# Line: 2784

len_lk = len(lk)

# ==================================================
# Occurrences: Lines 2805-2811 (3 instances)

llab, rlab = _sort_labels(uniques, llab, rlab)

# ==================================================
# Line: 2843

max(len(lk), len(rk)),

# ==================================================
# Occurrences: Lines 2867-2890 (9 instances)

rlab = rizer.factorize(rk_data, mask=rk_mask)

# ==================================================
# Occurrences: Lines 2914-2922 (4 instances)

lk = lk.astype(dtype, copy=False)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/reshape.py
# Line: 462

dummy = data.copy(deep=False)

# ==================================================
# Line: 484

dummy_df = data.copy(deep=False)

# ==================================================
# Occurrences: Lines 682-686 (2 instances)

new_values = frame._values.ravel()

# ==================================================
# Line: 704

result = stack(result, lev, dropna=dropna, sort=sort)  # type: ignore[assignment]

# ==================================================
# Line: 719

result = stack(result, lev, dropna=dropna, sort=sort)  # type: ignore[assignment]

# ==================================================
# Line: 956

ratio = 0 if frame.empty else len(result) // len(frame)

# ==================================================
# Line: 984

column_codes = [np.repeat(codes, len(frame)) for codes in column_codes]  # type: ignore[assignment]

# ==================================================
# Line: 993

len_df = len(frame)

# ==================================================
# Line: 1070

new_columns = frame.columns._drop_level_numbers(drop_levnums).unique()

# ==================================================
# Line: 1077

desired_columns = frame.columns._drop_level_numbers(drop_levnums).unique()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/concat.py
# Line: 538

new_index = _get_concat_axis_series(
    objs,
    ignore_index,
    bm_axis,
    keys,
    levels,
    verify_integrity,
    names,
)

# ==================================================
# Line: 569

columns = _get_concat_axis_series(
    objs, ignore_index, bm_axis, keys, levels, verify_integrity, names
)

# ==================================================
# Line: 810

if obj.ndim == max_ndim and sum(obj.shape):  # type: ignore[arg-type]

# ==================================================
# Line: 816

non_empties = [obj for obj in objs if sum(obj.shape)]

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/melt.py
# Line: 191

level = frame.columns.get_level_values(col_level)

# ==================================================
# Occurrences: Lines 208-214 (3 instances)

frame = frame.copy(deep=False)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/accessor.py
# Occurrences: Lines 117-121 (2 instances)

doc=getattr(delegate, accessor_mapping(name)).__doc__,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/sparse/array.py
# Line: 201

fill = op(_get_fill(left), _get_fill(right))

# ==================================================
# Line: 210

fill = op(_get_fill(left), _get_fill(right))

# ==================================================
# Line: 405

dtype = pandas_dtype(dtype)

# ==================================================
# Line: 419

dtype = pandas_dtype(dtype)

# ==================================================
# Line: 439

data = np.atleast_1d(np.asarray(data, dtype=dtype))

# ==================================================
# Line: 490

sparse_values = np.asarray(data, dtype=dtype)  # type: ignore[arg-type]

# ==================================================
# Occurrences: Lines 758-760 (2 instances)

return type(self)._simple_new(isna(self.sp_values), self.sp_index, dtype)

# ==================================================
# Occurrences: Lines 976-980 (3 instances)

start += len(self)

# ==================================================
# Occurrences: Lines 997-1001 (2 instances)

new_len = len(range(len(self))[key])

# ==================================================
# Line: 1023

n = len(self)

# ==================================================
# Occurrences: Lines 1128-1133 (2 instances)

taken = taken.astype(result_type)

# ==================================================
# Line: 1201

data = np.concatenate(values)

# ==================================================
# Line: 1225

data = np.concatenate(values)

# ==================================================
# Line: 1766

fill = op(_get_fill(self), np.asarray(other))

# ==================================================
# Line: 1780

other = np.asarray(other)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/datetimelike.py
# Line: 601

msg = self._validation_error_message(value, allow_listlike)

# ==================================================
# Line: 611

msg = self._validation_error_message(value, allow_listlike)

# ==================================================
# Line: 620

msg = self._validation_error_message(value, allow_listlike)

# ==================================================
# Line: 665

value = value.as_unit(self.unit, round_ok=False)  # type: ignore[attr-defined]

# ==================================================
# Line: 681

msg = self._validation_error_message(value, True)

# ==================================================
# Occurrences: Lines 687-689 (2 instances)

value = extract_array(value, extract_numpy=True)

# ==================================================
# Line: 705

value = extract_array(value, extract_numpy=True)

# ==================================================
# Occurrences: Lines 711-716 (2 instances)

msg = self._validation_error_message(value, True)

# ==================================================
# Line: 1079

self = cast("TimedeltaArray", self)

# ==================================================
# Occurrences: Lines 1095-1102 (3 instances)

self = cast("TimedeltaArray", self)

# ==================================================
# Occurrences: Lines 1372-1373 (2 instances)

obj = cast("PeriodArray", self)

# ==================================================
# Occurrences: Lines 1390-1391 (2 instances)

obj = cast("PeriodArray", self)

# ==================================================
# Occurrences: Lines 1430-1434 (3 instances)

obj = cast("PeriodArray", self)

# ==================================================
# Occurrences: Lines 1450-1455 (3 instances)

result = self._sub_periodlike(other)

# ==================================================
# Line: 2009

freq = to_offset(freq)

# ==================================================
# Line: 2015

freq = to_offset(freq)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/masked.py
# Line: 247

new_values = self.copy()

# ==================================================
# Line: 253

new_values = self.copy()

# ==================================================
# Occurrences: Lines 547-551 (2 instances)

cls = dtype.construct_array_type()

# ==================================================
# Occurrences: Lines 647-653 (6 instances)

m = mask.copy()

# ==================================================
# Occurrences: Lines 1035-1038 (2 instances)

size = len(uniques)

# ==================================================
# Occurrences: Lines 1158-1160 (2 instances)

out_mask = np.zeros(res.shape, dtype=bool)

# ==================================================
# Line: 1526

mask = self._mask.copy()

# ==================================================
# Line: 1533

mask = self._mask.copy()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/arrow/array.py
# Occurrences: Lines 348-352 (2 instances)

scalars = to_datetime(strings, errors="raise")

# ==================================================
# Line: 363

strings = pa.array(strings, type=pa.string(), from_pandas=True)

# ==================================================
# Line: 384

scalars = pa.array(strings, type=pa.string(), from_pandas=True)

# ==================================================
# Line: 446

value = value.as_unit(pa_type.unit)

# ==================================================
# Line: 452

value = value.as_unit(pa_type.unit)

# ==================================================
# Line: 485

value = value.copy()

# ==================================================
# Line: 500

value = value.copy()

# ==================================================
# Occurrences: Lines 511-514 (2 instances)

value = value.to_numpy()

# ==================================================
# Occurrences: Lines 524-525 (2 instances)

value = value.to_numpy()

# ==================================================
# Occurrences: Lines 539-542 (2 instances)

pa_array = pa_array.cast(pa_type)

# ==================================================
# Occurrences: Lines 734-742 (4 instances)

result = pc_func(self._pa_array, self._box_pa(other))

# ==================================================
# Occurrences: Lines 751-752 (2 instances)

result = ops.invalid_comparison(self, other, op)

# ==================================================
# Occurrences: Lines 797-798 (2 instances)

pa_integral = pc.if_else(pc.less(integral, 0), 0, integral)

# ==================================================
# Occurrences: Lines 809-810 (2 instances)

pa_integral = pc.if_else(pc.less(integral, 0), 0, integral)

# ==================================================
# Occurrences: Lines 1211-1215 (2 instances)

encoded = data.dictionary_encode(null_encoding=null_encoding)

# ==================================================
# Occurrences: Lines 1362-1367 (3 instances)

result = self._pa_array.take(indices_array)

# ==================================================
# Line: 1380

return type(self)(self._pa_array.take(indices_array))

# ==================================================
# Line: 1450

result[data.isna()] = na_value

# ==================================================
# Line: 1475

mask = data.isna()

# ==================================================
# Line: 1761

data_to_cmp = self._pa_array.cast(pa.int64())

# ==================================================
# Line: 1769

data_to_reduce = self._pa_array.cast(pa.int64())

# ==================================================
# Line: 1776

data_to_reduce = self._pa_array.cast(pa.int64())

# ==================================================
# Line: 1853

result = result.cast(pa_type)

# ==================================================
# Occurrences: Lines 1860-1865 (4 instances)

result = result.cast(pa.int64(), **cast_kwargs)

# ==================================================
# Line: 1992

n = len(self)

# ==================================================
# Occurrences: Lines 2015-2020 (3 instances)

mask = np.zeros(len(self), dtype=np.bool_)

# ==================================================
# Occurrences: Lines 2029-2029 (2 instances)

mask = np.zeros(len(self), dtype=np.bool_)

# ==================================================
# Line: 2056

pa_type = pa.float64()

# ==================================================
# Occurrences: Lines 2086-2092 (5 instances)

result_max = result_max.cast(pa.float64())

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/base.py
# Line: 1251

new_values = self.copy()

# ==================================================
# Line: 1257

new_values = self.copy()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/numeric.py
# Line: 160

values = values.copy()

# ==================================================
# Occurrences: Lines 173-178 (2 instances)

name = dtype_cls.__name__.strip("_")

# ==================================================
# Line: 185

name = dtype_cls.__name__.strip("_")

# ==================================================
# Line: 194

mask = np.zeros(len(values), dtype=np.bool_)

# ==================================================
# Line: 231

values = values.copy()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/timedeltas.py
# Occurrences: Lines 371-376 (2 instances)

for i in range(len(self)):

# ==================================================
# Line: 530

return op(self._ndarray, other)

# ==================================================
# Line: 541

result = op(self._ndarray, other)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/interval.py
# Line: 2027

values = np.asarray(values)

# ==================================================
# Line: 2035

values = np.asarray(values)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/string_arrow.py
# Occurrences: Lines 248-252 (2 instances)

values = values.fill_null(na)

# ==================================================
# Occurrences: Lines 443-445 (2 instances)

arr = pc.or_kleene(nas, pc.not_equal(self._pa_array, ""))

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/categorical.py
# Occurrences: Lines 427-430 (2 instances)

values = sanitize_array(values, None)

# ==================================================
# Line: 462

values = sanitize_array(values, None)

# ==================================================
# Occurrences: Lines 2265-2271 (3 instances)

cur_col_len = len(levheader)  # header

# ==================================================
# Line: 2304

length = len(self)

# ==================================================
# Line: 2313

length_info = f"Length: {len(self)}"

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/string_.py
# Line: 155

storage = get_option("mode.string_storage")

# ==================================================
# Line: 162

storage = get_option("mode.string_storage")

# ==================================================
# Occurrences: Lines 778-781 (2 instances)

mask = isna(value)

# ==================================================
# Occurrences: Lines 820-831 (5 instances)

return self.copy()

# ==================================================
# Occurrences: Lines 839-840 (2 instances)

arr = self._ndarray.copy()

# ==================================================
# Occurrences: Lines 1064-1069 (2 instances)

result[valid] = op(self._ndarray[valid], other)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/datetimes.py
# Occurrences: Lines 157-162 (4 instances)

result = fields.get_date_field(values, field, reso=self._creso)

# ==================================================
# Line: 371

tz = _validate_tz_from_dtype(dtype, tz, explicit_tz_none)

# ==================================================
# Line: 394

_validate_tz_from_dtype(dtype, tz, explicit_tz_none)

# ==================================================
# Occurrences: Lines 677-682 (2 instances)

for i in range(len(self)):

# ==================================================
# Line: 2430

data = cast(np.ndarray, data)

# ==================================================
# Line: 2484

data = cast(np.ndarray, data)

# ==================================================
# Line: 2495

data = cast(np.ndarray, data)

# ==================================================
# Occurrences: Lines 2999-3000 (2 instances)

next_date = offset._apply(cur)

# ==================================================
# Occurrences: Lines 3014-3015 (2 instances)

next_date = offset._apply(cur)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/boolean.py
# Occurrences: Lines 182-183 (2 instances)

values = values.copy()

# ==================================================
# Occurrences: Lines 189-193 (2 instances)

values = values.copy()

# ==================================================
# Line: 213

values = np.zeros(len(values), dtype=bool)

# ==================================================
# Line: 235

mask = mask.copy()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/period.py
# Occurrences: Lines 1424-1425 (2 instances)

freq = to_offset(freq, is_period=True)

# ==================================================
# Occurrences: Lines 1438-1439 (2 instances)

freq = to_offset(freq, is_period=True)

# ==================================================
# Occurrences: Lines 1451-1454 (4 instances)

if length is not None and len(x) != length:

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/frame.py
# Line: 720

data = data.copy(deep=False)

# ==================================================
# Line: 733

data = data.copy(deep=False)

# ==================================================
# Line: 783

mgr = ndarray_to_mgr(
    data,
    index,
    columns,
    dtype=dtype,
    copy=copy,
)

# ==================================================
# Line: 814

mgr = ndarray_to_mgr(
    data,
    index,
    columns,
    dtype=dtype,
    copy=copy,
)

# ==================================================
# Line: 836

columns = ensure_index(columns)

# ==================================================
# Line: 852

mgr = ndarray_to_mgr(
    data,
    index,
    columns,
    dtype=dtype,
    copy=copy,
)

# ==================================================
# Line: 872

columns = ensure_index(columns)

# ==================================================
# Line: 1720

np.dot(lvals, rvals),

# ==================================================
# Occurrences: Lines 1729-1732 (2 instances)

np.dot(lvals, rvals), index=left.index, copy=False, dtype=common_type

# ==================================================
# Occurrences: Lines 2274-2282 (3 instances)

arrays, arr_columns, result_index = maybe_reorder(
    arrays, arr_columns, columns, index
)

# ==================================================
# Line: 2298

arrays, arr_columns, result_index = maybe_reorder(
    arrays, arr_columns, columns, index
)

# ==================================================
# Line: 4004

is_mi = isinstance(self.columns, MultiIndex)

# ==================================================
# Line: 4057

if data.shape[1] == 1 and not isinstance(self.columns, MultiIndex):

# ==================================================
# Line: 4312

self[col] = igetitem(value, i)

# ==================================================
# Line: 4332

self[iloc] = igetitem(value, i)

# ==================================================
# Line: 5919

for col in range(min(ncols, abs(periods))):

# ==================================================
# Line: 5926

for col in range(min(ncols, abs(periods))):

# ==================================================
# Line: 5944

nper = abs(periods)

# ==================================================
# Occurrences: Lines 7259-7262 (2 instances)

return self.copy(deep=False)

# ==================================================
# Line: 8272

right = to_series(right)

# ==================================================
# Occurrences: Lines 8284-8293 (2 instances)

right = left._constructor(
    right, index=left.index, columns=left.columns, dtype=dtype
)

# ==================================================
# Line: 8318

right = to_series(right)

# ==================================================
# Occurrences: Lines 8895-8895 (2 instances)

series = series.astype(new_dtype)

# ==================================================
# Occurrences: Lines 8902-8902 (2 instances)

series = series.astype(new_dtype)

# ==================================================
# Occurrences: Lines 9152-9163 (8 instances)

mask = ~filter_func(this) | isna(that)

# ==================================================
# Line: 10654

r = func(Series([], dtype=np.float64), *args, **kwargs)

# ==================================================
# Line: 10666

r = func(Series([], dtype=np.float64), *args, **kwargs)

# ==================================================
# Occurrences: Lines 11789-11792 (3 instances)

dtype = find_common_type([block.values.dtype for block in df._mgr.blocks])

# ==================================================
# Line: 11814

dtype = find_common_type(
    [block.values.dtype for block in df._mgr.blocks]
)

# ==================================================
# Occurrences: Lines 11825-11826 (2 instances)

df = df.astype(dtype)

# ==================================================
# Line: 13535

dtype = find_common_type(list(self.dtypes))

# ==================================================
# Line: 13553

cdtype = find_common_type(list(self.dtypes))

# ==================================================
# Line: 13577

dtype = find_common_type(list(self.dtypes))

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/common.py
# Line: 243

return construct_1d_object_array_from_listlike(values)

# ==================================================
# Line: 257

return construct_1d_object_array_from_listlike(values)  # type: ignore[arg-type]

# ==================================================
# Line: 265

result = construct_1d_object_array_from_listlike(values)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arraylike.py
# Line: 372

return reconstruct(result)

# ==================================================
# Occurrences: Lines 395-399 (2 instances)

result = getattr(ufunc, method)(*inputs, **kwargs)

# ==================================================
# Line: 414

result = reconstruct(result)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/internals/construction.py
# Line: 112

index = ensure_index(index)

# ==================================================
# Line: 123

index = ensure_index(index)

# ==================================================
# Line: 252

values = _ensure_2d(values)

# ==================================================
# Line: 262

values = _ensure_2d(values)

# ==================================================
# Line: 302

nb = new_block_2d(values, placement=bp, refs=refs)

# ==================================================
# Line: 319

nb = new_block_2d(values, placement=bp, refs=refs)

# ==================================================
# Occurrences: Lines 498-501 (2 instances)

values = np.array([convert(v) for v in values])

# ==================================================
# Line: 647

has_some_name = any(getattr(s, "name", None) is not None for s in data)

# ==================================================
# Line: 654

n = getattr(s, "name", None)

# ==================================================
# Line: 758

arr = _list_to_arrays(data)

# ==================================================
# Line: 766

arr = _list_to_arrays(data)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/internals/blocks.py
# Occurrences: Lines 922-925 (2 instances)

nb = nb.copy()

# ==================================================
# Line: 1158

values = cast(np.ndarray, self.values)

# ==================================================
# Line: 1175

values = cast(np.ndarray, self.values)

# ==================================================
# Occurrences: Lines 1647-1651 (2 instances)

nb = self.coerce_to_target_dtype(orig_value, raise_on_upcast=True)

# ==================================================
# Line: 1688

blk = self.coerce_to_target_dtype(orig_other, raise_on_upcast=False)

# ==================================================
# Line: 1701

blk = self.coerce_to_target_dtype(orig_other, raise_on_upcast=False)

# ==================================================
# Line: 1758

blk = self.coerce_to_target_dtype(orig_new, raise_on_upcast=True)

# ==================================================
# Line: 1764

blk = self.coerce_to_target_dtype(orig_new, raise_on_upcast=True)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/internals/managers.py
# Occurrences: Lines 136-138 (2 instances)

dtype = np.dtype("object")

# ==================================================
# Occurrences: Lines 1332-1332 (2 instances)

self._blknos[unfit_idxr] = np.arange(unfit_count) + len(self.blocks)

# ==================================================
# Occurrences: Lines 1347-1348 (2 instances)

self._blknos[unfit_idxr] = len(self.blocks)

# ==================================================
# Occurrences: Lines 1493-1494 (2 instances)

self._blklocs = np.array([0], dtype=np.intp)

# ==================================================
# Occurrences: Lines 1587-1590 (4 instances)

result_blocks = extend_blocks(applied, result_blocks)

# ==================================================
# Occurrences: Lines 1706-1707 (2 instances)

assert fac == int(fac)

# ==================================================
# Line: 1851

arr = blk.get_values(dtype)

# ==================================================
# Line: 1868

arr = blk.get_values(dtype)

# ==================================================
# Line: 2483

cls = dtype.construct_array_type()

# ==================================================
# Line: 2493

cls = dtype.construct_array_type()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/internals/concat.py
# Line: 88

mgrs = _maybe_reindex_columns_na_proxy(axes, mgrs_indexers, needs_copy)

# ==================================================
# Line: 107

mgrs = _maybe_reindex_columns_na_proxy(axes, mgrs_indexers, needs_copy)

# ==================================================
# Occurrences: Lines 218-219 (2 instances)

bp = libinternals.BlockPlacement(slice(shape[0]))

# ==================================================
# Occurrences: Lines 246-247 (2 instances)

bp = libinternals.BlockPlacement(slice(shape[0]))

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/algorithms.py
# Occurrences: Lines 466-471 (2 instances)

uniques = _reconstruct_data(uniques, original.dtype, original)

# ==================================================
# Line: 1493

ordered = _sort_mixed(values)

# ==================================================
# Line: 1508

ordered = _sort_mixed(values)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/compat/pickle_compat.py
# Occurrences: Lines 98-107 (4 instances)

args = self.stack.pop()  # type: ignore[attr-defined]

# ==================================================
