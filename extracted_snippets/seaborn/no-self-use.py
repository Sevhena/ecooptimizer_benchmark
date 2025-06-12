# no-self-use snippets for seaborn

# File: /root/ecooptimizer/seaborn/seaborn/_base.py
# Line: 52

def _check_list_length(self, levels, values, variable):
    """Input check when values are provided as a list."""
    # Copied from _core/properties; eventually will be replaced for that.
    message = ""
    if len(levels) > len(values):
        message = " ".join([
            f"\nThe {variable} list has fewer values ({len(values)})",
            f"than needed ({len(levels)}) and will cycle, which may",
            "produce an uninterpretable plot."
        ])
        values = [x for _, x in zip(levels, itertools.cycle(values))]

    elif len(values) > len(levels):
        message = " ".join([
            f"The {variable} list has more values ({len(values)})",
            f"than needed ({len(levels)}), which may not be intended.",
        ])
        values = values[:len(levels)]

    if message:
        warnings.warn(message, UserWarning, stacklevel=6)

    return values


# ==================================================
# Line: 205

def infer_map_type(self, palette, norm, input_format, var_type):
    """Determine how to implement the mapping."""
    if palette in QUAL_PALETTES:
        map_type = "categorical"
    elif norm is not None:
        map_type = "numeric"
    elif isinstance(palette, (dict, list)):
        map_type = "categorical"
    elif input_format == "wide":
        map_type = "categorical"
    else:
        map_type = var_type

    return map_type


# ==================================================
# Line: 254

def numeric_mapping(self, data, palette, norm):
    """Determine colors when the hue variable is quantitative."""
    if isinstance(palette, dict):

        # The presence of a norm object overrides a dictionary of hues
        # in specifying a numeric mapping, so we need to process it here.
        levels = list(sorted(palette))
        colors = [palette[k] for k in sorted(palette)]
        cmap = mpl.colors.ListedColormap(colors)
        lookup_table = palette.copy()

    else:

        # The levels are the sorted unique values in the data
        levels = list(np.sort(remove_na(data.unique())))

        # --- Sort out the colormap to use from the palette argument

        # Default numeric palette is our default cubehelix palette
        # TODO do we want to do something complicated to ensure contrast?
        palette = "ch:" if palette is None else palette

        if isinstance(palette, mpl.colors.Colormap):
            cmap = palette
        else:
            cmap = color_palette(palette, as_cmap=True)

        # Now sort out the data normalization
        if norm is None:
            norm = mpl.colors.Normalize()
        elif isinstance(norm, tuple):
            norm = mpl.colors.Normalize(*norm)
        elif not isinstance(norm, mpl.colors.Normalize):
            err = "``hue_norm`` must be None, tuple, or Normalize object."
            raise ValueError(err)

        if not norm.scaled():
            norm(np.asarray(data.dropna()))

        lookup_table = dict(zip(levels, cmap(norm(levels))))

    return levels, lookup_table, norm, cmap



# ==================================================
# Line: 359

def infer_map_type(self, norm, sizes, var_type):

    if norm is not None:
        map_type = "numeric"
    elif isinstance(sizes, (dict, list)):
        map_type = "categorical"
    else:
        map_type = var_type

    return map_type


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/regression.py
# Line: 347

def regress_out(self, a, b):
    """Regress b from a keeping a's original mean."""
    a_mean = a.mean()
    a = a - a_mean
    b = b - b.mean()
    b = np.c_[b]
    a_prime = a - b.dot(np.linalg.pinv(b).dot(a))
    return np.asarray(a_prime + a_mean).reshape(a.shape)


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/utils.py
# Line: 681

def get_view_interval(self):
    return limits


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_marks/line.py
# Line: 102

def _handle_capstyle(self, kws, vals):

    # Work around for this matplotlib issue:
    # https://github.com/matplotlib/matplotlib/issues/23437
    if vals["linestyle"][1] is None:
        capstyle = kws.get("solid_capstyle", mpl.rcParams["lines.solid_capstyle"])
        kws["dash_capstyle"] = capstyle



# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_marks/area.py
# Line: 53

def _standardize_coordinate_parameters(self, data, orient):
    return data


# ==================================================
# Line: 59

