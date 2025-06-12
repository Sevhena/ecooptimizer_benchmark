# cached-repeated-calls snippets for dask

# File: /root/ecooptimizer/dask/dask/local.py
# Occurrences: Lines 174-177 (4 instances)

dependencies = defaultdict(set)

# ==================================================
# Occurrences: Lines 540-540 (3 instances)

exc, tb = loads(res_info)

# ==================================================
# Occurrences: Lines 550-550 (3 instances)

res, worker_id = loads(res_info)

# ==================================================
# File: /root/ecooptimizer/dask/dask/_expr.py
# Line: 740

expr_name = name(expr)

# ==================================================
# Line: 758

expr_name = name(expr)

# ==================================================
# File: /root/ecooptimizer/dask/dask/blockwise.py
# Line: 775

k = clone_key(k, seed)  # type: ignore

# ==================================================
# Line: 786

k = clone_key(k, seed)

# ==================================================
# Occurrences: Lines 1102-1105 (2 instances)

out = _optimize_blockwise(graph, keys=keys)

# ==================================================
# Occurrences: Lines 1342-1342 (3 instances)

for i in range(i + 1, len(indices) + 1)

# ==================================================
# Occurrences: Lines 1374-1375 (8 instances)

index_map[id_key] = len(indices)

# ==================================================
# Occurrences: Lines 1396-1397 (4 instances)

seen[x] = len(new_indices)

# ==================================================
# File: /root/ecooptimizer/dask/dask/utils.py
# Line: 909

doc = getattr(original_method, "__doc__", None)

# ==================================================
# Occurrences: Lines 915-920 (2 instances)

doc = getattr(original_method, "__doc__", None)

# ==================================================
# Occurrences: Lines 1895-1896 (2 instances)

if int(result) == result:

# ==================================================
# Line: 1929

size = next(iter_sizes, None)

# ==================================================
# Line: 1935

size = next(iter_sizes, None)

# ==================================================
# File: /root/ecooptimizer/dask/dask/multiprocessing.py
# Occurrences: Lines 116-123 (6 instances)

exc_type, exc_value, exc_traceback = sys.exc_info()

# ==================================================
# File: /root/ecooptimizer/dask/dask/system.py
# Occurrences: Lines 21-23 (4 instances)

quota = int(f.read())

# ==================================================
# File: /root/ecooptimizer/dask/dask/dot.py
# Occurrences: Lines 32-34 (2 instances)

return f"{funcname(func.funcs[0])}(...)"

# ==================================================
# File: /root/ecooptimizer/dask/dask/highlevelgraph.py
# Line: 157

{k: self.get_dependencies(k, all_hlg_keys) for k in self.keys()},

# ==================================================
# Line: 168

ret_deps[k] = self.get_dependencies(k, all_hlg_keys)

# ==================================================
# Occurrences: Lines 319-324 (2 instances)

info[key] = html.escape(str(val))

# ==================================================
# Line: 926

layer_name = name(layer)

# ==================================================
# Line: 975

layer_name = name(layer)

# ==================================================
# File: /root/ecooptimizer/dask/dask/base.py
# Occurrences: Lines 821-824 (2 instances)

o_stats = order(dsk, return_stats=True)

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/utils.py
# Occurrences: Lines 663-665 (2 instances)

assert max(map(len, dependencies.values())) == n

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/backends.py
# Line: 359

typ = type(idx)

# ==================================================
# Line: 390

start = np.timedelta64(1, "D")

# ==================================================
# Line: 396

start = np.timedelta64(1, "D")

# ==================================================
# Line: 429

raise TypeError(f"Don't know how to handle index of type {typename(type(idx))}")

# ==================================================
# Line: 443

data = pd.array([entry, entry], dtype=dtype)

# ==================================================
# Occurrences: Lines 461-465 (4 instances)

entry = _scalar_from_dtype(dtype.subtype)

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/partitionquantiles.py
# Line: 225

prev_keys = iter(keys)

# ==================================================
# Line: 236

prev_keys = iter(keys)

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_expr.py
# Occurrences: Lines 811-812 (2 instances)

