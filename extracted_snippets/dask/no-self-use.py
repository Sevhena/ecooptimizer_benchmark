# no-self-use snippets for dask

# File: /root/ecooptimizer/dask/dask/_expr.py
# Occurrences: Lines 75-78 (2 instances)

def _tune_down(self):
    return None


# ==================================================
# Occurrences: Lines 459-462 (2 instances)

def _simplify_down(self):
    return


# ==================================================
# Line: 526

def _lower(self):
    return


# ==================================================
# Line: 553

def __dask_annotations__(self):
    return {}


# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_quantiles.py
# Line: 35

def __dask_postcompute__(self):
    return toolz.first, ()


# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_collection.py
# Line: 2057

def _create_alignable_frame(self, other, join="outer"):
    if not is_dask_collection(other) and (
        is_series_like(other) or is_dataframe_like(other)
    ):
        if join in ("inner", "left"):
            npartitions = 1
        else:
            # We have to trigger alignment, otherwise pandas will add
            # the same values to every partition
            npartitions = 2
        other = from_pandas(other, npartitions=npartitions)
    return other


# ==================================================
# Line: 2744

def __array_ufunc__(self, numpy_ufunc, method, *inputs, **kwargs):
    out = kwargs.get("out", ())
    for x in inputs + out:
        # ufuncs work with 0-dimensional NumPy ndarrays
        # so we don't want to raise NotImplemented
        if isinstance(x, np.ndarray) and x.shape == ():
            continue
        elif not isinstance(
            x, (Number, Scalar, FrameBase, Array, pd.DataFrame, pd.Series, pd.Index)
        ):
            return NotImplemented

    if method == "__call__":
        if numpy_ufunc.signature is not None:
            return NotImplemented
        if numpy_ufunc.nout > 1:
            # ufuncs with multiple output values
            # are not yet supported for frames
            return NotImplemented
        else:
            return elemwise(numpy_ufunc, *inputs, **kwargs)
    else:
        # ufunc methods are not yet supported for frames
        return NotImplemented


# ==================================================
# Line: 4153

def __array_ufunc__(self, numpy_ufunc, method, *inputs, **kwargs):
    out = kwargs.get("out", ())
    for x in inputs + out:
        # ufuncs work with 0-dimensional NumPy ndarrays
        # so we don't want to raise NotImplemented
        if isinstance(x, np.ndarray) and x.shape == ():
            continue
        elif not isinstance(
            x, (Number, Scalar, FrameBase, Array, pd.DataFrame, pd.Series, pd.Index)
        ):
            return NotImplemented

    if method == "__call__":
        if numpy_ufunc.signature is not None:
            return NotImplemented
        if numpy_ufunc.nout > 1:
            # ufuncs with multiple output values
            # are not yet supported for frames
            return NotImplemented
        else:
            return elemwise(numpy_ufunc, *inputs, **kwargs)
    else:
        # ufunc methods are not yet supported for frames
        return NotImplemented


# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_merge.py
# Line: 276

def _on_condition_alread_partitioned(self, expr, on):
    if not isinstance(on, list):
        result = (
            on in expr.unique_partition_mapping_columns_from_shuffle
            or (on,) in expr.unique_partition_mapping_columns_from_shuffle
        )
    else:
        result = tuple(on) in expr.unique_partition_mapping_columns_from_shuffle
    return result


# ==================================================
# Line: 892

def _broadcast_dep(self, dep: Expr):
    return dep.npartitions == 1


# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_reductions.py
# Line: 330

def __dask_postcompute__(self):
    return toolz.first, ()


# ==================================================
# Line: 376

def _divisions(self):
    return (None, None)


# ==================================================
# Line: 821

def __dask_postcompute__(self):
    return toolz.first, ()


# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_groupby.py
# Line: 1574

def _numeric_only_kwargs(self, numeric_only):
    kwargs = {"numeric_only": numeric_only}
    return {"chunk_kwargs": kwargs.copy(), "aggregate_kwargs": kwargs.copy()}


# ==================================================
# Line: 1965

def _warn_if_no_meta(self, meta, method="apply"):
    if meta is no_default:
        msg = f"""`meta` is not specified, inferred from partial data.

# ==================================================
# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/io/parquet.py
# Line: 271

def _divisions(self):
    return (None, None)


# ==================================================
# Line: 313

def _divisions(self):
    return (None, None)


# ==================================================
# File: /root/ecooptimizer/dask/dask/bag/core.py
# Line: 396

def __dask_postcompute__(self):
    return finalize_item, ()


# ==================================================
# Line: 506

def __dask_postcompute__(self):
    return finalize, ()


# ==================================================
# File: /root/ecooptimizer/dask/dask/delayed.py
# Line: 716

def __dask_postcompute__(self):
    return single_key, ()


# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_array_expr/_collection.py
# Line: 52

def __dask_postcompute__(self):
    return finalize, ()


# ==================================================
# File: /root/ecooptimizer/dask/dask/array/core.py
# Line: 1435

def __dask_postcompute__(self):
    return finalize, ()


# ==================================================
# Line: 1558

def chunks(self, chunks):
    raise TypeError(
        "Can not set chunks directly\n\n"
        "Please use the rechunk method instead:\n"
        f"  x.rechunk({chunks})\n\n"
        "If trying to avoid unknown chunks, use\n"
        "  x.compute_chunk_sizes()"
    )


# ==================================================
# Line: 1696

def name(self, val):
    raise TypeError(
        "Cannot set name directly\n\n"
        "Name is used to relate the array to the task graph.\n"
        "It is uncommon to need to change it, but if you do\n"
        "please set ``._name``"
    )


# ==================================================