def _get_verts(self, data, orient):

    dv = {"x": "y", "y": "x"}[orient]
    data = data.sort_values(orient, kind="mergesort")
    verts = np.concatenate([
        data[[orient, f"{dv}min"]].to_numpy(),
        data[[orient, f"{dv}max"]].to_numpy()[::-1],
    ])
    if orient == "y":
        verts = verts[:, ::-1]
    return verts


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_marks/dot.py
# Line: 29

def _resolve_paths(self, data):

    paths = []
    path_cache = {}
    marker = data["marker"]

    def get_transformed_path(m):
        return m.get_path().transformed(m.get_transform())

    if isinstance(marker, mpl.markers.MarkerStyle):
        return get_transformed_path(marker)

    for m in marker:
        if m not in path_cache:
            path_cache[m] = get_transformed_path(m)
        paths.append(path_cache[m])
    return paths


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_marks/base.py
# Line: 200

def _infer_orient(self, scales: dict) -> str:  # TODO type scales

    # TODO The original version of this (in seaborn._base) did more checking.
    # Paring that down here for the prototype to see what restrictions make sense.

    # TODO rethink this to map from scale type to "DV priority" and use that?
    # e.g. Nominal > Discrete > Continuous

    x = 0 if "x" not in scales else scales["x"]._priority
    y = 0 if "y" not in scales else scales["y"]._priority

    if y > x:
        return "y"
    else:
        return "x"


# ==================================================
# Line: 225