if self.operand("meta") is not no_default:

# ==================================================
# Occurrences: Lines 2388-2392 (2 instances)

if isinstance(parent.operand("columns"), list):

# ==================================================
# Occurrences: Lines 2540-2541 (2 instances)

npartitions = self.operand("npartitions")

# ==================================================
# Occurrences: Lines 3209-3209 (2 instances)

next = stack.pop()

# ==================================================
# Occurrences: Lines 3245-3245 (2 instances)

next = stack.pop()

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_collection.py
# Line: 202

axis = _validate_axis(axis)

# ==================================================
# Line: 209

other = self._create_alignable_frame(other)

# ==================================================
# Occurrences: Lines 248-251 (2 instances)

axis = _validate_axis(axis)

# ==================================================
# Occurrences: Lines 2805-2805 (3 instances)

result = new_collection(expr.Assign(result, *args))

# ==================================================
# Occurrences: Lines 2814-2814 (2 instances)

result = expr.Assign(result, *args)

# ==================================================
# Occurrences: Lines 2835-2835 (2 instances)

result = new_collection(expr.Assign(result, *args))

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_repartition.py
# Occurrences: Lines 65-67 (2 instances)

and self.operand("new_partitions") is not None

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/diagnostics/_analyze.py
# Occurrences: Lines 180-182 (2 instances)

size = frame.memory_usage(deep=True).sum()

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_concat.py
# Line: 162

divs = self._divisions()

# ==================================================
# Line: 217

divs = self._divisions()

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_reductions.py
# Occurrences: Lines 324-327 (2 instances)

if funcname(self.combine) in ("combine", "aggregate"):

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_version.py
# Occurrences: Lines 181-191 (12 instances)

mo = re.search(r'=\s*"(.*)"', line)

# ==================================================
# Occurrences: Lines 241-242 (2 instances)

print("likely tags: %s" % ",".join(sorted(tags)))

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_groupby.py
# Line: 397

spec = _normalize_spec({None: self.arg}, [])

# ==================================================
# Line: 404

spec = _normalize_spec({None: self.arg}, [])

# ==================================================
# Line: 964

map_columns, unmap_columns = get_map_columns(df)

# ==================================================
# Line: 1002

map_columns, unmap_columns = get_map_columns(df)

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/io/io.py
# Occurrences: Lines 268-269 (2 instances)

if self.operand("user_meta") is not no_default:

# ==================================================
# Line: 475

nrows = len(data)

# ==================================================
# Occurrences: Lines 484-491 (3 instances)

chunksize=self.operand("chunksize"),

# ==================================================
# Occurrences: Lines 508-513 (2 instances)

_lengths = self._get_lengths()

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/io/parquet.py
# Occurrences: Lines 759-764 (2 instances)

_lengths = self._get_lengths()

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/groupby.py
# Line: 353

g = _groupby_raise_unaligned(df, by=by, observed=observed, dropna=dropna)

# ==================================================
# Line: 361

g2 = _groupby_raise_unaligned(df, by=by, observed=observed, dropna=dropna)

# ==================================================
# Line: 731

key = funcname(known_np_funcs.get(func, func)), input_column

# ==================================================
# Line: 751

func = funcname(known_np_funcs.get(func, func))

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/io/sql.py
# Line: 145

minmax = pd.read_sql(q, engine)

# ==================================================
# Line: 154

count = pd.read_sql(q, engine)["count_1"][0]

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/io/io.py
# Occurrences: Lines 338-338 (2 instances)

pos = int(offsets[ind])

# ==================================================
# Occurrences: Lines 347-347 (2 instances)

i = int(offsets[ind]) if ind < len(offsets) else len(seq)

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/io/parquet/utils.py
# Occurrences: Lines 433-436 (2 instances)

l = len(basepath)

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/io/parquet/arrow.py
# Occurrences: Lines 410-412 (4 instances)

expr = field.isin(val)

# ==================================================
# Line: 686

full_metadata = pq.read_metadata(fil)

# ==================================================
# Line: 694

tail_metadata = pq.read_metadata(fil)

