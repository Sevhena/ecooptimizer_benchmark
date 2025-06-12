# long-message-chain snippets for pandas

# File: /root/ecooptimizer/pandas/pandas/io/sql.py
# Line: 2475

uname = str(name).encode("utf-8", "strict").decode("utf-8")

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/html.py
# Line: 586

not in getattr(x, attr_name).get("style", "").replace(" ", "")

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/parsers/python_parser.py
# Line: 505

cats = Index(values).unique().dropna()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/pytables.py
# Line: 5281

Series(data.ravel(), copy=False, dtype="object")
.str.encode(encoding, errors)
._values.reshape(data.shape)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/stata.py
# Occurrences: Lines 391-393 (2 instances)

year_start = np.asarray(dates).astype("M8[Y]").astype(dates.dtype)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/info.py
# Line: 1106

return df.dtypes.value_counts().groupby(lambda x: x.name).sum()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/string.py
# Line: 158

max_len = Series(lines).str.len().max()

# ==================================================
# Line: 164

col_lens = Series([Series(ele).str.len().max() for ele in strcols])

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/style_render.py
# Line: 1939

formatter(x)
.replace(",", "§_§-")  # rare string to avoid "," <-> "." clash.
.replace(".", decimal)
.replace("§_§-", thousands)

# ==================================================
# Line: 2481

return str(value).replace(arg, "").replace("/*", "").replace("*/", "").strip()

# ==================================================
# Line: 2578

s.replace("\\", "ab2§=§8yz")  # rare string for final conversion: avoid \\ clash
.replace("ab2§=§8yz ", "ab2§=§8yz\\space ")  # since \backslash gobbles spaces
.replace("&", "\\&")
.replace("%", "\\%")
.replace("$", "\\$")
.replace("#", "\\#")
.replace("_", "\\_")
.replace("{", "\\{")
.replace("}", "\\}")
.replace("~ ", "~\\space ")  # since \textasciitilde gobbles spaces
.replace("~", "\\textasciitilde ")
.replace("^ ", "^\\space ")  # since \textasciicircum gobbles spaces
.replace("^", "\\textasciicircum ")
.replace("ab2§=§8yz", "\\textbackslash ")

# ==================================================
# Occurrences: Lines 2653-2659 (2 instances)

_escape_latex(item).replace("LEFT", r"\(").replace("RIGHT", r"\)")

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/io/formats/format.py
# Line: 1591

out[int_idx] = percentiles[int_idx].round().astype(int).astype(str)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/generic.py
# Line: 9362

np.arange(diff.shape[axis])
.reshape([2, diff.shape[axis] // 2])
.T.reshape(-1)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/interchange/from_dataframe.py
# Line: 385

data = pd.Series(data).dt.tz_localize("UTC").dt.tz_convert(tz)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/interchange/column.py
# Line: 235

return self._col.isna().sum().item()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/window/doc.py
# Line: 153

    dedent(
        """
engine : str, default None
    * ``'cython'`` : Runs the operation through C-extensions from cython.
    * ``'numba'`` : Runs the operation through JIT compiled code from numba.
    * ``None`` : Defaults to ``'cython'`` or globally setting ``compute.use_numba``

      .. versionadded:: {version}.0

engine_kwargs : dict, default None
    * For ``'cython'`` engine, there are no accepted ``engine_kwargs``
    * For ``'numba'`` engine, the engine can accept ``nopython``, ``nogil``
      and ``parallel`` dictionary keys. The values must either be ``True`` or
      ``False``. The default ``engine_kwargs`` for the ``'numba'`` engine is
      ``{{'nopython': True, 'nogil': False, 'parallel': False}}``

      .. versionadded:: {version}.0\n
"""
    )
    .replace("\n", "", 1)
    .replace("{version}", version)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/strings/accessor.py
# Line: 345

pa.compute.list_flatten(result._pa_array)
.to_numpy()
.reshape(len(result), max_len)

# ==================================================
# Line: 3968

arr = arr.to_series().reset_index(drop=True).astype(arr.dtype)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/datetimelike.py
# Line: 727

return super()._union(other, sort)._with_freq("infer")

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/accessors.py
# Line: 234

cast(ArrowExtensionArray, self._parent.array)
._dt_isocalendar()
._pa_array.combine_chunks()

# ==================================================
# Line: 428

return self._get_values().isocalendar().set_index(self._parent.index)

# ==================================================
# Line: 547

self._get_values()
.components.set_index(self._parent.index)
.__finalize__(self._parent)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/base.py
# Line: 734

Series(np.arange(len(self)), copy=False)
.groupby(self, observed=False)
.agg(list)[duplicates]

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/indexes/multi.py
# Line: 2416

level_codes.view(np.ndarray).astype(np.intp, copy=False).repeat(repeats)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/series.py
# Line: 2018

return notna(self._values).sum().astype("int64")

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/tile.py
# Line: 372

bins = x_idx.to_series().dropna().quantile(quantiles)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/merge.py
# Occurrences: Lines 2788-2799 (3 instances)

pa.chunked_array(lk.chunks + rk.chunks)  # type: ignore[union-attr]
.combine_chunks()
.dictionary_encode()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/reshape.py
# Line: 282

sorted_values.reshape(length, width, stride)
.swapaxes(1, 2)
.reshape(result_shape)

# ==================================================
# Line: 843

idx = np.arange(N * K).reshape(K, N).T.reshape(-1)

# ==================================================
# Line: 925

idx = np.arange(n_rows * n_columns).reshape(n_columns, n_rows).T.reshape(-1)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/arrow/array.py
# Line: 2527

lengths = pc.list_value_length(split).fill_null(0).to_numpy()

# ==================================================
# Line: 2970

indices = np.arange(nrows * ncols).reshape(ncols, nrows).T.reshape(-1)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/categorical.py
# Line: 1428

removals = Index(removals).unique().dropna()

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/arrays/period.py
# Line: 954

return self.to_timestamp().tz_localize(tz).as_unit(unit)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/frame.py
# Line: 5900

super()
.shift(periods=period, freq=freq, axis=axis, fill_value=fill_value)
.add_suffix(f"{suffix}_{period}" if suffix else f"_{period}")

# ==================================================
# Line: 11847

mask = df.isna().to_numpy(dtype=np.bool_).any(axis=1)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/algorithms.py
# Line: 902

Series(index=values, name=name)
.groupby(level=levels, dropna=dropna)
.size()

# ==================================================