def _legend_artist(
    self, variables: list[str], value: Any, scales: dict[str, Scale],

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/external/docscrape.py
# Line: 206

def _strip(self, doc):
    i = 0
    j = 0
    for i, line in enumerate(doc):
        if line.strip():
            break

    for j, line in enumerate(doc[::-1]):
        if line.strip():
            break

    return doc[i:len(doc)-j]


# ==================================================
# Line: 242

def _parse_param_list(self, content, single_element_is_type=False):
    r = Reader(content)
    params = []
    while not r.eof():
        header = r.read().strip()
        if ' : ' in header:
            arg_name, arg_type = header.split(' : ')[:2]
        else:
            if single_element_is_type:
                arg_name, arg_type = '', header
            else:
                arg_name, arg_type = header, ''

        desc = r.read_to_next_unindented_line()
        desc = dedent_lines(desc)
        desc = strip_blank_lines(desc)

        params.append(Parameter(arg_name, arg_type, desc))

    return params


# ==================================================
# Line: 352

def _parse_index(self, section, content):
    """
    .. index: default
       :refguide: something, else, and more

    """
    def strip_each_in(lst):
        return [s.strip() for s in lst]

    out = {}
    section = section.split('::')
    if len(section) > 1:
        out['default'] = strip_each_in(section[1].split(','))[0]
    for line in content:
        line = line.split(':')
        if len(line) > 2:
            out[line[1]] = strip_each_in(line[2].split(','))
    return out


# ==================================================
# Occurrences: Lines 445-448 (2 instances)

def _str_header(self, name, symbol='-'):
    return [name, len(name)*symbol]


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_stats/aggregation.py
# Line: 94

def _process(
    self, data: DataFrame, var: str, estimator: EstimateAggregator

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_stats/counting.py
# Line: 123

def _define_bin_edges(self, vals, weight, bins, binwidth, binrange, discrete):
    """Inner function that takes bin parameters as arguments."""
    vals = vals.replace(-np.inf, np.nan).replace(np.inf, np.nan).dropna()

    if binrange is None:
        start, stop = vals.min(), vals.max()
    else:
        start, stop = binrange

    if discrete:
        bin_edges = np.arange(start - .5, stop + 1.5)
    else:
        if binwidth is not None:
            bins = int(round((stop - start) / binwidth))
        bin_edges = np.histogram_bin_edges(vals, bins, binrange, weight)

    # TODO warning or cap on too many bins?

    return bin_edges


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/categorical.py
# Line: 207

def _point_kwargs_backcompat(self, scale, join, kwargs):
    """Provide two cycles where scale= and join= work, but redirect to kwargs."""
    if scale is not deprecated:
        lw = mpl.rcParams["lines.linewidth"] * 1.8 * scale
        mew = lw * .75
        ms = lw * 2

        msg = (
            "\n\n"
            "The `scale` parameter is deprecated and will be removed in v0.15.0. "
            "You can now control the size of each plot element using matplotlib "
            "`Line2D` parameters (e.g., `linewidth`, `markersize`, etc.)."
            "\n"
        )
        warnings.warn(msg, stacklevel=3)
        kwargs.update(linewidth=lw, markeredgewidth=mew, markersize=ms)

    if join is not deprecated:
        msg = (
            "\n\n"
            "The `join` parameter is deprecated and will be removed in v0.15.0."
        )
        if not join:
            msg += (
                " You can remove the line between points with `linestyle='none'`."
            )
            kwargs.update(linestyle="")
        msg += "\n"
        warnings.warn(msg, stacklevel=3)


# ==================================================
# Line: 237

def _err_kws_backcompat(self, err_kws, errcolor, errwidth, capsize):
    """Provide two cycles where existing signature-level err_kws are handled."""
    def deprecate_err_param(name, key, val):
        if val is deprecated:
            return
        suggest = f"err_kws={{'{key}': {val!r}}}"
        msg = (
            f"\n\nThe `{name}` parameter is deprecated. And will be removed "
            f"in v0.15.0. Pass `{suggest}` instead.\n"
        )
        warnings.warn(msg, FutureWarning, stacklevel=4)
        err_kws[key] = val

    if errcolor is not None:
        deprecate_err_param("errcolor", "color", errcolor)
    deprecate_err_param("errwidth", "linewidth", errwidth)

    if capsize is None:
        capsize = 0
        msg = (
            "\n\nPassing `capsize=None` is deprecated and will be removed "
            "in v0.15.0. Pass `capsize=0` to disable caps.\n"
        )
        warnings.warn(msg, FutureWarning, stacklevel=3)

    return err_kws, capsize


# ==================================================
# Line: 264

def _violin_scale_backcompat(self, scale, scale_hue, density_norm, common_norm):
    """Provide two cycles of backcompat for scale kwargs"""
    if scale is not deprecated:
        density_norm = scale
        msg = (
            "\n\nThe `scale` parameter has been renamed and will be removed "
            f"in v0.15.0. Pass `density_norm={scale!r}` for the same effect."
        )
        warnings.warn(msg, FutureWarning, stacklevel=3)

    if scale_hue is not deprecated:
        common_norm = scale_hue
        msg = (
            "\n\nThe `scale_hue` parameter has been replaced and will be removed "
            f"in v0.15.0. Pass `common_norm={not scale_hue}` for the same effect."
        )
        warnings.warn(msg, FutureWarning, stacklevel=3)

    return density_norm, common_norm


# ==================================================
# Line: 284

def _violin_bw_backcompat(self, bw, bw_method):
    """Provide two cycles of backcompat for violin bandwidth parameterization."""
    if bw is not deprecated:
        bw_method = bw
        msg = dedent(f"""\n
            The `bw` parameter is deprecated in favor of `bw_method`/`bw_adjust`.
            Setting `bw_method={bw!r}`, but please see docs for the new parameters
            and update your code. This will become an error in seaborn v0.15.0.
        """)
        warnings.warn(msg, FutureWarning, stacklevel=3)
    return bw_method


# ==================================================
# Line: 296

def _boxen_scale_backcompat(self, scale, width_method):
    """Provide two cycles of backcompat for scale kwargs"""
    if scale is not deprecated:
        width_method = scale
        msg = (
            "\n\nThe `scale` parameter has been renamed to `width_method` and "
            f"will be removed in v0.15. Pass `width_method={scale!r}"
        )
        if scale == "area":
            msg += ", but note that the result for 'area' will appear different."
        else:
            msg += " for the same effect."
        warnings.warn(msg, FutureWarning, stacklevel=3)

    return width_method


# ==================================================
# Line: 312

def _complement_color(self, color, base_color, hue_map):
    """Allow a color to be set automatically using a basis of comparison."""
    if color == "gray":
        msg = (
            'Use "auto" to set automatic grayscale colors. From v0.14.0, '
            '"gray" will default to matplotlib\'s definition.'
        )
        warnings.warn(msg, FutureWarning, stacklevel=3)
        color = "auto"
    elif color is None or color is default:
        color = "auto"

    if color != "auto":
        return color

    if hue_map.lookup_table is None:
        if base_color is None:
            return None
        basis = [mpl.colors.to_rgb(base_color)]
    else:
        basis = [mpl.colors.to_rgb(c) for c in hue_map.lookup_table.values()]
    unique_colors = np.unique(basis, axis=0)
    light_vals = [rgb_to_hls(*rgb[:3])[1] for rgb in unique_colors]
    lum = min(light_vals) * .6
    return (lum, lum, lum)


# ==================================================
# Line: 3332

def could_overlap(self, xyr_i, swarm):
    """Return a list of all swarm points that could overlap with target."""
    # Because we work backwards through the swarm and can short-circuit,
    # the for-loop is faster than vectorization
    _, y_i, r_i = xyr_i
    neighbors = []
    for xyr_j in reversed(swarm):
        _, y_j, r_j = xyr_j
        if (y_i - y_j) < (r_i + r_j):
            neighbors.append(xyr_j)
        else:
            break
    return np.array(neighbors)[::-1]


# ==================================================
# Line: 3346

def position_candidates(self, xyr_i, neighbors):
    """Return a list of coordinates that might be valid by adjusting x."""
    candidates = [xyr_i]
    x_i, y_i, r_i = xyr_i
    left_first = True
    for x_j, y_j, r_j in neighbors:
        dy = y_i - y_j
        dx = np.sqrt(max((r_i + r_j) ** 2 - dy ** 2, 0)) * 1.05
        cl, cr = (x_j - dx, y_i, r_i), (x_j + dx, y_i, r_i)
        if left_first:
            new_candidates = [cl, cr]
        else:
            new_candidates = [cr, cl]
        candidates.extend(new_candidates)
        left_first = not left_first
    return np.array(candidates)


# ==================================================
# Line: 3363

def first_non_overlapping_candidate(self, candidates, neighbors):
    """Find the first candidate that does not overlap with the swarm."""

    # If we have no neighbors, all candidates are good.
    if len(neighbors) == 0:
        return candidates[0]

    neighbors_x = neighbors[:, 0]
    neighbors_y = neighbors[:, 1]
    neighbors_r = neighbors[:, 2]

    for xyr_i in candidates:

        x_i, y_i, r_i = xyr_i

        dx = neighbors_x - x_i
        dy = neighbors_y - y_i
        sq_distances = np.square(dx) + np.square(dy)

        sep_needed = np.square(neighbors_r + r_i)

        # Good candidate does not overlap any of neighbors which means that
        # squared distance between candidate and any of the neighbors has
        # to be at least square of the summed radii
        good_candidate = np.all(sq_distances >= sep_needed)

        if good_candidate:
            return xyr_i

    raise RuntimeError(
        "No non-overlapping candidates found. This should not happen."
    )


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/plot.py
# Line: 188

def _html_table(self, params: dict[str, Any]) -> list[str]:

    lines = ["<table>"]
    for k, v in params.items():
        row = f"<tr><td>{k}:</td><td style='text-align:left'>{v!r}</td></tr>"
        lines.append(row)
    lines.append("</table>")
    return lines


# ==================================================
# Line: 339

def _resolve_positionals(
    self,
    args: tuple[DataSource | VariableSpec, ...],
    data: DataSource,
    variables: dict[str, VariableSpec],

# ==================================================
# Line: 1071

def _extract_data(self, p: Plot) -> tuple[PlotData, list[Layer]]:

    common_data = (
        p._data
        .join(None, p._facet_spec.get("variables"))
        .join(None, p._pair_spec.get("variables"))
    )

    layers: list[Layer] = []
    for layer in p._layers:
        spec = layer.copy()
        spec["data"] = common_data.join(layer.get("source"), layer.get("vars"))
        layers.append(spec)

    return common_data, layers


# ==================================================
# Line: 1087

def _resolve_label(self, p: Plot, var: str, auto_label: str | None) -> str:

    if re.match(r"[xy]\d+", var):
        key = var if var in p._labels else var[0]
    else:
        key = var

    label: str
    if key in p._labels:
        manual_label = p._labels[key]
        if callable(manual_label) and auto_label is not None:
            label = manual_label(auto_label)
        else:
            label = cast(str, manual_label)
    elif auto_label is None:
        label = ""
    else:
        label = auto_label
    return label


# ==================================================
# Line: 1263

def _get_scale(
    self, p: Plot, var: str, prop: Property, values: Series

# ==================================================
# Line: 1564

def _get_subplot_index(self, df: DataFrame, subplot: dict) -> Index:

    dims = df.columns.intersection(["col", "row"])
    if dims.empty:
        return df.index

    keep_rows = pd.Series(True, df.index, dtype=bool)
    for dim in dims:
        keep_rows &= df[dim] == subplot[dim]
    return df.index[keep_rows]


# ==================================================
# Line: 1575

def _filter_subplot_data(self, df: DataFrame, subplot: dict) -> DataFrame:
    # TODO note redundancies with preceding function ... needs refactoring
    dims = df.columns.intersection(["col", "row"])
    if dims.empty:
        return df

    keep_rows = pd.Series(True, df.index, dtype=bool)
    for dim in dims:
        keep_rows &= df[dim] == subplot[dim]
    return df[keep_rows]


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/moves.py
# Line: 165

def _stack(self, df, orient):

    # TODO should stack do something with ymin/ymax style marks?
    # Should there be an upstream conversion to baseline/height parameterization?

    if df["baseline"].nunique() > 1:
        err = "Stack move cannot be used when baselines are already heterogeneous"
        raise RuntimeError(err)

    other = {"x": "y", "y": "x"}[orient]
    stacked_lengths = (df[other] - df["baseline"]).dropna().cumsum()
    offsets = stacked_lengths.shift(1).fillna(0)

    df[other] = stacked_lengths
    df["baseline"] = df["baseline"] + offsets

    return df


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/properties.py
# Line: 59

def default_scale(self, data: Series) -> Scale:
    """Given data, initialize appropriate scale class."""

    var_type = variable_type(data, boolean_type="boolean", strict_boolean=True)
    if var_type == "numeric":
        return Continuous()
    elif var_type == "datetime":
        return Temporal()
    elif var_type == "boolean":
        return Boolean()
    else:
        return Nominal()


# ==================================================
# Line: 92

def get_mapping(self, scale: Scale, data: Series) -> Mapping:
    """Return a function that maps from data domain to property range."""
    def identity(x):
        return x
    return identity


# ==================================================
# Line: 98

def standardize(self, val: Any) -> Any:
    """Coerce flexible property value to standardized representation."""
    return val


# ==================================================
# Occurrences: Lines 163-167 (2 instances)

def _forward(self, values: ArrayLike) -> ArrayLike:
    """Transform applied to native values before linear mapping into interval."""
    return values


# ==================================================
# Line: 571

def _standardize_color_sequence(self, colors: ArrayLike) -> ArrayLike:
    """Convert color sequence to RGB(A) array, preserving but not adding alpha."""
    def has_alpha(x):
        return to_rgba(x) != to_rgba(x, 1)

    if isinstance(colors, np.ndarray):
        needs_alpha = colors.shape[1] == 4
    else:
        needs_alpha = any(has_alpha(x) for x in colors)

    if needs_alpha:
        return to_rgba_array(colors)
    else:
        return to_rgba_array(colors)[:, :3]


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/groupby.py
# Line: 73

def _reorder_columns(self, res, data):
    """Reorder result columns to match original order with new columns appended."""
    cols = [c for c in data if c in res]
    cols += [c for c in res if c not in data]
    return res.reindex(columns=pd.Index(cols))


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/subplots.py
# Line: 46

def _check_dimension_uniqueness(
    self, facet_spec: FacetSpec, pair_spec: PairSpec

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/data.py
# Line: 127

def _assign_variables(
    self,
    data: DataFrame | Mapping | None,
    variables: dict[str, VariableSpec],

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/scales.py
# Line: 84

def _get_scale(self, name: str, forward: Callable, inverse: Callable):

    major_locator, minor_locator = self._get_locators(**self._tick_params)
    major_formatter = self._get_formatter(major_locator, **self._label_params)

    class InternalScale(mpl.scale.FuncScale):
        def set_default_locators_and_formatters(self, axis):
            axis.set_major_locator(major_locator)
            if minor_locator is not None:
                axis.set_minor_locator(minor_locator)
            axis.set_major_formatter(major_formatter)

    return InternalScale(name, (forward, inverse))


# ==================================================
# Line: 90

def set_default_locators_and_formatters(self, axis):
    axis.set_major_locator(major_locator)
    if minor_locator is not None:
        axis.set_minor_locator(minor_locator)
    axis.set_major_formatter(major_formatter)


# ==================================================
# Line: 281

def set_default_locators_and_formatters(self, axis):
    ...
    # axis.set_major_locator(major_locator)
    # if minor_locator is not None:
    #     axis.set_minor_locator(minor_locator)
    # axis.set_major_formatter(major_formatter)


# ==================================================
# Line: 651

def _parse_for_log_params(
    self, trans: str | TransFuncs | None

# ==================================================
# Line: 933

def get_tick_space(self):
    # TODO how to do this in a configurable / auto way?
    # Would be cool to have legend density adapt to figure size, etc.
    return 5


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/matrix.py
# Line: 265

def _skip_ticks(self, labels, tickevery):
    """Return ticks and labels at evenly spaced intervals."""
    n = len(labels)
    if tickevery == 0:
        ticks, labels = [], []
    elif tickevery == 1:
        ticks, labels = np.arange(n) + .5, labels
    else:
        start, end, step = 0, n, tickevery
        ticks = np.arange(start, end, step) + .5
        labels = labels[start:end:step]
    return ticks, labels


# ==================================================
# Line: 774

def _preprocess_colors(self, data, colors, axis):
    """Preprocess {row/col}_colors to extract labels and convert colors."""
    labels = None

    if colors is not None:
        if isinstance(colors, (pd.DataFrame, pd.Series)):

            # If data is unindexed, raise
            if (not hasattr(data, "index") and axis == 0) or (
                not hasattr(data, "columns") and axis == 1
            ):
                axis_name = "col" if axis else "row"
                msg = (f"{axis_name}_colors indices can't be matched with data "
                       f"indices. Provide {axis_name}_colors as a non-indexed "
                       "datatype, e.g. by using `.to_numpy()``")
                raise TypeError(msg)

            # Ensure colors match data indices
            if axis == 0:
                colors = colors.reindex(data.index)
            else:
                colors = colors.reindex(data.columns)

            # Replace na's with white color
            # TODO We should set these to transparent instead
            colors = colors.astype(object).fillna('white')

            # Extract color values and labels from frame/series
            if isinstance(colors, pd.DataFrame):
                labels = list(colors.columns)
                colors = colors.T.values
            else:
                if colors.name is None:
                    labels = [""]
                else:
                    labels = [colors.name]
                colors = colors.values

        colors = _convert_colors(colors)

    return colors, labels


# ==================================================
# Line: 900

def dim_ratios(self, colors, dendrogram_ratio, colors_ratio):
    """Get the proportions of the figure taken up by each axes."""
    ratios = [dendrogram_ratio]

    if colors is not None:
        # Colors are encoded as rgb, so there is an extra dimension
        if np.ndim(colors) > 2:
            n_colors = len(colors)
        else:
            n_colors = 1

        ratios += [n_colors * colors_ratio]

    # Add the ratio for the heatmap itself
    ratios.append(1 - sum(ratios))

    return ratios


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_statistics.py
# Line: 90

def _define_support_grid(self, x, bw, cut, clip, gridsize):
    """Create the grid of evaluation points depending for vector x."""
    clip_lo = -np.inf if clip[0] is None else clip[0]
    clip_hi = +np.inf if clip[1] is None else clip[1]
    gridmin = max(x.min() - bw * cut, clip_lo)
    gridmax = min(x.max() + bw * cut, clip_hi)
    return np.linspace(gridmin, gridmax, gridsize)


# ==================================================
# Line: 255

def _define_bin_edges(self, x, weights, bins, binwidth, binrange, discrete):
    """Inner function that takes bin parameters as arguments."""
    if binrange is None:
        start, stop = x.min(), x.max()
    else:
        start, stop = binrange

    if discrete:
        bin_edges = np.arange(start - .5, stop + 1.5)
    elif binwidth is not None:
        step = binwidth
        bin_edges = np.arange(start, stop + step, step)
        # Handle roundoff error (maybe there is a less clumsy way?)
        if bin_edges.max() < stop or len(bin_edges) < 2:
            bin_edges = np.append(bin_edges, bin_edges.max() + step)
    else:
        bin_edges = np.histogram_bin_edges(
            x, bins, binrange, weights,
        )
    return bin_edges


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/distributions.py
# Line: 170

def _artist_kws(self, kws, fill, element, multiple, color, alpha):
    """Handle differences between artists in filled/unfilled plots."""
    kws = kws.copy()
    if fill:
        kws = normalize_kwargs(kws, mpl.collections.PolyCollection)
        kws.setdefault("facecolor", to_rgba(color, alpha))

        if element == "bars":
            # Make bar() interface with property cycle correctly
            # https://github.com/matplotlib/matplotlib/issues/19385
            kws["color"] = "none"

        if multiple in ["stack", "fill"] or element == "bars":
            kws.setdefault("edgecolor", mpl.rcParams["patch.edgecolor"])
        else:
            kws.setdefault("edgecolor", to_rgba(color, 1))
    elif element == "bars":
        kws["facecolor"] = "none"
        kws["edgecolor"] = to_rgba(color, alpha)
    else:
        kws["color"] = to_rgba(color, alpha)
    return kws


# ==================================================
# Line: 193

def _quantile_to_level(self, data, quantile):
    """Return data levels corresponding to quantile cuts of mass."""
    isoprop = np.asarray(quantile)
    values = np.ravel(data)
    sorted_values = np.sort(values)[::-1]
    normalized_values = np.cumsum(sorted_values) / values.sum()
    idx = np.searchsorted(normalized_values, 1 - isoprop)
    levels = np.take(sorted_values, idx, mode="clip")
    return levels


# ==================================================
# Line: 203

def _cmap_from_color(self, color):
    """Return a sequential colormap given a color seed."""
    # Like so much else here, this is broadly useful, but keeping it
    # in this class to signify that I haven't thought overly hard about it...
    r, g, b, _ = to_rgba(color)
    h, s, _ = husl.rgb_to_husl(r, g, b)
    xx = np.linspace(-1, 1, int(1.15 * 256))[:256]
    ramp = np.zeros((256, 3))
    ramp[:, 0] = h
    ramp[:, 1] = s * np.cos(xx)
    ramp[:, 2] = np.linspace(35, 80, 256)
    colors = np.clip([husl.husl_to_rgb(*hsl) for hsl in ramp], 0, 1)
    return mpl.colors.ListedColormap(colors[::-1])


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/axisgrid.py
# Line: 249

def _get_palette(self, data, hue, hue_order, palette):
    """Get a list of colors for the hue variable."""
    if hue is None:
        palette = color_palette(n_colors=1)

    else:
        hue_names = categorical_order(data[hue], hue_order)
        n_colors = len(hue_names)

        # By default use either the current color palette or HUSL
        if palette is None:
            current_palette = utils.get_color_cycle()
            if n_colors > len(current_palette):
                colors = color_palette("husl", n_colors)
            else:
                colors = color_palette(n_colors=n_colors)

        # Allow for palette to map from hue variable names
        elif isinstance(palette, dict):
            color_names = [palette[h] for h in hue_names]
            colors = color_palette(color_names, n_colors)

        # Otherwise act as if we just got a list of colors
        else:
            colors = color_palette(palette, n_colors)

        palette = color_palette(colors, n_colors)

    return palette


# ==================================================
# Line: 1670

def _find_numeric_cols(self, data):
    """Find which variables in a DataFrame are numeric."""
    numeric_cols = []
    for col in data:
        if variable_type(data[col]) == "numeric":
            numeric_cols.append(col)
    return numeric_cols



# ==================================================
# Line: 1769

def _inject_kwargs(self, func, kws, params):
    """Add params to kws if they are accepted by func."""
    func_params = signature(func).parameters
    for key, val in params.items():
        if key in func_params:
            kws.setdefault(key, val)


# ==================================================