# ==================================================
# Occurrences: Lines 941-944 (2 instances)

if len(paths) == 1 and fs.isdir(paths[0]):

# ==================================================
# Occurrences: Lines 950-959 (2 instances)

ds = pa_ds.parquet_dataset(
    meta_path,
    filesystem=_wrapped_fs(fs),
    **_processed_dataset_kwargs,
)

# ==================================================
# Occurrences: Lines 971-972 (2 instances)

elif len(paths) > 1:

# ==================================================
# Line: 978

ds = pa_ds.parquet_dataset(
    meta_path,
    filesystem=_wrapped_fs(fs),
    **_processed_dataset_kwargs,
)

# ==================================================
# Line: 1336

for full_path in sorted(ds.files, key=natural_sort_key)

# ==================================================
# Line: 1372

file_frags = sorted(
    (frag for frag in ds.get_fragments(ds_filters)),
    key=lambda x: natural_sort_key(x.path),
)

# ==================================================
# Line: 1383

all_files = sorted(
    (frag for frag in ds.get_fragments(ds_filters)),
    key=lambda x: natural_sort_key(x.path),
)

# ==================================================
# Line: 1393

all_files = sorted(ds.files, key=natural_sort_key)

# ==================================================
# Occurrences: Lines 1480-1482 (3 instances)

file_row_groups = defaultdict(list)

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/io/parquet/core.py
# Line: 318

parts = len(paths)

# ==================================================
# Line: 343

if len(paths) == 1:

# ==================================================
# Occurrences: Lines 558-560 (2 instances)

out_parts, out_statistics = apply_conjunction(parts, statistics, conjunction)

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/io/csv.py
# Occurrences: Lines 468-470 (3 instances)

if isinstance(kwargs.get("skiprows"), int):

# ==================================================
# Line: 476

skiprows = set(kwargs.get("skiprows"))

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/io/orc/arrow.py
# Line: 40

o = orc.ORCFile(f)

# ==================================================
# Line: 61

o = orc.ORCFile(f)

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/io/orc/core.py
# Line: 168

df = df.optimize()

# ==================================================
# Line: 223

dsk.update(df.optimize().__dask_graph__())

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/io/hdf.py
# Line: 138

df = df.optimize()

# ==================================================
# Line: 183

formatted_names = [name_function(i) for i in range(df.npartitions)]

# ==================================================
# Line: 234

"key": key.replace("*", i_name),

# ==================================================
# Occurrences: Lines 253-258 (3 instances)

i_name = name_function(i)

# ==================================================
# Line: 290

dsk.update(df.optimize().__dask_graph__())

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/io/demo.py
# Occurrences: Lines 307-310 (2 instances)

start=start, end=end, freq=kwargs.get("freq"), name="timestamp"

# ==================================================
# Occurrences: Lines 471-474 (2 instances)

start = pd.Timestamp(spec.index_spec.start)

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/methods.py
# Line: 204

typ = type(q)

# ==================================================
# Line: 225

if is_series_like(q) and typ != type(q):

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/multi.py
# Occurrences: Lines 114-121 (8 instances)

lhs.index = left.astype(dtype)

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/core.py
# Occurrences: Lines 168-169 (2 instances)

sums = np.zeros_like(df.values, shape=shape)

# ==================================================
# Line: 184

m = np.zeros_like(df.values, shape=shape)

# ==================================================
# File: /root/ecooptimizer/dask/dask/order.py
# Line: 122

expected_len = len(dsk)

# ==================================================
# Line: 139

requires_data_task = defaultdict(set)

# ==================================================
# Line: 154

prio = len(dsk) - 1 - n_removed_leaves

# ==================================================
# Line: 184

if len(total_dependencies) != len(dsk):

# ==================================================
# Occurrences: Lines 421-423 (3 instances)

leafs_per_degree = defaultdict(set)

# ==================================================
# Occurrences: Lines 458-459 (6 instances)

size = len(leafs_connected[r])

# ==================================================
# Occurrences: Lines 574-574 (2 instances)

next_deps = dependencies[item].difference(result)

