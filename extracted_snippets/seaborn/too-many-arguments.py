# too-many-arguments snippets for seaborn

# File: /root/ecooptimizer/seaborn/seaborn/_base.py
# Line: 849

def iter_data(
    self, grouping_vars=None, *,
    reverse=False, from_comp_data=False,
    by_facet=True, allow_empty=False, dropna=True,

# ==================================================
# Line: 1284

def _update_legend_data(
    self,
    update,
    var,
    verbosity,
    title,
    title_kws,
    attr_names,
    other_props,

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/regression.py
# Line: 76

def __init__(self, x, y, data=None, x_estimator=None, x_bins=None,
             x_ci="ci", scatter=True, fit_reg=True, ci=95, n_boot=1000,
             units=None, seed=None, order=1, logistic=False, lowess=False,
             robust=False, logx=False, x_partial=None, y_partial=None,
             truncate=False, dropna=True, x_jitter=None, y_jitter=None,
             color=None, label=None):

    # Set member attributes
    self.x_estimator = x_estimator
    self.ci = ci
    self.x_ci = ci if x_ci == "ci" else x_ci
    self.n_boot = n_boot
    self.seed = seed
    self.scatter = scatter
    self.fit_reg = fit_reg
    self.order = order
    self.logistic = logistic
    self.lowess = lowess
    self.robust = robust
    self.logx = logx
    self.truncate = truncate
    self.x_jitter = x_jitter
    self.y_jitter = y_jitter
    self.color = color
    self.label = label

    # Validate the regression options:
    if sum((order > 1, logistic, robust, lowess, logx)) > 1:
        raise ValueError("Mutually exclusive regression options.")

    # Extract the data vals from the arguments or passed dataframe
    self.establish_variables(data, x=x, y=y, units=units,
                             x_partial=x_partial, y_partial=y_partial)

    # Drop null observations
    if dropna:
        self.dropna("x", "y", "units", "x_partial", "y_partial")

    # Regress nuisance variables out of the data
    if self.x_partial is not None:
        self.x = self.regress_out(self.x, self.x_partial)
    if self.y_partial is not None:
        self.y = self.regress_out(self.y, self.y_partial)

    # Possibly bin the predictor variable, which implies a point estimate
    if x_bins is not None:
        self.x_estimator = np.mean if x_estimator is None else x_estimator
        x_discrete, x_bins = self.bin_predictor(x_bins)
        self.x_discrete = x_discrete
    else:
        self.x_discrete = self.x

    # Disable regression in case of singleton inputs
    if len(self.x) <= 1:
        self.fit_reg = False

    # Save the range of the x variable for the grid later
    if self.fit_reg:
        self.x_range = self.x.min(), self.x.max()


# ==================================================
# Line: 580

def lmplot(
    data, *,
    x=None, y=None, hue=None, col=None, row=None,
    palette=None, col_wrap=None, height=5, aspect=1, markers="o",
    sharex=None, sharey=None, hue_order=None, col_order=None, row_order=None,
    legend=True, legend_out=None, x_estimator=None, x_bins=None,
    x_ci="ci", scatter=True, fit_reg=True, ci=95, n_boot=1000,
    units=None, seed=None, order=1, logistic=False, lowess=False,
    robust=False, logx=False, x_partial=None, y_partial=None,
    truncate=True, x_jitter=None, y_jitter=None, scatter_kws=None,
    line_kws=None, facet_kws=None,

# ==================================================
# Line: 761

def regplot(
    data=None, *, x=None, y=None,
    x_estimator=None, x_bins=None, x_ci="ci",
    scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None,
    seed=None, order=1, logistic=False, lowess=False, robust=False,
    logx=False, x_partial=None, y_partial=None,
    truncate=True, dropna=True, x_jitter=None, y_jitter=None,
    label=None, color=None, marker="o",
    scatter_kws=None, line_kws=None, ax=None

# ==================================================
# Line: 864

def residplot(
    data=None, *, x=None, y=None,
    x_partial=None, y_partial=None, lowess=False,
    order=1, robust=False, dropna=True, label=None, color=None,
    scatter_kws=None, line_kws=None, ax=None

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/utils.py
# Line: 277

def despine(fig=None, ax=None, top=True, right=True, left=False,
            bottom=False, offset=None, trim=False):
    """Remove the top and right spines from plot(s).

    fig : matplotlib figure, optional
        Figure to despine all axes of, defaults to the current figure.
    ax : matplotlib axes, optional
        Specific axes object to despine. Ignored if fig is provided.
    top, right, left, bottom : boolean, optional
        If True, remove that spine.
    offset : int or dict, optional
        Absolute distance, in points, spines should be moved away
        from the axes (negative values move spines inward). A single value
        applies to all spines; a dict can be used to set offset values per
        side.
    trim : bool, optional
        If True, limit spines to the smallest and largest major tick
        on each non-despined axis.

    Returns
    -------
    None

    """
    # Get references to the axes we want
    if fig is None and ax is None:
        axes = plt.gcf().axes
    elif fig is not None:
        axes = fig.axes
    elif ax is not None:
        axes = [ax]

    for ax_i in axes:
        for side in ["top", "right", "left", "bottom"]:
            # Toggle the spine objects
            is_visible = not locals()[side]
            ax_i.spines[side].set_visible(is_visible)
            if offset is not None and is_visible:
                try:
                    val = offset.get(side, 0)
                except AttributeError:
                    val = offset
                ax_i.spines[side].set_position(('outward', val))

        # Potentially move the ticks
        if left and not right:
            maj_on = any(
                t.tick1line.get_visible()
                for t in ax_i.yaxis.majorTicks
            )
            min_on = any(
                t.tick1line.get_visible()
                for t in ax_i.yaxis.minorTicks
            )
            ax_i.yaxis.set_ticks_position("right")
            for t in ax_i.yaxis.majorTicks:
                t.tick2line.set_visible(maj_on)
            for t in ax_i.yaxis.minorTicks:
                t.tick2line.set_visible(min_on)

        if bottom and not top:
            maj_on = any(
                t.tick1line.get_visible()
                for t in ax_i.xaxis.majorTicks
            )
            min_on = any(
                t.tick1line.get_visible()
                for t in ax_i.xaxis.minorTicks
            )
            ax_i.xaxis.set_ticks_position("top")
            for t in ax_i.xaxis.majorTicks:
                t.tick2line.set_visible(maj_on)
            for t in ax_i.xaxis.minorTicks:
                t.tick2line.set_visible(min_on)

        if trim:
            # clip off the parts of the spines that extend past major ticks
            xticks = np.asarray(ax_i.get_xticks())
            if xticks.size:
                firsttick = np.compress(xticks >= min(ax_i.get_xlim()),
                                        xticks)[0]
                lasttick = np.compress(xticks <= max(ax_i.get_xlim()),
                                       xticks)[-1]
                ax_i.spines['bottom'].set_bounds(firsttick, lasttick)
                ax_i.spines['top'].set_bounds(firsttick, lasttick)
                newticks = xticks.compress(xticks <= lasttick)
                newticks = newticks.compress(newticks >= firsttick)
                ax_i.set_xticks(newticks)

            yticks = np.asarray(ax_i.get_yticks())
            if yticks.size:
                firsttick = np.compress(yticks >= min(ax_i.get_ylim()),
                                        yticks)[0]
                lasttick = np.compress(yticks <= max(ax_i.get_ylim()),
                                       yticks)[-1]
                ax_i.spines['left'].set_bounds(firsttick, lasttick)
                ax_i.spines['right'].set_bounds(firsttick, lasttick)
                newticks = yticks.compress(yticks <= lasttick)
                newticks = newticks.compress(newticks >= firsttick)
                ax_i.set_yticks(newticks)



# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/rcmod.py
# Line: 82

def set_theme(context="notebook", style="darkgrid", palette="deep",
              font="sans-serif", font_scale=1, color_codes=True, rc=None):
    """
    Set aspects of the visual theme for all matplotlib and seaborn plots.

    This function changes the global defaults for all plots using the
    matplotlib rcParams system. The themeing is decomposed into several distinct
    sets of parameter values.

    The options are illustrated in the :doc:`aesthetics <../tutorial/aesthetics>`
    and :doc:`color palette <../tutorial/color_palettes>` tutorials.

    Parameters
    ----------
    context : string or dict
        Scaling parameters, see :func:`plotting_context`.
    style : string or dict
        Axes style parameters, see :func:`axes_style`.
    palette : string or sequence
        Color palette, see :func:`color_palette`.
    font : string
        Font family, see matplotlib font manager.
    font_scale : float, optional
        Separate scaling factor to independently scale the size of the
        font elements.
    color_codes : bool
        If ``True`` and ``palette`` is a seaborn palette, remap the shorthand
        color codes (e.g. "b", "g", "r", etc.) to the colors from this palette.
    rc : dict or None
        Dictionary of rc parameter mappings to override the above.

    Examples
    --------

    .. include:: ../docstrings/set_theme.rst

    """
    set_context(context, font_scale)
    set_style(style, rc={"font.family": font})
    set_palette(palette, color_codes=color_codes)
    if rc is not None:
        mpl.rcParams.update(rc)



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
# File: /root/ecooptimizer/seaborn/seaborn/palettes.py
# Line: 532

def diverging_palette(h_neg, h_pos, s=75, l=50, sep=1, n=6,  # noqa
                      center="light", as_cmap=False):
    """Make a diverging palette between two HUSL colors.

    If you are using the IPython notebook, you can also choose this palette
    interactively with the :func:`choose_diverging_palette` function.

    Parameters
    ----------
    h_neg, h_pos : float in [0, 359]
        Anchor hues for negative and positive extents of the map.
    s : float in [0, 100], optional
        Anchor saturation for both extents of the map.
    l : float in [0, 100], optional
        Anchor lightness for both extents of the map.
    sep : int, optional
        Size of the intermediate region.
    n : int, optional
        Number of colors in the palette (if not returning a cmap)
    center : {"light", "dark"}, optional
        Whether the center of the palette is light or dark
    as_cmap : bool, optional
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    dark_palette : Create a sequential palette with dark values.
    light_palette : Create a sequential palette with light values.

    Examples
    --------
    .. include: ../docstrings/diverging_palette.rst

    """
    palfunc = dict(dark=dark_palette, light=light_palette)[center]
    n_half = int(128 - (sep // 2))
    neg = palfunc((h_neg, s, l), n_half, reverse=True, input="husl")
    pos = palfunc((h_pos, s, l), n_half, input="husl")
    midpoint = dict(light=[(.95, .95, .95)], dark=[(.133, .133, .133)])[center]
    mid = midpoint * sep
    pal = blend_palette(np.concatenate([neg, mid, pos]), n, as_cmap=as_cmap)
    return pal



# ==================================================
# Line: 665

def cubehelix_palette(n_colors=6, start=0, rot=.4, gamma=1.0, hue=0.8,
                      light=.85, dark=.15, reverse=False, as_cmap=False):
    """Make a sequential palette from the cubehelix system.

    This produces a colormap with linearly-decreasing (or increasing)
    brightness. That means that information will be preserved if printed to
    black and white or viewed by someone who is colorblind.  "cubehelix" is
    also available as a matplotlib-based palette, but this function gives the
    user more control over the look of the palette and has a different set of
    defaults.

    In addition to using this function, it is also possible to generate a
    cubehelix palette generally in seaborn using a string starting with
    `ch:` and containing other parameters (e.g. `"ch:s=.25,r=-.5"`).

    Parameters
    ----------
    n_colors : int
        Number of colors in the palette.
    start : float, 0 <= start <= 3
        The hue value at the start of the helix.
    rot : float
        Rotations around the hue wheel over the range of the palette.
    gamma : float 0 <= gamma
        Nonlinearity to emphasize dark (gamma < 1) or light (gamma > 1) colors.
    hue : float, 0 <= hue <= 1
        Saturation of the colors.
    dark : float 0 <= dark <= 1
        Intensity of the darkest color in the palette.
    light : float 0 <= light <= 1
        Intensity of the lightest color in the palette.
    reverse : bool
        If True, the palette will go from dark to light.
    as_cmap : bool
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    choose_cubehelix_palette : Launch an interactive widget to select cubehelix
                               palette parameters.
    dark_palette : Create a sequential palette with dark low values.
    light_palette : Create a sequential palette with bright low values.

    References
    ----------
    Green, D. A. (2011). "A colour scheme for the display of astronomical
    intensity images". Bulletin of the Astromical Society of India, Vol. 39,
    p. 289-295.

    Examples
    --------
    .. include:: ../docstrings/cubehelix_palette.rst

    """
    def get_color_function(p0, p1):
        # Copied from matplotlib because it lives in private module
        def color(x):
            # Apply gamma factor to emphasise low or high intensity values
            xg = x ** gamma

            # Calculate amplitude and angle of deviation from the black
            # to white diagonal in the plane of constant
            # perceived intensity.
            a = hue * xg * (1 - xg) / 2

            phi = 2 * np.pi * (start / 3 + rot * x)

            return xg + a * (p0 * np.cos(phi) + p1 * np.sin(phi))
        return color

    cdict = {
        "red": get_color_function(-0.14861, 1.78277),
        "green": get_color_function(-0.29227, -0.90649),
        "blue": get_color_function(1.97294, 0.0),
    }

    cmap = mpl.colors.LinearSegmentedColormap("cubehelix", cdict)

    x = np.linspace(light, dark, int(n_colors))
    pal = cmap(x)[:, :3].tolist()
    if reverse:
        pal = pal[::-1]

    if as_cmap:
        x_256 = np.linspace(light, dark, 256)
        if reverse:
            x_256 = x_256[::-1]
        pal_256 = cmap(x_256)
        cmap = mpl.colors.ListedColormap(pal_256, "seaborn_cubehelix")
        return cmap
    else:
        return _ColorPalette(pal)



# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/categorical.py
# Line: 56

def __init__(
    self,
    data=None,
    variables={},
    order=None,
    orient=None,
    require_numeric=False,
    color=None,
    legend="auto",

# ==================================================
# Line: 591

def plot_boxes(
    self,
    width,
    dodge,
    gap,
    fill,
    whis,
    color,
    linecolor,
    linewidth,
    fliersize,
    plot_kws,  # TODO rename user_kws?

# ==================================================
# Line: 755

def plot_boxens(
    self,
    width,
    dodge,
    gap,
    fill,
    color,
    linecolor,
    linewidth,
    width_method,
    k_depth,
    outlier_prop,
    trust_alpha,
    showfliers,
    box_kws,
    flier_kws,
    line_kws,
    plot_kws,

# ==================================================
# Line: 896

def plot_violins(
    self,
    width,
    dodge,
    gap,
    split,
    color,
    fill,
    linecolor,
    linewidth,
    inner,
    density_norm,
    common_norm,
    kde_kws,
    inner_kws,
    plot_kws,

# ==================================================
# Line: 1172

def plot_points(
    self,
    aggregator,
    markers,
    linestyles,
    dodge,
    color,
    capsize,
    err_kws,
    plot_kws,

# ==================================================
# Line: 1252

def plot_bars(
    self,
    aggregator,
    dodge,
    gap,
    width,
    fill,
    color,
    capsize,
    err_kws,
    plot_kws,

# ==================================================
# Line: 1597

def boxplot(
    data=None, *, x=None, y=None, hue=None, order=None, hue_order=None,
    orient=None, color=None, palette=None, saturation=.75, fill=True,
    dodge="auto", width=.8, gap=0, whis=1.5, linecolor="auto", linewidth=None,
    fliersize=None, hue_norm=None, native_scale=False, log_scale=None, formatter=None,
    legend="auto", ax=None, **kwargs

# ==================================================
# Line: 1722

def violinplot(
    data=None, *, x=None, y=None, hue=None, order=None, hue_order=None,
    orient=None, color=None, palette=None, saturation=.75, fill=True,
    inner="box", split=False, width=.8, dodge="auto", gap=0,
    linewidth=None, linecolor="auto", cut=2, gridsize=100,
    bw_method="scott", bw_adjust=1, density_norm="area", common_norm=False,
    hue_norm=None, formatter=None, log_scale=None, native_scale=False,
    legend="auto", scale=deprecated, scale_hue=deprecated, bw=deprecated,
    inner_kws=None, ax=None, **kwargs,

# ==================================================
# Line: 1912

def boxenplot(
    data=None, *, x=None, y=None, hue=None, order=None, hue_order=None,
    orient=None, color=None, palette=None, saturation=.75, fill=True,
    dodge="auto", width=.8, gap=0, linewidth=None, linecolor=None,
    width_method="exponential", k_depth="tukey", outlier_prop=0.007, trust_alpha=0.05,
    showfliers=True, hue_norm=None, log_scale=None, native_scale=False, formatter=None,
    legend="auto", scale=deprecated, box_kws=None, flier_kws=None, line_kws=None,
    ax=None, **kwargs,

# ==================================================
# Line: 2082

def stripplot(
    data=None, *, x=None, y=None, hue=None, order=None, hue_order=None,
    jitter=True, dodge=False, orient=None, color=None, palette=None,
    size=5, edgecolor=default, linewidth=0,
    hue_norm=None, log_scale=None, native_scale=False, formatter=None, legend="auto",
    ax=None, **kwargs

# ==================================================
# Line: 2207

def swarmplot(
    data=None, *, x=None, y=None, hue=None, order=None, hue_order=None,
    dodge=False, orient=None, color=None, palette=None,
    size=5, edgecolor=None, linewidth=0, hue_norm=None, log_scale=None,
    native_scale=False, formatter=None, legend="auto", warn_thresh=.05,
    ax=None, **kwargs

# ==================================================
# Line: 2336

def barplot(
    data=None, *, x=None, y=None, hue=None, order=None, hue_order=None,
    estimator="mean", errorbar=("ci", 95), n_boot=1000, seed=None, units=None,
    weights=None, orient=None, color=None, palette=None, saturation=.75,
    fill=True, hue_norm=None, width=.8, dodge="auto", gap=0, log_scale=None,
    native_scale=False, formatter=None, legend="auto", capsize=0, err_kws=None,
    ci=deprecated, errcolor=deprecated, errwidth=deprecated, ax=None, **kwargs,

# ==================================================
# Line: 2478

def pointplot(
    data=None, *, x=None, y=None, hue=None, order=None, hue_order=None,
    estimator="mean", errorbar=("ci", 95), n_boot=1000, seed=None, units=None,
    weights=None, color=None, palette=None, hue_norm=None, markers=default,
    linestyles=default, dodge=False, log_scale=None, native_scale=False,
    orient=None, capsize=0, formatter=None, legend="auto", err_kws=None,
    ci=deprecated, errwidth=deprecated, join=deprecated, scale=deprecated,
    ax=None, **kwargs,

# ==================================================
# Line: 2627

def countplot(
    data=None, *, x=None, y=None, hue=None, order=None, hue_order=None,
    orient=None, color=None, palette=None, saturation=.75, fill=True, hue_norm=None,
    stat="count", width=.8, dodge="auto", gap=0, log_scale=None, native_scale=False,
    formatter=None, legend="auto", ax=None, **kwargs

# ==================================================
# Line: 2761

def catplot(
    data=None, *, x=None, y=None, hue=None, row=None, col=None, kind="strip",
    estimator="mean", errorbar=("ci", 95), n_boot=1000, seed=None, units=None,
    weights=None, order=None, hue_order=None, row_order=None, col_order=None,
    col_wrap=None, height=5, aspect=1, log_scale=None, native_scale=False,
    formatter=None, orient=None, color=None, palette=None, hue_norm=None,
    legend="auto", legend_out=True, sharex=True, sharey=True,
    margin_titles=False, facet_kws=None, ci=deprecated, **kwargs

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/scales.py
# Line: 538

def tick(
    self,
    locator: Locator | None = None, *,
    at: Sequence[float] | None = None,
    upto: int | None = None,
    count: int | None = None,
    every: float | None = None,
    between: tuple[float, float] | None = None,
    minor: int | None = None,

# ==================================================
# Line: 665

def _get_locators(self, locator, at, upto, count, every, between, minor):

    log_base, symlog_thresh = self._parse_for_log_params(self.trans)

    if locator is not None:
        major_locator = locator

    elif upto is not None:
        if log_base:
            major_locator = LogLocator(base=log_base, numticks=upto)
        else:
            major_locator = MaxNLocator(upto, steps=[1, 1.5, 2, 2.5, 3, 5, 10])

    elif count is not None:
        if between is None:
            # This is rarely useful (unless you are setting limits)
            major_locator = LinearLocator(count)
        else:
            if log_base or symlog_thresh:
                forward, inverse = self._get_transform()
                lo, hi = forward(between)
                ticks = inverse(np.linspace(lo, hi, num=count))
            else:
                ticks = np.linspace(*between, num=count)
            major_locator = FixedLocator(ticks)

    elif every is not None:
        if between is None:
            major_locator = MultipleLocator(every)
        else:
            lo, hi = between
            ticks = np.arange(lo, hi + every, every)
            major_locator = FixedLocator(ticks)

    elif at is not None:
        major_locator = FixedLocator(at)

    else:
        if log_base:
            major_locator = LogLocator(log_base)
        elif symlog_thresh:
            major_locator = SymmetricalLogLocator(linthresh=symlog_thresh, base=10)
        else:
            major_locator = AutoLocator()

    if minor is None:
        minor_locator = LogLocator(log_base, subs=None) if log_base else None
    else:
        if log_base:
            subs = np.linspace(0, log_base, minor + 2)[1:-1]
            minor_locator = LogLocator(log_base, subs=subs)
        else:
            minor_locator = AutoMinorLocator(minor + 1)

    return major_locator, minor_locator


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/matrix.py
# Line: 100

def __init__(self, data, vmin, vmax, cmap, center, robust, annot, fmt,
             annot_kws, cbar, cbar_kws,
             xticklabels=True, yticklabels=True, mask=None):
    """Initialize the plotting object."""
    # We always want to have a DataFrame with semantic information
    # and an ndarray to pass to matplotlib
    if isinstance(data, pd.DataFrame):
        plot_data = data.values
    else:
        plot_data = np.asarray(data)
        data = pd.DataFrame(plot_data)

    # Validate the mask and convert to DataFrame
    mask = _matrix_mask(data, mask)

    plot_data = np.ma.masked_where(np.asarray(mask), plot_data)

    # Get good names for the rows and columns
    xtickevery = 1
    if isinstance(xticklabels, int):
        xtickevery = xticklabels
        xticklabels = _index_to_ticklabels(data.columns)
    elif xticklabels is True:
        xticklabels = _index_to_ticklabels(data.columns)
    elif xticklabels is False:
        xticklabels = []

    ytickevery = 1
    if isinstance(yticklabels, int):
        ytickevery = yticklabels
        yticklabels = _index_to_ticklabels(data.index)
    elif yticklabels is True:
        yticklabels = _index_to_ticklabels(data.index)
    elif yticklabels is False:
        yticklabels = []

    if not len(xticklabels):
        self.xticks = []
        self.xticklabels = []
    elif isinstance(xticklabels, str) and xticklabels == "auto":
        self.xticks = "auto"
        self.xticklabels = _index_to_ticklabels(data.columns)
    else:
        self.xticks, self.xticklabels = self._skip_ticks(xticklabels,
                                                         xtickevery)

    if not len(yticklabels):
        self.yticks = []
        self.yticklabels = []
    elif isinstance(yticklabels, str) and yticklabels == "auto":
        self.yticks = "auto"
        self.yticklabels = _index_to_ticklabels(data.index)
    else:
        self.yticks, self.yticklabels = self._skip_ticks(yticklabels,
                                                         ytickevery)

    # Get good names for the axis labels
    xlabel = _index_to_label(data.columns)
    ylabel = _index_to_label(data.index)
    self.xlabel = xlabel if xlabel is not None else ""
    self.ylabel = ylabel if ylabel is not None else ""

    # Determine good default values for the colormapping
    self._determine_cmap_params(plot_data, vmin, vmax,
                                cmap, center, robust)

    # Sort out the annotations
    if annot is None or annot is False:
        annot = False
        annot_data = None
    else:
        if isinstance(annot, bool):
            annot_data = plot_data
        else:
            annot_data = np.asarray(annot)
            if annot_data.shape != plot_data.shape:
                err = "`data` and `annot` must have same shape."
                raise ValueError(err)
        annot = True

    # Save other attributes to the object
    self.data = data
    self.plot_data = plot_data

    self.annot = annot
    self.annot_data = annot_data

    self.fmt = fmt
    self.annot_kws = {} if annot_kws is None else annot_kws.copy()
    self.cbar = cbar
    self.cbar_kws = {} if cbar_kws is None else cbar_kws.copy()


# ==================================================
# Line: 192

def _determine_cmap_params(self, plot_data, vmin, vmax,
                           cmap, center, robust):
    """Use some heuristics to set good defaults for colorbar and range."""

    # plot_data is a np.ma.array instance
    calc_data = plot_data.astype(float).filled(np.nan)
    if vmin is None:
        if robust:
            vmin = np.nanpercentile(calc_data, 2)
        else:
            vmin = np.nanmin(calc_data)
    if vmax is None:
        if robust:
            vmax = np.nanpercentile(calc_data, 98)
        else:
            vmax = np.nanmax(calc_data)
    self.vmin, self.vmax = vmin, vmax

    # Choose default colormaps if not provided
    if cmap is None:
        if center is None:
            self.cmap = cm.rocket
        else:
            self.cmap = cm.icefire
    elif isinstance(cmap, str):
        self.cmap = get_colormap(cmap)
    elif isinstance(cmap, list):
        self.cmap = mpl.colors.ListedColormap(cmap)
    else:
        self.cmap = cmap

    # Recenter a divergent colormap
    if center is not None:

        # Copy bad values
        # in mpl<3.2 only masked values are honored with "bad" color spec
        # (see https://github.com/matplotlib/matplotlib/pull/14257)
        bad = self.cmap(np.ma.masked_invalid([np.nan]))[0]

        # under/over values are set for sure when cmap extremes
        # do not map to the same color as +-inf
        under = self.cmap(-np.inf)
        over = self.cmap(np.inf)
        under_set = under != self.cmap(0)
        over_set = over != self.cmap(self.cmap.N - 1)

        vrange = max(vmax - center, center - vmin)
        normlize = mpl.colors.Normalize(center - vrange, center + vrange)
        cmin, cmax = normlize([vmin, vmax])
        cc = np.linspace(cmin, cmax, 256)
        self.cmap = mpl.colors.ListedColormap(self.cmap(cc))
        self.cmap.set_bad(bad)
        if under_set:
            self.cmap.set_under(under)
        if over_set:
            self.cmap.set_over(over)


# ==================================================
# Line: 355

def heatmap(
    data, *,
    vmin=None, vmax=None, cmap=None, center=None, robust=False,
    annot=None, fmt=".2g", annot_kws=None,
    linewidths=0, linecolor="white",
    cbar=True, cbar_kws=None, cbar_ax=None,
    square=False, xticklabels="auto", yticklabels="auto",
    mask=None, ax=None,
    **kwargs

# ==================================================
# Line: 466

def __init__(self, data, linkage, metric, method, axis, label, rotate):
    """Plot a dendrogram of the relationships between the columns of data

    Parameters
    ----------
    data : pandas.DataFrame
        Rectangular data
    """
    self.axis = axis
    if self.axis == 1:
        data = data.T

    if isinstance(data, pd.DataFrame):
        array = data.values
    else:
        array = np.asarray(data)
        data = pd.DataFrame(array)

    self.array = array
    self.data = data

    self.shape = self.data.shape
    self.metric = metric
    self.method = method
    self.axis = axis
    self.label = label
    self.rotate = rotate

    if linkage is None:
        self.linkage = self.calculated_linkage
    else:
        self.linkage = linkage
    self.dendrogram = self.calculate_dendrogram()

    # Dendrogram ends are always at multiples of 5, who knows why
    ticks = 10 * np.arange(self.data.shape[0]) + 5

    if self.label:
        ticklabels = _index_to_ticklabels(self.data.index)
        ticklabels = [ticklabels[i] for i in self.reordered_ind]
        if self.rotate:
            self.xticks = []
            self.yticks = ticks
            self.xticklabels = []

            self.yticklabels = ticklabels
            self.ylabel = _index_to_label(self.data.index)
            self.xlabel = ''
        else:
            self.xticks = ticks
            self.yticks = []
            self.xticklabels = ticklabels
            self.yticklabels = []
            self.ylabel = ''
            self.xlabel = _index_to_label(self.data.index)
    else:
        self.xticks, self.yticks = [], []
        self.yticklabels, self.xticklabels = [], []
        self.xlabel, self.ylabel = '', ''

    self.dependent_coord = self.dendrogram['dcoord']
    self.independent_coord = self.dendrogram['icoord']


# ==================================================
# Line: 642

def dendrogram(
    data, *,
    linkage=None, axis=1, label=True, metric='euclidean',
    method='average', rotate=False, tree_kws=None, ax=None

# ==================================================
# Line: 698

def __init__(self, data, pivot_kws=None, z_score=None, standard_scale=None,
             figsize=None, row_colors=None, col_colors=None, mask=None,
             dendrogram_ratio=None, colors_ratio=None, cbar_pos=None):
    """Grid object for organizing clustered heatmap input on to axes"""
    if _no_scipy:
        raise RuntimeError("ClusterGrid requires scipy to be available")

    if isinstance(data, pd.DataFrame):
        self.data = data
    else:
        self.data = pd.DataFrame(data)

    self.data2d = self.format_data(self.data, pivot_kws, z_score,
                                   standard_scale)

    self.mask = _matrix_mask(self.data2d, mask)

    self._figure = plt.figure(figsize=figsize)

    self.row_colors, self.row_color_labels = \
        self._preprocess_colors(data, row_colors, axis=0)
    self.col_colors, self.col_color_labels = \
        self._preprocess_colors(data, col_colors, axis=1)

    try:
        row_dendrogram_ratio, col_dendrogram_ratio = dendrogram_ratio
    except TypeError:
        row_dendrogram_ratio = col_dendrogram_ratio = dendrogram_ratio

    try:
        row_colors_ratio, col_colors_ratio = colors_ratio
    except TypeError:
        row_colors_ratio = col_colors_ratio = colors_ratio

    width_ratios = self.dim_ratios(self.row_colors,
                                   row_dendrogram_ratio,
                                   row_colors_ratio)
    height_ratios = self.dim_ratios(self.col_colors,
                                    col_dendrogram_ratio,
                                    col_colors_ratio)

    nrows = 2 if self.col_colors is None else 3
    ncols = 2 if self.row_colors is None else 3

    self.gs = gridspec.GridSpec(nrows, ncols,
                                width_ratios=width_ratios,
                                height_ratios=height_ratios)

    self.ax_row_dendrogram = self._figure.add_subplot(self.gs[-1, 0])
    self.ax_col_dendrogram = self._figure.add_subplot(self.gs[0, -1])
    self.ax_row_dendrogram.set_axis_off()
    self.ax_col_dendrogram.set_axis_off()

    self.ax_row_colors = None
    self.ax_col_colors = None

    if self.row_colors is not None:
        self.ax_row_colors = self._figure.add_subplot(
            self.gs[-1, 1])
    if self.col_colors is not None:
        self.ax_col_colors = self._figure.add_subplot(
            self.gs[1, -1])

    self.ax_heatmap = self._figure.add_subplot(self.gs[-1, -1])
    if cbar_pos is None:
        self.ax_cbar = self.cax = None
    else:
        # Initialize the colorbar axes in the gridspec so that tight_layout
        # works. We will move it where it belongs later. This is a hack.
        self.ax_cbar = self._figure.add_subplot(self.gs[0, 0])
        self.cax = self.ax_cbar  # Backwards compatibility
    self.cbar_pos = cbar_pos

    self.dendrogram_row = None
    self.dendrogram_col = None


# ==================================================
# Line: 970

def plot_dendrograms(self, row_cluster, col_cluster, metric, method,
                     row_linkage, col_linkage, tree_kws):
    # Plot the row dendrogram
    if row_cluster:
        self.dendrogram_row = dendrogram(
            self.data2d, metric=metric, method=method, label=False, axis=0,
            ax=self.ax_row_dendrogram, rotate=True, linkage=row_linkage,
            tree_kws=tree_kws
        )
    else:
        self.ax_row_dendrogram.set_xticks([])
        self.ax_row_dendrogram.set_yticks([])
    # PLot the column dendrogram
    if col_cluster:
        self.dendrogram_col = dendrogram(
            self.data2d, metric=metric, method=method, label=False,
            axis=1, ax=self.ax_col_dendrogram, linkage=col_linkage,
            tree_kws=tree_kws
        )
    else:
        self.ax_col_dendrogram.set_xticks([])
        self.ax_col_dendrogram.set_yticks([])
    despine(ax=self.ax_row_dendrogram, bottom=True, left=True)
    despine(ax=self.ax_col_dendrogram, bottom=True, left=True)


# ==================================================
# Line: 1117

def plot(self, metric, method, colorbar_kws, row_cluster, col_cluster,
         row_linkage, col_linkage, tree_kws, **kws):

    # heatmap square=True sets the aspect ratio on the axes, but that is
    # not compatible with the multi-axes layout of clustergrid
    if kws.get("square", False):
        msg = "``square=True`` ignored in clustermap"
        warnings.warn(msg)
        kws.pop("square")

    colorbar_kws = {} if colorbar_kws is None else colorbar_kws

    self.plot_dendrograms(row_cluster, col_cluster, metric, method,
                          row_linkage=row_linkage, col_linkage=col_linkage,
                          tree_kws=tree_kws)
    try:
        xind = self.dendrogram_col.reordered_ind
    except AttributeError:
        xind = np.arange(self.data2d.shape[1])
    try:
        yind = self.dendrogram_row.reordered_ind
    except AttributeError:
        yind = np.arange(self.data2d.shape[0])

    self.plot_colors(xind, yind, **kws)
    self.plot_matrix(colorbar_kws, xind, yind, **kws)
    return self



# ==================================================
# Line: 1146

def clustermap(
    data, *,
    pivot_kws=None, method='average', metric='euclidean',
    z_score=None, standard_scale=None, figsize=(10, 10),
    cbar_kws=None, row_cluster=True, col_cluster=True,
    row_linkage=None, col_linkage=None,
    row_colors=None, col_colors=None, mask=None,
    dendrogram_ratio=.2, colors_ratio=0.03,
    cbar_pos=(.02, .8, .05, .18), tree_kws=None,
    **kwargs

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/widgets.py
# Line: 346

def choose_diverging_palette(
    h_neg=IntSlider(min=0,
                    max=359,
                    value=220),
    h_pos=IntSlider(min=0,
                    max=359,
                    value=10),
    s=IntSlider(min=0, max=99, value=74),
    l=IntSlider(min=0, max=99, value=50),  # noqa: E741
    sep=IntSlider(min=1, max=50, value=10),
    n=(2, 16),
    center=["light", "dark"]

# ==================================================
# Line: 405

def choose_cubehelix(n_colors=IntSlider(min=2, max=16, value=9),
                     start=FloatSlider(min=0, max=3, value=0),
                     rot=FloatSlider(min=-1, max=1, value=.4),
                     gamma=FloatSlider(min=0, max=5, value=1),
                     hue=FloatSlider(min=0, max=1, value=.8),
                     light=FloatSlider(min=0, max=1, value=.85),
                     dark=FloatSlider(min=0, max=1, value=.15),
                     reverse=False):

    if as_cmap:
        colors = cubehelix_palette(256, start, rot, gamma,
                                   hue, light, dark, reverse)
        _update_lut(cmap, np.c_[colors, np.ones(256)])
        _show_cmap(cmap)
    else:
        pal[:] = cubehelix_palette(n_colors, start, rot, gamma,
                                   hue, light, dark, reverse)
        palplot(pal)


# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/relational.py
# Line: 202

def __init__(
    self, *,
    data=None, variables={},
    estimator=None, n_boot=None, seed=None, errorbar=None,
    sort=True, orient="x", err_style=None, err_kws=None, legend=None

# ==================================================
# Line: 471

def lineplot(
    data=None, *,
    x=None, y=None, hue=None, size=None, style=None, units=None, weights=None,
    palette=None, hue_order=None, hue_norm=None,
    sizes=None, size_order=None, size_norm=None,
    dashes=True, markers=None, style_order=None,
    estimator="mean", errorbar=("ci", 95), n_boot=1000, seed=None,
    orient="x", sort=True, err_style="band", err_kws=None,
    legend="auto", ci="deprecated", ax=None, **kwargs

# ==================================================
# Line: 606

def scatterplot(
    data=None, *,
    x=None, y=None, hue=None, size=None, style=None,
    palette=None, hue_order=None, hue_norm=None,
    sizes=None, size_order=None, size_norm=None,
    markers=True, style_order=None, legend="auto", ax=None,
    **kwargs

# ==================================================
# Line: 700

def relplot(
    data=None, *,
    x=None, y=None, hue=None, size=None, style=None, units=None, weights=None,
    row=None, col=None, col_wrap=None, row_order=None, col_order=None,
    palette=None, hue_order=None, hue_norm=None,
    sizes=None, size_order=None, size_norm=None,
    markers=None, dashes=None, style_order=None,
    legend="auto", kind="scatter", height=5, aspect=1, facet_kws=None,
    **kwargs

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_statistics.py
# Line: 44

def __init__(
    self, *,
    bw_method=None,
    bw_adjust=1,
    gridsize=200,
    cut=3,
    clip=None,
    cumulative=False,

# ==================================================
# Line: 202

def __init__(
    self,
    stat="count",
    bins="auto",
    binwidth=None,
    binrange=None,
    discrete=False,
    cumulative=False,

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
# Line: 135

def _add_legend(
    self,
    ax_obj, artist, fill, element, multiple, alpha, artist_kws, legend_kws,

# ==================================================
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
# Line: 376

def plot_univariate_histogram(
    self,
    multiple,
    element,
    fill,
    common_norm,
    common_bins,
    shrink,
    kde,
    kde_kws,
    color,
    legend,
    line_kws,
    estimate_kws,
    **plot_kws,

# ==================================================
# Line: 740

def plot_bivariate_histogram(
    self,
    common_bins, common_norm,
    thresh, pthresh, pmax,
    color, legend,
    cbar, cbar_ax, cbar_kws,
    estimate_kws,
    **plot_kws,

# ==================================================
# Line: 897

def plot_univariate_density(
    self,
    multiple,
    common_norm,
    common_grid,
    warn_singular,
    fill,
    color,
    legend,
    estimate_kws,
    **plot_kws,

# ==================================================
# Line: 1028

def plot_bivariate_density(
    self,
    common_norm,
    fill,
    levels,
    thresh,
    color,
    legend,
    cbar,
    warn_singular,
    cbar_ax,
    cbar_kws,
    estimate_kws,
    **contour_kws,

# ==================================================
# Line: 1358

def histplot(
    data=None, *,
    # Vector variables
    x=None, y=None, hue=None, weights=None,
    # Histogram computation parameters
    stat="count", bins="auto", binwidth=None, binrange=None,
    discrete=None, cumulative=False, common_bins=True, common_norm=True,
    # Histogram appearance parameters
    multiple="layer", element="bars", fill=True, shrink=1,
    # Histogram smoothing with a kernel density estimate
    kde=False, kde_kws=None, line_kws=None,
    # Bivariate histogram parameters
    thresh=0, pthresh=None, pmax=None, cbar=False, cbar_ax=None, cbar_kws=None,
    # Hue mapping parameters
    palette=None, hue_order=None, hue_norm=None, color=None,
    # Axes information
    log_scale=None, legend=True, ax=None,
    # Other appearance keywords
    **kwargs,

# ==================================================
# Line: 1581

def kdeplot(
    data=None, *, x=None, y=None, hue=None, weights=None,
    palette=None, hue_order=None, hue_norm=None, color=None, fill=None,
    multiple="layer", common_norm=True, common_grid=False, cumulative=False,
    bw_method="scott", bw_adjust=1, warn_singular=True, log_scale=None,
    levels=10, thresh=.05, gridsize=200, cut=3, clip=None,
    legend=True, cbar=False, cbar_ax=None, cbar_kws=None, ax=None,
    **kwargs,

# ==================================================
# Line: 1861

def ecdfplot(
    data=None, *,
    # Vector variables
    x=None, y=None, hue=None, weights=None,
    # Computation parameters
    stat="proportion", complementary=False,
    # Hue mapping parameters
    palette=None, hue_order=None, hue_norm=None,
    # Axes information
    log_scale=None, legend=True, ax=None,
    # Other appearance keywords
    **kwargs,

# ==================================================
# Line: 1973

def rugplot(
    data=None, *, x=None, y=None, hue=None, height=.025, expand_margins=True,
    palette=None, hue_order=None, hue_norm=None, legend=True, ax=None, **kwargs

# ==================================================
# Line: 2094

def displot(
    data=None, *,
    # Vector variables
    x=None, y=None, hue=None, row=None, col=None, weights=None,
    # Other plot parameters
    kind="hist", rug=False, rug_kws=None, log_scale=None, legend=True,
    # Hue-mapping parameters
    palette=None, hue_order=None, hue_norm=None, color=None,
    # Faceting parameters
    col_wrap=None, row_order=None, col_order=None,
    height=5, aspect=1, facet_kws=None,
    **kwargs,

# ==================================================
# Line: 2390

def distplot(a=None, bins=None, hist=True, kde=True, rug=False, fit=None,
             hist_kws=None, kde_kws=None, rug_kws=None, fit_kws=None,
             color=None, vertical=False, norm_hist=False, axlabel=None,
             label=None, ax=None, x=None):
    """
    DEPRECATED

    This function has been deprecated and will be removed in seaborn v0.14.0.
    It has been replaced by :func:`histplot` and :func:`displot`, two functions
    with a modern API and many more capabilities.

    For a guide to updating, please see this notebook:

    https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

    """

    if kde and not hist:
        axes_level_suggestion = (
            "`kdeplot` (an axes-level function for kernel density plots)"
        )
    else:
        axes_level_suggestion = (
            "`histplot` (an axes-level function for histograms)"
        )

    msg = textwrap.dedent(f"""

    `distplot` is a deprecated function and will be removed in seaborn v0.14.0.

    Please adapt your code to use either `displot` (a figure-level function with
    similar flexibility) or {axes_level_suggestion}.

    For a guide to updating your code to use the new functions, please see
    https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751
    """)
    warnings.warn(msg, UserWarning, stacklevel=2)

    if ax is None:
        ax = plt.gca()

    # Intelligently label the support axis
    label_ax = bool(axlabel)
    if axlabel is None and hasattr(a, "name"):
        axlabel = a.name
        if axlabel is not None:
            label_ax = True

    # Support new-style API
    if x is not None:
        a = x

    # Make a a 1-d float array
    a = np.asarray(a, float)
    if a.ndim > 1:
        a = a.squeeze()

    # Drop null values from array
    a = remove_na(a)

    # Decide if the hist is normed
    norm_hist = norm_hist or kde or (fit is not None)

    # Handle dictionary defaults
    hist_kws = {} if hist_kws is None else hist_kws.copy()
    kde_kws = {} if kde_kws is None else kde_kws.copy()
    rug_kws = {} if rug_kws is None else rug_kws.copy()
    fit_kws = {} if fit_kws is None else fit_kws.copy()

    # Get the color from the current color cycle
    if color is None:
        if vertical:
            line, = ax.plot(0, a.mean())
        else:
            line, = ax.plot(a.mean(), 0)
        color = line.get_color()
        line.remove()

    # Plug the label into the right kwarg dictionary
    if label is not None:
        if hist:
            hist_kws["label"] = label
        elif kde:
            kde_kws["label"] = label
        elif rug:
            rug_kws["label"] = label
        elif fit:
            fit_kws["label"] = label

    if hist:
        if bins is None:
            bins = min(_freedman_diaconis_bins(a), 50)
        hist_kws.setdefault("alpha", 0.4)
        hist_kws.setdefault("density", norm_hist)

        orientation = "horizontal" if vertical else "vertical"
        hist_color = hist_kws.pop("color", color)
        ax.hist(a, bins, orientation=orientation,
                color=hist_color, **hist_kws)
        if hist_color != color:
            hist_kws["color"] = hist_color

    axis = "y" if vertical else "x"

    if kde:
        kde_color = kde_kws.pop("color", color)
        kdeplot(**{axis: a}, ax=ax, color=kde_color, **kde_kws)
        if kde_color != color:
            kde_kws["color"] = kde_color

    if rug:
        rug_color = rug_kws.pop("color", color)
        rugplot(**{axis: a}, ax=ax, color=rug_color, **rug_kws)
        if rug_color != color:
            rug_kws["color"] = rug_color

    if fit is not None:

        def pdf(x):
            return fit.pdf(x, *params)

        fit_color = fit_kws.pop("color", "#282828")
        gridsize = fit_kws.pop("gridsize", 200)
        cut = fit_kws.pop("cut", 3)
        clip = fit_kws.pop("clip", (-np.inf, np.inf))
        bw = gaussian_kde(a).scotts_factor() * a.std(ddof=1)
        x = _kde_support(a, bw, gridsize, cut, clip)
        params = fit.fit(a)
        y = pdf(x)
        if vertical:
            x, y = y, x
        ax.plot(x, y, color=fit_color, **fit_kws)
        if fit_color != "#282828":
            fit_kws["color"] = fit_color

    if label_ax:
        if vertical:
            ax.set_ylabel(axlabel)
        else:
            ax.set_xlabel(axlabel)

    return ax

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/axisgrid.py
# Line: 371

def __init__(
    self, data, *,
    row=None, col=None, hue=None, col_wrap=None,
    sharex=True, sharey=True, height=3, aspect=1, palette=None,
    row_order=None, col_order=None, hue_order=None, hue_kws=None,
    dropna=False, legend_out=True, despine=True,
    margin_titles=False, xlim=None, ylim=None, subplot_kws=None,
    gridspec_kws=None,

# ==================================================
# Line: 1191

def __init__(
    self, data, *, hue=None, vars=None, x_vars=None, y_vars=None,
    hue_order=None, palette=None, hue_kws=None, corner=False, diag_sharey=True,
    height=2.5, aspect=1, layout_pad=.5, despine=True, dropna=False,

# ==================================================
# Line: 1687

def __init__(
    self, data=None, *,
    x=None, y=None, hue=None,
    height=6, ratio=5, space=.2,
    palette=None, hue_order=None, hue_norm=None,
    dropna=False, xlim=None, ylim=None, marginal_ticks=False,

# ==================================================
# Line: 1899

def refline(
    self, *, x=None, y=None, joint=True, marginal=True,
    color='.5', linestyle='--', **line_kws

# ==================================================
# Line: 2010

def pairplot(
    data, *,
    hue=None, hue_order=None, palette=None,
    vars=None, x_vars=None, y_vars=None,
    kind="scatter", diag_kind="auto", markers=None,
    height=2.5, aspect=1, corner=False, dropna=False,
    plot_kws=None, diag_kws=None, grid_kws=None, size=None,

# ==================================================
# Line: 2184

def jointplot(
    data=None, *, x=None, y=None, hue=None, kind="scatter",
    height=6, ratio=5, space=.2, dropna=False, xlim=None, ylim=None,
    color=None, palette=None, hue_order=None, hue_norm=None, marginal_ticks=False,
    joint_kws=None, marginal_kws=None,
    **kwargs

# ==================================================
