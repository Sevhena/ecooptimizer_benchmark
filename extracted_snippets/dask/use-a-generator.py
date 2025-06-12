# use-a-generator snippets for dask

# File: /root/ecooptimizer/dask/dask/dataframe/dask_expr/_collection.py
# Line: 3454

if any([isinstance(c, FrameBase) for c in other]):

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/routines.py
# Occurrences: Lines 1365-1367 (2 instances)

dc_bins = dc_bins or any([is_dask_collection(b) for b in bins])

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/_array_expr/_overlap.py
# Line: 460

original_chunks_too_small = any([min(c) < d for d, c in zip(depths, x.chunks)])

# ==================================================
# Line: 728

if all([all(depth_val == 0 for depth_val in d.values()) for d in depth]):

# ==================================================
# File: /root/ecooptimizer/dask/dask/array/overlap.py
# Line: 446

original_chunks_too_small = any([min(c) < d for d, c in zip(depths, x.chunks)])

# ==================================================
# Line: 712

if all([all(depth_val == 0 for depth_val in d.values()) for d in depth]):

# ==================================================