# ==================================================
# Occurrences: Lines 586-586 (2 instances)

deps = dependencies[item].difference(result)

# ==================================================
# File: /root/ecooptimizer/dask/dask/bytes/core.py
# Occurrences: Lines 171-175 (3 instances)

sample = f.read(sample)

# ==================================================
# File: /root/ecooptimizer/dask/dask/tokenize.py
# Occurrences: Lines 244-252 (8 instances)

out = cloudpickle.dumps(o, protocol=5, buffer_callback=buffers.append)

# ==================================================
# File: /root/ecooptimizer/dask/dask/_task_spec.py
# Occurrences: Lines 578-581 (2 instances)

key = (type(value).__name__, next(_anom_count))

# ==================================================
# File: /root/ecooptimizer/dask/dask/_version.py
# Occurrences: Lines 181-191 (12 instances)

mo = re.search(r'=\s*"(.*)"', line)

# ==================================================
# Occurrences: Lines 241-242 (2 instances)

print("likely tags: %s" % ",".join(sorted(tags)))

# ==================================================
# File: /root/ecooptimizer/dask/dask/bag/avro.py
# Occurrences: Lines 18-23 (2 instances)

c = fo.read(1)

# ==================================================
# File: /root/ecooptimizer/dask/dask/bag/random.py
# Line: 143

w = math.exp(math.log(rnd.random()) / k)

# ==================================================
# Line: 149

w *= math.exp(math.log(rnd.random()) / k)

# ==================================================
# Line: 177

min_nxt = min(nxt)

# ==================================================
# Line: 186

min_nxt = min(nxt)

# ==================================================
# File: /root/ecooptimizer/dask/dask/bag/core.py
# Line: 2576

random_state = random_state.randint(0, maxuint32)

# ==================================================
# Line: 2591

tuple(random_state.randint(0, maxuint32) for _ in range(624)) + (624,),

# ==================================================
# File: /root/ecooptimizer/dask/dask/config.py
# Occurrences: Lines 429-434 (2 instances)

key = check_deprecations(key)

# ==================================================
# File: /root/ecooptimizer/dask/dask/delayed.py
# Occurrences: Lines 170-171 (2 instances)

expr = collections_to_expr(expr).finalize_compute()

# ==================================================
# Line: 179

expr2 = ProhibitReuse(collections_to_expr(expr).finalize_compute())

# ==================================================
# Occurrences: Lines 188-204 (7 instances)

f"single key. Got {type(expr)} with {keys=}",

# ==================================================
# Line: 217

args, collections = _finalize_args_collections(args, collections)

# ==================================================
# Line: 235

args, collections = _finalize_args_collections(args, collections)

# ==================================================
# Line: 246

args, collections = _finalize_args_collections(args, collections)

# ==================================================
# Line: 262

args, collections = _finalize_args_collections(args, collections)

# ==================================================
# Line: 290

args, collections = _finalize_args_collections(args, collections)

# ==================================================
# Occurrences: Lines 351-357 (4 instances)

if type(expr) is type(iter(list())):

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/routines.py
# Occurrences: Lines 694-696 (2 instances)

f = f.astype(float)

# ==================================================
# Occurrences: Lines 1033-1037 (2 instances)

for i, k in enumerate(flatten(a.__dask_keys__()))

# ==================================================
# Line: 1053

nchunks = len(list(flatten(a.__dask_keys__())))

# ==================================================
# Line: 1363

dc_bins = is_dask_collection(bins)

# ==================================================
# Line: 1392

D = len(sample)

# ==================================================
# Line: 1404

if not isinstance(bins, (Array, Delayed)) and is_dask_collection(bins):

# ==================================================
# Line: 1491

list(flatten(sample[i].__dask_keys__())) for i in _range(len(sample))

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/utils.py
# Occurrences: Lines 96-98 (2 instances)

meta = np.ma.array(np.empty((0,) * ndim, dtype=dtype or x.dtype), mask=True)

# ==================================================
# Line: 288

x = np.array(x, dtype="O")

# ==================================================
# Line: 295

x = np.array(x, dtype="O")

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/einsumfuncs.py
# Line: 122

input_tmp, output_sub = subscripts.split("->")

# ==================================================
# Occurrences: Lines 163-164 (2 instances)

tmp_subscripts = subscripts.replace(",", "")

# ==================================================
# Occurrences: Lines 175-181 (3 instances)

input_subscripts, output_subscript = subscripts.split("->")

# ==================================================
# Line: 236

if len(inputs) > 1 and len(outputs) > 0:

# ==================================================
# Line: 261

f = max(factor ** (len(changeable_dimensions) / len(outputs)), 1)

# ==================================================
# Line: 290

size = len(outputs)

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/slicing.py
# Line: 315

if np.isnan(dim) and ind != slice(None, None, None):

# ==================================================
# Line: 347

empty_slice = slice(None, None, None)

# ==================================================
# Occurrences: Lines 553-557 (2 instances)

left = np.empty(len(sizes) + 1, dtype=int)

# ==================================================
# Line: 610

chunk_tuples = product(*(range(len(c)) for i, c in enumerate(chunks)))

# ==================================================
# Line: 635

chunk_tuples = product(*(range(len(c)) for i, c in enumerate(chunks)))

# ==================================================
# Occurrences: Lines 975-979 (4 instances)

x = slice_with_int_dask_array_on_axis(x, idx, out_axis)

# ==================================================
# Occurrences: Lines 1197-1198 (2 instances)

index2 = np.empty_like(index)

# ==================================================
# Occurrences: Lines 1330-1334 (4 instances)

start, stop, step = index.indices(size)

# ==================================================
# Occurrences: Lines 1352-1352 (2 instances)

start, stop, step = index.indices(size)

# ==================================================
# Occurrences: Lines 1359-1362 (4 instances)

index = slice(start, stop, step)

# ==================================================
# Line: 1586

i = concatenate_array_chunks(i)

# ==================================================
# Line: 1648

return n_preceding_from_1d_bool_index(dim, loc0)

# ==================================================
# Occurrences: Lines 1692-1697 (4 instances)

i = concatenate_array_chunks(i)

# ==================================================
# Line: 1924

n_preceding = n_preceding_from_1d_bool_index(dim, loc0)

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/percentile.py
# Occurrences: Lines 19-20 (2 instances)

n = len(a)

# ==================================================
# Line: 176

dsk2 = {(name2, 0): (_percentiles_from_tdigest, q, sorted(dsk))}

# ==================================================
# Line: 195

sorted(dsk),

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/wrap.py
# Line: 218

f"fill_value must be scalar. Received {type(fill_value).__name__} instead."

# ==================================================
# Line: 224

kwargs["dtype"] = type(fill_value)

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_reductions_generic.py
# Occurrences: Lines 248-248 (2 instances)

func = compose(func, partial(_concatenate2, axes=sorted(axis)))

# ==================================================
# Occurrences: Lines 261-261 (2 instances)

func = compose(func, partial(_concatenate2, axes=sorted(axis)))

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/chunk.py
# Occurrences: Lines 31-31 (2 instances)

axes = range(x.ndim)

# ==================================================
# Occurrences: Lines 37-37 (2 instances)

for each_axis in range(x.ndim):

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_array_expr/_collection.py
# Line: 649

da_ufunc = getattr(ufunc, numpy_ufunc.__name__)

# ==================================================
# Line: 659

da_ufunc = getattr(ufunc, numpy_ufunc.__name__)

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_array_expr/_map_blocks.py
# Line: 316

ndim_out = len(out_ind)

# ==================================================
# Occurrences: Lines 324-330 (3 instances)

if new_axis is None and chunks is not None and len(out_ind) < len(chunks):

# ==================================================
# Occurrences: Lines 341-343 (2 instances)

if len(chunks) != len(out_ind):

# ==================================================
# Line: 354

expected_ndim=len(out_ind),

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_array_expr/_shuffle.py
# Occurrences: Lines 26-28 (2 instances)

if max(map(max, indexer)) >= sum(chunks[axis]):

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_array_expr/_overlap.py
# Line: 729

return map_blocks(func, *args, **kwargs)

# ==================================================
# Line: 757

x = map_blocks(func, *args, **kwargs)

# ==================================================
# Line: 772

ndim_out = max(a.ndim for a in args if isinstance(a, Array))

# ==================================================
# Line: 787

ndim_out = max(a.ndim for a in args if isinstance(a, Array))

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_array_expr/random.py
# Line: 929

bitgen_token = tokenize(bitgens)

# ==================================================
# Line: 935

bitgen_token = tokenize(bitgens)

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_array_expr/_reductions.py
# Occurrences: Lines 235-235 (2 instances)

func = compose(func, partial(_concatenate2, axes=sorted(axis)))

# ==================================================
# Occurrences: Lines 248-248 (2 instances)

func = compose(func, partial(_concatenate2, axes=sorted(axis)))

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_array_expr/_blockwise.py
# Occurrences: Lines 257-259 (2 instances)

if self.operand("dtype") is not None:

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_array_expr/_creation.py
# Line: 466

f"fill_value must be scalar. Received {type(fill_value).__name__} instead."

# ==================================================
# Line: 472

kwargs["dtype"] = type(fill_value)

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_array_expr/_slicing.py
# Occurrences: Lines 66-70 (4 instances)

x = slice_with_int_dask_array_on_axis(x, idx, out_axis, in_axis)

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/linalg.py
# Occurrences: Lines 225-230 (2 instances)

data, len((sum(vchunks_rstacked), n)), dtype=rr.dtype

# ==================================================
# Line: 265

dsk_q_st3 = blockwise(
    np.dot,
    name_q_st3,
    "ij",
    name_q_st1,
    "ij",
    name_q_st2,
    "ij",
    numblocks={name_q_st1: numblocks, name_q_st2: numblocks},
)

# ==================================================
# Line: 377

dsk_q_st3 = blockwise(
    np.dot,
    name_q_st3,
    "ij",
    name_q_st1,
    "ij",
    name_q_st2,
    "ij",
    numblocks={name_q_st1: numblocks, name_q_st2: numblocks},
)

# ==================================================
# Occurrences: Lines 733-742 (6 instances)

q, _ = tsqr(mat_h)

# ==================================================
# Line: 939

k = min(a.shape)

# ==================================================
# Line: 962

k = min(a.shape)

# ==================================================
# Line: 1168

target = _b_init(i, j)

# ==================================================
# Line: 1180

target = _b_init(i, j)

# ==================================================
# Line: 1355

meta_from_array(a),

# ==================================================
# Line: 1386

a_meta = meta_from_array(a)

# ==================================================
# Line: 1503

r = r.squeeze(axis=axis)

# ==================================================
# Line: 1510

r = r.squeeze(axis=axis)

# ==================================================
# Occurrences: Lines 1522-1526 (2 instances)

r = r.squeeze(axis=axis)

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_shuffle.py
# Occurrences: Lines 175-177 (2 instances)

if max(map(max, indexer)) >= sum(chunks[axis]):

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/creation.py
# Occurrences: Lines 661-664 (2 instances)

for i, row in enumerate(v.__dask_keys__())

# ==================================================
# Line: 671

blocks = v.__dask_keys__()

# ==================================================
# Line: 681

graph = HighLevelGraph.from_collections(name, dsk, dependencies=[v])

# ==================================================
# Line: 756

meta = meta_from_array(a, ndims_free + 1)

# ==================================================
# Line: 821

meta = meta_from_array(a, ndims_free + 1)

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/reshape.py
# Occurrences: Lines 329-334 (3 instances)

if len(known_sizes) < len(shape):

# ==================================================
# Line: 344

meta = meta_from_array(x, len(shape))

# ==================================================
# Line: 350

new_key = (name,) + (0,) * len(shape)

# ==================================================
# Line: 358

dout = len(shape)

# ==================================================
# Line: 519

graph = HighLevelGraph.from_collections(outname, dsk, dependencies=[x])  # type: ignore[arg-type]

# ==================================================
# Line: 568

graph = HighLevelGraph.from_collections(outname, dsk, dependencies=[x])  # type: ignore[arg-type]

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/random.py
# Line: 948

res = _broadcast_any(ar, size, chunks)

# ==================================================
# Line: 963

res = _broadcast_any(ar, size, chunks)

# ==================================================
# Line: 978

bitgen_token = tokenize(bitgens)

# ==================================================
# Line: 984

bitgen_token = tokenize(bitgens)

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/overlap.py
# Line: 713

return map_blocks(func, *args, **kwargs)

# ==================================================
# Line: 741

x = map_blocks(func, *args, **kwargs)

# ==================================================
# Line: 756

ndim_out = max(a.ndim for a in args if isinstance(a, Array))

# ==================================================
# Line: 771

ndim_out = max(a.ndim for a in args if isinstance(a, Array))

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/rechunk.py
# Line: 451

if len(desired_chunks) <= max_number:

# ==================================================
# Line: 458

n = len(desired_chunks)

# ==================================================
# Occurrences: Lines 468-472 (2 instances)

nmerges = len(desired_chunks) - max_number

# ==================================================
# Occurrences: Lines 509-510 (2 instances)

old_largest_width = [max(c) for c in old_chunks]

# ==================================================
# Line: 565

largest_block_size = largest_block_size * max(c) // largest_width

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/gufunc.py
# Occurrences: Lines 463-464 (6 instances)

factor *= a.shape[i] / max(a.chunks[i])

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/core.py
# Line: 855

ndim_out = len(out_ind)

# ==================================================
# Occurrences: Lines 863-869 (3 instances)

if new_axis is None and chunks is not None and len(out_ind) < len(chunks):

# ==================================================
# Occurrences: Lines 880-882 (2 instances)

if len(chunks) != len(out_ind):

# ==================================================
# Line: 893

expected_ndim=len(out_ind),

# ==================================================
# Occurrences: Lines 1041-1042 (2 instances)

if getattr(out, "ndim", 0) != expected_ndim:

# ==================================================
# Line: 1600

da_ufunc = getattr(ufunc, numpy_ufunc.__name__)

# ==================================================
# Line: 1610

da_ufunc = getattr(ufunc, numpy_ufunc.__name__)

# ==================================================
# Line: 3342

multiplier = _compute_multiplier(limit, dtype, largest_block, median_chunks)

# ==================================================
# Line: 3406

multiplier = _compute_multiplier(
    limit, dtype, largest_block, median_chunks
)

# ==================================================
# Occurrences: Lines 3440-3445 (2 instances)

if math.ceil(m) / m > this_chunksize_tolerance:

# ==================================================
# Occurrences: Lines 4371-4373 (4 instances)

curr_depth = len(index)

# ==================================================
# Line: 5097

result = result.astype(dtype)

# ==================================================
# Line: 5103

result = result.astype(dtype)

# ==================================================
# Line: 5464

x = unpack_singleton(arrays)

# ==================================================
# Line: 5470

x = unpack_singleton(arrays)

# ==================================================
# Occurrences: Lines 5761-5762 (4 instances)

merge_inputs = defaultdict(list)

# ==================================================
# Occurrences: Lines 5770-5770 (3 instances)

k = keyname(name, i, okey)

# ==================================================
# Occurrences: Lines 5778-5778 (3 instances)

merge_inputs[outblock].append(TaskRef(keyname(name, i, okey)))

# ==================================================
# File: /root/ecooptimizer/dask/dask/optimization.py
# Occurrences: Lines 196-199 (4 instances)

child = chain.pop()

# ==================================================
# Occurrences: Lines 429-442 (6 instances)

first_name = utils.key_split(first_key)

# ==================================================
# Occurrences: Lines 668-668 (3 instances)

num_children_edges = len(children_edges)

# ==================================================
# Occurrences: Lines 735-736 (6 instances)

if fudge > int(ave_width - 1):

# ==================================================
# Occurrences: Lines 780-784 (11 instances)

if len(cur_edges) > max_num_edges:

# ==================================================
# Occurrences: Lines 858-859 (6 instances)

if fudge > int(ave_width - 1):

# ==================================================
