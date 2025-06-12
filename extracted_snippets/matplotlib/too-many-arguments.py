# too-many-arguments snippets for matplotlib

# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/grid_finder.py
# Line: 135

def __init__(self,
             transform,
             extreme_finder=None,
             grid_locator1=None,
             grid_locator2=None,
             tick_formatter1=None,
             tick_formatter2=None):
    if extreme_finder is None:
        extreme_finder = ExtremeFinderSimple(20, 20)
    if grid_locator1 is None:
        grid_locator1 = MaxNLocator()
    if grid_locator2 is None:
        grid_locator2 = MaxNLocator()
    if tick_formatter1 is None:
        tick_formatter1 = FormatterPrettyPrint()
    if tick_formatter2 is None:
        tick_formatter2 = FormatterPrettyPrint()
    self.extreme_finder = extreme_finder
    self.grid_locator1 = grid_locator1
    self.grid_locator2 = grid_locator2
    self.tick_formatter1 = tick_formatter1
    self.tick_formatter2 = tick_formatter2
    self.set_transform(transform)


# ==================================================
# Line: 261

def __init__(self, nbins=10, steps=None,
             trim=True,
             integer=False,
             symmetric=False,
             prune=None):
    # trim argument has no effect. It has been left for API compatibility
    super().__init__(nbins, steps=steps, integer=integer,
                     symmetric=symmetric, prune=prune)
    self.create_dummy_axis()


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/floating_axes.py
# Line: 130

def __init__(self, aux_trans, extremes,
             grid_locator1=None,
             grid_locator2=None,
             tick_formatter1=None,
             tick_formatter2=None):
    # docstring inherited
    super().__init__(aux_trans,
                     extreme_finder=ExtremeFinderFixed(extremes),
                     grid_locator1=grid_locator1,
                     grid_locator2=grid_locator2,
                     tick_formatter1=tick_formatter1,
                     tick_formatter2=tick_formatter2)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/grid_helper_curvelinear.py
# Line: 277

def __init__(self, aux_trans,
             extreme_finder=None,
             grid_locator1=None,
             grid_locator2=None,
             tick_formatter1=None,
             tick_formatter2=None):
    """
    Parameters
    ----------
    aux_trans : `.Transform` or tuple[Callable, Callable]
        The transform from curved coordinates to rectilinear coordinate:
        either a `.Transform` instance (which provides also its inverse),
        or a pair of callables ``(trans, inv_trans)`` that define the
        transform and its inverse.  The callables should have signature::

            x_rect, y_rect = trans(x_curved, y_curved)
            x_curved, y_curved = inv_trans(x_rect, y_rect)

    extreme_finder

    grid_locator1, grid_locator2
        Grid locators for each axis.

    tick_formatter1, tick_formatter2
        Tick formatters for each axis.
    """
    super().__init__()
    self._grid_info = None
    self.grid_finder = GridFinder(aux_trans,
                                  extreme_finder,
                                  grid_locator1,
                                  grid_locator2,
                                  tick_formatter1,
                                  tick_formatter2)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/angle_helper.py
# Line: 314

def __init__(self, nx, ny,
             lon_cycle=360., lat_cycle=None,
             lon_minmax=None, lat_minmax=(-90, 90)):
    """
    This subclass handles the case where one or both coordinates should be
    taken modulo 360, or be restricted to not exceed a specific range.

    Parameters
    ----------
    nx, ny : int
        The number of samples in each direction.

    lon_cycle, lat_cycle : 360 or None
        If not None, values in the corresponding direction are taken modulo
        *lon_cycle* or *lat_cycle*; in theory this can be any number but
        the implementation actually assumes that it is 360 (if not None);
        other values give nonsensical results.

        This is done by "unwrapping" the transformed grid coordinates so
        that jumps are less than a half-cycle; then normalizing the span to
        no more than a full cycle.

        For example, if values are in the union of the [0, 2] and
        [358, 360] intervals (typically, angles measured modulo 360), the
        values in the second interval are normalized to [-2, 0] instead so
        that the values now cover [-2, 2].  If values are in a range of
        [5, 1000], this gets normalized to [5, 365].

    lon_minmax, lat_minmax : (float, float) or None
        If not None, the computed bounding box is clipped to the given
        range in the corresponding direction.
    """
    self.nx, self.ny = nx, ny
    self.lon_cycle, self.lat_cycle = lon_cycle, lat_cycle
    self.lon_minmax = lon_minmax
    self.lat_minmax = lat_minmax


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/mplot3d/axis3d.py
# Line: 436

def _draw_ticks(self, renderer, edgep1, centers, deltas, highs,
                deltas_per_point, pos):
    ticks = self._update_ticks()
    info = self._axinfo
    index = info["i"]
    juggled = info["juggled"]

    mins, maxs, tc, highs = self._get_coord_info()
    centers, deltas = self._calc_centers_deltas(maxs, mins)

    # Draw ticks:
    tickdir = self._get_tickdir(pos)
    tickdelta = deltas[tickdir] if highs[tickdir] else -deltas[tickdir]

    tick_info = info['tick']
    tick_out = tick_info['outward_factor'] * tickdelta
    tick_in = tick_info['inward_factor'] * tickdelta
    tick_lw = tick_info['linewidth']
    edgep1_tickdir = edgep1[tickdir]
    out_tickdir = edgep1_tickdir + tick_out
    in_tickdir = edgep1_tickdir - tick_in

    default_label_offset = 8.  # A rough estimate
    points = deltas_per_point * deltas
    for tick in ticks:
        # Get tick line positions
        pos = edgep1.copy()
        pos[index] = tick.get_loc()
        pos[tickdir] = out_tickdir
        x1, y1, z1 = proj3d.proj_transform(*pos, self.axes.M)
        pos[tickdir] = in_tickdir
        x2, y2, z2 = proj3d.proj_transform(*pos, self.axes.M)

        # Get position of label
        labeldeltas = (tick.get_pad() + default_label_offset) * points

        pos[tickdir] = edgep1_tickdir
        pos = _move_from_center(pos, centers, labeldeltas, self._axmask())
        lx, ly, lz = proj3d.proj_transform(*pos, self.axes.M)

        _tick_update_position(tick, (x1, x2), (y1, y2), (lx, ly))
        tick.tick1line.set_linewidth(tick_lw[tick._major])
        tick.draw(renderer)


# ==================================================
# Line: 480

def _draw_offset_text(self, renderer, edgep1, edgep2, labeldeltas, centers,
                      highs, pep, dx, dy):
    # Get general axis information:
    info = self._axinfo
    index = info["i"]
    juggled = info["juggled"]
    tickdir = info["tickdir"]

    # Which of the two edge points do we want to
    # use for locating the offset text?
    if juggled[2] == 2:
        outeredgep = edgep1
        outerindex = 0
    else:
        outeredgep = edgep2
        outerindex = 1

    pos = _move_from_center(outeredgep, centers, labeldeltas,
                            self._axmask())
    olx, oly, olz = proj3d.proj_transform(*pos, self.axes.M)
    self.offsetText.set_text(self.major.formatter.get_offset())
    self.offsetText.set_position((olx, oly))
    angle = art3d._norm_text_angle(np.rad2deg(np.arctan2(dy, dx)))
    self.offsetText.set_rotation(angle)
    # Must set rotation mode to "anchor" so that
    # the alignment point is used as the "fulcrum" for rotation.
    self.offsetText.set_rotation_mode('anchor')

    # ----------------------------------------------------------------------
    # Note: the following statement for determining the proper alignment of
    # the offset text. This was determined entirely by trial-and-error
    # and should not be in any way considered as "the way".  There are
    # still some edge cases where alignment is not quite right, but this
    # seems to be more of a geometry issue (in other words, I might be
    # using the wrong reference points).
    #
    # (TT, FF, TF, FT) are the shorthand for the tuple of
    #   (centpt[tickdir] <= pep[tickdir, outerindex],
    #    centpt[index] <= pep[index, outerindex])
    #
    # Three-letters (e.g., TFT, FTT) are short-hand for the array of bools
    # from the variable 'highs'.
    # ---------------------------------------------------------------------
    centpt = proj3d.proj_transform(*centers, self.axes.M)
    if centpt[tickdir] > pep[tickdir, outerindex]:
        # if FT and if highs has an even number of Trues
        if (centpt[index] <= pep[index, outerindex]
                and np.count_nonzero(highs) % 2 == 0):
            # Usually, this means align right, except for the FTT case,
            # in which offset for axis 1 and 2 are aligned left.
            if highs.tolist() == [False, True, True] and index in (1, 2):
                align = 'left'
            else:
                align = 'right'
        else:
            # The FF case
            align = 'left'
    else:
        # if TF and if highs has an even number of Trues
        if (centpt[index] > pep[index, outerindex]
                and np.count_nonzero(highs) % 2 == 0):
            # Usually mean align left, except if it is axis 2
            align = 'right' if index == 2 else 'left'
        else:
            # The TT case
            align = 'right'

    self.offsetText.set_va('center')
    self.offsetText.set_ha(align)
    self.offsetText.draw(renderer)


# ==================================================
# Line: 551

def _draw_labels(self, renderer, edgep1, edgep2, labeldeltas, centers, dx, dy):
    label = self._axinfo["label"]

    # Draw labels
    lxyz = 0.5 * (edgep1 + edgep2)
    lxyz = _move_from_center(lxyz, centers, labeldeltas, self._axmask())
    tlx, tly, tlz = proj3d.proj_transform(*lxyz, self.axes.M)
    self.label.set_position((tlx, tly))
    if self.get_rotate_label(self.label.get_text()):
        angle = art3d._norm_text_angle(np.rad2deg(np.arctan2(dy, dx)))
        self.label.set_rotation(angle)
    self.label.set_va(label['va'])
    self.label.set_ha(label['ha'])
    self.label.set_rotation_mode(label['rotation_mode'])
    self.label.draw(renderer)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/mplot3d/art3d.py
# Line: 124

def __init__(self, x=0, y=0, z=0, text='', zdir='z', axlim_clip=False,
             **kwargs):
    mtext.Text.__init__(self, x, y, text, **kwargs)
    self.set_3d_properties(z, zdir, axlim_clip)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/mplot3d/axes3d.py
# Line: 60

def __init__(
    self, fig, rect=None, *args,
    elev=30, azim=-60, roll=0, shareview=None, sharez=None,
    proj_type='persp', focal_length=None,
    box_aspect=None,
    computed_zorder=True,
    **kwargs,

# ==================================================
# Line: 677

def _set_bound3d(self, get_bound, set_lim, axis_inverted,
                 lower=None, upper=None, view_margin=None):
    """
    Set 3D axis bounds.
    """
    if upper is None and np.iterable(lower):
        lower, upper = lower

    old_lower, old_upper = get_bound()
    if lower is None:
        lower = old_lower
    if upper is None:
        upper = old_upper

    set_lim(sorted((lower, upper), reverse=bool(axis_inverted())),
            auto=None, view_margin=view_margin)


# ==================================================
# Line: 768

def _set_lim3d(self, axis, lower=None, upper=None, *, emit=True,
               auto=False, view_margin=None, axmin=None, axmax=None):
    """
    Set 3D axis limits.
    """
    if upper is None:
        if np.iterable(lower):
            lower, upper = lower
        elif axmax is None:
            upper = axis.get_view_interval()[1]
    if lower is None and axmin is None:
        lower = axis.get_view_interval()[0]
    if axmin is not None:
        if lower is not None:
            raise TypeError("Cannot pass both 'lower' and 'min'")
        lower = axmin
    if axmax is not None:
        if upper is not None:
            raise TypeError("Cannot pass both 'upper' and 'max'")
        upper = axmax
    if np.isinf(lower) or np.isinf(upper):
        raise ValueError(f"Axis limits {lower}, {upper} cannot be infinite")
    if view_margin is None:
        if mpl.rcParams['axes3d.automargin']:
            view_margin = self._view_margin
        else:
            view_margin = 0
    delta = (upper - lower) * view_margin
    lower -= delta
    upper += delta
    return axis._set_lim(lower, upper, emit=emit, auto=auto)


# ==================================================
# Line: 800

def set_xlim(self, left=None, right=None, *, emit=True, auto=False,
             view_margin=None, xmin=None, xmax=None):
    """
    Set the 3D x-axis view limits.

    Parameters
    ----------
    left : float, optional
        The left xlim in data coordinates. Passing *None* leaves the
        limit unchanged.

        The left and right xlims may also be passed as the tuple
        (*left*, *right*) as the first positional argument (or as
        the *left* keyword argument).

        .. ACCEPTS: (left: float, right: float)

    right : float, optional
        The right xlim in data coordinates. Passing *None* leaves the
        limit unchanged.

    emit : bool, default: True
        Whether to notify observers of limit change.

    auto : bool or None, default: False
        Whether to turn on autoscaling of the x-axis. *True* turns on,
        *False* turns off, *None* leaves unchanged.

    view_margin : float, optional
        The additional margin to apply to the limits.

    xmin, xmax : float, optional
        They are equivalent to left and right respectively, and it is an
        error to pass both *xmin* and *left* or *xmax* and *right*.

    Returns
    -------
    left, right : (float, float)
        The new x-axis limits in data coordinates.

    See Also
    --------
    get_xlim
    set_xbound, get_xbound
    invert_xaxis, xaxis_inverted

    Notes
    -----
    The *left* value may be greater than the *right* value, in which
    case the x-axis values will decrease from *left* to *right*.

    Examples
    --------
    >>> set_xlim(left, right)
    >>> set_xlim((left, right))
    >>> left, right = set_xlim(left, right)

    One limit may be left unchanged.

    >>> set_xlim(right=right_lim)

    Limits may be passed in reverse order to flip the direction of
    the x-axis. For example, suppose ``x`` represents depth of the
    ocean in m. The x-axis limits might be set like the following
    so 5000 m depth is at the left of the plot and the surface,
    0 m, is at the right.

    >>> set_xlim(5000, 0)
    """
    return self._set_lim3d(self.xaxis, left, right, emit=emit, auto=auto,
                           view_margin=view_margin, axmin=xmin, axmax=xmax)


# ==================================================
# Line: 872

def set_ylim(self, bottom=None, top=None, *, emit=True, auto=False,
             view_margin=None, ymin=None, ymax=None):
    """
    Set the 3D y-axis view limits.

    Parameters
    ----------
    bottom : float, optional
        The bottom ylim in data coordinates. Passing *None* leaves the
        limit unchanged.

        The bottom and top ylims may also be passed as the tuple
        (*bottom*, *top*) as the first positional argument (or as
        the *bottom* keyword argument).

        .. ACCEPTS: (bottom: float, top: float)

    top : float, optional
        The top ylim in data coordinates. Passing *None* leaves the
        limit unchanged.

    emit : bool, default: True
        Whether to notify observers of limit change.

    auto : bool or None, default: False
        Whether to turn on autoscaling of the y-axis. *True* turns on,
        *False* turns off, *None* leaves unchanged.

    view_margin : float, optional
        The additional margin to apply to the limits.

    ymin, ymax : float, optional
        They are equivalent to bottom and top respectively, and it is an
        error to pass both *ymin* and *bottom* or *ymax* and *top*.

    Returns
    -------
    bottom, top : (float, float)
        The new y-axis limits in data coordinates.

    See Also
    --------
    get_ylim
    set_ybound, get_ybound
    invert_yaxis, yaxis_inverted

    Notes
    -----
    The *bottom* value may be greater than the *top* value, in which
    case the y-axis values will decrease from *bottom* to *top*.

    Examples
    --------
    >>> set_ylim(bottom, top)
    >>> set_ylim((bottom, top))
    >>> bottom, top = set_ylim(bottom, top)

    One limit may be left unchanged.

    >>> set_ylim(top=top_lim)

    Limits may be passed in reverse order to flip the direction of
    the y-axis. For example, suppose ``y`` represents depth of the
    ocean in m. The y-axis limits might be set like the following
    so 5000 m depth is at the bottom of the plot and the surface,
    0 m, is at the top.

    >>> set_ylim(5000, 0)
    """
    return self._set_lim3d(self.yaxis, bottom, top, emit=emit, auto=auto,
                           view_margin=view_margin, axmin=ymin, axmax=ymax)


# ==================================================
# Line: 944

def set_zlim(self, bottom=None, top=None, *, emit=True, auto=False,
             view_margin=None, zmin=None, zmax=None):
    """
    Set the 3D z-axis view limits.

    Parameters
    ----------
    bottom : float, optional
        The bottom zlim in data coordinates. Passing *None* leaves the
        limit unchanged.

        The bottom and top zlims may also be passed as the tuple
        (*bottom*, *top*) as the first positional argument (or as
        the *bottom* keyword argument).

        .. ACCEPTS: (bottom: float, top: float)

    top : float, optional
        The top zlim in data coordinates. Passing *None* leaves the
        limit unchanged.

    emit : bool, default: True
        Whether to notify observers of limit change.

    auto : bool or None, default: False
        Whether to turn on autoscaling of the z-axis. *True* turns on,
        *False* turns off, *None* leaves unchanged.

    view_margin : float, optional
        The additional margin to apply to the limits.

    zmin, zmax : float, optional
        They are equivalent to bottom and top respectively, and it is an
        error to pass both *zmin* and *bottom* or *zmax* and *top*.

    Returns
    -------
    bottom, top : (float, float)
        The new z-axis limits in data coordinates.

    See Also
    --------
    get_zlim
    set_zbound, get_zbound
    invert_zaxis, zaxis_inverted

    Notes
    -----
    The *bottom* value may be greater than the *top* value, in which
    case the z-axis values will decrease from *bottom* to *top*.

    Examples
    --------
    >>> set_zlim(bottom, top)
    >>> set_zlim((bottom, top))
    >>> bottom, top = set_zlim(bottom, top)

    One limit may be left unchanged.

    >>> set_zlim(top=top_lim)

    Limits may be passed in reverse order to flip the direction of
    the z-axis. For example, suppose ``z`` represents depth of the
    ocean in m. The z-axis limits might be set like the following
    so 5000 m depth is at the bottom of the plot and the surface,
    0 m, is at the top.

    >>> set_zlim(5000, 0)
    """
    return self._set_lim3d(self.zaxis, bottom, top, emit=emit, auto=auto,
                           view_margin=view_margin, axmin=zmin, axmax=zmax)


# ==================================================
# Line: 1934

def text(self, x, y, z, s, zdir=None, *, axlim_clip=False, **kwargs):
    """
    Add the text *s* to the 3D Axes at location *x*, *y*, *z* in data coordinates.

    Parameters
    ----------
    x, y, z : float
        The position to place the text.
    s : str
        The text.
    zdir : {'x', 'y', 'z', 3-tuple}, optional
        The direction to be used as the z-direction. Default: 'z'.
        See `.get_dir_vector` for a description of the values.
    axlim_clip : bool, default: False
        Whether to hide text that is outside the axes view limits.

        .. versionadded:: 3.10
    **kwargs
        Other arguments are forwarded to `matplotlib.axes.Axes.text`.

    Returns
    -------
    `.Text3D`
        The created `.Text3D` instance.
    """
    text = super().text(x, y, s, **kwargs)
    art3d.text_2d_to_3d(text, z, zdir, axlim_clip)
    return text


# ==================================================
# Line: 2012

def fill_between(self, x1, y1, z1, x2, y2, z2, *,
                 where=None, mode='auto', facecolors=None, shade=None,
                 axlim_clip=False, **kwargs):
    """
    Fill the area between two 3D curves.

    The curves are defined by the points (*x1*, *y1*, *z1*) and
    (*x2*, *y2*, *z2*). This creates one or multiple quadrangle
    polygons that are filled. All points must be the same length N, or a
    single value to be used for all points.

    Parameters
    ----------
    x1, y1, z1 : float or 1D array-like
        x, y, and z  coordinates of vertices for 1st line.

    x2, y2, z2 : float or 1D array-like
        x, y, and z coordinates of vertices for 2nd line.

    where : array of bool (length N), optional
        Define *where* to exclude some regions from being filled. The
        filled regions are defined by the coordinates ``pts[where]``,
        for all x, y, and z pts. More precisely, fill between ``pts[i]``
        and ``pts[i+1]`` if ``where[i] and where[i+1]``. Note that this
        definition implies that an isolated *True* value between two
        *False* values in *where* will not result in filling. Both sides of
        the *True* position remain unfilled due to the adjacent *False*
        values.

    mode : {'quad', 'polygon', 'auto'}, default: 'auto'
        The fill mode. One of:

        - 'quad':  A separate quadrilateral polygon is created for each
          pair of subsequent points in the two lines.
        - 'polygon': The two lines are connected to form a single polygon.
          This is faster and can render more cleanly for simple shapes
          (e.g. for filling between two lines that lie within a plane).
        - 'auto': If the points all lie on the same 3D plane, 'polygon' is
          used. Otherwise, 'quad' is used.

    facecolors : list of :mpltype:`color`, default: None
        Colors of each individual patch, or a single color to be used for
        all patches.

    shade : bool, default: None
        Whether to shade the facecolors. If *None*, then defaults to *True*
        for 'quad' mode and *False* for 'polygon' mode.

    axlim_clip : bool, default: False
        Whether to hide data that is outside the axes view limits.

        .. versionadded:: 3.10

    **kwargs
        All other keyword arguments are passed on to `.Poly3DCollection`.

    Returns
    -------
    `.Poly3DCollection`
        A `.Poly3DCollection` containing the plotted polygons.

    """
    _api.check_in_list(['auto', 'quad', 'polygon'], mode=mode)

    had_data = self.has_data()
    x1, y1, z1, x2, y2, z2 = cbook._broadcast_with_masks(x1, y1, z1, x2, y2, z2)

    if facecolors is None:
        facecolors = [self._get_patches_for_fill.get_next_color()]
    facecolors = list(mcolors.to_rgba_array(facecolors))

    if where is None:
        where = True
    else:
        where = np.asarray(where, dtype=bool)
        if where.size != x1.size:
            raise ValueError(f"where size ({where.size}) does not match "
                             f"size ({x1.size})")
    where = where & ~np.isnan(x1)  # NaNs were broadcast in _broadcast_with_masks

    if mode == 'auto':
        if art3d._all_points_on_plane(np.concatenate((x1[where], x2[where])),
                                      np.concatenate((y1[where], y2[where])),
                                      np.concatenate((z1[where], z2[where])),
                                      atol=1e-12):
            mode = 'polygon'
        else:
            mode = 'quad'

    if shade is None:
        if mode == 'quad':
            shade = True
        else:
            shade = False

    polys = []
    for idx0, idx1 in cbook.contiguous_regions(where):
        x1i = x1[idx0:idx1]
        y1i = y1[idx0:idx1]
        z1i = z1[idx0:idx1]
        x2i = x2[idx0:idx1]
        y2i = y2[idx0:idx1]
        z2i = z2[idx0:idx1]

        if not len(x1i):
            continue

        if mode == 'quad':
            # Preallocate the array for the region's vertices, and fill it in
            n_polys_i = len(x1i) - 1
            polys_i = np.empty((n_polys_i, 4, 3))
            polys_i[:, 0, :] = np.column_stack((x1i[:-1], y1i[:-1], z1i[:-1]))
            polys_i[:, 1, :] = np.column_stack((x1i[1:], y1i[1:], z1i[1:]))
            polys_i[:, 2, :] = np.column_stack((x2i[1:], y2i[1:], z2i[1:]))
            polys_i[:, 3, :] = np.column_stack((x2i[:-1], y2i[:-1], z2i[:-1]))
            polys = polys + [*polys_i]
        elif mode == 'polygon':
            line1 = np.column_stack((x1i, y1i, z1i))
            line2 = np.column_stack((x2i[::-1], y2i[::-1], z2i[::-1]))
            poly = np.concatenate((line1, line2), axis=0)
            polys.append(poly)

    polyc = art3d.Poly3DCollection(polys, facecolors=facecolors, shade=shade,
                                   axlim_clip=axlim_clip, **kwargs)
    self.add_collection(polyc)

    self.auto_scale_xyz([x1, x2], [y1, y2], [z1, z2], had_data)
    return polyc


# ==================================================
# Line: 2141

def plot_surface(self, X, Y, Z, *, norm=None, vmin=None,
                 vmax=None, lightsource=None, axlim_clip=False, **kwargs):
    """
    Create a surface plot.

    By default, it will be colored in shades of a solid color, but it also
    supports colormapping by supplying the *cmap* argument.

    .. note::

       The *rcount* and *ccount* kwargs, which both default to 50,
       determine the maximum number of samples used in each direction.  If
       the input data is larger, it will be downsampled (by slicing) to
       these numbers of points.

    .. note::

       To maximize rendering speed consider setting *rstride* and *cstride*
       to divisors of the number of rows minus 1 and columns minus 1
       respectively. For example, given 51 rows rstride can be any of the
       divisors of 50.

       Similarly, a setting of *rstride* and *cstride* equal to 1 (or
       *rcount* and *ccount* equal the number of rows and columns) can use
       the optimized path.

    Parameters
    ----------
    X, Y, Z : 2D arrays
        Data values.

    rcount, ccount : int
        Maximum number of samples used in each direction.  If the input
        data is larger, it will be downsampled (by slicing) to these
        numbers of points.  Defaults to 50.

    rstride, cstride : int
        Downsampling stride in each direction.  These arguments are
        mutually exclusive with *rcount* and *ccount*.  If only one of
        *rstride* or *cstride* is set, the other defaults to 10.

        'classic' mode uses a default of ``rstride = cstride = 10`` instead
        of the new default of ``rcount = ccount = 50``.

    color : :mpltype:`color`
        Color of the surface patches.

    cmap : Colormap, optional
        Colormap of the surface patches.

    facecolors : list of :mpltype:`color`
        Colors of each individual patch.

    norm : `~matplotlib.colors.Normalize`, optional
        Normalization for the colormap.

    vmin, vmax : float, optional
        Bounds for the normalization.

    shade : bool, default: True
        Whether to shade the facecolors.  Shading is always disabled when
        *cmap* is specified.

    lightsource : `~matplotlib.colors.LightSource`, optional
        The lightsource to use when *shade* is True.

    axlim_clip : bool, default: False
        Whether to hide patches with a vertex outside the axes view limits.

        .. versionadded:: 3.10

    **kwargs
        Other keyword arguments are forwarded to `.Poly3DCollection`.
    """

    had_data = self.has_data()

    if Z.ndim != 2:
        raise ValueError("Argument Z must be 2-dimensional.")

    Z = cbook._to_unmasked_float_array(Z)
    X, Y, Z = np.broadcast_arrays(X, Y, Z)
    rows, cols = Z.shape

    has_stride = 'rstride' in kwargs or 'cstride' in kwargs
    has_count = 'rcount' in kwargs or 'ccount' in kwargs

    if has_stride and has_count:
        raise ValueError("Cannot specify both stride and count arguments")

    rstride = kwargs.pop('rstride', 10)
    cstride = kwargs.pop('cstride', 10)
    rcount = kwargs.pop('rcount', 50)
    ccount = kwargs.pop('ccount', 50)

    if mpl.rcParams['_internal.classic_mode']:
        # Strides have priority over counts in classic mode.
        # So, only compute strides from counts
        # if counts were explicitly given
        compute_strides = has_count
    else:
        # If the strides are provided then it has priority.
        # Otherwise, compute the strides from the counts.
        compute_strides = not has_stride

    if compute_strides:
        rstride = int(max(np.ceil(rows / rcount), 1))
        cstride = int(max(np.ceil(cols / ccount), 1))

    fcolors = kwargs.pop('facecolors', None)

    cmap = kwargs.get('cmap', None)
    shade = kwargs.pop('shade', cmap is None)
    if shade is None:
        raise ValueError("shade cannot be None.")

    colset = []  # the sampled facecolor
    if (rows - 1) % rstride == 0 and \
       (cols - 1) % cstride == 0 and \
       fcolors is None:
        polys = np.stack(
            [cbook._array_patch_perimeters(a, rstride, cstride)
             for a in (X, Y, Z)],
            axis=-1)
    else:
        # evenly spaced, and including both endpoints
        row_inds = list(range(0, rows-1, rstride)) + [rows-1]
        col_inds = list(range(0, cols-1, cstride)) + [cols-1]

        polys = []
        for rs, rs_next in itertools.pairwise(row_inds):
            for cs, cs_next in itertools.pairwise(col_inds):
                ps = [
                    # +1 ensures we share edges between polygons
                    cbook._array_perimeter(a[rs:rs_next+1, cs:cs_next+1])
                    for a in (X, Y, Z)
                ]
                # ps = np.stack(ps, axis=-1)
                ps = np.array(ps).T
                polys.append(ps)

                if fcolors is not None:
                    colset.append(fcolors[rs][cs])

    # In cases where there are non-finite values in the data (possibly NaNs from
    # masked arrays), artifacts can be introduced. Here check whether such values
    # are present and remove them.
    if not isinstance(polys, np.ndarray) or not np.isfinite(polys).all():
        new_polys = []
        new_colset = []

        # Depending on fcolors, colset is either an empty list or has as
        # many elements as polys. In the former case new_colset results in
        # a list with None entries, that is discarded later.
        for p, col in itertools.zip_longest(polys, colset):
            new_poly = np.array(p)[np.isfinite(p).all(axis=1)]
            if len(new_poly):
                new_polys.append(new_poly)
                new_colset.append(col)

        # Replace previous polys and, if fcolors is not None, colset
        polys = new_polys
        if fcolors is not None:
            colset = new_colset

    # note that the striding causes some polygons to have more coordinates
    # than others

    if fcolors is not None:
        polyc = art3d.Poly3DCollection(
            polys, edgecolors=colset, facecolors=colset, shade=shade,
            lightsource=lightsource, axlim_clip=axlim_clip, **kwargs)
    elif cmap:
        polyc = art3d.Poly3DCollection(polys, axlim_clip=axlim_clip, **kwargs)
        # can't always vectorize, because polys might be jagged
        if isinstance(polys, np.ndarray):
            avg_z = polys[..., 2].mean(axis=-1)
        else:
            avg_z = np.array([ps[:, 2].mean() for ps in polys])
        polyc.set_array(avg_z)
        if vmin is not None or vmax is not None:
            polyc.set_clim(vmin, vmax)
        if norm is not None:
            polyc.set_norm(norm)
    else:
        color = kwargs.pop('color', None)
        if color is None:
            color = self._get_lines.get_next_color()
        color = np.array(mcolors.to_rgba(color))

        polyc = art3d.Poly3DCollection(
            polys, facecolors=color, shade=shade, lightsource=lightsource,
            axlim_clip=axlim_clip, **kwargs)

    self.add_collection(polyc)
    self.auto_scale_xyz(X, Y, Z, had_data)

    return polyc


# ==================================================
# Line: 2465

def plot_trisurf(self, *args, color=None, norm=None, vmin=None, vmax=None,
                 lightsource=None, axlim_clip=False, **kwargs):
    """
    Plot a triangulated surface.

    The (optional) triangulation can be specified in one of two ways;
    either::

      plot_trisurf(triangulation, ...)

    where triangulation is a `~matplotlib.tri.Triangulation` object, or::

      plot_trisurf(X, Y, ...)
      plot_trisurf(X, Y, triangles, ...)
      plot_trisurf(X, Y, triangles=triangles, ...)

    in which case a Triangulation object will be created.  See
    `.Triangulation` for an explanation of these possibilities.

    The remaining arguments are::

      plot_trisurf(..., Z)

    where *Z* is the array of values to contour, one per point
    in the triangulation.

    Parameters
    ----------
    X, Y, Z : array-like
        Data values as 1D arrays.
    color
        Color of the surface patches.
    cmap
        A colormap for the surface patches.
    norm : `~matplotlib.colors.Normalize`, optional
        An instance of Normalize to map values to colors.
    vmin, vmax : float, optional
        Minimum and maximum value to map.
    shade : bool, default: True
        Whether to shade the facecolors.  Shading is always disabled when
        *cmap* is specified.
    lightsource : `~matplotlib.colors.LightSource`, optional
        The lightsource to use when *shade* is True.
    axlim_clip : bool, default: False
        Whether to hide patches with a vertex outside the axes view limits.

        .. versionadded:: 3.10
    **kwargs
        All other keyword arguments are passed on to
        :class:`~mpl_toolkits.mplot3d.art3d.Poly3DCollection`

    Examples
    --------
    .. plot:: gallery/mplot3d/trisurf3d.py
    .. plot:: gallery/mplot3d/trisurf3d_2.py
    """

    had_data = self.has_data()

    # TODO: Support custom face colours
    if color is None:
        color = self._get_lines.get_next_color()
    color = np.array(mcolors.to_rgba(color))

    cmap = kwargs.get('cmap', None)
    shade = kwargs.pop('shade', cmap is None)

    tri, args, kwargs = \
        Triangulation.get_from_args_and_kwargs(*args, **kwargs)
    try:
        z = kwargs.pop('Z')
    except KeyError:
        # We do this so Z doesn't get passed as an arg to PolyCollection
        z, *args = args
    z = np.asarray(z)

    triangles = tri.get_masked_triangles()
    xt = tri.x[triangles]
    yt = tri.y[triangles]
    zt = z[triangles]
    verts = np.stack((xt, yt, zt), axis=-1)

    if cmap:
        polyc = art3d.Poly3DCollection(verts, *args,
                                       axlim_clip=axlim_clip, **kwargs)
        # average over the three points of each triangle
        avg_z = verts[:, :, 2].mean(axis=1)
        polyc.set_array(avg_z)
        if vmin is not None or vmax is not None:
            polyc.set_clim(vmin, vmax)
        if norm is not None:
            polyc.set_norm(norm)
    else:
        polyc = art3d.Poly3DCollection(
            verts, *args, shade=shade, lightsource=lightsource,
            facecolors=color, axlim_clip=axlim_clip, **kwargs)

    self.add_collection(polyc)
    self.auto_scale_xyz(tri.x, tri.y, z, had_data)

    return polyc


# ==================================================
# Line: 2595

def add_contour_set(
        self, cset, extend3d=False, stride=5, zdir='z', offset=None,
        axlim_clip=False):
    zdir = '-' + zdir
    if extend3d:
        self._3d_extend_contour(cset, stride)
    else:
        art3d.collection_2d_to_3d(
            cset, zs=offset if offset is not None else cset.levels, zdir=zdir,
            axlim_clip=axlim_clip)


# ==================================================
# Line: 2634

def contour(self, X, Y, Z, *args,
            extend3d=False, stride=5, zdir='z', offset=None, axlim_clip=False,
            **kwargs):
    """
    Create a 3D contour plot.

    Parameters
    ----------
    X, Y, Z : array-like,
        Input data. See `.Axes.contour` for supported data shapes.
    extend3d : bool, default: False
        Whether to extend contour in 3D.
    stride : int, default: 5
        Step size for extending contour.
    zdir : {'x', 'y', 'z'}, default: 'z'
        The direction to use.
    offset : float, optional
        If specified, plot a projection of the contour lines at this
        position in a plane normal to *zdir*.
    axlim_clip : bool, default: False
        Whether to hide lines with a vertex outside the axes view limits.

        .. versionadded:: 3.10
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    *args, **kwargs
        Other arguments are forwarded to `matplotlib.axes.Axes.contour`.

    Returns
    -------
    matplotlib.contour.QuadContourSet
    """
    had_data = self.has_data()

    jX, jY, jZ = art3d.rotate_axes(X, Y, Z, zdir)
    cset = super().contour(jX, jY, jZ, *args, **kwargs)
    self.add_contour_set(cset, extend3d, stride, zdir, offset, axlim_clip)

    self.auto_scale_xyz(X, Y, Z, had_data)
    return cset


# ==================================================
# Line: 2736

def _auto_scale_contourf(self, X, Y, Z, zdir, levels, had_data):
    # Autoscale in the zdir based on the levels added, which are
    # different from data range if any contour extensions are present
    dim_vals = {'x': X, 'y': Y, 'z': Z, zdir: levels}
    # Input data and levels have different sizes, but auto_scale_xyz
    # expected same-size input, so manually take min/max limits
    limits = [(np.nanmin(dim_vals[dim]), np.nanmax(dim_vals[dim]))
              for dim in ['x', 'y', 'z']]
    self.auto_scale_xyz(*limits, had_data)


# ==================================================
# Line: 2747

def contourf(self, X, Y, Z, *args,
             zdir='z', offset=None, axlim_clip=False, **kwargs):
    """
    Create a 3D filled contour plot.

    Parameters
    ----------
    X, Y, Z : array-like
        Input data. See `.Axes.contourf` for supported data shapes.
    zdir : {'x', 'y', 'z'}, default: 'z'
        The direction to use.
    offset : float, optional
        If specified, plot a projection of the contour lines at this
        position in a plane normal to *zdir*.
    axlim_clip : bool, default: False
        Whether to hide lines with a vertex outside the axes view limits.

        .. versionadded:: 3.10
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER
    *args, **kwargs
        Other arguments are forwarded to `matplotlib.axes.Axes.contourf`.

    Returns
    -------
    matplotlib.contour.QuadContourSet
    """
    had_data = self.has_data()

    jX, jY, jZ = art3d.rotate_axes(X, Y, Z, zdir)
    cset = super().contourf(jX, jY, jZ, *args, **kwargs)
    levels = self._add_contourf_set(cset, zdir, offset, axlim_clip)

    self._auto_scale_contourf(X, Y, Z, zdir, levels, had_data)
    return cset


# ==================================================
# Line: 2910

def scatter(self, xs, ys, zs=0, zdir='z', s=20, c=None, depthshade=None,
            *args,
            depthshade_minalpha=None,
            axlim_clip=False,
            **kwargs):
    """
    Create a scatter plot.

    Parameters
    ----------
    xs, ys : array-like
        The data positions.
    zs : float or array-like, default: 0
        The z-positions. Either an array of the same length as *xs* and
        *ys* or a single value to place all points in the same plane.
    zdir : {'x', 'y', 'z', '-x', '-y', '-z'}, default: 'z'
        The axis direction for the *zs*. This is useful when plotting 2D
        data on a 3D Axes. The data must be passed as *xs*, *ys*. Setting
        *zdir* to 'y' then plots the data to the x-z-plane.

        See also :doc:`/gallery/mplot3d/2dcollections3d`.

    s : float or array-like, default: 20
        The marker size in points**2. Either an array of the same length
        as *xs* and *ys* or a single value to make all markers the same
        size.
    c : :mpltype:`color`, sequence, or sequence of colors, optional
        The marker color. Possible values:

        - A single color format string.
        - A sequence of colors of length n.
        - A sequence of n numbers to be mapped to colors using *cmap* and
          *norm*.
        - A 2D array in which the rows are RGB or RGBA.

        For more details see the *c* argument of `~.axes.Axes.scatter`.
    depthshade : bool, default: None
        Whether to shade the scatter markers to give the appearance of
        depth. Each call to ``scatter()`` will perform its depthshading
        independently.
        If None, use the value from rcParams['axes3d.depthshade'].

    depthshade_minalpha : float, default: None
        The lowest alpha value applied by depth-shading.
        If None, use the value from rcParams['axes3d.depthshade_minalpha'].

        .. versionadded:: 3.11

    axlim_clip : bool, default: False
        Whether to hide the scatter points outside the axes view limits.

        .. versionadded:: 3.10

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        All other keyword arguments are passed on to `~.axes.Axes.scatter`.

    Returns
    -------
    paths : `~matplotlib.collections.PathCollection`
    """

    had_data = self.has_data()
    zs_orig = zs

    xs, ys, zs = cbook._broadcast_with_masks(xs, ys, zs)
    s = np.ma.ravel(s)  # This doesn't have to match x, y in size.

    xs, ys, zs, s, c, color = cbook.delete_masked_points(
        xs, ys, zs, s, c, kwargs.get('color', None)
        )
    if kwargs.get("color") is not None:
        kwargs['color'] = color
    if depthshade is None:
        depthshade = mpl.rcParams['axes3d.depthshade']
    if depthshade_minalpha is None:
        depthshade_minalpha = mpl.rcParams['axes3d.depthshade_minalpha']

    # For xs and ys, 2D scatter() will do the copying.
    if np.may_share_memory(zs_orig, zs):  # Avoid unnecessary copies.
        zs = zs.copy()

    patches = super().scatter(xs, ys, s=s, c=c, *args, **kwargs)
    art3d.patch_collection_2d_to_3d(
        patches,
        zs=zs,
        zdir=zdir,
        depthshade=depthshade,
        depthshade_minalpha=depthshade_minalpha,
        axlim_clip=axlim_clip,
    )
    if self._zmargin < 0.05 and xs.size > 0:
        self.set_zmargin(0.05)

    self.auto_scale_xyz(xs, ys, zs, had_data)

    return patches


# ==================================================
# Line: 3073

def bar3d(self, x, y, z, dx, dy, dz, color=None,
          zsort='average', shade=True, lightsource=None, *args,
          axlim_clip=False, **kwargs):
    """
    Generate a 3D barplot.

    This method creates three-dimensional barplot where the width,
    depth, height, and color of the bars can all be uniquely set.

    Parameters
    ----------
    x, y, z : array-like
        The coordinates of the anchor point of the bars.

    dx, dy, dz : float or array-like
        The width, depth, and height of the bars, respectively.

    color : sequence of colors, optional
        The color of the bars can be specified globally or
        individually. This parameter can be:

        - A single color, to color all bars the same color.
        - An array of colors of length N bars, to color each bar
          independently.
        - An array of colors of length 6, to color the faces of the
          bars similarly.
        - An array of colors of length 6 * N bars, to color each face
          independently.

        When coloring the faces of the boxes specifically, this is
        the order of the coloring:

        1. -Z (bottom of box)
        2. +Z (top of box)
        3. -Y
        4. +Y
        5. -X
        6. +X

    zsort : {'average', 'min', 'max'}, default: 'average'
        The z-axis sorting scheme passed onto `~.art3d.Poly3DCollection`

    shade : bool, default: True
        When true, this shades the dark sides of the bars (relative
        to the plot's source of light).

    lightsource : `~matplotlib.colors.LightSource`, optional
        The lightsource to use when *shade* is True.

    axlim_clip : bool, default: False
        Whether to hide the bars with points outside the axes view limits.

        .. versionadded:: 3.10

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Any additional keyword arguments are passed onto
        `~.art3d.Poly3DCollection`.

    Returns
    -------
    collection : `~.art3d.Poly3DCollection`
        A collection of three-dimensional polygons representing the bars.
    """

    had_data = self.has_data()

    x, y, z, dx, dy, dz = np.broadcast_arrays(
        np.atleast_1d(x), y, z, dx, dy, dz)
    minx = np.min(x)
    maxx = np.max(x + dx)
    miny = np.min(y)
    maxy = np.max(y + dy)
    minz = np.min(z)
    maxz = np.max(z + dz)

    # shape (6, 4, 3)
    # All faces are oriented facing outwards - when viewed from the
    # outside, their vertices are in a counterclockwise ordering.
    cuboid = np.array([
        # -z
        (
            (0, 0, 0),
            (0, 1, 0),
            (1, 1, 0),
            (1, 0, 0),
        ),
        # +z
        (
            (0, 0, 1),
            (1, 0, 1),
            (1, 1, 1),
            (0, 1, 1),
        ),
        # -y
        (
            (0, 0, 0),
            (1, 0, 0),
            (1, 0, 1),
            (0, 0, 1),
        ),
        # +y
        (
            (0, 1, 0),
            (0, 1, 1),
            (1, 1, 1),
            (1, 1, 0),
        ),
        # -x
        (
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 1),
            (0, 1, 0),
        ),
        # +x
        (
            (1, 0, 0),
            (1, 1, 0),
            (1, 1, 1),
            (1, 0, 1),
        ),
    ])

    # indexed by [bar, face, vertex, coord]
    polys = np.empty(x.shape + cuboid.shape)

    # handle each coordinate separately
    for i, p, dp in [(0, x, dx), (1, y, dy), (2, z, dz)]:
        p = p[..., np.newaxis, np.newaxis]
        dp = dp[..., np.newaxis, np.newaxis]
        polys[..., i] = p + dp * cuboid[..., i]

    # collapse the first two axes
    polys = polys.reshape((-1,) + polys.shape[2:])

    facecolors = []
    if color is None:
        color = [self._get_patches_for_fill.get_next_color()]

    color = list(mcolors.to_rgba_array(color))

    if len(color) == len(x):
        # bar colors specified, need to expand to number of faces
        for c in color:
            facecolors.extend([c] * 6)
    else:
        # a single color specified, or face colors specified explicitly
        facecolors = color
        if len(facecolors) < len(x):
            facecolors *= (6 * len(x))

    col = art3d.Poly3DCollection(polys,
                                 zsort=zsort,
                                 facecolors=facecolors,
                                 shade=shade,
                                 lightsource=lightsource,
                                 axlim_clip=axlim_clip,
                                 *args, **kwargs)
    self.add_collection(col)

    self.auto_scale_xyz((minx, maxx), (miny, maxy), (minz, maxz), had_data)

    return col


# ==================================================
# Line: 3248

def quiver(self, X, Y, Z, U, V, W, *,
           length=1, arrow_length_ratio=.3, pivot='tail', normalize=False,
           axlim_clip=False, **kwargs):
    """
    Plot a 3D field of arrows.

    The arguments can be array-like or scalars, so long as they can be
    broadcast together. The arguments can also be masked arrays. If an
    element in any of argument is masked, then that corresponding quiver
    element will not be plotted.

    Parameters
    ----------
    X, Y, Z : array-like
        The x, y and z coordinates of the arrow locations (default is
        tail of arrow; see *pivot* kwarg).

    U, V, W : array-like
        The x, y and z components of the arrow vectors.

    length : float, default: 1
        The length of each quiver.

    arrow_length_ratio : float, default: 0.3
        The ratio of the arrow head with respect to the quiver.

    pivot : {'tail', 'middle', 'tip'}, default: 'tail'
        The part of the arrow that is at the grid point; the arrow
        rotates about this point, hence the name *pivot*.

    normalize : bool, default: False
        Whether all arrows are normalized to have the same length, or keep
        the lengths defined by *u*, *v*, and *w*.

    axlim_clip : bool, default: False
        Whether to hide arrows with points outside the axes view limits.

        .. versionadded:: 3.10

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Any additional keyword arguments are delegated to
        :class:`.Line3DCollection`
    """

    def calc_arrows(UVW):
        # get unit direction vector perpendicular to (u, v, w)
        x = UVW[:, 0]
        y = UVW[:, 1]
        norm = np.linalg.norm(UVW[:, :2], axis=1)
        x_p = np.divide(y, norm, where=norm != 0, out=np.zeros_like(x))
        y_p = np.divide(-x,  norm, where=norm != 0, out=np.ones_like(x))
        # compute the two arrowhead direction unit vectors
        rangle = math.radians(15)
        c = math.cos(rangle)
        s = math.sin(rangle)
        # construct the rotation matrices of shape (3, 3, n)
        r13 = y_p * s
        r32 = x_p * s
        r12 = x_p * y_p * (1 - c)
        Rpos = np.array(
            [[c + (x_p ** 2) * (1 - c), r12, r13],
             [r12, c + (y_p ** 2) * (1 - c), -r32],
             [-r13, r32, np.full_like(x_p, c)]])
        # opposite rotation negates all the sin terms
        Rneg = Rpos.copy()
        Rneg[[0, 1, 2, 2], [2, 2, 0, 1]] *= -1
        # Batch n (3, 3) x (3) matrix multiplications ((3, 3, n) x (n, 3)).
        Rpos_vecs = np.einsum("ij...,...j->...i", Rpos, UVW)
        Rneg_vecs = np.einsum("ij...,...j->...i", Rneg, UVW)
        # Stack into (n, 2, 3) result.
        return np.stack([Rpos_vecs, Rneg_vecs], axis=1)

    had_data = self.has_data()

    input_args = cbook._broadcast_with_masks(X, Y, Z, U, V, W,
                                             compress=True)

    if any(len(v) == 0 for v in input_args):
        # No quivers, so just make an empty collection and return early
        linec = art3d.Line3DCollection([], **kwargs)
        self.add_collection(linec)
        return linec

    shaft_dt = np.array([0., length], dtype=float)
    arrow_dt = shaft_dt * arrow_length_ratio

    _api.check_in_list(['tail', 'middle', 'tip'], pivot=pivot)
    if pivot == 'tail':
        shaft_dt -= length
    elif pivot == 'middle':
        shaft_dt -= length / 2

    XYZ = np.column_stack(input_args[:3])
    UVW = np.column_stack(input_args[3:]).astype(float)

    # Normalize rows of UVW
    if normalize:
        norm = np.linalg.norm(UVW, axis=1)
        norm[norm == 0] = 1
        UVW = UVW / norm.reshape((-1, 1))

    if len(XYZ) > 0:
        # compute the shaft lines all at once with an outer product
        shafts = (XYZ - np.multiply.outer(shaft_dt, UVW)).swapaxes(0, 1)
        # compute head direction vectors, n heads x 2 sides x 3 dimensions
        head_dirs = calc_arrows(UVW)
        # compute all head lines at once, starting from the shaft ends
        heads = shafts[:, :1] - np.multiply.outer(arrow_dt, head_dirs)
        # stack left and right head lines together
        heads = heads.reshape((len(arrow_dt), -1, 3))
        # transpose to get a list of lines
        heads = heads.swapaxes(0, 1)

        lines = [*shafts, *heads[::2], *heads[1::2]]
    else:
        lines = []

    linec = art3d.Line3DCollection(lines, axlim_clip=axlim_clip, **kwargs)
    self.add_collection(linec)

    self.auto_scale_xyz(XYZ[:, 0], XYZ[:, 1], XYZ[:, 2], had_data)

    return linec


# ==================================================
# Line: 3593

def errorbar(self, x, y, z, zerr=None, yerr=None, xerr=None, fmt='',
             barsabove=False, errorevery=1, ecolor=None, elinewidth=None,
             capsize=None, capthick=None, xlolims=False, xuplims=False,
             ylolims=False, yuplims=False, zlolims=False, zuplims=False,
             axlim_clip=False,
             **kwargs):
    """
    Plot lines and/or markers with errorbars around them.

    *x*/*y*/*z* define the data locations, and *xerr*/*yerr*/*zerr* define
    the errorbar sizes. By default, this draws the data markers/lines as
    well the errorbars. Use fmt='none' to draw errorbars only.

    Parameters
    ----------
    x, y, z : float or array-like
        The data positions.

    xerr, yerr, zerr : float or array-like, shape (N,) or (2, N), optional
        The errorbar sizes:

        - scalar: Symmetric +/- values for all data points.
        - shape(N,): Symmetric +/-values for each data point.
        - shape(2, N): Separate - and + values for each bar. First row
          contains the lower errors, the second row contains the upper
          errors.
        - *None*: No errorbar.

        Note that all error arrays should have *positive* values.

    fmt : str, default: ''
        The format for the data points / data lines. See `.plot` for
        details.

        Use 'none' (case-insensitive) to plot errorbars without any data
        markers.

    ecolor : :mpltype:`color`, default: None
        The color of the errorbar lines.  If None, use the color of the
        line connecting the markers.

    elinewidth : float, default: None
        The linewidth of the errorbar lines. If None, the linewidth of
        the current style is used.

    capsize : float, default: :rc:`errorbar.capsize`
        The length of the error bar caps in points.

    capthick : float, default: None
        An alias to the keyword argument *markeredgewidth* (a.k.a. *mew*).
        This setting is a more sensible name for the property that
        controls the thickness of the error bar cap in points. For
        backwards compatibility, if *mew* or *markeredgewidth* are given,
        then they will over-ride *capthick*. This may change in future
        releases.

    barsabove : bool, default: False
        If True, will plot the errorbars above the plot
        symbols. Default is below.

    xlolims, ylolims, zlolims : bool, default: False
        These arguments can be used to indicate that a value gives only
        lower limits. In that case a caret symbol is used to indicate
        this. *lims*-arguments may be scalars, or array-likes of the same
        length as the errors. To use limits with inverted axes,
        `~.set_xlim`, `~.set_ylim`, or `~.set_zlim` must be
        called before `errorbar`. Note the tricky parameter names: setting
        e.g. *ylolims* to True means that the y-value is a *lower* limit of
        the True value, so, only an *upward*-pointing arrow will be drawn!

    xuplims, yuplims, zuplims : bool, default: False
        Same as above, but for controlling the upper limits.

    errorevery : int or (int, int), default: 1
        draws error bars on a subset of the data. *errorevery* =N draws
        error bars on the points (x[::N], y[::N], z[::N]).
        *errorevery* =(start, N) draws error bars on the points
        (x[start::N], y[start::N], z[start::N]). e.g. *errorevery* =(6, 3)
        adds error bars to the data at (x[6], x[9], x[12], x[15], ...).
        Used to avoid overlapping error bars when two series share x-axis
        values.

    axlim_clip : bool, default: False
        Whether to hide error bars that are outside the axes limits.

        .. versionadded:: 3.10

    Returns
    -------
    errlines : list
        List of `~mpl_toolkits.mplot3d.art3d.Line3DCollection` instances
        each containing an errorbar line.
    caplines : list
        List of `~mpl_toolkits.mplot3d.art3d.Line3D` instances each
        containing a capline object.
    limmarks : list
        List of `~mpl_toolkits.mplot3d.art3d.Line3D` instances each
        containing a marker with an upper or lower limit.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        All other keyword arguments for styling errorbar lines are passed
        `~mpl_toolkits.mplot3d.art3d.Line3DCollection`.

    Examples
    --------
    .. plot:: gallery/mplot3d/errorbar3d.py
    """
    had_data = self.has_data()

    kwargs = cbook.normalize_kwargs(kwargs, mlines.Line2D)
    # Drop anything that comes in as None to use the default instead.
    kwargs = {k: v for k, v in kwargs.items() if v is not None}
    kwargs.setdefault('zorder', 2)

    self._process_unit_info([("x", x), ("y", y), ("z", z)], kwargs,
                            convert=False)

    # make sure all the args are iterable; use lists not arrays to
    # preserve units
    x = x if np.iterable(x) else [x]
    y = y if np.iterable(y) else [y]
    z = z if np.iterable(z) else [z]

    if not len(x) == len(y) == len(z):
        raise ValueError("'x', 'y', and 'z' must have the same size")

    everymask = self._errorevery_to_mask(x, errorevery)

    label = kwargs.pop("label", None)
    kwargs['label'] = '_nolegend_'

    # Create the main line and determine overall kwargs for child artists.
    # We avoid calling self.plot() directly, or self._get_lines(), because
    # that would call self._process_unit_info again, and do other indirect
    # data processing.
    (data_line, base_style), = self._get_lines._plot_args(
        self, (x, y) if fmt == '' else (x, y, fmt), kwargs, return_kwargs=True)
    art3d.line_2d_to_3d(data_line, zs=z, axlim_clip=axlim_clip)

    # Do this after creating `data_line` to avoid modifying `base_style`.
    if barsabove:
        data_line.set_zorder(kwargs['zorder'] - .1)
    else:
        data_line.set_zorder(kwargs['zorder'] + .1)

    # Add line to plot, or throw it away and use it to determine kwargs.
    if fmt.lower() != 'none':
        self.add_line(data_line)
    else:
        data_line = None
        # Remove alpha=0 color that _process_plot_format returns.
        base_style.pop('color')

    if 'color' not in base_style:
        base_style['color'] = 'C0'
    if ecolor is None:
        ecolor = base_style['color']

    # Eject any line-specific information from format string, as it's not
    # needed for bars or caps.
    for key in ['marker', 'markersize', 'markerfacecolor',
                'markeredgewidth', 'markeredgecolor', 'markevery',
                'linestyle', 'fillstyle', 'drawstyle', 'dash_capstyle',
                'dash_joinstyle', 'solid_capstyle', 'solid_joinstyle']:
        base_style.pop(key, None)

    # Make the style dict for the line collections (the bars).
    eb_lines_style = {**base_style, 'color': ecolor}

    if elinewidth:
        eb_lines_style['linewidth'] = elinewidth
    elif 'linewidth' in kwargs:
        eb_lines_style['linewidth'] = kwargs['linewidth']

    for key in ('transform', 'alpha', 'zorder', 'rasterized'):
        if key in kwargs:
            eb_lines_style[key] = kwargs[key]

    # Make the style dict for caps (the "hats").
    eb_cap_style = {**base_style, 'linestyle': 'None'}
    if capsize is None:
        capsize = mpl.rcParams["errorbar.capsize"]
    if capsize > 0:
        eb_cap_style['markersize'] = 2. * capsize
    if capthick is not None:
        eb_cap_style['markeredgewidth'] = capthick
    eb_cap_style['color'] = ecolor

    def _apply_mask(arrays, mask):
        # Return, for each array in *arrays*, the elements for which *mask*
        # is True, without using fancy indexing.
        return [[*itertools.compress(array, mask)] for array in arrays]

    def _extract_errs(err, data, lomask, himask):
        # For separate +/- error values we need to unpack err
        if len(err.shape) == 2:
            low_err, high_err = err
        else:
            low_err, high_err = err, err

        lows = np.where(lomask | ~everymask, data, data - low_err)
        highs = np.where(himask | ~everymask, data, data + high_err)

        return lows, highs

    # collect drawn items while looping over the three coordinates
    errlines, caplines, limmarks = [], [], []

    # list of endpoint coordinates, used for auto-scaling
    coorderrs = []

    # define the markers used for errorbar caps and limits below
    # the dictionary key is mapped by the `i_xyz` helper dictionary
    capmarker = {0: '|', 1: '|', 2: '_'}
    i_xyz = {'x': 0, 'y': 1, 'z': 2}

    # Calculate marker size from points to quiver length. Because these are
    # not markers, and 3D Axes do not use the normal transform stack, this
    # is a bit involved. Since the quiver arrows will change size as the
    # scene is rotated, they are given a standard size based on viewing
    # them directly in planar form.
    quiversize = eb_cap_style.get('markersize',
                                  mpl.rcParams['lines.markersize']) ** 2
    quiversize *= self.get_figure(root=True).dpi / 72
    quiversize = self.transAxes.inverted().transform([
        (0, 0), (quiversize, quiversize)])
    quiversize = np.mean(np.diff(quiversize, axis=0))
    # quiversize is now in Axes coordinates, and to convert back to data
    # coordinates, we need to run it through the inverse 3D transform. For
    # consistency, this uses a fixed elevation, azimuth, and roll.
    with cbook._setattr_cm(self, elev=0, azim=0, roll=0):
        invM = np.linalg.inv(self.get_proj())
    # elev=azim=roll=0 produces the Y-Z plane, so quiversize in 2D 'x' is
    # 'y' in 3D, hence the 1 index.
    quiversize = np.dot(invM, [quiversize, 0, 0, 0])[1]
    # Quivers use a fixed 15-degree arrow head, so scale up the length so
    # that the size corresponds to the base. In other words, this constant
    # corresponds to the equation tan(15) = (base / 2) / (arrow length).
    quiversize *= 1.8660254037844388
    eb_quiver_style = {**eb_cap_style,
                       'length': quiversize, 'arrow_length_ratio': 1}
    eb_quiver_style.pop('markersize', None)

    # loop over x-, y-, and z-direction and draw relevant elements
    for zdir, data, err, lolims, uplims in zip(
            ['x', 'y', 'z'], [x, y, z], [xerr, yerr, zerr],
            [xlolims, ylolims, zlolims], [xuplims, yuplims, zuplims]):

        dir_vector = art3d.get_dir_vector(zdir)
        i_zdir = i_xyz[zdir]

        if err is None:
            continue

        if not np.iterable(err):
            err = [err] * len(data)

        err = np.atleast_1d(err)

        # arrays fine here, they are booleans and hence not units
        lolims = np.broadcast_to(lolims, len(data)).astype(bool)
        uplims = np.broadcast_to(uplims, len(data)).astype(bool)

        # a nested list structure that expands to (xl,xh),(yl,yh),(zl,zh),
        # where x/y/z and l/h correspond to dimensions and low/high
        # positions of errorbars in a dimension we're looping over
        coorderr = [
            _extract_errs(err * dir_vector[i], coord, lolims, uplims)
            for i, coord in enumerate([x, y, z])]
        (xl, xh), (yl, yh), (zl, zh) = coorderr

        # draws capmarkers - flat caps orthogonal to the error bars
        nolims = ~(lolims | uplims)
        if nolims.any() and capsize > 0:
            lo_caps_xyz = _apply_mask([xl, yl, zl], nolims & everymask)
            hi_caps_xyz = _apply_mask([xh, yh, zh], nolims & everymask)

            # setting '_' for z-caps and '|' for x- and y-caps;
            # these markers will rotate as the viewing angle changes
            cap_lo = art3d.Line3D(*lo_caps_xyz, ls='',
                                  marker=capmarker[i_zdir],
                                  axlim_clip=axlim_clip,
                                  **eb_cap_style)
            cap_hi = art3d.Line3D(*hi_caps_xyz, ls='',
                                  marker=capmarker[i_zdir],
                                  axlim_clip=axlim_clip,
                                  **eb_cap_style)
            self.add_line(cap_lo)
            self.add_line(cap_hi)
            caplines.append(cap_lo)
            caplines.append(cap_hi)

        if lolims.any():
            xh0, yh0, zh0 = _apply_mask([xh, yh, zh], lolims & everymask)
            self.quiver(xh0, yh0, zh0, *dir_vector, **eb_quiver_style)
        if uplims.any():
            xl0, yl0, zl0 = _apply_mask([xl, yl, zl], uplims & everymask)
            self.quiver(xl0, yl0, zl0, *-dir_vector, **eb_quiver_style)

        errline = art3d.Line3DCollection(np.array(coorderr).T,
                                         axlim_clip=axlim_clip,
                                         **eb_lines_style)
        self.add_collection(errline)
        errlines.append(errline)
        coorderrs.append(coorderr)

    coorderrs = np.array(coorderrs)

    def _digout_minmax(err_arr, coord_label):
        return (np.nanmin(err_arr[:, i_xyz[coord_label], :, :]),
                np.nanmax(err_arr[:, i_xyz[coord_label], :, :]))

    minx, maxx = _digout_minmax(coorderrs, 'x')
    miny, maxy = _digout_minmax(coorderrs, 'y')
    minz, maxz = _digout_minmax(coorderrs, 'z')
    self.auto_scale_xyz((minx, maxx), (miny, maxy), (minz, maxz), had_data)

    # Adapting errorbar containers for 3d case, assuming z-axis points "up"
    errorbar_container = mcontainer.ErrorbarContainer(
        (data_line, tuple(caplines), tuple(errlines)),
        has_xerr=(xerr is not None or yerr is not None),
        has_yerr=(zerr is not None),
        label=label)
    self.containers.append(errorbar_container)

    return errlines, caplines, limmarks


# ==================================================
# Line: 3942

def stem(self, x, y, z, *, linefmt='C0-', markerfmt='C0o', basefmt='C3-',
         bottom=0, label=None, orientation='z', axlim_clip=False):
    """
    Create a 3D stem plot.

    A stem plot draws lines perpendicular to a baseline, and places markers
    at the heads. By default, the baseline is defined by *x* and *y*, and
    stems are drawn vertically from *bottom* to *z*.

    Parameters
    ----------
    x, y, z : array-like
        The positions of the heads of the stems. The stems are drawn along
        the *orientation*-direction from the baseline at *bottom* (in the
        *orientation*-coordinate) to the heads. By default, the *x* and *y*
        positions are used for the baseline and *z* for the head position,
        but this can be changed by *orientation*.

    linefmt : str, default: 'C0-'
        A string defining the properties of the vertical lines. Usually,
        this will be a color or a color and a linestyle:

        =========  =============
        Character  Line Style
        =========  =============
        ``'-'``    solid line
        ``'--'``   dashed line
        ``'-.'``   dash-dot line
        ``':'``    dotted line
        =========  =============

        Note: While it is technically possible to specify valid formats
        other than color or color and linestyle (e.g. 'rx' or '-.'), this
        is beyond the intention of the method and will most likely not
        result in a reasonable plot.

    markerfmt : str, default: 'C0o'
        A string defining the properties of the markers at the stem heads.

    basefmt : str, default: 'C3-'
        A format string defining the properties of the baseline.

    bottom : float, default: 0
        The position of the baseline, in *orientation*-coordinates.

    label : str, optional
        The label to use for the stems in legends.

    orientation : {'x', 'y', 'z'}, default: 'z'
        The direction along which stems are drawn.

    axlim_clip : bool, default: False
        Whether to hide stems that are outside the axes limits.

        .. versionadded:: 3.10

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    Returns
    -------
    `.StemContainer`
        The container may be treated like a tuple
        (*markerline*, *stemlines*, *baseline*)

    Examples
    --------
    .. plot:: gallery/mplot3d/stem3d_demo.py
    """

    from matplotlib.container import StemContainer

    had_data = self.has_data()

    _api.check_in_list(['x', 'y', 'z'], orientation=orientation)

    xlim = (np.min(x), np.max(x))
    ylim = (np.min(y), np.max(y))
    zlim = (np.min(z), np.max(z))

    # Determine the appropriate plane for the baseline and the direction of
    # stemlines based on the value of orientation.
    if orientation == 'x':
        basex, basexlim = y, ylim
        basey, baseylim = z, zlim
        lines = [[(bottom, thisy, thisz), (thisx, thisy, thisz)]
                 for thisx, thisy, thisz in zip(x, y, z)]
    elif orientation == 'y':
        basex, basexlim = x, xlim
        basey, baseylim = z, zlim
        lines = [[(thisx, bottom, thisz), (thisx, thisy, thisz)]
                 for thisx, thisy, thisz in zip(x, y, z)]
    else:
        basex, basexlim = x, xlim
        basey, baseylim = y, ylim
        lines = [[(thisx, thisy, bottom), (thisx, thisy, thisz)]
                 for thisx, thisy, thisz in zip(x, y, z)]

    # Determine style for stem lines.
    linestyle, linemarker, linecolor = _process_plot_format(linefmt)
    linestyle = mpl._val_or_rc(linestyle, 'lines.linestyle')

    # Plot everything in required order.
    baseline, = self.plot(basex, basey, basefmt, zs=bottom,
                          zdir=orientation, label='_nolegend_')
    stemlines = art3d.Line3DCollection(
        lines, linestyles=linestyle, colors=linecolor, label='_nolegend_',
        axlim_clip=axlim_clip)
    self.add_collection(stemlines)
    markerline, = self.plot(x, y, z, markerfmt, label='_nolegend_')

    stem_container = StemContainer((markerline, stemlines, baseline),
                                   label=label)
    self.add_container(stem_container)

    jx, jy, jz = art3d.juggle_axes(basexlim, baseylim, [bottom, bottom],
                                   orientation)
    self.auto_scale_xyz([*jx, *xlim], [*jy, *ylim], [*jz, *zlim], had_data)

    return stem_container


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/mplot3d/proj3d.py
# Line: 10

def world_transformation(xmin, xmax,
                         ymin, ymax,
                         zmin, zmax, pb_aspect=None):
    """
    Produce a matrix that scales homogeneous coords in the specified ranges
    to [0, 1], or [0, pb_aspect[i]] if the plotbox aspect ratio is specified.
    """
    dx = xmax - xmin
    dy = ymax - ymin
    dz = zmax - zmin
    if pb_aspect is not None:
        ax, ay, az = pb_aspect
        dx /= ax
        dy /= ay
        dz /= az

    return np.array([[1/dx,    0,    0, -xmin/dx],
                     [   0, 1/dy,    0, -ymin/dy],
                     [   0,    0, 1/dz, -zmin/dz],
                     [   0,    0,    0,        1]])



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axes_grid1/axes_grid.py
# Line: 61

def __init__(self, fig,
             rect,
             nrows_ncols,
             n_axes=None,
             direction="row",
             axes_pad=0.02,
             *,
             share_all=False,
             share_x=True,
             share_y=True,
             label_mode="L",
             axes_class=None,
             aspect=False,
             ):
    """
    Parameters
    ----------
    fig : `.Figure`
        The parent figure.
    rect : (float, float, float, float), (int, int, int), int, or \

# ==================================================
# Line: 298

def __init__(self, fig,
             rect,
             nrows_ncols,
             n_axes=None,
             direction="row",
             axes_pad=0.02,
             *,
             share_all=False,
             aspect=True,
             label_mode="L",
             cbar_mode=None,
             cbar_location="right",
             cbar_pad=None,
             cbar_size="5%",
             cbar_set_cax=True,
             axes_class=None,
             ):
    """
    Parameters
    ----------
    fig : `.Figure`
        The parent figure.
    rect : (float, float, float, float) or int
        The axes position, as a ``(left, bottom, width, height)`` tuple or
        as a three-digit subplot position code (e.g., "121").
    nrows_ncols : (int, int)
        Number of rows and columns in the grid.
    n_axes : int or None, default: None
        If not None, only the first *n_axes* axes in the grid are created.
    direction : {"row", "column"}, default: "row"
        Whether axes are created in row-major ("row by row") or
        column-major order ("column by column").  This also affects the
        order in which axes are accessed using indexing (``grid[index]``).
    axes_pad : float or (float, float), default: 0.02in
        Padding or (horizontal padding, vertical padding) between axes, in
        inches.
    share_all : bool, default: False
        Whether all axes share their x- and y-axis.  Note that in any case,
        all axes in a column share their x-axis and all axes in a row share
        their y-axis.
    aspect : bool, default: True
        Whether the axes aspect ratio follows the aspect ratio of the data
        limits.
    label_mode : {"L", "1", "all"}, default: "L"
        Determines which axes will get tick labels:

        - "L": All axes on the left column get vertical tick labels;
          all axes on the bottom row get horizontal tick labels.
        - "1": Only the bottom left axes is labelled.
        - "all": all axes are labelled.

    cbar_mode : {"each", "single", "edge", None}, default: None
        Whether to create a colorbar for "each" axes, a "single" colorbar
        for the entire grid, colorbars only for axes on the "edge"
        determined by *cbar_location*, or no colorbars.  The colorbars are
        stored in the :attr:`!cbar_axes` attribute.
    cbar_location : {"left", "right", "bottom", "top"}, default: "right"
    cbar_pad : float, default: None
        Padding between the image axes and the colorbar axes.

        .. versionchanged:: 3.10
            ``cbar_mode="single"`` no longer adds *axes_pad* between the axes
            and the colorbar if the *cbar_location* is "left" or "bottom".

    cbar_size : size specification (see `!.Size.from_any`), default: "5%"
        Colorbar size.
    cbar_set_cax : bool, default: True
        If True, each axes in the grid has a *cax* attribute that is bound
        to associated *cbar_axes*.
    axes_class : subclass of `matplotlib.axes.Axes`, default: None
    """
    _api.check_in_list(["each", "single", "edge", None],
                       cbar_mode=cbar_mode)
    _api.check_in_list(["left", "right", "bottom", "top"],
                       cbar_location=cbar_location)
    self._colorbar_mode = cbar_mode
    self._colorbar_location = cbar_location
    self._colorbar_pad = cbar_pad
    self._colorbar_size = cbar_size
    # The colorbar axes are created in _init_locators().

    super().__init__(
        fig, rect, nrows_ncols, n_axes,
        direction=direction, axes_pad=axes_pad,
        share_all=share_all, share_x=True, share_y=True, aspect=aspect,
        label_mode=label_mode, axes_class=axes_class)

    for ax in self.cbar_axes:
        fig.add_axes(ax)

    if cbar_set_cax:
        if self._colorbar_mode == "single":
            for ax in self.axes_all:
                ax.cax = self.cbar_axes[0]
        elif self._colorbar_mode == "edge":
            for index, ax in enumerate(self.axes_all):
                col, row = self._get_col_row(index)
                if self._colorbar_location in ("left", "right"):
                    ax.cax = self.cbar_axes[row]
                else:
                    ax.cax = self.cbar_axes[col]
        else:
            for ax, cax in zip(self.axes_all, self.cbar_axes):
                ax.cax = cax


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axes_grid1/anchored_artists.py
# Line: 13

def __init__(self, width, height, xdescent, ydescent,
             loc, pad=0.4, borderpad=0.5, prop=None, frameon=True,
             **kwargs):
    """
    An anchored container with a fixed size and fillable `.DrawingArea`.

    Artists added to the *drawing_area* will have their coordinates
    interpreted as pixels. Any transformations set on the artists will be
    overridden.

    Parameters
    ----------
    width, height : float
        Width and height of the container, in pixels.
    xdescent, ydescent : float
        Descent of the container in the x- and y- direction, in pixels.
    loc : str
        Location of this artist.  Valid locations are
        'upper left', 'upper center', 'upper right',
        'center left', 'center', 'center right',
        'lower left', 'lower center', 'lower right'.
        For backward compatibility, numeric values are accepted as well.
        See the parameter *loc* of `.Legend` for details.
    pad : float, default: 0.4
        Padding around the child objects, in fraction of the font size.
    borderpad : float, default: 0.5
        Border padding, in fraction of the font size.
    prop : `~matplotlib.font_manager.FontProperties`, optional
        Font property used as a reference for paddings.
    frameon : bool, default: True
        If True, draw a box around this artist.
    **kwargs
        Keyword arguments forwarded to `.AnchoredOffsetbox`.

    Attributes
    ----------
    drawing_area : `~matplotlib.offsetbox.DrawingArea`
        A container for artists to display.

    Examples
    --------
    To display blue and red circles of different sizes in the upper right
    of an Axes *ax*:

    >>> ada = AnchoredDrawingArea(20, 20, 0, 0,
    ...                           loc='upper right', frameon=False)
    >>> ada.drawing_area.add_artist(Circle((10, 10), 10, fc="b"))
    >>> ada.drawing_area.add_artist(Circle((30, 10), 5, fc="r"))
    >>> ax.add_artist(ada)
    """
    self.da = DrawingArea(width, height, xdescent, ydescent)
    self.drawing_area = self.da

    super().__init__(
        loc, pad=pad, borderpad=borderpad, child=self.da, prop=None,
        frameon=frameon, **kwargs
    )



# ==================================================
# Line: 73

def __init__(self, transform, loc,
             pad=0.4, borderpad=0.5, prop=None, frameon=True, **kwargs):
    """
    An anchored container with transformed coordinates.

    Artists added to the *drawing_area* are scaled according to the
    coordinates of the transformation used. The dimensions of this artist
    will scale to contain the artists added.

    Parameters
    ----------
    transform : `~matplotlib.transforms.Transform`
        The transformation object for the coordinate system in use, i.e.,
        :attr:`!matplotlib.axes.Axes.transData`.
    loc : str
        Location of this artist.  Valid locations are
        'upper left', 'upper center', 'upper right',
        'center left', 'center', 'center right',
        'lower left', 'lower center', 'lower right'.
        For backward compatibility, numeric values are accepted as well.
        See the parameter *loc* of `.Legend` for details.
    pad : float, default: 0.4
        Padding around the child objects, in fraction of the font size.
    borderpad : float, default: 0.5
        Border padding, in fraction of the font size.
    prop : `~matplotlib.font_manager.FontProperties`, optional
        Font property used as a reference for paddings.
    frameon : bool, default: True
        If True, draw a box around this artist.
    **kwargs
        Keyword arguments forwarded to `.AnchoredOffsetbox`.

    Attributes
    ----------
    drawing_area : `~matplotlib.offsetbox.AuxTransformBox`
        A container for artists to display.

    Examples
    --------
    To display an ellipse in the upper left, with a width of 0.1 and
    height of 0.4 in data coordinates:

    >>> box = AnchoredAuxTransformBox(ax.transData, loc='upper left')
    >>> el = Ellipse((0, 0), width=0.1, height=0.4, angle=30)
    >>> box.drawing_area.add_artist(el)
    >>> ax.add_artist(box)
    """
    self.drawing_area = AuxTransformBox(transform)

    super().__init__(loc, pad=pad, borderpad=borderpad,
                     child=self.drawing_area, prop=prop, frameon=frameon,
                     **kwargs)



# ==================================================
# Line: 128

def __init__(self, transform, size, label, loc,
             pad=0.1, borderpad=0.1, sep=2,
             frameon=True, size_vertical=0, color='black',
             label_top=False, fontproperties=None, fill_bar=None,
             **kwargs):
    """
    Draw a horizontal scale bar with a center-aligned label underneath.

    Parameters
    ----------
    transform : `~matplotlib.transforms.Transform`
        The transformation object for the coordinate system in use, i.e.,
        :attr:`!matplotlib.axes.Axes.transData`.
    size : float
        Horizontal length of the size bar, given in coordinates of
        *transform*.
    label : str
        Label to display.
    loc : str
        Location of the size bar.  Valid locations are
        'upper left', 'upper center', 'upper right',
        'center left', 'center', 'center right',
        'lower left', 'lower center', 'lower right'.
        For backward compatibility, numeric values are accepted as well.
        See the parameter *loc* of `.Legend` for details.
    pad : float, default: 0.1
        Padding around the label and size bar, in fraction of the font
        size.
    borderpad : float, default: 0.1
        Border padding, in fraction of the font size.
    sep : float, default: 2
        Separation between the label and the size bar, in points.
    frameon : bool, default: True
        If True, draw a box around the horizontal bar and label.
    size_vertical : float, default: 0
        Vertical length of the size bar, given in coordinates of
        *transform*.
    color : str, default: 'black'
        Color for the size bar and label.
    label_top : bool, default: False
        If True, the label will be over the size bar.
    fontproperties : `~matplotlib.font_manager.FontProperties`, optional
        Font properties for the label text.
    fill_bar : bool, optional
        If True and if *size_vertical* is nonzero, the size bar will
        be filled in with the color specified by the size bar.
        Defaults to True if *size_vertical* is greater than
        zero and False otherwise.
    **kwargs
        Keyword arguments forwarded to `.AnchoredOffsetbox`.

    Attributes
    ----------
    size_bar : `~matplotlib.offsetbox.AuxTransformBox`
        Container for the size bar.
    txt_label : `~matplotlib.offsetbox.TextArea`
        Container for the label of the size bar.

    Notes
    -----
    If *prop* is passed as a keyword argument, but *fontproperties* is
    not, then *prop* is assumed to be the intended *fontproperties*.
    Using both *prop* and *fontproperties* is not supported.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> from mpl_toolkits.axes_grid1.anchored_artists import (
    ...     AnchoredSizeBar)
    >>> fig, ax = plt.subplots()
    >>> ax.imshow(np.random.random((10, 10)))
    >>> bar = AnchoredSizeBar(ax.transData, 3, '3 data units', 4)
    >>> ax.add_artist(bar)
    >>> fig.show()

    Using all the optional parameters

    >>> import matplotlib.font_manager as fm
    >>> fontprops = fm.FontProperties(size=14, family='monospace')
    >>> bar = AnchoredSizeBar(ax.transData, 3, '3 units', 4, pad=0.5,
    ...                       sep=5, borderpad=0.5, frameon=False,
    ...                       size_vertical=0.5, color='white',
    ...                       fontproperties=fontprops)
    """
    if fill_bar is None:
        fill_bar = size_vertical > 0

    self.size_bar = AuxTransformBox(transform)
    self.size_bar.add_artist(Rectangle((0, 0), size, size_vertical,
                                       fill=fill_bar, facecolor=color,
                                       edgecolor=color))

    if fontproperties is None and 'prop' in kwargs:
        fontproperties = kwargs.pop('prop')

    if fontproperties is None:
        textprops = {'color': color}
    else:
        textprops = {'color': color, 'fontproperties': fontproperties}

    self.txt_label = TextArea(label, textprops=textprops)

    if label_top:
        _box_children = [self.txt_label, self.size_bar]
    else:
        _box_children = [self.size_bar, self.txt_label]

    self._box = VPacker(children=_box_children,
                        align="center",
                        pad=0, sep=sep)

    super().__init__(loc, pad=pad, borderpad=borderpad, child=self._box,
                     prop=fontproperties, frameon=frameon, **kwargs)



# ==================================================
# Line: 245

def __init__(self, transform, label_x, label_y, length=0.15,
             fontsize=0.08, loc='upper left', angle=0, aspect_ratio=1,
             pad=0.4, borderpad=0.4, frameon=False, color='w', alpha=1,
             sep_x=0.01, sep_y=0, fontproperties=None, back_length=0.15,
             head_width=10, head_length=15, tail_width=2,
             text_props=None, arrow_props=None,
             **kwargs):
    """
    Draw two perpendicular arrows to indicate directions.

    Parameters
    ----------
    transform : `~matplotlib.transforms.Transform`
        The transformation object for the coordinate system in use, i.e.,
        :attr:`!matplotlib.axes.Axes.transAxes`.
    label_x, label_y : str
        Label text for the x and y arrows
    length : float, default: 0.15
        Length of the arrow, given in coordinates of *transform*.
    fontsize : float, default: 0.08
        Size of label strings, given in coordinates of *transform*.
    loc : str, default: 'upper left'
        Location of the arrow.  Valid locations are
        'upper left', 'upper center', 'upper right',
        'center left', 'center', 'center right',
        'lower left', 'lower center', 'lower right'.
        For backward compatibility, numeric values are accepted as well.
        See the parameter *loc* of `.Legend` for details.
    angle : float, default: 0
        The angle of the arrows in degrees.
    aspect_ratio : float, default: 1
        The ratio of the length of arrow_x and arrow_y.
        Negative numbers can be used to change the direction.
    pad : float, default: 0.4
        Padding around the labels and arrows, in fraction of the font size.
    borderpad : float, default: 0.4
        Border padding, in fraction of the font size.
    frameon : bool, default: False
        If True, draw a box around the arrows and labels.
    color : str, default: 'white'
        Color for the arrows and labels.
    alpha : float, default: 1
        Alpha values of the arrows and labels
    sep_x, sep_y : float, default: 0.01 and 0 respectively
        Separation between the arrows and labels in coordinates of
        *transform*.
    fontproperties : `~matplotlib.font_manager.FontProperties`, optional
        Font properties for the label text.
    back_length : float, default: 0.15
        Fraction of the arrow behind the arrow crossing.
    head_width : float, default: 10
        Width of arrow head, sent to `.ArrowStyle`.
    head_length : float, default: 15
        Length of arrow head, sent to `.ArrowStyle`.
    tail_width : float, default: 2
        Width of arrow tail, sent to `.ArrowStyle`.
    text_props, arrow_props : dict
        Properties of the text and arrows, passed to `.TextPath` and
        `.FancyArrowPatch`.
    **kwargs
        Keyword arguments forwarded to `.AnchoredOffsetbox`.

    Attributes
    ----------
    arrow_x, arrow_y : `~matplotlib.patches.FancyArrowPatch`
        Arrow x and y
    text_path_x, text_path_y : `~matplotlib.text.TextPath`
        Path for arrow labels
    p_x, p_y : `~matplotlib.patches.PathPatch`
        Patch for arrow labels
    box : `~matplotlib.offsetbox.AuxTransformBox`
        Container for the arrows and labels.

    Notes
    -----
    If *prop* is passed as a keyword argument, but *fontproperties* is
    not, then *prop* is assumed to be the intended *fontproperties*.
    Using both *prop* and *fontproperties* is not supported.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> from mpl_toolkits.axes_grid1.anchored_artists import (
    ...     AnchoredDirectionArrows)
    >>> fig, ax = plt.subplots()
    >>> ax.imshow(np.random.random((10, 10)))
    >>> arrows = AnchoredDirectionArrows(ax.transAxes, '111', '110')
    >>> ax.add_artist(arrows)
    >>> fig.show()

    Using several of the optional parameters, creating downward pointing
    arrow and high contrast text labels.

    >>> import matplotlib.font_manager as fm
    >>> fontprops = fm.FontProperties(family='monospace')
    >>> arrows = AnchoredDirectionArrows(ax.transAxes, 'East', 'South',
    ...                                  loc='lower left', color='k',
    ...                                  aspect_ratio=-1, sep_x=0.02,
    ...                                  sep_y=-0.01,
    ...                                  text_props={'ec':'w', 'fc':'k'},
    ...                                  fontproperties=fontprops)
    """
    if arrow_props is None:
        arrow_props = {}

    if text_props is None:
        text_props = {}

    arrowstyle = ArrowStyle("Simple",
                            head_width=head_width,
                            head_length=head_length,
                            tail_width=tail_width)

    if fontproperties is None and 'prop' in kwargs:
        fontproperties = kwargs.pop('prop')

    if 'color' not in arrow_props:
        arrow_props['color'] = color

    if 'alpha' not in arrow_props:
        arrow_props['alpha'] = alpha

    if 'color' not in text_props:
        text_props['color'] = color

    if 'alpha' not in text_props:
        text_props['alpha'] = alpha

    t_start = transform
    t_end = t_start + transforms.Affine2D().rotate_deg(angle)

    self.box = AuxTransformBox(t_end)

    length_x = length
    length_y = length*aspect_ratio

    self.arrow_x = FancyArrowPatch(
            (0, back_length*length_y),
            (length_x, back_length*length_y),
            arrowstyle=arrowstyle,
            shrinkA=0.0,
            shrinkB=0.0,
            **arrow_props)

    self.arrow_y = FancyArrowPatch(
            (back_length*length_x, 0),
            (back_length*length_x, length_y),
            arrowstyle=arrowstyle,
            shrinkA=0.0,
            shrinkB=0.0,
            **arrow_props)

    self.box.add_artist(self.arrow_x)
    self.box.add_artist(self.arrow_y)

    text_path_x = TextPath((
        length_x+sep_x, back_length*length_y+sep_y), label_x,
        size=fontsize, prop=fontproperties)
    self.p_x = PathPatch(text_path_x, transform=t_start, **text_props)
    self.box.add_artist(self.p_x)

    text_path_y = TextPath((
        length_x*back_length+sep_x, length_y*(1-back_length)+sep_y),
        label_y, size=fontsize, prop=fontproperties)
    self.p_y = PathPatch(text_path_y, **text_props)
    self.box.add_artist(self.p_y)

    super().__init__(loc, pad=pad, borderpad=borderpad, child=self.box,
                     frameon=frameon, **kwargs)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axes_grid1/inset_locator.py
# Line: 40

def __init__(self, bbox_to_anchor, x_size, y_size, loc,
             borderpad=0.5, bbox_transform=None):
    super().__init__(
        bbox_to_anchor, None, loc,
        borderpad=borderpad, bbox_transform=bbox_transform
    )

    self.x_size = Size.from_any(x_size)
    self.y_size = Size.from_any(y_size)


# ==================================================
# Line: 66

def __init__(self, parent_axes, zoom, loc,
             borderpad=0.5,
             bbox_to_anchor=None,
             bbox_transform=None):
    self.parent_axes = parent_axes
    self.zoom = zoom
    if bbox_to_anchor is None:
        bbox_to_anchor = parent_axes.bbox
    super().__init__(
        bbox_to_anchor, None, loc, borderpad=borderpad,
        bbox_transform=bbox_transform)


# ==================================================
# Line: 196

def __init__(self, bbox1, bbox2, loc1a, loc2a, loc1b, loc2b, **kwargs):
    """
    Connect two bboxes with a quadrilateral.

    The quadrilateral is specified by two lines that start and end at
    corners of the bboxes. The four sides of the quadrilateral are defined
    by the two lines given, the line between the two corners specified in
    *bbox1* and the line between the two corners specified in *bbox2*.

    Parameters
    ----------
    bbox1, bbox2 : `~matplotlib.transforms.Bbox`
        Bounding boxes to connect.

    loc1a, loc2a, loc1b, loc2b : {1, 2, 3, 4}
        The first line connects corners *loc1a* of *bbox1* and *loc2a* of
        *bbox2*; the second line connects corners *loc1b* of *bbox1* and
        *loc2b* of *bbox2*.  Valid values are::

            'upper right'  : 1,
            'upper left'   : 2,
            'lower left'   : 3,
            'lower right'  : 4

    **kwargs
        Patch properties for the line drawn:

        %(Patch:kwdoc)s
    """
    if "transform" in kwargs:
        raise ValueError("transform should not be set")
    super().__init__(bbox1, bbox2, loc1a, loc2a, **kwargs)
    self.loc1b = loc1b
    self.loc2b = loc2b


# ==================================================
# Line: 254

def inset_axes(parent_axes, width, height, loc='upper right',
               bbox_to_anchor=None, bbox_transform=None,
               axes_class=None, axes_kwargs=None,
               borderpad=0.5):
    """
    Create an inset axes with a given width and height.

    Both sizes used can be specified either in inches or percentage.
    For example,::

        inset_axes(parent_axes, width='40%%', height='30%%', loc='lower left')

    creates in inset axes in the lower left corner of *parent_axes* which spans
    over 30%% in height and 40%% in width of the *parent_axes*. Since the usage
    of `.inset_axes` may become slightly tricky when exceeding such standard
    cases, it is recommended to read :doc:`the examples
    </gallery/axes_grid1/inset_locator_demo>`.

    Notes
    -----
    The meaning of *bbox_to_anchor* and *bbox_to_transform* is interpreted
    differently from that of legend. The value of bbox_to_anchor
    (or the return value of its get_points method; the default is
    *parent_axes.bbox*) is transformed by the bbox_transform (the default
    is Identity transform) and then interpreted as points in the pixel
    coordinate (which is dpi dependent).

    Thus, following three calls are identical and creates an inset axes
    with respect to the *parent_axes*::

       axins = inset_axes(parent_axes, "30%%", "40%%")
       axins = inset_axes(parent_axes, "30%%", "40%%",
                          bbox_to_anchor=parent_axes.bbox)
       axins = inset_axes(parent_axes, "30%%", "40%%",
                          bbox_to_anchor=(0, 0, 1, 1),
                          bbox_transform=parent_axes.transAxes)

    Parameters
    ----------
    parent_axes : `matplotlib.axes.Axes`
        Axes to place the inset axes.

    width, height : float or str
        Size of the inset axes to create. If a float is provided, it is
        the size in inches, e.g. *width=1.3*. If a string is provided, it is
        the size in relative units, e.g. *width='40%%'*. By default, i.e. if
        neither *bbox_to_anchor* nor *bbox_transform* are specified, those
        are relative to the parent_axes. Otherwise, they are to be understood
        relative to the bounding box provided via *bbox_to_anchor*.

    loc : str, default: 'upper right'
        Location to place the inset axes.  Valid locations are
        'upper left', 'upper center', 'upper right',
        'center left', 'center', 'center right',
        'lower left', 'lower center', 'lower right'.
        For backward compatibility, numeric values are accepted as well.
        See the parameter *loc* of `.Legend` for details.

    bbox_to_anchor : tuple or `~matplotlib.transforms.BboxBase`, optional
        Bbox that the inset axes will be anchored to. If None,
        a tuple of (0, 0, 1, 1) is used if *bbox_transform* is set
        to *parent_axes.transAxes* or *parent_axes.figure.transFigure*.
        Otherwise, *parent_axes.bbox* is used. If a tuple, can be either
        [left, bottom, width, height], or [left, bottom].
        If the kwargs *width* and/or *height* are specified in relative units,
        the 2-tuple [left, bottom] cannot be used. Note that,
        unless *bbox_transform* is set, the units of the bounding box
        are interpreted in the pixel coordinate. When using *bbox_to_anchor*
        with tuple, it almost always makes sense to also specify
        a *bbox_transform*. This might often be the axes transform
        *parent_axes.transAxes*.

    bbox_transform : `~matplotlib.transforms.Transform`, optional
        Transformation for the bbox that contains the inset axes.
        If None, a `.transforms.IdentityTransform` is used. The value
        of *bbox_to_anchor* (or the return value of its get_points method)
        is transformed by the *bbox_transform* and then interpreted
        as points in the pixel coordinate (which is dpi dependent).
        You may provide *bbox_to_anchor* in some normalized coordinate,
        and give an appropriate transform (e.g., *parent_axes.transAxes*).

    axes_class : `~matplotlib.axes.Axes` type, default: `.HostAxes`
        The type of the newly created inset axes.

    axes_kwargs : dict, optional
        Keyword arguments to pass to the constructor of the inset axes.
        Valid arguments include:

        %(Axes:kwdoc)s

    borderpad : float, default: 0.5
        Padding between inset axes and the bbox_to_anchor.
        The units are axes font size, i.e. for a default font size of 10 points
        *borderpad = 0.5* is equivalent to a padding of 5 points.

    Returns
    -------
    inset_axes : *axes_class*
        Inset axes object created.
    """

    if (bbox_transform in [parent_axes.transAxes,
                           parent_axes.get_figure(root=False).transFigure]
            and bbox_to_anchor is None):
        _api.warn_external("Using the axes or figure transform requires a "
                           "bounding box in the respective coordinates. "
                           "Using bbox_to_anchor=(0, 0, 1, 1) now.")
        bbox_to_anchor = (0, 0, 1, 1)
    if bbox_to_anchor is None:
        bbox_to_anchor = parent_axes.bbox
    if (isinstance(bbox_to_anchor, tuple) and
            (isinstance(width, str) or isinstance(height, str))):
        if len(bbox_to_anchor) != 4:
            raise ValueError("Using relative units for width or height "
                             "requires to provide a 4-tuple or a "
                             "`Bbox` instance to `bbox_to_anchor.")
    return _add_inset_axes(
        parent_axes, axes_class, axes_kwargs,
        AnchoredSizeLocator(
            bbox_to_anchor, width, height, loc=loc,
            bbox_transform=bbox_transform, borderpad=borderpad))



# ==================================================
# Line: 378

def zoomed_inset_axes(parent_axes, zoom, loc='upper right',
                      bbox_to_anchor=None, bbox_transform=None,
                      axes_class=None, axes_kwargs=None,
                      borderpad=0.5):
    """
    Create an anchored inset axes by scaling a parent axes. For usage, also see
    :doc:`the examples </gallery/axes_grid1/inset_locator_demo2>`.

    Parameters
    ----------
    parent_axes : `~matplotlib.axes.Axes`
        Axes to place the inset axes.

    zoom : float
        Scaling factor of the data axes. *zoom* > 1 will enlarge the
        coordinates (i.e., "zoomed in"), while *zoom* < 1 will shrink the
        coordinates (i.e., "zoomed out").

    loc : str, default: 'upper right'
        Location to place the inset axes.  Valid locations are
        'upper left', 'upper center', 'upper right',
        'center left', 'center', 'center right',
        'lower left', 'lower center', 'lower right'.
        For backward compatibility, numeric values are accepted as well.
        See the parameter *loc* of `.Legend` for details.

    bbox_to_anchor : tuple or `~matplotlib.transforms.BboxBase`, optional
        Bbox that the inset axes will be anchored to. If None,
        *parent_axes.bbox* is used. If a tuple, can be either
        [left, bottom, width, height], or [left, bottom].
        If the kwargs *width* and/or *height* are specified in relative units,
        the 2-tuple [left, bottom] cannot be used. Note that
        the units of the bounding box are determined through the transform
        in use. When using *bbox_to_anchor* it almost always makes sense to
        also specify a *bbox_transform*. This might often be the axes transform
        *parent_axes.transAxes*.

    bbox_transform : `~matplotlib.transforms.Transform`, optional
        Transformation for the bbox that contains the inset axes.
        If None, a `.transforms.IdentityTransform` is used (i.e. pixel
        coordinates). This is useful when not providing any argument to
        *bbox_to_anchor*. When using *bbox_to_anchor* it almost always makes
        sense to also specify a *bbox_transform*. This might often be the
        axes transform *parent_axes.transAxes*. Inversely, when specifying
        the axes- or figure-transform here, be aware that not specifying
        *bbox_to_anchor* will use *parent_axes.bbox*, the units of which are
        in display (pixel) coordinates.

    axes_class : `~matplotlib.axes.Axes` type, default: `.HostAxes`
        The type of the newly created inset axes.

    axes_kwargs : dict, optional
        Keyword arguments to pass to the constructor of the inset axes.
        Valid arguments include:

        %(Axes:kwdoc)s

    borderpad : float, default: 0.5
        Padding between inset axes and the bbox_to_anchor.
        The units are axes font size, i.e. for a default font size of 10 points
        *borderpad = 0.5* is equivalent to a padding of 5 points.

    Returns
    -------
    inset_axes : *axes_class*
        Inset axes object created.
    """

    return _add_inset_axes(
        parent_axes, axes_class, axes_kwargs,
        AnchoredZoomLocator(
            parent_axes, zoom=zoom, loc=loc,
            bbox_to_anchor=bbox_to_anchor, bbox_transform=bbox_transform,
            borderpad=borderpad))



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axes_grid1/axes_divider.py
# Line: 28

def __init__(self, fig, pos, horizontal, vertical,
             aspect=None, anchor="C"):
    """
    Parameters
    ----------
    fig : Figure
    pos : tuple of 4 floats
        Position of the rectangle that will be divided.
    horizontal : list of :mod:`~mpl_toolkits.axes_grid1.axes_size`
        Sizes for horizontal division.
    vertical : list of :mod:`~mpl_toolkits.axes_grid1.axes_size`
        Sizes for vertical division.
    aspect : bool, optional
        Whether overall rectangular area is reduced so that the relative
        part of the horizontal and vertical scales have the same scale.
    anchor : (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', 'N', \

# ==================================================
# Line: 202

def _locate(self, nx, ny, nx1, ny1, axes, renderer):
    """
    Implementation of ``divider.new_locator().__call__``.

    The axes locator callable returned by ``new_locator()`` is created as
    a `functools.partial` of this method with *nx*, *ny*, *nx1*, and *ny1*
    specifying the requested cell.
    """
    nx += self._xrefindex
    nx1 += self._xrefindex
    ny += self._yrefindex
    ny1 += self._yrefindex

    fig_w, fig_h = self._fig.bbox.size / self._fig.dpi
    x, y, w, h = self.get_position_runtime(axes, renderer)

    hsizes = self.get_horizontal_sizes(renderer)
    vsizes = self.get_vertical_sizes(renderer)
    k_h = self._calc_k(hsizes, fig_w * w)
    k_v = self._calc_k(vsizes, fig_h * h)

    if self.get_aspect():
        k = min(k_h, k_v)
        ox = self._calc_offsets(hsizes, k)
        oy = self._calc_offsets(vsizes, k)

        ww = (ox[-1] - ox[0]) / fig_w
        hh = (oy[-1] - oy[0]) / fig_h
        pb = mtransforms.Bbox.from_bounds(x, y, w, h)
        pb1 = mtransforms.Bbox.from_bounds(x, y, ww, hh)
        x0, y0 = pb1.anchored(self.get_anchor(), pb).p0

    else:
        ox = self._calc_offsets(hsizes, k_h)
        oy = self._calc_offsets(vsizes, k_v)
        x0, y0 = x, y

    if nx1 is None:
        nx1 = -1
    if ny1 is None:
        ny1 = -1

    x1, w1 = x0 + ox[nx] / fig_w, (ox[nx1] - ox[nx]) / fig_w
    y1, h1 = y0 + oy[ny] / fig_h, (oy[ny1] - oy[ny]) / fig_h

    return mtransforms.Bbox.from_bounds(x1, y1, w1, h1)


# ==================================================
# Line: 483

def _locate(x, y, w, h, summed_widths, equal_heights, fig_w, fig_h, anchor):

    total_width = fig_w * w
    max_height = fig_h * h

    # Determine the k factors.
    n = len(equal_heights)
    eq_rels, eq_abss = equal_heights.T
    sm_rels, sm_abss = summed_widths.T
    A = np.diag([*eq_rels, 0])
    A[:n, -1] = -1
    A[-1, :-1] = sm_rels
    B = [*(-eq_abss), total_width - sm_abss.sum()]
    # A @ K = B: This finds factors {k_0, ..., k_{N-1}, H} so that
    #   eq_rel_i * k_i + eq_abs_i = H for all i: all axes have the same height
    #   sum(sm_rel_i * k_i + sm_abs_i) = total_width: fixed total width
    # (foo_rel_i * k_i + foo_abs_i will end up being the size of foo.)
    *karray, height = np.linalg.solve(A, B)
    if height > max_height:  # Additionally, upper-bound the height.
        karray = (max_height - eq_abss) / eq_rels

    # Compute the offsets corresponding to these factors.
    ox = np.cumsum([0, *(sm_rels * karray + sm_abss)])
    ww = (ox[-1] - ox[0]) / fig_w
    h0_rel, h0_abs = equal_heights[0]
    hh = (karray[0]*h0_rel + h0_abs) / fig_h
    pb = mtransforms.Bbox.from_bounds(x, y, w, h)
    pb1 = mtransforms.Bbox.from_bounds(x, y, ww, hh)
    x0, y0 = pb1.anchored(anchor, pb).p0

    return x0, y0, ox, hh



# ==================================================
# Line: 540

def _locate(self, nx, ny, nx1, ny1, axes, renderer):
    # docstring inherited
    nx += self._xrefindex
    nx1 += self._xrefindex
    fig_w, fig_h = self._fig.bbox.size / self._fig.dpi
    x, y, w, h = self.get_position_runtime(axes, renderer)
    summed_ws = self.get_horizontal_sizes(renderer)
    equal_hs = self.get_vertical_sizes(renderer)
    x0, y0, ox, hh = _locate(
        x, y, w, h, summed_ws, equal_hs, fig_w, fig_h, self.get_anchor())
    if nx1 is None:
        nx1 = -1
    x1, w1 = x0 + ox[nx] / fig_w, (ox[nx1] - ox[nx]) / fig_w
    y1, h1 = y0, hh
    return mtransforms.Bbox.from_bounds(x1, y1, w1, h1)



# ==================================================
# Line: 577

def _locate(self, nx, ny, nx1, ny1, axes, renderer):
    # docstring inherited
    ny += self._yrefindex
    ny1 += self._yrefindex
    fig_w, fig_h = self._fig.bbox.size / self._fig.dpi
    x, y, w, h = self.get_position_runtime(axes, renderer)
    summed_hs = self.get_vertical_sizes(renderer)
    equal_ws = self.get_horizontal_sizes(renderer)
    y0, x0, oy, ww = _locate(
        y, x, h, w, summed_hs, equal_ws, fig_h, fig_w, self.get_anchor())
    if ny1 is None:
        ny1 = -1
    x1, w1 = x0, ww
    y1, h1 = y0 + oy[ny] / fig_h, (oy[ny1] - oy[ny]) / fig_h
    return mtransforms.Bbox.from_bounds(x1, y1, w1, h1)



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_api/deprecation.py
# Line: 24

def _generate_deprecation_warning(
        since, message='', name='', alternative='', pending=False, obj_type='',
        addendum='', *, removal=''):
    if pending:
        if removal:
            raise ValueError("A pending deprecation cannot have a scheduled removal")
    elif removal == '':
        macro, meso, *_ = since.split('.')
        removal = f'{macro}.{int(meso) + 2}'
    if not message:
        message = (
            ("The %(name)s %(obj_type)s" if obj_type else "%(name)s") +
            (" will be deprecated in a future version" if pending else
             (" was deprecated in Matplotlib %(since)s" +
              (" and will be removed in %(removal)s" if removal else ""))) +
            "." +
            (" Use %(alternative)s instead." if alternative else "") +
            (" %(addendum)s" if addendum else ""))
    warning_cls = PendingDeprecationWarning if pending else MatplotlibDeprecationWarning
    return warning_cls(message % dict(
        func=name, name=name, obj_type=obj_type, since=since, removal=removal,
        alternative=alternative, addendum=addendum))



# ==================================================
# Line: 48

def warn_deprecated(
        since, *, message='', name='', alternative='', pending=False,
        obj_type='', addendum='', removal=''):
    """
    Display a standardized deprecation.

    Parameters
    ----------
    since : str
        The release at which this API became deprecated.
    message : str, optional
        Override the default deprecation message.  The ``%(since)s``,
        ``%(name)s``, ``%(alternative)s``, ``%(obj_type)s``, ``%(addendum)s``,
        and ``%(removal)s`` format specifiers will be replaced by the values
        of the respective arguments passed to this function.
    name : str, optional
        The name of the deprecated object.
    alternative : str, optional
        An alternative API that the user may use in place of the deprecated
        API.  The deprecation warning will tell the user about this alternative
        if provided.
    pending : bool, optional
        If True, uses a PendingDeprecationWarning instead of a
        DeprecationWarning.  Cannot be used together with *removal*.
    obj_type : str, optional
        The object type being deprecated.
    addendum : str, optional
        Additional text appended directly to the final message.
    removal : str, optional
        The expected removal version.  With the default (an empty string), a
        removal version is automatically computed from *since*.  Set to other
        Falsy values to not schedule a removal date.  Cannot be used together
        with *pending*.

    Examples
    --------
    ::

        # To warn of the deprecation of "matplotlib.name_of_module"
        warn_deprecated('1.4.0', name='matplotlib.name_of_module',
                        obj_type='module')
    """
    warning = _generate_deprecation_warning(
        since, message, name, alternative, pending, obj_type, addendum,
        removal=removal)
    from . import warn_external
    warn_external(warning, category=MatplotlibDeprecationWarning)



# ==================================================
# Line: 97

def deprecated(since, *, message='', name='', alternative='', pending=False,
               obj_type=None, addendum='', removal=''):
    """
    Decorator to mark a function, a class, or a property as deprecated.

    When deprecating a classmethod, a staticmethod, or a property, the
    ``@deprecated`` decorator should go *under* ``@classmethod`` and
    ``@staticmethod`` (i.e., `deprecated` should directly decorate the
    underlying callable), but *over* ``@property``.

    When deprecating a class ``C`` intended to be used as a base class in a
    multiple inheritance hierarchy, ``C`` *must* define an ``__init__`` method
    (if ``C`` instead inherited its ``__init__`` from its own base class, then
    ``@deprecated`` would mess up ``__init__`` inheritance when installing its
    own (deprecation-emitting) ``C.__init__``).

    Parameters are the same as for `warn_deprecated`, except that *obj_type*
    defaults to 'class' if decorating a class, 'attribute' if decorating a
    property, and 'function' otherwise.

    Examples
    --------
    ::

        @deprecated('1.4.0')
        def the_function_to_deprecate():
            pass
    """

    def deprecate(obj, message=message, name=name, alternative=alternative,
                  pending=pending, obj_type=obj_type, addendum=addendum):
        from matplotlib._api import classproperty

        if isinstance(obj, type):
            if obj_type is None:
                obj_type = "class"
            func = obj.__init__
            name = name or obj.__name__
            old_doc = obj.__doc__

            def finalize(wrapper, new_doc):
                try:
                    obj.__doc__ = new_doc
                except AttributeError:  # Can't set on some extension objects.
                    pass
                obj.__init__ = functools.wraps(obj.__init__)(wrapper)
                return obj

        elif isinstance(obj, (property, classproperty)):
            if obj_type is None:
                obj_type = "attribute"
            func = None
            name = name or obj.fget.__name__
            old_doc = obj.__doc__

            class _deprecated_property(type(obj)):
                def __get__(self, instance, owner=None):
                    if instance is not None or owner is not None \
                            and isinstance(self, classproperty):
                        emit_warning()
                    return super().__get__(instance, owner)

                def __set__(self, instance, value):
                    if instance is not None:
                        emit_warning()
                    return super().__set__(instance, value)

                def __delete__(self, instance):
                    if instance is not None:
                        emit_warning()
                    return super().__delete__(instance)

                def __set_name__(self, owner, set_name):
                    nonlocal name
                    if name == "<lambda>":
                        name = set_name

            def finalize(_, new_doc):
                return _deprecated_property(
                    fget=obj.fget, fset=obj.fset, fdel=obj.fdel, doc=new_doc)

        else:
            if obj_type is None:
                obj_type = "function"
            func = obj
            name = name or obj.__name__
            old_doc = func.__doc__

            def finalize(wrapper, new_doc):
                wrapper = functools.wraps(func)(wrapper)
                wrapper.__doc__ = new_doc
                return wrapper

        def emit_warning():
            warn_deprecated(
                since, message=message, name=name, alternative=alternative,
                pending=pending, obj_type=obj_type, addendum=addendum,
                removal=removal)

        def wrapper(*args, **kwargs):
            emit_warning()
            return func(*args, **kwargs)

        old_doc = inspect.cleandoc(old_doc or '').strip('\n')

        notes_header = '\nNotes\n-----'
        second_arg = ' '.join([t.strip() for t in
                               (message, f"Use {alternative} instead."
                                if alternative else "", addendum) if t])
        new_doc = (f"[*Deprecated*] {old_doc}\n"
                   f"{notes_header if notes_header not in old_doc else ''}\n"
                   f".. deprecated:: {since}\n"
                   f"   {second_arg}")

        if not old_doc:
            # This is to prevent a spurious 'unexpected unindent' warning from
            # docutils when the original docstring was blank.
            new_doc += r'\ '

        return finalize(wrapper, new_doc)

    return deprecate



# ==================================================
# Line: 126

def deprecate(obj, message=message, name=name, alternative=alternative,
              pending=pending, obj_type=obj_type, addendum=addendum):
    from matplotlib._api import classproperty

    if isinstance(obj, type):
        if obj_type is None:
            obj_type = "class"
        func = obj.__init__
        name = name or obj.__name__
        old_doc = obj.__doc__

        def finalize(wrapper, new_doc):
            try:
                obj.__doc__ = new_doc
            except AttributeError:  # Can't set on some extension objects.
                pass
            obj.__init__ = functools.wraps(obj.__init__)(wrapper)
            return obj

    elif isinstance(obj, (property, classproperty)):
        if obj_type is None:
            obj_type = "attribute"
        func = None
        name = name or obj.fget.__name__
        old_doc = obj.__doc__

        class _deprecated_property(type(obj)):
            def __get__(self, instance, owner=None):
                if instance is not None or owner is not None \
                        and isinstance(self, classproperty):
                    emit_warning()
                return super().__get__(instance, owner)

            def __set__(self, instance, value):
                if instance is not None:
                    emit_warning()
                return super().__set__(instance, value)

            def __delete__(self, instance):
                if instance is not None:
                    emit_warning()
                return super().__delete__(instance)

            def __set_name__(self, owner, set_name):
                nonlocal name
                if name == "<lambda>":
                    name = set_name

        def finalize(_, new_doc):
            return _deprecated_property(
                fget=obj.fget, fset=obj.fset, fdel=obj.fdel, doc=new_doc)

    else:
        if obj_type is None:
            obj_type = "function"
        func = obj
        name = name or obj.__name__
        old_doc = func.__doc__

        def finalize(wrapper, new_doc):
            wrapper = functools.wraps(func)(wrapper)
            wrapper.__doc__ = new_doc
            return wrapper

    def emit_warning():
        warn_deprecated(
            since, message=message, name=name, alternative=alternative,
            pending=pending, obj_type=obj_type, addendum=addendum,
            removal=removal)

    def wrapper(*args, **kwargs):
        emit_warning()
        return func(*args, **kwargs)

    old_doc = inspect.cleandoc(old_doc or '').strip('\n')

    notes_header = '\nNotes\n-----'
    second_arg = ' '.join([t.strip() for t in
                           (message, f"Use {alternative} instead."
                            if alternative else "", addendum) if t])
    new_doc = (f"[*Deprecated*] {old_doc}\n"
               f"{notes_header if notes_header not in old_doc else ''}\n"
               f".. deprecated:: {since}\n"
               f"   {second_arg}")

    if not old_doc:
        # This is to prevent a spurious 'unexpected unindent' warning from
        # docutils when the original docstring was blank.
        new_doc += r'\ '

    return finalize(wrapper, new_doc)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/lines.py
# Line: 301

def __init__(self, xdata, ydata, *,
             linewidth=None,  # all Nones default to rc
             linestyle=None,
             color=None,
             gapcolor=None,
             marker=None,
             markersize=None,
             markeredgewidth=None,
             markeredgecolor=None,
             markerfacecolor=None,
             markerfacecoloralt='none',
             fillstyle=None,
             antialiased=None,
             dash_capstyle=None,
             solid_capstyle=None,
             dash_joinstyle=None,
             solid_joinstyle=None,
             pickradius=5,
             drawstyle=None,
             markevery=None,
             **kwargs
             ):
    """
    Create a `.Line2D` instance with *x* and *y* data in sequences of
    *xdata*, *ydata*.

    Additional keyword arguments are `.Line2D` properties:

    %(Line2D:kwdoc)s

    See :meth:`set_linestyle` for a description of the line styles,
    :meth:`set_marker` for a description of the markers, and
    :meth:`set_drawstyle` for a description of the draw styles.

    """
    super().__init__()

    # Convert sequences to NumPy arrays.
    if not np.iterable(xdata):
        raise RuntimeError('xdata must be a sequence')
    if not np.iterable(ydata):
        raise RuntimeError('ydata must be a sequence')

    linewidth = mpl._val_or_rc(linewidth, 'lines.linewidth')
    linestyle = mpl._val_or_rc(linestyle, 'lines.linestyle')
    marker = mpl._val_or_rc(marker, 'lines.marker')
    color = mpl._val_or_rc(color, 'lines.color')
    markersize = mpl._val_or_rc(markersize, 'lines.markersize')
    antialiased = mpl._val_or_rc(antialiased, 'lines.antialiased')
    dash_capstyle = mpl._val_or_rc(dash_capstyle, 'lines.dash_capstyle')
    dash_joinstyle = mpl._val_or_rc(dash_joinstyle, 'lines.dash_joinstyle')
    solid_capstyle = mpl._val_or_rc(solid_capstyle, 'lines.solid_capstyle')
    solid_joinstyle = mpl._val_or_rc(solid_joinstyle, 'lines.solid_joinstyle')

    if drawstyle is None:
        drawstyle = 'default'

    self._dashcapstyle = None
    self._dashjoinstyle = None
    self._solidjoinstyle = None
    self._solidcapstyle = None
    self.set_dash_capstyle(dash_capstyle)
    self.set_dash_joinstyle(dash_joinstyle)
    self.set_solid_capstyle(solid_capstyle)
    self.set_solid_joinstyle(solid_joinstyle)

    self._linestyles = None
    self._drawstyle = None
    self._linewidth = linewidth
    self._unscaled_dash_pattern = (0, None)  # offset, dash
    self._dash_pattern = (0, None)  # offset, dash (scaled by linewidth)

    self.set_linewidth(linewidth)
    self.set_linestyle(linestyle)
    self.set_drawstyle(drawstyle)

    self._color = None
    self.set_color(color)
    if marker is None:
        marker = 'none'  # Default.
    if not isinstance(marker, MarkerStyle):
        self._marker = MarkerStyle(marker, fillstyle)
    else:
        self._marker = marker

    self._gapcolor = None
    self.set_gapcolor(gapcolor)

    self._markevery = None
    self._markersize = None
    self._antialiased = None

    self.set_markevery(markevery)
    self.set_antialiased(antialiased)
    self.set_markersize(markersize)

    self._markeredgecolor = None
    self._markeredgewidth = None
    self._markerfacecolor = None
    self._markerfacecoloralt = None

    self.set_markerfacecolor(markerfacecolor)  # Normalizes None to rc.
    self.set_markerfacecoloralt(markerfacecoloralt)
    self.set_markeredgecolor(markeredgecolor)  # Normalizes None to rc.
    self.set_markeredgewidth(markeredgewidth)

    # update kwargs before updating data to give the caller a
    # chance to init axes (and hence unit support)
    self._internal_update(kwargs)
    self.pickradius = pickradius
    self.ind_offset = 0
    if (isinstance(self._picker, Number) and
            not isinstance(self._picker, bool)):
        self._pickradius = self._picker

    self._xorig = np.asarray([])
    self._yorig = np.asarray([])
    self._invalidx = True
    self._invalidy = True
    self._x = None
    self._y = None
    self._xy = None
    self._path = None
    self._transformed_path = None
    self._subslice = False
    self._x_filled = None  # used in subslicing; only x is needed

    self.set_data(xdata, ydata)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/table.py
# Line: 58

def __init__(self, xy, width, height, *,
             edgecolor='k', facecolor='w',
             fill=True,
             text='',
             loc='right',
             fontproperties=None,
             visible_edges='closed',
             ):
    """
    Parameters
    ----------
    xy : 2-tuple
        The position of the bottom left corner of the cell.
    width : float
        The cell width.
    height : float
        The cell height.
    edgecolor : :mpltype:`color`, default: 'k'
        The color of the cell border.
    facecolor : :mpltype:`color`, default: 'w'
        The cell facecolor.
    fill : bool, default: True
        Whether the cell background is filled.
    text : str, optional
        The cell text.
    loc : {'right', 'center', 'left'}
        The alignment of the text within the cell.
    fontproperties : dict, optional
        A dict defining the font properties of the text. Supported keys and
        values are the keyword arguments accepted by `.FontProperties`.
    visible_edges : {'closed', 'open', 'horizontal', 'vertical'} or \

# ==================================================
# Line: 651

def table(ax,
          cellText=None, cellColours=None,
          cellLoc='right', colWidths=None,
          rowLabels=None, rowColours=None, rowLoc='left',
          colLabels=None, colColours=None, colLoc='center',
          loc='bottom', bbox=None, edges='closed',
          **kwargs):
    """
    Add a table to an `~.axes.Axes`.

    At least one of *cellText* or *cellColours* must be specified. These
    parameters must be 2D lists, in which the outer lists define the rows and
    the inner list define the column values per row. Each row must have the
    same number of elements.

    The table can optionally have row and column headers, which are configured
    using *rowLabels*, *rowColours*, *rowLoc* and *colLabels*, *colColours*,
    *colLoc* respectively.

    For finer grained control over tables, use the `.Table` class and add it to
    the Axes with `.Axes.add_table`.

    Parameters
    ----------
    cellText : 2D list of str or pandas.DataFrame, optional
        The texts to place into the table cells.

        *Note*: Line breaks in the strings are currently not accounted for and
        will result in the text exceeding the cell boundaries.

    cellColours : 2D list of :mpltype:`color`, optional
        The background colors of the cells.

    cellLoc : {'right', 'center', 'left'}
        The alignment of the text within the cells.

    colWidths : list of float, optional
        The column widths in units of the axes. If not given, all columns will
        have a width of *1 / ncols*.

    rowLabels : list of str, optional
        The text of the row header cells.

    rowColours : list of :mpltype:`color`, optional
        The colors of the row header cells.

    rowLoc : {'left', 'center', 'right'}
        The text alignment of the row header cells.

    colLabels : list of str, optional
        The text of the column header cells.

    colColours : list of :mpltype:`color`, optional
        The colors of the column header cells.

    colLoc : {'center', 'left', 'right'}
        The text alignment of the column header cells.

    loc : str, default: 'bottom'
        The position of the cell with respect to *ax*. This must be one of
        the `~.Table.codes`.

    bbox : `.Bbox` or [xmin, ymin, width, height], optional
        A bounding box to draw the table into. If this is not *None*, this
        overrides *loc*.

    edges : {'closed', 'open', 'horizontal', 'vertical'} or substring of 'BRTL'
        The cell edges to be drawn with a line. See also
        `~.Cell.visible_edges`.

    Returns
    -------
    `~matplotlib.table.Table`
        The created table.

    Other Parameters
    ----------------
    **kwargs
        `.Table` properties.

    %(Table:kwdoc)s
    """

    if cellColours is None and cellText is None:
        raise ValueError('At least one argument from "cellColours" or '
                         '"cellText" must be provided to create a table.')

    # Check we have some cellText
    if cellText is None:
        # assume just colours are needed
        rows = len(cellColours)
        cols = len(cellColours[0])
        cellText = [[''] * cols] * rows

    # Check if we have a Pandas DataFrame
    if _is_pandas_dataframe(cellText):
        # if rowLabels/colLabels are empty, use DataFrame entries.
        # Otherwise, throw an error.
        if rowLabels is None:
            rowLabels = cellText.index
        else:
            raise ValueError("rowLabels cannot be used alongside Pandas DataFrame")
        if colLabels is None:
            colLabels = cellText.columns
        else:
            raise ValueError("colLabels cannot be used alongside Pandas DataFrame")
        # Update cellText with only values
        cellText = cellText.values

    rows = len(cellText)
    cols = len(cellText[0])
    for row in cellText:
        if len(row) != cols:
            raise ValueError(f"Each row in 'cellText' must have {cols} "
                             "columns")

    if cellColours is not None:
        if len(cellColours) != rows:
            raise ValueError(f"'cellColours' must have {rows} rows")
        for row in cellColours:
            if len(row) != cols:
                raise ValueError("Each row in 'cellColours' must have "
                                 f"{cols} columns")
    else:
        cellColours = ['w' * cols] * rows

    # Set colwidths if not given
    if colWidths is None:
        colWidths = [1.0 / cols] * cols

    # Fill in missing information for column
    # and row labels
    rowLabelWidth = 0
    if rowLabels is None:
        if rowColours is not None:
            rowLabels = [''] * rows
            rowLabelWidth = colWidths[0]
    elif rowColours is None:
        rowColours = 'w' * rows

    if rowLabels is not None:
        if len(rowLabels) != rows:
            raise ValueError(f"'rowLabels' must be of length {rows}")

    # If we have column labels, need to shift
    # the text and colour arrays down 1 row
    offset = 1
    if colLabels is None:
        if colColours is not None:
            colLabels = [''] * cols
        else:
            offset = 0
    elif colColours is None:
        colColours = 'w' * cols

    # Set up cell colours if not given
    if cellColours is None:
        cellColours = ['w' * cols] * rows

    # Now create the table
    table = Table(ax, loc, bbox, **kwargs)
    table.edges = edges
    height = table._approx_text_height()

    # Add the cells
    for row in range(rows):
        for col in range(cols):
            table.add_cell(row + offset, col,
                           width=colWidths[col], height=height,
                           text=cellText[row][col],
                           facecolor=cellColours[row][col],
                           loc=cellLoc)
    # Do column labels
    if colLabels is not None:
        for col in range(cols):
            table.add_cell(0, col,
                           width=colWidths[col], height=height,
                           text=colLabels[col], facecolor=colColours[col],
                           loc=colLoc)

    # Do row labels
    if rowLabels is not None:
        for row in range(rows):
            table.add_cell(row + offset, -1,
                           width=rowLabelWidth or 1e-15, height=height,
                           text=rowLabels[row], facecolor=rowColours[row],
                           loc=rowLoc)
        if rowLabelWidth == 0:
            table.auto_set_column_width(-1)

    # set_fontsize is only effective after cells are added
    if "fontsize" in kwargs:
        table.set_fontsize(kwargs["fontsize"])

    ax.add_table(table)
    return table

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/collections.py
# Line: 79

def __init__(self, *,
             edgecolors=None,
             facecolors=None,
             hatchcolors=None,
             linewidths=None,
             linestyles='solid',
             capstyle=None,
             joinstyle=None,
             antialiaseds=None,
             offsets=None,
             offset_transform=None,
             norm=None,  # optional for ScalarMappable
             cmap=None,  # ditto
             colorizer=None,
             pickradius=5.0,
             hatch=None,
             urls=None,
             zorder=1,
             **kwargs
             ):
    """
    Parameters
    ----------
    edgecolors : :mpltype:`color` or list of colors, default: :rc:`patch.edgecolor`
        Edge color for each patch making up the collection. The special
        value 'face' can be passed to make the edgecolor match the
        facecolor.
    facecolors : :mpltype:`color` or list of colors, default: :rc:`patch.facecolor`
        Face color for each patch making up the collection.
    hatchcolors : :mpltype:`color` or list of colors, default: :rc:`hatch.color`
        Hatch color for each patch making up the collection. The color
        can be set to the special value 'edge' to make the hatchcolor match the
        edgecolor.
    linewidths : float or list of floats, default: :rc:`patch.linewidth`
        Line width for each patch making up the collection.
    linestyles : str or tuple or list thereof, default: 'solid'
        Valid strings are ['solid', 'dashed', 'dashdot', 'dotted', '-',
        '--', '-.', ':']. Dash tuples should be of the form::

            (offset, onoffseq),

        where *onoffseq* is an even length tuple of on and off ink lengths
        in points. For examples, see
        :doc:`/gallery/lines_bars_and_markers/linestyles`.
    capstyle : `.CapStyle`-like, default: 'butt'
        Style to use for capping lines for all paths in the collection.
        Allowed values are %(CapStyle)s.
    joinstyle : `.JoinStyle`-like, default: 'round'
        Style to use for joining lines for all paths in the collection.
        Allowed values are %(JoinStyle)s.
    antialiaseds : bool or list of bool, default: :rc:`patch.antialiased`
        Whether each patch in the collection should be drawn with
        antialiasing.
    offsets : (float, float) or list thereof, default: (0, 0)
        A vector by which to translate each patch after rendering (default
        is no translation). The translation is performed in screen (pixel)
        coordinates (i.e. after the Artist's transform is applied).
    offset_transform : `~.Transform`, default: `.IdentityTransform`
        A single transform which will be applied to each *offsets* vector
        before it is used.
    cmap, norm
        Data normalization and colormapping parameters. See
        `.ScalarMappable` for a detailed description.
    hatch : str, optional
        Hatching pattern to use in filled paths, if any. Valid strings are
        ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']. See
        :doc:`/gallery/shapes_and_collections/hatch_style_reference` for
        the meaning of each hatch type.
    pickradius : float, default: 5.0
        If ``pickradius <= 0``, then `.Collection.contains` will return
        ``True`` whenever the test point is inside of one of the polygons
        formed by the control points of a Path in the Collection. On the
        other hand, if it is greater than 0, then we instead check if the
        test point is contained in a stroke of width ``2*pickradius``
        following any of the Paths in the Collection.
    urls : list of str, default: None
        A URL for each patch to link to once drawn. Currently only works
        for the SVG backend. See :doc:`/gallery/misc/hyperlinks_sgskip` for
        examples.
    zorder : float, default: 1
        The drawing order, shared by all Patches in the Collection. See
        :doc:`/gallery/misc/zorder_demo` for all defaults and examples.
    **kwargs
        Remaining keyword arguments will be used to set properties as
        ``Collection.set_{key}(val)`` for each key-value pair in *kwargs*.
    """

    super().__init__(self._get_colorizer(cmap, norm, colorizer))
    # list of un-scaled dash patterns
    # this is needed scaling the dash pattern by linewidth
    self._us_linestyles = [(0, None)]
    # list of dash patterns
    self._linestyles = [(0, None)]
    # list of unbroadcast/scaled linewidths
    self._us_lw = [0]
    self._linewidths = [0]

    self._gapcolor = None  # Currently only used by LineCollection.

    # Flags set by _set_mappable_flags: are colors from mapping an array?
    self._face_is_mapped = None
    self._edge_is_mapped = None
    self._mapped_colors = None  # calculated in update_scalarmappable
    self._hatch_linewidth = mpl.rcParams['hatch.linewidth']
    self.set_facecolor(facecolors)
    self.set_edgecolor(edgecolors)
    self.set_linewidth(linewidths)
    self.set_linestyle(linestyles)
    self.set_antialiased(antialiaseds)
    self.set_pickradius(pickradius)
    self.set_urls(urls)
    self.set_hatch(hatch)
    self.set_hatchcolor(hatchcolors)
    self.set_zorder(zorder)

    if capstyle:
        self.set_capstyle(capstyle)
    else:
        self._capstyle = None

    if joinstyle:
        self.set_joinstyle(joinstyle)
    else:
        self._joinstyle = None

    if offsets is not None:
        offsets = np.asanyarray(offsets, float)
        # Broadcast (2,) -> (1, 2) but nothing else.
        if offsets.shape == (2,):
            offsets = offsets[None, :]

    self._offsets = offsets
    self._offset_transform = offset_transform

    self._path_effects = None
    self._internal_update(kwargs)
    self._paths = None


# ==================================================
# Line: 1361

def __init__(
        self, t_direction, t, f1, f2, *,
        where=None, interpolate=False, step=None, **kwargs):
    """
    Parameters
    ----------
    t_direction : {{'x', 'y'}}
        The axes on which the variable lies.

        - 'x': the curves are ``(t, f1)`` and ``(t, f2)``.
        - 'y': the curves are ``(f1, t)`` and ``(f2, t)``.

    t : array-like
        The ``t_direction`` coordinates of the nodes defining the curves.

    f1 : array-like or float
        The other coordinates of the nodes defining the first curve.

    f2 : array-like or float
        The other coordinates of the nodes defining the second curve.

    where : array-like of bool, optional
        Define *where* to exclude some {dir} regions from being filled.
        The filled regions are defined by the coordinates ``t[where]``.
        More precisely, fill between ``t[i]`` and ``t[i+1]`` if
        ``where[i] and where[i+1]``.  Note that this definition implies
        that an isolated *True* value between two *False* values in *where*
        will not result in filling.  Both sides of the *True* position
        remain unfilled due to the adjacent *False* values.

    interpolate : bool, default: False
        This option is only relevant if *where* is used and the two curves
        are crossing each other.

        Semantically, *where* is often used for *f1* > *f2* or
        similar.  By default, the nodes of the polygon defining the filled
        region will only be placed at the positions in the *t* array.
        Such a polygon cannot describe the above semantics close to the
        intersection.  The t-sections containing the intersection are
        simply clipped.

        Setting *interpolate* to *True* will calculate the actual
        intersection point and extend the filled region up to this point.

    step : {{'pre', 'post', 'mid'}}, optional
        Define *step* if the filling should be a step function,
        i.e. constant in between *t*.  The value determines where the
        step will occur:

        - 'pre': The f value is continued constantly to the left from
          every *t* position, i.e. the interval ``(t[i-1], t[i]]`` has the
          value ``f[i]``.
        - 'post': The y value is continued constantly to the right from
          every *x* position, i.e. the interval ``[t[i], t[i+1])`` has the
          value ``f[i]``.
        - 'mid': Steps occur half-way between the *t* positions.

    **kwargs
        Forwarded to `.PolyCollection`.

    See Also
    --------
    .Axes.fill_between, .Axes.fill_betweenx
    """
    self.t_direction = t_direction
    self._interpolate = interpolate
    self._step = step
    verts = self._make_verts(t, f1, f2, where)
    super().__init__(verts, **kwargs)


# ==================================================
# Line: 1871

def __init__(self,
             positions,  # Cannot be None.
             orientation='horizontal',
             *,
             lineoffset=0,
             linelength=1,
             linewidth=None,
             color=None,
             linestyle='solid',
             antialiased=None,
             **kwargs
             ):
    """
    Parameters
    ----------
    positions : 1D array-like
        Each value is an event.
    orientation : {'horizontal', 'vertical'}, default: 'horizontal'
        The sequence of events is plotted along this direction.
        The marker lines of the single events are along the orthogonal
        direction.
    lineoffset : float, default: 0
        The offset of the center of the markers from the origin, in the
        direction orthogonal to *orientation*.
    linelength : float, default: 1
        The total height of the marker (i.e. the marker stretches from
        ``lineoffset - linelength/2`` to ``lineoffset + linelength/2``).
    linewidth : float or list thereof, default: :rc:`lines.linewidth`
        The line width of the event lines, in points.
    color : :mpltype:`color` or list of :mpltype:`color`, default: :rc:`lines.color`
        The color of the event lines.
    linestyle : str or tuple or list thereof, default: 'solid'
        Valid strings are ['solid', 'dashed', 'dashdot', 'dotted',
        '-', '--', '-.', ':']. Dash tuples should be of the form::

            (offset, onoffseq),

        where *onoffseq* is an even length tuple of on and off ink
        in points.
    antialiased : bool or list thereof, default: :rc:`lines.antialiased`
        Whether to use antialiasing for drawing the lines.
    **kwargs
        Forwarded to `.LineCollection`.

    Examples
    --------
    .. plot:: gallery/lines_bars_and_markers/eventcollection_demo.py
    """
    super().__init__([],
                     linewidths=linewidth, linestyles=linestyle,
                     colors=color, antialiaseds=antialiased,
                     **kwargs)
    self._is_horizontal = True  # Initial value, may be switched below.
    self._linelength = linelength
    self._lineoffset = lineoffset
    self.set_orientation(orientation)
    self.set_positions(positions)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/layout_engine.py
# Line: 225

def __init__(self, *, h_pad=None, w_pad=None,
             hspace=None, wspace=None, rect=(0, 0, 1, 1),
             compress=False, **kwargs):
    """
    Initialize ``constrained_layout`` settings.

    Parameters
    ----------
    h_pad, w_pad : float
        Padding around the Axes elements in inches.
        Default to :rc:`figure.constrained_layout.h_pad` and
        :rc:`figure.constrained_layout.w_pad`.
    hspace, wspace : float
        Fraction of the figure to dedicate to space between the
        axes.  These are evenly spread between the gaps between the Axes.
        A value of 0.2 for a three-column layout would have a space
        of 0.1 of the figure width between each column.
        If h/wspace < h/w_pad, then the pads are used instead.
        Default to :rc:`figure.constrained_layout.hspace` and
        :rc:`figure.constrained_layout.wspace`.
    rect : tuple of 4 floats
        Rectangle in figure coordinates to perform constrained layout in
        (left, bottom, width, height), each from 0-1.
    compress : bool
        Whether to shift Axes so that white space in between them is
        removed. This is useful for simple grids of fixed-aspect Axes (e.g.
        a grid of images).  See :ref:`compressed_layout`.
    """
    super().__init__(**kwargs)
    # set the defaults:
    self.set(w_pad=mpl.rcParams['figure.constrained_layout.w_pad'],
             h_pad=mpl.rcParams['figure.constrained_layout.h_pad'],
             wspace=mpl.rcParams['figure.constrained_layout.wspace'],
             hspace=mpl.rcParams['figure.constrained_layout.hspace'],
             rect=(0, 0, 1, 1))
    # set anything that was passed in (None will be ignored):
    self.set(w_pad=w_pad, h_pad=h_pad, wspace=wspace, hspace=hspace,
             rect=rect)
    self._compress = compress


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_template.py
# Line: 82

def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):
    pass


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_agg.py
# Line: 173

def draw_mathtext(self, gc, x, y, s, prop, angle):
    """Draw mathtext using :mod:`matplotlib.mathtext`."""
    ox, oy, width, height, descent, font_image = \
        self.mathtext_parser.parse(s, self.dpi, prop,
                                   antialiased=gc.get_antialiased())

    xd = descent * sin(radians(angle))
    yd = descent * cos(radians(angle))
    x = round(x + ox + xd)
    y = round(y - oy + yd)
    self._renderer.draw_text_image(font_image, x, y + 1, angle, gc)


# ==================================================
# Line: 185

def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):
    # docstring inherited
    if ismath:
        return self.draw_mathtext(gc, x, y, s, prop, angle)
    font = self._prepare_font(prop)
    # We pass '0' for angle here, since it will be rotated (in raster
    # space) in the following call to draw_text_image).
    font.set_text(s, 0, flags=get_hinting_flag())
    font.draw_glyphs_to_bitmap(
        antialiased=gc.get_antialiased())
    d = font.get_descent() / 64.0
    # The descent needs to be adjusted for the angle.
    xo, yo = font.get_bitmap_offset()
    xo /= 64.0
    yo /= 64.0
    xd = d * sin(radians(angle))
    yd = d * cos(radians(angle))
    x = round(x + xo + xd)
    y = round(y + yo + yd)
    self._renderer.draw_text_image(font, x, y + 1, angle, gc)


# ==================================================
# Line: 227

def draw_tex(self, gc, x, y, s, prop, angle, *, mtext=None):
    # docstring inherited
    # todo, handle props, angle, origins
    size = prop.get_size_in_points()

    texmanager = self.get_texmanager()

    Z = texmanager.get_grey(s, size, self.dpi)
    Z = np.array(Z * 255.0, np.uint8)

    w, h, d = self.get_text_width_height_descent(s, prop, ismath="TeX")
    xd = d * sin(radians(angle))
    yd = d * cos(radians(angle))
    x = round(x + xd)
    y = round(y + yd)
    self._renderer.draw_text_image(Z, x, y, angle, gc)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_mixed.py
# Line: 16

def __init__(self, figure, width, height, dpi, vector_renderer,
             raster_renderer_class=None,
             bbox_inches_restore=None):
    """
    Parameters
    ----------
    figure : `~matplotlib.figure.Figure`
        The figure instance.
    width : float
        The width of the canvas in logical units
    height : float
        The height of the canvas in logical units
    dpi : float
        The dpi of the canvas
    vector_renderer : `~matplotlib.backend_bases.RendererBase`
        An instance of a subclass of
        `~matplotlib.backend_bases.RendererBase` that will be used for the
        vector drawing.
    raster_renderer_class : `~matplotlib.backend_bases.RendererBase`
        The renderer class to use for the raster drawing.  If not provided,
        this will use the Agg backend (which is currently the only viable
        option anyway.)

    """
    if raster_renderer_class is None:
        raster_renderer_class = RendererAgg

    self._raster_renderer_class = raster_renderer_class
    self._width = width
    self._height = height
    self.dpi = dpi

    self._vector_renderer = vector_renderer

    self._raster_renderer = None

    # A reference to the figure is needed as we need to change
    # the figure dpi before and after the rasterization. Although
    # this looks ugly, I couldn't find a better solution. -JJL
    self.figure = figure
    self._figdpi = figure.dpi

    self._bbox_inches_restore = bbox_inches_restore

    self._renderer = vector_renderer


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/_backend_tk.py
# Line: 997

def add_toolitem(
        self, name, group, position, image_file, description, toggle):
    frame = self._get_groupframe(group)
    buttons = frame.pack_slaves()
    if position >= len(buttons) or position < 0:
        before = None
    else:
        before = buttons[position]
    button = NavigationToolbar2Tk._Button(frame, name, image_file, toggle,
                                          lambda: self._button_click(name))
    button.pack_configure(before=before)
    if description is not None:
        add_tooltip(button, description)
    self._toolitems.setdefault(name, [])
    self._toolitems[name].append(button)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_cairo.py
# Line: 156

def draw_markers(self, gc, marker_path, marker_trans, path, transform,
                 rgbFace=None):
    # docstring inherited

    ctx = gc.ctx
    ctx.new_path()
    # Create the path for the marker; it needs to be flipped here already!
    _append_path(ctx, marker_path, marker_trans + Affine2D().scale(1, -1))
    marker_path = ctx.copy_path_flat()

    # Figure out whether the path has a fill
    x1, y1, x2, y2 = ctx.fill_extents()
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        filled = False
        # No fill, just unset this (so we don't try to fill it later on)
        rgbFace = None
    else:
        filled = True

    transform = (transform
                 + Affine2D().scale(1, -1).translate(0, self.height))

    ctx.new_path()
    for i, (vertices, codes) in enumerate(
            path.iter_segments(transform, simplify=False)):
        if len(vertices):
            x, y = vertices[-2:]
            ctx.save()

            # Translate and apply path
            ctx.translate(x, y)
            ctx.append_path(marker_path)

            ctx.restore()

            # Slower code path if there is a fill; we need to draw
            # the fill and stroke for each marker at the same time.
            # Also flush out the drawing every once in a while to
            # prevent the paths from getting way too long.
            if filled or i % 1000 == 0:
                self._fill_and_stroke(
                    ctx, rgbFace, gc.get_alpha(), gc.get_forced_alpha())

    # Fast path, if there is no fill, draw everything in one step
    if not filled:
        self._fill_and_stroke(
            ctx, rgbFace, gc.get_alpha(), gc.get_forced_alpha())


# ==================================================
# Line: 217

def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):
    # docstring inherited

    # Note: (x, y) are device/display coords, not user-coords, unlike other
    # draw_* methods
    if ismath:
        self._draw_mathtext(gc, x, y, s, prop, angle)

    else:
        ctx = gc.ctx
        ctx.new_path()
        ctx.move_to(x, y)

        ctx.save()
        ctx.select_font_face(*_cairo_font_args_from_font_prop(prop))
        ctx.set_font_size(self.points_to_pixels(prop.get_size_in_points()))
        opts = cairo.FontOptions()
        opts.set_antialias(gc.get_antialiased())
        ctx.set_font_options(opts)
        if angle:
            ctx.rotate(np.deg2rad(-angle))
        ctx.show_text(s)
        ctx.restore()


# ==================================================
# Line: 241

def _draw_mathtext(self, gc, x, y, s, prop, angle):
    ctx = gc.ctx
    width, height, descent, glyphs, rects = \
        self._text2path.mathtext_parser.parse(s, self.dpi, prop)

    ctx.save()
    ctx.translate(x, y)
    if angle:
        ctx.rotate(np.deg2rad(-angle))

    for font, fontsize, idx, ox, oy in glyphs:
        ctx.new_path()
        ctx.move_to(ox, -oy)
        ctx.select_font_face(
            *_cairo_font_args_from_font_prop(ttfFontProperty(font)))
        ctx.set_font_size(self.points_to_pixels(fontsize))
        ctx.show_text(chr(idx))

    for ox, oy, w, h in rects:
        ctx.new_path()
        ctx.rectangle(ox, -oy, w, -h)
        ctx.set_source_rgb(0, 0, 0)
        ctx.fill_preserve()

    ctx.restore()


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_wx.py
# Line: 226

def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):
    # docstring inherited

    if ismath:
        s = cbook.strip_math(s)
    _log.debug("%s - draw_text()", type(self))
    gc.select()
    self.handle_clip_rectangle(gc)
    gfx_ctx = gc.gfx_ctx

    font = self.get_wx_font(s, prop)
    color = gc.get_wxcolour(gc.get_rgb())
    gfx_ctx.SetFont(font, color)

    w, h, d = self.get_text_width_height_descent(s, prop, ismath)
    x = int(x)
    y = int(y - h)

    if angle == 0.0:
        gfx_ctx.DrawText(s, x, y)
    else:
        rads = math.radians(angle)
        xo = h * math.sin(rads)
        yo = h * math.cos(rads)
        gfx_ctx.DrawRotatedText(s, x - xo, y - yo, rads)

    gc.unselect()


# ==================================================
# Line: 1221

def add_toolitem(self, name, group, position, image_file, description,
                 toggle):
    # Find or create the separator that follows this group.
    if group not in self._groups:
        self._groups[group] = self.InsertSeparator(
            self._get_tool_pos(self._space))
    sep = self._groups[group]
    # List all separators.
    seps = [t for t in map(self.GetToolByPos, range(self.ToolsCount))
            if t.IsSeparator() and not t.IsStretchableSpace()]
    # Find where to insert the tool.
    if position >= 0:
        # Find the start of the group by looking for the separator
        # preceding this one; then move forward from it.
        start = (0 if sep == seps[0]
                 else self._get_tool_pos(seps[seps.index(sep) - 1]) + 1)
    else:
        # Move backwards from this separator.
        start = self._get_tool_pos(sep) + 1
    idx = start + position
    if image_file:
        bmp = NavigationToolbar2Wx._icon(image_file)
        kind = wx.ITEM_NORMAL if not toggle else wx.ITEM_CHECK
        tool = self.InsertTool(idx, -1, name, bmp, wx.NullBitmap, kind,
                               description or "")
    else:
        size = (self.GetTextExtent(name)[0] + 10, -1)
        if toggle:
            control = wx.ToggleButton(self, -1, name, size=size)
        else:
            control = wx.Button(self, -1, name, size=size)
        tool = self.InsertControl(idx, control, label=name)
    self.Realize()

    def handler(event):
        self.trigger_tool(name)

    if image_file:
        self.Bind(wx.EVT_TOOL, handler, tool)
    else:
        control.Bind(wx.EVT_LEFT_DOWN, handler)

    self._toolitems.setdefault(name, [])
    self._toolitems[name].append((tool, handler))


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/qt_editor/_formlayout.py
# Line: 421

def __init__(self, data, title="", comment="",
             icon=None, parent=None, apply=None):
    super().__init__(parent)

    self.apply_callback = apply

    # Form
    if isinstance(data[0][0], (list, tuple)):
        self.formwidget = FormTabWidget(data, comment=comment,
                                        parent=self)
    elif len(data[0]) == 3:
        self.formwidget = FormComboWidget(data, comment=comment,
                                          parent=self)
    else:
        self.formwidget = FormWidget(data, comment=comment,
                                     parent=self)
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(self.formwidget)

    self.float_fields = []
    self.formwidget.setup()

    # Button box
    self.bbox = bbox = QtWidgets.QDialogButtonBox(
        QtWidgets.QDialogButtonBox.StandardButton(
                _to_int(QtWidgets.QDialogButtonBox.StandardButton.Ok) |
                _to_int(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        ))
    self.formwidget.update_buttons.connect(self.update_buttons)
    if self.apply_callback is not None:
        apply_btn = bbox.addButton(
            QtWidgets.QDialogButtonBox.StandardButton.Apply)
        apply_btn.clicked.connect(self.apply)

    bbox.accepted.connect(self.accept)
    bbox.rejected.connect(self.reject)
    layout.addWidget(bbox)

    self.setLayout(layout)

    self.setWindowTitle(title)
    if not isinstance(icon, QtGui.QIcon):
        icon = QtWidgets.QWidget().style().standardIcon(
            QtWidgets.QStyle.SP_MessageBoxQuestion)
    self.setWindowIcon(icon)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_gtk4.py
# Line: 450

def add_toolitem(self, name, group, position, image_file, description,
                 toggle):
    if toggle:
        button = Gtk.ToggleButton()
    else:
        button = Gtk.Button()
    button.set_label(name)
    button.add_css_class('flat')

    if image_file is not None:
        image = Gtk.Image.new_from_gicon(
            Gio.Icon.new_for_string(image_file))
        button.set_child(image)
        button.add_css_class('image-button')

    if position is None:
        position = -1

    self._add_button(button, group, position)
    signal = button.connect('clicked', self._call_tool, name)
    button.set_tooltip_text(description)
    self._toolitems.setdefault(name, [])
    self._toolitems[name].append((button, signal))


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_ps.py
# Line: 620

def draw_markers(
        self, gc, marker_path, marker_trans, path, trans, rgbFace=None):
    # docstring inherited

    ps_color = (
        None
        if self._is_transparent(rgbFace)
        else f'{_nums_to_str(rgbFace[0])} setgray'
        if rgbFace[0] == rgbFace[1] == rgbFace[2]
        else f'{_nums_to_str(*rgbFace[:3])} setrgbcolor')

    # construct the generic marker command:

    # don't want the translate to be global
    ps_cmd = ['/o {', 'gsave', 'newpath', 'translate']

    lw = gc.get_linewidth()
    alpha = (gc.get_alpha()
             if gc.get_forced_alpha() or len(gc.get_rgb()) == 3
             else gc.get_rgb()[3])
    stroke = lw > 0 and alpha > 0
    if stroke:
        ps_cmd.append('%.1f setlinewidth' % lw)
        ps_cmd.append(self._linejoin_cmd(gc.get_joinstyle()))
        ps_cmd.append(self._linecap_cmd(gc.get_capstyle()))

    ps_cmd.append(self._convert_path(marker_path, marker_trans,
                                     simplify=False))

    if rgbFace:
        if stroke:
            ps_cmd.append('gsave')
        if ps_color:
            ps_cmd.extend([ps_color, 'fill'])
        if stroke:
            ps_cmd.append('grestore')

    if stroke:
        ps_cmd.append('stroke')
    ps_cmd.extend(['grestore', '} bind def'])

    for vertices, code in path.iter_segments(
            trans,
            clip=(0, 0, self.width*72, self.height*72),
            simplify=False):
        if len(vertices):
            x, y = vertices[-2:]
            ps_cmd.append(f"{x:g} {y:g} o")

    ps = '\n'.join(ps_cmd)
    self._draw_ps(ps, gc, rgbFace, fill=False, stroke=False)


# ==================================================
# Line: 673

def draw_path_collection(self, gc, master_transform, paths, all_transforms,
                         offsets, offset_trans, facecolors, edgecolors,
                         linewidths, linestyles, antialiaseds, urls,
                         offset_position, *, hatchcolors=None):
    if hatchcolors is None:
        hatchcolors = []
    # Is the optimization worth it? Rough calculation:
    # cost of emitting a path in-line is
    #     (len_path + 2) * uses_per_path
    # cost of definition+use is
    #     (len_path + 3) + 3 * uses_per_path
    len_path = len(paths[0].vertices) if len(paths) > 0 else 0
    uses_per_path = self._iter_collection_uses_per_path(
        paths, all_transforms, offsets, facecolors, edgecolors)
    should_do_optimization = \
        len_path + 3 * uses_per_path + 3 < (len_path + 2) * uses_per_path
    if not should_do_optimization:
        return RendererBase.draw_path_collection(
            self, gc, master_transform, paths, all_transforms,
            offsets, offset_trans, facecolors, edgecolors,
            linewidths, linestyles, antialiaseds, urls,
            offset_position, hatchcolors=hatchcolors)

    path_codes = []
    for i, (path, transform) in enumerate(self._iter_collection_raw_paths(
            master_transform, paths, all_transforms)):
        name = 'p%d_%d' % (self._path_collection_id, i)
        path_bytes = self._convert_path(path, transform, simplify=False)
        self._pswriter.write(f"""\

# ==================================================
# Line: 720

def draw_tex(self, gc, x, y, s, prop, angle, *, mtext=None):
    # docstring inherited
    if self._is_transparent(gc.get_rgb()):
        return  # Special handling for fully transparent.

    if not hasattr(self, "psfrag"):
        self._logwarn_once(
            "The PS backend determines usetex status solely based on "
            "rcParams['text.usetex'] and does not support having "
            "usetex=True only for some elements; this element will thus "
            "be rendered as if usetex=False.")
        self.draw_text(gc, x, y, s, prop, angle, False, mtext)
        return

    w, h, bl = self.get_text_width_height_descent(s, prop, ismath="TeX")
    fontsize = prop.get_size_in_points()
    thetext = 'psmarker%d' % self.textcnt
    color = _nums_to_str(*gc.get_rgb()[:3], sep=',')
    fontcmd = {'sans-serif': r'{\sffamily %s}',
               'monospace': r'{\ttfamily %s}'}.get(
                   mpl.rcParams['font.family'][0], r'{\rmfamily %s}')
    s = fontcmd % s
    tex = r'\color[rgb]{%s} %s' % (color, s)

    # Stick to bottom-left alignment, so subtract descent from the text-normal
    # direction since text is normally positioned by its baseline.
    rangle = np.radians(angle + 90)
    pos = _nums_to_str(x - bl * np.cos(rangle), y - bl * np.sin(rangle))
    self.psfrag.append(
        r'\psfrag{%s}[bl][bl][1][%f]{\fontsize{%f}{%f}%s}' % (
            thetext, angle, fontsize, fontsize*1.25, tex))

    self._pswriter.write(f"""\

# ==================================================
# Line: 762

def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):
    # docstring inherited

    if self._is_transparent(gc.get_rgb()):
        return  # Special handling for fully transparent.

    if ismath == 'TeX':
        return self.draw_tex(gc, x, y, s, prop, angle)

    if ismath:
        return self.draw_mathtext(gc, x, y, s, prop, angle)

    stream = []  # list of (ps_name, x, char_name)

    if mpl.rcParams['ps.useafm']:
        font = self._get_font_afm(prop)
        ps_name = (font.postscript_name.encode("ascii", "replace")
                    .decode("ascii"))
        scale = 0.001 * prop.get_size_in_points()
        thisx = 0
        last_name = None  # kerns returns 0 for None.
        for c in s:
            name = uni2type1.get(ord(c), f"uni{ord(c):04X}")
            try:
                width = font.get_width_from_char_name(name)
            except KeyError:
                name = 'question'
                width = font.get_width_char(ord('?'))
            kern = font.get_kern_dist_from_name(last_name, name)
            last_name = name
            thisx += kern * scale
            stream.append((ps_name, thisx, name))
            thisx += width * scale

    else:
        font = self._get_font_ttf(prop)
        self._character_tracker.track(font, s)
        for item in _text_helpers.layout(s, font):
            ps_name = (item.ft_object.postscript_name
                       .encode("ascii", "replace").decode("ascii"))
            glyph_name = item.ft_object.get_glyph_name(item.glyph_idx)
            stream.append((ps_name, item.x, glyph_name))
    self.set_color(*gc.get_rgb())

    for ps_name, group in itertools. \
            groupby(stream, lambda entry: entry[0]):
        self.set_font(ps_name, prop.get_size_in_points(), False)
        thetext = "\n".join(f"{x:g} 0 m /{name:s} glyphshow"
                            for _, x, name in group)
        self._pswriter.write(f"""\

# ==================================================
# Line: 821

def draw_mathtext(self, gc, x, y, s, prop, angle):
    """Draw the math text using matplotlib.mathtext."""
    width, height, descent, glyphs, rects = \
        self._text2path.mathtext_parser.parse(s, 72, prop)
    self.set_color(*gc.get_rgb())
    self._pswriter.write(
        f"gsave\n"
        f"{x:g} {y:g} translate\n"
        f"{angle:g} rotate\n")
    lastfont = None
    for font, fontsize, num, ox, oy in glyphs:
        self._character_tracker.track_glyph(font, num)
        if (font.postscript_name, fontsize) != lastfont:
            lastfont = font.postscript_name, fontsize
            self._pswriter.write(
                f"/{font.postscript_name} {fontsize} selectfont\n")
        glyph_name = font.get_glyph_name(font.get_char_index(num))
        self._pswriter.write(
            f"{ox:g} {oy:g} moveto\n"
            f"/{glyph_name} glyphshow\n")
    for ox, oy, w, h in rects:
        self._pswriter.write(f"{ox} {oy} {w} {h} rectfill\n")
    self._pswriter.write("grestore\n")


# ==================================================
# Line: 960

def _print_ps(
        self, fmt, outfile, *,
        metadata=None, papertype=None, orientation='portrait',
        bbox_inches_restore=None, **kwargs):

    dpi = self.figure.dpi
    self.figure.dpi = 72  # Override the dpi kwarg

    dsc_comments = {}
    if isinstance(outfile, (str, os.PathLike)):
        filename = pathlib.Path(outfile).name
        dsc_comments["Title"] = \
            filename.encode("ascii", "replace").decode("ascii")
    dsc_comments["Creator"] = (metadata or {}).get(
        "Creator",
        f"Matplotlib v{mpl.__version__}, https://matplotlib.org/")
    # See https://reproducible-builds.org/specs/source-date-epoch/
    source_date_epoch = os.getenv("SOURCE_DATE_EPOCH")
    dsc_comments["CreationDate"] = (
        datetime.datetime.fromtimestamp(
            int(source_date_epoch),
            datetime.timezone.utc).strftime("%a %b %d %H:%M:%S %Y")
        if source_date_epoch
        else time.ctime())
    dsc_comments = "\n".join(
        f"%%{k}: {v}" for k, v in dsc_comments.items())

    if papertype is None:
        papertype = mpl.rcParams['ps.papersize']
    papertype = papertype.lower()
    _api.check_in_list(['figure', *papersize], papertype=papertype)

    orientation = _api.check_getitem(
        _Orientation, orientation=orientation.lower())

    printer = (self._print_figure_tex
               if mpl.rcParams['text.usetex'] else
               self._print_figure)
    printer(fmt, outfile, dpi=dpi, dsc_comments=dsc_comments,
            orientation=orientation, papertype=papertype,
            bbox_inches_restore=bbox_inches_restore, **kwargs)


# ==================================================
# Line: 1002

def _print_figure(
        self, fmt, outfile, *,
        dpi, dsc_comments, orientation, papertype,
        bbox_inches_restore=None):
    """
    Render the figure to a filesystem path or a file-like object.

    Parameters are as for `.print_figure`, except that *dsc_comments* is a
    string containing Document Structuring Convention comments,
    generated from the *metadata* parameter to `.print_figure`.
    """
    is_eps = fmt == 'eps'
    if not (isinstance(outfile, (str, os.PathLike))
            or is_writable_file_like(outfile)):
        raise ValueError("outfile must be a path or a file-like object")

    # find the appropriate papertype
    width, height = self.figure.get_size_inches()
    if is_eps or papertype == 'figure':
        paper_width, paper_height = width, height
    else:
        paper_width, paper_height = orientation.swap_if_landscape(
            papersize[papertype])

    # center the figure on the paper
    xo = 72 * 0.5 * (paper_width - width)
    yo = 72 * 0.5 * (paper_height - height)

    llx = xo
    lly = yo
    urx = llx + self.figure.bbox.width
    ury = lly + self.figure.bbox.height
    rotation = 0
    if orientation is _Orientation.landscape:
        llx, lly, urx, ury = lly, llx, ury, urx
        xo, yo = 72 * paper_height - yo, xo
        rotation = 90
    bbox = (llx, lly, urx, ury)

    self._pswriter = StringIO()

    # mixed mode rendering
    ps_renderer = RendererPS(width, height, self._pswriter, imagedpi=dpi)
    renderer = MixedModeRenderer(
        self.figure, width, height, dpi, ps_renderer,
        bbox_inches_restore=bbox_inches_restore)

    self.figure.draw(renderer)

    def print_figure_impl(fh):
        # write the PostScript headers
        if is_eps:
            print("%!PS-Adobe-3.0 EPSF-3.0", file=fh)
        else:
            print("%!PS-Adobe-3.0", file=fh)
            if papertype != 'figure':
                print(f"%%DocumentPaperSizes: {papertype}", file=fh)
            print("%%Pages: 1", file=fh)
        print(f"%%LanguageLevel: 3\n"
              f"{dsc_comments}\n"
              f"%%Orientation: {orientation.name}\n"
              f"{_get_bbox_header(bbox)}\n"
              f"%%EndComments\n",
              end="", file=fh)

        Ndict = len(_psDefs)
        print("%%BeginProlog", file=fh)
        if not mpl.rcParams['ps.useafm']:
            Ndict += len(ps_renderer._character_tracker.used)
        print("/mpldict %d dict def" % Ndict, file=fh)
        print("mpldict begin", file=fh)
        print("\n".join(_psDefs), file=fh)
        if not mpl.rcParams['ps.useafm']:
            for font_path, chars \
                    in ps_renderer._character_tracker.used.items():
                if not chars:
                    continue
                fonttype = mpl.rcParams['ps.fonttype']
                # Can't use more than 255 chars from a single Type 3 font.
                if len(chars) > 255:
                    fonttype = 42
                fh.flush()
                if fonttype == 3:
                    fh.write(_font_to_ps_type3(font_path, chars))
                else:  # Type 42 only.
                    _font_to_ps_type42(font_path, chars, fh)
        print("end", file=fh)
        print("%%EndProlog", file=fh)

        if not is_eps:
            print("%%Page: 1 1", file=fh)
        print("mpldict begin", file=fh)

        print("%s translate" % _nums_to_str(xo, yo), file=fh)
        if rotation:
            print("%d rotate" % rotation, file=fh)
        print(f"0 0 {_nums_to_str(width*72, height*72)} rectclip", file=fh)

        # write the figure
        print(self._pswriter.getvalue(), file=fh)

        # write the trailer
        print("end", file=fh)
        print("showpage", file=fh)
        if not is_eps:
            print("%%EOF", file=fh)
        fh.flush()

    if mpl.rcParams['ps.usedistiller']:
        # We are going to use an external program to process the output.
        # Write to a temporary file.
        with TemporaryDirectory() as tmpdir:
            tmpfile = os.path.join(tmpdir, "tmp.ps")
            with open(tmpfile, 'w', encoding='latin-1') as fh:
                print_figure_impl(fh)
            if mpl.rcParams['ps.usedistiller'] == 'ghostscript':
                _try_distill(gs_distill,
                             tmpfile, is_eps, ptype=papertype, bbox=bbox)
            elif mpl.rcParams['ps.usedistiller'] == 'xpdf':
                _try_distill(xpdf_distill,
                             tmpfile, is_eps, ptype=papertype, bbox=bbox)
            _move_path_to_path_or_stream(tmpfile, outfile)

    else:  # Write directly to outfile.
        with cbook.open_file_cm(outfile, "w", encoding="latin-1") as file:
            if not file_requires_unicode(file):
                file = codecs.getwriter("latin-1")(file)
            print_figure_impl(file)


# ==================================================
# Line: 1131

def _print_figure_tex(
        self, fmt, outfile, *,
        dpi, dsc_comments, orientation, papertype,
        bbox_inches_restore=None):
    """
    If :rc:`text.usetex` is True, a temporary pair of tex/eps files
    are created to allow tex to manage the text layout via the PSFrags
    package. These files are processed to yield the final ps or eps file.

    The rest of the behavior is as for `._print_figure`.
    """
    is_eps = fmt == 'eps'

    width, height = self.figure.get_size_inches()
    xo = 0
    yo = 0

    llx = xo
    lly = yo
    urx = llx + self.figure.bbox.width
    ury = lly + self.figure.bbox.height
    bbox = (llx, lly, urx, ury)

    self._pswriter = StringIO()

    # mixed mode rendering
    ps_renderer = RendererPS(width, height, self._pswriter, imagedpi=dpi)
    renderer = MixedModeRenderer(self.figure,
                                 width, height, dpi, ps_renderer,
                                 bbox_inches_restore=bbox_inches_restore)

    self.figure.draw(renderer)

    # write to a temp file, we'll move it to outfile when done
    with TemporaryDirectory() as tmpdir:
        tmppath = pathlib.Path(tmpdir, "tmp.ps")
        tmppath.write_text(
            f"""\

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_pdf.py
# Line: 1821

def markerObject(self, path, trans, fill, stroke, lw, joinstyle,
                 capstyle):
    """Return name of a marker XObject representing the given path."""
    # self.markers used by markerObject, writeMarkers, close:
    # mapping from (path operations, fill?, stroke?) to
    #   [name, object reference, bounding box, linewidth]
    # This enables different draw_markers calls to share the XObject
    # if the gc is sufficiently similar: colors etc can vary, but
    # the choices of whether to fill and whether to stroke cannot.
    # We need a bounding box enclosing all of the XObject path,
    # but since line width may vary, we store the maximum of all
    # occurring line widths in self.markers.
    # close() is somewhat tightly coupled in that it expects the
    # first two components of each value in self.markers to be the
    # name and object reference.
    pathops = self.pathOperations(path, trans, simplify=False)
    key = (tuple(pathops), bool(fill), bool(stroke), joinstyle, capstyle)
    result = self.markers.get(key)
    if result is None:
        name = Name('M%d' % len(self.markers))
        ob = self.reserveObject('marker %d' % len(self.markers))
        bbox = path.get_extents(trans)
        self.markers[key] = [name, ob, bbox, lw]
    else:
        if result[-1] < lw:
            result[-1] = lw
        name = result[0]
    return name


# ==================================================
# Line: 1872

def pathCollectionObject(self, gc, path, trans, padding, filled, stroked):
    name = Name('P%d' % len(self.paths))
    ob = self.reserveObject('path %d' % len(self.paths))
    self.paths.append(
        (name, path, trans, ob, gc.get_joinstyle(), gc.get_capstyle(),
         padding, filled, stroked))
    return name


# ==================================================
# Line: 2053

def draw_path_collection(self, gc, master_transform, paths, all_transforms,
                         offsets, offset_trans, facecolors, edgecolors,
                         linewidths, linestyles, antialiaseds, urls,
                         offset_position, *, hatchcolors=None):
    # We can only reuse the objects if the presence of fill and
    # stroke (and the amount of alpha for each) is the same for
    # all of them
    can_do_optimization = True
    facecolors = np.asarray(facecolors)
    edgecolors = np.asarray(edgecolors)

    if hatchcolors is None:
        hatchcolors = []

    if not len(facecolors):
        filled = False
        can_do_optimization = not gc.get_hatch()
    else:
        if np.all(facecolors[:, 3] == facecolors[0, 3]):
            filled = facecolors[0, 3] != 0.0
        else:
            can_do_optimization = False

    if not len(edgecolors):
        stroked = False
    else:
        if np.all(np.asarray(linewidths) == 0.0):
            stroked = False
        elif np.all(edgecolors[:, 3] == edgecolors[0, 3]):
            stroked = edgecolors[0, 3] != 0.0
        else:
            can_do_optimization = False

    # Is the optimization worth it? Rough calculation:
    # cost of emitting a path in-line is len_path * uses_per_path
    # cost of XObject is len_path + 5 for the definition,
    #    uses_per_path for the uses
    len_path = len(paths[0].vertices) if len(paths) > 0 else 0
    uses_per_path = self._iter_collection_uses_per_path(
        paths, all_transforms, offsets, facecolors, edgecolors)
    should_do_optimization = \
        len_path + uses_per_path + 5 < len_path * uses_per_path

    if (not can_do_optimization) or (not should_do_optimization):
        return RendererBase.draw_path_collection(
            self, gc, master_transform, paths, all_transforms,
            offsets, offset_trans, facecolors, edgecolors,
            linewidths, linestyles, antialiaseds, urls,
            offset_position, hatchcolors=hatchcolors)

    padding = np.max(linewidths)
    path_codes = []
    for i, (path, transform) in enumerate(self._iter_collection_raw_paths(
            master_transform, paths, all_transforms)):
        name = self.file.pathCollectionObject(
            gc, path, transform, padding, filled, stroked)
        path_codes.append(name)

    output = self.file.output
    output(*self.gc.push())
    lastx, lasty = 0, 0
    for xo, yo, path_id, gc0, rgbFace in self._iter_collection(
            gc, path_codes, offsets, offset_trans,
            facecolors, edgecolors, linewidths, linestyles,
            antialiaseds, urls, offset_position, hatchcolors=hatchcolors):

        self.check_gc(gc0, rgbFace)
        dx, dy = xo - lastx, yo - lasty
        output(1, 0, 0, 1, dx, dy, Op.concat_matrix, path_id,
               Op.use_xobject)
        lastx, lasty = xo, yo
    output(*self.gc.pop())


# ==================================================
# Line: 2126

def draw_markers(self, gc, marker_path, marker_trans, path, trans,
                 rgbFace=None):
    # docstring inherited

    # Same logic as in draw_path_collection
    len_marker_path = len(marker_path)
    uses = len(path)
    if len_marker_path * uses < len_marker_path + uses + 5:
        RendererBase.draw_markers(self, gc, marker_path, marker_trans,
                                  path, trans, rgbFace)
        return

    self.check_gc(gc, rgbFace)
    fill = gc.fill(rgbFace)
    stroke = gc.stroke()

    output = self.file.output
    marker = self.file.markerObject(
        marker_path, marker_trans, fill, stroke, self.gc._linewidth,
        gc.get_joinstyle(), gc.get_capstyle())

    output(Op.gsave)
    lastx, lasty = 0, 0
    for vertices, code in path.iter_segments(
            trans,
            clip=(0, 0, self.file.width*72, self.file.height*72),
            simplify=False):
        if len(vertices):
            x, y = vertices[-2:]
            if not (0 <= x <= self.file.width * 72
                    and 0 <= y <= self.file.height * 72):
                continue
            dx, dy = x - lastx, y - lasty
            output(1, 0, 0, 1, dx, dy, Op.concat_matrix,
                   marker, Op.use_xobject)
            lastx, lasty = x, y
    output(Op.grestore)


# ==================================================
# Line: 2204

def _setup_textpos(self, x, y, angle, oldx=0, oldy=0, oldangle=0):
    if angle == oldangle == 0:
        self.file.output(x - oldx, y - oldy, Op.textpos)
    else:
        angle = math.radians(angle)
        self.file.output(math.cos(angle), math.sin(angle),
                         -math.sin(angle), math.cos(angle),
                         x, y, Op.textmatrix)
        self.file.output(0, 0, Op.textpos)


# ==================================================
# Line: 2214

def draw_mathtext(self, gc, x, y, s, prop, angle):
    # TODO: fix positioning and encoding
    width, height, descent, glyphs, rects = \
        self._text2path.mathtext_parser.parse(s, 72, prop)

    if gc.get_url() is not None:
        self.file._annotations[-1][1].append(_get_link_annotation(
            gc, x, y, width, height, angle))

    fonttype = mpl.rcParams['pdf.fonttype']

    # Set up a global transformation matrix for the whole math expression
    a = math.radians(angle)
    self.file.output(Op.gsave)
    self.file.output(math.cos(a), math.sin(a),
                     -math.sin(a), math.cos(a),
                     x, y, Op.concat_matrix)

    self.check_gc(gc, gc._rgb)
    prev_font = None, None
    oldx, oldy = 0, 0
    unsupported_chars = []

    self.file.output(Op.begin_text)
    for font, fontsize, num, ox, oy in glyphs:
        self.file._character_tracker.track_glyph(font, num)
        fontname = font.fname
        if not _font_supports_glyph(fonttype, num):
            # Unsupported chars (i.e. multibyte in Type 3 or beyond BMP in
            # Type 42) must be emitted separately (below).
            unsupported_chars.append((font, fontsize, ox, oy, num))
        else:
            self._setup_textpos(ox, oy, 0, oldx, oldy)
            oldx, oldy = ox, oy
            if (fontname, fontsize) != prev_font:
                self.file.output(self.file.fontName(fontname), fontsize,
                                 Op.selectfont)
                prev_font = fontname, fontsize
            self.file.output(self.encode_string(chr(num), fonttype),
                             Op.show)
    self.file.output(Op.end_text)

    for font, fontsize, ox, oy, num in unsupported_chars:
        self._draw_xobject_glyph(
            font, fontsize, font.get_char_index(num), ox, oy)

    # Draw any horizontal lines in the math layout
    for ox, oy, width, height in rects:
        self.file.output(Op.gsave, ox, oy, width, height,
                         Op.rectangle, Op.fill, Op.grestore)

    # Pop off the global transformation
    self.file.output(Op.grestore)


# ==================================================
# Line: 2268

def draw_tex(self, gc, x, y, s, prop, angle, *, mtext=None):
    # docstring inherited
    texmanager = self.get_texmanager()
    fontsize = prop.get_size_in_points()
    dvifile = texmanager.make_dvi(s, fontsize)
    with dviread.Dvi(dvifile, 72) as dvi:
        page, = dvi

    if gc.get_url() is not None:
        self.file._annotations[-1][1].append(_get_link_annotation(
            gc, x, y, page.width, page.height, angle))

    # Gather font information and do some setup for combining
    # characters into strings. The variable seq will contain a
    # sequence of font and text entries. A font entry is a list
    # ['font', name, size] where name is a Name object for the
    # font. A text entry is ['text', x, y, glyphs, x+w] where x
    # and y are the starting coordinates, w is the width, and
    # glyphs is a list; in this phase it will always contain just
    # one single-character string, but later it may have longer
    # strings interspersed with kern amounts.
    oldfont, seq = None, []
    for x1, y1, dvifont, glyph, width in page.text:
        if dvifont != oldfont:
            pdfname = self.file.dviFontName(dvifont)
            seq += [['font', pdfname, dvifont.size]]
            oldfont = dvifont
        seq += [['text', x1, y1, [bytes([glyph])], x1+width]]
        self.file._character_tracker.track(dvifont, chr(glyph))

    # Find consecutive text strings with constant y coordinate and
    # combine into a sequence of strings and kerns, or just one
    # string (if any kerns would be less than 0.1 points).
    i, curx, fontsize = 0, 0, None
    while i < len(seq)-1:
        elt, nxt = seq[i:i+2]
        if elt[0] == 'font':
            fontsize = elt[2]
        elif elt[0] == nxt[0] == 'text' and elt[2] == nxt[2]:
            offset = elt[4] - nxt[1]
            if abs(offset) < 0.1:
                elt[3][-1] += nxt[3][0]
                elt[4] += nxt[4]-nxt[1]
            else:
                elt[3] += [offset*1000.0/fontsize, nxt[3][0]]
                elt[4] = nxt[4]
            del seq[i+1]
            continue
        i += 1

    # Create a transform to map the dvi contents to the canvas.
    mytrans = Affine2D().rotate_deg(angle).translate(x, y)

    # Output the text.
    self.check_gc(gc, gc._rgb)
    self.file.output(Op.begin_text)
    curx, cury, oldx, oldy = 0, 0, 0, 0
    for elt in seq:
        if elt[0] == 'font':
            self.file.output(elt[1], elt[2], Op.selectfont)
        elif elt[0] == 'text':
            curx, cury = mytrans.transform((elt[1], elt[2]))
            self._setup_textpos(curx, cury, angle, oldx, oldy)
            oldx, oldy = curx, cury
            if len(elt[3]) == 1:
                self.file.output(elt[3][0], Op.show)
            else:
                self.file.output(elt[3], Op.showkern)
        else:
            assert False
    self.file.output(Op.end_text)

    # Then output the boxes (e.g., variable-length lines of square
    # roots).
    boxgc = self.new_gc()
    boxgc.copy_properties(gc)
    boxgc.set_linewidth(0)
    pathops = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO,
               Path.CLOSEPOLY]
    for x1, y1, h, w in page.boxes:
        path = Path([[x1, y1], [x1+w, y1], [x1+w, y1+h], [x1, y1+h],
                     [0, 0]], pathops)
        self.draw_path(boxgc, path, mytrans, gc._rgb)


# ==================================================
# Line: 2357

def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):
    # docstring inherited

    # TODO: combine consecutive texts into one BT/ET delimited section

    self.check_gc(gc, gc._rgb)
    if ismath:
        return self.draw_mathtext(gc, x, y, s, prop, angle)

    fontsize = prop.get_size_in_points()

    if mpl.rcParams['pdf.use14corefonts']:
        font = self._get_font_afm(prop)
        fonttype = 1
    else:
        font = self._get_font_ttf(prop)
        self.file._character_tracker.track(font, s)
        fonttype = mpl.rcParams['pdf.fonttype']

    if gc.get_url() is not None:
        font.set_text(s)
        width, height = font.get_width_height()
        self.file._annotations[-1][1].append(_get_link_annotation(
            gc, x, y, width / 64, height / 64, angle))

    # If fonttype is neither 3 nor 42, emit the whole string at once
    # without manual kerning.
    if fonttype not in [3, 42]:
        self.file.output(Op.begin_text,
                         self.file.fontName(prop), fontsize, Op.selectfont)
        self._setup_textpos(x, y, angle)
        self.file.output(self.encode_string(s, fonttype),
                         Op.show, Op.end_text)

    # A sequence of characters is broken into multiple chunks. The chunking
    # serves two purposes:
    #   - For Type 3 fonts, there is no way to access multibyte characters,
    #     as they cannot have a CIDMap.  Therefore, in this case we break
    #     the string into chunks, where each chunk contains either a string
    #     of consecutive 1-byte characters or a single multibyte character.
    #   - A sequence of 1-byte characters is split into chunks to allow for
    #     kerning adjustments between consecutive chunks.
    #
    # Each chunk is emitted with a separate command: 1-byte characters use
    # the regular text show command (TJ) with appropriate kerning between
    # chunks, whereas multibyte characters use the XObject command (Do).
    else:
        # List of (ft_object, start_x, [prev_kern, char, char, ...]),
        # w/o zero kerns.
        singlebyte_chunks = []
        # List of (ft_object, start_x, glyph_index).
        multibyte_glyphs = []
        prev_was_multibyte = True
        prev_font = font
        for item in _text_helpers.layout(s, font, kern_mode=Kerning.UNFITTED):
            if _font_supports_glyph(fonttype, ord(item.char)):
                if prev_was_multibyte or item.ft_object != prev_font:
                    singlebyte_chunks.append((item.ft_object, item.x, []))
                    prev_font = item.ft_object
                if item.prev_kern:
                    singlebyte_chunks[-1][2].append(item.prev_kern)
                singlebyte_chunks[-1][2].append(item.char)
                prev_was_multibyte = False
            else:
                multibyte_glyphs.append((item.ft_object, item.x, item.glyph_idx))
                prev_was_multibyte = True
        # Do the rotation and global translation as a single matrix
        # concatenation up front
        self.file.output(Op.gsave)
        a = math.radians(angle)
        self.file.output(math.cos(a), math.sin(a),
                         -math.sin(a), math.cos(a),
                         x, y, Op.concat_matrix)
        # Emit all the 1-byte characters in a BT/ET group.

        self.file.output(Op.begin_text)
        prev_start_x = 0
        for ft_object, start_x, kerns_or_chars in singlebyte_chunks:
            ft_name = self.file.fontName(ft_object.fname)
            self.file.output(ft_name, fontsize, Op.selectfont)
            self._setup_textpos(start_x, 0, 0, prev_start_x, 0, 0)
            self.file.output(
                # See pdf spec "Text space details" for the 1000/fontsize
                # (aka. 1000/T_fs) factor.
                [-1000 * next(group) / fontsize if tp == float  # a kern
                 else self.encode_string("".join(group), fonttype)
                 for tp, group in itertools.groupby(kerns_or_chars, type)],
                Op.showkern)
            prev_start_x = start_x
        self.file.output(Op.end_text)
        # Then emit all the multibyte characters, one at a time.
        for ft_object, start_x, glyph_idx in multibyte_glyphs:
            self._draw_xobject_glyph(
                ft_object, fontsize, glyph_idx, start_x, 0
            )
        self.file.output(Op.grestore)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_gtk3.py
# Line: 416

def add_toolitem(self, name, group, position, image_file, description,
                 toggle):
    if toggle:
        button = Gtk.ToggleToolButton()
    else:
        button = Gtk.ToolButton()
    button.set_label(name)

    if image_file is not None:
        image = Gtk.Image.new_from_gicon(
            Gio.Icon.new_for_string(image_file),
            Gtk.IconSize.LARGE_TOOLBAR)
        button.set_icon_widget(image)

    if position is None:
        position = -1

    self._add_button(button, group, position)
    signal = button.connect('clicked', self._call_tool, name)
    button.set_tooltip_text(description)
    button.show_all()
    self._toolitems.setdefault(name, [])
    self._toolitems[name].append((button, signal))


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_pgf.py
# Line: 387

def draw_markers(self, gc, marker_path, marker_trans, path, trans,
                 rgbFace=None):
    # docstring inherited

    _writeln(self.fh, r"\begin{pgfscope}")

    # convert from display units to in
    f = 1. / self.dpi

    # set style and clip
    self._print_pgf_clip(gc)
    self._print_pgf_path_styles(gc, rgbFace)

    # build marker definition
    bl, tr = marker_path.get_extents(marker_trans).get_points()
    coords = bl[0] * f, bl[1] * f, tr[0] * f, tr[1] * f
    _writeln(self.fh,
             r"\pgfsys@defobject{currentmarker}"
             r"{\pgfqpoint{%fin}{%fin}}{\pgfqpoint{%fin}{%fin}}{" % coords)
    self._print_pgf_path(None, marker_path, marker_trans)
    self._pgf_path_draw(stroke=gc.get_linewidth() != 0.0,
                        fill=rgbFace is not None)
    _writeln(self.fh, r"}")

    maxcoord = 16383 / 72.27 * self.dpi  # Max dimensions in LaTeX.
    clip = (-maxcoord, -maxcoord, maxcoord, maxcoord)

    # draw marker for each vertex
    for point, code in path.iter_segments(trans, simplify=False,
                                          clip=clip):
        x, y = point[0] * f, point[1] * f
        _writeln(self.fh, r"\begin{pgfscope}")
        _writeln(self.fh, r"\pgfsys@transformshift{%fin}{%fin}" % (x, y))
        _writeln(self.fh, r"\pgfsys@useobject{currentmarker}{}")
        _writeln(self.fh, r"\end{pgfscope}")

    _writeln(self.fh, r"\end{pgfscope}")


# ==================================================
# Occurrences: Lines 672-676 (2 instances)

def draw_tex(self, gc, x, y, s, prop, angle, *, mtext=None):
    # docstring inherited
    self.draw_text(gc, x, y, s, prop, angle, ismath="TeX", mtext=mtext)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_qt.py
# Line: 976

def add_toolitem(
        self, name, group, position, image_file, description, toggle):

    button = QtWidgets.QToolButton(self)
    if image_file:
        button.setIcon(NavigationToolbar2QT._icon(self, image_file))
    button.setText(name)
    if description:
        button.setToolTip(description)

    def handler():
        self.trigger_tool(name)
    if toggle:
        button.setCheckable(True)
        button.toggled.connect(handler)
    else:
        button.clicked.connect(handler)

    self._toolitems.setdefault(name, [])
    self._add_to_group(group, name, button, position)
    self._toolitems[name].append((button, handler))


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_svg.py
# Line: 290

def __init__(self, width, height, svgwriter, basename=None, image_dpi=72,
             *, metadata=None):
    self.width = width
    self.height = height
    self.writer = XMLWriter(svgwriter)
    self.image_dpi = image_dpi  # actual dpi at which we rasterize stuff

    if basename is None:
        basename = getattr(svgwriter, "name", "")
        if not isinstance(basename, str):
            basename = ""
    self.basename = basename

    self._groupd = {}
    self._image_counter = itertools.count()
    self._clip_path_ids = {}
    self._clipd = {}
    self._markers = {}
    self._path_collection_id = 0
    self._hatchd = {}
    self._has_gouraud = False
    self._n_gradients = 0

    super().__init__()
    self._glyph_map = dict()
    str_height = _short_float_fmt(height)
    str_width = _short_float_fmt(width)
    svgwriter.write(svgProlog)
    self._start_id = self.writer.start(
        'svg',
        width=f'{str_width}pt',
        height=f'{str_height}pt',
        viewBox=f'0 0 {str_width} {str_height}',
        xmlns="http://www.w3.org/2000/svg",
        version="1.1",
        id=mpl.rcParams['svg.id'],
        attrib={'xmlns:xlink': "http://www.w3.org/1999/xlink"})
    self._write_metadata(metadata)
    self._write_default_style()


# ==================================================
# Line: 693

def draw_markers(
        self, gc, marker_path, marker_trans, path, trans, rgbFace=None):
    # docstring inherited

    if not len(path.vertices):
        return

    writer = self.writer
    path_data = self._convert_path(
        marker_path,
        marker_trans + Affine2D().scale(1.0, -1.0),
        simplify=False)
    style = self._get_style_dict(gc, rgbFace)
    dictkey = (path_data, _generate_css(style))
    oid = self._markers.get(dictkey)
    style = _generate_css({k: v for k, v in style.items()
                          if k.startswith('stroke')})

    if oid is None:
        oid = self._make_id('m', dictkey)
        writer.start('defs')
        writer.element('path', id=oid, d=path_data, style=style)
        writer.end('defs')
        self._markers[dictkey] = oid

    writer.start('g', **self._get_clip_attrs(gc))
    if gc.get_url() is not None:
        self.writer.start('a', {'xlink:href': gc.get_url()})
    trans_and_flip = self._make_flip_transform(trans)
    attrib = {'xlink:href': f'#{oid}'}
    clip = (0, 0, self.width*72, self.height*72)
    for vertices, code in path.iter_segments(
            trans_and_flip, clip=clip, simplify=False):
        if len(vertices):
            x, y = vertices[-2:]
            attrib['x'] = _short_float_fmt(x)
            attrib['y'] = _short_float_fmt(y)
            attrib['style'] = self._get_style(gc, rgbFace)
            writer.element('use', attrib=attrib)
    if gc.get_url() is not None:
        self.writer.end('a')
    writer.end('g')


# ==================================================
# Line: 736

def draw_path_collection(self, gc, master_transform, paths, all_transforms,
                         offsets, offset_trans, facecolors, edgecolors,
                         linewidths, linestyles, antialiaseds, urls,
                         offset_position, *, hatchcolors=None):
    if hatchcolors is None:
        hatchcolors = []
    # Is the optimization worth it? Rough calculation:
    # cost of emitting a path in-line is
    #    (len_path + 5) * uses_per_path
    # cost of definition+use is
    #    (len_path + 3) + 9 * uses_per_path
    len_path = len(paths[0].vertices) if len(paths) > 0 else 0
    uses_per_path = self._iter_collection_uses_per_path(
        paths, all_transforms, offsets, facecolors, edgecolors)
    should_do_optimization = \
        len_path + 9 * uses_per_path + 3 < (len_path + 5) * uses_per_path
    if not should_do_optimization:
        return super().draw_path_collection(
            gc, master_transform, paths, all_transforms,
            offsets, offset_trans, facecolors, edgecolors,
            linewidths, linestyles, antialiaseds, urls,
            offset_position, hatchcolors=hatchcolors)

    writer = self.writer
    path_codes = []
    writer.start('defs')
    for i, (path, transform) in enumerate(self._iter_collection_raw_paths(
            master_transform, paths, all_transforms)):
        transform = Affine2D(transform.get_matrix()).scale(1.0, -1.0)
        d = self._convert_path(path, transform, simplify=False)
        oid = 'C{:x}_{:x}_{}'.format(
            self._path_collection_id, i, self._make_id('', d))
        writer.element('path', id=oid, d=d)
        path_codes.append(oid)
    writer.end('defs')

    for xo, yo, path_id, gc0, rgbFace in self._iter_collection(
            gc, path_codes, offsets, offset_trans,
            facecolors, edgecolors, linewidths, linestyles,
            antialiaseds, urls, offset_position, hatchcolors=hatchcolors):
        url = gc0.get_url()
        if url is not None:
            writer.start('a', attrib={'xlink:href': url})
        clip_attrs = self._get_clip_attrs(gc0)
        if clip_attrs:
            writer.start('g', **clip_attrs)
        attrib = {
            'xlink:href': f'#{path_id}',
            'x': _short_float_fmt(xo),
            'y': _short_float_fmt(self.height - yo),
            'style': self._get_style(gc0, rgbFace)
            }
        writer.element('use', attrib=attrib)
        if clip_attrs:
            writer.end('g')
        if url is not None:
            writer.end('a')

    self._path_collection_id += 1


# ==================================================
# Line: 1040

def _draw_text_as_path(self, gc, x, y, s, prop, angle, ismath, mtext=None):
    # docstring inherited
    writer = self.writer

    writer.comment(s)

    glyph_map = self._glyph_map

    text2path = self._text2path
    color = rgb2hex(gc.get_rgb())
    fontsize = prop.get_size_in_points()

    style = {}
    if color != '#000000':
        style['fill'] = color
    alpha = gc.get_alpha() if gc.get_forced_alpha() else gc.get_rgb()[3]
    if alpha != 1:
        style['opacity'] = _short_float_fmt(alpha)
    font_scale = fontsize / text2path.FONT_SCALE
    attrib = {
        'style': _generate_css(style),
        'transform': _generate_transform([
            ('translate', (x, y)),
            ('rotate', (-angle,)),
            ('scale', (font_scale, -font_scale))]),
    }
    writer.start('g', attrib=attrib)

    if not ismath:
        font = text2path._get_font(prop)
        _glyphs = text2path.get_glyphs_with_font(
            font, s, glyph_map=glyph_map, return_new_glyphs_only=True)
        glyph_info, glyph_map_new, rects = _glyphs
        self._update_glyph_map_defs(glyph_map_new)

        for glyph_id, xposition, yposition, scale in glyph_info:
            writer.element(
                'use',
                transform=_generate_transform([
                    ('translate', (xposition, yposition)),
                    ('scale', (scale,)),
                    ]),
                attrib={'xlink:href': f'#{glyph_id}'})

    else:
        if ismath == "TeX":
            _glyphs = text2path.get_glyphs_tex(
                prop, s, glyph_map=glyph_map, return_new_glyphs_only=True)
        else:
            _glyphs = text2path.get_glyphs_mathtext(
                prop, s, glyph_map=glyph_map, return_new_glyphs_only=True)
        glyph_info, glyph_map_new, rects = _glyphs
        self._update_glyph_map_defs(glyph_map_new)

        for char_id, xposition, yposition, scale in glyph_info:
            char_id = self._adjust_char_id(char_id)
            writer.element(
                'use',
                transform=_generate_transform([
                    ('translate', (xposition, yposition)),
                    ('scale', (scale,)),
                    ]),
                attrib={'xlink:href': f'#{char_id}'})

        for verts, codes in rects:
            path = Path(verts, codes)
            path_data = self._convert_path(path, simplify=False)
            writer.element('path', d=path_data)

    writer.end('g')


# ==================================================
# Line: 1111

def _draw_text_as_text(self, gc, x, y, s, prop, angle, ismath, mtext=None):
    # NOTE: If you change the font styling CSS, then be sure the check for
    # svg.fonttype = none in `lib/matplotlib/testing/compare.py::convert` remains in
    # sync. Also be sure to re-generate any SVG using this mode, or else such tests
    # will fail to use the right converter for the expected images, and they will
    # fail strangely.
    writer = self.writer

    color = rgb2hex(gc.get_rgb())
    font_style = {}
    color_style = {}
    if color != '#000000':
        color_style['fill'] = color

    alpha = gc.get_alpha() if gc.get_forced_alpha() else gc.get_rgb()[3]
    if alpha != 1:
        color_style['opacity'] = _short_float_fmt(alpha)

    if not ismath:
        attrib = {}

        # Separate font style in their separate attributes
        if prop.get_style() != 'normal':
            font_style['font-style'] = prop.get_style()
        if prop.get_variant() != 'normal':
            font_style['font-variant'] = prop.get_variant()
        weight = fm.weight_dict[prop.get_weight()]
        if weight != 400:
            font_style['font-weight'] = f'{weight}'

        def _normalize_sans(name):
            return 'sans-serif' if name in ['sans', 'sans serif'] else name

        def _expand_family_entry(fn):
            fn = _normalize_sans(fn)
            # prepend generic font families with all configured font names
            if fn in fm.font_family_aliases:
                # get all of the font names and fix spelling of sans-serif
                # (we accept 3 ways CSS only supports 1)
                for name in fm.FontManager._expand_aliases(fn):
                    yield _normalize_sans(name)
            # whether a generic name or a family name, it must appear at
            # least once
            yield fn

        def _get_all_quoted_names(prop):
            # only quote specific names, not generic names
            return [name if name in fm.font_family_aliases else repr(name)
                    for entry in prop.get_family()
                    for name in _expand_family_entry(entry)]

        font_style['font-size'] = f'{_short_float_fmt(prop.get_size())}px'
        # ensure expansion, quoting, and dedupe of font names
        font_style['font-family'] = ", ".join(
            dict.fromkeys(_get_all_quoted_names(prop))
            )

        if prop.get_stretch() != 'normal':
            font_style['font-stretch'] = prop.get_stretch()
        attrib['style'] = _generate_css({**font_style, **color_style})

        if mtext and (angle == 0 or mtext.get_rotation_mode() == "anchor"):
            # If text anchoring can be supported, get the original
            # coordinates and add alignment information.

            # Get anchor coordinates.
            transform = mtext.get_transform()
            ax, ay = transform.transform(mtext.get_unitless_position())
            ay = self.height - ay

            # Don't do vertical anchor alignment. Most applications do not
            # support 'alignment-baseline' yet. Apply the vertical layout
            # to the anchor point manually for now.
            angle_rad = np.deg2rad(angle)
            dir_vert = np.array([np.sin(angle_rad), np.cos(angle_rad)])
            v_offset = np.dot(dir_vert, [(x - ax), (y - ay)])
            ax = ax + v_offset * dir_vert[0]
            ay = ay + v_offset * dir_vert[1]

            ha_mpl_to_svg = {'left': 'start', 'right': 'end',
                             'center': 'middle'}
            font_style['text-anchor'] = ha_mpl_to_svg[mtext.get_ha()]

            attrib['x'] = _short_float_fmt(ax)
            attrib['y'] = _short_float_fmt(ay)
            attrib['style'] = _generate_css({**font_style, **color_style})
            attrib['transform'] = _generate_transform([
                ("rotate", (-angle, ax, ay))])

        else:
            attrib['transform'] = _generate_transform([
                ('translate', (x, y)),
                ('rotate', (-angle,))])

        writer.element('text', s, attrib=attrib)

    else:
        writer.comment(s)

        width, height, descent, glyphs, rects = \
            self._text2path.mathtext_parser.parse(s, 72, prop)

        # Apply attributes to 'g', not 'text', because we likely have some
        # rectangles as well with the same style and transformation.
        writer.start('g',
                     style=_generate_css({**font_style, **color_style}),
                     transform=_generate_transform([
                         ('translate', (x, y)),
                         ('rotate', (-angle,))]),
                     )

        writer.start('text')

        # Sort the characters by font, and output one tspan for each.
        spans = {}
        for font, fontsize, thetext, new_x, new_y in glyphs:
            entry = fm.ttfFontProperty(font)
            font_style = {}
            # Separate font style in its separate attributes
            if entry.style != 'normal':
                font_style['font-style'] = entry.style
            if entry.variant != 'normal':
                font_style['font-variant'] = entry.variant
            if entry.weight != 400:
                font_style['font-weight'] = f'{entry.weight}'
            font_style['font-size'] = f'{_short_float_fmt(fontsize)}px'
            font_style['font-family'] = f'{entry.name!r}'  # ensure quoting
            if entry.stretch != 'normal':
                font_style['font-stretch'] = entry.stretch
            style = _generate_css({**font_style, **color_style})
            if thetext == 32:
                thetext = 0xa0  # non-breaking space
            spans.setdefault(style, []).append((new_x, -new_y, thetext))

        for style, chars in spans.items():
            chars.sort()  # Sort by increasing x position
            for x, y, t in chars:  # Output one tspan for each character
                writer.element(
                    'tspan',
                    chr(t),
                    x=_short_float_fmt(x),
                    y=_short_float_fmt(y),
                    style=style)

        writer.end('text')

        for x, y, width, height in rects:
            writer.element(
                'rect',
                x=_short_float_fmt(x),
                y=_short_float_fmt(-y-1),
                width=_short_float_fmt(width),
                height=_short_float_fmt(height)
                )

        writer.end('g')


# ==================================================
# Line: 1268

def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):
    # docstring inherited

    clip_attrs = self._get_clip_attrs(gc)
    if clip_attrs:
        # Cannot apply clip-path directly to the text, because
        # it has a transformation
        self.writer.start('g', **clip_attrs)

    if gc.get_url() is not None:
        self.writer.start('a', {'xlink:href': gc.get_url()})

    if mpl.rcParams['svg.fonttype'] == 'path':
        self._draw_text_as_path(gc, x, y, s, prop, angle, ismath, mtext)
    else:
        self._draw_text_as_text(gc, x, y, s, prop, angle, ismath, mtext)

    if gc.get_url() is not None:
        self.writer.end('a')

    if clip_attrs:
        self.writer.end('g')


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/ticker.py
# Line: 1372

def __init__(self, unit="", places=None, sep=" ", *, usetex=None,
             useMathText=None, useOffset=False):
    r"""
    Parameters
    ----------
    unit : str, default: ""
        Unit symbol to use, suitable for use with single-letter
        representations of powers of 1000. For example, 'Hz' or 'm'.

    places : int, default: None
        Precision with which to display the number, specified in
        digits after the decimal point (there will be between one
        and three digits before the decimal point). If it is None,
        the formatting falls back to the floating point format '%g',
        which displays up to 6 *significant* digits, i.e. the equivalent
        value for *places* varies between 0 and 5 (inclusive).

    sep : str, default: " "
        Separator used between the value and the prefix/unit. For
        example, one get '3.14 mV' if ``sep`` is " " (default) and
        '3.14mV' if ``sep`` is "". Besides the default behavior, some
        other useful options may be:

        * ``sep=""`` to append directly the prefix/unit to the value;
        * ``sep="\N{THIN SPACE}"`` (``U+2009``);
        * ``sep="\N{NARROW NO-BREAK SPACE}"`` (``U+202F``);
        * ``sep="\N{NO-BREAK SPACE}"`` (``U+00A0``).

    usetex : bool, default: :rc:`text.usetex`
        To enable/disable the use of TeX's math mode for rendering the
        numbers in the formatter.

    useMathText : bool, default: :rc:`axes.formatter.use_mathtext`
        To enable/disable the use mathtext for rendering the numbers in
        the formatter.
    useOffset : bool or float, default: False
        Whether to use offset notation with :math:`10^{3*N}` based prefixes.
        This features allows showing an offset with standard SI order of
        magnitude prefix near the axis. Offset is computed similarly to
        how `ScalarFormatter` computes it internally, but here you are
        guaranteed to get an offset which will make the tick labels exceed
        3 digits. See also `.set_useOffset`.

        .. versionadded:: 3.10
    """
    self.unit = unit
    self.places = places
    self.sep = sep
    super().__init__(
        useOffset=useOffset,
        useMathText=useMathText,
        useLocale=False,
        usetex=usetex,
    )


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_constrained_layout.py
# Line: 63

def do_constrained_layout(fig, h_pad, w_pad,
                          hspace=None, wspace=None, rect=(0, 0, 1, 1),
                          compress=False):
    """
    Do the constrained_layout.  Called at draw time in
     ``figure.constrained_layout()``

    Parameters
    ----------
    fig : `~matplotlib.figure.Figure`
        `.Figure` instance to do the layout in.

    h_pad, w_pad : float
      Padding around the Axes elements in figure-normalized units.

    hspace, wspace : float
       Fraction of the figure to dedicate to space between the
       Axes.  These are evenly spread between the gaps between the Axes.
       A value of 0.2 for a three-column layout would have a space
       of 0.1 of the figure width between each column.
       If h/wspace < h/w_pad, then the pads are used instead.

    rect : tuple of 4 floats
        Rectangle in figure coordinates to perform constrained layout in
        [left, bottom, width, height], each from 0-1.

    compress : bool
        Whether to shift Axes so that white space in between them is
        removed. This is useful for simple grids of fixed-aspect Axes (e.g.
        a grid of images).

    Returns
    -------
    layoutgrid : private debugging structure
    """

    renderer = fig._get_renderer()
    # make layoutgrid tree...
    layoutgrids = make_layoutgrids(fig, None, rect=rect)
    if not layoutgrids['hasgrids']:
        _api.warn_external('There are no gridspecs with layoutgrids. '
                           'Possibly did not call parent GridSpec with the'
                           ' "figure" keyword')
        return

    for _ in range(2):
        # do the algorithm twice.  This has to be done because decorations
        # change size after the first re-position (i.e. x/yticklabels get
        # larger/smaller).  This second reposition tends to be much milder,
        # so doing twice makes things work OK.

        # make margins for all the Axes and subfigures in the
        # figure.  Add margins for colorbars...
        make_layout_margins(layoutgrids, fig, renderer, h_pad=h_pad,
                            w_pad=w_pad, hspace=hspace, wspace=wspace)
        make_margin_suptitles(layoutgrids, fig, renderer, h_pad=h_pad,
                              w_pad=w_pad)

        # if a layout is such that a columns (or rows) margin has no
        # constraints, we need to make all such instances in the grid
        # match in margin size.
        match_submerged_margins(layoutgrids, fig)

        # update all the variables in the layout.
        layoutgrids[fig].update_variables()

        warn_collapsed = ('constrained_layout not applied because '
                          'axes sizes collapsed to zero.  Try making '
                          'figure larger or Axes decorations smaller.')
        if check_no_collapsed_axes(layoutgrids, fig):
            reposition_axes(layoutgrids, fig, renderer, h_pad=h_pad,
                            w_pad=w_pad, hspace=hspace, wspace=wspace)
            if compress:
                layoutgrids = compress_fixed_aspect(layoutgrids, fig)
                layoutgrids[fig].update_variables()
                if check_no_collapsed_axes(layoutgrids, fig):
                    reposition_axes(layoutgrids, fig, renderer, h_pad=h_pad,
                                    w_pad=w_pad, hspace=hspace, wspace=wspace)
                else:
                    _api.warn_external(warn_collapsed)

                if ((suptitle := fig._suptitle) is not None and
                        suptitle.get_in_layout() and suptitle._autopos):
                    x, _ = suptitle.get_position()
                    suptitle.set_position(
                        (x, layoutgrids[fig].get_inner_bbox().y1 + h_pad))
                    suptitle.set_verticalalignment('bottom')
        else:
            _api.warn_external(warn_collapsed)
        reset_margins(layoutgrids, fig)
    return layoutgrids



# ==================================================
# Line: 342

def make_layout_margins(layoutgrids, fig, renderer, *, w_pad=0, h_pad=0,
                        hspace=0, wspace=0):
    """
    For each Axes, make a margin between the *pos* layoutbox and the
    *axes* layoutbox be a minimum size that can accommodate the
    decorations on the axis.

    Then make room for colorbars.

    Parameters
    ----------
    layoutgrids : dict
    fig : `~matplotlib.figure.Figure`
        `.Figure` instance to do the layout in.
    renderer : `~matplotlib.backend_bases.RendererBase` subclass.
        The renderer to use.
    w_pad, h_pad : float, default: 0
        Width and height padding (in fraction of figure).
    hspace, wspace : float, default: 0
        Width and height padding as fraction of figure size divided by
        number of columns or rows.
    """
    for sfig in fig.subfigs:  # recursively make child panel margins
        ss = sfig._subplotspec
        gs = ss.get_gridspec()

        make_layout_margins(layoutgrids, sfig, renderer,
                            w_pad=w_pad, h_pad=h_pad,
                            hspace=hspace, wspace=wspace)

        margins = get_margin_from_padding(sfig, w_pad=0, h_pad=0,
                                          hspace=hspace, wspace=wspace)
        layoutgrids[gs].edit_outer_margin_mins(margins, ss)

    for ax in fig._localaxes:
        if not ax.get_subplotspec() or not ax.get_in_layout():
            continue

        ss = ax.get_subplotspec()
        gs = ss.get_gridspec()

        if gs not in layoutgrids:
            return

        margin = get_margin_from_padding(ax, w_pad=w_pad, h_pad=h_pad,
                                         hspace=hspace, wspace=wspace)
        pos, bbox = get_pos_and_bbox(ax, renderer)
        # the margin is the distance between the bounding box of the Axes
        # and its position (plus the padding from above)
        margin['left'] += pos.x0 - bbox.x0
        margin['right'] += bbox.x1 - pos.x1
        # remember that rows are ordered from top:
        margin['bottom'] += pos.y0 - bbox.y0
        margin['top'] += bbox.y1 - pos.y1

        # make margin for colorbars.  These margins go in the
        # padding margin, versus the margin for Axes decorators.
        for cbax in ax._colorbars:
            # note pad is a fraction of the parent width...
            pad = colorbar_get_pad(layoutgrids, cbax)
            # colorbars can be child of more than one subplot spec:
            cbp_rspan, cbp_cspan = get_cb_parent_spans(cbax)
            loc = cbax._colorbar_info['location']
            cbpos, cbbbox = get_pos_and_bbox(cbax, renderer)
            if loc == 'right':
                if cbp_cspan.stop == ss.colspan.stop:
                    # only increase if the colorbar is on the right edge
                    margin['rightcb'] += cbbbox.width + pad
            elif loc == 'left':
                if cbp_cspan.start == ss.colspan.start:
                    # only increase if the colorbar is on the left edge
                    margin['leftcb'] += cbbbox.width + pad
            elif loc == 'top':
                if cbp_rspan.start == ss.rowspan.start:
                    margin['topcb'] += cbbbox.height + pad
            else:
                if cbp_rspan.stop == ss.rowspan.stop:
                    margin['bottomcb'] += cbbbox.height + pad
            # If the colorbars are wider than the parent box in the
            # cross direction
            if loc in ['top', 'bottom']:
                if (cbp_cspan.start == ss.colspan.start and
                        cbbbox.x0 < bbox.x0):
                    margin['left'] += bbox.x0 - cbbbox.x0
                if (cbp_cspan.stop == ss.colspan.stop and
                        cbbbox.x1 > bbox.x1):
                    margin['right'] += cbbbox.x1 - bbox.x1
            # or taller:
            if loc in ['left', 'right']:
                if (cbp_rspan.stop == ss.rowspan.stop and
                        cbbbox.y0 < bbox.y0):
                    margin['bottom'] += bbox.y0 - cbbbox.y0
                if (cbp_rspan.start == ss.rowspan.start and
                        cbbbox.y1 > bbox.y1):
                    margin['top'] += cbbbox.y1 - bbox.y1
        # pass the new margins down to the layout grid for the solution...
        layoutgrids[gs].edit_outer_margin_mins(margin, ss)

    # make margins for figure-level legends:
    for leg in fig.legends:
        inv_trans_fig = None
        if leg._outside_loc and leg._bbox_to_anchor is None:
            if inv_trans_fig is None:
                inv_trans_fig = fig.transFigure.inverted().transform_bbox
            bbox = inv_trans_fig(leg.get_tightbbox(renderer))
            w = bbox.width + 2 * w_pad
            h = bbox.height + 2 * h_pad
            legendloc = leg._outside_loc
            if legendloc == 'lower':
                layoutgrids[fig].edit_margin_min('bottom', h)
            elif legendloc == 'upper':
                layoutgrids[fig].edit_margin_min('top', h)
            if legendloc == 'right':
                layoutgrids[fig].edit_margin_min('right', w)
            elif legendloc == 'left':
                layoutgrids[fig].edit_margin_min('left', w)



# ==================================================
# Line: 653

def reposition_axes(layoutgrids, fig, renderer, *,
                    w_pad=0, h_pad=0, hspace=0, wspace=0):
    """
    Reposition all the Axes based on the new inner bounding box.
    """
    trans_fig_to_subfig = fig.transFigure - fig.transSubfigure
    for sfig in fig.subfigs:
        bbox = layoutgrids[sfig].get_outer_bbox()
        sfig._redo_transform_rel_fig(
            bbox=bbox.transformed(trans_fig_to_subfig))
        reposition_axes(layoutgrids, sfig, renderer,
                        w_pad=w_pad, h_pad=h_pad,
                        wspace=wspace, hspace=hspace)

    for ax in fig._localaxes:
        if ax.get_subplotspec() is None or not ax.get_in_layout():
            continue

        # grid bbox is in Figure coordinates, but we specify in panel
        # coordinates...
        ss = ax.get_subplotspec()
        gs = ss.get_gridspec()
        if gs not in layoutgrids:
            return

        bbox = layoutgrids[gs].get_inner_bbox(rows=ss.rowspan,
                                              cols=ss.colspan)

        # transform from figure to panel for set_position:
        newbbox = trans_fig_to_subfig.transform_bbox(bbox)
        ax._set_position(newbbox)

        # move the colorbars:
        # we need to keep track of oldw and oldh if there is more than
        # one colorbar:
        offset = {'left': 0, 'right': 0, 'bottom': 0, 'top': 0}
        for nn, cbax in enumerate(ax._colorbars[::-1]):
            if ax == cbax._colorbar_info['parents'][0]:
                reposition_colorbar(layoutgrids, cbax, renderer,
                                    offset=offset)



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/units.py
# Line: 79

def __init__(self, majloc=None, minloc=None,
             majfmt=None, minfmt=None, label=None,
             default_limits=None):
    """
    Parameters
    ----------
    majloc, minloc : Locator, optional
        Tick locators for the major and minor ticks.
    majfmt, minfmt : Formatter, optional
        Tick formatters for the major and minor ticks.
    label : str, optional
        The default axis label.
    default_limits : optional
        The default min and max limits of the axis if no data has
        been plotted.

    Notes
    -----
    If any of the above are ``None``, the axis will simply use the
    default value.
    """
    self.majloc = majloc
    self.minloc = minloc
    self.majfmt = majfmt
    self.minfmt = minfmt
    self.label = label
    self.default_limits = default_limits



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/image.py
# Line: 251

def __init__(self, ax,
             cmap=None,
             norm=None,
             colorizer=None,
             interpolation=None,
             origin=None,
             filternorm=True,
             filterrad=4.0,
             resample=False,
             *,
             interpolation_stage=None,
             **kwargs
             ):
    super().__init__(self._get_colorizer(cmap, norm, colorizer))
    origin = mpl._val_or_rc(origin, 'image.origin')
    _api.check_in_list(["upper", "lower"], origin=origin)
    self.origin = origin
    self.set_filternorm(filternorm)
    self.set_filterrad(filterrad)
    self.set_interpolation(interpolation)
    self.set_interpolation_stage(interpolation_stage)
    self.set_resample(resample)
    self.axes = ax

    self._imcache = None

    self._internal_update(kwargs)


# ==================================================
# Line: 337

def _make_image(self, A, in_bbox, out_bbox, clip_bbox, magnification=1.0,
                unsampled=False, round_to_pixel_border=True):
    """
    Normalize, rescale, and colormap the image *A* from the given *in_bbox*
    (in data space), to the given *out_bbox* (in pixel space) clipped to
    the given *clip_bbox* (also in pixel space), and magnified by the
    *magnification* factor.

    Parameters
    ----------
    A : ndarray

        - a (M, N) array interpreted as scalar (greyscale) image,
          with one of the dtypes `~numpy.float32`, `~numpy.float64`,
          `~numpy.float128`, `~numpy.uint16` or `~numpy.uint8`.
        - (M, N, 4) RGBA image with a dtype of `~numpy.float32`,
          `~numpy.float64`, `~numpy.float128`, or `~numpy.uint8`.

    in_bbox : `~matplotlib.transforms.Bbox`

    out_bbox : `~matplotlib.transforms.Bbox`

    clip_bbox : `~matplotlib.transforms.Bbox`

    magnification : float, default: 1

    unsampled : bool, default: False
        If True, the image will not be scaled, but an appropriate
        affine transformation will be returned instead.

    round_to_pixel_border : bool, default: True
        If True, the output image size will be rounded to the nearest pixel
        boundary.  This makes the images align correctly with the Axes.
        It should not be used if exact scaling is needed, such as for
        `.FigureImage`.

    Returns
    -------
    image : (M, N, 4) `numpy.uint8` array
        The RGBA image, resampled unless *unsampled* is True.
    x, y : float
        The upper left corner where the image should be drawn, in pixel
        space.
    trans : `~matplotlib.transforms.Affine2D`
        The affine transformation from image to pixel space.
    """
    if A is None:
        raise RuntimeError('You must first set the image '
                           'array or the image attribute')
    if A.size == 0:
        raise RuntimeError("_make_image must get a non-empty image. "
                           "Your Artist's draw method must filter before "
                           "this method is called.")

    clipped_bbox = Bbox.intersection(out_bbox, clip_bbox)

    if clipped_bbox is None:
        return None, 0, 0, None

    out_width_base = clipped_bbox.width * magnification
    out_height_base = clipped_bbox.height * magnification

    if out_width_base == 0 or out_height_base == 0:
        return None, 0, 0, None

    if self.origin == 'upper':
        # Flip the input image using a transform.  This avoids the
        # problem with flipping the array, which results in a copy
        # when it is converted to contiguous in the C wrapper
        t0 = Affine2D().translate(0, -A.shape[0]).scale(1, -1)
    else:
        t0 = IdentityTransform()

    t0 += (
        Affine2D()
        .scale(
            in_bbox.width / A.shape[1],
            in_bbox.height / A.shape[0])
        .translate(in_bbox.x0, in_bbox.y0)
        + self.get_transform())

    t = (t0
         + (Affine2D()
            .translate(-clipped_bbox.x0, -clipped_bbox.y0)
            .scale(magnification)))

    # So that the image is aligned with the edge of the Axes, we want to
    # round up the output width to the next integer.  This also means
    # scaling the transform slightly to account for the extra subpixel.
    if ((not unsampled) and t.is_affine and round_to_pixel_border and
            (out_width_base % 1.0 != 0.0 or out_height_base % 1.0 != 0.0)):
        out_width = math.ceil(out_width_base)
        out_height = math.ceil(out_height_base)
        extra_width = (out_width - out_width_base) / out_width_base
        extra_height = (out_height - out_height_base) / out_height_base
        t += Affine2D().scale(1.0 + extra_width, 1.0 + extra_height)
    else:
        out_width = int(out_width_base)
        out_height = int(out_height_base)
    out_shape = (out_height, out_width)

    if not unsampled:
        if not (A.ndim == 2 or A.ndim == 3 and A.shape[-1] in (3, 4)):
            raise ValueError(f"Invalid shape {A.shape} for image data")

        float_rgba_in = A.ndim == 3 and A.shape[-1] == 4 and A.dtype.kind == 'f'

        # if antialiased, this needs to change as window sizes
        # change:
        interpolation_stage = self._interpolation_stage
        if interpolation_stage in ['antialiased', 'auto']:
            pos = np.array([[0, 0], [A.shape[1], A.shape[0]]])
            disp = t.transform(pos)
            dispx = np.abs(np.diff(disp[:, 0])) / A.shape[1]
            dispy = np.abs(np.diff(disp[:, 1])) / A.shape[0]
            if (dispx < 3) or (dispy < 3):
                interpolation_stage = 'rgba'
            else:
                interpolation_stage = 'data'

        if A.ndim == 2 and interpolation_stage == 'data':
            # if we are a 2D array, then we are running through the
            # norm + colormap transformation.  However, in general the
            # input data is not going to match the size on the screen so we
            # have to resample to the correct number of pixels

            if A.dtype.kind == 'f':  # Float dtype: scale to same dtype.
                scaled_dtype = np.dtype("f8" if A.dtype.itemsize > 4 else "f4")
                if scaled_dtype.itemsize < A.dtype.itemsize:
                    _api.warn_external(f"Casting input data from {A.dtype}"
                                       f" to {scaled_dtype} for imshow.")
            else:  # Int dtype, likely.
                # TODO slice input array first
                # Scale to appropriately sized float: use float32 if the
                # dynamic range is small, to limit the memory footprint.
                da = A.max().astype("f8") - A.min().astype("f8")
                scaled_dtype = "f8" if da > 1e8 else "f4"

            # resample the input data to the correct resolution and shape
            A_resampled = _resample(self, A.astype(scaled_dtype), out_shape, t)

            # if using NoNorm, cast back to the original datatype
            if isinstance(self.norm, mcolors.NoNorm):
                A_resampled = A_resampled.astype(A.dtype)

            # Compute out_mask (what screen pixels include "bad" data
            # pixels) and out_alpha (to what extent screen pixels are
            # covered by data pixels: 0 outside the data extent, 1 inside
            # (even for bad data), and intermediate values at the edges).
            mask = (np.where(A.mask, np.float32(np.nan), np.float32(1))
                    if A.mask.shape == A.shape  # nontrivial mask
                    else np.ones_like(A, np.float32))
            # we always have to interpolate the mask to account for
            # non-affine transformations
            out_alpha = _resample(self, mask, out_shape, t, resample=True)
            del mask  # Make sure we don't use mask anymore!
            out_mask = np.isnan(out_alpha)
            out_alpha[out_mask] = 1
            # Apply the pixel-by-pixel alpha values if present
            alpha = self.get_alpha()
            if alpha is not None and np.ndim(alpha) > 0:
                out_alpha *= _resample(self, alpha, out_shape, t, resample=True)
            # mask and run through the norm
            resampled_masked = np.ma.masked_array(A_resampled, out_mask)
            res = self.norm(resampled_masked)
        else:
            if A.ndim == 2:  # interpolation_stage = 'rgba'
                self.norm.autoscale_None(A)
                A = self.to_rgba(A)
            if A.dtype == np.uint8:
                # uint8 is too imprecise for premultiplied alpha roundtrips.
                A = np.divide(A, 0xff, dtype=np.float32)
            alpha = self.get_alpha()
            post_apply_alpha = False
            if alpha is None:  # alpha parameter not specified
                if A.shape[2] == 3:  # image has no alpha channel
                    A = np.dstack([A, np.ones(A.shape[:2])])
            elif np.ndim(alpha) > 0:  # Array alpha
                # user-specified array alpha overrides the existing alpha channel
                A = np.dstack([A[..., :3], alpha])
            else:  # Scalar alpha
                if A.shape[2] == 3:  # broadcast scalar alpha
                    A = np.dstack([A, np.full(A.shape[:2], alpha, np.float32)])
                else:  # or apply scalar alpha to existing alpha channel
                    post_apply_alpha = True
            # Resample in premultiplied alpha space.  (TODO: Consider
            # implementing premultiplied-space resampling in
            # span_image_resample_rgba_affine::generate?)
            if float_rgba_in and np.ndim(alpha) == 0 and np.any(A[..., 3] < 1):
                # Do not modify original RGBA input
                A = A.copy()
            A[..., :3] *= A[..., 3:]
            res = _resample(self, A, out_shape, t)
            np.divide(res[..., :3], res[..., 3:], out=res[..., :3],
                        where=res[..., 3:] != 0)
            if post_apply_alpha:
                res[..., 3] *= alpha

        # res is now either a 2D array of normed (int or float) data
        # or an RGBA array of re-sampled input
        output = self.to_rgba(res, bytes=True, norm=False)
        # output is now a correctly sized RGBA array of uint8

        # Apply alpha *after* if the input was greyscale without a mask
        if A.ndim == 2:
            alpha = self._get_scalar_alpha()
            alpha_channel = output[:, :, 3]
            alpha_channel[:] = (  # Assignment will cast to uint8.
                alpha_channel.astype(np.float32) * out_alpha * alpha)

    else:
        if self._imcache is None:
            self._imcache = self.to_rgba(A, bytes=True, norm=(A.ndim == 2))
        output = self._imcache

        # Subset the input image to only the part that will be displayed.
        subset = TransformedBbox(clip_bbox, t0.inverted()).frozen()
        output = output[
            int(max(subset.ymin, 0)):
            int(min(subset.ymax + 1, output.shape[0])),
            int(max(subset.xmin, 0)):
            int(min(subset.xmax + 1, output.shape[1]))]

        t = Affine2D().translate(
            int(max(subset.xmin, 0)), int(max(subset.ymin, 0))) + t

    return output, clipped_bbox.x0, clipped_bbox.y0, t


# ==================================================
# Line: 875

def __init__(self, ax,
             *,
             cmap=None,
             norm=None,
             colorizer=None,
             interpolation=None,
             origin=None,
             extent=None,
             filternorm=True,
             filterrad=4.0,
             resample=False,
             interpolation_stage=None,
             **kwargs
             ):

    self._extent = extent

    super().__init__(
        ax,
        cmap=cmap,
        norm=norm,
        colorizer=colorizer,
        interpolation=interpolation,
        origin=origin,
        filternorm=filternorm,
        filterrad=filterrad,
        resample=resample,
        interpolation_stage=interpolation_stage,
        **kwargs
    )


# ==================================================
# Line: 1196

def __init__(self, ax,
             x=None,
             y=None,
             A=None,
             *,
             cmap=None,
             norm=None,
             colorizer=None,
             **kwargs
             ):
    """
    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        The Axes the image will belong to.
    x, y : 1D array-like, optional
        Monotonic arrays of length N+1 and M+1, respectively, specifying
        rectangle boundaries.  If not given, will default to
        ``range(N + 1)`` and ``range(M + 1)``, respectively.
    A : array-like
        The data to be color-coded. The interpretation depends on the
        shape:

        - (M, N) `~numpy.ndarray` or masked array: values to be colormapped
        - (M, N, 3): RGB array
        - (M, N, 4): RGBA array

    cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
        The Colormap instance or registered colormap name used to map
        scalar data to colors.
    norm : str or `~matplotlib.colors.Normalize`
        Maps luminance to 0-1.
    **kwargs : `~matplotlib.artist.Artist` properties
    """
    super().__init__(ax, norm=norm, cmap=cmap, colorizer=colorizer)
    self._internal_update(kwargs)
    if A is not None:
        self.set_data(x, y, A)


# ==================================================
# Line: 1330

def __init__(self, fig,
             *,
             cmap=None,
             norm=None,
             colorizer=None,
             offsetx=0,
             offsety=0,
             origin=None,
             **kwargs
             ):
    """
    cmap is a colors.Colormap instance
    norm is a colors.Normalize instance to map luminance to 0-1

    kwargs are an optional list of Artist keyword args
    """
    super().__init__(
        None,
        norm=norm,
        cmap=cmap,
        colorizer=colorizer,
        origin=origin
    )
    self.set_figure(fig)
    self.ox = offsetx
    self.oy = offsety
    self._internal_update(kwargs)
    self.magnification = 1.0


# ==================================================
# Line: 1436

def __init__(self, bbox,
             *,
             cmap=None,
             norm=None,
             colorizer=None,
             interpolation=None,
             origin=None,
             filternorm=True,
             filterrad=4.0,
             resample=False,
             **kwargs
             ):

    super().__init__(
        None,
        cmap=cmap,
        norm=norm,
        colorizer=colorizer,
        interpolation=interpolation,
        origin=origin,
        filternorm=filternorm,
        filterrad=filterrad,
        resample=resample,
        **kwargs
    )
    self.bbox = bbox


# ==================================================
# Line: 1572

def imsave(fname, arr, vmin=None, vmax=None, cmap=None, format=None,
           origin=None, dpi=100, *, metadata=None, pil_kwargs=None):
    """
    Colormap and save an array as an image file.

    RGB(A) images are passed through.  Single channel images will be
    colormapped according to *cmap* and *norm*.

    .. note::

       If you want to save a single channel image as gray scale please use an
       image I/O library (such as pillow, tifffile, or imageio) directly.

    Parameters
    ----------
    fname : str or path-like or file-like
        A path or a file-like object to store the image in.
        If *format* is not set, then the output format is inferred from the
        extension of *fname*, if any, and from :rc:`savefig.format` otherwise.
        If *format* is set, it determines the output format.
    arr : array-like
        The image data. Accepts NumPy arrays or sequences
        (e.g., lists or tuples). The shape can be one of
        MxN (luminance), MxNx3 (RGB) or MxNx4 (RGBA).
    vmin, vmax : float, optional
        *vmin* and *vmax* set the color scaling for the image by fixing the
        values that map to the colormap color limits. If either *vmin*
        or *vmax* is None, that limit is determined from the *arr*
        min/max value.
    cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
        A Colormap instance or registered colormap name. The colormap
        maps scalar data to colors. It is ignored for RGB(A) data.
    format : str, optional
        The file format, e.g. 'png', 'pdf', 'svg', ...  The behavior when this
        is unset is documented under *fname*.
    origin : {'upper', 'lower'}, default: :rc:`image.origin`
        Indicates whether the ``(0, 0)`` index of the array is in the upper
        left or lower left corner of the Axes.
    dpi : float
        The DPI to store in the metadata of the file.  This does not affect the
        resolution of the output image.  Depending on file format, this may be
        rounded to the nearest integer.
    metadata : dict, optional
        Metadata in the image file.  The supported keys depend on the output
        format, see the documentation of the respective backends for more
        information.
        Currently only supported for "png", "pdf", "ps", "eps", and "svg".
    pil_kwargs : dict, optional
        Keyword arguments passed to `PIL.Image.Image.save`.  If the 'pnginfo'
        key is present, it completely overrides *metadata*, including the
        default 'Software' key.
    """
    from matplotlib.figure import Figure

    # Normalizing input (e.g., list or tuples) to NumPy array if needed
    arr = np.asanyarray(arr)

    if isinstance(fname, os.PathLike):
        fname = os.fspath(fname)
    if format is None:
        format = (Path(fname).suffix[1:] if isinstance(fname, str)
                  else mpl.rcParams["savefig.format"]).lower()
    if format in ["pdf", "ps", "eps", "svg"]:
        # Vector formats that are not handled by PIL.
        if pil_kwargs is not None:
            raise ValueError(
                f"Cannot use 'pil_kwargs' when saving to {format}")
        fig = Figure(dpi=dpi, frameon=False)
        fig.figimage(arr, cmap=cmap, vmin=vmin, vmax=vmax, origin=origin,
                     resize=True)
        fig.savefig(fname, dpi=dpi, format=format, transparent=True,
                    metadata=metadata)
    else:
        # Don't bother creating an image; this avoids rounding errors on the
        # size when dividing and then multiplying by dpi.
        origin = mpl._val_or_rc(origin, "image.origin")
        _api.check_in_list(('upper', 'lower'), origin=origin)
        if origin == "lower":
            arr = arr[::-1]
        if (isinstance(arr, memoryview) and arr.format == "B"
                and arr.ndim == 3 and arr.shape[-1] == 4):
            # Such an ``arr`` would also be handled fine by sm.to_rgba below
            # (after casting with asarray), but it is useful to special-case it
            # because that's what backend_agg passes, and can be in fact used
            # as is, saving a few operations.
            rgba = arr
        else:
            sm = mcolorizer.Colorizer(cmap=cmap)
            sm.set_clim(vmin, vmax)
            rgba = sm.to_rgba(arr, bytes=True)
        if pil_kwargs is None:
            pil_kwargs = {}
        else:
            # we modify this below, so make a copy (don't modify caller's dict)
            pil_kwargs = pil_kwargs.copy()
        pil_shape = (rgba.shape[1], rgba.shape[0])
        rgba = np.require(rgba, requirements='C')
        image = PIL.Image.frombuffer(
            "RGBA", pil_shape, rgba, "raw", "RGBA", 0, 1)
        if format == "png":
            # Only use the metadata kwarg if pnginfo is not set, because the
            # semantics of duplicate keys in pnginfo is unclear.
            if "pnginfo" in pil_kwargs:
                if metadata:
                    _api.warn_external("'metadata' is overridden by the "
                                       "'pnginfo' entry in 'pil_kwargs'.")
            else:
                metadata = {
                    "Software": (f"Matplotlib version{mpl.__version__}, "
                                 f"https://matplotlib.org/"),
                    **(metadata if metadata is not None else {}),
                }
                pil_kwargs["pnginfo"] = pnginfo = PIL.PngImagePlugin.PngInfo()
                for k, v in metadata.items():
                    if v is not None:
                        pnginfo.add_text(k, v)
        elif metadata is not None:
            raise ValueError(f"metadata not supported for format {format!r}")
        if format in ["jpg", "jpeg"]:
            format = "jpeg"  # Pillow doesn't recognize "jpg".
            facecolor = mpl.rcParams["savefig.facecolor"]
            if cbook._str_equal(facecolor, "auto"):
                facecolor = mpl.rcParams["figure.facecolor"]
            color = tuple(int(x * 255) for x in mcolors.to_rgb(facecolor))
            background = PIL.Image.new("RGB", pil_shape, color)
            background.paste(image, image)
            image = background
        pil_kwargs.setdefault("format", format)
        pil_kwargs.setdefault("dpi", (dpi, dpi))
        image.save(fname, **pil_kwargs)



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/contour.py
# Line: 62

def clabel(self, levels=None, *,
           fontsize=None, inline=True, inline_spacing=5, fmt=None,
           colors=None, use_clabeltext=False, manual=False,
           rightside_up=True, zorder=None):
    """
    Label a contour plot.

    Adds labels to line contours in this `.ContourSet` (which inherits from
    this mixin class).

    Parameters
    ----------
    levels : array-like, optional
        A list of level values, that should be labeled. The list must be
        a subset of ``cs.levels``. If not given, all levels are labeled.

    fontsize : str or float, default: :rc:`font.size`
        Size in points or relative size e.g., 'smaller', 'x-large'.
        See `.Text.set_size` for accepted string values.

    colors : :mpltype:`color` or colors or None, default: None
        The label colors:

        - If *None*, the color of each label matches the color of
          the corresponding contour.

        - If one string color, e.g., *colors* = 'r' or *colors* =
          'red', all labels will be plotted in this color.

        - If a tuple of colors (string, float, RGB, etc), different labels
          will be plotted in different colors in the order specified.

    inline : bool, default: True
        If ``True`` the underlying contour is removed where the label is
        placed.

    inline_spacing : float, default: 5
        Space in pixels to leave on each side of label when placing inline.

        This spacing will be exact for labels at locations where the
        contour is straight, less so for labels on curved contours.

    fmt : `.Formatter` or str or callable or dict, optional
        How the levels are formatted:

        - If a `.Formatter`, it is used to format all levels at once, using
          its `.Formatter.format_ticks` method.
        - If a str, it is interpreted as a %-style format string.
        - If a callable, it is called with one level at a time and should
          return the corresponding label.
        - If a dict, it should directly map levels to labels.

        The default is to use a standard `.ScalarFormatter`.

    manual : bool or iterable, default: False
        If ``True``, contour labels will be placed manually using
        mouse clicks. Click the first button near a contour to
        add a label, click the second button (or potentially both
        mouse buttons at once) to finish adding labels. The third
        button can be used to remove the last label added, but
        only if labels are not inline. Alternatively, the keyboard
        can be used to select label locations (enter to end label
        placement, delete or backspace act like the third mouse button,
        and any other key will select a label location).

        *manual* can also be an iterable object of (x, y) tuples.
        Contour labels will be created as if mouse is clicked at each
        (x, y) position.

    rightside_up : bool, default: True
        If ``True``, label rotations will always be plus
        or minus 90 degrees from level.

    use_clabeltext : bool, default: False
        If ``True``, use `.Text.set_transform_rotates_text` to ensure that
        label rotation is updated whenever the Axes aspect changes.

    zorder : float or None, default: ``(2 + contour.get_zorder())``
        zorder of the contour labels.

    Returns
    -------
    labels
        A list of `.Text` instances for the labels.
    """

    # Based on the input arguments, clabel() adds a list of "label
    # specific" attributes to the ContourSet object.  These attributes are
    # all of the form label* and names should be fairly self explanatory.
    #
    # Once these attributes are set, clabel passes control to the labels()
    # method (for automatic label placement) or blocking_input_loop and
    # _contour_labeler_event_handler (for manual label placement).

    if fmt is None:
        fmt = ticker.ScalarFormatter(useOffset=False)
        fmt.create_dummy_axis()
    self.labelFmt = fmt
    self._use_clabeltext = use_clabeltext
    self.labelManual = manual
    self.rightside_up = rightside_up
    self._clabel_zorder = 2 + self.get_zorder() if zorder is None else zorder

    if levels is None:
        levels = self.levels
        indices = list(range(len(self.cvalues)))
    else:
        levlabs = list(levels)
        indices, levels = [], []
        for i, lev in enumerate(self.levels):
            if lev in levlabs:
                indices.append(i)
                levels.append(lev)
        if len(levels) < len(levlabs):
            raise ValueError(f"Specified levels {levlabs} don't match "
                             f"available levels {self.levels}")
    self.labelLevelList = levels
    self.labelIndiceList = indices

    self._label_font_props = font_manager.FontProperties(size=fontsize)

    if colors is None:
        self.labelMappable = self
        self.labelCValueList = np.take(self.cvalues, self.labelIndiceList)
    else:
        # handling of explicit colors for labels:
        # make labelCValueList contain integers [0, 1, 2, ...] and a cmap
        # so that cmap(i) == colors[i]
        num_levels = len(self.labelLevelList)
        colors = cbook._resize_sequence(mcolors.to_rgba_array(colors), num_levels)
        self.labelMappable = cm.ScalarMappable(
            cmap=mcolors.ListedColormap(colors), norm=mcolors.NoNorm())
        self.labelCValueList = list(range(num_levels))

    self.labelXYs = []

    if np.iterable(manual):
        for x, y in manual:
            self.add_label_near(x, y, inline, inline_spacing)
    elif manual:
        print('Select label locations manually using first mouse button.')
        print('End manual selection with second mouse button.')
        if not inline:
            print('Remove last label by clicking third mouse button.')
        mpl._blocking_input.blocking_input_loop(
            self.axes.get_figure(root=True),
            ["button_press_event", "key_press_event"],
            timeout=-1, handler=functools.partial(
                _contour_labeler_event_handler,
                self, inline, inline_spacing))
    else:
        self.labels(inline, inline_spacing)

    return cbook.silent_list('text.Text', self.labelTexts)


# ==================================================
# Line: 600

def __init__(self, ax, *args,
             levels=None, filled=False, linewidths=None, linestyles=None,
             hatches=(None,), alpha=None, origin=None, extent=None,
             cmap=None, colors=None, norm=None, vmin=None, vmax=None,
             colorizer=None, extend='neither', antialiased=None, nchunk=0,
             locator=None, transform=None, negative_linestyles=None, clip_path=None,
             **kwargs):
    """
    Draw contour lines or filled regions, depending on
    whether keyword arg *filled* is ``False`` (default) or ``True``.

    Call signature::

        ContourSet(ax, levels, allsegs, [allkinds], **kwargs)

    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        The `~.axes.Axes` object to draw on.

    levels : [level0, level1, ..., leveln]
        A list of floating point numbers indicating the contour
        levels.

    allsegs : [level0segs, level1segs, ...]
        List of all the polygon segments for all the *levels*.
        For contour lines ``len(allsegs) == len(levels)``, and for
        filled contour regions ``len(allsegs) = len(levels)-1``. The lists
        should look like ::

            level0segs = [polygon0, polygon1, ...]
            polygon0 = [[x0, y0], [x1, y1], ...]

    allkinds : [level0kinds, level1kinds, ...], optional
        Optional list of all the polygon vertex kinds (code types), as
        described and used in Path. This is used to allow multiply-
        connected paths such as holes within filled polygons.
        If not ``None``, ``len(allkinds) == len(allsegs)``. The lists
        should look like ::

            level0kinds = [polygon0kinds, ...]
            polygon0kinds = [vertexcode0, vertexcode1, ...]

        If *allkinds* is not ``None``, usually all polygons for a
        particular contour level are grouped together so that
        ``level0segs = [polygon0]`` and ``level0kinds = [polygon0kinds]``.

    **kwargs
        Keyword arguments are as described in the docstring of
        `~.Axes.contour`.
    """
    if antialiased is None and filled:
        # Eliminate artifacts; we are not stroking the boundaries.
        antialiased = False
        # The default for line contours will be taken from the
        # LineCollection default, which uses :rc:`lines.antialiased`.
    super().__init__(
        antialiaseds=antialiased,
        alpha=alpha,
        clip_path=clip_path,
        transform=transform,
        colorizer=colorizer,
    )
    self.axes = ax
    self.levels = levels
    self.filled = filled
    self.hatches = hatches
    self.origin = origin
    self.extent = extent
    self.colors = colors
    self.extend = extend

    self.nchunk = nchunk
    self.locator = locator

    if colorizer:
        self._set_colorizer_check_keywords(colorizer, cmap=cmap,
                                           norm=norm, vmin=vmin,
                                           vmax=vmax, colors=colors)
        norm = colorizer.norm
        cmap = colorizer.cmap
    if (isinstance(norm, mcolors.LogNorm)
            or isinstance(self.locator, ticker.LogLocator)):
        self.logscale = True
        if norm is None:
            norm = mcolors.LogNorm()
    else:
        self.logscale = False

    _api.check_in_list([None, 'lower', 'upper', 'image'], origin=origin)
    if self.extent is not None and len(self.extent) != 4:
        raise ValueError(
            "If given, 'extent' must be None or (x0, x1, y0, y1)")
    if self.colors is not None and cmap is not None:
        raise ValueError('Either colors or cmap must be None')
    if self.origin == 'image':
        self.origin = mpl.rcParams['image.origin']

    self._orig_linestyles = linestyles  # Only kept for user access.
    self.negative_linestyles = mpl._val_or_rc(negative_linestyles,
                                              'contour.negative_linestyle')

    kwargs = self._process_args(*args, **kwargs)
    self._process_levels()

    self._extend_min = self.extend in ['min', 'both']
    self._extend_max = self.extend in ['max', 'both']
    if self.colors is not None:
        if mcolors.is_color_like(self.colors):
            color_sequence = [self.colors]
        else:
            color_sequence = self.colors

        ncolors = len(self.levels)
        if self.filled:
            ncolors -= 1
        i0 = 0

        # Handle the case where colors are given for the extended
        # parts of the contour.

        use_set_under_over = False
        # if we are extending the lower end, and we've been given enough
        # colors then skip the first color in the resulting cmap. For the
        # extend_max case we don't need to worry about passing more colors
        # than ncolors as ListedColormap will clip.
        total_levels = (ncolors +
                        int(self._extend_min) +
                        int(self._extend_max))
        if (len(color_sequence) == total_levels and
                (self._extend_min or self._extend_max)):
            use_set_under_over = True
            if self._extend_min:
                i0 = 1

        cmap = mcolors.ListedColormap(
            cbook._resize_sequence(color_sequence[i0:], ncolors))

        if use_set_under_over:
            if self._extend_min:
                cmap.set_under(color_sequence[0])
            if self._extend_max:
                cmap.set_over(color_sequence[-1])

    # label lists must be initialized here
    self.labelTexts = []
    self.labelCValues = []

    self.set_cmap(cmap)
    if norm is not None:
        self.set_norm(norm)
    with self.norm.callbacks.blocked(signal="changed"):
        if vmin is not None:
            self.norm.vmin = vmin
        if vmax is not None:
            self.norm.vmax = vmax
    self.norm._changed()
    self._process_colors()

    if self._paths is None:
        self._paths = self._make_paths_from_contour_generator()

    if self.filled:
        if linewidths is not None:
            _api.warn_external('linewidths is ignored by contourf')
        # Lower and upper contour levels.
        lowers, uppers = self._get_lowers_and_uppers()
        self.set(
            edgecolor="none",
            # Default zorder taken from Collection
            zorder=kwargs.pop("zorder", 1),
            rasterized=kwargs.pop("rasterized", False),
        )

    else:
        self.set(
            facecolor="none",
            linewidths=self._process_linewidths(linewidths),
            linestyle=self._process_linestyles(linestyles),
            # Default zorder taken from LineCollection, which is higher
            # than for filled contours so that lines are displayed on top.
            zorder=kwargs.pop("zorder", 2),
            label="_nolegend_",
        )

    self.axes.add_collection(self, autolim=False)
    self.sticky_edges.x[:] = [self._mins[0], self._maxs[0]]
    self.sticky_edges.y[:] = [self._mins[1], self._maxs[1]]
    self.axes.update_datalim([self._mins, self._maxs])
    self.axes.autoscale_view(tight=True)

    self.changed()  # set the colors

    if kwargs:
        _api.warn_external(
            'The following kwargs were not used by contour: ' +
            ", ".join(map(repr, kwargs))
        )


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/patches.py
# Line: 48

def __init__(self, *,
             edgecolor=None,
             facecolor=None,
             color=None,
             linewidth=None,
             linestyle=None,
             antialiased=None,
             hatch=None,
             fill=True,
             capstyle=None,
             joinstyle=None,
             hatchcolor=None,
             **kwargs):
    """
    The following kwarg properties are supported

    %(Patch:kwdoc)s
    """
    super().__init__()

    if linestyle is None:
        linestyle = "solid"
    if capstyle is None:
        capstyle = CapStyle.butt
    if joinstyle is None:
        joinstyle = JoinStyle.miter

    self._hatch_linewidth = mpl.rcParams['hatch.linewidth']
    self._fill = bool(fill)  # needed for set_facecolor call
    if color is not None:
        if edgecolor is not None or facecolor is not None:
            _api.warn_external(
                "Setting the 'color' property will override "
                "the edgecolor or facecolor properties.")
        self.set_color(color)
    else:
        self.set_edgecolor(edgecolor)
        self.set_hatchcolor(hatchcolor)
        self.set_facecolor(facecolor)

    self._linewidth = 0
    self._unscaled_dash_pattern = (0, None)  # offset, dash
    self._dash_pattern = (0, None)  # offset, dash (scaled by linewidth)

    self.set_linestyle(linestyle)
    self.set_linewidth(linewidth)
    self.set_antialiased(antialiased)
    self.set_hatch(hatch)
    self.set_capstyle(capstyle)
    self.set_joinstyle(joinstyle)

    if len(kwargs):
        self._internal_update(kwargs)


# ==================================================
# Line: 1430

def __init__(self, x, y, dx, dy, *,
             width=0.001, length_includes_head=False, head_width=None,
             head_length=None, shape='full', overhang=0,
             head_starts_at_zero=False, **kwargs):
    """
    Parameters
    ----------
    x, y : float
        The x and y coordinates of the arrow base.

    dx, dy : float
        The length of the arrow along x and y direction.

    width : float, default: 0.001
        Width of full arrow tail.

    length_includes_head : bool, default: False
        True if head is to be counted in calculating the length.

    head_width : float or None, default: 3*width
        Total width of the full arrow head.

    head_length : float or None, default: 1.5*head_width
        Length of arrow head.

    shape : {'full', 'left', 'right'}, default: 'full'
        Draw the left-half, right-half, or full arrow.

    overhang : float, default: 0
        Fraction that the arrow is swept back (0 overhang means
        triangular shape). Can be negative or greater than one.

    head_starts_at_zero : bool, default: False
        If True, the head starts being drawn at coordinate 0
        instead of ending at coordinate 0.

    **kwargs
        `.Patch` properties:

        %(Patch:kwdoc)s
    """
    self._x = x
    self._y = y
    self._dx = dx
    self._dy = dy
    self._width = width
    self._length_includes_head = length_includes_head
    self._head_width = head_width
    self._head_length = head_length
    self._shape = shape
    self._overhang = overhang
    self._head_starts_at_zero = head_starts_at_zero
    self._make_verts()
    super().__init__(self.verts, closed=True, **kwargs)


# ==================================================
# Line: 1485

def set_data(self, *, x=None, y=None, dx=None, dy=None, width=None,
             head_width=None, head_length=None):
    """
    Set `.FancyArrow` x, y, dx, dy, width, head_with, and head_length.
    Values left as None will not be updated.

    Parameters
    ----------
    x, y : float or None, default: None
        The x and y coordinates of the arrow base.

    dx, dy : float or None, default: None
        The length of the arrow along x and y direction.

    width : float or None, default: None
        Width of full arrow tail.

    head_width : float or None, default: None
        Total width of the full arrow head.

    head_length : float or None, default: None
        Length of arrow head.
    """
    if x is not None:
        self._x = x
    if y is not None:
        self._y = y
    if dx is not None:
        self._dx = dx
    if dy is not None:
        self._dy = dy
    if width is not None:
        self._width = width
    if head_width is not None:
        self._head_width = head_width
    if head_length is not None:
        self._head_length = head_length
    self._make_verts()
    self.set_xy(self.verts)


# ==================================================
# Line: 2042

def __init__(self, xy, width, height, *,
             angle=0.0, theta1=0.0, theta2=360.0, **kwargs):
    """
    Parameters
    ----------
    xy : (float, float)
        The center of the ellipse.

    width : float
        The length of the horizontal axis.

    height : float
        The length of the vertical axis.

    angle : float
        Rotation of the ellipse in degrees (counterclockwise).

    theta1, theta2 : float, default: 0, 360
        Starting and ending angles of the arc in degrees. These values
        are relative to *angle*, e.g. if *angle* = 45 and *theta1* = 90
        the absolute starting angle is 135.
        Default *theta1* = 0, *theta2* = 360, i.e. a complete ellipse.
        The arc is drawn in the counterclockwise direction.
        Angles greater than or equal to 360, or smaller than 0, are
        represented by an equivalent angle in the range [0, 360), by
        taking the input value mod 360.

    Other Parameters
    ----------------
    **kwargs : `~matplotlib.patches.Patch` properties
        Most `.Patch` properties are supported as keyword arguments,
        except *fill* and *facecolor* because filling is not supported.

    %(Patch:kwdoc)s
    """
    fill = kwargs.setdefault('fill', False)
    if fill:
        raise ValueError("Arc objects cannot be filled")

    super().__init__(xy, width, height, angle=angle, **kwargs)

    self.theta1 = theta1
    self.theta2 = theta2
    (self._theta1, self._theta2, self._stretched_width,
     self._stretched_height) = self._theta_stretch()
    self._path = Path.arc(self._theta1, self._theta2)


# ==================================================
# Line: 2848

def __call__(self, posA, posB,
             shrinkA=2., shrinkB=2., patchA=None, patchB=None):
    """
    Call the *connect* method to create a path between *posA* and
    *posB*; then clip and shrink the path.
    """
    path = self.connect(posA, posB)
    path = self._clip(
        path,
        self._in_patch(patchA) if patchA else None,
        self._in_patch(patchB) if patchB else None,
    )
    path = self._clip(
        path,
        inside_circle(*path.vertices[0], shrinkA) if shrinkA else None,
        inside_circle(*path.vertices[-1], shrinkB) if shrinkB else None
    )
    return path


# ==================================================
# Line: 3323

def __init__(self, head_length=.4, head_width=.2, widthA=1., widthB=1.,
             lengthA=0.2, lengthB=0.2, angleA=0, angleB=0, scaleA=None,
             scaleB=None):
    """
    Parameters
    ----------
    head_length : float, default: 0.4
        Length of the arrow head, relative to *mutation_size*.
    head_width : float, default: 0.2
        Width of the arrow head, relative to *mutation_size*.
    widthA, widthB : float, default: 1.0
        Width of the bracket.
    lengthA, lengthB : float, default: 0.2
        Length of the bracket.
    angleA, angleB : float, default: 0
        Orientation of the bracket, as a counterclockwise angle.
        0 degrees means perpendicular to the line.
    scaleA, scaleB : float, default: *mutation_size*
        The scale of the brackets.
    """

    self.head_length, self.head_width = head_length, head_width
    self.widthA, self.widthB = widthA, widthB
    self.lengthA, self.lengthB = lengthA, lengthB
    self.angleA, self.angleB = angleA, angleB
    self.scaleA, self.scaleB = scaleA, scaleB

    self._beginarrow_head = False
    self._beginarrow_bracket = False
    self._endarrow_head = False
    self._endarrow_bracket = False

    if "-" not in self.arrow:
        raise ValueError("arrow must have the '-' between "
                         "the two heads")

    beginarrow, endarrow = self.arrow.split("-", 1)

    if beginarrow == "<":
        self._beginarrow_head = True
        self._beginarrow_bracket = False
    elif beginarrow == "<|":
        self._beginarrow_head = True
        self._beginarrow_bracket = False
        self.fillbegin = True
    elif beginarrow in ("]", "|"):
        self._beginarrow_head = False
        self._beginarrow_bracket = True

    if endarrow == ">":
        self._endarrow_head = True
        self._endarrow_bracket = False
    elif endarrow == "|>":
        self._endarrow_head = True
        self._endarrow_bracket = False
        self.fillend = True
    elif endarrow in ("[", "|"):
        self._endarrow_head = False
        self._endarrow_bracket = True

    super().__init__()


# ==================================================
# Line: 3385

def _get_arrow_wedge(self, x0, y0, x1, y1,
                     head_dist, cos_t, sin_t, linewidth):
    """
    Return the paths for arrow heads. Since arrow lines are
    drawn with capstyle=projected, The arrow goes beyond the
    desired point. This method also returns the amount of the path
    to be shrunken so that it does not overshoot.
    """

    # arrow from x0, y0 to x1, y1
    dx, dy = x0 - x1, y0 - y1

    cp_distance = np.hypot(dx, dy)

    # pad_projected : amount of pad to account the
    # overshooting of the projection of the wedge
    pad_projected = (.5 * linewidth / sin_t)

    # Account for division by zero
    if cp_distance == 0:
        cp_distance = 1

    # apply pad for projected edge
    ddx = pad_projected * dx / cp_distance
    ddy = pad_projected * dy / cp_distance

    # offset for arrow wedge
    dx = dx / cp_distance * head_dist
    dy = dy / cp_distance * head_dist

    dx1, dy1 = cos_t * dx + sin_t * dy, -sin_t * dx + cos_t * dy
    dx2, dy2 = cos_t * dx - sin_t * dy, sin_t * dx + cos_t * dy

    vertices_arrow = [(x1 + ddx + dx1, y1 + ddy + dy1),
                      (x1 + ddx, y1 + ddy),
                      (x1 + ddx + dx2, y1 + ddy + dy2)]
    codes_arrow = [Path.MOVETO,
                   Path.LINETO,
                   Path.LINETO]

    return vertices_arrow, codes_arrow, ddx, ddy


# ==================================================
# Line: 3427

def _get_bracket(self, x0, y0,
                 x1, y1, width, length, angle):

    cos_t, sin_t = get_cos_sin(x1, y1, x0, y0)

    # arrow from x0, y0 to x1, y1
    from matplotlib.bezier import get_normal_points
    x1, y1, x2, y2 = get_normal_points(x0, y0, cos_t, sin_t, width)

    dx, dy = length * cos_t, length * sin_t

    vertices_arrow = [(x1 + dx, y1 + dy),
                      (x1, y1),
                      (x2, y2),
                      (x2 + dx, y2 + dy)]
    codes_arrow = [Path.MOVETO,
                   Path.LINETO,
                   Path.LINETO,
                   Path.LINETO]

    if angle:
        trans = transforms.Affine2D().rotate_deg_around(x0, y0, angle)
        vertices_arrow = trans.transform(vertices_arrow)

    return vertices_arrow, codes_arrow


# ==================================================
# Line: 3620

def __init__(self,
             widthA=1., lengthA=0.2, angleA=0,
             widthB=1., lengthB=0.2, angleB=0):
    """
    Parameters
    ----------
    widthA, widthB : float, default: 1.0
        Width of the bracket.
    lengthA, lengthB : float, default: 0.2
        Length of the bracket.
    angleA, angleB : float, default: 0 degrees
        Orientation of the bracket, as a counterclockwise angle.
        0 degrees means perpendicular to the line.
    """
    super().__init__(widthA=widthA, lengthA=lengthA, angleA=angleA,
                     widthB=widthB, lengthB=lengthB, angleB=angleB)


# ==================================================
# Line: 3928

def __init__(self, xy, width, height, boxstyle="round", *,
             mutation_scale=1, mutation_aspect=1, **kwargs):
    """
    Parameters
    ----------
    xy : (float, float)
      The lower left corner of the box.

    width : float
        The width of the box.

    height : float
        The height of the box.

    boxstyle : str or `~matplotlib.patches.BoxStyle`
        The style of the fancy box. This can either be a `.BoxStyle`
        instance or a string of the style name and optionally comma
        separated attributes (e.g. "Round, pad=0.2"). This string is
        passed to `.BoxStyle` to construct a `.BoxStyle` object. See
        there for a full documentation.

        The following box styles are available:

        %(BoxStyle:table)s

    mutation_scale : float, default: 1
        Scaling factor applied to the attributes of the box style
        (e.g. pad or rounding_size).

    mutation_aspect : float, default: 1
        The height of the rectangle will be squeezed by this value before
        the mutation and the mutated box will be stretched by the inverse
        of it. For example, this allows different horizontal and vertical
        padding.

    Other Parameters
    ----------------
    **kwargs : `~matplotlib.patches.Patch` properties

    %(Patch:kwdoc)s
    """

    super().__init__(**kwargs)
    self._x, self._y = xy
    self._width = width
    self._height = height
    self.set_boxstyle(boxstyle)
    self._mutation_scale = mutation_scale
    self._mutation_aspect = mutation_aspect
    self.stale = True


# ==================================================
# Line: 4180

def __init__(self, posA=None, posB=None, *,
             path=None, arrowstyle="simple", connectionstyle="arc3",
             patchA=None, patchB=None, shrinkA=2, shrinkB=2,
             mutation_scale=1, mutation_aspect=1, **kwargs):
    """
    **Defining the arrow position and path**

    There are two ways to define the arrow position and path:

    - **Start, end and connection**:
      The typical approach is to define the start and end points of the
      arrow using *posA* and *posB*. The curve between these two can
      further be configured using *connectionstyle*.

      If given, the arrow curve is clipped by *patchA* and *patchB*,
      allowing it to start/end at the border of these patches.
      Additionally, the arrow curve can be shortened by *shrinkA* and *shrinkB*
      to create a margin between start/end (after possible clipping) and the
      drawn arrow.

    - **path**: Alternatively if *path* is provided, an arrow is drawn along
      this Path. In this case, *connectionstyle*, *patchA*, *patchB*,
      *shrinkA*, and *shrinkB* are ignored.

    **Styling**

    The *arrowstyle* defines the styling of the arrow head, tail and shaft.
    The resulting arrows can be styled further by setting the `.Patch`
    properties such as *linewidth*, *color*, *facecolor*, *edgecolor*
    etc. via keyword arguments.

    Parameters
    ----------
    posA, posB : (float, float), optional
        (x, y) coordinates of start and end point of the arrow.
        The actually drawn start and end positions may be modified
        through *patchA*, *patchB*, *shrinkA*, and *shrinkB*.

        *posA*, *posB* are exclusive of *path*.

    path : `~matplotlib.path.Path`, optional
        If provided, an arrow is drawn along this path and *patchA*,
        *patchB*, *shrinkA*, and *shrinkB* are ignored.

        *path* is exclusive of *posA*, *posB*.

    arrowstyle : str or `.ArrowStyle`, default: 'simple'
        The styling of arrow head, tail and shaft. This can be

        - `.ArrowStyle` or one of its subclasses
        - The shorthand string name (e.g. "->") as given in the table below,
          optionally containing a comma-separated list of style parameters,
          e.g. "->, head_length=10, head_width=5".

        The style parameters are scaled by *mutation_scale*.

        The following arrow styles are available. See also
        :doc:`/gallery/text_labels_and_annotations/fancyarrow_demo`.

        %(ArrowStyle:table)s

        Only the styles ``<|-``, ``-|>``, ``<|-|>`` ``simple``, ``fancy``
        and ``wedge`` contain closed paths and can be filled.

    connectionstyle : str or `.ConnectionStyle` or None, optional, \

# ==================================================
# Line: 4548

def __init__(self, xyA, xyB, coordsA, coordsB=None, *,
             axesA=None, axesB=None,
             arrowstyle="-",
             connectionstyle="arc3",
             patchA=None,
             patchB=None,
             shrinkA=0.,
             shrinkB=0.,
             mutation_scale=10.,
             mutation_aspect=None,
             clip_on=False,
             **kwargs):
    """
    Connect point *xyA* in *coordsA* with point *xyB* in *coordsB*.

    Valid keys are

    ===============  ======================================================
    Key              Description
    ===============  ======================================================
    arrowstyle       the arrow style
    connectionstyle  the connection style
    relpos           default is (0.5, 0.5)
    patchA           default is bounding box of the text
    patchB           default is None
    shrinkA          default is 2 points
    shrinkB          default is 2 points
    mutation_scale   default is text size (in points)
    mutation_aspect  default is 1.
    ?                any key for `matplotlib.patches.PathPatch`
    ===============  ======================================================

    *coordsA* and *coordsB* are strings that indicate the
    coordinates of *xyA* and *xyB*.

    ==================== ==================================================
    Property             Description
    ==================== ==================================================
    'figure points'      points from the lower left corner of the figure
    'figure pixels'      pixels from the lower left corner of the figure
    'figure fraction'    0, 0 is lower left of figure and 1, 1 is upper
                         right
    'subfigure points'   points from the lower left corner of the subfigure
    'subfigure pixels'   pixels from the lower left corner of the subfigure
    'subfigure fraction' fraction of the subfigure, 0, 0 is lower left.
    'axes points'        points from lower left corner of the Axes
    'axes pixels'        pixels from lower left corner of the Axes
    'axes fraction'      0, 0 is lower left of Axes and 1, 1 is upper right
    'data'               use the coordinate system of the object being
                         annotated (default)
    'offset points'      offset (in points) from the *xy* value
    'polar'              you can specify *theta*, *r* for the annotation,
                         even in cartesian plots.  Note that if you are
                         using a polar Axes, you do not need to specify
                         polar for the coordinate system since that is the
                         native "data" coordinate system.
    ==================== ==================================================

    Alternatively they can be set to any valid
    `~matplotlib.transforms.Transform`.

    Note that 'subfigure pixels' and 'figure pixels' are the same
    for the parent figure, so users who want code that is usable in
    a subfigure can use 'subfigure pixels'.

    .. note::

       Using `ConnectionPatch` across two `~.axes.Axes` instances
       is not directly compatible with :ref:`constrained layout
       <constrainedlayout_guide>`. Add the artist
       directly to the `.Figure` instead of adding it to a specific Axes,
       or exclude it from the layout using ``con.set_in_layout(False)``.

       .. code-block:: default

          fig, ax = plt.subplots(1, 2, constrained_layout=True)
          con = ConnectionPatch(..., axesA=ax[0], axesB=ax[1])
          fig.add_artist(con)

    """
    if coordsB is None:
        coordsB = coordsA
    # we'll draw ourself after the artist we annotate by default
    self.xy1 = xyA
    self.xy2 = xyB
    self.coords1 = coordsA
    self.coords2 = coordsB

    self.axesA = axesA
    self.axesB = axesB

    super().__init__(posA=(0, 0), posB=(1, 1),
                     arrowstyle=arrowstyle,
                     connectionstyle=connectionstyle,
                     patchA=patchA, patchB=patchB,
                     shrinkA=shrinkA, shrinkB=shrinkB,
                     mutation_scale=mutation_scale,
                     mutation_aspect=mutation_aspect,
                     clip_on=clip_on,
                     **kwargs)
    # if True, draw annotation only if self.xy is inside the Axes
    self._annotation_clip = None


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/gridspec.py
# Line: 314

def __init__(self, nrows, ncols, figure=None,
             left=None, bottom=None, right=None, top=None,
             wspace=None, hspace=None,
             width_ratios=None, height_ratios=None):
    """
    Parameters
    ----------
    nrows, ncols : int
        The number of rows and columns of the grid.

    figure : `.Figure`, optional
        Only used for constrained layout to create a proper layoutgrid.

    left, right, top, bottom : float, optional
        Extent of the subplots as a fraction of figure width or height.
        Left cannot be larger than right, and bottom cannot be larger than
        top. If not given, the values will be inferred from a figure or
        rcParams at draw time. See also `GridSpec.get_subplot_params`.

    wspace : float, optional
        The amount of width reserved for space between subplots,
        expressed as a fraction of the average axis width.
        If not given, the values will be inferred from a figure or
        rcParams when necessary. See also `GridSpec.get_subplot_params`.

    hspace : float, optional
        The amount of height reserved for space between subplots,
        expressed as a fraction of the average axis height.
        If not given, the values will be inferred from a figure or
        rcParams when necessary. See also `GridSpec.get_subplot_params`.

    width_ratios : array-like of length *ncols*, optional
        Defines the relative widths of the columns. Each column gets a
        relative width of ``width_ratios[i] / sum(width_ratios)``.
        If not given, all columns will have the same width.

    height_ratios : array-like of length *nrows*, optional
        Defines the relative heights of the rows. Each row gets a
        relative height of ``height_ratios[i] / sum(height_ratios)``.
        If not given, all rows will have the same height.

    """
    self.left = left
    self.bottom = bottom
    self.right = right
    self.top = top
    self.wspace = wspace
    self.hspace = hspace
    self.figure = figure

    super().__init__(nrows, ncols,
                     width_ratios=width_ratios,
                     height_ratios=height_ratios)


# ==================================================
# Line: 370

def update(self, *, left=_UNSET, bottom=_UNSET, right=_UNSET, top=_UNSET,
           wspace=_UNSET, hspace=_UNSET):
    """
    Update the subplot parameters of the grid.

    Parameters that are not explicitly given are not changed. Setting a
    parameter to *None* resets it to :rc:`figure.subplot.*`.

    Parameters
    ----------
    left, right, top, bottom : float or None, optional
        Extent of the subplots as a fraction of figure width or height.
    wspace, hspace : float or None, optional
        Spacing between the subplots as a fraction of the average subplot
        width / height.
    """
    if left is not _UNSET:
        self.left = left
    if bottom is not _UNSET:
        self.bottom = bottom
    if right is not _UNSET:
        self.right = right
    if top is not _UNSET:
        self.top = top
    if wspace is not _UNSET:
        self.wspace = wspace
    if hspace is not _UNSET:
        self.hspace = hspace

    for figmanager in _pylab_helpers.Gcf.figs.values():
        for ax in figmanager.canvas.figure.axes:
            if ax.get_subplotspec() is not None:
                ss = ax.get_subplotspec().get_topmost_subplotspec()
                if ss.get_gridspec() == self:
                    fig = ax.get_figure(root=False)
                    ax._set_position(ax.get_subplotspec().get_position(fig))


# ==================================================
# Line: 439

def tight_layout(self, figure, renderer=None,
                 pad=1.08, h_pad=None, w_pad=None, rect=None):
    """
    Adjust subplot parameters to give specified padding.

    Parameters
    ----------
    figure : `.Figure`
        The figure.
    renderer :  `.RendererBase` subclass, optional
        The renderer to be used.
    pad : float
        Padding between the figure edge and the edges of subplots, as a
        fraction of the font-size.
    h_pad, w_pad : float, optional
        Padding (height/width) between edges of adjacent subplots.
        Defaults to *pad*.
    rect : tuple (left, bottom, right, top), default: None
        (left, bottom, right, top) rectangle in normalized figure
        coordinates that the whole subplots area (including labels) will
        fit into. Default (None) is the whole figure.
    """
    if renderer is None:
        renderer = figure._get_renderer()
    kwargs = _tight_layout.get_tight_layout_figure(
        figure, figure.axes,
        _tight_layout.get_subplotspec_list(figure.axes, grid_spec=self),
        renderer, pad=pad, h_pad=h_pad, w_pad=w_pad, rect=rect)
    if kwargs:
        self.update(**kwargs)



# ==================================================
# Line: 476

def __init__(self, nrows, ncols,
             subplot_spec,
             wspace=None, hspace=None,
             height_ratios=None, width_ratios=None):
    """
    Parameters
    ----------
    nrows, ncols : int
        Number of rows and number of columns of the grid.
    subplot_spec : SubplotSpec
        Spec from which the layout parameters are inherited.
    wspace, hspace : float, optional
        See `GridSpec` for more details. If not specified default values
        (from the figure or rcParams) are used.
    height_ratios : array-like of length *nrows*, optional
        See `GridSpecBase` for details.
    width_ratios : array-like of length *ncols*, optional
        See `GridSpecBase` for details.
    """
    self._wspace = wspace
    self._hspace = hspace
    if isinstance(subplot_spec, SubplotSpec):
        self._subplot_spec = subplot_spec
    else:
        raise TypeError(
                        "subplot_spec must be type SubplotSpec, "
                        "usually from GridSpec, or axes.get_subplotspec.")
    self.figure = self._subplot_spec.get_gridspec().figure
    super().__init__(nrows, ncols,
                     width_ratios=width_ratios,
                     height_ratios=height_ratios)


# ==================================================
# Line: 746

def __init__(self, left=None, bottom=None, right=None, top=None,
             wspace=None, hspace=None):
    """
    Defaults are given by :rc:`figure.subplot.[name]`.

    Parameters
    ----------
    left : float, optional
        The position of the left edge of the subplots,
        as a fraction of the figure width.
    right : float, optional
        The position of the right edge of the subplots,
        as a fraction of the figure width.
    bottom : float, optional
        The position of the bottom edge of the subplots,
        as a fraction of the figure height.
    top : float, optional
        The position of the top edge of the subplots,
        as a fraction of the figure height.
    wspace : float, optional
        The width of the padding between subplots,
        as a fraction of the average Axes width.
    hspace : float, optional
        The height of the padding between subplots,
        as a fraction of the average Axes height.
    """
    for key in ["left", "bottom", "right", "top", "wspace", "hspace"]:
        setattr(self, key, mpl.rcParams[f"figure.subplot.{key}"])
    self.update(left, bottom, right, top, wspace, hspace)


# ==================================================
# Line: 776

def update(self, left=None, bottom=None, right=None, top=None,
           wspace=None, hspace=None):
    """
    Update the dimensions of the passed parameters. *None* means unchanged.
    """
    if ((left if left is not None else self.left)
            >= (right if right is not None else self.right)):
        raise ValueError('left cannot be >= right')
    if ((bottom if bottom is not None else self.bottom)
            >= (top if top is not None else self.top)):
        raise ValueError('bottom cannot be >= top')
    if left is not None:
        self.left = left
    if right is not None:
        self.right = right
    if bottom is not None:
        self.bottom = bottom
    if top is not None:
        self.top = top
    if wspace is not None:
        self.wspace = wspace
    if hspace is not None:
        self.hspace = hspace


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/path.py
# Line: 346

def iter_segments(self, transform=None, remove_nans=True, clip=None,
                  snap=False, stroke_width=1.0, simplify=None,
                  curves=True, sketch=None):
    """
    Iterate over all curve segments in the path.

    Each iteration returns a pair ``(vertices, code)``, where ``vertices``
    is a sequence of 1-3 coordinate pairs, and ``code`` is a `Path` code.

    Additionally, this method can provide a number of standard cleanups and
    conversions to the path.

    Parameters
    ----------
    transform : None or :class:`~matplotlib.transforms.Transform`
        If not None, the given affine transformation will be applied to the
        path.
    remove_nans : bool, optional
        Whether to remove all NaNs from the path and skip over them using
        MOVETO commands.
    clip : None or (float, float, float, float), optional
        If not None, must be a four-tuple (x1, y1, x2, y2)
        defining a rectangle in which to clip the path.
    snap : None or bool, optional
        If True, snap all nodes to pixels; if False, don't snap them.
        If None, snap if the path contains only segments
        parallel to the x or y axes, and no more than 1024 of them.
    stroke_width : float, optional
        The width of the stroke being drawn (used for path snapping).
    simplify : None or bool, optional
        Whether to simplify the path by removing vertices
        that do not affect its appearance.  If None, use the
        :attr:`should_simplify` attribute.  See also :rc:`path.simplify`
        and :rc:`path.simplify_threshold`.
    curves : bool, optional
        If True, curve segments will be returned as curve segments.
        If False, all curves will be converted to line segments.
    sketch : None or sequence, optional
        If not None, must be a 3-tuple of the form
        (scale, length, randomness), representing the sketch parameters.
    """
    if not len(self):
        return

    cleaned = self.cleaned(transform=transform,
                           remove_nans=remove_nans, clip=clip,
                           snap=snap, stroke_width=stroke_width,
                           simplify=simplify, curves=curves,
                           sketch=sketch)

    # Cache these object lookups for performance in the loop.
    NUM_VERTICES_FOR_CODE = self.NUM_VERTICES_FOR_CODE
    STOP = self.STOP

    vertices = iter(cleaned.vertices)
    codes = iter(cleaned.codes)
    for curr_vertices, code in zip(vertices, codes):
        if code == STOP:
            break
        extra_vertices = NUM_VERTICES_FOR_CODE[code] - 1
        if extra_vertices:
            for i in range(extra_vertices):
                next(codes)
                curr_vertices = np.append(curr_vertices, next(vertices))
        yield curr_vertices, code


# ==================================================
# Line: 469

def cleaned(self, transform=None, remove_nans=False, clip=None,
            *, simplify=False, curves=False,
            stroke_width=1.0, snap=False, sketch=None):
    """
    Return a new `Path` with vertices and codes cleaned according to the
    parameters.

    See Also
    --------
    Path.iter_segments : for details of the keyword arguments.
    """
    vertices, codes = _path.cleanup_path(
        self, transform, remove_nans, clip, snap, stroke_width, simplify,
        curves, sketch)
    pth = Path._fast_from_codes_and_verts(vertices, codes, self)
    if not simplify:
        pth._should_simplify = False
    return pth


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/colorbar.py
# Line: 225

def __init__(
    self, ax, mappable=None, *,
    alpha=None,
    location=None,
    extend=None,
    extendfrac=None,
    extendrect=False,
    ticks=None,
    format=None,
    values=None,
    boundaries=None,
    spacing='uniform',
    drawedges=False,
    label='',
    cmap=None, norm=None,  # redundant with *mappable*
    orientation=None, ticklocation='auto',  # redundant with *location*

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/mlab.py
# Line: 213

def _spectral_helper(x, y=None, NFFT=None, Fs=None, detrend_func=None,
                     window=None, noverlap=None, pad_to=None,
                     sides=None, scale_by_freq=None, mode=None):
    """
    Private helper implementing the common parts between the psd, csd,
    spectrogram and complex, magnitude, angle, and phase spectrums.
    """
    if y is None:
        # if y is None use x for y
        same_data = True
    else:
        # The checks for if y is x are so that we can use the same function to
        # implement the core of psd(), csd(), and spectrogram() without doing
        # extra calculations.  We return the unaveraged Pxy, freqs, and t.
        same_data = y is x

    if Fs is None:
        Fs = 2
    if noverlap is None:
        noverlap = 0
    if detrend_func is None:
        detrend_func = detrend_none
    if window is None:
        window = window_hanning

    # if NFFT is set to None use the whole signal
    if NFFT is None:
        NFFT = 256

    if noverlap >= NFFT:
        raise ValueError('noverlap must be less than NFFT')

    if mode is None or mode == 'default':
        mode = 'psd'
    _api.check_in_list(
        ['default', 'psd', 'complex', 'magnitude', 'angle', 'phase'],
        mode=mode)

    if not same_data and mode != 'psd':
        raise ValueError("x and y must be equal if mode is not 'psd'")

    # Make sure we're dealing with a numpy array. If y and x were the same
    # object to start with, keep them that way
    x = np.asarray(x)
    if not same_data:
        y = np.asarray(y)

    if sides is None or sides == 'default':
        if np.iscomplexobj(x):
            sides = 'twosided'
        else:
            sides = 'onesided'
    _api.check_in_list(['default', 'onesided', 'twosided'], sides=sides)

    # zero pad x and y up to NFFT if they are shorter than NFFT
    if len(x) < NFFT:
        n = len(x)
        x = np.resize(x, NFFT)
        x[n:] = 0

    if not same_data and len(y) < NFFT:
        n = len(y)
        y = np.resize(y, NFFT)
        y[n:] = 0

    if pad_to is None:
        pad_to = NFFT

    if mode != 'psd':
        scale_by_freq = False
    elif scale_by_freq is None:
        scale_by_freq = True

    # For real x, ignore the negative frequencies unless told otherwise
    if sides == 'twosided':
        numFreqs = pad_to
        if pad_to % 2:
            freqcenter = (pad_to - 1)//2 + 1
        else:
            freqcenter = pad_to//2
        scaling_factor = 1.
    elif sides == 'onesided':
        if pad_to % 2:
            numFreqs = (pad_to + 1)//2
        else:
            numFreqs = pad_to//2 + 1
        scaling_factor = 2.

    if not np.iterable(window):
        window = window(np.ones(NFFT, x.dtype))
    if len(window) != NFFT:
        raise ValueError(
            "The window length must match the data's first dimension")

    result = np.lib.stride_tricks.sliding_window_view(
        x, NFFT, axis=0)[::NFFT - noverlap].T
    result = detrend(result, detrend_func, axis=0)
    result = result * window.reshape((-1, 1))
    result = np.fft.fft(result, n=pad_to, axis=0)[:numFreqs, :]
    freqs = np.fft.fftfreq(pad_to, 1/Fs)[:numFreqs]

    if not same_data:
        # if same_data is False, mode must be 'psd'
        resultY = np.lib.stride_tricks.sliding_window_view(
            y, NFFT, axis=0)[::NFFT - noverlap].T
        resultY = detrend(resultY, detrend_func, axis=0)
        resultY = resultY * window.reshape((-1, 1))
        resultY = np.fft.fft(resultY, n=pad_to, axis=0)[:numFreqs, :]
        result = np.conj(result) * resultY
    elif mode == 'psd':
        result = np.conj(result) * result
    elif mode == 'magnitude':
        result = np.abs(result) / window.sum()
    elif mode == 'angle' or mode == 'phase':
        # we unwrap the phase later to handle the onesided vs. twosided case
        result = np.angle(result)
    elif mode == 'complex':
        result /= window.sum()

    if mode == 'psd':

        # Also include scaling factors for one-sided densities and dividing by
        # the sampling frequency, if desired. Scale everything, except the DC
        # component and the NFFT/2 component:

        # if we have a even number of frequencies, don't scale NFFT/2
        if not NFFT % 2:
            slc = slice(1, -1, None)
        # if we have an odd number, just don't scale DC
        else:
            slc = slice(1, None, None)

        result[slc] *= scaling_factor

        # MATLAB divides by the sampling frequency so that density function
        # has units of dB/Hz and can be integrated by the plotted frequency
        # values. Perform the same scaling here.
        if scale_by_freq:
            result /= Fs
            # Scale the spectrum by the norm of the window to compensate for
            # windowing loss; see Bendat & Piersol Sec 11.5.2.
            result /= (window**2).sum()
        else:
            # In this case, preserve power in the segment, not amplitude
            result /= window.sum()**2

    t = np.arange(NFFT/2, len(x) - NFFT/2 + 1, NFFT - noverlap)/Fs

    if sides == 'twosided':
        # center the frequency range at zero
        freqs = np.roll(freqs, -freqcenter, axis=0)
        result = np.roll(result, -freqcenter, axis=0)
    elif not pad_to % 2:
        # get the last value correctly, it is negative otherwise
        freqs[-1] *= -1

    # we unwrap the phase here to handle the onesided vs. twosided case
    if mode == 'phase':
        result = np.unwrap(result, axis=0)

    return result, freqs, t



# ==================================================
# Line: 462

def psd(x, NFFT=None, Fs=None, detrend=None, window=None,
        noverlap=None, pad_to=None, sides=None, scale_by_freq=None):
    r"""
    Compute the power spectral density.

    The power spectral density :math:`P_{xx}` by Welch's average
    periodogram method.  The vector *x* is divided into *NFFT* length
    segments.  Each segment is detrended by function *detrend* and
    windowed by function *window*.  *noverlap* gives the length of
    the overlap between segments.  The :math:`|\mathrm{fft}(i)|^2`
    of each segment :math:`i` are averaged to compute :math:`P_{xx}`.

    If len(*x*) < *NFFT*, it will be zero padded to *NFFT*.

    Parameters
    ----------
    x : 1-D array or sequence
        Array or sequence containing the data

    %(Spectral)s

    %(PSD)s

    noverlap : int, default: 0 (no overlap)
        The number of points of overlap between segments.

    Returns
    -------
    Pxx : 1-D array
        The values for the power spectrum :math:`P_{xx}` (real valued)

    freqs : 1-D array
        The frequencies corresponding to the elements in *Pxx*

    References
    ----------
    Bendat & Piersol -- Random Data: Analysis and Measurement Procedures, John
    Wiley & Sons (1986)

    See Also
    --------
    specgram
        `specgram` differs in the default overlap; in not returning the mean of
        the segment periodograms; and in returning the times of the segments.

    magnitude_spectrum : returns the magnitude spectrum.

    csd : returns the spectral density between two signals.
    """
    Pxx, freqs = csd(x=x, y=None, NFFT=NFFT, Fs=Fs, detrend=detrend,
                     window=window, noverlap=noverlap, pad_to=pad_to,
                     sides=sides, scale_by_freq=scale_by_freq)
    return Pxx.real, freqs



# ==================================================
# Line: 518

def csd(x, y, NFFT=None, Fs=None, detrend=None, window=None,
        noverlap=None, pad_to=None, sides=None, scale_by_freq=None):
    """
    Compute the cross-spectral density.

    The cross spectral density :math:`P_{xy}` by Welch's average
    periodogram method.  The vectors *x* and *y* are divided into
    *NFFT* length segments.  Each segment is detrended by function
    *detrend* and windowed by function *window*.  *noverlap* gives
    the length of the overlap between segments.  The product of
    the direct FFTs of *x* and *y* are averaged over each segment
    to compute :math:`P_{xy}`, with a scaling to correct for power
    loss due to windowing.

    If len(*x*) < *NFFT* or len(*y*) < *NFFT*, they will be zero
    padded to *NFFT*.

    Parameters
    ----------
    x, y : 1-D arrays or sequences
        Arrays or sequences containing the data

    %(Spectral)s

    %(PSD)s

    noverlap : int, default: 0 (no overlap)
        The number of points of overlap between segments.

    Returns
    -------
    Pxy : 1-D array
        The values for the cross spectrum :math:`P_{xy}` before scaling (real
        valued)

    freqs : 1-D array
        The frequencies corresponding to the elements in *Pxy*

    References
    ----------
    Bendat & Piersol -- Random Data: Analysis and Measurement Procedures, John
    Wiley & Sons (1986)

    See Also
    --------
    psd : equivalent to setting ``y = x``.
    """
    if NFFT is None:
        NFFT = 256
    Pxy, freqs, _ = _spectral_helper(x=x, y=y, NFFT=NFFT, Fs=Fs,
                                     detrend_func=detrend, window=window,
                                     noverlap=noverlap, pad_to=pad_to,
                                     sides=sides, scale_by_freq=scale_by_freq,
                                     mode='psd')

    if Pxy.ndim == 2:
        if Pxy.shape[1] > 1:
            Pxy = Pxy.mean(axis=1)
        else:
            Pxy = Pxy[:, 0]
    return Pxy, freqs



# ==================================================
# Line: 638

def specgram(x, NFFT=None, Fs=None, detrend=None, window=None,
             noverlap=None, pad_to=None, sides=None, scale_by_freq=None,
             mode=None):
    """
    Compute a spectrogram.

    Compute and plot a spectrogram of data in *x*.  Data are split into
    *NFFT* length segments and the spectrum of each section is
    computed.  The windowing function *window* is applied to each
    segment, and the amount of overlap of each segment is
    specified with *noverlap*.

    Parameters
    ----------
    x : array-like
        1-D array or sequence.

    %(Spectral)s

    %(PSD)s

    noverlap : int, default: 128
        The number of points of overlap between blocks.
    mode : str, default: 'psd'
        What sort of spectrum to use:
            'psd'
                Returns the power spectral density.
            'complex'
                Returns the complex-valued frequency spectrum.
            'magnitude'
                Returns the magnitude spectrum.
            'angle'
                Returns the phase spectrum without unwrapping.
            'phase'
                Returns the phase spectrum with unwrapping.

    Returns
    -------
    spectrum : array-like
        2D array, columns are the periodograms of successive segments.

    freqs : array-like
        1-D array, frequencies corresponding to the rows in *spectrum*.

    t : array-like
        1-D array, the times corresponding to midpoints of segments
        (i.e the columns in *spectrum*).

    See Also
    --------
    psd : differs in the overlap and in the return values.
    complex_spectrum : similar, but with complex valued frequencies.
    magnitude_spectrum : similar single segment when *mode* is 'magnitude'.
    angle_spectrum : similar to single segment when *mode* is 'angle'.
    phase_spectrum : similar to single segment when *mode* is 'phase'.

    Notes
    -----
    *detrend* and *scale_by_freq* only apply when *mode* is set to 'psd'.

    """
    if noverlap is None:
        noverlap = 128  # default in _spectral_helper() is noverlap = 0
    if NFFT is None:
        NFFT = 256  # same default as in _spectral_helper()
    if len(x) <= NFFT:
        _api.warn_external("Only one segment is calculated since parameter "
                           f"NFFT (={NFFT}) >= signal length (={len(x)}).")

    spec, freqs, t = _spectral_helper(x=x, y=None, NFFT=NFFT, Fs=Fs,
                                      detrend_func=detrend, window=window,
                                      noverlap=noverlap, pad_to=pad_to,
                                      sides=sides,
                                      scale_by_freq=scale_by_freq,
                                      mode=mode)

    if mode != 'complex':
        spec = spec.real  # Needed since helper implements generically

    return spec, freqs, t



# ==================================================
# Line: 721

def cohere(x, y, NFFT=256, Fs=2, detrend=detrend_none, window=window_hanning,
           noverlap=0, pad_to=None, sides='default', scale_by_freq=None):
    r"""
    The coherence between *x* and *y*.  Coherence is the normalized
    cross spectral density:

    .. math::

        C_{xy} = \frac{|P_{xy}|^2}{P_{xx}P_{yy}}

    Parameters
    ----------
    x, y
        Array or sequence containing the data

    %(Spectral)s

    %(PSD)s

    noverlap : int, default: 0 (no overlap)
        The number of points of overlap between segments.

    Returns
    -------
    Cxy : 1-D array
        The coherence vector.
    freqs : 1-D array
            The frequencies for the elements in *Cxy*.

    See Also
    --------
    :func:`psd`, :func:`csd` :
        For information about the methods used to compute :math:`P_{xy}`,
        :math:`P_{xx}` and :math:`P_{yy}`.
    """
    if len(x) < 2 * NFFT:
        raise ValueError(
            "Coherence is calculated by averaging over *NFFT* length "
            "segments.  Your signal is too short for your choice of *NFFT*.")
    Pxx, f = psd(x, NFFT, Fs, detrend, window, noverlap, pad_to, sides,
                 scale_by_freq)
    Pyy, f = psd(y, NFFT, Fs, detrend, window, noverlap, pad_to, sides,
                 scale_by_freq)
    Pxy, f = csd(x, y, NFFT, Fs, detrend, window, noverlap, pad_to, sides,
                 scale_by_freq)
    Cxy = np.abs(Pxy) ** 2 / (Pxx * Pyy)
    return Cxy, f



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/offsetbox.py
# Line: 389

def __init__(self, pad=0., sep=0., width=None, height=None,
             align="baseline", mode="fixed", children=None):
    """
    Parameters
    ----------
    pad : float, default: 0.0
        The boundary padding in points.

    sep : float, default: 0.0
        The spacing between items in points.

    width, height : float, optional
        Width and height of the container box in pixels, calculated if
        *None*.

    align : {'top', 'bottom', 'left', 'right', 'center', 'baseline'}, \

# ==================================================
# Line: 933

def __init__(self, loc, *,
             pad=0.4, borderpad=0.5,
             child=None, prop=None, frameon=True,
             bbox_to_anchor=None,
             bbox_transform=None,
             **kwargs):
    """
    Parameters
    ----------
    loc : str
        The box location.  Valid locations are
        'upper left', 'upper center', 'upper right',
        'center left', 'center', 'center right',
        'lower left', 'lower center', 'lower right'.
        For backward compatibility, numeric values are accepted as well.
        See the parameter *loc* of `.Legend` for details.
    pad : float, default: 0.4
        Padding around the child as fraction of the fontsize.
    borderpad : float, default: 0.5
        Padding between the offsetbox frame and the *bbox_to_anchor*.
    child : `.OffsetBox`
        The box that will be anchored.
    prop : `.FontProperties`
        This is only used as a reference for paddings. If not given,
        :rc:`legend.fontsize` is used.
    frameon : bool
        Whether to draw a frame around the box.
    bbox_to_anchor : `.BboxBase`, 2-tuple, or 4-tuple of floats
        Box that is used to position the legend in conjunction with *loc*.
    bbox_transform : None or :class:`matplotlib.transforms.Transform`
        The transform for the bounding box (*bbox_to_anchor*).
    **kwargs
        All other parameters are passed on to `.OffsetBox`.

    Notes
    -----
    See `.Legend` for a detailed description of the anchoring mechanism.
    """
    super().__init__(**kwargs)

    self.set_bbox_to_anchor(bbox_to_anchor, bbox_transform)
    self.set_child(child)

    if isinstance(loc, str):
        loc = _api.check_getitem(self.codes, loc=loc)

    self.loc = loc
    self.borderpad = borderpad
    self.pad = pad

    if prop is None:
        self.prop = FontProperties(size=mpl.rcParams["legend.fontsize"])
    else:
        self.prop = FontProperties._from_any(prop)
        if isinstance(prop, dict) and "size" not in prop:
            self.prop.set_size(mpl.rcParams["legend.fontsize"])

    self.patch = FancyBboxPatch(
        xy=(0.0, 0.0), width=1., height=1.,
        facecolor='w', edgecolor='k',
        mutation_scale=self.prop.get_size_in_points(),
        snap=True,
        visible=frameon,
        boxstyle="square,pad=0",
    )


# ==================================================
# Line: 1146

def __init__(self, arr, *,
             zoom=1,
             cmap=None,
             norm=None,
             interpolation=None,
             origin=None,
             filternorm=True,
             filterrad=4.0,
             resample=False,
             dpi_cor=True,
             **kwargs
             ):

    super().__init__()
    self._dpi_cor = dpi_cor

    self.image = BboxImage(bbox=self.get_window_extent,
                           cmap=cmap,
                           norm=norm,
                           interpolation=interpolation,
                           origin=origin,
                           filternorm=filternorm,
                           filterrad=filterrad,
                           resample=resample,
                           **kwargs
                           )

    self._children = [self.image]

    self.set_zoom(zoom)
    self.set_data(arr)


# ==================================================
# Line: 1230

def __init__(self, offsetbox, xy, xybox=None, xycoords='data', boxcoords=None, *,
             frameon=True, pad=0.4,  # FancyBboxPatch boxstyle.
             annotation_clip=None,
             box_alignment=(0.5, 0.5),
             bboxprops=None,
             arrowprops=None,
             fontsize=None,
             **kwargs):
    """
    Parameters
    ----------
    offsetbox : `OffsetBox`

    xy : (float, float)
        The point *(x, y)* to annotate. The coordinate system is determined
        by *xycoords*.

    xybox : (float, float), default: *xy*
        The position *(x, y)* to place the text at. The coordinate system
        is determined by *boxcoords*.

    xycoords : single or two-tuple of str or `.Artist` or `.Transform` or \

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backend_bases.py
# Line: 177

def draw_markers(self, gc, marker_path, marker_trans, path,
                 trans, rgbFace=None):
    """
    Draw a marker at each of *path*'s vertices (excluding control points).

    The base (fallback) implementation makes multiple calls to `draw_path`.
    Backends may want to override this method in order to draw the marker
    only once and reuse it multiple times.

    Parameters
    ----------
    gc : `.GraphicsContextBase`
        The graphics context.
    marker_path : `~matplotlib.path.Path`
        The path for the marker.
    marker_trans : `~matplotlib.transforms.Transform`
        An affine transform applied to the marker.
    path : `~matplotlib.path.Path`
        The locations to draw the markers.
    trans : `~matplotlib.transforms.Transform`
        An affine transform applied to the path.
    rgbFace : :mpltype:`color`, optional
    """
    for vertices, codes in path.iter_segments(trans, simplify=False):
        if len(vertices):
            x, y = vertices[-2:]
            self.draw_path(gc, marker_path,
                           marker_trans +
                           transforms.Affine2D().translate(x, y),
                           rgbFace)


# ==================================================
# Line: 208

def draw_path_collection(self, gc, master_transform, paths, all_transforms,
                         offsets, offset_trans, facecolors, edgecolors,
                         linewidths, linestyles, antialiaseds, urls,
                         offset_position, *, hatchcolors=None):
    """
    Draw a collection of *paths*.

    Each path is first transformed by the corresponding entry
    in *all_transforms* (a list of (3, 3) matrices) and then by
    *master_transform*.  They are then translated by the corresponding
    entry in *offsets*, which has been first transformed by *offset_trans*.

    *facecolors*, *edgecolors*, *linewidths*, *linestyles*, *antialiased*
    and *hatchcolors* are lists that set the corresponding properties.

    .. versionadded:: 3.11
        Allow *hatchcolors* to be specified.

    *offset_position* is unused now, but the argument is kept for
    backwards compatibility.

    The base (fallback) implementation makes multiple calls to `draw_path`.
    Backends may want to override this in order to render each set of
    path data only once, and then reference that path multiple times with
    the different offsets, colors, styles etc.  The generator methods
    `!_iter_collection_raw_paths` and `!_iter_collection` are provided to
    help with (and standardize) the implementation across backends.  It
    is highly recommended to use those generators, so that changes to the
    behavior of `draw_path_collection` can be made globally.
    """
    path_ids = self._iter_collection_raw_paths(master_transform,
                                               paths, all_transforms)

    if hatchcolors is None:
        hatchcolors = []

    for xo, yo, path_id, gc0, rgbFace in self._iter_collection(
            gc, list(path_ids), offsets, offset_trans,
            facecolors, edgecolors, linewidths, linestyles,
            antialiaseds, urls, offset_position, hatchcolors=hatchcolors):
        path, transform = path_id
        # Only apply another translation if we have an offset, else we
        # reuse the initial transform.
        if xo != 0 or yo != 0:
            # The transformation can be used by multiple paths. Since
            # translate is a inplace operation, we need to copy the
            # transformation by .frozen() before applying the translation.
            transform = transform.frozen()
            transform.translate(xo, yo)
        self.draw_path(gc0, path, transform, rgbFace)


# ==================================================
# Line: 259

def draw_quad_mesh(self, gc, master_transform, meshWidth, meshHeight,
                   coordinates, offsets, offsetTrans, facecolors,
                   antialiased, edgecolors):
    """
    Draw a quadmesh.

    The base (fallback) implementation converts the quadmesh to paths and
    then calls `draw_path_collection`.
    """

    from matplotlib.collections import QuadMesh
    paths = QuadMesh._convert_mesh_to_paths(coordinates)

    if edgecolors is None:
        edgecolors = facecolors
    linewidths = np.array([gc.get_linewidth()], float)

    return self.draw_path_collection(
        gc, master_transform, paths, [], offsets, offsetTrans, facecolors,
        edgecolors, linewidths, [], [antialiased], [None], 'screen')


# ==================================================
# Line: 344

def _iter_collection(self, gc, path_ids, offsets, offset_trans, facecolors,
                     edgecolors, linewidths, linestyles,
                     antialiaseds, urls, offset_position, *, hatchcolors):
    """
    Helper method (along with `_iter_collection_raw_paths`) to implement
    `draw_path_collection` in a memory-efficient manner.

    This method yields all of the path, offset and graphics context
    combinations to draw the path collection.  The caller should already
    have looped over the results of `_iter_collection_raw_paths` to draw
    this collection.

    The arguments should be the same as that passed into
    `draw_path_collection`, with the exception of *path_ids*, which is a
    list of arbitrary objects that the backend will use to reference one of
    the paths created in the `_iter_collection_raw_paths` stage.

    Each yielded result is of the form::

       xo, yo, path_id, gc, rgbFace

    where *xo*, *yo* is an offset; *path_id* is one of the elements of
    *path_ids*; *gc* is a graphics context and *rgbFace* is a color to
    use for filling the path.
    """
    Npaths = len(path_ids)
    Noffsets = len(offsets)
    N = max(Npaths, Noffsets)
    Nfacecolors = len(facecolors)
    Nedgecolors = len(edgecolors)
    Nhatchcolors = len(hatchcolors)
    Nlinewidths = len(linewidths)
    Nlinestyles = len(linestyles)
    Nurls = len(urls)

    if (Nfacecolors == 0 and Nedgecolors == 0 and Nhatchcolors == 0) or Npaths == 0:
        return

    gc0 = self.new_gc()
    gc0.copy_properties(gc)

    def cycle_or_default(seq, default=None):
        # Cycle over *seq* if it is not empty; else always yield *default*.
        return (itertools.cycle(seq) if len(seq)
                else itertools.repeat(default))

    pathids = cycle_or_default(path_ids)
    toffsets = cycle_or_default(offset_trans.transform(offsets), (0, 0))
    fcs = cycle_or_default(facecolors)
    ecs = cycle_or_default(edgecolors)
    hcs = cycle_or_default(hatchcolors)
    lws = cycle_or_default(linewidths)
    lss = cycle_or_default(linestyles)
    aas = cycle_or_default(antialiaseds)
    urls = cycle_or_default(urls)

    if Nedgecolors == 0:
        gc0.set_linewidth(0.0)

    for pathid, (xo, yo), fc, ec, hc, lw, ls, aa, url in itertools.islice(
            zip(pathids, toffsets, fcs, ecs, hcs, lws, lss, aas, urls), N):
        if not (np.isfinite(xo) and np.isfinite(yo)):
            continue
        if Nedgecolors:
            if Nlinewidths:
                gc0.set_linewidth(lw)
            if Nlinestyles:
                gc0.set_dashes(*ls)
            if len(ec) == 4 and ec[3] == 0.0:
                gc0.set_linewidth(0)
            else:
                gc0.set_foreground(ec)
        if Nhatchcolors:
            gc0.set_hatch_color(hc)
        if fc is not None and len(fc) == 4 and fc[3] == 0:
            fc = None
        gc0.set_antialiased(aa)
        if Nurls:
            gc0.set_url(url)
        yield xo, yo, pathid, gc0, fc
    gc0.restore()


# ==================================================
# Line: 484

def draw_tex(self, gc, x, y, s, prop, angle, *, mtext=None):
    """
    Draw a TeX instance.

    Parameters
    ----------
    gc : `.GraphicsContextBase`
        The graphics context.
    x : float
        The x location of the text in display coords.
    y : float
        The y location of the text baseline in display coords.
    s : str
        The TeX text string.
    prop : `~matplotlib.font_manager.FontProperties`
        The font properties.
    angle : float
        The rotation angle in degrees anti-clockwise.
    mtext : `~matplotlib.text.Text`
        The original text object to be rendered.
    """
    self._draw_text_as_path(gc, x, y, s, prop, angle, ismath="TeX")


# ==================================================
# Line: 507

def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):
    """
    Draw a text instance.

    Parameters
    ----------
    gc : `.GraphicsContextBase`
        The graphics context.
    x : float
        The x location of the text in display coords.
    y : float
        The y location of the text baseline in display coords.
    s : str
        The text string.
    prop : `~matplotlib.font_manager.FontProperties`
        The font properties.
    angle : float
        The rotation angle in degrees anti-clockwise.
    ismath : bool or "TeX"
        If True, use mathtext parser.
    mtext : `~matplotlib.text.Text`
        The original text object to be rendered.

    Notes
    -----
    **Notes for backend implementers:**

    `.RendererBase.draw_text` also supports passing "TeX" to the *ismath*
    parameter to use TeX rendering, but this is not required for actual
    rendering backends, and indeed many builtin backends do not support
    this.  Rather, TeX rendering is provided by `~.RendererBase.draw_tex`.
    """
    self._draw_text_as_path(gc, x, y, s, prop, angle, ismath)


# ==================================================
# Line: 541

def _draw_text_as_path(self, gc, x, y, s, prop, angle, ismath):
    """
    Draw the text by converting them to paths using `.TextToPath`.

    This private helper supports the same parameters as
    `~.RendererBase.draw_text`; setting *ismath* to "TeX" triggers TeX
    rendering.
    """
    text2path = self._text2path
    fontsize = self.points_to_pixels(prop.get_size_in_points())
    verts, codes = text2path.get_text_path(prop, s, ismath=ismath)
    path = Path(verts, codes)
    if self.flipy():
        width, height = self.get_canvas_width_height()
        transform = (Affine2D()
                     .scale(fontsize / text2path.FONT_SCALE)
                     .rotate_deg(angle)
                     .translate(x, height - y))
    else:
        transform = (Affine2D()
                     .scale(fontsize / text2path.FONT_SCALE)
                     .rotate_deg(angle)
                     .translate(x, y))
    color = gc.get_rgb()
    gc.set_linewidth(0.0)
    self.draw_path(gc, path, transform, rgbFace=color)


# ==================================================
# Line: 1269

def __init__(self, name, canvas, x, y, guiEvent=None, *, modifiers=None):
    super().__init__(name, canvas, guiEvent=guiEvent)
    # x position - pixels from left of canvas
    self.x = int(x) if x is not None else x
    # y position - pixels from right of canvas
    self.y = int(y) if y is not None else y
    self.inaxes = None  # the Axes instance the mouse is over
    self.xdata = None   # x coord of mouse in data coords
    self.ydata = None   # y coord of mouse in data coords
    self.modifiers = frozenset(modifiers if modifiers is not None else [])

    if x is None or y is None:
        # cannot check if event was in Axes if no (x, y) info
        return

    self._set_inaxes(self.canvas.inaxes((x, y))
                     if self.canvas.mouse_grabber is None else
                     self.canvas.mouse_grabber,
                     (x, y))


# ==================================================
# Line: 1387

def __init__(self, name, canvas, x, y, button=None, key=None,
             step=0, dblclick=False, guiEvent=None, *,
             buttons=None, modifiers=None):
    super().__init__(
        name, canvas, x, y, guiEvent=guiEvent, modifiers=modifiers)
    if button in MouseButton.__members__.values():
        button = MouseButton(button)
    if name == "scroll_event" and button is None:
        if step > 0:
            button = "up"
        elif step < 0:
            button = "down"
    self.button = button
    if name == "motion_notify_event":
        self.buttons = frozenset(buttons if buttons is not None else [])
    else:
        # We don't support 'buttons' for button_press/release_event because
        # toolkits are inconsistent as to whether they report the state
        # before or after the event.
        if buttons:
            raise ValueError(
                "'buttons' is only supported for 'motion_notify_event'")
        self.buttons = None
    self.key = key
    self.step = step
    self.dblclick = dblclick


# ==================================================
# Line: 1502

def __init__(self, name, canvas, key, x=0, y=0, guiEvent=None):
    super().__init__(name, canvas, x, y, guiEvent=guiEvent)
    self.key = key



# ==================================================
# Line: 2052

def print_figure(
        self, filename, dpi=None, facecolor=None, edgecolor=None,
        orientation='portrait', format=None, *,
        bbox_inches=None, pad_inches=None, bbox_extra_artists=None,
        backend=None, **kwargs):
    """
    Render the figure to hardcopy. Set the figure patch face and edge
    colors.  This is useful because some of the GUIs have a gray figure
    face color background and you'll probably want to override this on
    hardcopy.

    Parameters
    ----------
    filename : str or path-like or file-like
        The file where the figure is saved.

    dpi : float, default: :rc:`savefig.dpi`
        The dots per inch to save the figure in.

    facecolor : :mpltype:`color` or 'auto', default: :rc:`savefig.facecolor`
        The facecolor of the figure.  If 'auto', use the current figure
        facecolor.

    edgecolor : :mpltype:`color` or 'auto', default: :rc:`savefig.edgecolor`
        The edgecolor of the figure.  If 'auto', use the current figure
        edgecolor.

    orientation : {'landscape', 'portrait'}, default: 'portrait'
        Only currently applies to PostScript printing.

    format : str, optional
        Force a specific file format. If not given, the format is inferred
        from the *filename* extension, and if that fails from
        :rc:`savefig.format`.

    bbox_inches : 'tight' or `.Bbox`, default: :rc:`savefig.bbox`
        Bounding box in inches: only the given portion of the figure is
        saved.  If 'tight', try to figure out the tight bbox of the figure.

    pad_inches : float or 'layout', default: :rc:`savefig.pad_inches`
        Amount of padding in inches around the figure when bbox_inches is
        'tight'. If 'layout' use the padding from the constrained or
        compressed layout engine; ignored if one of those engines is not in
        use.

    bbox_extra_artists : list of `~matplotlib.artist.Artist`, optional
        A list of extra artists that will be considered when the
        tight bbox is calculated.

    backend : str, optional
        Use a non-default backend to render the file, e.g. to render a
        png file with the "cairo" backend rather than the default "agg",
        or a pdf file with the "pgf" backend rather than the default
        "pdf".  Note that the default backend is normally sufficient.  See
        :ref:`the-builtin-backends` for a list of valid backends for each
        file format.  Custom backends can be referenced as "module://...".
    """
    if format is None:
        # get format from filename, or from backend's default filetype
        if isinstance(filename, os.PathLike):
            filename = os.fspath(filename)
        if isinstance(filename, str):
            format = os.path.splitext(filename)[1][1:]
        if format is None or format == '':
            format = self.get_default_filetype()
            if isinstance(filename, str):
                filename = filename.rstrip('.') + '.' + format
    format = format.lower()

    dpi = mpl._val_or_rc(dpi, 'savefig.dpi')
    if dpi == 'figure':
        dpi = getattr(self.figure, '_original_dpi', self.figure.dpi)

    # Remove the figure manager, if any, to avoid resizing the GUI widget.
    with (cbook._setattr_cm(self, manager=None),
          self._switch_canvas_and_return_print_method(format, backend)
             as print_method,
          cbook._setattr_cm(self.figure, dpi=dpi),
          cbook._setattr_cm(self.figure.canvas, _device_pixel_ratio=1),
          cbook._setattr_cm(self.figure.canvas, _is_saving=True),
          ExitStack() as stack):

        for prop, color in [("facecolor", facecolor), ("edgecolor", edgecolor)]:
            color = mpl._val_or_rc(color, f"savefig.{prop}")
            if not cbook._str_equal(color, "auto"):
                stack.enter_context(self.figure._cm_set(**{prop: color}))

        bbox_inches = mpl._val_or_rc(bbox_inches, 'savefig.bbox')

        layout_engine = self.figure.get_layout_engine()
        if layout_engine is not None or bbox_inches == "tight":
            # we need to trigger a draw before printing to make sure
            # CL works.  "tight" also needs a draw to get the right
            # locations:
            renderer = _get_renderer(
                self.figure,
                functools.partial(
                    print_method, orientation=orientation)
            )
            # we do this instead of `self.figure.draw_without_rendering`
            # so that we can inject the orientation
            with getattr(renderer, "_draw_disabled", nullcontext)():
                self.figure.draw(renderer)
        else:
            renderer = None

        if bbox_inches:
            if bbox_inches == "tight":
                bbox_inches = self.figure.get_tightbbox(
                    renderer, bbox_extra_artists=bbox_extra_artists)
                if (isinstance(layout_engine, ConstrainedLayoutEngine) and
                        pad_inches == "layout"):
                    h_pad = layout_engine.get()["h_pad"]
                    w_pad = layout_engine.get()["w_pad"]
                else:
                    if pad_inches in [None, "layout"]:
                        pad_inches = rcParams['savefig.pad_inches']
                    h_pad = w_pad = pad_inches
                bbox_inches = bbox_inches.padded(w_pad, h_pad)

            # call adjust_bbox to save only the given area
            restore_bbox = _tight_bbox.adjust_bbox(
                self.figure, bbox_inches, renderer, self.figure.canvas.fixed_dpi)

            _bbox_inches_restore = (bbox_inches, restore_bbox)
        else:
            _bbox_inches_restore = None

        # we have already done layout above, so turn it off:
        stack.enter_context(self.figure._cm_set(layout_engine='none'))
        try:
            # _get_renderer may change the figure dpi (as vector formats
            # force the figure dpi to 72), so we need to set it again here.
            with cbook._setattr_cm(self.figure, dpi=dpi):
                result = print_method(
                    filename,
                    facecolor=facecolor,
                    edgecolor=edgecolor,
                    orientation=orientation,
                    bbox_inches_restore=_bbox_inches_restore,
                    **kwargs)
        finally:
            if bbox_inches and restore_bbox:
                restore_bbox()

        return result


# ==================================================
# Line: 3397

def add_toolitem(self, name, group, position, image, description, toggle):
    """
    A hook to add a toolitem to the container.

    This hook must be implemented in each backend and contains the
    backend-specific code to add an element to the toolbar.

    .. warning::
        This is part of the backend implementation and should
        not be called by end-users.  They should instead call
        `.ToolContainerBase.add_tool`.

    The callback associated with the button click event
    must be *exactly* ``self.trigger_tool(name)``.

    Parameters
    ----------
    name : str
        Name of the tool to add, this gets used as the tool's ID and as the
        default label of the buttons.
    group : str
        Name of the group that this tool belongs to.
    position : int
        Position of the tool within its group, if -1 it goes at the end.
    image : str
        Filename of the image for the button or `None`.
    description : str
        Description of the tool, used for the tooltips.
    toggle : bool
        * `True` : The button is a toggle (change the pressed/unpressed
          state between consecutive clicks).
        * `False` : The button is a normal button (returns to unpressed
          state after release).
    """
    raise NotImplementedError


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/tri/_tripcolor.py
# Line: 9

def tripcolor(ax, *args, alpha=1.0, norm=None, cmap=None, vmin=None,
              vmax=None, shading='flat', facecolors=None, **kwargs):
    """
    Create a pseudocolor plot of an unstructured triangular grid.

    Call signatures::

      tripcolor(triangulation, c, *, ...)
      tripcolor(x, y, c, *, [triangles=triangles], [mask=mask], ...)

    The triangular grid can be specified either by passing a `.Triangulation`
    object as the first parameter, or by passing the points *x*, *y* and
    optionally the *triangles* and a *mask*. See `.Triangulation` for an
    explanation of these parameters.

    It is possible to pass the triangles positionally, i.e.
    ``tripcolor(x, y, triangles, c, ...)``. However, this is discouraged.
    For more clarity, pass *triangles* via keyword argument.

    If neither of *triangulation* or *triangles* are given, the triangulation
    is calculated on the fly. In this case, it does not make sense to provide
    colors at the triangle faces via *c* or *facecolors* because there are
    multiple possible triangulations for a group of points and you don't know
    which triangles will be constructed.

    Parameters
    ----------
    triangulation : `.Triangulation`
        An already created triangular grid.
    x, y, triangles, mask
        Parameters defining the triangular grid. See `.Triangulation`.
        This is mutually exclusive with specifying *triangulation*.
    c : array-like
        The color values, either for the points or for the triangles. Which one
        is automatically inferred from the length of *c*, i.e. does it match
        the number of points or the number of triangles. If there are the same
        number of points and triangles in the triangulation it is assumed that
        color values are defined at points; to force the use of color values at
        triangles use the keyword argument ``facecolors=c`` instead of just
        ``c``.
        This parameter is position-only.
    facecolors : array-like, optional
        Can be used alternatively to *c* to specify colors at the triangle
        faces. This parameter takes precedence over *c*.
    shading : {'flat', 'gouraud'}, default: 'flat'
        If  'flat' and the color values *c* are defined at points, the color
        values used for each triangle are from the mean c of the triangle's
        three points. If *shading* is 'gouraud' then color values must be
        defined at points.
    %(cmap_doc)s

    %(norm_doc)s

    %(vmin_vmax_doc)s

    %(colorizer_doc)s

    Returns
    -------
    `~matplotlib.collections.PolyCollection` or `~matplotlib.collections.TriMesh`
        The result depends on *shading*: For ``shading='flat'`` the result is a
        `.PolyCollection`, for ``shading='gouraud'`` the result is a `.TriMesh`.

    Other Parameters
    ----------------
    **kwargs : `~matplotlib.collections.Collection` properties

        %(Collection:kwdoc)s
    """
    _api.check_in_list(['flat', 'gouraud'], shading=shading)

    tri, args, kwargs = Triangulation.get_from_args_and_kwargs(*args, **kwargs)

    # Parse the color to be in one of (the other variable will be None):
    # - facecolors: if specified at the triangle faces
    # - point_colors: if specified at the points
    if facecolors is not None:
        if args:
            _api.warn_external(
                "Positional parameter c has no effect when the keyword "
                "facecolors is given")
        point_colors = None
        if len(facecolors) != len(tri.triangles):
            raise ValueError("The length of facecolors must match the number "
                             "of triangles")
    else:
        # Color from positional parameter c
        if not args:
            raise TypeError(
                "tripcolor() missing 1 required positional argument: 'c'; or "
                "1 required keyword-only argument: 'facecolors'")
        elif len(args) > 1:
            raise TypeError(f"Unexpected positional parameters: {args[1:]!r}")
        c = np.asarray(args[0])
        if len(c) == len(tri.x):
            # having this before the len(tri.triangles) comparison gives
            # precedence to nodes if there are as many nodes as triangles
            point_colors = c
            facecolors = None
        elif len(c) == len(tri.triangles):
            point_colors = None
            facecolors = c
        else:
            raise ValueError('The length of c must match either the number '
                             'of points or the number of triangles')

    # Handling of linewidths, shading, edgecolors and antialiased as
    # in Axes.pcolor
    linewidths = (0.25,)
    if 'linewidth' in kwargs:
        kwargs['linewidths'] = kwargs.pop('linewidth')
    kwargs.setdefault('linewidths', linewidths)

    edgecolors = 'none'
    if 'edgecolor' in kwargs:
        kwargs['edgecolors'] = kwargs.pop('edgecolor')
    ec = kwargs.setdefault('edgecolors', edgecolors)

    if 'antialiased' in kwargs:
        kwargs['antialiaseds'] = kwargs.pop('antialiased')
    if 'antialiaseds' not in kwargs and ec.lower() == "none":
        kwargs['antialiaseds'] = False

    if shading == 'gouraud':
        if facecolors is not None:
            raise ValueError(
                "shading='gouraud' can only be used when the colors "
                "are specified at the points, not at the faces.")
        collection = TriMesh(tri, alpha=alpha, array=point_colors,
                             cmap=cmap, norm=norm, **kwargs)
    else:  # 'flat'
        # Vertices of triangles.
        maskedTris = tri.get_masked_triangles()
        verts = np.stack((tri.x[maskedTris], tri.y[maskedTris]), axis=-1)

        # Color values.
        if facecolors is None:
            # One color per triangle, the mean of the 3 vertex color values.
            colors = point_colors[maskedTris].mean(axis=1)
        elif tri.mask is not None:
            # Remove color values of masked triangles.
            colors = facecolors[~tri.mask]
        else:
            colors = facecolors
        collection = PolyCollection(verts, alpha=alpha, array=colors,
                                    cmap=cmap, norm=norm, **kwargs)

    collection._scale_norm(norm, vmin, vmax)
    ax.grid(False)

    minx = tri.x.min()
    maxx = tri.x.max()
    miny = tri.y.min()
    maxy = tri.y.max()
    corners = (minx, miny), (maxx, maxy)
    ax.update_datalim(corners)
    ax.autoscale_view()
    ax.add_collection(collection)
    return collection

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_layoutgrid.py
# Line: 36

def __init__(self, parent=None, parent_pos=(0, 0),
             parent_inner=False, name='', ncols=1, nrows=1,
             h_pad=None, w_pad=None, width_ratios=None,
             height_ratios=None):
    Variable = kiwi.Variable
    self.parent_pos = parent_pos
    self.parent_inner = parent_inner
    self.name = name + seq_id()
    if isinstance(parent, LayoutGrid):
        self.name = f'{parent.name}.{self.name}'
    self.nrows = nrows
    self.ncols = ncols
    self.height_ratios = np.atleast_1d(height_ratios)
    if height_ratios is None:
        self.height_ratios = np.ones(nrows)
    self.width_ratios = np.atleast_1d(width_ratios)
    if width_ratios is None:
        self.width_ratios = np.ones(ncols)

    sn = self.name + '_'
    if not isinstance(parent, LayoutGrid):
        # parent can be a rect if not a LayoutGrid
        # allows specifying a rectangle to contain the layout.
        self.solver = kiwi.Solver()
    else:
        parent.add_child(self, *parent_pos)
        self.solver = parent.solver
    # keep track of artist associated w/ this layout.  Can be none
    self.artists = np.empty((nrows, ncols), dtype=object)
    self.children = np.empty((nrows, ncols), dtype=object)

    self.margins = {}
    self.margin_vals = {}
    # all the boxes in each column share the same left/right margins:
    for todo in ['left', 'right', 'leftcb', 'rightcb']:
        # track the value so we can change only if a margin is larger
        # than the current value
        self.margin_vals[todo] = np.zeros(ncols)

    sol = self.solver

    self.lefts = [Variable(f'{sn}lefts[{i}]') for i in range(ncols)]
    self.rights = [Variable(f'{sn}rights[{i}]') for i in range(ncols)]
    for todo in ['left', 'right', 'leftcb', 'rightcb']:
        self.margins[todo] = [Variable(f'{sn}margins[{todo}][{i}]')
                              for i in range(ncols)]
        for i in range(ncols):
            sol.addEditVariable(self.margins[todo][i], 'strong')

    for todo in ['bottom', 'top', 'bottomcb', 'topcb']:
        self.margins[todo] = np.empty((nrows), dtype=object)
        self.margin_vals[todo] = np.zeros(nrows)

    self.bottoms = [Variable(f'{sn}bottoms[{i}]') for i in range(nrows)]
    self.tops = [Variable(f'{sn}tops[{i}]') for i in range(nrows)]
    for todo in ['bottom', 'top', 'bottomcb', 'topcb']:
        self.margins[todo] = [Variable(f'{sn}margins[{todo}][{i}]')
                              for i in range(nrows)]
        for i in range(nrows):
            sol.addEditVariable(self.margins[todo][i], 'strong')

    # set these margins to zero by default. They will be edited as
    # children are filled.
    self.reset_margins()
    self.add_constraints(parent)

    self.h_pad = h_pad
    self.w_pad = w_pad


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/streamplot.py
# Line: 18

def streamplot(axes, x, y, u, v, density=1, linewidth=None, color=None,
               cmap=None, norm=None, arrowsize=1, arrowstyle='-|>',
               minlength=0.1, transform=None, zorder=None, start_points=None,
               maxlength=4.0, integration_direction='both',
               broken_streamlines=True, *, integration_max_step_scale=1.0,
               integration_max_error_scale=1.0, num_arrows=1):
    """
    Draw streamlines of a vector flow.

    Parameters
    ----------
    x, y : 1D/2D arrays
        Evenly spaced strictly increasing arrays to make a grid.  If 2D, all
        rows of *x* must be equal and all columns of *y* must be equal; i.e.,
        they must be as if generated by ``np.meshgrid(x_1d, y_1d)``.
    u, v : 2D arrays
        *x* and *y*-velocities. The number of rows and columns must match
        the length of *y* and *x*, respectively.
    density : float or (float, float)
        Controls the closeness of streamlines. When ``density = 1``, the domain
        is divided into a 30x30 grid. *density* linearly scales this grid.
        Each cell in the grid can have, at most, one traversing streamline.
        For different densities in each direction, use a tuple
        (density_x, density_y).
    linewidth : float or 2D array
        The width of the streamlines. With a 2D array the line width can be
        varied across the grid. The array must have the same shape as *u*
        and *v*.
    color : :mpltype:`color` or 2D array
        The streamline color. If given an array, its values are converted to
        colors using *cmap* and *norm*.  The array must have the same shape
        as *u* and *v*.
    cmap, norm
        Data normalization and colormapping parameters for *color*; only used
        if *color* is an array of floats. See `~.Axes.imshow` for a detailed
        description.
    arrowsize : float
        Scaling factor for the arrow size.
    arrowstyle : str
        Arrow style specification.
        See `~matplotlib.patches.FancyArrowPatch`.
    minlength : float
        Minimum length of streamline in axes coordinates.
    start_points : (N, 2) array
        Coordinates of starting points for the streamlines in data coordinates
        (the same coordinates as the *x* and *y* arrays).
    zorder : float
        The zorder of the streamlines and arrows.
        Artists with lower zorder values are drawn first.
    maxlength : float
        Maximum length of streamline in axes coordinates.
    integration_direction : {'forward', 'backward', 'both'}, default: 'both'
        Integrate the streamline in forward, backward or both directions.
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER
    broken_streamlines : boolean, default: True
        If False, forces streamlines to continue until they
        leave the plot domain.  If True, they may be terminated if they
        come too close to another streamline.
    integration_max_step_scale : float, default: 1.0
        Multiplier on the maximum allowable step in the streamline integration routine.
        A value between zero and one results in a max integration step smaller than
        the default max step, resulting in more accurate streamlines at the cost
        of greater computation time; a value greater than one does the converse. Must be
        greater than zero.

        .. versionadded:: 3.11

    integration_max_error_scale : float, default: 1.0
        Multiplier on the maximum allowable error in the streamline integration routine.
        A value between zero and one results in a tighter max integration error than
        the default max error, resulting in more accurate streamlines at the cost
        of greater computation time; a value greater than one does the converse. Must be
        greater than zero.

        .. versionadded:: 3.11

    num_arrows : int
        Number of arrows per streamline. The arrows are spaced equally along the steps
        each streamline takes. Note that this can be different to being spaced equally
        along the distance of the streamline.


    Returns
    -------
    StreamplotSet
        Container object with attributes

        - ``lines``: `.LineCollection` of streamlines

        - ``arrows``: `.PatchCollection` containing `.FancyArrowPatch`
          objects representing the arrows half-way along streamlines.

        This container will probably change in the future to allow changes
        to the colormap, alpha, etc. for both lines and arrows, but these
        changes should be backward compatible.
    """
    grid = Grid(x, y)
    mask = StreamMask(density)
    dmap = DomainMap(grid, mask)

    if integration_max_step_scale <= 0.0:
        raise ValueError(
            "The value of integration_max_step_scale must be > 0, " +
            f"got {integration_max_step_scale}"
        )

    if integration_max_error_scale <= 0.0:
        raise ValueError(
            "The value of integration_max_error_scale must be > 0, " +
            f"got {integration_max_error_scale}"
        )

    if num_arrows < 0:
        raise ValueError(f"The value of num_arrows must be >= 0, got {num_arrows=}")

    if zorder is None:
        zorder = mlines.Line2D.zorder

    # default to data coordinates
    if transform is None:
        transform = axes.transData

    if color is None:
        color = axes._get_lines.get_next_color()

    linewidth = mpl._val_or_rc(linewidth, 'lines.linewidth')

    line_kw = {}
    arrow_kw = dict(arrowstyle=arrowstyle, mutation_scale=10 * arrowsize)

    _api.check_in_list(['both', 'forward', 'backward'],
                       integration_direction=integration_direction)

    if integration_direction == 'both':
        maxlength /= 2.

    use_multicolor_lines = isinstance(color, np.ndarray)
    if use_multicolor_lines:
        if color.shape != grid.shape:
            raise ValueError("If 'color' is given, it must match the shape of "
                             "the (x, y) grid")
        line_colors = [[]]  # Empty entry allows concatenation of zero arrays.
        color = np.ma.masked_invalid(color)
    else:
        line_kw['color'] = color
        arrow_kw['color'] = color

    if isinstance(linewidth, np.ndarray):
        if linewidth.shape != grid.shape:
            raise ValueError("If 'linewidth' is given, it must match the "
                             "shape of the (x, y) grid")
        line_kw['linewidth'] = []
    else:
        line_kw['linewidth'] = linewidth
        arrow_kw['linewidth'] = linewidth

    line_kw['zorder'] = zorder
    arrow_kw['zorder'] = zorder

    # Sanity checks.
    if u.shape != grid.shape or v.shape != grid.shape:
        raise ValueError("'u' and 'v' must match the shape of the (x, y) grid")

    u = np.ma.masked_invalid(u)
    v = np.ma.masked_invalid(v)

    integrate = _get_integrator(u, v, dmap, minlength, maxlength,
                                integration_direction)

    trajectories = []
    if start_points is None:
        for xm, ym in _gen_starting_points(mask.shape):
            if mask[ym, xm] == 0:
                xg, yg = dmap.mask2grid(xm, ym)
                t = integrate(xg, yg, broken_streamlines,
                              integration_max_step_scale,
                              integration_max_error_scale)
                if t is not None:
                    trajectories.append(t)
    else:
        sp2 = np.asanyarray(start_points, dtype=float).copy()

        # Check if start_points are outside the data boundaries
        for xs, ys in sp2:
            if not (grid.x_origin <= xs <= grid.x_origin + grid.width and
                    grid.y_origin <= ys <= grid.y_origin + grid.height):
                raise ValueError(f"Starting point ({xs}, {ys}) outside of "
                                 "data boundaries")

        # Convert start_points from data to array coords
        # Shift the seed points from the bottom left of the data so that
        # data2grid works properly.
        sp2[:, 0] -= grid.x_origin
        sp2[:, 1] -= grid.y_origin

        for xs, ys in sp2:
            xg, yg = dmap.data2grid(xs, ys)
            # Floating point issues can cause xg, yg to be slightly out of
            # bounds for xs, ys on the upper boundaries. Because we have
            # already checked that the starting points are within the original
            # grid, clip the xg, yg to the grid to work around this issue
            xg = np.clip(xg, 0, grid.nx - 1)
            yg = np.clip(yg, 0, grid.ny - 1)

            t = integrate(xg, yg, broken_streamlines, integration_max_step_scale,
                          integration_max_error_scale)
            if t is not None:
                trajectories.append(t)

    if use_multicolor_lines:
        if norm is None:
            norm = mcolors.Normalize(color.min(), color.max())
        cmap = cm._ensure_cmap(cmap)

    streamlines = []
    arrows = []
    for t in trajectories:
        tgx, tgy = t.T
        # Rescale from grid-coordinates to data-coordinates.
        tx, ty = dmap.grid2data(tgx, tgy)
        tx += grid.x_origin
        ty += grid.y_origin

        # Create multiple tiny segments if varying width or color is given
        if isinstance(linewidth, np.ndarray) or use_multicolor_lines:
            points = np.transpose([tx, ty]).reshape(-1, 1, 2)
            streamlines.extend(np.hstack([points[:-1], points[1:]]))
        else:
            points = np.transpose([tx, ty])
            streamlines.append(points)

        # Distance along streamline
        s = np.cumsum(np.hypot(np.diff(tx), np.diff(ty)))
        if isinstance(linewidth, np.ndarray):
            line_widths = interpgrid(linewidth, tgx, tgy)[:-1]
            line_kw['linewidth'].extend(line_widths)
        if use_multicolor_lines:
            color_values = interpgrid(color, tgx, tgy)[:-1]
            line_colors.append(color_values)

        # Add arrows along each trajectory.
        for x in range(1, num_arrows+1):
            # Get index of distance along streamline to place arrow
            idx = np.searchsorted(s, s[-1] * (x/(num_arrows+1)))
            arrow_tail = (tx[idx], ty[idx])
            arrow_head = (np.mean(tx[idx:idx + 2]), np.mean(ty[idx:idx + 2]))

            if isinstance(linewidth, np.ndarray):
                arrow_kw['linewidth'] = line_widths[idx]

            if use_multicolor_lines:
                arrow_kw['color'] = cmap(norm(color_values[idx]))

            p = patches.FancyArrowPatch(
                arrow_tail, arrow_head, transform=transform, **arrow_kw)
            arrows.append(p)

    lc = mcollections.LineCollection(
        streamlines, transform=transform, **line_kw)
    lc.sticky_edges.x[:] = [grid.x_origin, grid.x_origin + grid.width]
    lc.sticky_edges.y[:] = [grid.y_origin, grid.y_origin + grid.height]
    if use_multicolor_lines:
        lc.set_array(np.ma.hstack(line_colors))
        lc.set_cmap(cmap)
        lc.set_norm(norm)
    axes.add_collection(lc)

    ac = mcollections.PatchCollection(arrows)
    # Adding the collection itself is broken; see #2341.
    for p in arrows:
        axes.add_patch(p)

    axes.autoscale_view()
    stream_container = StreamplotSet(lc, ac)
    return stream_container



# ==================================================
# Line: 566

def _integrate_rk12(x0, y0, dmap, f, maxlength, broken_streamlines=True,
                    integration_max_step_scale=1.0,
                    integration_max_error_scale=1.0):
    """
    2nd-order Runge-Kutta algorithm with adaptive step size.

    This method is also referred to as the improved Euler's method, or Heun's
    method. This method is favored over higher-order methods because:

    1. To get decent looking trajectories and to sample every mask cell
       on the trajectory we need a small timestep, so a lower order
       solver doesn't hurt us unless the data is *very* high resolution.
       In fact, for cases where the user inputs
       data smaller or of similar grid size to the mask grid, the higher
       order corrections are negligible because of the very fast linear
       interpolation used in `interpgrid`.

    2. For high resolution input data (i.e. beyond the mask
       resolution), we must reduce the timestep. Therefore, an adaptive
       timestep is more suited to the problem as this would be very hard
       to judge automatically otherwise.

    This integrator is about 1.5 - 2x as fast as RK4 and RK45 solvers (using
    similar Python implementations) in most setups.
    """
    # This error is below that needed to match the RK4 integrator. It
    # is set for visual reasons -- too low and corners start
    # appearing ugly and jagged. Can be tuned.
    maxerror = 0.003 * integration_max_error_scale

    # This limit is important (for all integrators) to avoid the
    # trajectory skipping some mask cells. We could relax this
    # condition if we use the code which is commented out below to
    # increment the location gradually. However, due to the efficient
    # nature of the interpolation, this doesn't boost speed by much
    # for quite a bit of complexity.
    maxds = min(1. / dmap.mask.nx, 1. / dmap.mask.ny, 0.1)
    maxds *= integration_max_step_scale

    ds = maxds
    stotal = 0
    xi = x0
    yi = y0
    xyf_traj = []

    while True:
        try:
            if dmap.grid.within_grid(xi, yi):
                xyf_traj.append((xi, yi))
            else:
                raise OutOfBounds

            # Compute the two intermediate gradients.
            # f should raise OutOfBounds if the locations given are
            # outside the grid.
            k1x, k1y = f(xi, yi)
            k2x, k2y = f(xi + ds * k1x, yi + ds * k1y)

        except OutOfBounds:
            # Out of the domain during this step.
            # Take an Euler step to the boundary to improve neatness
            # unless the trajectory is currently empty.
            if xyf_traj:
                ds, xyf_traj = _euler_step(xyf_traj, dmap, f)
                stotal += ds
            break
        except TerminateTrajectory:
            break

        dx1 = ds * k1x
        dy1 = ds * k1y
        dx2 = ds * 0.5 * (k1x + k2x)
        dy2 = ds * 0.5 * (k1y + k2y)

        ny, nx = dmap.grid.shape
        # Error is normalized to the axes coordinates
        error = np.hypot((dx2 - dx1) / (nx - 1), (dy2 - dy1) / (ny - 1))

        # Only save step if within error tolerance
        if error < maxerror:
            xi += dx2
            yi += dy2
            try:
                dmap.update_trajectory(xi, yi, broken_streamlines)
            except InvalidIndexError:
                break
            if stotal + ds > maxlength:
                break
            stotal += ds

        # recalculate stepsize based on step error
        if error == 0:
            ds = maxds
        else:
            ds = min(maxds, 0.85 * ds * (maxerror / error) ** 0.5)

    return stotal, xyf_traj



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/axis.py
# Line: 60

def __init__(
    self, axes, loc, *,
    size=None,  # points
    width=None,
    color=None,
    tickdir=None,
    pad=None,
    labelsize=None,
    labelcolor=None,
    labelfontfamily=None,
    zorder=None,
    gridOn=None,  # defaults to axes.grid depending on axes.grid.which
    tick1On=True,
    tick2On=True,
    label1On=True,
    label2On=False,
    major=True,
    labelrotation=0,
    labelrotation_mode=None,
    grid_color=None,
    grid_linestyle=None,
    grid_linewidth=None,
    grid_alpha=None,
    **kwargs,  # Other Line2D kwargs applied to gridlines.

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/spines.py
# Line: 453

def arc_spine(cls, axes, spine_type, center, radius, theta1, theta2,
              **kwargs):
    """Create and return an arc `Spine`."""
    path = mpath.Path.arc(theta1, theta2)
    result = cls(axes, spine_type, path, **kwargs)
    result.set_patch_arc(center, radius, theta1, theta2)
    return result


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_tight_layout.py
# Line: 20

def _auto_adjust_subplotpars(
        fig, renderer, shape, span_pairs, subplot_list,
        ax_bbox_list=None, pad=1.08, h_pad=None, w_pad=None, rect=None):
    """
    Return a dict of subplot parameters to adjust spacing between subplots
    or ``None`` if resulting Axes would have zero height or width.

    Note that this function ignores geometry information of subplot itself, but
    uses what is given by the *shape* and *subplot_list* parameters.  Also, the
    results could be incorrect if some subplots have ``adjustable=datalim``.

    Parameters
    ----------
    shape : tuple[int, int]
        Number of rows and columns of the grid.
    span_pairs : list[tuple[slice, slice]]
        List of rowspans and colspans occupied by each subplot.
    subplot_list : list of subplots
        List of subplots that will be used to calculate optimal subplot_params.
    pad : float
        Padding between the figure edge and the edges of subplots, as a
        fraction of the font size.
    h_pad, w_pad : float
        Padding (height/width) between edges of adjacent subplots, as a
        fraction of the font size.  Defaults to *pad*.
    rect : tuple
        (left, bottom, right, top), default: None.
    """
    rows, cols = shape

    font_size_inch = (FontProperties(
        size=mpl.rcParams["font.size"]).get_size_in_points() / 72)
    pad_inch = pad * font_size_inch
    vpad_inch = h_pad * font_size_inch if h_pad is not None else pad_inch
    hpad_inch = w_pad * font_size_inch if w_pad is not None else pad_inch

    if len(span_pairs) != len(subplot_list) or len(subplot_list) == 0:
        raise ValueError

    if rect is None:
        margin_left = margin_bottom = margin_right = margin_top = None
    else:
        margin_left, margin_bottom, _right, _top = rect
        margin_right = 1 - _right if _right else None
        margin_top = 1 - _top if _top else None

    vspaces = np.zeros((rows + 1, cols))
    hspaces = np.zeros((rows, cols + 1))

    if ax_bbox_list is None:
        ax_bbox_list = [
            Bbox.union([ax.get_position(original=True) for ax in subplots])
            for subplots in subplot_list]

    for subplots, ax_bbox, (rowspan, colspan) in zip(
            subplot_list, ax_bbox_list, span_pairs):
        if all(not ax.get_visible() for ax in subplots):
            continue

        bb = []
        for ax in subplots:
            if ax.get_visible():
                bb += [martist._get_tightbbox_for_layout_only(ax, renderer)]

        tight_bbox_raw = Bbox.union(bb)
        tight_bbox = fig.transFigure.inverted().transform_bbox(tight_bbox_raw)

        hspaces[rowspan, colspan.start] += ax_bbox.xmin - tight_bbox.xmin  # l
        hspaces[rowspan, colspan.stop] += tight_bbox.xmax - ax_bbox.xmax  # r
        vspaces[rowspan.start, colspan] += tight_bbox.ymax - ax_bbox.ymax  # t
        vspaces[rowspan.stop, colspan] += ax_bbox.ymin - tight_bbox.ymin  # b

    fig_width_inch, fig_height_inch = fig.get_size_inches()

    # margins can be negative for Axes with aspect applied, so use max(, 0) to
    # make them nonnegative.
    if not margin_left:
        margin_left = max(hspaces[:, 0].max(), 0) + pad_inch/fig_width_inch
        suplabel = fig._supylabel
        if suplabel and suplabel.get_in_layout():
            rel_width = fig.transFigure.inverted().transform_bbox(
                suplabel.get_window_extent(renderer)).width
            margin_left += rel_width + pad_inch/fig_width_inch
    if not margin_right:
        margin_right = max(hspaces[:, -1].max(), 0) + pad_inch/fig_width_inch
    if not margin_top:
        margin_top = max(vspaces[0, :].max(), 0) + pad_inch/fig_height_inch
        if fig._suptitle and fig._suptitle.get_in_layout():
            rel_height = fig.transFigure.inverted().transform_bbox(
                fig._suptitle.get_window_extent(renderer)).height
            margin_top += rel_height + pad_inch/fig_height_inch
    if not margin_bottom:
        margin_bottom = max(vspaces[-1, :].max(), 0) + pad_inch/fig_height_inch
        suplabel = fig._supxlabel
        if suplabel and suplabel.get_in_layout():
            rel_height = fig.transFigure.inverted().transform_bbox(
                suplabel.get_window_extent(renderer)).height
            margin_bottom += rel_height + pad_inch/fig_height_inch

    if margin_left + margin_right >= 1:
        _api.warn_external('Tight layout not applied. The left and right '
                           'margins cannot be made large enough to '
                           'accommodate all Axes decorations.')
        return None
    if margin_bottom + margin_top >= 1:
        _api.warn_external('Tight layout not applied. The bottom and top '
                           'margins cannot be made large enough to '
                           'accommodate all Axes decorations.')
        return None

    kwargs = dict(left=margin_left,
                  right=1 - margin_right,
                  bottom=margin_bottom,
                  top=1 - margin_top)

    if cols > 1:
        hspace = hspaces[:, 1:-1].max() + hpad_inch / fig_width_inch
        # axes widths:
        h_axes = (1 - margin_right - margin_left - hspace * (cols - 1)) / cols
        if h_axes < 0:
            _api.warn_external('Tight layout not applied. tight_layout '
                               'cannot make Axes width small enough to '
                               'accommodate all Axes decorations')
            return None
        else:
            kwargs["wspace"] = hspace / h_axes
    if rows > 1:
        vspace = vspaces[1:-1, :].max() + vpad_inch / fig_height_inch
        v_axes = (1 - margin_top - margin_bottom - vspace * (rows - 1)) / rows
        if v_axes < 0:
            _api.warn_external('Tight layout not applied. tight_layout '
                               'cannot make Axes height small enough to '
                               'accommodate all Axes decorations.')
            return None
        else:
            kwargs["hspace"] = vspace / v_axes

    return kwargs



# ==================================================
# Line: 194

def get_tight_layout_figure(fig, axes_list, subplotspec_list, renderer,
                            pad=1.08, h_pad=None, w_pad=None, rect=None):
    """
    Return subplot parameters for tight-layouted-figure with specified padding.

    Parameters
    ----------
    fig : Figure
    axes_list : list of Axes
    subplotspec_list : list of `.SubplotSpec`
        The subplotspecs of each Axes.
    renderer : renderer
    pad : float
        Padding between the figure edge and the edges of subplots, as a
        fraction of the font size.
    h_pad, w_pad : float
        Padding (height/width) between edges of adjacent subplots.  Defaults to
        *pad*.
    rect : tuple (left, bottom, right, top), default: None.
        rectangle in normalized figure coordinates
        that the whole subplots area (including labels) will fit into.
        Defaults to using the entire figure.

    Returns
    -------
    subplotspec or None
        subplotspec kwargs to be passed to `.Figure.subplots_adjust` or
        None if tight_layout could not be accomplished.
    """

    # Multiple Axes can share same subplotspec (e.g., if using axes_grid1);
    # we need to group them together.
    ss_to_subplots = {ss: [] for ss in subplotspec_list}
    for ax, ss in zip(axes_list, subplotspec_list):
        ss_to_subplots[ss].append(ax)
    if ss_to_subplots.pop(None, None):
        _api.warn_external(
            "This figure includes Axes that are not compatible with "
            "tight_layout, so results might be incorrect.")
    if not ss_to_subplots:
        return {}
    subplot_list = list(ss_to_subplots.values())
    ax_bbox_list = [ss.get_position(fig) for ss in ss_to_subplots]

    max_nrows = max(ss.get_gridspec().nrows for ss in ss_to_subplots)
    max_ncols = max(ss.get_gridspec().ncols for ss in ss_to_subplots)

    span_pairs = []
    for ss in ss_to_subplots:
        # The intent here is to support Axes from different gridspecs where
        # one's nrows (or ncols) is a multiple of the other (e.g. 2 and 4),
        # but this doesn't actually work because the computed wspace, in
        # relative-axes-height, corresponds to different physical spacings for
        # the 2-row grid and the 4-row grid.  Still, this code is left, mostly
        # for backcompat.
        rows, cols = ss.get_gridspec().get_geometry()
        div_row, mod_row = divmod(max_nrows, rows)
        div_col, mod_col = divmod(max_ncols, cols)
        if mod_row != 0:
            _api.warn_external('tight_layout not applied: number of rows '
                               'in subplot specifications must be '
                               'multiples of one another.')
            return {}
        if mod_col != 0:
            _api.warn_external('tight_layout not applied: number of '
                               'columns in subplot specifications must be '
                               'multiples of one another.')
            return {}
        span_pairs.append((
            slice(ss.rowspan.start * div_row, ss.rowspan.stop * div_row),
            slice(ss.colspan.start * div_col, ss.colspan.stop * div_col)))

    kwargs = _auto_adjust_subplotpars(fig, renderer,
                                      shape=(max_nrows, max_ncols),
                                      span_pairs=span_pairs,
                                      subplot_list=subplot_list,
                                      ax_bbox_list=ax_bbox_list,
                                      pad=pad, h_pad=h_pad, w_pad=w_pad)

    # kwargs can be none if tight_layout fails...
    if rect is not None and kwargs is not None:
        # if rect is given, the whole subplots area (including
        # labels) will fit into the rect instead of the
        # figure. Note that the rect argument of
        # *auto_adjust_subplotpars* specify the area that will be
        # covered by the total area of axes.bbox. Thus we call
        # auto_adjust_subplotpars twice, where the second run
        # with adjusted rect parameters.

        left, bottom, right, top = rect
        if left is not None:
            left += kwargs["left"]
        if bottom is not None:
            bottom += kwargs["bottom"]
        if right is not None:
            right -= (1 - kwargs["right"])
        if top is not None:
            top -= (1 - kwargs["top"])

        kwargs = _auto_adjust_subplotpars(fig, renderer,
                                          shape=(max_nrows, max_ncols),
                                          span_pairs=span_pairs,
                                          subplot_list=subplot_list,
                                          ax_bbox_list=ax_bbox_list,
                                          pad=pad, h_pad=h_pad, w_pad=w_pad,
                                          rect=(left, bottom, right, top))

    return kwargs

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/dviread.py
# Line: 433

def _bop(self, c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, p):
    self.state = _dvistate.inpage
    self.h = self.v = self.w = self.x = self.y = self.z = 0
    self.stack = []
    self.text = []          # list of Text objects
    self.boxes = []         # list of Box objects


# ==================================================
# Occurrences: Lines 502-505 (2 instances)

def _fnt_def(self, k, c, s, d, a, l):
    self._fnt_def_real(k, c, s, d, a, l)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/dates.py
# Line: 668

def __init__(self, locator, tz=None, formats=None, offset_formats=None,
             zero_formats=None, show_offset=True, *, usetex=None):
    """
    Autoformat the date labels.  The default format is used to form an
    initial string, and then redundant elements are removed.
    """
    self._locator = locator
    self._tz = tz
    self.defaultfmt = '%Y'
    # there are 6 levels with each level getting a specific format
    # 0: mostly years,  1: months,  2: days,
    # 3: hours, 4: minutes, 5: seconds
    if formats:
        if len(formats) != 6:
            raise ValueError('formats argument must be a list of '
                             '6 format strings (or None)')
        self.formats = formats
    else:
        self.formats = ['%Y',  # ticks are mostly years
                        '%b',          # ticks are mostly months
                        '%d',          # ticks are mostly days
                        '%H:%M',       # hrs
                        '%H:%M',       # min
                        '%S.%f',       # secs
                        ]
    # fmt for zeros ticks at this level.  These are
    # ticks that should be labeled w/ info the level above.
    # like 1 Jan can just be labelled "Jan".  02:02:00 can
    # just be labeled 02:02.
    if zero_formats:
        if len(zero_formats) != 6:
            raise ValueError('zero_formats argument must be a list of '
                             '6 format strings (or None)')
        self.zero_formats = zero_formats
    elif formats:
        # use the users formats for the zero tick formats
        self.zero_formats = [''] + self.formats[:-1]
    else:
        # make the defaults a bit nicer:
        self.zero_formats = [''] + self.formats[:-1]
        self.zero_formats[3] = '%b-%d'

    if offset_formats:
        if len(offset_formats) != 6:
            raise ValueError('offset_formats argument must be a list of '
                             '6 format strings (or None)')
        self.offset_formats = offset_formats
    else:
        self.offset_formats = ['',
                               '%Y',
                               '%Y-%b',
                               '%Y-%b-%d',
                               '%Y-%b-%d',
                               '%Y-%b-%d %H:%M']
    self.offset_string = ''
    self.show_offset = show_offset
    self._usetex = mpl._val_or_rc(usetex, 'text.usetex')


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/colors.py
# Line: 1068

def __init__(self, name, segmentdata, N=256, gamma=1.0, *,
             bad=None, under=None, over=None):
    """
    Create colormap from linear mapping segments.

    Parameters
    ----------
    name : str
        The name of the colormap.
    segmentdata : dict
        A dictionary with keys "red", "green", "blue" for the color channels.
        Each entry should be a list of *x*, *y0*, *y1* tuples, forming rows
        in a table. Entries for alpha are optional.

        Example: suppose you want red to increase from 0 to 1 over
        the bottom half, green to do the same over the middle half,
        and blue over the top half.  Then you would use::

            {
                'red':   [(0.0,  0.0, 0.0),
                          (0.5,  1.0, 1.0),
                          (1.0,  1.0, 1.0)],
                'green': [(0.0,  0.0, 0.0),
                          (0.25, 0.0, 0.0),
                          (0.75, 1.0, 1.0),
                          (1.0,  1.0, 1.0)],
                'blue':  [(0.0,  0.0, 0.0),
                          (0.5,  0.0, 0.0),
                          (1.0,  1.0, 1.0)]
            }

        Each row in the table for a given color is a sequence of
        *x*, *y0*, *y1* tuples.  In each sequence, *x* must increase
        monotonically from 0 to 1.  For any input value *z* falling
        between *x[i]* and *x[i+1]*, the output value of a given color
        will be linearly interpolated between *y1[i]* and *y0[i+1]*::

            row i:   x  y0  y1
                           /
                          /
            row i+1: x  y0  y1

        Hence, y0 in the first row and y1 in the last row are never used.

    N : int
        The number of RGB quantization levels.
    gamma : float
        Gamma correction factor for input distribution x of the mapping.
        See also https://en.wikipedia.org/wiki/Gamma_correction.
    bad : :mpltype:`color`, default: transparent
        The color for invalid values (NaN or masked).

        .. versionadded:: 3.11

    under : :mpltype:`color`, default: color of the lowest value
        The color for low out-of-range values.

        .. versionadded:: 3.11

    over : :mpltype:`color`, default: color of the highest value
        The color for high out-of-range values.

        .. versionadded:: 3.11

    See Also
    --------
    LinearSegmentedColormap.from_list
        Static method; factory function for generating a smoothly-varying
        LinearSegmentedColormap.
    """
    # True only if all colors in map are identical; needed for contouring.
    self.monochrome = False
    super().__init__(name, N, bad=bad, under=under, over=over)
    self._segmentdata = segmentdata
    self._gamma = gamma


# ==================================================
# Line: 1164

def from_list(name, colors, N=256, gamma=1.0, *, bad=None, under=None, over=None):
    """
    Create a `LinearSegmentedColormap` from a list of colors.

    Parameters
    ----------
    name : str
        The name of the colormap.
    colors : list of :mpltype:`color` or list of (value, color)
        If only colors are given, they are equidistantly mapped from the
        range :math:`[0, 1]`; i.e. 0 maps to ``colors[0]`` and 1 maps to
        ``colors[-1]``.
        If (value, color) pairs are given, the mapping is from *value*
        to *color*. This can be used to divide the range unevenly. The
        values must increase monotonically from 0 to 1.
    N : int
        The number of RGB quantization levels.
    gamma : float

    bad : :mpltype:`color`, default: transparent
        The color for invalid values (NaN or masked).
    under : :mpltype:`color`, default: color of the lowest value
        The color for low out-of-range values.
    over : :mpltype:`color`, default: color of the highest value
        The color for high out-of-range values.
    """
    if not np.iterable(colors):
        raise ValueError('colors must be iterable')

    try:
        # Assume the passed colors are a list of colors
        # and not a (value, color) tuple.
        r, g, b, a = to_rgba_array(colors).T
        vals = np.linspace(0, 1, len(colors))
    except Exception as e:
        # Assume the passed values are a list of
        # (value, color) tuples.
        try:
            _vals, _colors = itertools.zip_longest(*colors)
        except Exception as e2:
            raise e2 from e
        vals = np.asarray(_vals)
        if np.min(vals) < 0 or np.max(vals) > 1 or np.any(np.diff(vals) <= 0):
            raise ValueError(
                "the values passed in the (value, color) pairs "
                "must increase monotonically from 0 to 1."
            )
        r, g, b, a = to_rgba_array(_colors).T

    cdict = {
        "red": np.column_stack([vals, r, r]),
        "green": np.column_stack([vals, g, g]),
        "blue": np.column_stack([vals, b, b]),
        "alpha": np.column_stack([vals, a, a]),
    }

    return LinearSegmentedColormap(name, cdict, N, gamma,
                                   bad=bad, under=under, over=over)


# ==================================================
# Line: 1324

def __init__(self, colors, name='from_list', N=None, *,
             bad=None, under=None, over=None):
    if N is None:
        self.colors = colors
        N = len(colors)
    else:
        if isinstance(colors, str):
            self.colors = [colors] * N
        elif np.iterable(colors):
            self.colors = list(
                itertools.islice(itertools.cycle(colors), N))
        else:
            try:
                gray = float(colors)
            except TypeError:
                pass
            else:
                self.colors = [gray] * N
    super().__init__(name, N, bad=bad, under=under, over=over)


# ==================================================
# Line: 3390

def __init__(self, azdeg=315, altdeg=45, hsv_min_val=0, hsv_max_val=1,
             hsv_min_sat=1, hsv_max_sat=0):
    """
    Specify the azimuth (measured clockwise from south) and altitude
    (measured up from the plane of the surface) of the light source
    in degrees.

    Parameters
    ----------
    azdeg : float, default: 315 degrees (from the northwest)
        The azimuth (0-360, degrees clockwise from North) of the light
        source.
    altdeg : float, default: 45 degrees
        The altitude (0-90, degrees up from horizontal) of the light
        source.
    hsv_min_val : number, default: 0
        The minimum value ("v" in "hsv") that the *intensity* map can shift the
        output image to.
    hsv_max_val : number, default: 1
        The maximum value ("v" in "hsv") that the *intensity* map can shift the
        output image to.
    hsv_min_sat : number, default: 1
        The minimum saturation value that the *intensity* map can shift the output
        image to.
    hsv_max_sat : number, default: 0
        The maximum saturation value that the *intensity* map can shift the output
        image to.

    Notes
    -----
    For backwards compatibility, the parameters *hsv_min_val*,
    *hsv_max_val*, *hsv_min_sat*, and *hsv_max_sat* may be supplied at
    initialization as well.  However, these parameters will only be used if
    "blend_mode='hsv'" is passed into `shade` or `shade_rgb`.
    See the documentation for `blend_hsv` for more details.
    """
    self.azdeg = azdeg
    self.altdeg = altdeg
    self.hsv_min_val = hsv_min_val
    self.hsv_max_val = hsv_max_val
    self.hsv_min_sat = hsv_min_sat
    self.hsv_max_sat = hsv_max_sat


# ==================================================
# Line: 3545

def shade(self, data, cmap, norm=None, blend_mode='overlay', vmin=None,
          vmax=None, vert_exag=1, dx=1, dy=1, fraction=1, **kwargs):
    """
    Combine colormapped data values with an illumination intensity map
    (a.k.a.  "hillshade") of the values.

    Parameters
    ----------
    data : 2D array-like
        The height values used to generate a shaded map.
    cmap : `~matplotlib.colors.Colormap`
        The colormap used to color the *data* array. Note that this must be
        a `~matplotlib.colors.Colormap` instance.  For example, rather than
        passing in ``cmap='gist_earth'``, use
        ``cmap=plt.get_cmap('gist_earth')`` instead.
    norm : `~matplotlib.colors.Normalize` instance, optional
        The normalization used to scale values before colormapping. If
        None, the input will be linearly scaled between its min and max.
    blend_mode : {'hsv', 'overlay', 'soft'} or callable, optional
        The type of blending used to combine the colormapped data
        values with the illumination intensity.  Default is
        "overlay".  Note that for most topographic surfaces,
        "overlay" or "soft" appear more visually realistic. If a
        user-defined function is supplied, it is expected to
        combine an (M, N, 3) RGB array of floats (ranging 0 to 1) with
        an (M, N, 1) hillshade array (also 0 to 1).  (Call signature
        ``func(rgb, illum, **kwargs)``) Additional kwargs supplied
        to this function will be passed on to the *blend_mode*
        function.
    vmin : float or None, optional
        The minimum value used in colormapping *data*. If *None* the
        minimum value in *data* is used. If *norm* is specified, then this
        argument will be ignored.
    vmax : float or None, optional
        The maximum value used in colormapping *data*. If *None* the
        maximum value in *data* is used. If *norm* is specified, then this
        argument will be ignored.
    vert_exag : number, optional
        The amount to exaggerate the elevation values by when calculating
        illumination. This can be used either to correct for differences in
        units between the x-y coordinate system and the elevation
        coordinate system (e.g. decimal degrees vs. meters) or to
        exaggerate or de-emphasize topography.
    dx : number, optional
        The x-spacing (columns) of the input *elevation* grid.
    dy : number, optional
        The y-spacing (rows) of the input *elevation* grid.
    fraction : number, optional
        Increases or decreases the contrast of the hillshade.  Values
        greater than one will cause intermediate values to move closer to
        full illumination or shadow (and clipping any values that move
        beyond 0 or 1). Note that this is not visually or mathematically
        the same as vertical exaggeration.
    **kwargs
        Additional kwargs are passed on to the *blend_mode* function.

    Returns
    -------
    `~numpy.ndarray`
        An (M, N, 4) array of floats ranging between 0-1.
    """
    if vmin is None:
        vmin = data.min()
    if vmax is None:
        vmax = data.max()
    if norm is None:
        norm = Normalize(vmin=vmin, vmax=vmax)

    rgb0 = cmap(norm(data))
    rgb1 = self.shade_rgb(rgb0, elevation=data, blend_mode=blend_mode,
                          vert_exag=vert_exag, dx=dx, dy=dy,
                          fraction=fraction, **kwargs)
    # Don't overwrite the alpha channel, if present.
    rgb0[..., :3] = rgb1[..., :3]
    return rgb0


# ==================================================
# Line: 3621

def shade_rgb(self, rgb, elevation, fraction=1., blend_mode='hsv',
              vert_exag=1, dx=1, dy=1, **kwargs):
    """
    Use this light source to adjust the colors of the *rgb* input array to
    give the impression of a shaded relief map with the given *elevation*.

    Parameters
    ----------
    rgb : array-like
        An (M, N, 3) RGB array, assumed to be in the range of 0 to 1.
    elevation : array-like
        An (M, N) array of the height values used to generate a shaded map.
    fraction : number
        Increases or decreases the contrast of the hillshade.  Values
        greater than one will cause intermediate values to move closer to
        full illumination or shadow (and clipping any values that move
        beyond 0 or 1). Note that this is not visually or mathematically
        the same as vertical exaggeration.
    blend_mode : {'hsv', 'overlay', 'soft'} or callable, optional
        The type of blending used to combine the colormapped data values
        with the illumination intensity.  For backwards compatibility, this
        defaults to "hsv". Note that for most topographic surfaces,
        "overlay" or "soft" appear more visually realistic. If a
        user-defined function is supplied, it is expected to combine an
        (M, N, 3) RGB array of floats (ranging 0 to 1) with an (M, N, 1)
        hillshade array (also 0 to 1).  (Call signature
        ``func(rgb, illum, **kwargs)``)
        Additional kwargs supplied to this function will be passed on to
        the *blend_mode* function.
    vert_exag : number, optional
        The amount to exaggerate the elevation values by when calculating
        illumination. This can be used either to correct for differences in
        units between the x-y coordinate system and the elevation
        coordinate system (e.g. decimal degrees vs. meters) or to
        exaggerate or de-emphasize topography.
    dx : number, optional
        The x-spacing (columns) of the input *elevation* grid.
    dy : number, optional
        The y-spacing (rows) of the input *elevation* grid.
    **kwargs
        Additional kwargs are passed on to the *blend_mode* function.

    Returns
    -------
    `~numpy.ndarray`
        An (m, n, 3) array of floats ranging between 0-1.
    """
    # Calculate the "hillshade" intensity.
    intensity = self.hillshade(elevation, vert_exag, dx, dy, fraction)
    intensity = intensity[..., np.newaxis]

    # Blend the hillshade and rgb data using the specified mode
    lookup = {
            'hsv': self.blend_hsv,
            'soft': self.blend_soft_light,
            'overlay': self.blend_overlay,
            }
    if blend_mode in lookup:
        blend = lookup[blend_mode](rgb, intensity, **kwargs)
    else:
        try:
            blend = blend_mode(rgb, intensity, **kwargs)
        except TypeError as err:
            raise ValueError('"blend_mode" must be callable or one of '
                             f'{lookup.keys}') from err

    # Only apply result where hillshade intensity isn't masked
    if np.ma.is_masked(intensity):
        mask = intensity.mask[..., 0]
        for i in range(3):
            blend[..., i][mask] = rgb[..., i][mask]

    return blend


# ==================================================
# Line: 3695

def blend_hsv(self, rgb, intensity, hsv_max_sat=None, hsv_max_val=None,
              hsv_min_val=None, hsv_min_sat=None):
    """
    Take the input data array, convert to HSV values in the given colormap,
    then adjust those color values to give the impression of a shaded
    relief map with a specified light source.  RGBA values are returned,
    which can then be used to plot the shaded image with imshow.

    The color of the resulting image will be darkened by moving the (s, v)
    values (in HSV colorspace) toward (hsv_min_sat, hsv_min_val) in the
    shaded regions, or lightened by sliding (s, v) toward (hsv_max_sat,
    hsv_max_val) in regions that are illuminated.  The default extremes are
    chose so that completely shaded points are nearly black (s = 1, v = 0)
    and completely illuminated points are nearly white (s = 0, v = 1).

    Parameters
    ----------
    rgb : `~numpy.ndarray`
        An (M, N, 3) RGB array of floats ranging from 0 to 1 (color image).
    intensity : `~numpy.ndarray`
        An (M, N, 1) array of floats ranging from 0 to 1 (grayscale image).
    hsv_max_sat : number, optional
        The maximum saturation value that the *intensity* map can shift the output
        image to. If not provided, use the value provided upon initialization.
    hsv_min_sat : number, optional
        The minimum saturation value that the *intensity* map can shift the output
        image to. If not provided, use the value provided upon initialization.
    hsv_max_val : number, optional
        The maximum value ("v" in "hsv") that the *intensity* map can shift the
        output image to. If not provided, use the value provided upon
        initialization.
    hsv_min_val : number, optional
        The minimum value ("v" in "hsv") that the *intensity* map can shift the
        output image to. If not provided, use the value provided upon
        initialization.

    Returns
    -------
    `~numpy.ndarray`
        An (M, N, 3) RGB array representing the combined images.
    """
    # Backward compatibility...
    if hsv_max_sat is None:
        hsv_max_sat = self.hsv_max_sat
    if hsv_max_val is None:
        hsv_max_val = self.hsv_max_val
    if hsv_min_sat is None:
        hsv_min_sat = self.hsv_min_sat
    if hsv_min_val is None:
        hsv_min_val = self.hsv_min_val

    # Expects a 2D intensity array scaled between -1 to 1...
    intensity = intensity[..., 0]
    intensity = 2 * intensity - 1

    # Convert to rgb, then rgb to hsv
    hsv = rgb_to_hsv(rgb[:, :, 0:3])
    hue, sat, val = np.moveaxis(hsv, -1, 0)

    # Modify hsv values (in place) to simulate illumination.
    # putmask(A, mask, B) <=> A[mask] = B[mask]
    np.putmask(sat, (np.abs(sat) > 1.e-10) & (intensity > 0),
               (1 - intensity) * sat + intensity * hsv_max_sat)
    np.putmask(sat, (np.abs(sat) > 1.e-10) & (intensity < 0),
               (1 + intensity) * sat - intensity * hsv_min_sat)
    np.putmask(val, intensity > 0,
               (1 - intensity) * val + intensity * hsv_max_val)
    np.putmask(val, intensity < 0,
               (1 + intensity) * val - intensity * hsv_min_val)
    np.clip(hsv[:, :, 1:], 0, 1, out=hsv[:, :, 1:])

    # Convert modified hsv back to rgb.
    return hsv_to_rgb(hsv)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/sankey.py
# Line: 42

def __init__(self, ax=None, scale=1.0, unit='', format='%G', gap=0.25,
             radius=0.1, shoulder=0.03, offset=0.15, head_angle=100,
             margin=0.4, tolerance=1e-6, **kwargs):
    """
    Create a new Sankey instance.

    The optional arguments listed below are applied to all subdiagrams so
    that there is consistent alignment and formatting.

    In order to draw a complex Sankey diagram, create an instance of
    `Sankey` by calling it without any kwargs::

        sankey = Sankey()

    Then add simple Sankey sub-diagrams::

        sankey.add() # 1
        sankey.add() # 2
        #...
        sankey.add() # n

    Finally, create the full diagram::

        sankey.finish()

    Or, instead, simply daisy-chain those calls::

        Sankey().add().add...  .add().finish()

    Other Parameters
    ----------------
    ax : `~matplotlib.axes.Axes`
        Axes onto which the data should be plotted.  If *ax* isn't
        provided, new Axes will be created.
    scale : float
        Scaling factor for the flows.  *scale* sizes the width of the paths
        in order to maintain proper layout.  The same scale is applied to
        all subdiagrams.  The value should be chosen such that the product
        of the scale and the sum of the inputs is approximately 1.0 (and
        the product of the scale and the sum of the outputs is
        approximately -1.0).
    unit : str
        The physical unit associated with the flow quantities.  If *unit*
        is None, then none of the quantities are labeled.
    format : str or callable
        A Python number formatting string or callable used to label the
        flows with their quantities (i.e., a number times a unit, where the
        unit is given). If a format string is given, the label will be
        ``format % quantity``. If a callable is given, it will be called
        with ``quantity`` as an argument.
    gap : float
        Space between paths that break in/break away to/from the top or
        bottom.
    radius : float
        Inner radius of the vertical paths.
    shoulder : float
        Size of the shoulders of output arrows.
    offset : float
        Text offset (from the dip or tip of the arrow).
    head_angle : float
        Angle, in degrees, of the arrow heads (and negative of the angle of
        the tails).
    margin : float
        Minimum space between Sankey outlines and the edge of the plot
        area.
    tolerance : float
        Acceptable maximum of the magnitude of the sum of flows.  The
        magnitude of the sum of connected flows cannot be greater than
        *tolerance*.
    **kwargs
        Any additional keyword arguments will be passed to `add`, which
        will create the first subdiagram.

    See Also
    --------
    Sankey.add
    Sankey.finish

    Examples
    --------
    .. plot:: gallery/specialty_plots/sankey_basics.py
    """
    # Check the arguments.
    if gap < 0:
        raise ValueError(
            "'gap' is negative, which is not allowed because it would "
            "cause the paths to overlap")
    if radius > gap:
        raise ValueError(
            "'radius' is greater than 'gap', which is not allowed because "
            "it would cause the paths to overlap")
    if head_angle < 0:
        raise ValueError(
            "'head_angle' is negative, which is not allowed because it "
            "would cause inputs to look like outputs and vice versa")
    if tolerance < 0:
        raise ValueError(
            "'tolerance' is negative, but it must be a magnitude")

    # Create Axes if necessary.
    if ax is None:
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[])

    self.diagrams = []

    # Store the inputs.
    self.ax = ax
    self.unit = unit
    self.format = format
    self.scale = scale
    self.gap = gap
    self.radius = radius
    self.shoulder = shoulder
    self.offset = offset
    self.margin = margin
    self.pitch = np.tan(np.pi * (1 - head_angle / 180.0) / 2.0)
    self.tolerance = tolerance

    # Initialize the vertices of tight box around the diagram(s).
    self.extent = np.array((np.inf, -np.inf, np.inf, -np.inf))

    # If there are any kwargs, create the first subdiagram.
    if len(kwargs):
        self.add(**kwargs)


# ==================================================
# Line: 351

def add(self, patchlabel='', flows=None, orientations=None, labels='',
        trunklength=1.0, pathlengths=0.25, prior=None, connect=(0, 0),
        rotation=0, **kwargs):
    """
    Add a simple Sankey diagram with flows at the same hierarchical level.

    Parameters
    ----------
    patchlabel : str
        Label to be placed at the center of the diagram.
        Note that *label* (not *patchlabel*) can be passed as keyword
        argument to create an entry in the legend.

    flows : list of float
        Array of flow values.  By convention, inputs are positive and
        outputs are negative.

        Flows are placed along the top of the diagram from the inside out
        in order of their index within *flows*.  They are placed along the
        sides of the diagram from the top down and along the bottom from
        the outside in.

        If the sum of the inputs and outputs is
        nonzero, the discrepancy will appear as a cubic Bézier curve along
        the top and bottom edges of the trunk.

    orientations : list of {-1, 0, 1}
        List of orientations of the flows (or a single orientation to be
        used for all flows).  Valid values are 0 (inputs from
        the left, outputs to the right), 1 (from and to the top) or -1
        (from and to the bottom).

    labels : list of (str or None)
        List of labels for the flows (or a single label to be used for all
        flows).  Each label may be *None* (no label), or a labeling string.
        If an entry is a (possibly empty) string, then the quantity for the
        corresponding flow will be shown below the string.  However, if
        the *unit* of the main diagram is None, then quantities are never
        shown, regardless of the value of this argument.

    trunklength : float
        Length between the bases of the input and output groups (in
        data-space units).

    pathlengths : list of float
        List of lengths of the vertical arrows before break-in or after
        break-away.  If a single value is given, then it will be applied to
        the first (inside) paths on the top and bottom, and the length of
        all other arrows will be justified accordingly.  The *pathlengths*
        are not applied to the horizontal inputs and outputs.

    prior : int
        Index of the prior diagram to which this diagram should be
        connected.

    connect : (int, int)
        A (prior, this) tuple indexing the flow of the prior diagram and
        the flow of this diagram which should be connected.  If this is the
        first diagram or *prior* is *None*, *connect* will be ignored.

    rotation : float
        Angle of rotation of the diagram in degrees.  The interpretation of
        the *orientations* argument will be rotated accordingly (e.g., if
        *rotation* == 90, an *orientations* entry of 1 means to/from the
        left).  *rotation* is ignored if this diagram is connected to an
        existing one (using *prior* and *connect*).

    Returns
    -------
    Sankey
        The current `.Sankey` instance.

    Other Parameters
    ----------------
    **kwargs
       Additional keyword arguments set `matplotlib.patches.PathPatch`
       properties, listed below.  For example, one may want to use
       ``fill=False`` or ``label="A legend entry"``.

    %(Patch:kwdoc)s

    See Also
    --------
    Sankey.finish
    """
    # Check and preprocess the arguments.
    flows = np.array([1.0, -1.0]) if flows is None else np.array(flows)
    n = flows.shape[0]  # Number of flows
    if rotation is None:
        rotation = 0
    else:
        # In the code below, angles are expressed in deg/90.
        rotation /= 90.0
    if orientations is None:
        orientations = 0
    try:
        orientations = np.broadcast_to(orientations, n)
    except ValueError:
        raise ValueError(
            f"The shapes of 'flows' {np.shape(flows)} and 'orientations' "
            f"{np.shape(orientations)} are incompatible"
        ) from None
    try:
        labels = np.broadcast_to(labels, n)
    except ValueError:
        raise ValueError(
            f"The shapes of 'flows' {np.shape(flows)} and 'labels' "
            f"{np.shape(labels)} are incompatible"
        ) from None
    if trunklength < 0:
        raise ValueError(
            "'trunklength' is negative, which is not allowed because it "
            "would cause poor layout")
    if abs(np.sum(flows)) > self.tolerance:
        _log.info("The sum of the flows is nonzero (%f; patchlabel=%r); "
                  "is the system not at steady state?",
                  np.sum(flows), patchlabel)
    scaled_flows = self.scale * flows
    gain = sum(max(flow, 0) for flow in scaled_flows)
    loss = sum(min(flow, 0) for flow in scaled_flows)
    if prior is not None:
        if prior < 0:
            raise ValueError("The index of the prior diagram is negative")
        if min(connect) < 0:
            raise ValueError(
                "At least one of the connection indices is negative")
        if prior >= len(self.diagrams):
            raise ValueError(
                f"The index of the prior diagram is {prior}, but there "
                f"are only {len(self.diagrams)} other diagrams")
        if connect[0] >= len(self.diagrams[prior].flows):
            raise ValueError(
                "The connection index to the source diagram is {}, but "
                "that diagram has only {} flows".format(
                    connect[0], len(self.diagrams[prior].flows)))
        if connect[1] >= n:
            raise ValueError(
                f"The connection index to this diagram is {connect[1]}, "
                f"but this diagram has only {n} flows")
        if self.diagrams[prior].angles[connect[0]] is None:
            raise ValueError(
                f"The connection cannot be made, which may occur if the "
                f"magnitude of flow {connect[0]} of diagram {prior} is "
                f"less than the specified tolerance")
        flow_error = (self.diagrams[prior].flows[connect[0]] +
                      flows[connect[1]])
        if abs(flow_error) >= self.tolerance:
            raise ValueError(
                f"The scaled sum of the connected flows is {flow_error}, "
                f"which is not within the tolerance ({self.tolerance})")

    # Determine if the flows are inputs.
    are_inputs = [None] * n
    for i, flow in enumerate(flows):
        if flow >= self.tolerance:
            are_inputs[i] = True
        elif flow <= -self.tolerance:
            are_inputs[i] = False
        else:
            _log.info(
                "The magnitude of flow %d (%f) is below the tolerance "
                "(%f).\nIt will not be shown, and it cannot be used in a "
                "connection.", i, flow, self.tolerance)

    # Determine the angles of the arrows (before rotation).
    angles = [None] * n
    for i, (orient, is_input) in enumerate(zip(orientations, are_inputs)):
        if orient == 1:
            if is_input:
                angles[i] = DOWN
            elif is_input is False:
                # Be specific since is_input can be None.
                angles[i] = UP
        elif orient == 0:
            if is_input is not None:
                angles[i] = RIGHT
        else:
            if orient != -1:
                raise ValueError(
                    f"The value of orientations[{i}] is {orient}, "
                    f"but it must be -1, 0, or 1")
            if is_input:
                angles[i] = UP
            elif is_input is False:
                angles[i] = DOWN

    # Justify the lengths of the paths.
    if np.iterable(pathlengths):
        if len(pathlengths) != n:
            raise ValueError(
                f"The lengths of 'flows' ({n}) and 'pathlengths' "
                f"({len(pathlengths)}) are incompatible")
    else:  # Make pathlengths into a list.
        urlength = pathlengths
        ullength = pathlengths
        lrlength = pathlengths
        lllength = pathlengths
        d = dict(RIGHT=pathlengths)
        pathlengths = [d.get(angle, 0) for angle in angles]
        # Determine the lengths of the top-side arrows
        # from the middle outwards.
        for i, (angle, is_input, flow) in enumerate(zip(angles, are_inputs,
                                                        scaled_flows)):
            if angle == DOWN and is_input:
                pathlengths[i] = ullength
                ullength += flow
            elif angle == UP and is_input is False:
                pathlengths[i] = urlength
                urlength -= flow  # Flow is negative for outputs.
        # Determine the lengths of the bottom-side arrows
        # from the middle outwards.
        for i, (angle, is_input, flow) in enumerate(reversed(list(zip(
              angles, are_inputs, scaled_flows)))):
            if angle == UP and is_input:
                pathlengths[n - i - 1] = lllength
                lllength += flow
            elif angle == DOWN and is_input is False:
                pathlengths[n - i - 1] = lrlength
                lrlength -= flow
        # Determine the lengths of the left-side arrows
        # from the bottom upwards.
        has_left_input = False
        for i, (angle, is_input, spec) in enumerate(reversed(list(zip(
              angles, are_inputs, zip(scaled_flows, pathlengths))))):
            if angle == RIGHT:
                if is_input:
                    if has_left_input:
                        pathlengths[n - i - 1] = 0
                    else:
                        has_left_input = True
        # Determine the lengths of the right-side arrows
        # from the top downwards.
        has_right_output = False
        for i, (angle, is_input, spec) in enumerate(zip(
              angles, are_inputs, list(zip(scaled_flows, pathlengths)))):
            if angle == RIGHT:
                if is_input is False:
                    if has_right_output:
                        pathlengths[i] = 0
                    else:
                        has_right_output = True

    # Begin the subpaths, and smooth the transition if the sum of the flows
    # is nonzero.
    urpath = [(Path.MOVETO, [(self.gap - trunklength / 2.0),  # Upper right
                             gain / 2.0]),
              (Path.LINETO, [(self.gap - trunklength / 2.0) / 2.0,
                             gain / 2.0]),
              (Path.CURVE4, [(self.gap - trunklength / 2.0) / 8.0,
                             gain / 2.0]),
              (Path.CURVE4, [(trunklength / 2.0 - self.gap) / 8.0,
                             -loss / 2.0]),
              (Path.LINETO, [(trunklength / 2.0 - self.gap) / 2.0,
                             -loss / 2.0]),
              (Path.LINETO, [(trunklength / 2.0 - self.gap),
                             -loss / 2.0])]
    llpath = [(Path.LINETO, [(trunklength / 2.0 - self.gap),  # Lower left
                             loss / 2.0]),
              (Path.LINETO, [(trunklength / 2.0 - self.gap) / 2.0,
                             loss / 2.0]),
              (Path.CURVE4, [(trunklength / 2.0 - self.gap) / 8.0,
                             loss / 2.0]),
              (Path.CURVE4, [(self.gap - trunklength / 2.0) / 8.0,
                             -gain / 2.0]),
              (Path.LINETO, [(self.gap - trunklength / 2.0) / 2.0,
                             -gain / 2.0]),
              (Path.LINETO, [(self.gap - trunklength / 2.0),
                             -gain / 2.0])]
    lrpath = [(Path.LINETO, [(trunklength / 2.0 - self.gap),  # Lower right
                             loss / 2.0])]
    ulpath = [(Path.LINETO, [self.gap - trunklength / 2.0,  # Upper left
                             gain / 2.0])]

    # Add the subpaths and assign the locations of the tips and labels.
    tips = np.zeros((n, 2))
    label_locations = np.zeros((n, 2))
    # Add the top-side inputs and outputs from the middle outwards.
    for i, (angle, is_input, spec) in enumerate(zip(
          angles, are_inputs, list(zip(scaled_flows, pathlengths)))):
        if angle == DOWN and is_input:
            tips[i, :], label_locations[i, :] = self._add_input(
                ulpath, angle, *spec)
        elif angle == UP and is_input is False:
            tips[i, :], label_locations[i, :] = self._add_output(
                urpath, angle, *spec)
    # Add the bottom-side inputs and outputs from the middle outwards.
    for i, (angle, is_input, spec) in enumerate(reversed(list(zip(
          angles, are_inputs, list(zip(scaled_flows, pathlengths)))))):
        if angle == UP and is_input:
            tip, label_location = self._add_input(llpath, angle, *spec)
            tips[n - i - 1, :] = tip
            label_locations[n - i - 1, :] = label_location
        elif angle == DOWN and is_input is False:
            tip, label_location = self._add_output(lrpath, angle, *spec)
            tips[n - i - 1, :] = tip
            label_locations[n - i - 1, :] = label_location
    # Add the left-side inputs from the bottom upwards.
    has_left_input = False
    for i, (angle, is_input, spec) in enumerate(reversed(list(zip(
          angles, are_inputs, list(zip(scaled_flows, pathlengths)))))):
        if angle == RIGHT and is_input:
            if not has_left_input:
                # Make sure the lower path extends
                # at least as far as the upper one.
                if llpath[-1][1][0] > ulpath[-1][1][0]:
                    llpath.append((Path.LINETO, [ulpath[-1][1][0],
                                                 llpath[-1][1][1]]))
                has_left_input = True
            tip, label_location = self._add_input(llpath, angle, *spec)
            tips[n - i - 1, :] = tip
            label_locations[n - i - 1, :] = label_location
    # Add the right-side outputs from the top downwards.
    has_right_output = False
    for i, (angle, is_input, spec) in enumerate(zip(
          angles, are_inputs, list(zip(scaled_flows, pathlengths)))):
        if angle == RIGHT and is_input is False:
            if not has_right_output:
                # Make sure the upper path extends
                # at least as far as the lower one.
                if urpath[-1][1][0] < lrpath[-1][1][0]:
                    urpath.append((Path.LINETO, [lrpath[-1][1][0],
                                                 urpath[-1][1][1]]))
                has_right_output = True
            tips[i, :], label_locations[i, :] = self._add_output(
                urpath, angle, *spec)
    # Trim any hanging vertices.
    if not has_left_input:
        ulpath.pop()
        llpath.pop()
    if not has_right_output:
        lrpath.pop()
        urpath.pop()

    # Concatenate the subpaths in the correct order (clockwise from top).
    path = (urpath + self._revert(lrpath) + llpath + self._revert(ulpath) +
            [(Path.CLOSEPOLY, urpath[0][1])])

    # Create a patch with the Sankey outline.
    codes, vertices = zip(*path)
    vertices = np.array(vertices)

    def _get_angle(a, r):
        if a is None:
            return None
        else:
            return a + r

    if prior is None:
        if rotation != 0:  # By default, none of this is needed.
            angles = [_get_angle(angle, rotation) for angle in angles]
            rotate = Affine2D().rotate_deg(rotation * 90).transform_affine
            tips = rotate(tips)
            label_locations = rotate(label_locations)
            vertices = rotate(vertices)
        text = self.ax.text(0, 0, s=patchlabel, ha='center', va='center')
    else:
        rotation = (self.diagrams[prior].angles[connect[0]] -
                    angles[connect[1]])
        angles = [_get_angle(angle, rotation) for angle in angles]
        rotate = Affine2D().rotate_deg(rotation * 90).transform_affine
        tips = rotate(tips)
        offset = self.diagrams[prior].tips[connect[0]] - tips[connect[1]]
        translate = Affine2D().translate(*offset).transform_affine
        tips = translate(tips)
        label_locations = translate(rotate(label_locations))
        vertices = translate(rotate(vertices))
        kwds = dict(s=patchlabel, ha='center', va='center')
        text = self.ax.text(*offset, **kwds)
    if mpl.rcParams['_internal.classic_mode']:
        fc = kwargs.pop('fc', kwargs.pop('facecolor', '#bfd1d4'))
        lw = kwargs.pop('lw', kwargs.pop('linewidth', 0.5))
    else:
        fc = kwargs.pop('fc', kwargs.pop('facecolor', None))
        lw = kwargs.pop('lw', kwargs.pop('linewidth', None))
    if fc is None:
        fc = self.ax._get_patches_for_fill.get_next_color()
    patch = PathPatch(Path(vertices, codes), fc=fc, lw=lw, **kwargs)
    self.ax.add_patch(patch)

    # Add the path labels.
    texts = []
    for number, angle, label, location in zip(flows, angles, labels,
                                              label_locations):
        if label is None or angle is None:
            label = ''
        elif self.unit is not None:
            if isinstance(self.format, str):
                quantity = self.format % abs(number) + self.unit
            elif callable(self.format):
                quantity = self.format(number)
            else:
                raise TypeError(
                    'format must be callable or a format string')
            if label != '':
                label += "\n"
            label += quantity
        texts.append(self.ax.text(x=location[0], y=location[1],
                                  s=label,
                                  ha='center', va='center'))
    # Text objects are placed even they are empty (as long as the magnitude
    # of the corresponding flow is larger than the tolerance) in case the
    # user wants to provide labels later.

    # Expand the size of the diagram if necessary.
    self.extent = (min(np.min(vertices[:, 0]),
                       np.min(label_locations[:, 0]),
                       self.extent[0]),
                   max(np.max(vertices[:, 0]),
                       np.max(label_locations[:, 0]),
                       self.extent[1]),
                   min(np.min(vertices[:, 1]),
                       np.min(label_locations[:, 1]),
                       self.extent[2]),
                   max(np.max(vertices[:, 1]),
                       np.max(label_locations[:, 1]),
                       self.extent[3]))
    # Include both vertices _and_ label locations in the extents; there are
    # where either could determine the margins (e.g., arrow shoulders).

    # Add this diagram as a subdiagram.
    self.diagrams.append(
        SimpleNamespace(patch=patch, flows=flows, angles=angles, tips=tips,
                        text=text, texts=texts))

    # Allow a daisy-chained call structure (see docstring for the class).
    return self


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/sphinxext/plot_directive.py
# Line: 603

def render_figures(code, code_path, output_dir, output_base, context,
                   function_name, config, context_reset=False,
                   close_figs=False,
                   code_includes=None):
    """
    Run a pyplot script and save the images in *output_dir*.

    Save the images under *output_dir* with file names derived from
    *output_base*
    """

    if function_name is not None:
        output_base = f'{output_base}_{function_name}'
    formats = get_plot_formats(config)

    # Try to determine if all images already exist

    is_doctest, code_pieces = _split_code_at_show(code, function_name)
    # Look for single-figure output files first
    img = ImageFile(output_base, output_dir)
    for format, dpi in formats:
        if context or out_of_date(code_path, img.filename(format),
                                  includes=code_includes):
            all_exists = False
            break
        img.formats.append(format)
    else:
        all_exists = True

    if all_exists:
        return [(code, [img])]

    # Then look for multi-figure output files
    results = []
    for i, code_piece in enumerate(code_pieces):
        images = []
        for j in itertools.count():
            if len(code_pieces) > 1:
                img = ImageFile('%s_%02d_%02d' % (output_base, i, j),
                                output_dir)
            else:
                img = ImageFile('%s_%02d' % (output_base, j), output_dir)
            for fmt, dpi in formats:
                if context or out_of_date(code_path, img.filename(fmt),
                                          includes=code_includes):
                    all_exists = False
                    break
                img.formats.append(fmt)

            # assume that if we have one, we have them all
            if not all_exists:
                all_exists = (j > 0)
                break
            images.append(img)
        if not all_exists:
            break
        results.append((code_piece, images))
    else:
        all_exists = True

    if all_exists:
        return results

    # We didn't find the files, so build them

    results = []
    ns = plot_context if context else {}

    if context_reset:
        clear_state(config.plot_rcparams)
        plot_context.clear()

    close_figs = not context or close_figs

    for i, code_piece in enumerate(code_pieces):

        if not context or config.plot_apply_rcparams:
            clear_state(config.plot_rcparams, close_figs)
        elif close_figs:
            plt.close('all')

        _run_code(doctest.script_from_examples(code_piece) if is_doctest
                  else code_piece,
                  code_path, ns, function_name)

        images = []
        fig_managers = _pylab_helpers.Gcf.get_all_fig_managers()
        for j, figman in enumerate(fig_managers):
            if len(fig_managers) == 1 and len(code_pieces) == 1:
                img = ImageFile(output_base, output_dir)
            elif len(code_pieces) == 1:
                img = ImageFile("%s_%02d" % (output_base, j), output_dir)
            else:
                img = ImageFile("%s_%02d_%02d" % (output_base, i, j),
                                output_dir)
            images.append(img)

            for fmt, dpi in formats:
                try:
                    figman.canvas.figure.savefig(img.filename(fmt), dpi=dpi)
                    if fmt == formats[0][0] and config.plot_srcset:
                        # save a 2x, 3x etc version of the default...
                        srcset = _parse_srcset(config.plot_srcset)
                        for mult, suffix in srcset.items():
                            fm = f'{suffix}.{fmt}'
                            img.formats.append(fm)
                            figman.canvas.figure.savefig(img.filename(fm),
                                                         dpi=int(dpi * mult))
                except Exception as err:
                    raise PlotError(traceback.format_exc()) from err
                img.formats.append(fmt)

        results.append((code_piece, images))

    if not context or config.plot_apply_rcparams:
        clear_state(config.plot_rcparams, close=not context)

    return results



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/sphinxext/mathmpl.py
# Line: 95

def math_role(role, rawtext, text, lineno, inliner,
              options={}, content=[]):
    i = rawtext.find('`')
    latex = rawtext[i+1:-1]
    node = latex_math(rawtext)
    node['latex'] = latex
    node['fontset'] = options.get('fontset', 'cm')
    node['fontsize'] = options.get('fontsize',
                                   setup.app.config.mathmpl_fontsize)
    return [node], []

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/sphinxext/roles.py
# Line: 81

def _rcparam_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """
    Sphinx role ``:rc:`` to highlight and link ``rcParams`` entries.

    Usage: Give the desired ``rcParams`` key as parameter.

    :code:`:rc:`figure.dpi`` will render as: :rc:`figure.dpi`
    """
    # Generate a pending cross-reference so that Sphinx will ensure this link
    # isn't broken at some point in the future.
    title = f'rcParams["{text}"]'
    target = 'matplotlibrc-sample'
    ref_nodes, messages = inliner.interpreted(title, f'{title} <{target}>',
                                              'ref', lineno)

    qr = _QueryReference(rawtext, highlight=text)
    qr += ref_nodes
    node_list = [qr]

    # The default backend would be printed as "agg", but that's not correct (as
    # the default is actually determined by fallback).
    if text in rcParamsDefault and text != "backend":
        node_list.extend([
            nodes.Text(' (default: '),
            nodes.literal('', repr(rcParamsDefault[text])),
            nodes.Text(')'),
            ])

    return node_list, messages



# ==================================================
# Line: 112

def _mpltype_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """
    Sphinx role ``:mpltype:`` for custom matplotlib types.

    In Matplotlib, there are a number of type-like concepts that do not have a
    direct type representation; example: color. This role allows to properly
    highlight them in the docs and link to their definition.

    Currently supported values:

    - :code:`:mpltype:`color`` will render as: :mpltype:`color`

    """
    mpltype = text
    type_to_link_target = {
        'color': 'colors_def',
        'hatch': 'hatch_def',
    }
    if mpltype not in type_to_link_target:
        raise ValueError(f"Unknown mpltype: {mpltype!r}")

    node_list, messages = inliner.interpreted(
        mpltype, f'{mpltype} <{type_to_link_target[mpltype]}>', 'ref', lineno)
    return node_list, messages



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/widgets.py
# Line: 167

def __init__(self, ax, label, image=None,
             color='0.85', hovercolor='0.95', *, useblit=True):
    """
    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        The `~.axes.Axes` instance the button will be placed into.
    label : str
        The button text.
    image : array-like or PIL Image
        The image to place in the button, if not *None*.  The parameter is
        directly forwarded to `~.axes.Axes.imshow`.
    color : :mpltype:`color`
        The color of the button when not activated.
    hovercolor : :mpltype:`color`
        The color of the button when the mouse is over it.
    useblit : bool, default: True
        Use blitting for faster drawing if supported by the backend.
        See the tutorial :ref:`blitting` for details.

        .. versionadded:: 3.7
    """
    super().__init__(ax)

    if image is not None:
        ax.imshow(image)
    self.label = ax.text(0.5, 0.5, label,
                         verticalalignment='center',
                         horizontalalignment='center',
                         transform=ax.transAxes)

    self._useblit = useblit and self.canvas.supports_blit

    self._observers = cbook.CallbackRegistry(signals=["clicked"])

    self.connect_event('button_press_event', self._click)
    self.connect_event('button_release_event', self._release)
    self.connect_event('motion_notify_event', self._motion)
    ax.set_navigate(False)
    ax.set_facecolor(color)
    ax.set_xticks([])
    ax.set_yticks([])
    self.color = color
    self.hovercolor = hovercolor


# ==================================================
# Line: 258

def __init__(self, ax, orientation, closedmin, closedmax,
             valmin, valmax, valfmt, dragging, valstep):
    if ax.name == '3d':
        raise ValueError('Sliders cannot be added to 3D Axes')

    super().__init__(ax)
    _api.check_in_list(['horizontal', 'vertical'], orientation=orientation)

    self.orientation = orientation
    self.closedmin = closedmin
    self.closedmax = closedmax
    self.valmin = valmin
    self.valmax = valmax
    self.valstep = valstep
    self.drag_active = False
    self.valfmt = valfmt

    if orientation == "vertical":
        ax.set_ylim((valmin, valmax))
        axis = ax.yaxis
    else:
        ax.set_xlim((valmin, valmax))
        axis = ax.xaxis

    self._fmt = axis.get_major_formatter()
    if not isinstance(self._fmt, ticker.ScalarFormatter):
        self._fmt = ticker.ScalarFormatter()
        self._fmt.set_axis(axis)
    self._fmt.set_useOffset(False)  # No additive offset.
    self._fmt.set_useMathText(True)  # x sign before multiplicative offset.

    ax.set_axis_off()
    ax.set_navigate(False)

    self.connect_event("button_press_event", self._update)
    self.connect_event("button_release_event", self._update)
    if dragging:
        self.connect_event("motion_notify_event", self._update)
    self._observers = cbook.CallbackRegistry(signals=["changed"])


# ==================================================
# Line: 343

def __init__(self, ax, label, valmin, valmax, *, valinit=0.5, valfmt=None,
             closedmin=True, closedmax=True, slidermin=None,
             slidermax=None, dragging=True, valstep=None,
             orientation='horizontal', initcolor='r',
             track_color='lightgrey', handle_style=None, **kwargs):
    """
    Parameters
    ----------
    ax : Axes
        The Axes to put the slider in.

    label : str
        Slider label.

    valmin : float
        The minimum value of the slider.

    valmax : float
        The maximum value of the slider.

    valinit : float, default: 0.5
        The slider initial position.

    valfmt : str, default: None
        %-format string used to format the slider value.  If None, a
        `.ScalarFormatter` is used instead.

    closedmin : bool, default: True
        Whether the slider interval is closed on the bottom.

    closedmax : bool, default: True
        Whether the slider interval is closed on the top.

    slidermin : Slider, default: None
        Do not allow the current slider to have a value less than
        the value of the Slider *slidermin*.

    slidermax : Slider, default: None
        Do not allow the current slider to have a value greater than
        the value of the Slider *slidermax*.

    dragging : bool, default: True
        If True the slider can be dragged by the mouse.

    valstep : float or array-like, default: None
        If a float, the slider will snap to multiples of *valstep*.
        If an array the slider will snap to the values in the array.

    orientation : {'horizontal', 'vertical'}, default: 'horizontal'
        The orientation of the slider.

    initcolor : :mpltype:`color`, default: 'r'
        The color of the line at the *valinit* position. Set to ``'none'``
        for no line.

    track_color : :mpltype:`color`, default: 'lightgrey'
        The color of the background track. The track is accessible for
        further styling via the *track* attribute.

    handle_style : dict
        Properties of the slider handle. Default values are

        ========= ===== ======= ========================================
        Key       Value Default Description
        ========= ===== ======= ========================================
        facecolor color 'white' The facecolor of the slider handle.
        edgecolor color '.75'   The edgecolor of the slider handle.
        size      int   10      The size of the slider handle in points.
        ========= ===== ======= ========================================

        Other values will be transformed as marker{foo} and passed to the
        `~.Line2D` constructor. e.g. ``handle_style = {'style'='x'}`` will
        result in ``markerstyle = 'x'``.

    Notes
    -----
    Additional kwargs are passed on to ``self.poly`` which is the
    `~matplotlib.patches.Rectangle` that draws the slider knob.  See the
    `.Rectangle` documentation for valid property names (``facecolor``,
    ``edgecolor``, ``alpha``, etc.).
    """
    super().__init__(ax, orientation, closedmin, closedmax,
                     valmin, valmax, valfmt, dragging, valstep)

    if slidermin is not None and not hasattr(slidermin, 'val'):
        raise ValueError(
            f"Argument slidermin ({type(slidermin)}) has no 'val'")
    if slidermax is not None and not hasattr(slidermax, 'val'):
        raise ValueError(
            f"Argument slidermax ({type(slidermax)}) has no 'val'")
    self.slidermin = slidermin
    self.slidermax = slidermax
    valinit = self._value_in_bounds(valinit)
    if valinit is None:
        valinit = valmin
    self.val = valinit
    self.valinit = valinit

    defaults = {'facecolor': 'white', 'edgecolor': '.75', 'size': 10}
    handle_style = {} if handle_style is None else handle_style
    marker_props = {
        f'marker{k}': v for k, v in {**defaults, **handle_style}.items()
    }

    if orientation == 'vertical':
        self.track = Rectangle(
            (.25, 0), .5, 1,
            transform=ax.transAxes,
            facecolor=track_color
        )
        ax.add_patch(self.track)
        self.poly = ax.axhspan(valmin, valinit, .25, .75, **kwargs)
        # Drawing a longer line and clipping it to the track avoids
        # pixelation-related asymmetries.
        self.hline = ax.axhline(valinit, 0, 1, color=initcolor, lw=1,
                                clip_path=TransformedPatchPath(self.track))
        handleXY = [[0.5], [valinit]]
    else:
        self.track = Rectangle(
            (0, .25), 1, .5,
            transform=ax.transAxes,
            facecolor=track_color
        )
        ax.add_patch(self.track)
        self.poly = ax.axvspan(valmin, valinit, .25, .75, **kwargs)
        self.vline = ax.axvline(valinit, 0, 1, color=initcolor, lw=1,
                                clip_path=TransformedPatchPath(self.track))
        handleXY = [[valinit], [0.5]]
    self._handle, = ax.plot(
        *handleXY,
        "o",
        **marker_props,
        clip_on=False
    )

    if orientation == 'vertical':
        self.label = ax.text(0.5, 1.02, label, transform=ax.transAxes,
                             verticalalignment='bottom',
                             horizontalalignment='center')

        self.valtext = ax.text(0.5, -0.02, self._format(valinit),
                               transform=ax.transAxes,
                               verticalalignment='top',
                               horizontalalignment='center')
    else:
        self.label = ax.text(-0.02, 0.5, label, transform=ax.transAxes,
                             verticalalignment='center',
                             horizontalalignment='right')

        self.valtext = ax.text(1.02, 0.5, self._format(valinit),
                               transform=ax.transAxes,
                               verticalalignment='center',
                               horizontalalignment='left')

    self.set_val(valinit)


# ==================================================
# Line: 610

def __init__(
    self,
    ax,
    label,
    valmin,
    valmax,
    *,
    valinit=None,
    valfmt=None,
    closedmin=True,
    closedmax=True,
    dragging=True,
    valstep=None,
    orientation="horizontal",
    track_color='lightgrey',
    handle_style=None,
    **kwargs,

# ==================================================
# Line: 993

def __init__(self, ax, labels, actives=None, *, useblit=True,
             label_props=None, frame_props=None, check_props=None):
    """
    Add check buttons to `~.axes.Axes` instance *ax*.

    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        The parent Axes for the widget.
    labels : list of str
        The labels of the check buttons.
    actives : list of bool, optional
        The initial check states of the buttons. The list must have the
        same length as *labels*. If not given, all buttons are unchecked.
    useblit : bool, default: True
        Use blitting for faster drawing if supported by the backend.
        See the tutorial :ref:`blitting` for details.

        .. versionadded:: 3.7

    label_props : dict, optional
        Dictionary of `.Text` properties to be used for the labels.

        .. versionadded:: 3.7
    frame_props : dict, optional
        Dictionary of scatter `.Collection` properties to be used for the
        check button frame. Defaults (label font size / 2)**2 size, black
        edgecolor, no facecolor, and 1.0 linewidth.

        .. versionadded:: 3.7
    check_props : dict, optional
        Dictionary of scatter `.Collection` properties to be used for the
        check button check. Defaults to (label font size / 2)**2 size,
        black color, and 1.0 linewidth.

        .. versionadded:: 3.7
    """
    super().__init__(ax)

    _api.check_isinstance((dict, None), label_props=label_props,
                          frame_props=frame_props, check_props=check_props)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_navigate(False)

    if actives is None:
        actives = [False] * len(labels)

    self._useblit = useblit and self.canvas.supports_blit
    self._background = None

    ys = np.linspace(1, 0, len(labels)+2)[1:-1]

    label_props = _expand_text_props(label_props)
    self.labels = [
        ax.text(0.25, y, label, transform=ax.transAxes,
                horizontalalignment="left", verticalalignment="center",
                **props)
        for y, label, props in zip(ys, labels, label_props)]
    text_size = np.array([text.get_fontsize() for text in self.labels]) / 2

    frame_props = {
        's': text_size**2,
        'linewidth': 1,
        **cbook.normalize_kwargs(frame_props, collections.PathCollection),
        'marker': 's',
        'transform': ax.transAxes,
    }
    frame_props.setdefault('facecolor', frame_props.get('color', 'none'))
    frame_props.setdefault('edgecolor', frame_props.pop('color', 'black'))
    self._frames = ax.scatter([0.15] * len(ys), ys, **frame_props)
    check_props = {
        'linewidth': 1,
        's': text_size**2,
        **cbook.normalize_kwargs(check_props, collections.PathCollection),
        'marker': 'x',
        'transform': ax.transAxes,
        'animated': self._useblit,
    }
    check_props.setdefault('facecolor', check_props.pop('color', 'black'))
    self._checks = ax.scatter([0.15] * len(ys), ys, **check_props)
    # The user may have passed custom colours in check_props, so we need to
    # create the checks (above), and modify the visibility after getting
    # whatever the user set.
    self._init_status(actives)

    self.connect_event('button_press_event', self._clicked)
    if self._useblit:
        self.connect_event('draw_event', self._clear)

    self._observers = cbook.CallbackRegistry(signals=["clicked"])


# ==================================================
# Line: 1300

def __init__(self, ax, label, initial='', *,
             color='.95', hovercolor='1', label_pad=.01,
             textalignment="left"):
    """
    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        The `~.axes.Axes` instance the button will be placed into.
    label : str
        Label for this text box.
    initial : str
        Initial value in the text box.
    color : :mpltype:`color`
        The color of the box.
    hovercolor : :mpltype:`color`
        The color of the box when the mouse is over it.
    label_pad : float
        The distance between the label and the right side of the textbox.
    textalignment : {'left', 'center', 'right'}
        The horizontal location of the text.
    """
    super().__init__(ax)

    self._text_position = _api.check_getitem(
        {"left": 0.05, "center": 0.5, "right": 0.95},
        textalignment=textalignment)

    self.label = ax.text(
        -label_pad, 0.5, label, transform=ax.transAxes,
        verticalalignment='center', horizontalalignment='right')

    # TextBox's text object should not parse mathtext at all.
    self.text_disp = self.ax.text(
        self._text_position, 0.5, initial, transform=self.ax.transAxes,
        verticalalignment='center', horizontalalignment=textalignment,
        parse_math=False)

    self._observers = cbook.CallbackRegistry(signals=["change", "submit"])

    ax.set(
        xlim=(0, 1), ylim=(0, 1),  # s.t. cursor appears from first click.
        navigate=False, facecolor=color,
        xticks=[], yticks=[])

    self.cursor_index = 0

    self.cursor = ax.vlines(0, 0, 0, visible=False, color="k", lw=1,
                            transform=mpl.transforms.IdentityTransform())

    self.connect_event('button_press_event', self._click)
    self.connect_event('button_release_event', self._release)
    self.connect_event('motion_notify_event', self._motion)
    self.connect_event('key_press_event', self._keypress)
    self.connect_event('resize_event', self._resize)

    self.color = color
    self.hovercolor = hovercolor

    self.capturekeystrokes = False


# ==================================================
# Line: 1560

def __init__(self, ax, labels, active=0, activecolor=None, *,
             useblit=True, label_props=None, radio_props=None):
    """
    Add radio buttons to an `~.axes.Axes`.

    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        The Axes to add the buttons to.
    labels : list of str
        The button labels.
    active : int
        The index of the initially selected button.
    activecolor : :mpltype:`color`
        The color of the selected button. The default is ``'blue'`` if not
        specified here or in *radio_props*.
    useblit : bool, default: True
        Use blitting for faster drawing if supported by the backend.
        See the tutorial :ref:`blitting` for details.

        .. versionadded:: 3.7

    label_props : dict or list of dict, optional
        Dictionary of `.Text` properties to be used for the labels.

        .. versionadded:: 3.7
    radio_props : dict, optional
        Dictionary of scatter `.Collection` properties to be used for the
        radio buttons. Defaults to (label font size / 2)**2 size, black
        edgecolor, and *activecolor* facecolor (when active).

        .. note::
            If a facecolor is supplied in *radio_props*, it will override
            *activecolor*. This may be used to provide an active color per
            button.

        .. versionadded:: 3.7
    """
    super().__init__(ax)

    _api.check_isinstance((dict, None), label_props=label_props,
                          radio_props=radio_props)

    radio_props = cbook.normalize_kwargs(radio_props,
                                         collections.PathCollection)
    if activecolor is not None:
        if 'facecolor' in radio_props:
            _api.warn_external(
                'Both the *activecolor* parameter and the *facecolor* '
                'key in the *radio_props* parameter has been specified. '
                '*activecolor* will be ignored.')
    else:
        activecolor = 'blue'  # Default.

    self._activecolor = activecolor
    self._initial_active = active
    self.value_selected = labels[active]
    self.index_selected = active

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_navigate(False)

    ys = np.linspace(1, 0, len(labels) + 2)[1:-1]

    self._useblit = useblit and self.canvas.supports_blit
    self._background = None

    label_props = _expand_text_props(label_props)
    self.labels = [
        ax.text(0.25, y, label, transform=ax.transAxes,
                horizontalalignment="left", verticalalignment="center",
                **props)
        for y, label, props in zip(ys, labels, label_props)]
    text_size = np.array([text.get_fontsize() for text in self.labels]) / 2

    radio_props = {
        's': text_size**2,
        **radio_props,
        'marker': 'o',
        'transform': ax.transAxes,
        'animated': self._useblit,
    }
    radio_props.setdefault('edgecolor', radio_props.get('color', 'black'))
    radio_props.setdefault('facecolor',
                           radio_props.pop('color', activecolor))
    self._buttons = ax.scatter([.15] * len(ys), ys, **radio_props)
    # The user may have passed custom colours in radio_props, so we need to
    # create the radios, and modify the visibility after getting whatever
    # the user set.
    self._active_colors = self._buttons.get_facecolor()
    if len(self._active_colors) == 1:
        self._active_colors = np.repeat(self._active_colors, len(labels),
                                        axis=0)
    self._buttons.set_facecolor(
        [activecolor if i == active else "none"
         for i, activecolor in enumerate(self._active_colors)])

    self.connect_event('button_press_event', self._clicked)
    if self._useblit:
        self.connect_event('draw_event', self._clear)

    self._observers = cbook.CallbackRegistry(signals=["clicked"])


# ==================================================
# Line: 2094

def __init__(self, ax, onselect=None, useblit=False, button=None,
             state_modifier_keys=None, use_data_coordinates=False):
    super().__init__(ax)

    self._visible = True
    if onselect is None:
        self.onselect = lambda *args: None
    else:
        self.onselect = onselect
    self.useblit = useblit and self.canvas.supports_blit
    self.connect_default_events()

    self._state_modifier_keys = dict(move=' ', clear='escape',
                                     square='shift', center='control',
                                     rotate='r')
    self._state_modifier_keys.update(state_modifier_keys or {})
    self._use_data_coordinates = use_data_coordinates

    self.background = None

    if isinstance(button, Integral):
        self.validButtons = [button]
    else:
        self.validButtons = button

    # Set to True when a selection is completed, otherwise is False
    self._selection_completed = False

    # will save the data (position at mouseclick)
    self._eventpress = None
    # will save the data (pos. at mouserelease)
    self._eventrelease = None
    self._prev_event = None
    self._state = set()


# ==================================================
# Line: 2529

def __init__(self, ax, onselect, direction, *, minspan=0, useblit=False,
             props=None, onmove_callback=None, interactive=False,
             button=None, handle_props=None, grab_range=10,
             state_modifier_keys=None, drag_from_anywhere=False,
             ignore_event_outside=False, snap_values=None):

    if state_modifier_keys is None:
        state_modifier_keys = dict(clear='escape',
                                   square='not-applicable',
                                   center='not-applicable',
                                   rotate='not-applicable')
    super().__init__(ax, onselect, useblit=useblit, button=button,
                     state_modifier_keys=state_modifier_keys)

    if props is None:
        props = dict(facecolor='red', alpha=0.5)

    props['animated'] = self.useblit

    self.direction = direction
    self._extents_on_press = None
    self.snap_values = snap_values

    self.onmove_callback = onmove_callback
    self.minspan = minspan

    self.grab_range = grab_range
    self._interactive = interactive
    self._edge_handles = None
    self.drag_from_anywhere = drag_from_anywhere
    self.ignore_event_outside = ignore_event_outside

    self.new_axes(ax, _props=props, _init=True)

    # Setup handles
    self._handle_props = {
        'color': props.get('facecolor', 'r'),
        **cbook.normalize_kwargs(handle_props, Line2D)}

    if self._interactive:
        self._edge_order = ['min', 'max']
        self._setup_edge_handles(self._handle_props)

    self._active_handle = None


# ==================================================
# Line: 2990

def __init__(self, ax, x, y, *, marker='o', marker_props=None, useblit=True):
    self.ax = ax
    props = {'marker': marker, 'markersize': 7, 'markerfacecolor': 'w',
             'linestyle': 'none', 'alpha': 0.5, 'visible': False,
             'label': '_nolegend_',
             **cbook.normalize_kwargs(marker_props, Line2D._alias_map)}
    self._markers = Line2D(x, y, animated=useblit, **props)
    self.ax.add_line(self._markers)


# ==================================================
# Line: 3155

def __init__(self, ax, onselect=None, *, minspanx=0,
             minspany=0, useblit=False,
             props=None, spancoords='data', button=None, grab_range=10,
             handle_props=None, interactive=False,
             state_modifier_keys=None, drag_from_anywhere=False,
             ignore_event_outside=False, use_data_coordinates=False):
    super().__init__(ax, onselect, useblit=useblit, button=button,
                     state_modifier_keys=state_modifier_keys,
                     use_data_coordinates=use_data_coordinates)

    self._interactive = interactive
    self.drag_from_anywhere = drag_from_anywhere
    self.ignore_event_outside = ignore_event_outside
    self._rotation = 0.0
    self._aspect_ratio_correction = 1.0

    # State to allow the option of an interactive selector that can't be
    # interactively drawn. This is used in PolygonSelector as an
    # interactive bounding box to allow the polygon to be easily resized
    self._allow_creation = True

    if props is None:
        props = dict(facecolor='red', edgecolor='black',
                     alpha=0.2, fill=True)
    props = {**props, 'animated': self.useblit}
    self._visible = props.pop('visible', self._visible)
    to_draw = self._init_shape(**props)
    self.ax.add_patch(to_draw)

    self._selection_artist = to_draw
    self._set_aspect_ratio_correction()

    self.minspanx = minspanx
    self.minspany = minspany

    _api.check_in_list(['data', 'pixels'], spancoords=spancoords)
    self.spancoords = spancoords

    self.grab_range = grab_range

    if self._interactive:
        self._handle_props = {
            'markeredgecolor': (props or {}).get('edgecolor', 'black'),
            **cbook.normalize_kwargs(handle_props, Line2D)}

        self._corner_order = ['SW', 'SE', 'NE', 'NW']
        xc, yc = self.corners
        self._corner_handles = ToolHandles(self.ax, xc, yc,
                                           marker_props=self._handle_props,
                                           useblit=self.useblit)

        self._edge_order = ['W', 'S', 'E', 'N']
        xe, ye = self.edge_centers
        self._edge_handles = ToolHandles(self.ax, xe, ye, marker='s',
                                         marker_props=self._handle_props,
                                         useblit=self.useblit)

        xc, yc = self.center
        self._center_handle = ToolHandles(self.ax, [xc], [yc], marker='s',
                                          marker_props=self._handle_props,
                                          useblit=self.useblit)

        self._active_handle = None

    self._extents_on_press = None


# ==================================================
# Line: 3803

def __init__(self, ax, onselect=None, *, useblit=False,
             props=None, handle_props=None, grab_range=10,
             draw_bounding_box=False, box_handle_props=None,
             box_props=None):
    # The state modifiers 'move', 'square', and 'center' are expected by
    # _SelectorWidget but are not supported by PolygonSelector
    # Note: could not use the existing 'move' state modifier in-place of
    # 'move_all' because _SelectorWidget automatically discards 'move'
    # from the state on button release.
    state_modifier_keys = dict(clear='escape', move_vertex='control',
                               move_all='shift', move='not-applicable',
                               square='not-applicable',
                               center='not-applicable',
                               rotate='not-applicable')
    super().__init__(ax, onselect, useblit=useblit,
                     state_modifier_keys=state_modifier_keys)

    self._xys = [(0, 0)]

    if props is None:
        props = dict(color='k', linestyle='-', linewidth=2, alpha=0.5)
    props = {**props, 'animated': self.useblit}
    self._selection_artist = line = Line2D([], [], **props)
    self.ax.add_line(line)

    if handle_props is None:
        handle_props = dict(markeredgecolor='k',
                            markerfacecolor=props.get('color', 'k'))
    self._handle_props = handle_props
    self._polygon_handles = ToolHandles(self.ax, [], [],
                                        useblit=self.useblit,
                                        marker_props=self._handle_props)

    self._active_handle_idx = -1
    self.grab_range = grab_range

    self.set_visible(True)
    self._draw_box = draw_bounding_box
    self._box = None

    if box_handle_props is None:
        box_handle_props = {}
    self._box_handle_props = self._handle_props.update(box_handle_props)
    self._box_props = box_props


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/font_manager.py
# Line: 657

def __init__(self, family=None, style=None, variant=None, weight=None,
             stretch=None, size=None,
             fname=None,  # if set, it's a hardcoded filename to use
             math_fontfamily=None):
    self.set_family(family)
    self.set_style(style)
    self.set_variant(variant)
    self.set_weight(weight)
    self.set_stretch(stretch)
    self.set_file(fname)
    self.set_size(size)
    self.set_math_fontfamily(math_fontfamily)
    # Treat family as a fontconfig pattern if it is the only parameter
    # provided.  Even in that case, call the other setters first to set
    # attributes not specified by the pattern to the rcParams defaults.
    if (isinstance(family, str)
            and style is None and variant is None and weight is None
            and stretch is None and size is None and fname is None):
        self.set_fontconfig_pattern(family)


# ==================================================
# Line: 1448

def _findfont_cached(self, prop, fontext, directory, fallback_to_default,
                     rebuild_if_missing, rc_params):

    prop = FontProperties._from_any(prop)

    fname = prop.get_file()
    if fname is not None:
        return fname

    if fontext == 'afm':
        fontlist = self.afmlist
    else:
        fontlist = self.ttflist

    best_score = 1e64
    best_font = None

    _log.debug('findfont: Matching %s.', prop)
    for font in fontlist:
        if (directory is not None and
                Path(directory) not in Path(font.fname).parents):
            continue
        # Matching family should have top priority, so multiply it by 10.
        score = (self.score_family(prop.get_family(), font.name) * 10
                 + self.score_style(prop.get_style(), font.style)
                 + self.score_variant(prop.get_variant(), font.variant)
                 + self.score_weight(prop.get_weight(), font.weight)
                 + self.score_stretch(prop.get_stretch(), font.stretch)
                 + self.score_size(prop.get_size(), font.size))
        _log.debug('findfont: score(%s) = %s', font, score)
        if score < best_score:
            best_score = score
            best_font = font
        if score == 0:
            break

    if best_font is None or best_score >= 10.0:
        if fallback_to_default:
            _log.warning(
                'findfont: Font family %s not found. Falling back to %s.',
                prop.get_family(), self.defaultFamily[fontext])
            for family in map(str.lower, prop.get_family()):
                if family in font_family_aliases:
                    _log.warning(
                        "findfont: Generic family %r not found because "
                        "none of the following families were found: %s",
                        family, ", ".join(self._expand_aliases(family)))
            default_prop = prop.copy()
            default_prop.set_family(self.defaultFamily[fontext])
            return self.findfont(default_prop, fontext, directory,
                                 fallback_to_default=False)
        else:
            # This return instead of raise is intentional, as we wish to
            # cache that it was not found, which will not occur if it was
            # actually raised.
            return cbook._ExceptionInfo(
                ValueError,
                f"Failed to find font {prop}, and fallback to the default font was "
                f"disabled"
            )
    else:
        _log.debug('findfont: Matching %s to %s (%r) with score of %f.',
                   prop, best_font.name, best_font.fname, best_score)
        result = best_font.fname

    if not os.path.isfile(result):
        if rebuild_if_missing:
            _log.info(
                'findfont: Found a missing font file.  Rebuilding cache.')
            new_fm = _load_fontmanager(try_read_cache=False)
            # Replace self by the new fontmanager, because users may have
            # a reference to this specific instance.
            # TODO: _load_fontmanager should really be (used by) a method
            # modifying the instance in place.
            vars(self).update(vars(new_fm))
            return self.findfont(
                prop, fontext, directory, rebuild_if_missing=False)
        else:
            # This return instead of raise is intentional, as we wish to
            # cache that it was not found, which will not occur if it was
            # actually raised.
            return cbook._ExceptionInfo(ValueError, "No valid font could be found")

    return _cached_realpath(result)



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/axes/_base.py
# Line: 601

def __init__(self, fig,
             *args,
             facecolor=None,  # defaults to rc axes.facecolor
             frameon=True,
             sharex=None,  # use Axes instance's xaxis info
             sharey=None,  # use Axes instance's yaxis info
             label='',
             xscale=None,
             yscale=None,
             box_aspect=None,
             forward_navigation_events="auto",
             **kwargs
             ):
    """
    Build an Axes in a figure.

    Parameters
    ----------
    fig : `~matplotlib.figure.Figure`
        The Axes is built in the `.Figure` *fig*.

    *args
        ``*args`` can be a single ``(left, bottom, width, height)``
        rectangle or a single `.Bbox`.  This specifies the rectangle (in
        figure coordinates) where the Axes is positioned.

        ``*args`` can also consist of three numbers or a single three-digit
        number; in the latter case, the digits are considered as
        independent numbers.  The numbers are interpreted as ``(nrows,
        ncols, index)``: ``(nrows, ncols)`` specifies the size of an array
        of subplots, and ``index`` is the 1-based index of the subplot
        being created.  Finally, ``*args`` can also directly be a
        `.SubplotSpec` instance.

    sharex, sharey : `~matplotlib.axes.Axes`, optional
        The x- or y-`~.matplotlib.axis` is shared with the x- or y-axis in
        the input `~.axes.Axes`.  Note that it is not possible to unshare
        axes.

    frameon : bool, default: True
        Whether the Axes frame is visible.

    box_aspect : float, optional
        Set a fixed aspect for the Axes box, i.e. the ratio of height to
        width. See `~.axes.Axes.set_box_aspect` for details.

    forward_navigation_events : bool or "auto", default: "auto"
        Control whether pan/zoom events are passed through to Axes below
        this one. "auto" is *True* for axes with an invisible patch and
        *False* otherwise.

    **kwargs
        Other optional keyword arguments:

        %(Axes:kwdoc)s

    Returns
    -------
    `~.axes.Axes`
        The new `~.axes.Axes` object.
    """

    super().__init__()
    if "rect" in kwargs:
        if args:
            raise TypeError(
                "'rect' cannot be used together with positional arguments")
        rect = kwargs.pop("rect")
        _api.check_isinstance((mtransforms.Bbox, Iterable), rect=rect)
        args = (rect,)
    subplotspec = None
    if len(args) == 1 and isinstance(args[0], mtransforms.Bbox):
        self._position = args[0].frozen()
    elif len(args) == 1 and np.iterable(args[0]):
        self._position = mtransforms.Bbox.from_bounds(*args[0])
    else:
        self._position = self._originalPosition = mtransforms.Bbox.unit()
        subplotspec = SubplotSpec._from_subplot_args(fig, args)
    if self._position.width < 0 or self._position.height < 0:
        raise ValueError('Width and height specified must be non-negative')
    self._originalPosition = self._position.frozen()
    self.axes = self
    self._aspect = 'auto'
    self._adjustable = 'box'
    self._anchor = 'C'
    self._stale_viewlims = dict.fromkeys(self._axis_names, False)
    self._forward_navigation_events = forward_navigation_events
    self._sharex = sharex
    self._sharey = sharey
    self.set_label(label)
    self.set_figure(fig)
    # The subplotspec needs to be set after the figure (so that
    # figure-level subplotpars are taken into account), but the figure
    # needs to be set after self._position is initialized.
    if subplotspec:
        self.set_subplotspec(subplotspec)
    else:
        self._subplotspec = None
    self.set_box_aspect(box_aspect)
    self._axes_locator = None  # Optionally set via update(kwargs).

    self._children = []

    # placeholder for any colorbars added that use this Axes.
    # (see colorbar.py):
    self._colorbars = []
    self.spines = mspines.Spines.from_dict(self._gen_axes_spines())

    self.xaxis = None  # will be populated in _init_axis()
    self.yaxis = None  # will be populated in _init_axis()
    self._init_axis()  # this call may differ for non-sep axes, e.g., polar
    self._axis_map = {
        name: getattr(self, f"{name}axis") for name in self._axis_names
    }  # A mapping of axis names, e.g. 'x', to `Axis` instances.
    self._facecolor = mpl._val_or_rc(facecolor, 'axes.facecolor')
    self._frameon = frameon
    self.set_axisbelow(mpl.rcParams['axes.axisbelow'])

    self._rasterization_zorder = None
    self.clear()

    # funcs used to format x and y - fall back on major formatters
    self.fmt_xdata = None
    self.fmt_ydata = None

    self.set_navigate(True)
    self.set_navigate_mode(None)

    if xscale:
        self.set_xscale(xscale)
    if yscale:
        self.set_yscale(yscale)

    self._internal_update(kwargs)

    for name, axis in self._axis_map.items():
        axis.callbacks._connect_picklable(
            'units', self._unit_change_handler(name))

    rcParams = mpl.rcParams
    self.tick_params(
        top=rcParams['xtick.top'] and rcParams['xtick.minor.top'],
        bottom=rcParams['xtick.bottom'] and rcParams['xtick.minor.bottom'],
        labeltop=(rcParams['xtick.labeltop'] and
                  rcParams['xtick.minor.top']),
        labelbottom=(rcParams['xtick.labelbottom'] and
                     rcParams['xtick.minor.bottom']),
        left=rcParams['ytick.left'] and rcParams['ytick.minor.left'],
        right=rcParams['ytick.right'] and rcParams['ytick.minor.right'],
        labelleft=(rcParams['ytick.labelleft'] and
                   rcParams['ytick.minor.left']),
        labelright=(rcParams['ytick.labelright'] and
                    rcParams['ytick.minor.right']),
        which='minor')

    self.tick_params(
        top=rcParams['xtick.top'] and rcParams['xtick.major.top'],
        bottom=rcParams['xtick.bottom'] and rcParams['xtick.major.bottom'],
        labeltop=(rcParams['xtick.labeltop'] and
                  rcParams['xtick.major.top']),
        labelbottom=(rcParams['xtick.labelbottom'] and
                     rcParams['xtick.major.bottom']),
        left=rcParams['ytick.left'] and rcParams['ytick.major.left'],
        right=rcParams['ytick.right'] and rcParams['ytick.major.right'],
        labelleft=(rcParams['ytick.labelleft'] and
                   rcParams['ytick.major.left']),
        labelright=(rcParams['ytick.labelright'] and
                    rcParams['ytick.major.right']),
        which='major')


# ==================================================
# Line: 2999

def handle_single_axis(
        scale, shared_axes, name, axis, margin, stickies, set_bound):

    if not (scale and axis._get_autoscale_on()):
        return  # nothing to do...

    shared = shared_axes.get_siblings(self)
    # Base autoscaling on finite data limits when there is at least one
    # finite data limit among all the shared_axes and intervals.
    values = [val for ax in shared
              for val in getattr(ax.dataLim, f"interval{name}")
              if np.isfinite(val)]
    if values:
        x0, x1 = (min(values), max(values))
    elif getattr(self._viewLim, f"mutated{name}")():
        # No data, but explicit viewLims already set:
        # in mutatedx or mutatedy.
        return
    else:
        x0, x1 = (-np.inf, np.inf)
    # If x0 and x1 are nonfinite, get default limits from the locator.
    locator = axis.get_major_locator()
    x0, x1 = locator.nonsingular(x0, x1)
    # Find the minimum minpos for use in the margin calculation.
    minimum_minpos = min(
        getattr(ax.dataLim, f"minpos{name}") for ax in shared)

    # Prevent margin addition from crossing a sticky value.  A small
    # tolerance must be added due to floating point issues with
    # streamplot; it is defined relative to x1-x0 but has
    # no absolute term (e.g. "+1e-8") to avoid issues when working with
    # datasets where all values are tiny (less than 1e-8).
    tol = 1e-5 * abs(x1 - x0)
    # Index of largest element < x0 + tol, if any.
    i0 = stickies.searchsorted(x0 + tol) - 1
    x0bound = stickies[i0] if i0 != -1 else None
    # Index of smallest element > x1 - tol, if any.
    i1 = stickies.searchsorted(x1 - tol)
    x1bound = stickies[i1] if i1 != len(stickies) else None

    # Add the margin in figure space and then transform back, to handle
    # non-linear scales.
    transform = axis.get_transform()
    inverse_trans = transform.inverted()
    x0, x1 = axis._scale.limit_range_for_scale(x0, x1, minimum_minpos)
    x0t, x1t = transform.transform([x0, x1])
    delta = (x1t - x0t) * margin
    if not np.isfinite(delta):
        delta = 0  # If a bound isn't finite, set margin to zero.
    x0, x1 = inverse_trans.transform([x0t - delta, x1t + delta])

    # Apply sticky bounds.
    if x0bound is not None:
        x0 = max(x0, x0bound)
    if x1bound is not None:
        x1 = min(x1, x1bound)

    if not self._tight:
        x0, x1 = locator.view_limits(x0, x1)
    set_bound(x0, x1)
    # End of definition of internal function 'handle_single_axis'.


# ==================================================
# Line: 3339

def ticklabel_format(self, *, axis='both', style=None, scilimits=None,
                     useOffset=None, useLocale=None, useMathText=None):
    r"""
    Configure the `.ScalarFormatter` used by default for linear Axes.

    If a parameter is not set, the corresponding property of the formatter
    is left unchanged.

    Parameters
    ----------
    axis : {'x', 'y', 'both'}, default: 'both'
        The axis to configure.  Only major ticks are affected.

    style : {'sci', 'scientific', 'plain'}
        Whether to use scientific notation.
        The formatter default is to use scientific notation.
        'sci' is equivalent to 'scientific'.

    scilimits : pair of ints (m, n)
        Scientific notation is used only for numbers outside the range
        10\ :sup:`m` to 10\ :sup:`n` (and only if the formatter is
        configured to use scientific notation at all).  Use (0, 0) to
        include all numbers.  Use (m, m) where m != 0 to fix the order of
        magnitude to 10\ :sup:`m`.
        The formatter default is :rc:`axes.formatter.limits`.

    useOffset : bool or float
        If True, the offset is calculated as needed.
        If False, no offset is used.
        If a numeric value, it sets the offset.
        The formatter default is :rc:`axes.formatter.useoffset`.

    useLocale : bool
        Whether to format the number using the current locale or using the
        C (English) locale.  This affects e.g. the decimal separator.  The
        formatter default is :rc:`axes.formatter.use_locale`.

    useMathText : bool
        Render the offset and scientific notation in mathtext.
        The formatter default is :rc:`axes.formatter.use_mathtext`.

    Raises
    ------
    AttributeError
        If the current formatter is not a `.ScalarFormatter`.
    """
    if isinstance(style, str):
        style = style.lower()
    axis = axis.lower()
    if scilimits is not None:
        try:
            m, n = scilimits
            m + n + 1  # check that both are numbers
        except (ValueError, TypeError) as err:
            raise ValueError("scilimits must be a sequence of 2 integers"
                             ) from err
    STYLES = {'sci': True, 'scientific': True, 'plain': False, '': None, None: None}
    # The '' option is included for backwards-compatibility.
    is_sci_style = _api.check_getitem(STYLES, style=style)
    axis_map = {**{k: [v] for k, v in self._axis_map.items()},
                'both': list(self._axis_map.values())}
    axises = _api.check_getitem(axis_map, axis=axis)
    try:
        for axis in axises:
            if is_sci_style is not None:
                axis.major.formatter.set_scientific(is_sci_style)
            if scilimits is not None:
                axis.major.formatter.set_powerlimits(scilimits)
            if useOffset is not None:
                axis.major.formatter.set_useOffset(useOffset)
            if useLocale is not None:
                axis.major.formatter.set_useLocale(useLocale)
            if useMathText is not None:
                axis.major.formatter.set_useMathText(useMathText)
    except AttributeError as err:
        raise AttributeError(
            "This method only works with the ScalarFormatter") from err


# ==================================================
# Line: 3747

def set_xlim(self, left=None, right=None, *, emit=True, auto=False,
             xmin=None, xmax=None):
    """
    Set the x-axis view limits.

    Parameters
    ----------
    left : float, optional
        The left xlim in data coordinates. Passing *None* leaves the
        limit unchanged.

        The left and right xlims may also be passed as the tuple
        (*left*, *right*) as the first positional argument (or as
        the *left* keyword argument).

        .. ACCEPTS: (left: float, right: float)

    right : float, optional
        The right xlim in data coordinates. Passing *None* leaves the
        limit unchanged.

    emit : bool, default: True
        Whether to notify observers of limit change.

    auto : bool or None, default: False
        Whether to turn on autoscaling of the x-axis. True turns on,
        False turns off, None leaves unchanged.

    xmin, xmax : float, optional
        They are equivalent to left and right respectively, and it is an
        error to pass both *xmin* and *left* or *xmax* and *right*.

    Returns
    -------
    left, right : (float, float)
        The new x-axis limits in data coordinates.

    See Also
    --------
    get_xlim
    set_xbound, get_xbound
    invert_xaxis, xaxis_inverted

    Notes
    -----
    The *left* value may be greater than the *right* value, in which
    case the x-axis values will decrease from left to right.

    Examples
    --------
    >>> set_xlim(left, right)
    >>> set_xlim((left, right))
    >>> left, right = set_xlim(left, right)

    One limit may be left unchanged.

    >>> set_xlim(right=right_lim)

    Limits may be passed in reverse order to flip the direction of
    the x-axis. For example, suppose *x* represents the number of
    years before present. The x-axis limits might be set like the
    following so 5000 years ago is on the left of the plot and the
    present is on the right.

    >>> set_xlim(5000, 0)
    """
    if right is None and np.iterable(left):
        left, right = left
    if xmin is not None:
        if left is not None:
            raise TypeError("Cannot pass both 'left' and 'xmin'")
        left = xmin
    if xmax is not None:
        if right is not None:
            raise TypeError("Cannot pass both 'right' and 'xmax'")
        right = xmax
    return self.xaxis._set_lim(left, right, emit=emit, auto=auto)


# ==================================================
# Line: 3996

def set_ylim(self, bottom=None, top=None, *, emit=True, auto=False,
             ymin=None, ymax=None):
    """
    Set the y-axis view limits.

    Parameters
    ----------
    bottom : float, optional
        The bottom ylim in data coordinates. Passing *None* leaves the
        limit unchanged.

        The bottom and top ylims may also be passed as the tuple
        (*bottom*, *top*) as the first positional argument (or as
        the *bottom* keyword argument).

        .. ACCEPTS: (bottom: float, top: float)

    top : float, optional
        The top ylim in data coordinates. Passing *None* leaves the
        limit unchanged.

    emit : bool, default: True
        Whether to notify observers of limit change.

    auto : bool or None, default: False
        Whether to turn on autoscaling of the y-axis. *True* turns on,
        *False* turns off, *None* leaves unchanged.

    ymin, ymax : float, optional
        They are equivalent to bottom and top respectively, and it is an
        error to pass both *ymin* and *bottom* or *ymax* and *top*.

    Returns
    -------
    bottom, top : (float, float)
        The new y-axis limits in data coordinates.

    See Also
    --------
    get_ylim
    set_ybound, get_ybound
    invert_yaxis, yaxis_inverted

    Notes
    -----
    The *bottom* value may be greater than the *top* value, in which
    case the y-axis values will decrease from *bottom* to *top*.

    Examples
    --------
    >>> set_ylim(bottom, top)
    >>> set_ylim((bottom, top))
    >>> bottom, top = set_ylim(bottom, top)

    One limit may be left unchanged.

    >>> set_ylim(top=top_lim)

    Limits may be passed in reverse order to flip the direction of
    the y-axis. For example, suppose ``y`` represents depth of the
    ocean in m. The y-axis limits might be set like the following
    so 5000 m depth is at the bottom of the plot and the surface,
    0 m, is at the top.

    >>> set_ylim(5000, 0)
    """
    if top is None and np.iterable(bottom):
        bottom, top = bottom
    if ymin is not None:
        if bottom is not None:
            raise TypeError("Cannot pass both 'bottom' and 'ymin'")
        bottom = ymin
    if ymax is not None:
        if top is not None:
            raise TypeError("Cannot pass both 'top' and 'ymax'")
        top = ymax
    return self.yaxis._set_lim(bottom, top, emit=emit, auto=auto)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/axes/_axes.py
# Line: 429

def indicate_inset(self, bounds=None, inset_ax=None, *, transform=None,
                   facecolor='none', edgecolor='0.5', alpha=0.5,
                   zorder=None, **kwargs):
    """
    Add an inset indicator to the Axes.  This is a rectangle on the plot
    at the position indicated by *bounds* that optionally has lines that
    connect the rectangle to an inset Axes (`.Axes.inset_axes`).

    Warnings
    --------
    This method is experimental as of 3.0, and the API may change.

    Parameters
    ----------
    bounds : [x0, y0, width, height], optional
        Lower-left corner of rectangle to be marked, and its width
        and height.  If not set, the bounds will be calculated from the
        data limits of *inset_ax*, which must be supplied.

    inset_ax : `.Axes`, optional
        An optional inset Axes to draw connecting lines to.  Two lines are
        drawn connecting the indicator box to the inset Axes on corners
        chosen so as to not overlap with the indicator box.

    transform : `.Transform`
        Transform for the rectangle coordinates. Defaults to
        ``ax.transData``, i.e. the units of *rect* are in the Axes' data
        coordinates.

    facecolor : :mpltype:`color`, default: 'none'
        Facecolor of the rectangle.

    edgecolor : :mpltype:`color`, default: '0.5'
        Color of the rectangle and color of the connecting lines.

    alpha : float or None, default: 0.5
        Transparency of the rectangle and connector lines.  If not
        ``None``, this overrides any alpha value included in the
        *facecolor* and *edgecolor* parameters.

    zorder : float, default: 4.99
        Drawing order of the rectangle and connector lines.  The default,
        4.99, is just below the default level of inset Axes.

    **kwargs
        Other keyword arguments are passed on to the `.Rectangle` patch:

        %(Rectangle:kwdoc)s

    Returns
    -------
    inset_indicator : `.inset.InsetIndicator`
        An artist which contains

        inset_indicator.rectangle : `.Rectangle`
            The indicator frame.

        inset_indicator.connectors : 4-tuple of `.patches.ConnectionPatch`
            The four connector lines connecting to (lower_left, upper_left,
            lower_right upper_right) corners of *inset_ax*. Two lines are
            set with visibility to *False*,  but the user can set the
            visibility to True if the automatic choice is not deemed correct.

        .. versionchanged:: 3.10
            Previously the rectangle and connectors tuple were returned.
    """
    # to make the Axes connectors work, we need to apply the aspect to
    # the parent Axes.
    self.apply_aspect()

    if transform is None:
        transform = self.transData
    kwargs.setdefault('label', '_indicate_inset')

    indicator_patch = minset.InsetIndicator(
        bounds, inset_ax=inset_ax,
        facecolor=facecolor, edgecolor=edgecolor, alpha=alpha,
        zorder=zorder, transform=transform, **kwargs)
    self.add_artist(indicator_patch)

    return indicator_patch


# ==================================================
# Line: 729

def annotate(self, text, xy, xytext=None, xycoords='data', textcoords=None,
             arrowprops=None, annotation_clip=None, **kwargs):
    # Signature must match Annotation. This is verified in
    # test_annotate_signature().
    a = mtext.Annotation(text, xy, xytext=xytext, xycoords=xycoords,
                         textcoords=textcoords, arrowprops=arrowprops,
                         annotation_clip=annotation_clip, **kwargs)
    a.set_transform(mtransforms.IdentityTransform())
    if kwargs.get('clip_on', False) and a.get_clip_path() is None:
        a.set_clip_path(self.patch)
    self._add_text(a)
    return a

# ==================================================
# Line: 1113

def hlines(self, y, xmin, xmax, colors=None, linestyles='solid',
           label='', **kwargs):
    """
    Plot horizontal lines at each *y* from *xmin* to *xmax*.

    Parameters
    ----------
    y : float or array-like
        y-indexes where to plot the lines.

    xmin, xmax : float or array-like
        Respective beginning and end of each line. If scalars are
        provided, all lines will have the same length.

    colors : :mpltype:`color` or list of color , default: :rc:`lines.color`

    linestyles : {'solid', 'dashed', 'dashdot', 'dotted'}, default: 'solid'

    label : str, default: ''

    Returns
    -------
    `~matplotlib.collections.LineCollection`

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER
    **kwargs :  `~matplotlib.collections.LineCollection` properties.

    See Also
    --------
    vlines : vertical lines
    axhline : horizontal line across the Axes
    """

    # We do the conversion first since not all unitized data is uniform
    xmin, xmax, y = self._process_unit_info(
        [("x", xmin), ("x", xmax), ("y", y)], kwargs)

    if not np.iterable(y):
        y = [y]
    if not np.iterable(xmin):
        xmin = [xmin]
    if not np.iterable(xmax):
        xmax = [xmax]

    # Create and combine masked_arrays from input
    y, xmin, xmax = cbook._combine_masks(y, xmin, xmax)
    y = np.ravel(y)
    xmin = np.ravel(xmin)
    xmax = np.ravel(xmax)

    masked_verts = np.ma.empty((len(y), 2, 2))
    masked_verts[:, 0, 0] = xmin
    masked_verts[:, 0, 1] = y
    masked_verts[:, 1, 0] = xmax
    masked_verts[:, 1, 1] = y

    lines = mcoll.LineCollection(masked_verts, colors=colors,
                                 linestyles=linestyles, label=label)
    self.add_collection(lines, autolim=False)
    lines._internal_update(kwargs)

    if len(y) > 0:
        # Extreme values of xmin/xmax/y.  Using masked_verts here handles
        # the case of y being a masked *object* array (as can be generated
        # e.g. by errorbar()), which would make nanmin/nanmax stumble.
        updatex = True
        updatey = True
        if self.name == "rectilinear":
            datalim = lines.get_datalim(self.transData)
            t = lines.get_transform()
            updatex, updatey = t.contains_branch_seperately(self.transData)
            minx = np.nanmin(datalim.xmin)
            maxx = np.nanmax(datalim.xmax)
            miny = np.nanmin(datalim.ymin)
            maxy = np.nanmax(datalim.ymax)
        else:
            minx = np.nanmin(masked_verts[..., 0])
            maxx = np.nanmax(masked_verts[..., 0])
            miny = np.nanmin(masked_verts[..., 1])
            maxy = np.nanmax(masked_verts[..., 1])

        corners = (minx, miny), (maxx, maxy)
        self.update_datalim(corners, updatex, updatey)
        self._request_autoscale_view()
    return lines


# ==================================================
# Line: 1205

def vlines(self, x, ymin, ymax, colors=None, linestyles='solid',
           label='', **kwargs):
    """
    Plot vertical lines at each *x* from *ymin* to *ymax*.

    Parameters
    ----------
    x : float or array-like
        x-indexes where to plot the lines.

    ymin, ymax : float or array-like
        Respective beginning and end of each line. If scalars are
        provided, all lines will have the same length.

    colors : :mpltype:`color` or list of color, default: :rc:`lines.color`

    linestyles : {'solid', 'dashed', 'dashdot', 'dotted'}, default: 'solid'

    label : str, default: ''

    Returns
    -------
    `~matplotlib.collections.LineCollection`

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER
    **kwargs : `~matplotlib.collections.LineCollection` properties.

    See Also
    --------
    hlines : horizontal lines
    axvline : vertical line across the Axes
    """

    # We do the conversion first since not all unitized data is uniform
    x, ymin, ymax = self._process_unit_info(
        [("x", x), ("y", ymin), ("y", ymax)], kwargs)

    if not np.iterable(x):
        x = [x]
    if not np.iterable(ymin):
        ymin = [ymin]
    if not np.iterable(ymax):
        ymax = [ymax]

    # Create and combine masked_arrays from input
    x, ymin, ymax = cbook._combine_masks(x, ymin, ymax)
    x = np.ravel(x)
    ymin = np.ravel(ymin)
    ymax = np.ravel(ymax)

    masked_verts = np.ma.empty((len(x), 2, 2))
    masked_verts[:, 0, 0] = x
    masked_verts[:, 0, 1] = ymin
    masked_verts[:, 1, 0] = x
    masked_verts[:, 1, 1] = ymax

    lines = mcoll.LineCollection(masked_verts, colors=colors,
                                 linestyles=linestyles, label=label)
    self.add_collection(lines, autolim=False)
    lines._internal_update(kwargs)

    if len(x) > 0:
        # Extreme values of x/ymin/ymax.  Using masked_verts here handles
        # the case of x being a masked *object* array (as can be generated
        # e.g. by errorbar()), which would make nanmin/nanmax stumble.
        updatex = True
        updatey = True
        if self.name == "rectilinear":
            datalim = lines.get_datalim(self.transData)
            t = lines.get_transform()
            updatex, updatey = t.contains_branch_seperately(self.transData)
            minx = np.nanmin(datalim.xmin)
            maxx = np.nanmax(datalim.xmax)
            miny = np.nanmin(datalim.ymin)
            maxy = np.nanmax(datalim.ymax)
        else:
            minx = np.nanmin(masked_verts[..., 0])
            maxx = np.nanmax(masked_verts[..., 0])
            miny = np.nanmin(masked_verts[..., 1])
            maxy = np.nanmax(masked_verts[..., 1])

        corners = (minx, miny), (maxx, maxy)
        self.update_datalim(corners, updatex, updatey)
        self._request_autoscale_view()
    return lines


# ==================================================
# Line: 1299

def eventplot(self, positions, orientation='horizontal', lineoffsets=1,
              linelengths=1, linewidths=None, colors=None, alpha=None,
              linestyles='solid', **kwargs):
    """
    Plot identical parallel lines at the given positions.

    This type of plot is commonly used in neuroscience for representing
    neural events, where it is usually called a spike raster, dot raster,
    or raster plot.

    However, it is useful in any situation where you wish to show the
    timing or position of multiple sets of discrete events, such as the
    arrival times of people to a business on each day of the month or the
    date of hurricanes each year of the last century.

    Parameters
    ----------
    positions : array-like or list of array-like
        A 1D array-like defines the positions of one sequence of events.

        Multiple groups of events may be passed as a list of array-likes.
        Each group can be styled independently by passing lists of values
        to *lineoffsets*, *linelengths*, *linewidths*, *colors* and
        *linestyles*.

        Note that *positions* can be a 2D array, but in practice different
        event groups usually have different counts so that one will use a
        list of different-length arrays rather than a 2D array.

    orientation : {'horizontal', 'vertical'}, default: 'horizontal'
        The direction of the event sequence:

        - 'horizontal': the events are arranged horizontally.
          The indicator lines are vertical.
        - 'vertical': the events are arranged vertically.
          The indicator lines are horizontal.

    lineoffsets : float or array-like, default: 1
        The offset of the center of the lines from the origin, in the
        direction orthogonal to *orientation*.

        If *positions* is 2D, this can be a sequence with length matching
        the length of *positions*.

    linelengths : float or array-like, default: 1
        The total height of the lines (i.e. the lines stretches from
        ``lineoffset - linelength/2`` to ``lineoffset + linelength/2``).

        If *positions* is 2D, this can be a sequence with length matching
        the length of *positions*.

    linewidths : float or array-like, default: :rc:`lines.linewidth`
        The line width(s) of the event lines, in points.

        If *positions* is 2D, this can be a sequence with length matching
        the length of *positions*.

    colors : :mpltype:`color` or list of color, default: :rc:`lines.color`
        The color(s) of the event lines.

        If *positions* is 2D, this can be a sequence with length matching
        the length of *positions*.

    alpha : float or array-like, default: 1
        The alpha blending value(s), between 0 (transparent) and 1
        (opaque).

        If *positions* is 2D, this can be a sequence with length matching
        the length of *positions*.

    linestyles : str or tuple or list of such values, default: 'solid'
        Default is 'solid'. Valid strings are ['solid', 'dashed',
        'dashdot', 'dotted', '-', '--', '-.', ':']. Dash tuples
        should be of the form::

            (offset, onoffseq),

        where *onoffseq* is an even length tuple of on and off ink
        in points.

        If *positions* is 2D, this can be a sequence with length matching
        the length of *positions*.

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Other keyword arguments are line collection properties.  See
        `.LineCollection` for a list of the valid properties.

    Returns
    -------
    list of `.EventCollection`
        The `.EventCollection` that were added.

    Notes
    -----
    For *linelengths*, *linewidths*, *colors*, *alpha* and *linestyles*, if
    only a single value is given, that value is applied to all lines. If an
    array-like is given, it must have the same length as *positions*, and
    each value will be applied to the corresponding row of the array.

    Examples
    --------
    .. plot:: gallery/lines_bars_and_markers/eventplot_demo.py
    """

    lineoffsets, linelengths = self._process_unit_info(
            [("y", lineoffsets), ("y", linelengths)], kwargs)

    # fix positions, noting that it can be a list of lists:
    if not np.iterable(positions):
        positions = [positions]
    elif any(np.iterable(position) for position in positions):
        positions = [np.asanyarray(position) for position in positions]
    else:
        positions = [np.asanyarray(positions)]

    poss = []
    for position in positions:
        poss += self._process_unit_info([("x", position)], kwargs)
    positions = poss

    # prevent 'singular' keys from **kwargs dict from overriding the effect
    # of 'plural' keyword arguments (e.g. 'color' overriding 'colors')
    colors = cbook._local_over_kwdict(colors, kwargs, 'color')
    linewidths = cbook._local_over_kwdict(linewidths, kwargs, 'linewidth')
    linestyles = cbook._local_over_kwdict(linestyles, kwargs, 'linestyle')

    if not np.iterable(lineoffsets):
        lineoffsets = [lineoffsets]
    if not np.iterable(linelengths):
        linelengths = [linelengths]
    if not np.iterable(linewidths):
        linewidths = [linewidths]
    if not np.iterable(colors):
        colors = [colors]
    if not np.iterable(alpha):
        alpha = [alpha]
    if hasattr(linestyles, 'lower') or not np.iterable(linestyles):
        linestyles = [linestyles]

    lineoffsets = np.asarray(lineoffsets)
    linelengths = np.asarray(linelengths)
    linewidths = np.asarray(linewidths)

    if len(lineoffsets) == 0:
        raise ValueError('lineoffsets cannot be empty')
    if len(linelengths) == 0:
        raise ValueError('linelengths cannot be empty')
    if len(linestyles) == 0:
        raise ValueError('linestyles cannot be empty')
    if len(linewidths) == 0:
        raise ValueError('linewidths cannot be empty')
    if len(alpha) == 0:
        raise ValueError('alpha cannot be empty')
    if len(colors) == 0:
        colors = [None]
    try:
        # Early conversion of the colors into RGBA values to take care
        # of cases like colors='0.5' or colors='C1'.  (Issue #8193)
        colors = mcolors.to_rgba_array(colors)
    except ValueError:
        # Will fail if any element of *colors* is None. But as long
        # as len(colors) == 1 or len(positions), the rest of the
        # code should process *colors* properly.
        pass

    if len(lineoffsets) == 1 and len(positions) != 1:
        lineoffsets = np.tile(lineoffsets, len(positions))
        lineoffsets[0] = 0
        lineoffsets = np.cumsum(lineoffsets)
    if len(linelengths) == 1:
        linelengths = np.tile(linelengths, len(positions))
    if len(linewidths) == 1:
        linewidths = np.tile(linewidths, len(positions))
    if len(colors) == 1:
        colors = list(colors) * len(positions)
    if len(alpha) == 1:
        alpha = list(alpha) * len(positions)
    if len(linestyles) == 1:
        linestyles = [linestyles] * len(positions)

    if len(lineoffsets) != len(positions):
        raise ValueError('lineoffsets and positions are unequal sized '
                         'sequences')
    if len(linelengths) != len(positions):
        raise ValueError('linelengths and positions are unequal sized '
                         'sequences')
    if len(linewidths) != len(positions):
        raise ValueError('linewidths and positions are unequal sized '
                         'sequences')
    if len(colors) != len(positions):
        raise ValueError('colors and positions are unequal sized '
                         'sequences')
    if len(alpha) != len(positions):
        raise ValueError('alpha and positions are unequal sized '
                         'sequences')
    if len(linestyles) != len(positions):
        raise ValueError('linestyles and positions are unequal sized '
                         'sequences')

    colls = []
    for position, lineoffset, linelength, linewidth, color, alpha_, \
        linestyle in \
            zip(positions, lineoffsets, linelengths, linewidths,
                colors, alpha, linestyles):
        coll = mcoll.EventCollection(position,
                                     orientation=orientation,
                                     lineoffset=lineoffset,
                                     linelength=linelength,
                                     linewidth=linewidth,
                                     color=color,
                                     alpha=alpha_,
                                     linestyle=linestyle)
        self.add_collection(coll, autolim=False)
        coll._internal_update(kwargs)
        colls.append(coll)

    if len(positions) > 0:
        # try to get min/max
        min_max = [(np.min(_p), np.max(_p)) for _p in positions
                   if len(_p) > 0]
        # if we have any non-empty positions, try to autoscale
        if len(min_max) > 0:
            mins, maxes = zip(*min_max)
            minpos = np.min(mins)
            maxpos = np.max(maxes)

            minline = (lineoffsets - linelengths).min()
            maxline = (lineoffsets + linelengths).max()

            if orientation == "vertical":
                corners = (minline, minpos), (maxline, maxpos)
            else:  # "horizontal"
                corners = (minpos, minline), (maxpos, maxline)
            self.update_datalim(corners)
            self._request_autoscale_view()

    return colls


# ==================================================
# Line: 2022

def xcorr(self, x, y, normed=True, detrend=mlab.detrend_none,
          usevlines=True, maxlags=10, **kwargs):
    r"""
    Plot the cross correlation between *x* and *y*.

    The correlation with lag k is defined as
    :math:`\sum_n x[n+k] \cdot y^*[n]`, where :math:`y^*` is the complex
    conjugate of :math:`y`.

    Parameters
    ----------
    x, y : array-like of length n
        Neither *x* nor *y* are run through Matplotlib's unit conversion, so
        these should be unit-less arrays.

    detrend : callable, default: `.mlab.detrend_none` (no detrending)
        A detrending function applied to *x* and *y*.  It must have the
        signature ::

            detrend(x: np.ndarray) -> np.ndarray

    normed : bool, default: True
        If ``True``, input vectors are normalised to unit length.

    usevlines : bool, default: True
        Determines the plot style.

        If ``True``, vertical lines are plotted from 0 to the xcorr value
        using `.Axes.vlines`. Additionally, a horizontal line is plotted
        at y=0 using `.Axes.axhline`.

        If ``False``, markers are plotted at the xcorr values using
        `.Axes.plot`.

    maxlags : int, default: 10
        Number of lags to show. If None, will return all ``2 * len(x) - 1``
        lags.

    Returns
    -------
    lags : array (length ``2*maxlags+1``)
        The lag vector.
    c : array  (length ``2*maxlags+1``)
        The auto correlation vector.
    line : `.LineCollection` or `.Line2D`
        `.Artist` added to the Axes of the correlation:

        - `.LineCollection` if *usevlines* is True.
        - `.Line2D` if *usevlines* is False.
    b : `~matplotlib.lines.Line2D` or None
        Horizontal line at 0 if *usevlines* is True
        None *usevlines* is False.

    Other Parameters
    ----------------
    linestyle : `~matplotlib.lines.Line2D` property, optional
        The linestyle for plotting the data points.
        Only used if *usevlines* is ``False``.

    marker : str, default: 'o'
        The marker for plotting the data points.
        Only used if *usevlines* is ``False``.

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Additional parameters are passed to `.Axes.vlines` and
        `.Axes.axhline` if *usevlines* is ``True``; otherwise they are
        passed to `.Axes.plot`.

    Notes
    -----
    The cross correlation is performed with `numpy.correlate` with
    ``mode = "full"``.
    """
    Nx = len(x)
    if Nx != len(y):
        raise ValueError('x and y must be equal length')

    x = detrend(np.asarray(x))
    y = detrend(np.asarray(y))

    correls = np.correlate(x, y, mode="full")

    if normed:
        correls = correls / np.sqrt(np.dot(x, x) * np.dot(y, y))

    if maxlags is None:
        maxlags = Nx - 1

    if maxlags >= Nx or maxlags < 1:
        raise ValueError('maxlags must be None or strictly '
                         'positive < %d' % Nx)

    lags = np.arange(-maxlags, maxlags + 1)
    correls = correls[Nx - 1 - maxlags:Nx + maxlags]

    if usevlines:
        a = self.vlines(lags, [0], correls, **kwargs)
        # Make label empty so only vertical lines get a legend entry
        kwargs.pop('label', '')
        b = self.axhline(**kwargs)
    else:
        kwargs.setdefault('marker', 'o')
        kwargs.setdefault('linestyle', 'None')
        a, = self.plot(lags, correls, **kwargs)
        b = None
    return lags, correls, a, b


# ==================================================
# Line: 2651

def barh(self, y, width, height=0.8, left=None, *, align="center",
         data=None, **kwargs):
    r"""
    Make a horizontal bar plot.

    The bars are positioned at *y* with the given *align*\ment. Their
    dimensions are given by *width* and *height*. The horizontal baseline
    is *left* (default 0).

    Many parameters can take either a single value applying to all bars
    or a sequence of values, one for each bar.

    Parameters
    ----------
    y : float or array-like
        The y coordinates of the bars. See also *align* for the
        alignment of the bars to the coordinates.

        Bars are often used for categorical data, i.e. string labels below
        the bars. You can provide a list of strings directly to *y*.
        ``barh(['A', 'B', 'C'], [1, 2, 3])`` is often a shorter and more
        convenient notation compared to
        ``barh(range(3), [1, 2, 3], tick_label=['A', 'B', 'C'])``. They are
        equivalent as long as the names are unique. The explicit *tick_label*
        notation draws the names in the sequence given. However, when having
        duplicate values in categorical *y* data, these values map to the same
        numerical y coordinate, and hence the corresponding bars are drawn on
        top of each other.

    width : float or array-like
        The width(s) of the bars.

        Note that if *left* has units (e.g. datetime), *width* should be in
        units that are a difference from the value of *left* (e.g. timedelta).

    height : float or array-like, default: 0.8
        The heights of the bars.

        Note that if *y* has units (e.g. datetime), then *height* should be in
        units that are a difference (e.g. timedelta) around the *y* values.

    left : float or array-like, default: 0
        The x coordinates of the left side(s) of the bars.

        Note that if *left* has units, then the x-axis will get a Locator and
        Formatter appropriate for the units (e.g. dates, or categorical).

    align : {'center', 'edge'}, default: 'center'
        Alignment of the base to the *y* coordinates*:

        - 'center': Center the bars on the *y* positions.
        - 'edge': Align the bottom edges of the bars with the *y*
          positions.

        To align the bars on the top edge pass a negative *height* and
        ``align='edge'``.

    Returns
    -------
    `.BarContainer`
        Container with all the bars and optionally errorbars.

    Other Parameters
    ----------------
    color : :mpltype:`color` or list of :mpltype:`color`, optional
        The colors of the bar faces.

    edgecolor : :mpltype:`color` or list of :mpltype:`color`, optional
        The colors of the bar edges.

    linewidth : float or array-like, optional
        Width of the bar edge(s). If 0, don't draw edges.

    tick_label : str or list of str, optional
        The tick labels of the bars.
        Default: None (Use default numeric labels.)

    label : str or list of str, optional
        A single label is attached to the resulting `.BarContainer` as a
        label for the whole dataset.
        If a list is provided, it must be the same length as *y* and
        labels the individual bars. Repeated labels are not de-duplicated
        and will cause repeated label entries, so this is best used when
        bars also differ in style (e.g., by passing a list to *color*.)

    xerr, yerr : float or array-like of shape(N,) or shape(2, N), optional
        If not *None*, add horizontal / vertical errorbars to the bar tips.
        The values are +/- sizes relative to the data:

        - scalar: symmetric +/- values for all bars
        - shape(N,): symmetric +/- values for each bar
        - shape(2, N): Separate - and + values for each bar. First row
          contains the lower errors, the second row contains the upper
          errors.
        - *None*: No errorbar. (default)

        See :doc:`/gallery/statistics/errorbar_features` for an example on
        the usage of *xerr* and *yerr*.

    ecolor : :mpltype:`color` or list of :mpltype:`color`, default: 'black'
        The line color of the errorbars.

    capsize : float, default: :rc:`errorbar.capsize`
       The length of the error bar caps in points.

    error_kw : dict, optional
        Dictionary of keyword arguments to be passed to the
        `~.Axes.errorbar` method. Values of *ecolor* or *capsize* defined
        here take precedence over the independent keyword arguments.

    log : bool, default: False
        If ``True``, set the x-axis to be log scale.

    data : indexable object, optional
        If given, all parameters also accept a string ``s``, which is
        interpreted as ``data[s]`` if  ``s`` is a key in ``data``.

    **kwargs : `.Rectangle` properties

    %(Rectangle:kwdoc)s

    See Also
    --------
    bar : Plot a vertical bar plot.

    Notes
    -----
    Stacked bars can be achieved by passing individual *left* values per
    bar. See
    :doc:`/gallery/lines_bars_and_markers/horizontal_barchart_distribution`.
    """
    kwargs.setdefault('orientation', 'horizontal')
    patches = self.bar(x=left, height=height, width=width, bottom=y,
                       align=align, data=data, **kwargs)
    return patches


# ==================================================
# Line: 3036

def grouped_bar(self, heights, *, positions=None, group_spacing=1.5, bar_spacing=0,
                tick_labels=None, labels=None, orientation="vertical", colors=None,
                **kwargs):
    """
    Make a grouped bar plot.

    .. versionadded:: 3.11

        The API is still provisional. We may still fine-tune some aspects based on
        user-feedback.

    Grouped bar charts visualize a collection of categorical datasets. Each value
    in a dataset belongs to a distinct category and these categories are the same
    across all datasets. The categories typically have string names, but could
    also be dates or index keys. The values in each dataset are represented by a
    sequence of bars of the same color. The bars of all datasets are grouped
    together by their shared categories. The category names are drawn as the tick
    labels for each bar group. Each dataset has a distinct bar color, and can
    optionally get a label that is used for the legend.

    Example:

    .. code-block:: python

       grouped_bar([dataset_0, dataset_1, dataset_2],
                   tick_labels=['A', 'B'],
                   labels=['dataset 0', 'dataset 1', 'dataset 2'])

    .. plot:: _embedded_plots/grouped_bar.py

    Parameters
    ----------
    heights : list of array-like or dict of array-like or 2D array \

# ==================================================
# Line: 3339

def stem(self, *args, linefmt=None, markerfmt=None, basefmt=None, bottom=0,
         label=None, orientation='vertical'):
    """
    Create a stem plot.

    A stem plot draws lines perpendicular to a baseline at each location
    *locs* from the baseline to *heads*, and places a marker there. For
    vertical stem plots (the default), the *locs* are *x* positions, and
    the *heads* are *y* values. For horizontal stem plots, the *locs* are
    *y* positions, and the *heads* are *x* values.

    Call signature::

      stem([locs,] heads, linefmt=None, markerfmt=None, basefmt=None)

    The *locs*-positions are optional. *linefmt* may be provided as
    positional, but all other formats must be provided as keyword
    arguments.

    Parameters
    ----------
    locs : array-like, default: (0, 1, ..., len(heads) - 1)
        For vertical stem plots, the x-positions of the stems.
        For horizontal stem plots, the y-positions of the stems.

    heads : array-like
        For vertical stem plots, the y-values of the stem heads.
        For horizontal stem plots, the x-values of the stem heads.

    linefmt : str, optional
        A string defining the color and/or linestyle of the vertical lines:

        =========  =============
        Character  Line Style
        =========  =============
        ``'-'``    solid line
        ``'--'``   dashed line
        ``'-.'``   dash-dot line
        ``':'``    dotted line
        =========  =============

        Default: 'C0-', i.e. solid line with the first color of the color
        cycle.

        Note: Markers specified through this parameter (e.g. 'x') will be
        silently ignored. Instead, markers should be specified using
        *markerfmt*.

    markerfmt : str, optional
        A string defining the color and/or shape of the markers at the stem
        heads. If the marker is not given, use the marker 'o', i.e. filled
        circles. If the color is not given, use the color from *linefmt*.

    basefmt : str, default: 'C3-' ('C2-' in classic mode)
        A format string defining the properties of the baseline.

    orientation : {'vertical', 'horizontal'}, default: 'vertical'
        The orientation of the stems.

    bottom : float, default: 0
        The y/x-position of the baseline (depending on *orientation*).

    label : str, optional
        The label to use for the stems in legends.

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    Returns
    -------
    `.StemContainer`
        The container may be treated like a tuple
        (*markerline*, *stemlines*, *baseline*)

    Notes
    -----
    .. seealso::
        The MATLAB function
        `stem <https://www.mathworks.com/help/matlab/ref/stem.html>`_
        which inspired this method.
    """
    if not 1 <= len(args) <= 3:
        raise _api.nargs_error('stem', '1-3', len(args))
    _api.check_in_list(['horizontal', 'vertical'], orientation=orientation)

    if len(args) == 1:
        heads, = args
        locs = np.arange(len(heads))
        args = ()
    elif isinstance(args[1], str):
        heads, *args = args
        locs = np.arange(len(heads))
    else:
        locs, heads, *args = args

    if orientation == 'vertical':
        locs, heads = self._process_unit_info([("x", locs), ("y", heads)])
    else:  # horizontal
        heads, locs = self._process_unit_info([("x", heads), ("y", locs)])

    # resolve line format
    if linefmt is None:
        linefmt = args[0] if len(args) > 0 else "C0-"
    linestyle, linemarker, linecolor = _process_plot_format(linefmt)

    # resolve marker format
    if markerfmt is None:
        # if not given as kwarg, fall back to 'o'
        markerfmt = "o"
    if markerfmt == '':
        markerfmt = ' '  # = empty line style; '' would resolve rcParams
    markerstyle, markermarker, markercolor = _process_plot_format(markerfmt)
    if markermarker is None:
        markermarker = 'o'
    if markerstyle is None:
        markerstyle = 'None'
    if markercolor is None:
        markercolor = linecolor

    # resolve baseline format
    if basefmt is None:
        basefmt = ("C2-" if mpl.rcParams["_internal.classic_mode"] else
                   "C3-")
    basestyle, basemarker, basecolor = _process_plot_format(basefmt)

    # New behaviour in 3.1 is to use a LineCollection for the stemlines
    linestyle = mpl._val_or_rc(linestyle, 'lines.linestyle')
    xlines = self.vlines if orientation == "vertical" else self.hlines
    stemlines = xlines(
        locs, bottom, heads,
        colors=linecolor, linestyles=linestyle, label="_nolegend_")

    if orientation == 'horizontal':
        marker_x = heads
        marker_y = locs
        baseline_x = [bottom, bottom]
        baseline_y = [np.min(locs), np.max(locs)]
    else:
        marker_x = locs
        marker_y = heads
        baseline_x = [np.min(locs), np.max(locs)]
        baseline_y = [bottom, bottom]

    markerline, = self.plot(marker_x, marker_y,
                            color=markercolor, linestyle=markerstyle,
                            marker=markermarker, label="_nolegend_")

    baseline, = self.plot(baseline_x, baseline_y,
                          color=basecolor, linestyle=basestyle,
                          marker=basemarker, label="_nolegend_")
    baseline.get_path()._interpolation_steps = \
        mpl.axis.GRIDLINE_INTERPOLATION_STEPS

    stem_container = StemContainer((markerline, stemlines, baseline),
                                   label=label)
    self.add_container(stem_container)
    return stem_container


# ==================================================
# Line: 3499

def pie(self, x, explode=None, labels=None, colors=None,
        autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1,
        startangle=0, radius=1, counterclock=True,
        wedgeprops=None, textprops=None, center=(0, 0),
        frame=False, rotatelabels=False, *, normalize=True, hatch=None):
    """
    Plot a pie chart.

    Make a pie chart of array *x*.  The fractional area of each wedge is
    given by ``x/sum(x)``.

    The wedges are plotted counterclockwise, by default starting from the
    x-axis.

    Parameters
    ----------
    x : 1D array-like
        The wedge sizes.

    explode : array-like, default: None
        If not *None*, is a ``len(x)`` array which specifies the fraction
        of the radius with which to offset each wedge.

    labels : list, default: None
        A sequence of strings providing the labels for each wedge

    colors : :mpltype:`color` or list of :mpltype:`color`, default: None
        A sequence of colors through which the pie chart will cycle.  If
        *None*, will use the colors in the currently active cycle.

    hatch : str or list, default: None
        Hatching pattern applied to all pie wedges or sequence of patterns
        through which the chart will cycle. For a list of valid patterns,
        see :doc:`/gallery/shapes_and_collections/hatch_style_reference`.

        .. versionadded:: 3.7

    autopct : None or str or callable, default: None
        If not *None*, *autopct* is a string or function used to label the
        wedges with their numeric value. The label will be placed inside
        the wedge. If *autopct* is a format string, the label will be
        ``fmt % pct``. If *autopct* is a function, then it will be called.

    pctdistance : float, default: 0.6
        The relative distance along the radius at which the text
        generated by *autopct* is drawn. To draw the text outside the pie,
        set *pctdistance* > 1. This parameter is ignored if *autopct* is
        ``None``.

    labeldistance : float or None, default: 1.1
        The relative distance along the radius at which the labels are
        drawn. To draw the labels inside the pie, set  *labeldistance* < 1.
        If set to ``None``, labels are not drawn but are still stored for
        use in `.legend`.

    shadow : bool or dict, default: False
        If bool, whether to draw a shadow beneath the pie. If dict, draw a shadow
        passing the properties in the dict to `.Shadow`.

        .. versionadded:: 3.8
            *shadow* can be a dict.

    startangle : float, default: 0 degrees
        The angle by which the start of the pie is rotated,
        counterclockwise from the x-axis.

    radius : float, default: 1
        The radius of the pie.

    counterclock : bool, default: True
        Specify fractions direction, clockwise or counterclockwise.

    wedgeprops : dict, default: None
        Dict of arguments passed to each `.patches.Wedge` of the pie.
        For example, ``wedgeprops = {'linewidth': 3}`` sets the width of
        the wedge border lines equal to 3. By default, ``clip_on=False``.
        When there is a conflict between these properties and other
        keywords, properties passed to *wedgeprops* take precedence.

    textprops : dict, default: None
        Dict of arguments to pass to the text objects.

    center : (float, float), default: (0, 0)
        The coordinates of the center of the chart.

    frame : bool, default: False
        Plot Axes frame with the chart if true.

    rotatelabels : bool, default: False
        Rotate each label to the angle of the corresponding slice if true.

    normalize : bool, default: True
        When *True*, always make a full pie by normalizing x so that
        ``sum(x) == 1``. *False* makes a partial pie if ``sum(x) <= 1``
        and raises a `ValueError` for ``sum(x) > 1``.

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    Returns
    -------
    patches : list
        A sequence of `matplotlib.patches.Wedge` instances

    texts : list
        A list of the label `.Text` instances.

    autotexts : list
        A list of `.Text` instances for the numeric labels. This will only
        be returned if the parameter *autopct* is not *None*.

    Notes
    -----
    The pie chart will probably look best if the figure and Axes are
    square, or the Axes aspect is equal.
    This method sets the aspect ratio of the axis to "equal".
    The Axes aspect ratio can be controlled with `.Axes.set_aspect`.
    """
    self.set_aspect('equal')
    # The use of float32 is "historical", but can't be changed without
    # regenerating the test baselines.
    x = np.asarray(x, np.float32)
    if x.ndim > 1:
        raise ValueError("x must be 1D")

    if np.any(x < 0):
        raise ValueError("Wedge sizes 'x' must be non negative values")

    if not np.all(np.isfinite(x)):
        raise ValueError('Wedge sizes must be finite numbers')

    sx = x.sum()

    if sx == 0:
        raise ValueError('All wedge sizes are zero')

    if normalize:
        x = x / sx
    elif sx > 1:
        raise ValueError('Cannot plot an unnormalized pie with sum(x) > 1')
    if labels is None:
        labels = [''] * len(x)
    if explode is None:
        explode = [0] * len(x)
    if len(x) != len(labels):
        raise ValueError(f"'labels' must be of length 'x', not {len(labels)}")
    if len(x) != len(explode):
        raise ValueError(f"'explode' must be of length 'x', not {len(explode)}")
    if colors is None:
        get_next_color = self._get_patches_for_fill.get_next_color
    else:
        color_cycle = itertools.cycle(colors)

        def get_next_color():
            return next(color_cycle)

    hatch_cycle = itertools.cycle(np.atleast_1d(hatch))

    _api.check_isinstance(Real, radius=radius, startangle=startangle)
    if radius <= 0:
        raise ValueError(f"'radius' must be a positive number, not {radius}")

    # Starting theta1 is the start fraction of the circle
    theta1 = startangle / 360

    if wedgeprops is None:
        wedgeprops = {}
    if textprops is None:
        textprops = {}

    texts = []
    slices = []
    autotexts = []

    for frac, label, expl in zip(x, labels, explode):
        x, y = center
        theta2 = (theta1 + frac) if counterclock else (theta1 - frac)
        thetam = 2 * np.pi * 0.5 * (theta1 + theta2)
        x += expl * math.cos(thetam)
        y += expl * math.sin(thetam)

        w = mpatches.Wedge((x, y), radius, 360. * min(theta1, theta2),
                           360. * max(theta1, theta2),
                           facecolor=get_next_color(),
                           hatch=next(hatch_cycle),
                           clip_on=False,
                           label=label)
        w.set(**wedgeprops)
        slices.append(w)
        self.add_patch(w)

        if shadow:
            # Make sure to add a shadow after the call to add_patch so the
            # figure and transform props will be set.
            shadow_dict = {'ox': -0.02, 'oy': -0.02, 'label': '_nolegend_'}
            if isinstance(shadow, dict):
                shadow_dict.update(shadow)
            self.add_patch(mpatches.Shadow(w, **shadow_dict))

        if labeldistance is not None:
            xt = x + labeldistance * radius * math.cos(thetam)
            yt = y + labeldistance * radius * math.sin(thetam)
            label_alignment_h = 'left' if xt > 0 else 'right'
            label_alignment_v = 'center'
            label_rotation = 'horizontal'
            if rotatelabels:
                label_alignment_v = 'bottom' if yt > 0 else 'top'
                label_rotation = (np.rad2deg(thetam)
                                  + (0 if xt > 0 else 180))
            t = self.text(xt, yt, label,
                          clip_on=False,
                          horizontalalignment=label_alignment_h,
                          verticalalignment=label_alignment_v,
                          rotation=label_rotation,
                          size=mpl.rcParams['xtick.labelsize'])
            t.set(**textprops)
            texts.append(t)

        if autopct is not None:
            xt = x + pctdistance * radius * math.cos(thetam)
            yt = y + pctdistance * radius * math.sin(thetam)
            if isinstance(autopct, str):
                s = autopct % (100. * frac)
            elif callable(autopct):
                s = autopct(100. * frac)
            else:
                raise TypeError(
                    'autopct must be callable or a format string')
            if mpl._val_or_rc(textprops.get("usetex"), "text.usetex"):
                # escape % (i.e. \%) if it is not already escaped
                s = re.sub(r"([^\\])%", r"\1\\%", s)
            t = self.text(xt, yt, s,
                          clip_on=False,
                          horizontalalignment='center',
                          verticalalignment='center')
            t.set(**textprops)
            autotexts.append(t)

        theta1 = theta2

    if frame:
        self._request_autoscale_view()
    else:
        self.set(frame_on=False, xticks=[], yticks=[],
                 xlim=(-1.25 + center[0], 1.25 + center[0]),
                 ylim=(-1.25 + center[1], 1.25 + center[1]))

    if autopct is None:
        return slices, texts
    else:
        return slices, texts, autotexts


# ==================================================
# Line: 3787

def errorbar(self, x, y, yerr=None, xerr=None,
             fmt='', ecolor=None, elinewidth=None, capsize=None,
             barsabove=False, lolims=False, uplims=False,
             xlolims=False, xuplims=False, errorevery=1,
             capthick=None, elinestyle=None,
             **kwargs):
    """
    Plot y versus x as lines and/or markers with attached errorbars.

    *x*, *y* define the data locations, *xerr*, *yerr* define the errorbar
    sizes. By default, this draws the data markers/lines as well as the
    errorbars. Use fmt='none' to draw errorbars without any data markers.

    .. versionadded:: 3.7
       Caps and error lines are drawn in polar coordinates on polar plots.


    Parameters
    ----------
    x, y : float or array-like
        The data positions.

    xerr, yerr : float or array-like, shape(N,) or shape(2, N), optional
        The errorbar sizes:

        - scalar: Symmetric +/- values for all data points.
        - shape(N,): Symmetric +/-values for each data point.
        - shape(2, N): Separate - and + values for each bar. First row
          contains the lower errors, the second row contains the upper
          errors.
        - *None*: No errorbar.

        All values must be >= 0.

        See :doc:`/gallery/statistics/errorbar_features`
        for an example on the usage of ``xerr`` and ``yerr``.

    fmt : str, default: ''
        The format for the data points / data lines. See `.plot` for
        details.

        Use 'none' (case-insensitive) to plot errorbars without any data
        markers.

    ecolor : :mpltype:`color`, default: None
        The color of the errorbar lines.  If None, use the color of the
        line connecting the markers.

    elinewidth : float, default: None
        The linewidth of the errorbar lines. If None, the linewidth of
        the current style is used.

    elinestyle : str or tuple, default: 'solid'
       The linestyle of the errorbar lines.
       Valid values for linestyles include {'-', '--', '-.',
        ':', '', (offset, on-off-seq)}. See `.Line2D.set_linestyle` for a
        complete description.

    capsize : float, default: :rc:`errorbar.capsize`
        The length of the error bar caps in points.

    capthick : float, default: None
        An alias to the keyword argument *markeredgewidth* (a.k.a. *mew*).
        This setting is a more sensible name for the property that
        controls the thickness of the error bar cap in points. For
        backwards compatibility, if *mew* or *markeredgewidth* are given,
        then they will over-ride *capthick*. This may change in future
        releases.

    barsabove : bool, default: False
        If True, will plot the errorbars above the plot
        symbols. Default is below.

    lolims, uplims, xlolims, xuplims : bool or array-like, default: False
        These arguments can be used to indicate that a value gives only
        upper/lower limits.  In that case a caret symbol is used to
        indicate this. *lims*-arguments may be scalars, or array-likes of
        the same length as *xerr* and *yerr*.  To use limits with inverted
        axes, `~.Axes.set_xlim` or `~.Axes.set_ylim` must be called before
        :meth:`errorbar`.  Note the tricky parameter names: setting e.g.
        *lolims* to True means that the y-value is a *lower* limit of the
        True value, so, only an *upward*-pointing arrow will be drawn!

    errorevery : int or (int, int), default: 1
        draws error bars on a subset of the data. *errorevery* =N draws
        error bars on the points (x[::N], y[::N]).
        *errorevery* =(start, N) draws error bars on the points
        (x[start::N], y[start::N]). e.g. errorevery=(6, 3)
        adds error bars to the data at (x[6], x[9], x[12], x[15], ...).
        Used to avoid overlapping error bars when two series share x-axis
        values.

    Returns
    -------
    `.ErrorbarContainer`
        The container contains:

        - data_line : A `~matplotlib.lines.Line2D` instance of x, y plot markers
          and/or line.
        - caplines : A tuple of `~matplotlib.lines.Line2D` instances of the error
          bar caps.
        - barlinecols : A tuple of `.LineCollection` with the horizontal and
          vertical error ranges.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        All other keyword arguments are passed on to the `~.Axes.plot` call
        drawing the markers. For example, this code makes big red squares
        with thick green edges::

            x, y, yerr = rand(3, 10)
            errorbar(x, y, yerr, marker='s', mfc='red',
                     mec='green', ms=20, mew=4)

        where *mfc*, *mec*, *ms* and *mew* are aliases for the longer
        property names, *markerfacecolor*, *markeredgecolor*, *markersize*
        and *markeredgewidth*.

        Valid kwargs for the marker properties are:

        - *dashes*
        - *dash_capstyle*
        - *dash_joinstyle*
        - *drawstyle*
        - *fillstyle*
        - *linestyle*
        - *marker*
        - *markeredgecolor*
        - *markeredgewidth*
        - *markerfacecolor*
        - *markerfacecoloralt*
        - *markersize*
        - *markevery*
        - *solid_capstyle*
        - *solid_joinstyle*

        Refer to the corresponding `.Line2D` property for more details:

        %(Line2D:kwdoc)s
    """
    kwargs = cbook.normalize_kwargs(kwargs, mlines.Line2D)
    # Drop anything that comes in as None to use the default instead.
    kwargs = {k: v for k, v in kwargs.items() if v is not None}
    kwargs.setdefault('zorder', 2)

    # Casting to object arrays preserves units.
    if not isinstance(x, np.ndarray):
        x = np.asarray(x, dtype=object)
    if not isinstance(y, np.ndarray):
        y = np.asarray(y, dtype=object)

    def _upcast_err(err):
        """
        Safely handle tuple of containers that carry units.

        This function covers the case where the input to the xerr/yerr is a
        length 2 tuple of equal length ndarray-subclasses that carry the
        unit information in the container.

        If we have a tuple of nested numpy array (subclasses), we defer
        coercing the units to be consistent to the underlying unit
        library (and implicitly the broadcasting).

        Otherwise, fallback to casting to an object array.
        """

        if (
                # make sure it is not a scalar
                np.iterable(err) and
                # and it is not empty
                len(err) > 0 and
                # and the first element is an array sub-class use
                # safe_first_element because getitem is index-first not
                # location first on pandas objects so err[0] almost always
                # fails.
                isinstance(cbook._safe_first_finite(err), np.ndarray)
        ):
            # Get the type of the first element
            atype = type(cbook._safe_first_finite(err))
            # Promote the outer container to match the inner container
            if atype is np.ndarray:
                # Converts using np.asarray, because data cannot
                # be directly passed to init of np.ndarray
                return np.asarray(err, dtype=object)
            # If atype is not np.ndarray, directly pass data to init.
            # This works for types such as unyts and astropy units
            return atype(err)
        # Otherwise wrap it in an object array
        return np.asarray(err, dtype=object)

    if xerr is not None and not isinstance(xerr, np.ndarray):
        xerr = _upcast_err(xerr)
    if yerr is not None and not isinstance(yerr, np.ndarray):
        yerr = _upcast_err(yerr)
    x, y = np.atleast_1d(x, y)  # Make sure all the args are iterable.
    if len(x) != len(y):
        raise ValueError("'x' and 'y' must have the same size")

    everymask = self._errorevery_to_mask(x, errorevery)

    label = kwargs.pop("label", None)
    kwargs['label'] = '_nolegend_'

    # Create the main line and determine overall kwargs for child artists.
    # We avoid calling self.plot() directly, or self._get_lines(), because
    # that would call self._process_unit_info again, and do other indirect
    # data processing.
    (data_line, base_style), = self._get_lines._plot_args(
        self, (x, y) if fmt == '' else (x, y, fmt), kwargs, return_kwargs=True)

    # Do this after creating `data_line` to avoid modifying `base_style`.
    if barsabove:
        data_line.set_zorder(kwargs['zorder'] - .1)
    else:
        data_line.set_zorder(kwargs['zorder'] + .1)

    # Add line to plot, or throw it away and use it to determine kwargs.
    if fmt.lower() != 'none':
        self.add_line(data_line)
    else:
        data_line = None
        # Remove alpha=0 color that _get_lines._plot_args returns for
        # 'none' format, and replace it with user-specified color, if
        # supplied.
        base_style.pop('color')
        if 'color' in kwargs:
            base_style['color'] = kwargs.pop('color')

    if 'color' not in base_style:
        base_style['color'] = 'C0'
    if ecolor is None:
        ecolor = base_style['color']

    # Eject any line-specific information from format string, as it's not
    # needed for bars or caps.
    for key in ['marker', 'markersize', 'markerfacecolor',
                'markerfacecoloralt',
                'markeredgewidth', 'markeredgecolor', 'markevery',
                'linestyle', 'fillstyle', 'drawstyle', 'dash_capstyle',
                'dash_joinstyle', 'solid_capstyle', 'solid_joinstyle',
                'dashes']:
        base_style.pop(key, None)

    # Make the style dict for the line collections (the bars).
    eb_lines_style = {**base_style, 'color': ecolor}

    if elinewidth is not None:
        eb_lines_style['linewidth'] = elinewidth
    elif 'linewidth' in kwargs:
        eb_lines_style['linewidth'] = kwargs['linewidth']

    for key in ('transform', 'alpha', 'zorder', 'rasterized'):
        if key in kwargs:
            eb_lines_style[key] = kwargs[key]

    if elinestyle is not None:
        eb_lines_style['linestyle'] = elinestyle

    # Make the style dict for caps (the "hats").
    eb_cap_style = {**base_style, 'linestyle': 'none'}
    capsize = mpl._val_or_rc(capsize, "errorbar.capsize")
    if capsize > 0:
        eb_cap_style['markersize'] = 2. * capsize
    if capthick is not None:
        eb_cap_style['markeredgewidth'] = capthick

    # For backwards-compat, allow explicit setting of
    # 'markeredgewidth' to over-ride capthick.
    for key in ('markeredgewidth', 'transform', 'alpha',
                'zorder', 'rasterized'):
        if key in kwargs:
            eb_cap_style[key] = kwargs[key]
    eb_cap_style["markeredgecolor"] = ecolor

    barcols = []
    caplines = {'x': [], 'y': []}

    # Vectorized fancy-indexer.
    def apply_mask(arrays, mask):
        return [array[mask] for array in arrays]

    # dep: dependent dataset, indep: independent dataset
    for (dep_axis, dep, err, lolims, uplims, indep, lines_func,
         marker, lomarker, himarker) in [
            ("x", x, xerr, xlolims, xuplims, y, self.hlines,
             "|", mlines.CARETRIGHTBASE, mlines.CARETLEFTBASE),
            ("y", y, yerr, lolims, uplims, x, self.vlines,
             "_", mlines.CARETUPBASE, mlines.CARETDOWNBASE),
    ]:
        if err is None:
            continue
        lolims = np.broadcast_to(lolims, len(dep)).astype(bool)
        uplims = np.broadcast_to(uplims, len(dep)).astype(bool)
        try:
            np.broadcast_to(err, (2, len(dep)))
        except ValueError:
            raise ValueError(
                f"'{dep_axis}err' (shape: {np.shape(err)}) must be a "
                f"scalar or a 1D or (2, n) array-like whose shape matches "
                f"'{dep_axis}' (shape: {np.shape(dep)})") from None
        if err.dtype is np.dtype(object) and np.any(err == None):  # noqa: E711
            raise ValueError(
                f"'{dep_axis}err' must not contain None. "
                "Use NaN if you want to skip a value.")

        # Raise if any errors are negative, but not if they are nan.
        # To avoid nan comparisons (which lead to warnings on some
        # platforms), we select with `err==err` (which is False for nan).
        # Also, since datetime.timedelta cannot be compared with 0,
        # we compare with the negative error instead.
        if np.any((check := err[err == err]) < -check):
            raise ValueError(
                f"'{dep_axis}err' must not contain negative values")
        # This is like
        #     elow, ehigh = np.broadcast_to(...)
        #     return dep - elow * ~lolims, dep + ehigh * ~uplims
        # except that broadcast_to would strip units.
        low, high = dep + np.vstack([-(1 - lolims), 1 - uplims]) * err
        barcols.append(lines_func(
            *apply_mask([indep, low, high], everymask), **eb_lines_style))
        if self.name == "polar" and dep_axis == "x":
            for b in barcols:
                for p in b.get_paths():
                    p._interpolation_steps = 2
        # Normal errorbars for points without upper/lower limits.
        nolims = ~(lolims | uplims)
        if nolims.any() and capsize > 0:
            indep_masked, lo_masked, hi_masked = apply_mask(
                [indep, low, high], nolims & everymask)
            for lh_masked in [lo_masked, hi_masked]:
                # Since this has to work for x and y as dependent data, we
                # first set both x and y to the independent variable and
                # overwrite the respective dependent data in a second step.
                line = mlines.Line2D(indep_masked, indep_masked,
                                     marker=marker, **eb_cap_style)
                line.set(**{f"{dep_axis}data": lh_masked})
                caplines[dep_axis].append(line)
        for idx, (lims, hl) in enumerate([(lolims, high), (uplims, low)]):
            if not lims.any():
                continue
            hlmarker = (
                himarker
                if self._axis_map[dep_axis].get_inverted() ^ idx
                else lomarker)
            x_masked, y_masked, hl_masked = apply_mask(
                [x, y, hl], lims & everymask)
            # As above, we set the dependent data in a second step.
            line = mlines.Line2D(x_masked, y_masked,
                                 marker=hlmarker, **eb_cap_style)
            line.set(**{f"{dep_axis}data": hl_masked})
            caplines[dep_axis].append(line)
            if capsize > 0:
                caplines[dep_axis].append(mlines.Line2D(
                    x_masked, y_masked, marker=marker, **eb_cap_style))
    if self.name == 'polar':
        trans_shift = self.transShift
        for axis in caplines:
            for l in caplines[axis]:
                # Rotate caps to be perpendicular to the error bars
                for theta, r in zip(l.get_xdata(), l.get_ydata()):
                    rotation = _ScaledRotation(theta=theta, trans_shift=trans_shift)
                    if axis == 'y':
                        rotation += mtransforms.Affine2D().rotate(np.pi / 2)
                    ms = mmarkers.MarkerStyle(marker=marker,
                                              transform=rotation)
                    self.add_line(mlines.Line2D([theta], [r], marker=ms,
                                                **eb_cap_style))
    else:
        for axis in caplines:
            for l in caplines[axis]:
                self.add_line(l)

    self._request_autoscale_view()
    caplines = caplines['x'] + caplines['y']
    errorbar_container = ErrorbarContainer(
        (data_line, tuple(caplines), tuple(barcols)),
        has_xerr=(xerr is not None), has_yerr=(yerr is not None),
        label=label)
    self.add_container(errorbar_container)

    return errorbar_container  # (l0, caplines, barcols)


# ==================================================
# Line: 4176

def boxplot(self, x, notch=None, sym=None, vert=None,
            orientation='vertical', whis=None, positions=None,
            widths=None, patch_artist=None, bootstrap=None,
            usermedians=None, conf_intervals=None,
            meanline=None, showmeans=None, showcaps=None,
            showbox=None, showfliers=None, boxprops=None,
            tick_labels=None, flierprops=None, medianprops=None,
            meanprops=None, capprops=None, whiskerprops=None,
            manage_ticks=True, autorange=False, zorder=None,
            capwidths=None, label=None):
    """
    Draw a box and whisker plot.

    The box extends from the first quartile (Q1) to the third
    quartile (Q3) of the data, with a line at the median.
    The whiskers extend from the box to the farthest data point
    lying within 1.5x the inter-quartile range (IQR) from the box.
    Flier points are those past the end of the whiskers.
    See https://en.wikipedia.org/wiki/Box_plot for reference.

    .. code-block:: none

              Q1-1.5IQR   Q1   median  Q3   Q3+1.5IQR
                           |-----:-----|
           o      |--------|     :     |--------|    o  o
                           |-----:-----|
         flier             <----------->            fliers
                                IQR


    Parameters
    ----------
    x : Array or a sequence of vectors.
        The input data.  If a 2D array, a boxplot is drawn for each column
        in *x*.  If a sequence of 1D arrays, a boxplot is drawn for each
        array in *x*.

    notch : bool, default: :rc:`boxplot.notch`
        Whether to draw a notched boxplot (`True`), or a rectangular
        boxplot (`False`).  The notches represent the confidence interval
        (CI) around the median.  The documentation for *bootstrap*
        describes how the locations of the notches are computed by
        default, but their locations may also be overridden by setting the
        *conf_intervals* parameter.

        .. note::

            In cases where the values of the CI are less than the
            lower quartile or greater than the upper quartile, the
            notches will extend beyond the box, giving it a
            distinctive "flipped" appearance. This is expected
            behavior and consistent with other statistical
            visualization packages.

    sym : str, optional
        The default symbol for flier points.  An empty string ('') hides
        the fliers.  If `None`, then the fliers default to 'b+'.  More
        control is provided by the *flierprops* parameter.

    vert : bool, optional
        .. deprecated:: 3.11
            Use *orientation* instead.

            If this is given during the deprecation period, it overrides
            the *orientation* parameter.

        If True, plots the boxes vertically.
        If False, plots the boxes horizontally.

    orientation : {'vertical', 'horizontal'}, default: 'vertical'
        If 'horizontal', plots the boxes horizontally.
        Otherwise, plots the boxes vertically.

        .. versionadded:: 3.10

    whis : float or (float, float), default: 1.5
        The position of the whiskers.

        If a float, the lower whisker is at the lowest datum above
        ``Q1 - whis*(Q3-Q1)``, and the upper whisker at the highest datum
        below ``Q3 + whis*(Q3-Q1)``, where Q1 and Q3 are the first and
        third quartiles.  The default value of ``whis = 1.5`` corresponds
        to Tukey's original definition of boxplots.

        If a pair of floats, they indicate the percentiles at which to
        draw the whiskers (e.g., (5, 95)).  In particular, setting this to
        (0, 100) results in whiskers covering the whole range of the data.

        In the edge case where ``Q1 == Q3``, *whis* is automatically set
        to (0, 100) (cover the whole range of the data) if *autorange* is
        True.

        Beyond the whiskers, data are considered outliers and are plotted
        as individual points.

    bootstrap : int, optional
        Specifies whether to bootstrap the confidence intervals
        around the median for notched boxplots. If *bootstrap* is
        None, no bootstrapping is performed, and notches are
        calculated using a Gaussian-based asymptotic approximation
        (see McGill, R., Tukey, J.W., and Larsen, W.A., 1978, and
        Kendall and Stuart, 1967). Otherwise, bootstrap specifies
        the number of times to bootstrap the median to determine its
        95% confidence intervals. Values between 1000 and 10000 are
        recommended.

    usermedians : 1D array-like, optional
        A 1D array-like of length ``len(x)``.  Each entry that is not
        `None` forces the value of the median for the corresponding
        dataset.  For entries that are `None`, the medians are computed
        by Matplotlib as normal.

    conf_intervals : array-like, optional
        A 2D array-like of shape ``(len(x), 2)``.  Each entry that is not
        None forces the location of the corresponding notch (which is
        only drawn if *notch* is `True`).  For entries that are `None`,
        the notches are computed by the method specified by the other
        parameters (e.g., *bootstrap*).

    positions : array-like, optional
        The positions of the boxes. The ticks and limits are
        automatically set to match the positions. Defaults to
        ``range(1, N+1)`` where N is the number of boxes to be drawn.

    widths : float or array-like
        The widths of the boxes.  The default is 0.5, or ``0.15*(distance
        between extreme positions)``, if that is smaller.

    patch_artist : bool, default: :rc:`boxplot.patchartist`
        If `False` produces boxes with the Line2D artist. Otherwise,
        boxes are drawn with Patch artists.

    tick_labels : list of str, optional
        The tick labels of each boxplot.
        Ticks are always placed at the box *positions*. If *tick_labels* is given,
        the ticks are labelled accordingly. Otherwise, they keep their numeric
        values.

        .. versionchanged:: 3.9
            Renamed from *labels*, which is deprecated since 3.9
            and will be removed in 3.11.

    manage_ticks : bool, default: True
        If True, the tick locations and labels will be adjusted to match
        the boxplot positions.

    autorange : bool, default: False
        When `True` and the data are distributed such that the 25th and
        75th percentiles are equal, *whis* is set to (0, 100) such
        that the whisker ends are at the minimum and maximum of the data.

    meanline : bool, default: :rc:`boxplot.meanline`
        If `True` (and *showmeans* is `True`), will try to render the
        mean as a line spanning the full width of the box according to
        *meanprops* (see below).  Not recommended if *shownotches* is also
        True.  Otherwise, means will be shown as points.

    zorder : float, default: ``Line2D.zorder = 2``
        The zorder of the boxplot.

    Returns
    -------
    dict
      A dictionary mapping each component of the boxplot to a list
      of the `.Line2D` instances created. That dictionary has the
      following keys (assuming vertical boxplots):

      - ``boxes``: the main body of the boxplot showing the
        quartiles and the median's confidence intervals if
        enabled.

      - ``medians``: horizontal lines at the median of each box.

      - ``whiskers``: the vertical lines extending to the most
        extreme, non-outlier data points.

      - ``caps``: the horizontal lines at the ends of the
        whiskers.

      - ``fliers``: points representing data that extend beyond
        the whiskers (fliers).

      - ``means``: points or lines representing the means.

    Other Parameters
    ----------------
    showcaps : bool, default: :rc:`boxplot.showcaps`
        Show the caps on the ends of whiskers.
    showbox : bool, default: :rc:`boxplot.showbox`
        Show the central box.
    showfliers : bool, default: :rc:`boxplot.showfliers`
        Show the outliers beyond the caps.
    showmeans : bool, default: :rc:`boxplot.showmeans`
        Show the arithmetic means.
    capprops : dict, default: None
        The style of the caps.
    capwidths : float or array, default: None
        The widths of the caps.
    boxprops : dict, default: None
        The style of the box.
    whiskerprops : dict, default: None
        The style of the whiskers.
    flierprops : dict, default: None
        The style of the fliers.
    medianprops : dict, default: None
        The style of the median.
    meanprops : dict, default: None
        The style of the mean.
    label : str or list of str, optional
        Legend labels. Use a single string when all boxes have the same style and
        you only want a single legend entry for them. Use a list of strings to
        label all boxes individually. To be distinguishable, the boxes should be
        styled individually, which is currently only possible by modifying the
        returned artists, see e.g. :doc:`/gallery/statistics/boxplot_demo`.

        In the case of a single string, the legend entry will technically be
        associated with the first box only. By default, the legend will show the
        median line (``result["medians"]``); if *patch_artist* is True, the legend
        will show the box `.Patch` artists (``result["boxes"]``) instead.

        .. versionadded:: 3.9

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    See Also
    --------
    .Axes.bxp : Draw a boxplot from pre-computed statistics.
    violinplot : Draw an estimate of the probability density function.
    """

    # Missing arguments default to rcParams.
    whis = mpl._val_or_rc(whis, 'boxplot.whiskers')
    bootstrap = mpl._val_or_rc(bootstrap, 'boxplot.bootstrap')

    bxpstats = cbook.boxplot_stats(x, whis=whis, bootstrap=bootstrap,
                                   labels=tick_labels, autorange=autorange)
    notch = mpl._val_or_rc(notch, 'boxplot.notch')
    patch_artist = mpl._val_or_rc(patch_artist, 'boxplot.patchartist')
    meanline = mpl._val_or_rc(meanline, 'boxplot.meanline')
    showmeans = mpl._val_or_rc(showmeans, 'boxplot.showmeans')
    showcaps = mpl._val_or_rc(showcaps, 'boxplot.showcaps')
    showbox = mpl._val_or_rc(showbox, 'boxplot.showbox')
    showfliers = mpl._val_or_rc(showfliers, 'boxplot.showfliers')

    if boxprops is None:
        boxprops = {}
    if whiskerprops is None:
        whiskerprops = {}
    if capprops is None:
        capprops = {}
    if medianprops is None:
        medianprops = {}
    if meanprops is None:
        meanprops = {}
    if flierprops is None:
        flierprops = {}

    if patch_artist:
        boxprops['linestyle'] = 'solid'  # Not consistent with bxp.
        if 'color' in boxprops:
            boxprops['edgecolor'] = boxprops.pop('color')

    # if non-default sym value, put it into the flier dictionary
    # the logic for providing the default symbol ('b+') now lives
    # in bxp in the initial value of flierkw
    # handle all of the *sym* related logic here so we only have to pass
    # on the flierprops dict.
    if sym is not None:
        # no-flier case, which should really be done with
        # 'showfliers=False' but none-the-less deal with it to keep back
        # compatibility
        if sym == '':
            # blow away existing dict and make one for invisible markers
            flierprops = dict(linestyle='none', marker='', color='none')
            # turn the fliers off just to be safe
            showfliers = False
        # now process the symbol string
        else:
            # process the symbol string
            # discarded linestyle
            _, marker, color = _process_plot_format(sym)
            # if we have a marker, use it
            if marker is not None:
                flierprops['marker'] = marker
            # if we have a color, use it
            if color is not None:
                # assume that if color is passed in the user want
                # filled symbol, if the users want more control use
                # flierprops
                flierprops['color'] = color
                flierprops['markerfacecolor'] = color
                flierprops['markeredgecolor'] = color

    # replace medians if necessary:
    if usermedians is not None:
        if (len(np.ravel(usermedians)) != len(bxpstats) or
                np.shape(usermedians)[0] != len(bxpstats)):
            raise ValueError(
                "'usermedians' and 'x' have different lengths")
        else:
            # reassign medians as necessary
            for stats, med in zip(bxpstats, usermedians):
                if med is not None:
                    stats['med'] = med

    if conf_intervals is not None:
        if len(conf_intervals) != len(bxpstats):
            raise ValueError(
                "'conf_intervals' and 'x' have different lengths")
        else:
            for stats, ci in zip(bxpstats, conf_intervals):
                if ci is not None:
                    if len(ci) != 2:
                        raise ValueError('each confidence interval must '
                                         'have two values')
                    else:
                        if ci[0] is not None:
                            stats['cilo'] = ci[0]
                        if ci[1] is not None:
                            stats['cihi'] = ci[1]

    artists = self.bxp(bxpstats, positions=positions, widths=widths,
                       vert=vert, patch_artist=patch_artist,
                       shownotches=notch, showmeans=showmeans,
                       showcaps=showcaps, showbox=showbox,
                       boxprops=boxprops, flierprops=flierprops,
                       medianprops=medianprops, meanprops=meanprops,
                       meanline=meanline, showfliers=showfliers,
                       capprops=capprops, whiskerprops=whiskerprops,
                       manage_ticks=manage_ticks, zorder=zorder,
                       capwidths=capwidths, label=label,
                       orientation=orientation)
    return artists


# ==================================================
# Line: 4512

def bxp(self, bxpstats, positions=None, widths=None, vert=None,
        orientation='vertical', patch_artist=False, shownotches=False,
        showmeans=False, showcaps=True, showbox=True, showfliers=True,
        boxprops=None, whiskerprops=None, flierprops=None,
        medianprops=None, capprops=None, meanprops=None,
        meanline=False, manage_ticks=True, zorder=None,
        capwidths=None, label=None):
    """
    Draw a box and whisker plot from pre-computed statistics.

    The box extends from the first quartile *q1* to the third
    quartile *q3* of the data, with a line at the median (*med*).
    The whiskers extend from *whislow* to *whishi*.
    Flier points are markers past the end of the whiskers.
    See https://en.wikipedia.org/wiki/Box_plot for reference.

    .. code-block:: none

               whislow    q1    med    q3    whishi
                           |-----:-----|
           o      |--------|     :     |--------|    o  o
                           |-----:-----|
         flier                                      fliers

    .. note::
        This is a low-level drawing function for when you already
        have the statistical parameters. If you want a boxplot based
        on a dataset, use `~.Axes.boxplot` instead.

    Parameters
    ----------
    bxpstats : list of dicts
        A list of dictionaries containing stats for each boxplot.
        Required keys are:

        - ``med``: Median (float).
        - ``q1``, ``q3``: First & third quartiles (float).
        - ``whislo``, ``whishi``: Lower & upper whisker positions (float).

        Optional keys are:

        - ``mean``: Mean (float).  Needed if ``showmeans=True``.
        - ``fliers``: Data beyond the whiskers (array-like).
          Needed if ``showfliers=True``.
        - ``cilo``, ``cihi``: Lower & upper confidence intervals
          about the median. Needed if ``shownotches=True``.
        - ``label``: Name of the dataset (str).  If available,
          this will be used a tick label for the boxplot

    positions : array-like, default: [1, 2, ..., n]
        The positions of the boxes. The ticks and limits
        are automatically set to match the positions.

    widths : float or array-like, default: None
        The widths of the boxes.  The default is
        ``clip(0.15*(distance between extreme positions), 0.15, 0.5)``.

    capwidths : float or array-like, default: None
        Either a scalar or a vector and sets the width of each cap.
        The default is ``0.5*(width of the box)``, see *widths*.

    vert : bool, optional
        .. deprecated:: 3.11
            Use *orientation* instead.

            If this is given during the deprecation period, it overrides
            the *orientation* parameter.

        If True, plots the boxes vertically.
        If False, plots the boxes horizontally.

    orientation : {'vertical', 'horizontal'}, default: 'vertical'
        If 'horizontal', plots the boxes horizontally.
        Otherwise, plots the boxes vertically.

        .. versionadded:: 3.10

    patch_artist : bool, default: False
        If `False` produces boxes with the `.Line2D` artist.
        If `True` produces boxes with the `~matplotlib.patches.Patch` artist.

    shownotches, showmeans, showcaps, showbox, showfliers : bool
        Whether to draw the CI notches, the mean value (both default to
        False), the caps, the box, and the fliers (all three default to
        True).

    boxprops, whiskerprops, capprops, flierprops, medianprops, meanprops :\

# ==================================================
# Line: 5051

def scatter(self, x, y, s=None, c=None, marker=None, cmap=None, norm=None,
            vmin=None, vmax=None, alpha=None, linewidths=None, *,
            edgecolors=None, colorizer=None, plotnonfinite=False, **kwargs):
    """
    A scatter plot of *y* vs. *x* with varying marker size and/or color.

    Parameters
    ----------
    x, y : float or array-like, shape (n, )
        The data positions.

    s : float or array-like, shape (n, ), optional
        The marker size in points**2 (typographic points are 1/72 in.).
        Default is ``rcParams['lines.markersize'] ** 2``.

        The linewidth and edgecolor can visually interact with the marker
        size, and can lead to artifacts if the marker size is smaller than
        the linewidth.

        If the linewidth is greater than 0 and the edgecolor is anything
        but *'none'*, then the effective size of the marker will be
        increased by half the linewidth because the stroke will be centered
        on the edge of the shape.

        To eliminate the marker edge either set *linewidth=0* or
        *edgecolor='none'*.

    c : array-like or list of :mpltype:`color` or :mpltype:`color`, optional
        The marker colors. Possible values:

        - A scalar or sequence of n numbers to be mapped to colors using
          *cmap* and *norm*.
        - A 2D array in which the rows are RGB or RGBA.
        - A sequence of colors of length n.
        - A single color format string.

        Note that *c* should not be a single numeric RGB or RGBA sequence
        because that is indistinguishable from an array of values to be
        colormapped. If you want to specify the same RGB or RGBA value for
        all points, use a 2D array with a single row.  Otherwise,
        value-matching will have precedence in case of a size matching with
        *x* and *y*.

        If you wish to specify a single color for all points
        prefer the *color* keyword argument.

        Defaults to `None`. In that case the marker color is determined
        by the value of *color*, *facecolor* or *facecolors*. In case
        those are not specified or `None`, the marker color is determined
        by the next color of the ``Axes``' current "shape and fill" color
        cycle. This cycle defaults to :rc:`axes.prop_cycle`.

    marker : `~.markers.MarkerStyle`, default: :rc:`scatter.marker`
        The marker style. *marker* can be either an instance of the class
        or the text shorthand for a particular marker.
        See :mod:`matplotlib.markers` for more information about marker
        styles.

    %(cmap_doc)s

        This parameter is ignored if *c* is RGB(A).

    %(norm_doc)s

        This parameter is ignored if *c* is RGB(A).

    %(vmin_vmax_doc)s

        This parameter is ignored if *c* is RGB(A).

    alpha : float, default: None
        The alpha blending value, between 0 (transparent) and 1 (opaque).

    linewidths : float or array-like, default: :rc:`lines.linewidth`
        The linewidth of the marker edges. Note: The default *edgecolors*
        is 'face'. You may want to change this as well.

    edgecolors : {'face', 'none', *None*} or :mpltype:`color` or list of \

# ==================================================
# Line: 5344

def hexbin(self, x, y, C=None, gridsize=100, bins=None,
           xscale='linear', yscale='linear', extent=None,
           cmap=None, norm=None, vmin=None, vmax=None,
           alpha=None, linewidths=None, edgecolors='face',
           reduce_C_function=np.mean, mincnt=None, marginals=False,
           colorizer=None, **kwargs):
    """
    Make a 2D hexagonal binning plot of points *x*, *y*.

    If *C* is *None*, the value of the hexagon is determined by the number
    of points in the hexagon. Otherwise, *C* specifies values at the
    coordinate (x[i], y[i]). For each hexagon, these values are reduced
    using *reduce_C_function*.

    Parameters
    ----------
    x, y : array-like
        The data positions. *x* and *y* must be of the same length.

    C : array-like, optional
        If given, these values are accumulated in the bins. Otherwise,
        every point has a value of 1. Must be of the same length as *x*
        and *y*.

    gridsize : int or (int, int), default: 100
        If a single int, the number of hexagons in the *x*-direction.
        The number of hexagons in the *y*-direction is chosen such that
        the hexagons are approximately regular.

        Alternatively, if a tuple (*nx*, *ny*), the number of hexagons
        in the *x*-direction and the *y*-direction. In the
        *y*-direction, counting is done along vertically aligned
        hexagons, not along the zig-zag chains of hexagons; see the
        following illustration.

        .. plot::

           import numpy
           import matplotlib.pyplot as plt

           np.random.seed(19680801)
           n= 300
           x = np.random.standard_normal(n)
           y = np.random.standard_normal(n)

           fig, ax = plt.subplots(figsize=(4, 4))
           h = ax.hexbin(x, y, gridsize=(5, 3))
           hx, hy = h.get_offsets().T
           ax.plot(hx[24::3], hy[24::3], 'ro-')
           ax.plot(hx[-3:], hy[-3:], 'ro-')
           ax.set_title('gridsize=(5, 3)')
           ax.axis('off')

        To get approximately regular hexagons, choose
        :math:`n_x = \\sqrt{3}\\,n_y`.

    bins : 'log' or int or sequence, default: None
        Discretization of the hexagon values.

        - If *None*, no binning is applied; the color of each hexagon
          directly corresponds to its count value.
        - If 'log', use a logarithmic scale for the colormap.
          Internally, :math:`log_{10}(i+1)` is used to determine the
          hexagon color. This is equivalent to ``norm=LogNorm()``.
        - If an integer, divide the counts in the specified number
          of bins, and color the hexagons accordingly.
        - If a sequence of values, the values of the lower bound of
          the bins to be used.

    xscale : {'linear', 'log'}, default: 'linear'
        Use a linear or log10 scale on the horizontal axis.

    yscale : {'linear', 'log'}, default: 'linear'
        Use a linear or log10 scale on the vertical axis.

    mincnt : int >= 0, default: *None*
        If not *None*, only display cells with at least *mincnt*
        number of points in the cell.

    marginals : bool, default: *False*
        If marginals is *True*, plot the marginal density as
        colormapped rectangles along the bottom of the x-axis and
        left of the y-axis.

    extent : 4-tuple of float, default: *None*
        The limits of the bins (xmin, xmax, ymin, ymax).
        The default assigns the limits based on
        *gridsize*, *x*, *y*, *xscale* and *yscale*.

        If *xscale* or *yscale* is set to 'log', the limits are
        expected to be the exponent for a power of 10. E.g. for
        x-limits of 1 and 50 in 'linear' scale and y-limits
        of 10 and 1000 in 'log' scale, enter (1, 50, 1, 3).

    Returns
    -------
    `~matplotlib.collections.PolyCollection`
        A `.PolyCollection` defining the hexagonal bins.

        - `.PolyCollection.get_offsets` contains a Mx2 array containing
          the x, y positions of the M hexagon centers in data coordinates.
        - `.PolyCollection.get_array` contains the values of the M
          hexagons.

        If *marginals* is *True*, horizontal
        bar and vertical bar (both PolyCollections) will be attached
        to the return collection as attributes *hbar* and *vbar*.

    Other Parameters
    ----------------
    %(cmap_doc)s

    %(norm_doc)s

    %(vmin_vmax_doc)s

    alpha : float between 0 and 1, optional
        The alpha blending value, between 0 (transparent) and 1 (opaque).

    linewidths : float, default: *None*
        If *None*, defaults to :rc:`patch.linewidth`.

    edgecolors : {'face', 'none', *None*} or color, default: 'face'
        The color of the hexagon edges. Possible values are:

        - 'face': Draw the edges in the same color as the fill color.
        - 'none': No edges are drawn. This can sometimes lead to unsightly
          unpainted pixels between the hexagons.
        - *None*: Draw outlines in the default color.
        - An explicit color.

    reduce_C_function : callable, default: `numpy.mean`
        The function to aggregate *C* within the bins. It is ignored if
        *C* is not given. This must have the signature::

            def reduce_C_function(C: array) -> float

        Commonly used functions are:

        - `numpy.mean`: average of the points
        - `numpy.sum`: integral of the point values
        - `numpy.amax`: value taken from the largest point

        By default will only reduce cells with at least 1 point because some
        reduction functions (such as `numpy.amax`) will error/warn with empty
        input. Changing *mincnt* will adjust the cutoff, and if set to 0 will
        pass empty input to the reduction function.

    %(colorizer_doc)s

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs : `~matplotlib.collections.PolyCollection` properties
        All other keyword arguments are passed on to `.PolyCollection`:

        %(PolyCollection:kwdoc)s

    See Also
    --------
    hist2d : 2D histogram rectangular bins
    """
    self._process_unit_info([("x", x), ("y", y)], kwargs, convert=False)

    x, y, C = cbook.delete_masked_points(x, y, C)

    # Set the size of the hexagon grid
    if np.iterable(gridsize):
        nx, ny = gridsize
    else:
        nx = gridsize
        ny = int(nx / math.sqrt(3))
    # Count the number of data in each hexagon
    x = np.asarray(x, float)
    y = np.asarray(y, float)

    # Will be log()'d if necessary, and then rescaled.
    tx = x
    ty = y

    if xscale == 'log':
        if np.any(x <= 0.0):
            raise ValueError(
                "x contains non-positive values, so cannot be log-scaled")
        tx = np.log10(tx)
    if yscale == 'log':
        if np.any(y <= 0.0):
            raise ValueError(
                "y contains non-positive values, so cannot be log-scaled")
        ty = np.log10(ty)
    if extent is not None:
        xmin, xmax, ymin, ymax = extent
        if xmin > xmax:
            raise ValueError("In extent, xmax must be greater than xmin")
        if ymin > ymax:
            raise ValueError("In extent, ymax must be greater than ymin")
    else:
        xmin, xmax = (tx.min(), tx.max()) if len(x) else (0, 1)
        ymin, ymax = (ty.min(), ty.max()) if len(y) else (0, 1)

        # to avoid issues with singular data, expand the min/max pairs
        xmin, xmax = mtransforms.nonsingular(xmin, xmax, expander=0.1)
        ymin, ymax = mtransforms.nonsingular(ymin, ymax, expander=0.1)

    nx1 = nx + 1
    ny1 = ny + 1
    nx2 = nx
    ny2 = ny
    n = nx1 * ny1 + nx2 * ny2

    # In the x-direction, the hexagons exactly cover the region from
    # xmin to xmax. Need some padding to avoid roundoff errors.
    padding = 1.e-9 * (xmax - xmin)
    xmin -= padding
    xmax += padding
    sx = (xmax - xmin) / nx
    sy = (ymax - ymin) / ny
    # Positions in hexagon index coordinates.
    ix = (tx - xmin) / sx
    iy = (ty - ymin) / sy
    ix1 = np.round(ix).astype(int)
    iy1 = np.round(iy).astype(int)
    ix2 = np.floor(ix).astype(int)
    iy2 = np.floor(iy).astype(int)
    # flat indices, plus one so that out-of-range points go to position 0.
    i1 = np.where((0 <= ix1) & (ix1 < nx1) & (0 <= iy1) & (iy1 < ny1),
                  ix1 * ny1 + iy1 + 1, 0)
    i2 = np.where((0 <= ix2) & (ix2 < nx2) & (0 <= iy2) & (iy2 < ny2),
                  ix2 * ny2 + iy2 + 1, 0)

    d1 = (ix - ix1) ** 2 + 3.0 * (iy - iy1) ** 2
    d2 = (ix - ix2 - 0.5) ** 2 + 3.0 * (iy - iy2 - 0.5) ** 2
    bdist = (d1 < d2)

    if C is None:  # [1:] drops out-of-range points.
        counts1 = np.bincount(i1[bdist], minlength=1 + nx1 * ny1)[1:]
        counts2 = np.bincount(i2[~bdist], minlength=1 + nx2 * ny2)[1:]
        accum = np.concatenate([counts1, counts2]).astype(float)
        if mincnt is not None:
            accum[accum < mincnt] = np.nan
        C = np.ones(len(x))
    else:
        # store the C values in a list per hexagon index
        Cs_at_i1 = [[] for _ in range(1 + nx1 * ny1)]
        Cs_at_i2 = [[] for _ in range(1 + nx2 * ny2)]
        for i in range(len(x)):
            if bdist[i]:
                Cs_at_i1[i1[i]].append(C[i])
            else:
                Cs_at_i2[i2[i]].append(C[i])
        if mincnt is None:
            mincnt = 1
        accum = np.array(
            [reduce_C_function(acc) if len(acc) >= mincnt else np.nan
             for Cs_at_i in [Cs_at_i1, Cs_at_i2]
             for acc in Cs_at_i[1:]],  # [1:] drops out-of-range points.
            float)

    good_idxs = ~np.isnan(accum)

    offsets = np.zeros((n, 2), float)
    offsets[:nx1 * ny1, 0] = np.repeat(np.arange(nx1), ny1)
    offsets[:nx1 * ny1, 1] = np.tile(np.arange(ny1), nx1)
    offsets[nx1 * ny1:, 0] = np.repeat(np.arange(nx2) + 0.5, ny2)
    offsets[nx1 * ny1:, 1] = np.tile(np.arange(ny2), nx2) + 0.5
    offsets[:, 0] *= sx
    offsets[:, 1] *= sy
    offsets[:, 0] += xmin
    offsets[:, 1] += ymin
    # remove accumulation bins with no data
    offsets = offsets[good_idxs, :]
    accum = accum[good_idxs]

    polygon = [sx, sy / 3] * np.array(
        [[.5, -.5], [.5, .5], [0., 1.], [-.5, .5], [-.5, -.5], [0., -1.]])

    if linewidths is None:
        linewidths = [mpl.rcParams['patch.linewidth']]

    if xscale == 'log' or yscale == 'log':
        polygons = np.expand_dims(polygon, 0)
        if xscale == 'log':
            polygons[:, :, 0] = 10.0 ** polygons[:, :, 0]
            xmin = 10.0 ** xmin
            xmax = 10.0 ** xmax
            self.set_xscale(xscale)
        if yscale == 'log':
            polygons[:, :, 1] = 10.0 ** polygons[:, :, 1]
            ymin = 10.0 ** ymin
            ymax = 10.0 ** ymax
            self.set_yscale(yscale)
    else:
        polygons = [polygon]

    collection = mcoll.PolyCollection(
        polygons,
        edgecolors=edgecolors,
        linewidths=linewidths,
        offsets=offsets,
        offset_transform=mtransforms.AffineDeltaTransform(self.transData)
    )

    # Set normalizer if bins is 'log'
    if cbook._str_equal(bins, 'log'):
        if norm is not None:
            _api.warn_external("Only one of 'bins' and 'norm' arguments "
                               f"can be supplied, ignoring {bins=}")
        else:
            norm = mcolors.LogNorm(vmin=vmin, vmax=vmax)
            vmin = vmax = None
        bins = None

    if bins is not None:
        if not np.iterable(bins):
            minimum, maximum = min(accum), max(accum)
            bins -= 1  # one less edge than bins
            bins = minimum + (maximum - minimum) * np.arange(bins) / bins
        bins = np.sort(bins)
        accum = bins.searchsorted(accum)

    if colorizer:
        collection._set_colorizer_check_keywords(colorizer, cmap=cmap,
                                                 norm=norm, vmin=vmin,
                                                 vmax=vmax)
    else:
        collection.set_cmap(cmap)
        collection.set_norm(norm)
    collection.set_array(accum)
    collection.set_alpha(alpha)
    collection._internal_update(kwargs)
    collection._scale_norm(norm, vmin, vmax)

    # autoscale the norm with current accum values if it hasn't been set
    if norm is not None:
        if collection.norm.vmin is None and collection.norm.vmax is None:
            collection.norm.autoscale()

    corners = ((xmin, ymin), (xmax, ymax))
    self.update_datalim(corners)
    self._request_autoscale_view(tight=True)

    # add the collection last
    self.add_collection(collection, autolim=False)
    if not marginals:
        return collection

    # Process marginals
    bars = []
    for zname, z, zmin, zmax, zscale, nbins in [
            ("x", x, xmin, xmax, xscale, nx),
            ("y", y, ymin, ymax, yscale, 2 * ny),
    ]:

        if zscale == "log":
            bin_edges = np.geomspace(zmin, zmax, nbins + 1)
        else:
            bin_edges = np.linspace(zmin, zmax, nbins + 1)

        verts = np.empty((nbins, 4, 2))
        verts[:, 0, 0] = verts[:, 1, 0] = bin_edges[:-1]
        verts[:, 2, 0] = verts[:, 3, 0] = bin_edges[1:]
        verts[:, 0, 1] = verts[:, 3, 1] = .00
        verts[:, 1, 1] = verts[:, 2, 1] = .05
        if zname == "y":
            verts = verts[:, :, ::-1]  # Swap x and y.

        # Sort z-values into bins defined by bin_edges.
        bin_idxs = np.searchsorted(bin_edges, z) - 1
        values = np.empty(nbins)
        for i in range(nbins):
            # Get C-values for each bin, and compute bin value with
            # reduce_C_function.
            ci = C[bin_idxs == i]
            values[i] = reduce_C_function(ci) if len(ci) > 0 else np.nan

        mask = ~np.isnan(values)
        verts = verts[mask]
        values = values[mask]

        trans = getattr(self, f"get_{zname}axis_transform")(which="grid")
        bar = mcoll.PolyCollection(
            verts, transform=trans, edgecolors="face")
        bar.set_array(values)
        bar.set_cmap(cmap)
        bar.set_norm(norm)
        bar.set_alpha(alpha)
        bar._internal_update(kwargs)
        bars.append(self.add_collection(bar, autolim=False))

    collection.hbar, collection.vbar = bars

    def on_changed(collection):
        collection.hbar.set_cmap(collection.get_cmap())
        collection.hbar.set_cmap(collection.get_cmap())
        collection.vbar.set_clim(collection.get_clim())
        collection.vbar.set_clim(collection.get_clim())

    collection.callbacks.connect('changed', on_changed)

    return collection


# ==================================================
# Line: 5877

def _fill_between_x_or_y(
        self, ind_dir, ind, dep1, dep2=0, *,
        where=None, interpolate=False, step=None, **kwargs):
    # Common implementation between fill_between (*ind_dir*="x") and
    # fill_betweenx (*ind_dir*="y").  *ind* is the independent variable,
    # *dep* the dependent variable.  The docstring below is interpolated
    # to generate both methods' docstrings.
    """
    Fill the area between two {dir} curves.

    The curves are defined by the points (*{ind}*, *{dep}1*) and (*{ind}*,
    *{dep}2*).  This creates one or multiple polygons describing the filled
    area.

    You may exclude some {dir} sections from filling using *where*.

    By default, the edges connect the given points directly.  Use *step*
    if the filling should be a step function, i.e. constant in between
    *{ind}*.

    Parameters
    ----------
    {ind} : array-like
        The {ind} coordinates of the nodes defining the curves.

    {dep}1 : array-like or float
        The {dep} coordinates of the nodes defining the first curve.

    {dep}2 : array-like or float, default: 0
        The {dep} coordinates of the nodes defining the second curve.

    where : array-like of bool, optional
        Define *where* to exclude some {dir} regions from being filled.
        The filled regions are defined by the coordinates ``{ind}[where]``.
        More precisely, fill between ``{ind}[i]`` and ``{ind}[i+1]`` if
        ``where[i] and where[i+1]``.  Note that this definition implies
        that an isolated *True* value between two *False* values in *where*
        will not result in filling.  Both sides of the *True* position
        remain unfilled due to the adjacent *False* values.

    interpolate : bool, default: False
        This option is only relevant if *where* is used and the two curves
        are crossing each other.

        Semantically, *where* is often used for *{dep}1* > *{dep}2* or
        similar.  By default, the nodes of the polygon defining the filled
        region will only be placed at the positions in the *{ind}* array.
        Such a polygon cannot describe the above semantics close to the
        intersection.  The {ind}-sections containing the intersection are
        simply clipped.

        Setting *interpolate* to *True* will calculate the actual
        intersection point and extend the filled region up to this point.

    step : {{'pre', 'post', 'mid'}}, optional
        Define *step* if the filling should be a step function,
        i.e. constant in between *{ind}*.  The value determines where the
        step will occur:

        - 'pre': The {dep} value is continued constantly to the left from
          every *{ind}* position, i.e. the interval ``({ind}[i-1], {ind}[i]]``
          has the value ``{dep}[i]``.
        - 'post': The y value is continued constantly to the right from
          every *{ind}* position, i.e. the interval ``[{ind}[i], {ind}[i+1])``
          has the value ``{dep}[i]``.
        - 'mid': Steps occur half-way between the *{ind}* positions.

    Returns
    -------
    `.FillBetweenPolyCollection`
        A `.FillBetweenPolyCollection` containing the plotted polygons.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        All other keyword arguments are passed on to
        `.FillBetweenPolyCollection`. They control the `.Polygon` properties:

        %(FillBetweenPolyCollection:kwdoc)s

    See Also
    --------
    fill_between : Fill between two sets of y-values.
    fill_betweenx : Fill between two sets of x-values.
    """
    dep_dir = mcoll.FillBetweenPolyCollection._f_dir_from_t(ind_dir)

    if not mpl.rcParams["_internal.classic_mode"]:
        kwargs = cbook.normalize_kwargs(kwargs, mcoll.Collection)
        if not any(c in kwargs for c in ("color", "facecolor")):
            kwargs["facecolor"] = self._get_patches_for_fill.get_next_color()

    ind, dep1, dep2 = self._fill_between_process_units(
        ind_dir, dep_dir, ind, dep1, dep2, **kwargs)

    collection = mcoll.FillBetweenPolyCollection(
        ind_dir, ind, dep1, dep2,
        where=where, interpolate=interpolate, step=step, **kwargs)

    self.add_collection(collection)
    self._request_autoscale_view()
    return collection


# ==================================================
# Line: 5988

def fill_between(self, x, y1, y2=0, where=None, interpolate=False,
                 step=None, **kwargs):
    return self._fill_between_x_or_y(
        "x", x, y1, y2,
        where=where, interpolate=interpolate, step=step, **kwargs)


# ==================================================
# Line: 6002

def fill_betweenx(self, y, x1, x2=0, where=None,
                  step=None, interpolate=False, **kwargs):
    return self._fill_between_x_or_y(
        "y", y, x1, x2,
        where=where, interpolate=interpolate, step=step, **kwargs)


# ==================================================
# Line: 6020

def imshow(self, X, cmap=None, norm=None, *, aspect=None,
           interpolation=None, alpha=None,
           vmin=None, vmax=None, colorizer=None, origin=None, extent=None,
           interpolation_stage=None, filternorm=True, filterrad=4.0,
           resample=None, url=None, **kwargs):
    """
    Display data as an image, i.e., on a 2D regular raster.

    The input may either be actual RGB(A) data, or 2D scalar data, which
    will be rendered as a pseudocolor image. For displaying a grayscale
    image, set up the colormapping using the parameters
    ``cmap='gray', vmin=0, vmax=255``.

    The number of pixels used to render an image is set by the Axes size
    and the figure *dpi*. This can lead to aliasing artifacts when
    the image is resampled, because the displayed image size will usually
    not match the size of *X* (see
    :doc:`/gallery/images_contours_and_fields/image_antialiasing`).
    The resampling can be controlled via the *interpolation* parameter
    and/or :rc:`image.interpolation`.

    Parameters
    ----------
    X : array-like or PIL image
        The image data. Supported array shapes are:

        - (M, N): an image with scalar data. The values are mapped to
          colors using normalization and a colormap. See parameters *norm*,
          *cmap*, *vmin*, *vmax*.
        - (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
        - (M, N, 4): an image with RGBA values (0-1 float or 0-255 int),
          i.e. including transparency.

        The first two dimensions (M, N) define the rows and columns of
        the image.

        Out-of-range RGB(A) values are clipped.

    %(cmap_doc)s

        This parameter is ignored if *X* is RGB(A).

    %(norm_doc)s

        This parameter is ignored if *X* is RGB(A).

    %(vmin_vmax_doc)s

        This parameter is ignored if *X* is RGB(A).

    %(colorizer_doc)s

        This parameter is ignored if *X* is RGB(A).

    aspect : {'equal', 'auto'} or float or None, default: None
        The aspect ratio of the Axes.  This parameter is particularly
        relevant for images since it determines whether data pixels are
        square.

        This parameter is a shortcut for explicitly calling
        `.Axes.set_aspect`. See there for further details.

        - 'equal': Ensures an aspect ratio of 1. Pixels will be square
          (unless pixel sizes are explicitly made non-square in data
          coordinates using *extent*).
        - 'auto': The Axes is kept fixed and the aspect is adjusted so
          that the data fit in the Axes. In general, this will result in
          non-square pixels.

        Normally, None (the default) means to use :rc:`image.aspect`.  However, if
        the image uses a transform that does not contain the axes data transform,
        then None means to not modify the axes aspect at all (in that case, directly
        call `.Axes.set_aspect` if desired).

    interpolation : str, default: :rc:`image.interpolation`
        The interpolation method used.

        Supported values are 'none', 'auto', 'nearest', 'bilinear',
        'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite',
        'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell',
        'sinc', 'lanczos', 'blackman'.

        The data *X* is resampled to the pixel size of the image on the
        figure canvas, using the interpolation method to either up- or
        downsample the data.

        If *interpolation* is 'none', then for the ps, pdf, and svg
        backends no down- or upsampling occurs, and the image data is
        passed to the backend as a native image.  Note that different ps,
        pdf, and svg viewers may display these raw pixels differently. On
        other backends, 'none' is the same as 'nearest'.

        If *interpolation* is the default 'auto', then 'nearest'
        interpolation is used if the image is upsampled by more than a
        factor of three (i.e. the number of display pixels is at least
        three times the size of the data array).  If the upsampling rate is
        smaller than 3, or the image is downsampled, then 'hanning'
        interpolation is used to act as an anti-aliasing filter, unless the
        image happens to be upsampled by exactly a factor of two or one.

        See
        :doc:`/gallery/images_contours_and_fields/interpolation_methods`
        for an overview of the supported interpolation methods, and
        :doc:`/gallery/images_contours_and_fields/image_antialiasing` for
        a discussion of image antialiasing.

        Some interpolation methods require an additional radius parameter,
        which can be set by *filterrad*. Additionally, the antigrain image
        resize filter is controlled by the parameter *filternorm*.

    interpolation_stage : {'auto', 'data', 'rgba'}, default: 'auto'
        Supported values:

        - 'data': Interpolation is carried out on the data provided by the user
          This is useful if interpolating between pixels during upsampling.
        - 'rgba': The interpolation is carried out in RGBA-space after the
          color-mapping has been applied. This is useful if downsampling and
          combining pixels visually.
        - 'auto': Select a suitable interpolation stage automatically. This uses
          'rgba' when downsampling, or upsampling at a rate less than 3, and
          'data' when upsampling at a higher rate.

        See :doc:`/gallery/images_contours_and_fields/image_antialiasing` for
        a discussion of image antialiasing.

    alpha : float or array-like, optional
        The alpha blending value, between 0 (transparent) and 1 (opaque).
        If *alpha* is an array, the alpha blending values are applied pixel
        by pixel, and *alpha* must have the same shape as *X*.

    origin : {'upper', 'lower'}, default: :rc:`image.origin`
        Place the [0, 0] index of the array in the upper left or lower
        left corner of the Axes. The convention (the default) 'upper' is
        typically used for matrices and images.

        Note that the vertical axis points upward for 'lower'
        but downward for 'upper'.

        See the :ref:`imshow_extent` tutorial for
        examples and a more detailed description.

    extent : floats (left, right, bottom, top), optional
        The bounding box in data coordinates that the image will fill.
        These values may be unitful and match the units of the Axes.
        The image is stretched individually along x and y to fill the box.

        The default extent is determined by the following conditions.
        Pixels have unit size in data coordinates. Their centers are on
        integer coordinates, and their center coordinates range from 0 to
        columns-1 horizontally and from 0 to rows-1 vertically.

        Note that the direction of the vertical axis and thus the default
        values for top and bottom depend on *origin*:

        - For ``origin == 'upper'`` the default is
          ``(-0.5, numcols-0.5, numrows-0.5, -0.5)``.
        - For ``origin == 'lower'`` the default is
          ``(-0.5, numcols-0.5, -0.5, numrows-0.5)``.

        See the :ref:`imshow_extent` tutorial for
        examples and a more detailed description.

    filternorm : bool, default: True
        A parameter for the antigrain image resize filter (see the
        antigrain documentation).  If *filternorm* is set, the filter
        normalizes integer values and corrects the rounding errors. It
        doesn't do anything with the source floating point values, it
        corrects only integers according to the rule of 1.0 which means
        that any sum of pixel weights must be equal to 1.0.  So, the
        filter function must produce a graph of the proper shape.

    filterrad : float > 0, default: 4.0
        The filter radius for filters that have a radius parameter, i.e.
        when interpolation is one of: 'sinc', 'lanczos' or 'blackman'.

    resample : bool, default: :rc:`image.resample`
        When *True*, use a full resampling method.  When *False*, only
        resample when the output image is larger than the input image.

    url : str, optional
        Set the url of the created `.AxesImage`. See `.Artist.set_url`.

    Returns
    -------
    `~matplotlib.image.AxesImage`

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs : `~matplotlib.artist.Artist` properties
        These parameters are passed on to the constructor of the
        `.AxesImage` artist.

    See Also
    --------
    matshow : Plot a matrix or an array as an image.

    Notes
    -----
    Unless *extent* is used, pixel centers will be located at integer
    coordinates. In other words: the origin will coincide with the center
    of pixel (0, 0).

    There are two common representations for RGB images with an alpha
    channel:

    -   Straight (unassociated) alpha: R, G, and B channels represent the
        color of the pixel, disregarding its opacity.
    -   Premultiplied (associated) alpha: R, G, and B channels represent
        the color of the pixel, adjusted for its opacity by multiplication.

    `~matplotlib.pyplot.imshow` expects RGB images adopting the straight
    (unassociated) alpha representation.
    """
    im = mimage.AxesImage(self, cmap=cmap, norm=norm, colorizer=colorizer,
                          interpolation=interpolation, origin=origin,
                          extent=extent, filternorm=filternorm,
                          filterrad=filterrad, resample=resample,
                          interpolation_stage=interpolation_stage,
                          **kwargs)

    if aspect is None and not (
            im.is_transform_set()
            and not im.get_transform().contains_branch(self.transData)):
        aspect = mpl.rcParams['image.aspect']
    if aspect is not None:
        self.set_aspect(aspect)

    im.set_data(X)
    im.set_alpha(alpha)
    if im.get_clip_path() is None:
        # image does not already have clipping set, clip to Axes patch
        im.set_clip_path(self.patch)
    im._check_exclusionary_keywords(colorizer, vmin=vmin, vmax=vmax)
    im._scale_norm(norm, vmin, vmax)
    im.set_url(url)

    # update ax.dataLim, and, if autoscaling, set viewLim
    # to tightly fit the image, regardless of dataLim.
    im.set_extent(im.get_extent())

    self.add_image(im)
    return im


# ==================================================
# Line: 6381

def pcolor(self, *args, shading=None, alpha=None, norm=None, cmap=None,
           vmin=None, vmax=None, colorizer=None, **kwargs):
    r"""
    Create a pseudocolor plot with a non-regular rectangular grid.

    Call signature::

        pcolor([X, Y,] C, /, **kwargs)

    *X* and *Y* can be used to specify the corners of the quadrilaterals.

    The arguments *X*, *Y*, *C* are positional-only.

    .. hint::

        ``pcolor()`` can be very slow for large arrays. In most
        cases you should use the similar but much faster
        `~.Axes.pcolormesh` instead. See
        :ref:`Differences between pcolor() and pcolormesh()
        <differences-pcolor-pcolormesh>` for a discussion of the
        differences.

    Parameters
    ----------
    C : 2D array-like
        The color-mapped values.  Color-mapping is controlled by *cmap*,
        *norm*, *vmin*, and *vmax*.

    X, Y : array-like, optional
        The coordinates of the corners of quadrilaterals of a pcolormesh::

            (X[i+1, j], Y[i+1, j])       (X[i+1, j+1], Y[i+1, j+1])
                                  ●╶───╴●
                                  │     │
                                  ●╶───╴●
                (X[i, j], Y[i, j])       (X[i, j+1], Y[i, j+1])

        Note that the column index corresponds to the x-coordinate, and
        the row index corresponds to y. For details, see the
        :ref:`Notes <axes-pcolormesh-grid-orientation>` section below.

        If ``shading='flat'`` the dimensions of *X* and *Y* should be one
        greater than those of *C*, and the quadrilateral is colored due
        to the value at ``C[i, j]``.  If *X*, *Y* and *C* have equal
        dimensions, a warning will be raised and the last row and column
        of *C* will be ignored.

        If ``shading='nearest'``, the dimensions of *X* and *Y* should be
        the same as those of *C* (if not, a ValueError will be raised). The
        color ``C[i, j]`` will be centered on ``(X[i, j], Y[i, j])``.

        If *X* and/or *Y* are 1-D arrays or column vectors they will be
        expanded as needed into the appropriate 2D arrays, making a
        rectangular grid.

    shading : {'flat', 'nearest', 'auto'}, default: :rc:`pcolor.shading`
        The fill style for the quadrilateral. Possible values:

        - 'flat': A solid color is used for each quad. The color of the
          quad (i, j), (i+1, j), (i, j+1), (i+1, j+1) is given by
          ``C[i, j]``. The dimensions of *X* and *Y* should be
          one greater than those of *C*; if they are the same as *C*,
          then a deprecation warning is raised, and the last row
          and column of *C* are dropped.
        - 'nearest': Each grid point will have a color centered on it,
          extending halfway between the adjacent grid centers.  The
          dimensions of *X* and *Y* must be the same as *C*.
        - 'auto': Choose 'flat' if dimensions of *X* and *Y* are one
          larger than *C*.  Choose 'nearest' if dimensions are the same.

        See :doc:`/gallery/images_contours_and_fields/pcolormesh_grids`
        for more description.

    %(cmap_doc)s

    %(norm_doc)s

    %(vmin_vmax_doc)s

    %(colorizer_doc)s

    edgecolors : {'none', None, 'face', color, color sequence}, optional
        The color of the edges. Defaults to 'none'. Possible values:

        - 'none' or '': No edge.
        - *None*: :rc:`patch.edgecolor` will be used. Note that currently
          :rc:`patch.force_edgecolor` has to be True for this to work.
        - 'face': Use the adjacent face color.
        - A color or sequence of colors will set the edge color.

        The singular form *edgecolor* works as an alias.

    alpha : float, default: None
        The alpha blending value of the face color, between 0 (transparent)
        and 1 (opaque). Note: The edgecolor is currently not affected by
        this.

    snap : bool, default: False
        Whether to snap the mesh to pixel boundaries.

    Returns
    -------
    `matplotlib.collections.PolyQuadMesh`

    Other Parameters
    ----------------
    antialiaseds : bool, default: False
        The default *antialiaseds* is False if the default
        *edgecolors*\ ="none" is used.  This eliminates artificial lines
        at patch boundaries, and works regardless of the value of alpha.
        If *edgecolors* is not "none", then the default *antialiaseds*
        is taken from :rc:`patch.antialiased`.
        Stroking the edges may be preferred if *alpha* is 1, but will
        cause artifacts otherwise.

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Additionally, the following arguments are allowed. They are passed
        along to the `~matplotlib.collections.PolyQuadMesh` constructor:

    %(PolyCollection:kwdoc)s

    See Also
    --------
    pcolormesh : for an explanation of the differences between
        pcolor and pcolormesh.
    imshow : If *X* and *Y* are each equidistant, `~.Axes.imshow` can be a
        faster alternative.

    Notes
    -----
    **Masked arrays**

    *X*, *Y* and *C* may be masked arrays. If either ``C[i, j]``, or one
    of the vertices surrounding ``C[i, j]`` (*X* or *Y* at
    ``[i, j], [i+1, j], [i, j+1], [i+1, j+1]``) is masked, nothing is
    plotted.

    .. _axes-pcolor-grid-orientation:

    **Grid orientation**

    The grid orientation follows the standard matrix convention: An array
    *C* with shape (nrows, ncolumns) is plotted with the column number as
    *X* and the row number as *Y*.
    """

    if shading is None:
        shading = mpl.rcParams['pcolor.shading']
    shading = shading.lower()
    X, Y, C, shading = self._pcolorargs('pcolor', *args, shading=shading,
                                        kwargs=kwargs)
    linewidths = (0.25,)
    if 'linewidth' in kwargs:
        kwargs['linewidths'] = kwargs.pop('linewidth')
    kwargs.setdefault('linewidths', linewidths)

    if 'edgecolor' in kwargs:
        kwargs['edgecolors'] = kwargs.pop('edgecolor')
    ec = kwargs.setdefault('edgecolors', 'none')

    # aa setting will default via collections to patch.antialiased
    # unless the boundary is not stroked, in which case the
    # default will be False; with unstroked boundaries, aa
    # makes artifacts that are often disturbing.
    if 'antialiaseds' in kwargs:
        kwargs['antialiased'] = kwargs.pop('antialiaseds')
    if 'antialiased' not in kwargs and cbook._str_lower_equal(ec, "none"):
        kwargs['antialiased'] = False

    kwargs.setdefault('snap', False)

    if np.ma.isMaskedArray(X) or np.ma.isMaskedArray(Y):
        stack = np.ma.stack
        X = np.ma.asarray(X)
        Y = np.ma.asarray(Y)
        # For bounds collections later
        x = X.compressed()
        y = Y.compressed()
    else:
        stack = np.stack
        x = X
        y = Y
    coords = stack([X, Y], axis=-1)

    collection = mcoll.PolyQuadMesh(
        coords, array=C, cmap=cmap, norm=norm, colorizer=colorizer,
        alpha=alpha, **kwargs)
    collection._check_exclusionary_keywords(colorizer, vmin=vmin, vmax=vmax)
    collection._scale_norm(norm, vmin, vmax)

    coords = coords.reshape(-1, 2)  # flatten the grid structure; keep x, y
    self._update_pcolor_lims(collection, coords)
    return collection


# ==================================================
# Line: 6580

def pcolormesh(self, *args, alpha=None, norm=None, cmap=None, vmin=None,
               vmax=None, colorizer=None, shading=None, antialiased=False,
               **kwargs):
    """
    Create a pseudocolor plot with a non-regular rectangular grid.

    Call signature::

        pcolormesh([X, Y,] C, /, **kwargs)

    *X* and *Y* can be used to specify the corners of the quadrilaterals.

    The arguments *X*, *Y*, *C* are positional-only.

    .. hint::

       `~.Axes.pcolormesh` is similar to `~.Axes.pcolor`. It is much faster
       and preferred in most cases. For a detailed discussion on the
       differences see :ref:`Differences between pcolor() and pcolormesh()
       <differences-pcolor-pcolormesh>`.

    Parameters
    ----------
    C : array-like
        The mesh data. Supported array shapes are:

        - (M, N) or M*N: a mesh with scalar data. The values are mapped to
          colors using normalization and a colormap. See parameters *norm*,
          *cmap*, *vmin*, *vmax*.
        - (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
        - (M, N, 4): an image with RGBA values (0-1 float or 0-255 int),
          i.e. including transparency.

        The first two dimensions (M, N) define the rows and columns of
        the mesh data.

    X, Y : array-like, optional
        The coordinates of the corners of quadrilaterals of a pcolormesh::

            (X[i+1, j], Y[i+1, j])       (X[i+1, j+1], Y[i+1, j+1])
                                  ●╶───╴●
                                  │     │
                                  ●╶───╴●
                (X[i, j], Y[i, j])       (X[i, j+1], Y[i, j+1])

        Note that the column index corresponds to the x-coordinate, and
        the row index corresponds to y. For details, see the
        :ref:`Notes <axes-pcolormesh-grid-orientation>` section below.

        If ``shading='flat'`` the dimensions of *X* and *Y* should be one
        greater than those of *C*, and the quadrilateral is colored due
        to the value at ``C[i, j]``.  If *X*, *Y* and *C* have equal
        dimensions, a warning will be raised and the last row and column
        of *C* will be ignored.

        If ``shading='nearest'`` or ``'gouraud'``, the dimensions of *X*
        and *Y* should be the same as those of *C* (if not, a ValueError
        will be raised).  For ``'nearest'`` the color ``C[i, j]`` is
        centered on ``(X[i, j], Y[i, j])``.  For ``'gouraud'``, a smooth
        interpolation is carried out between the quadrilateral corners.

        If *X* and/or *Y* are 1-D arrays or column vectors they will be
        expanded as needed into the appropriate 2D arrays, making a
        rectangular grid.

    %(cmap_doc)s

    %(norm_doc)s

    %(vmin_vmax_doc)s

    %(colorizer_doc)s

    edgecolors : {'none', None, 'face', color, color sequence}, optional
        The color of the edges. Defaults to 'none'. Possible values:

        - 'none' or '': No edge.
        - *None*: :rc:`patch.edgecolor` will be used. Note that currently
          :rc:`patch.force_edgecolor` has to be True for this to work.
        - 'face': Use the adjacent face color.
        - A color or sequence of colors will set the edge color.

        The singular form *edgecolor* works as an alias.

    alpha : float, default: None
        The alpha blending value, between 0 (transparent) and 1 (opaque).

    shading : {'flat', 'nearest', 'gouraud', 'auto'}, optional
        The fill style for the quadrilateral; defaults to
        :rc:`pcolor.shading`. Possible values:

        - 'flat': A solid color is used for each quad. The color of the
          quad (i, j), (i+1, j), (i, j+1), (i+1, j+1) is given by
          ``C[i, j]``. The dimensions of *X* and *Y* should be
          one greater than those of *C*; if they are the same as *C*,
          then a deprecation warning is raised, and the last row
          and column of *C* are dropped.
        - 'nearest': Each grid point will have a color centered on it,
          extending halfway between the adjacent grid centers.  The
          dimensions of *X* and *Y* must be the same as *C*.
        - 'gouraud': Each quad will be Gouraud shaded: The color of the
          corners (i', j') are given by ``C[i', j']``. The color values of
          the area in between is interpolated from the corner values.
          The dimensions of *X* and *Y* must be the same as *C*. When
          Gouraud shading is used, *edgecolors* is ignored.
        - 'auto': Choose 'flat' if dimensions of *X* and *Y* are one
          larger than *C*.  Choose 'nearest' if dimensions are the same.

        See :doc:`/gallery/images_contours_and_fields/pcolormesh_grids`
        for more description.

    snap : bool, default: False
        Whether to snap the mesh to pixel boundaries.

    rasterized : bool, optional
        Rasterize the pcolormesh when drawing vector graphics.  This can
        speed up rendering and produce smaller files for large data sets.
        See also :doc:`/gallery/misc/rasterization_demo`.

    Returns
    -------
    `matplotlib.collections.QuadMesh`

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Additionally, the following arguments are allowed. They are passed
        along to the `~matplotlib.collections.QuadMesh` constructor:

    %(QuadMesh:kwdoc)s

    See Also
    --------
    pcolor : An alternative implementation with slightly different
        features. For a detailed discussion on the differences see
        :ref:`Differences between pcolor() and pcolormesh()
        <differences-pcolor-pcolormesh>`.
    imshow : If *X* and *Y* are each equidistant, `~.Axes.imshow` can be a
        faster alternative.

    Notes
    -----
    **Masked arrays**

    *C* may be a masked array. If ``C[i, j]`` is masked, the corresponding
    quadrilateral will be transparent. Masking of *X* and *Y* is not
    supported. Use `~.Axes.pcolor` if you need this functionality.

    .. _axes-pcolormesh-grid-orientation:

    **Grid orientation**

    The grid orientation follows the standard matrix convention: An array
    *C* with shape (nrows, ncolumns) is plotted with the column number as
    *X* and the row number as *Y*.

    .. _differences-pcolor-pcolormesh:

    **Differences between pcolor() and pcolormesh()**

    Both methods are used to create a pseudocolor plot of a 2D array
    using quadrilaterals.

    The main difference lies in the created object and internal data
    handling:
    While `~.Axes.pcolor` returns a `.PolyQuadMesh`, `~.Axes.pcolormesh`
    returns a `.QuadMesh`. The latter is more specialized for the given
    purpose and thus is faster. It should almost always be preferred.

    There is also a slight difference in the handling of masked arrays.
    Both `~.Axes.pcolor` and `~.Axes.pcolormesh` support masked arrays
    for *C*. However, only `~.Axes.pcolor` supports masked arrays for *X*
    and *Y*. The reason lies in the internal handling of the masked values.
    `~.Axes.pcolor` leaves out the respective polygons from the
    PolyQuadMesh. `~.Axes.pcolormesh` sets the facecolor of the masked
    elements to transparent. You can see the difference when using
    edgecolors. While all edges are drawn irrespective of masking in a
    QuadMesh, the edge between two adjacent masked quadrilaterals in
    `~.Axes.pcolor` is not drawn as the corresponding polygons do not
    exist in the PolyQuadMesh. Because PolyQuadMesh draws each individual
    polygon, it also supports applying hatches and linestyles to the collection.

    Another difference is the support of Gouraud shading in
    `~.Axes.pcolormesh`, which is not available with `~.Axes.pcolor`.

    """
    shading = mpl._val_or_rc(shading, 'pcolor.shading').lower()
    kwargs.setdefault('edgecolors', 'none')

    X, Y, C, shading = self._pcolorargs('pcolormesh', *args,
                                        shading=shading, kwargs=kwargs)
    coords = np.stack([X, Y], axis=-1)

    kwargs.setdefault('snap', mpl.rcParams['pcolormesh.snap'])

    collection = mcoll.QuadMesh(
        coords, antialiased=antialiased, shading=shading,
        array=C, cmap=cmap, norm=norm, colorizer=colorizer, alpha=alpha, **kwargs)
    collection._check_exclusionary_keywords(colorizer, vmin=vmin, vmax=vmax)
    collection._scale_norm(norm, vmin, vmax)

    coords = coords.reshape(-1, 2)  # flatten the grid structure; keep x, y
    self._update_pcolor_lims(collection, coords)
    return collection


# ==================================================
# Line: 6813

def pcolorfast(self, *args, alpha=None, norm=None, cmap=None, vmin=None,
               vmax=None, colorizer=None, **kwargs):
    """
    Create a pseudocolor plot with a non-regular rectangular grid.

    Call signature::

        ax.pcolorfast([X, Y], C, /, **kwargs)

    The arguments *X*, *Y*, *C* are positional-only.

    This method is similar to `~.Axes.pcolor` and `~.Axes.pcolormesh`.
    It's designed to provide the fastest pcolor-type plotting with the
    Agg backend. To achieve this, it uses different algorithms internally
    depending on the complexity of the input grid (regular rectangular,
    non-regular rectangular or arbitrary quadrilateral).

    .. warning::

        This method is experimental. Compared to `~.Axes.pcolor` or
        `~.Axes.pcolormesh` it has some limitations:

        - It supports only flat shading (no outlines)
        - It lacks support for log scaling of the axes.
        - It does not have a pyplot wrapper.

    Parameters
    ----------
    C : array-like
        The image data. Supported array shapes are:

        - (M, N): an image with scalar data.  Color-mapping is controlled
          by *cmap*, *norm*, *vmin*, and *vmax*.
        - (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
        - (M, N, 4): an image with RGBA values (0-1 float or 0-255 int),
          i.e. including transparency.

        The first two dimensions (M, N) define the rows and columns of
        the image.

        This parameter can only be passed positionally.

    X, Y : tuple or array-like, default: ``(0, N)``, ``(0, M)``
        *X* and *Y* are used to specify the coordinates of the
        quadrilaterals. There are different ways to do this:

        - Use tuples ``X=(xmin, xmax)`` and ``Y=(ymin, ymax)`` to define
          a *uniform rectangular grid*.

          The tuples define the outer edges of the grid. All individual
          quadrilaterals will be of the same size. This is the fastest
          version.

        - Use 1D arrays *X*, *Y* to specify a *non-uniform rectangular
          grid*.

          In this case *X* and *Y* have to be monotonic 1D arrays of length
          *N+1* and *M+1*, specifying the x and y boundaries of the cells.

          The speed is intermediate. Note: The grid is checked, and if
          found to be uniform the fast version is used.

        - Use 2D arrays *X*, *Y* if you need an *arbitrary quadrilateral
          grid* (i.e. if the quadrilaterals are not rectangular).

          In this case *X* and *Y* are 2D arrays with shape (M + 1, N + 1),
          specifying the x and y coordinates of the corners of the colored
          quadrilaterals.

          This is the most general, but the slowest to render.  It may
          produce faster and more compact output using ps, pdf, and
          svg backends, however.

        These arguments can only be passed positionally.

    %(cmap_doc)s

        This parameter is ignored if *C* is RGB(A).

    %(norm_doc)s

        This parameter is ignored if *C* is RGB(A).

    %(vmin_vmax_doc)s

        This parameter is ignored if *C* is RGB(A).

    %(colorizer_doc)s

        This parameter is ignored if *C* is RGB(A).

    alpha : float, default: None
        The alpha blending value, between 0 (transparent) and 1 (opaque).

    snap : bool, default: False
        Whether to snap the mesh to pixel boundaries.

    Returns
    -------
    `.AxesImage` or `.PcolorImage` or `.QuadMesh`
        The return type depends on the type of grid:

        - `.AxesImage` for a regular rectangular grid.
        - `.PcolorImage` for a non-regular rectangular grid.
        - `.QuadMesh` for a non-rectangular grid.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Supported additional parameters depend on the type of grid.
        See return types of *image* for further description.
    """

    C = args[-1]
    nr, nc = np.shape(C)[:2]
    if len(args) == 1:
        style = "image"
        x = [0, nc]
        y = [0, nr]
    elif len(args) == 3:
        x, y = args[:2]
        x = np.asarray(x)
        y = np.asarray(y)
        if x.ndim == 1 and y.ndim == 1:
            if x.size == 2 and y.size == 2:
                style = "image"
            else:
                if x.size != nc + 1:
                    raise ValueError(
                        f"Length of X ({x.size}) must be one larger than the "
                        f"number of columns in C ({nc})")
                if y.size != nr + 1:
                    raise ValueError(
                        f"Length of Y ({y.size}) must be one larger than the "
                        f"number of rows in C ({nr})"
                    )
                dx = np.diff(x)
                dy = np.diff(y)
                if (np.ptp(dx) < 0.01 * abs(dx.mean()) and
                        np.ptp(dy) < 0.01 * abs(dy.mean())):
                    style = "image"
                else:
                    style = "pcolorimage"
        elif x.ndim == 2 and y.ndim == 2:
            style = "quadmesh"
        else:
            raise TypeError(
                f"When 3 positional parameters are passed to pcolorfast, the first "
                f"two (X and Y) must be both 1D or both 2D; the given X was "
                f"{x.ndim}D and the given Y was {y.ndim}D")
    else:
        raise _api.nargs_error('pcolorfast', '1 or 3', len(args))

    mcolorizer.ColorizingArtist._check_exclusionary_keywords(colorizer, vmin=vmin,
                                                             vmax=vmax)
    if style == "quadmesh":
        # data point in each cell is value at lower left corner
        coords = np.stack([x, y], axis=-1)
        if np.ndim(C) not in {2, 3}:
            raise ValueError("C must be 2D or 3D")
        collection = mcoll.QuadMesh(
            coords, array=C,
            alpha=alpha, cmap=cmap, norm=norm, colorizer=colorizer,
            antialiased=False, edgecolors="none")
        self.add_collection(collection, autolim=False)
        xl, xr, yb, yt = x.min(), x.max(), y.min(), y.max()
        ret = collection

    else:  # It's one of the two image styles.
        extent = xl, xr, yb, yt = x[0], x[-1], y[0], y[-1]
        if style == "image":
            im = mimage.AxesImage(
                self, cmap=cmap, norm=norm, colorizer=colorizer,
                data=C, alpha=alpha, extent=extent,
                interpolation='nearest', origin='lower',
                **kwargs)
        elif style == "pcolorimage":
            im = mimage.PcolorImage(
                self, x, y, C,
                cmap=cmap, norm=norm, colorizer=colorizer, alpha=alpha,
                extent=extent, **kwargs)
        self.add_image(im)
        ret = im

    if np.ndim(C) == 2:  # C.ndim == 3 is RGB(A) so doesn't need scaling.
        ret._scale_norm(norm, vmin, vmax)

    if ret.get_clip_path() is None:
        # image does not already have clipping set, clip to Axes patch
        ret.set_clip_path(self.patch)

    ret.sticky_edges.x[:] = [xl, xr]
    ret.sticky_edges.y[:] = [yb, yt]
    self.update_datalim(np.array([[xl, yb], [xr, yt]]))
    self._request_autoscale_view(tight=True)
    return ret


# ==================================================
# Line: 7073

    def hist(self, x, bins=None, range=None, density=False, weights=None,
             cumulative=False, bottom=None, histtype='bar', align='mid',
             orientation='vertical', rwidth=None, log=False,
             color=None, label=None, stacked=False, **kwargs):
        """
        Compute and plot a histogram.

        This method uses `numpy.histogram` to bin the data in *x* and count the
        number of values in each bin, then draws the distribution either as a
        `.BarContainer` or `.Polygon`. The *bins*, *range*, *density*, and
        *weights* parameters are forwarded to `numpy.histogram`.

        If the data has already been binned and counted, use `~.bar` or
        `~.stairs` to plot the distribution::

            counts, bins = np.histogram(x)
            plt.stairs(counts, bins)

        Alternatively, plot pre-computed bins and counts using ``hist()`` by
        treating each bin as a single point with a weight equal to its count::

            plt.hist(bins[:-1], bins, weights=counts)

        The data input *x* can be a singular array, a list of datasets of
        potentially different lengths ([*x0*, *x1*, ...]), or a 2D ndarray in
        which each column is a dataset. Note that the ndarray form is
        transposed relative to the list form. If the input is an array, then
        the return value is a tuple (*n*, *bins*, *patches*); if the input is a
        sequence of arrays, then the return value is a tuple
        ([*n0*, *n1*, ...], *bins*, [*patches0*, *patches1*, ...]).

        Masked arrays are not supported.

        Parameters
        ----------
        x : (n,) array or sequence of (n,) arrays
            Input values, this takes either a single array or a sequence of
            arrays which are not required to be of the same length.

        bins : int or sequence or str, default: :rc:`hist.bins`
            If *bins* is an integer, it defines the number of equal-width bins
            in the range.

            If *bins* is a sequence, it defines the bin edges, including the
            left edge of the first bin and the right edge of the last bin;
            in this case, bins may be unequally spaced.  All but the last
            (righthand-most) bin is half-open.  In other words, if *bins* is::

                [1, 2, 3, 4]

            then the first bin is ``[1, 2)`` (including 1, but excluding 2) and
            the second ``[2, 3)``.  The last bin, however, is ``[3, 4]``, which
            *includes* 4.

            If *bins* is a string, it is one of the binning strategies
            supported by `numpy.histogram_bin_edges`: 'auto', 'fd', 'doane',
            'scott', 'stone', 'rice', 'sturges', or 'sqrt'.

        range : tuple or None, default: None
            The lower and upper range of the bins. Lower and upper outliers
            are ignored. If not provided, *range* is ``(x.min(), x.max())``.
            Range has no effect if *bins* is a sequence.

            If *bins* is a sequence or *range* is specified, autoscaling
            is based on the specified bin range instead of the
            range of x.

        density : bool, default: False
            If ``True``, draw and return a probability density: each bin
            will display the bin's raw count divided by the total number of
            counts *and the bin width*
            (``density = counts / (sum(counts) * np.diff(bins))``),
            so that the area under the histogram integrates to 1
            (``np.sum(density * np.diff(bins)) == 1``).

            If *stacked* is also ``True``, the sum of the histograms is
            normalized to 1.

        weights : (n,) array-like or None, default: None
            An array of weights, of the same shape as *x*.  Each value in
            *x* only contributes its associated weight towards the bin count
            (instead of 1).  If *density* is ``True``, the weights are
            normalized, so that the integral of the density over the range
            remains 1.

        cumulative : bool or -1, default: False
            If ``True``, then a histogram is computed where each bin gives the
            counts in that bin plus all bins for smaller values. The last bin
            gives the total number of datapoints.

            If *density* is also ``True`` then the histogram is normalized such
            that the last bin equals 1.

            If *cumulative* is a number less than 0 (e.g., -1), the direction
            of accumulation is reversed.  In this case, if *density* is also
            ``True``, then the histogram is normalized such that the first bin
            equals 1.

        bottom : array-like or float, default: 0
            Location of the bottom of each bin, i.e. bins are drawn from
            ``bottom`` to ``bottom + hist(x, bins)`` If a scalar, the bottom
            of each bin is shifted by the same amount. If an array, each bin
            is shifted independently and the length of bottom must match the
            number of bins. If None, defaults to 0.

        histtype : {'bar', 'barstacked', 'step', 'stepfilled'}, default: 'bar'
            The type of histogram to draw.

            - 'bar' is a traditional bar-type histogram.  If multiple data
              are given the bars are arranged side by side.
            - 'barstacked' is a bar-type histogram where multiple
              data are stacked on top of each other.
            - 'step' generates a lineplot that is by default unfilled.
            - 'stepfilled' generates a lineplot that is by default filled.

        align : {'left', 'mid', 'right'}, default: 'mid'
            The horizontal alignment of the histogram bars.

            - 'left': bars are centered on the left bin edges.
            - 'mid': bars are centered between the bin edges.
            - 'right': bars are centered on the right bin edges.

        orientation : {'vertical', 'horizontal'}, default: 'vertical'
            If 'horizontal', `~.Axes.barh` will be used for bar-type histograms
            and the *bottom* kwarg will be the left edges.

        rwidth : float or None, default: None
            The relative width of the bars as a fraction of the bin width.  If
            ``None``, automatically compute the width.

            Ignored if *histtype* is 'step' or 'stepfilled'.

        log : bool, default: False
            If ``True``, the histogram axis will be set to a log scale.

        color : :mpltype:`color` or list of :mpltype:`color` or None, default: None
            Color or sequence of colors, one per dataset.  Default (``None``)
            uses the standard line color sequence.

        label : str or list of str, optional
            String, or sequence of strings to match multiple datasets.  Bar
            charts yield multiple patches per dataset, but only the first gets
            the label, so that `~.Axes.legend` will work as expected.

        stacked : bool, default: False
            If ``True``, multiple data are stacked on top of each other If
            ``False`` multiple data are arranged side by side if histtype is
            'bar' or on top of each other if histtype is 'step'

        Returns
        -------
        n : array or list of arrays
            The values of the histogram bins. See *density* and *weights* for a
            description of the possible semantics.  If input *x* is an array,
            then this is an array of length *nbins*. If input is a sequence of
            arrays ``[data1, data2, ...]``, then this is a list of arrays with
            the values of the histograms for each of the arrays in the same
            order.  The dtype of the array *n* (or of its element arrays) will
            always be float even if no weighting or normalization is used.

        bins : array
            The edges of the bins. Length nbins + 1 (nbins left edges and right
            edge of last bin).  Always a single array even when multiple data
            sets are passed in.

        patches : `.BarContainer` or list of a single `.Polygon` or list of \
such objects
            Container of individual artists used to create the histogram
            or list of such containers if there are multiple input datasets.

        Other Parameters
        ----------------
        data : indexable object, optional
            DATA_PARAMETER_PLACEHOLDER

        **kwargs
            `~matplotlib.patches.Patch` properties. The following properties
            additionally accept a sequence of values corresponding to the
            datasets in *x*:
            *edgecolor*, *facecolor*, *linewidth*, *linestyle*, *hatch*.

            .. versionadded:: 3.10
               Allowing sequences of values in above listed Patch properties.

        See Also
        --------
        hist2d : 2D histogram with rectangular bins
        hexbin : 2D histogram with hexagonal bins
        stairs : Plot a pre-computed histogram
        bar : Plot a pre-computed histogram

        Notes
        -----
        For large numbers of bins (>1000), plotting can be significantly
        accelerated by using `~.Axes.stairs` to plot a pre-computed histogram
        (``plt.stairs(*np.histogram(data))``), or by setting *histtype* to
        'step' or 'stepfilled' rather than 'bar' or 'barstacked'.
        """
        # Avoid shadowing the builtin.
        bin_range = range
        from builtins import range

        kwargs = cbook.normalize_kwargs(kwargs, mpatches.Patch)

        if np.isscalar(x):
            x = [x]

        bins = mpl._val_or_rc(bins, 'hist.bins')

        # Validate string inputs here to avoid cluttering subsequent code.
        _api.check_in_list(['bar', 'barstacked', 'step', 'stepfilled'],
                           histtype=histtype)
        _api.check_in_list(['left', 'mid', 'right'], align=align)
        _api.check_in_list(['horizontal', 'vertical'], orientation=orientation)

        if histtype == 'barstacked' and not stacked:
            stacked = True

        # Massage 'x' for processing.
        x = cbook._reshape_2D(x, 'x')
        nx = len(x)  # number of datasets

        # Process unit information.  _process_unit_info sets the unit and
        # converts the first dataset; then we convert each following dataset
        # one at a time.
        if orientation == "vertical":
            convert_units = self.convert_xunits
            x = [*self._process_unit_info([("x", x[0])], kwargs),
                 *map(convert_units, x[1:])]
        else:  # horizontal
            convert_units = self.convert_yunits
            x = [*self._process_unit_info([("y", x[0])], kwargs),
                 *map(convert_units, x[1:])]

        if bin_range is not None:
            bin_range = convert_units(bin_range)

        if not cbook.is_scalar_or_string(bins):
            bins = convert_units(bins)

        # We need to do to 'weights' what was done to 'x'
        if weights is not None:
            w = cbook._reshape_2D(weights, 'weights')
        else:
            w = [None] * nx

        if len(w) != nx:
            raise ValueError('weights should have the same shape as x')

        input_empty = True
        for xi, wi in zip(x, w):
            len_xi = len(xi)
            if wi is not None and len(wi) != len_xi:
                raise ValueError('weights should have the same shape as x')
            if len_xi:
                input_empty = False

        if color is None:
            colors = [self._get_lines.get_next_color() for i in range(nx)]
        else:
            colors = mcolors.to_rgba_array(color)
            if len(colors) != nx:
                raise ValueError(f"The 'color' keyword argument must have one "
                                 f"color per dataset, but {nx} datasets and "
                                 f"{len(colors)} colors were provided")

        hist_kwargs = dict()

        # if the bin_range is not given, compute without nan numpy
        # does not do this for us when guessing the range (but will
        # happily ignore nans when computing the histogram).
        if bin_range is None:
            xmin = np.inf
            xmax = -np.inf
            for xi in x:
                if len(xi):
                    # python's min/max ignore nan,
                    # np.minnan returns nan for all nan input
                    xmin = min(xmin, np.nanmin(xi))
                    xmax = max(xmax, np.nanmax(xi))
            if xmin <= xmax:  # Only happens if we have seen a finite value.
                bin_range = (xmin, xmax)

        # If bins are not specified either explicitly or via range,
        # we need to figure out the range required for all datasets,
        # and supply that to np.histogram.
        if not input_empty and len(x) > 1:
            if weights is not None:
                _w = np.concatenate(w)
            else:
                _w = None
            bins = np.histogram_bin_edges(
                np.concatenate(x), bins, bin_range, _w)
        else:
            hist_kwargs['range'] = bin_range

        density = bool(density)
        if density and not stacked:
            hist_kwargs['density'] = density

        # List to store all the top coordinates of the histograms
        tops = []  # Will have shape (n_datasets, n_bins).
        # Loop through datasets
        for i in range(nx):
            # this will automatically overwrite bins,
            # so that each histogram uses the same bins
            m, bins = np.histogram(x[i], bins, weights=w[i], **hist_kwargs)
            tops.append(m)
        tops = np.array(tops, float)  # causes problems later if it's an int
        bins = np.array(bins, float)  # causes problems if float16
        if stacked:
            tops = tops.cumsum(axis=0)
            # If a stacked density plot, normalize so the area of all the
            # stacked histograms together is 1
            if density:
                tops = (tops / np.diff(bins)) / tops[-1].sum()
        if cumulative:
            slc = slice(None)
            if isinstance(cumulative, Number) and cumulative < 0:
                slc = slice(None, None, -1)
            if density:
                tops = (tops * np.diff(bins))[:, slc].cumsum(axis=1)[:, slc]
            else:
                tops = tops[:, slc].cumsum(axis=1)[:, slc]

        patches = []

        if histtype.startswith('bar'):

            totwidth = np.diff(bins)

            if rwidth is not None:
                dr = np.clip(rwidth, 0, 1)
            elif (len(tops) > 1 and
                  ((not stacked) or mpl.rcParams['_internal.classic_mode'])):
                dr = 0.8
            else:
                dr = 1.0

            if histtype == 'bar' and not stacked:
                width = dr * totwidth / nx
                dw = width
                boffset = -0.5 * dr * totwidth * (1 - 1 / nx)
            elif histtype == 'barstacked' or stacked:
                width = dr * totwidth
                boffset, dw = 0.0, 0.0

            if align == 'mid':
                boffset += 0.5 * totwidth
            elif align == 'right':
                boffset += totwidth

            if orientation == 'horizontal':
                _barfunc = self.barh
                bottom_kwarg = 'left'
            else:  # orientation == 'vertical'
                _barfunc = self.bar
                bottom_kwarg = 'bottom'

            for top, color in zip(tops, colors):
                if bottom is None:
                    bottom = np.zeros(len(top))
                if stacked:
                    height = top - bottom
                else:
                    height = top
                bars = _barfunc(bins[:-1]+boffset, height, width,
                                align='center', log=log,
                                color=color, **{bottom_kwarg: bottom})
                patches.append(bars)
                if stacked:
                    bottom = top
                boffset += dw
            # Remove stickies from all bars but the lowest ones, as otherwise
            # margin expansion would be unable to cross the stickies in the
            # middle of the bars.
            for bars in patches[1:]:
                for patch in bars:
                    patch.sticky_edges.x[:] = patch.sticky_edges.y[:] = []

        elif histtype.startswith('step'):
            # these define the perimeter of the polygon
            x = np.zeros(4 * len(bins) - 3)
            y = np.zeros(4 * len(bins) - 3)

            x[0:2*len(bins)-1:2], x[1:2*len(bins)-1:2] = bins, bins[:-1]
            x[2*len(bins)-1:] = x[1:2*len(bins)-1][::-1]

            if bottom is None:
                bottom = 0

            y[1:2*len(bins)-1:2] = y[2:2*len(bins):2] = bottom
            y[2*len(bins)-1:] = y[1:2*len(bins)-1][::-1]

            if log:
                if orientation == 'horizontal':
                    self.set_xscale('log', nonpositive='clip')
                else:  # orientation == 'vertical'
                    self.set_yscale('log', nonpositive='clip')

            if align == 'left':
                x -= 0.5*(bins[1]-bins[0])
            elif align == 'right':
                x += 0.5*(bins[1]-bins[0])

            # If fill kwarg is set, it will be passed to the patch collection,
            # overriding this
            fill = (histtype == 'stepfilled')

            xvals, yvals = [], []
            for top in tops:
                if stacked:
                    # top of the previous polygon becomes the bottom
                    y[2*len(bins)-1:] = y[1:2*len(bins)-1][::-1]
                # set the top of this polygon
                y[1:2*len(bins)-1:2] = y[2:2*len(bins):2] = top + bottom

                # The starting point of the polygon has not yet been
                # updated. So far only the endpoint was adjusted. This
                # assignment closes the polygon. The redundant endpoint is
                # later discarded (for step and stepfilled).
                y[0] = y[-1]

                if orientation == 'horizontal':
                    xvals.append(y.copy())
                    yvals.append(x.copy())
                else:
                    xvals.append(x.copy())
                    yvals.append(y.copy())

            # stepfill is closed, step is not
            split = -1 if fill else 2 * len(bins)
            # add patches in reverse order so that when stacking,
            # items lower in the stack are plotted on top of
            # items higher in the stack
            for x, y, color in reversed(list(zip(xvals, yvals, colors))):
                patches.append(self.fill(
                    x[:split], y[:split],
                    closed=True if fill else None,
                    facecolor=color,
                    edgecolor=None if fill else color,
                    fill=fill if fill else None,
                    zorder=None if fill else mlines.Line2D.zorder))
            for patch_list in patches:
                for patch in patch_list:
                    if orientation == 'vertical':
                        patch.sticky_edges.y.append(0)
                    elif orientation == 'horizontal':
                        patch.sticky_edges.x.append(0)

            # we return patches, so put it back in the expected order
            patches.reverse()

        # If None, make all labels None (via zip_longest below); otherwise,
        # cast each element to str, but keep a single str as it.
        labels = [] if label is None else np.atleast_1d(np.asarray(label, str))

        if histtype == "step":
            ec = kwargs.get('edgecolor', colors)
        else:
            ec = kwargs.get('edgecolor', None)
        if ec is None or cbook._str_lower_equal(ec, 'none'):
            edgecolors = itertools.repeat(ec)
        else:
            edgecolors = itertools.cycle(mcolors.to_rgba_array(ec))

        fc = kwargs.get('facecolor', colors)
        if cbook._str_lower_equal(fc, 'none'):
            facecolors = itertools.repeat(fc)
        else:
            facecolors = itertools.cycle(mcolors.to_rgba_array(fc))

        hatches = itertools.cycle(np.atleast_1d(kwargs.get('hatch', None)))
        linewidths = itertools.cycle(np.atleast_1d(kwargs.get('linewidth', None)))
        if 'linestyle' in kwargs:
            linestyles = itertools.cycle(mlines._get_dash_patterns(kwargs['linestyle']))
        else:
            linestyles = itertools.repeat(None)

        for patch, lbl in itertools.zip_longest(patches, labels):
            if not patch:
                continue
            p = patch[0]
            kwargs.update({
                'hatch': next(hatches),
                'linewidth': next(linewidths),
                'linestyle': next(linestyles),
                'edgecolor': next(edgecolors),
                'facecolor': next(facecolors),
            })
            p._internal_update(kwargs)
            if lbl is not None:
                p.set_label(lbl)
            for p in patch[1:]:
                p._internal_update(kwargs)
                p.set_label('_nolegend_')

        if nx == 1:
            return tops[0], bins, patches[0]
        else:
            patch_type = ("BarContainer" if histtype.startswith("bar")
                          else "list[Polygon]")
            return tops, bins, cbook.silent_list(patch_type, patches)


# ==================================================
# Line: 7677

def hist2d(self, x, y, bins=10, range=None, density=False, weights=None,
           cmin=None, cmax=None, **kwargs):
    """
    Make a 2D histogram plot.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input values

    bins : None or int or [int, int] or array-like or [array, array]

        The bin specification:

        - If int, the number of bins for the two dimensions
          (``nx = ny = bins``).
        - If ``[int, int]``, the number of bins in each dimension
          (``nx, ny = bins``).
        - If array-like, the bin edges for the two dimensions
          (``x_edges = y_edges = bins``).
        - If ``[array, array]``, the bin edges in each dimension
          (``x_edges, y_edges = bins``).

        The default value is 10.

    range : array-like shape(2, 2), optional
        The leftmost and rightmost edges of the bins along each dimension
        (if not specified explicitly in the bins parameters): ``[[xmin,
        xmax], [ymin, ymax]]``. All values outside of this range will be
        considered outliers and not tallied in the histogram.

    density : bool, default: False
        Normalize histogram.  See the documentation for the *density*
        parameter of `~.Axes.hist` for more details.

    weights : array-like, shape (n, ), optional
        An array of values w_i weighing each sample (x_i, y_i).

    cmin, cmax : float, default: None
        All bins that has count less than *cmin* or more than *cmax* will not be
        displayed (set to NaN before passing to `~.Axes.pcolormesh`) and these count
        values in the return value count histogram will also be set to nan upon
        return.

    Returns
    -------
    h : 2D array
        The bi-dimensional histogram of samples x and y. Values in x are
        histogrammed along the first dimension and values in y are
        histogrammed along the second dimension.
    xedges : 1D array
        The bin edges along the x-axis.
    yedges : 1D array
        The bin edges along the y-axis.
    image : `~.matplotlib.collections.QuadMesh`

    Other Parameters
    ----------------
    %(cmap_doc)s

    %(norm_doc)s

    %(vmin_vmax_doc)s

    %(colorizer_doc)s

    alpha : ``0 <= scalar <= 1`` or ``None``, optional
        The alpha blending value.

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Additional parameters are passed along to the
        `~.Axes.pcolormesh` method and `~matplotlib.collections.QuadMesh`
        constructor.

    See Also
    --------
    hist : 1D histogram plotting
    hexbin : 2D histogram with hexagonal bins

    Notes
    -----
    - Currently ``hist2d`` calculates its own axis limits, and any limits
      previously set are ignored.
    - Rendering the histogram with a logarithmic color scale is
      accomplished by passing a `.colors.LogNorm` instance to the *norm*
      keyword argument. Likewise, power-law normalization (similar
      in effect to gamma correction) can be accomplished with
      `.colors.PowerNorm`.
    """

    h, xedges, yedges = np.histogram2d(x, y, bins=bins, range=range,
                                       density=density, weights=weights)

    if cmin is not None:
        h[h < cmin] = None
    if cmax is not None:
        h[h > cmax] = None

    pc = self.pcolormesh(xedges, yedges, h.T, **kwargs)
    self.set_xlim(xedges[0], xedges[-1])
    self.set_ylim(yedges[0], yedges[-1])

    return h, xedges, yedges, pc


# ==================================================
# Line: 7889

def psd(self, x, NFFT=None, Fs=None, Fc=None, detrend=None,
        window=None, noverlap=None, pad_to=None,
        sides=None, scale_by_freq=None, return_line=None, **kwargs):
    r"""
    Plot the power spectral density.

    The power spectral density :math:`P_{xx}` by Welch's average
    periodogram method.  The vector *x* is divided into *NFFT* length
    segments.  Each segment is detrended by function *detrend* and
    windowed by function *window*.  *noverlap* gives the length of
    the overlap between segments.  The :math:`|\mathrm{fft}(i)|^2`
    of each segment :math:`i` are averaged to compute :math:`P_{xx}`,
    with a scaling to correct for power loss due to windowing.

    If len(*x*) < *NFFT*, it will be zero padded to *NFFT*.

    Parameters
    ----------
    x : 1-D array or sequence
        Array or sequence containing the data

    %(Spectral)s

    %(PSD)s

    noverlap : int, default: 0 (no overlap)
        The number of points of overlap between segments.

    Fc : int, default: 0
        The center frequency of *x*, which offsets the x extents of the
        plot to reflect the frequency range used when a signal is acquired
        and then filtered and downsampled to baseband.

    return_line : bool, default: False
        Whether to include the line object plotted in the returned values.

    Returns
    -------
    Pxx : 1-D array
        The values for the power spectrum :math:`P_{xx}` before scaling
        (real valued).

    freqs : 1-D array
        The frequencies corresponding to the elements in *Pxx*.

    line : `~matplotlib.lines.Line2D`
        The line created by this function.
        Only returned if *return_line* is True.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Keyword arguments control the `.Line2D` properties:

        %(Line2D:kwdoc)s

    See Also
    --------
    specgram
        Differs in the default overlap; in not returning the mean of the
        segment periodograms; in returning the times of the segments; and
        in plotting a colormap instead of a line.
    magnitude_spectrum
        Plots the magnitude spectrum.
    csd
        Plots the spectral density between two signals.

    Notes
    -----
    For plotting, the power is plotted as
    :math:`10\log_{10}(P_{xx})` for decibels, though *Pxx* itself
    is returned.

    References
    ----------
    Bendat & Piersol -- Random Data: Analysis and Measurement Procedures,
    John Wiley & Sons (1986)
    """
    if Fc is None:
        Fc = 0

    pxx, freqs = mlab.psd(x=x, NFFT=NFFT, Fs=Fs, detrend=detrend,
                          window=window, noverlap=noverlap, pad_to=pad_to,
                          sides=sides, scale_by_freq=scale_by_freq)
    freqs += Fc

    if scale_by_freq in (None, True):
        psd_units = 'dB/Hz'
    else:
        psd_units = 'dB'

    line = self.plot(freqs, 10 * np.log10(pxx), **kwargs)
    self.set_xlabel('Frequency')
    self.set_ylabel('Power Spectral Density (%s)' % psd_units)
    self.grid(True)

    vmin, vmax = self.get_ybound()
    step = max(10 * int(np.log10(vmax - vmin)), 1)
    ticks = np.arange(math.floor(vmin), math.ceil(vmax) + 1, step)
    self.set_yticks(ticks)

    if return_line is None or not return_line:
        return pxx, freqs
    else:
        return pxx, freqs, line


# ==================================================
# Line: 8001

def csd(self, x, y, NFFT=None, Fs=None, Fc=None, detrend=None,
        window=None, noverlap=None, pad_to=None,
        sides=None, scale_by_freq=None, return_line=None, **kwargs):
    r"""
    Plot the cross-spectral density.

    The cross spectral density :math:`P_{xy}` by Welch's average
    periodogram method.  The vectors *x* and *y* are divided into
    *NFFT* length segments.  Each segment is detrended by function
    *detrend* and windowed by function *window*.  *noverlap* gives
    the length of the overlap between segments.  The product of
    the direct FFTs of *x* and *y* are averaged over each segment
    to compute :math:`P_{xy}`, with a scaling to correct for power
    loss due to windowing.

    If len(*x*) < *NFFT* or len(*y*) < *NFFT*, they will be zero
    padded to *NFFT*.

    Parameters
    ----------
    x, y : 1-D arrays or sequences
        Arrays or sequences containing the data.

    %(Spectral)s

    %(PSD)s

    noverlap : int, default: 0 (no overlap)
        The number of points of overlap between segments.

    Fc : int, default: 0
        The center frequency of *x*, which offsets the x extents of the
        plot to reflect the frequency range used when a signal is acquired
        and then filtered and downsampled to baseband.

    return_line : bool, default: False
        Whether to include the line object plotted in the returned values.

    Returns
    -------
    Pxy : 1-D array
        The values for the cross spectrum :math:`P_{xy}` before scaling
        (complex valued).

    freqs : 1-D array
        The frequencies corresponding to the elements in *Pxy*.

    line : `~matplotlib.lines.Line2D`
        The line created by this function.
        Only returned if *return_line* is True.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Keyword arguments control the `.Line2D` properties:

        %(Line2D:kwdoc)s

    See Also
    --------
    psd : is equivalent to setting ``y = x``.

    Notes
    -----
    For plotting, the power is plotted as
    :math:`10 \log_{10}(P_{xy})` for decibels, though :math:`P_{xy}` itself
    is returned.

    References
    ----------
    Bendat & Piersol -- Random Data: Analysis and Measurement Procedures,
    John Wiley & Sons (1986)
    """
    if Fc is None:
        Fc = 0

    pxy, freqs = mlab.csd(x=x, y=y, NFFT=NFFT, Fs=Fs, detrend=detrend,
                          window=window, noverlap=noverlap, pad_to=pad_to,
                          sides=sides, scale_by_freq=scale_by_freq)
    # pxy is complex
    freqs += Fc

    line = self.plot(freqs, 10 * np.log10(np.abs(pxy)), **kwargs)
    self.set_xlabel('Frequency')
    self.set_ylabel('Cross Spectrum Magnitude (dB)')
    self.grid(True)

    vmin, vmax = self.get_ybound()
    step = max(10 * int(np.log10(vmax - vmin)), 1)
    ticks = np.arange(math.floor(vmin), math.ceil(vmax) + 1, step)
    self.set_yticks(ticks)

    if return_line is None or not return_line:
        return pxy, freqs
    else:
        return pxy, freqs, line


# ==================================================
# Line: 8104

def magnitude_spectrum(self, x, Fs=None, Fc=None, window=None,
                       pad_to=None, sides=None, scale=None,
                       **kwargs):
    """
    Plot the magnitude spectrum.

    Compute the magnitude spectrum of *x*.  Data is padded to a
    length of *pad_to* and the windowing function *window* is applied to
    the signal.

    Parameters
    ----------
    x : 1-D array or sequence
        Array or sequence containing the data.

    %(Spectral)s

    %(Single_Spectrum)s

    scale : {'default', 'linear', 'dB'}
        The scaling of the values in the *spec*.  'linear' is no scaling.
        'dB' returns the values in dB scale, i.e., the dB amplitude
        (20 * log10). 'default' is 'linear'.

    Fc : int, default: 0
        The center frequency of *x*, which offsets the x extents of the
        plot to reflect the frequency range used when a signal is acquired
        and then filtered and downsampled to baseband.

    Returns
    -------
    spectrum : 1-D array
        The values for the magnitude spectrum before scaling (real valued).

    freqs : 1-D array
        The frequencies corresponding to the elements in *spectrum*.

    line : `~matplotlib.lines.Line2D`
        The line created by this function.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Keyword arguments control the `.Line2D` properties:

        %(Line2D:kwdoc)s

    See Also
    --------
    psd
        Plots the power spectral density.
    angle_spectrum
        Plots the angles of the corresponding frequencies.
    phase_spectrum
        Plots the phase (unwrapped angle) of the corresponding frequencies.
    specgram
        Can plot the magnitude spectrum of segments within the signal in a
        colormap.
    """
    if Fc is None:
        Fc = 0

    spec, freqs = mlab.magnitude_spectrum(x=x, Fs=Fs, window=window,
                                          pad_to=pad_to, sides=sides)
    freqs += Fc

    yunits = _api.check_getitem(
        {None: 'energy', 'default': 'energy', 'linear': 'energy',
         'dB': 'dB'},
        scale=scale)
    if yunits == 'energy':
        Z = spec
    else:  # yunits == 'dB'
        Z = 20. * np.log10(spec)

    line, = self.plot(freqs, Z, **kwargs)
    self.set_xlabel('Frequency')
    self.set_ylabel('Magnitude (%s)' % yunits)

    return spec, freqs, line


# ==================================================
# Line: 8191

def angle_spectrum(self, x, Fs=None, Fc=None, window=None,
                   pad_to=None, sides=None, **kwargs):
    """
    Plot the angle spectrum.

    Compute the angle spectrum (wrapped phase spectrum) of *x*.
    Data is padded to a length of *pad_to* and the windowing function
    *window* is applied to the signal.

    Parameters
    ----------
    x : 1-D array or sequence
        Array or sequence containing the data.

    %(Spectral)s

    %(Single_Spectrum)s

    Fc : int, default: 0
        The center frequency of *x*, which offsets the x extents of the
        plot to reflect the frequency range used when a signal is acquired
        and then filtered and downsampled to baseband.

    Returns
    -------
    spectrum : 1-D array
        The values for the angle spectrum in radians (real valued).

    freqs : 1-D array
        The frequencies corresponding to the elements in *spectrum*.

    line : `~matplotlib.lines.Line2D`
        The line created by this function.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Keyword arguments control the `.Line2D` properties:

        %(Line2D:kwdoc)s

    See Also
    --------
    magnitude_spectrum
        Plots the magnitudes of the corresponding frequencies.
    phase_spectrum
        Plots the unwrapped version of this function.
    specgram
        Can plot the angle spectrum of segments within the signal in a
        colormap.
    """
    if Fc is None:
        Fc = 0

    spec, freqs = mlab.angle_spectrum(x=x, Fs=Fs, window=window,
                                      pad_to=pad_to, sides=sides)
    freqs += Fc

    lines = self.plot(freqs, spec, **kwargs)
    self.set_xlabel('Frequency')
    self.set_ylabel('Angle (radians)')

    return spec, freqs, lines[0]


# ==================================================
# Line: 8261

def phase_spectrum(self, x, Fs=None, Fc=None, window=None,
                   pad_to=None, sides=None, **kwargs):
    """
    Plot the phase spectrum.

    Compute the phase spectrum (unwrapped angle spectrum) of *x*.
    Data is padded to a length of *pad_to* and the windowing function
    *window* is applied to the signal.

    Parameters
    ----------
    x : 1-D array or sequence
        Array or sequence containing the data

    %(Spectral)s

    %(Single_Spectrum)s

    Fc : int, default: 0
        The center frequency of *x*, which offsets the x extents of the
        plot to reflect the frequency range used when a signal is acquired
        and then filtered and downsampled to baseband.

    Returns
    -------
    spectrum : 1-D array
        The values for the phase spectrum in radians (real valued).

    freqs : 1-D array
        The frequencies corresponding to the elements in *spectrum*.

    line : `~matplotlib.lines.Line2D`
        The line created by this function.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Keyword arguments control the `.Line2D` properties:

        %(Line2D:kwdoc)s

    See Also
    --------
    magnitude_spectrum
        Plots the magnitudes of the corresponding frequencies.
    angle_spectrum
        Plots the wrapped version of this function.
    specgram
        Can plot the phase spectrum of segments within the signal in a
        colormap.
    """
    if Fc is None:
        Fc = 0

    spec, freqs = mlab.phase_spectrum(x=x, Fs=Fs, window=window,
                                      pad_to=pad_to, sides=sides)
    freqs += Fc

    lines = self.plot(freqs, spec, **kwargs)
    self.set_xlabel('Frequency')
    self.set_ylabel('Phase (radians)')

    return spec, freqs, lines[0]


# ==================================================
# Line: 8331

def cohere(self, x, y, NFFT=256, Fs=2, Fc=0, detrend=mlab.detrend_none,
           window=mlab.window_hanning, noverlap=0, pad_to=None,
           sides='default', scale_by_freq=None, **kwargs):
    r"""
    Plot the coherence between *x* and *y*.

    Coherence is the normalized cross spectral density:

    .. math::

      C_{xy} = \frac{|P_{xy}|^2}{P_{xx}P_{yy}}

    Parameters
    ----------
    %(Spectral)s

    %(PSD)s

    noverlap : int, default: 0 (no overlap)
        The number of points of overlap between blocks.

    Fc : int, default: 0
        The center frequency of *x*, which offsets the x extents of the
        plot to reflect the frequency range used when a signal is acquired
        and then filtered and downsampled to baseband.

    Returns
    -------
    Cxy : 1-D array
        The coherence vector.

    freqs : 1-D array
        The frequencies for the elements in *Cxy*.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        Keyword arguments control the `.Line2D` properties:

        %(Line2D:kwdoc)s

    References
    ----------
    Bendat & Piersol -- Random Data: Analysis and Measurement Procedures,
    John Wiley & Sons (1986)
    """
    cxy, freqs = mlab.cohere(x=x, y=y, NFFT=NFFT, Fs=Fs, detrend=detrend,
                             window=window, noverlap=noverlap,
                             scale_by_freq=scale_by_freq, sides=sides,
                             pad_to=pad_to)
    freqs += Fc

    self.plot(freqs, cxy, **kwargs)
    self.set_xlabel('Frequency')
    self.set_ylabel('Coherence')
    self.grid(True)

    return cxy, freqs


# ==================================================
# Line: 8396

def specgram(self, x, NFFT=None, Fs=None, Fc=None, detrend=None,
             window=None, noverlap=None,
             cmap=None, xextent=None, pad_to=None, sides=None,
             scale_by_freq=None, mode=None, scale=None,
             vmin=None, vmax=None, **kwargs):
    """
    Plot a spectrogram.

    Compute and plot a spectrogram of data in *x*.  Data are split into
    *NFFT* length segments and the spectrum of each section is
    computed.  The windowing function *window* is applied to each
    segment, and the amount of overlap of each segment is
    specified with *noverlap*. The spectrogram is plotted as a colormap
    (using imshow).

    Parameters
    ----------
    x : 1-D array or sequence
        Array or sequence containing the data.

    %(Spectral)s

    %(PSD)s

    mode : {'default', 'psd', 'magnitude', 'angle', 'phase'}
        What sort of spectrum to use.  Default is 'psd', which takes the
        power spectral density.  'magnitude' returns the magnitude
        spectrum.  'angle' returns the phase spectrum without unwrapping.
        'phase' returns the phase spectrum with unwrapping.

    noverlap : int, default: 128
        The number of points of overlap between blocks.

    scale : {'default', 'linear', 'dB'}
        The scaling of the values in the *spec*.  'linear' is no scaling.
        'dB' returns the values in dB scale.  When *mode* is 'psd',
        this is dB power (10 * log10).  Otherwise, this is dB amplitude
        (20 * log10). 'default' is 'dB' if *mode* is 'psd' or
        'magnitude' and 'linear' otherwise.  This must be 'linear'
        if *mode* is 'angle' or 'phase'.

    Fc : int, default: 0
        The center frequency of *x*, which offsets the x extents of the
        plot to reflect the frequency range used when a signal is acquired
        and then filtered and downsampled to baseband.

    cmap : `.Colormap`, default: :rc:`image.cmap`

    xextent : *None* or (xmin, xmax)
        The image extent along the x-axis. The default sets *xmin* to the
        left border of the first bin (*spectrum* column) and *xmax* to the
        right border of the last bin. Note that for *noverlap>0* the width
        of the bins is smaller than those of the segments.

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    vmin, vmax : float, optional
        vmin and vmax define the data range that the colormap covers.
        By default, the colormap covers the complete value range of the
        data.

    **kwargs
        Additional keyword arguments are passed on to `~.axes.Axes.imshow`
        which makes the specgram image. The origin keyword argument
        is not supported.

    Returns
    -------
    spectrum : 2D array
        Columns are the periodograms of successive segments.

    freqs : 1-D array
        The frequencies corresponding to the rows in *spectrum*.

    t : 1-D array
        The times corresponding to midpoints of segments (i.e., the columns
        in *spectrum*).

    im : `.AxesImage`
        The image created by imshow containing the spectrogram.

    See Also
    --------
    psd
        Differs in the default overlap; in returning the mean of the
        segment periodograms; in not returning times; and in generating a
        line plot instead of colormap.
    magnitude_spectrum
        A single spectrum, similar to having a single segment when *mode*
        is 'magnitude'. Plots a line instead of a colormap.
    angle_spectrum
        A single spectrum, similar to having a single segment when *mode*
        is 'angle'. Plots a line instead of a colormap.
    phase_spectrum
        A single spectrum, similar to having a single segment when *mode*
        is 'phase'. Plots a line instead of a colormap.

    Notes
    -----
    The parameters *detrend* and *scale_by_freq* do only apply when *mode*
    is set to 'psd'.
    """
    if NFFT is None:
        NFFT = 256  # same default as in mlab.specgram()
    if Fc is None:
        Fc = 0  # same default as in mlab._spectral_helper()
    if noverlap is None:
        noverlap = 128  # same default as in mlab.specgram()
    if Fs is None:
        Fs = 2  # same default as in mlab._spectral_helper()

    if mode == 'complex':
        raise ValueError('Cannot plot a complex specgram')

    if scale is None or scale == 'default':
        if mode in ['angle', 'phase']:
            scale = 'linear'
        else:
            scale = 'dB'
    elif mode in ['angle', 'phase'] and scale == 'dB':
        raise ValueError('Cannot use dB scale with angle or phase mode')

    spec, freqs, t = mlab.specgram(x=x, NFFT=NFFT, Fs=Fs,
                                   detrend=detrend, window=window,
                                   noverlap=noverlap, pad_to=pad_to,
                                   sides=sides,
                                   scale_by_freq=scale_by_freq,
                                   mode=mode)

    if scale == 'linear':
        Z = spec
    elif scale == 'dB':
        if mode is None or mode == 'default' or mode == 'psd':
            Z = 10. * np.log10(spec)
        else:
            Z = 20. * np.log10(spec)
    else:
        raise ValueError(f'Unknown scale {scale!r}')

    Z = np.flipud(Z)

    if xextent is None:
        # padding is needed for first and last segment:
        pad_xextent = (NFFT-noverlap) / Fs / 2
        xextent = np.min(t) - pad_xextent, np.max(t) + pad_xextent
    xmin, xmax = xextent
    freqs += Fc
    extent = xmin, xmax, freqs[0], freqs[-1]

    if 'origin' in kwargs:
        raise _api.kwarg_error("specgram", "origin")

    im = self.imshow(Z, cmap, extent=extent, vmin=vmin, vmax=vmax,
                     origin='upper', **kwargs)
    self.axis('auto')

    return spec, freqs, t, im


# ==================================================
# Line: 8557

def spy(self, Z, precision=0, marker=None, markersize=None,
        aspect='equal', origin="upper", **kwargs):
    """
    Plot the sparsity pattern of a 2D array.

    This visualizes the non-zero values of the array.

    Two plotting styles are available: image and marker. Both
    are available for full arrays, but only the marker style
    works for `scipy.sparse.spmatrix` instances.

    **Image style**

    If *marker* and *markersize* are *None*, `~.Axes.imshow` is used. Any
    extra remaining keyword arguments are passed to this method.

    **Marker style**

    If *Z* is a `scipy.sparse.spmatrix` or *marker* or *markersize* are
    *None*, a `.Line2D` object will be returned with the value of marker
    determining the marker type, and any remaining keyword arguments
    passed to `~.Axes.plot`.

    Parameters
    ----------
    Z : (M, N) array-like
        The array to be plotted.

    precision : float or 'present', default: 0
        If *precision* is 0, any non-zero value will be plotted. Otherwise,
        values of :math:`|Z| > precision` will be plotted.

        For `scipy.sparse.spmatrix` instances, you can also
        pass 'present'. In this case any value present in the array
        will be plotted, even if it is identically zero.

    aspect : {'equal', 'auto', None} or float, default: 'equal'
        The aspect ratio of the Axes.  This parameter is particularly
        relevant for images since it determines whether data pixels are
        square.

        This parameter is a shortcut for explicitly calling
        `.Axes.set_aspect`. See there for further details.

        - 'equal': Ensures an aspect ratio of 1. Pixels will be square.
        - 'auto': The Axes is kept fixed and the aspect is adjusted so
          that the data fit in the Axes. In general, this will result in
          non-square pixels.
        - *None*: Use :rc:`image.aspect`.

    origin : {'upper', 'lower'}, default: :rc:`image.origin`
        Place the [0, 0] index of the array in the upper left or lower left
        corner of the Axes. The convention 'upper' is typically used for
        matrices and images.

    Returns
    -------
    `~matplotlib.image.AxesImage` or `.Line2D`
        The return type depends on the plotting style (see above).

    Other Parameters
    ----------------
    **kwargs
        The supported additional parameters depend on the plotting style.

        For the image style, you can pass the following additional
        parameters of `~.Axes.imshow`:

        - *cmap*
        - *alpha*
        - *url*
        - any `.Artist` properties (passed on to the `.AxesImage`)

        For the marker style, you can pass any `.Line2D` property except
        for *linestyle*:

        %(Line2D:kwdoc)s
    """
    if marker is None and markersize is None and hasattr(Z, 'tocoo'):
        marker = 's'
    _api.check_in_list(["upper", "lower"], origin=origin)
    if marker is None and markersize is None:
        Z = np.asarray(Z)
        mask = np.abs(Z) > precision

        if 'cmap' not in kwargs:
            kwargs['cmap'] = mcolors.ListedColormap(['w', 'k'],
                                                    name='binary')
        if 'interpolation' in kwargs:
            raise _api.kwarg_error("spy", "interpolation")
        if 'norm' not in kwargs:
            kwargs['norm'] = mcolors.NoNorm()
        ret = self.imshow(mask, interpolation='nearest',
                          aspect=aspect, origin=origin,
                          **kwargs)
    else:
        if hasattr(Z, 'tocoo'):
            c = Z.tocoo()
            if precision == 'present':
                y = c.row
                x = c.col
            else:
                nonzero = np.abs(c.data) > precision
                y = c.row[nonzero]
                x = c.col[nonzero]
        else:
            Z = np.asarray(Z)
            nonzero = np.abs(Z) > precision
            y, x = np.nonzero(nonzero)
        if marker is None:
            marker = 's'
        if markersize is None:
            markersize = 10
        if 'linestyle' in kwargs:
            raise _api.kwarg_error("spy", "linestyle")
        ret = mlines.Line2D(
            x, y, linestyle='None', marker=marker, markersize=markersize,
            **kwargs)
        self.add_line(ret)
        nr, nc = Z.shape
        self.set_xlim(-0.5, nc - 0.5)
        if origin == "upper":
            self.set_ylim(nr - 0.5, -0.5)
        else:
            self.set_ylim(-0.5, nr - 0.5)
        self.set_aspect(aspect)
    self.title.set_y(1.05)
    if origin == "upper":
        self.xaxis.tick_top()
    else:  # lower
        self.xaxis.tick_bottom()
    self.xaxis.set_ticks_position('both')
    self.xaxis.set_major_locator(
        mticker.MaxNLocator(nbins=9, steps=[1, 2, 5, 10], integer=True))
    self.yaxis.set_major_locator(
        mticker.MaxNLocator(nbins=9, steps=[1, 2, 5, 10], integer=True))
    return ret


# ==================================================
# Line: 8748

def violinplot(self, dataset, positions=None, vert=None,
               orientation='vertical', widths=0.5, showmeans=False,
               showextrema=True, showmedians=False, quantiles=None,
               points=100, bw_method=None, side='both',
               facecolor=None, linecolor=None):
    """
    Make a violin plot.

    Make a violin plot for each column of *dataset* or each vector in
    sequence *dataset*.  Each filled area extends to represent the
    entire data range, with optional lines at the mean, the median,
    the minimum, the maximum, and user-specified quantiles.

    Parameters
    ----------
    dataset : Array or a sequence of vectors.
        The input data.

    positions : array-like, default: [1, 2, ..., n]
        The positions of the violins; i.e. coordinates on the x-axis for
        vertical violins (or y-axis for horizontal violins).

    vert : bool, optional
        .. deprecated:: 3.10
            Use *orientation* instead.

            If this is given during the deprecation period, it overrides
            the *orientation* parameter.

        If True, plots the violins vertically.
        If False, plots the violins horizontally.

    orientation : {'vertical', 'horizontal'}, default: 'vertical'
        If 'horizontal', plots the violins horizontally.
        Otherwise, plots the violins vertically.

        .. versionadded:: 3.10

    widths : float or array-like, default: 0.5
        The maximum width of each violin in units of the *positions* axis.
        The default is 0.5, which is half the available space when using default
        *positions*.

    showmeans : bool, default: False
        Whether to show the mean with a line.

    showextrema : bool, default: True
        Whether to show extrema with a line.

    showmedians : bool, default: False
        Whether to show the median with a line.

    quantiles : array-like, default: None
        If not None, set a list of floats in interval [0, 1] for each violin,
        which stands for the quantiles that will be rendered for that
        violin.

    points : int, default: 100
        The number of points to evaluate each of the gaussian kernel density
        estimations at.

    bw_method : {'scott', 'silverman'} or float or callable, default: 'scott'
        The method used to calculate the estimator bandwidth.  If a
        float, this will be used directly as `!kde.factor`.  If a
        callable, it should take a `matplotlib.mlab.GaussianKDE` instance as
        its only parameter and return a float.

    side : {'both', 'low', 'high'}, default: 'both'
        'both' plots standard violins. 'low'/'high' only
        plots the side below/above the positions value.

    facecolor : :mpltype:`color` or list of :mpltype:`color`, optional
        If provided, will set the face color(s) of the violins.

        .. versionadded:: 3.11

    linecolor : :mpltype:`color` or list of :mpltype:`color`, optional
        If provided, will set the line color(s) of the violins (the
        horizontal and vertical spines and body edges).

        .. versionadded:: 3.11

    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    Returns
    -------
    dict
        A dictionary mapping each component of the violinplot to a
        list of the corresponding collection instances created. The
        dictionary has the following keys:

        - ``bodies``: A list of the `~.collections.PolyCollection`
          instances containing the filled area of each violin.

        - ``cmeans``: A `~.collections.LineCollection` instance that marks
          the mean values of each of the violin's distribution.

        - ``cmins``: A `~.collections.LineCollection` instance that marks
          the bottom of each violin's distribution.

        - ``cmaxes``: A `~.collections.LineCollection` instance that marks
          the top of each violin's distribution.

        - ``cbars``: A `~.collections.LineCollection` instance that marks
          the centers of each violin's distribution.

        - ``cmedians``: A `~.collections.LineCollection` instance that
          marks the median values of each of the violin's distribution.

        - ``cquantiles``: A `~.collections.LineCollection` instance created
          to identify the quantile values of each of the violin's
          distribution.

    See Also
    --------
    .Axes.violin : Draw a violin from pre-computed statistics.
    boxplot : Draw a box and whisker plot.
    """

    def _kde_method(X, coords):
        # Unpack in case of e.g. Pandas or xarray object
        X = cbook._unpack_to_numpy(X)
        # fallback gracefully if the vector contains only one value
        if np.all(X[0] == X):
            return (X[0] == coords).astype(float)
        kde = mlab.GaussianKDE(X, bw_method)
        return kde.evaluate(coords)

    vpstats = cbook.violin_stats(dataset, _kde_method, points=points,
                                 quantiles=quantiles)
    return self.violin(vpstats, positions=positions, vert=vert,
                       orientation=orientation, widths=widths,
                       showmeans=showmeans, showextrema=showextrema,
                       showmedians=showmedians, side=side,
                       facecolor=facecolor, linecolor=linecolor)


# ==================================================
# Line: 8886

def violin(self, vpstats, positions=None, vert=None,
           orientation='vertical', widths=0.5, showmeans=False,
           showextrema=True, showmedians=False, side='both',
           facecolor=None, linecolor=None):
    """
    Draw a violin plot from pre-computed statistics.

    Draw a violin plot for each column of *vpstats*. Each filled area
    extends to represent the entire data range, with optional lines at the
    mean, the median, the minimum, the maximum, and the quantiles values.

    Parameters
    ----------
    vpstats : list of dicts
        A list of dictionaries containing stats for each violin plot.
        Required keys are:

        - ``coords``: A list of scalars containing the coordinates that
          the violin's kernel density estimate were evaluated at.

        - ``vals``: A list of scalars containing the values of the
          kernel density estimate at each of the coordinates given
          in *coords*.

        - ``mean``: The mean value for this violin's dataset.

        - ``median``: The median value for this violin's dataset.

        - ``min``: The minimum value for this violin's dataset.

        - ``max``: The maximum value for this violin's dataset.

        Optional keys are:

        - ``quantiles``: A list of scalars containing the quantile values
          for this violin's dataset.

    positions : array-like, default: [1, 2, ..., n]
        The positions of the violins; i.e. coordinates on the x-axis for
        vertical violins (or y-axis for horizontal violins).

    vert : bool, optional
        .. deprecated:: 3.10
            Use *orientation* instead.

            If this is given during the deprecation period, it overrides
            the *orientation* parameter.

        If True, plots the violins vertically.
        If False, plots the violins horizontally.

    orientation : {'vertical', 'horizontal'}, default: 'vertical'
        If 'horizontal', plots the violins horizontally.
        Otherwise, plots the violins vertically.

        .. versionadded:: 3.10

    widths : float or array-like, default: 0.5
        The maximum width of each violin in units of the *positions* axis.
        The default is 0.5, which is half available space when using default
        *positions*.

    showmeans : bool, default: False
        Whether to show the mean with a line.

    showextrema : bool, default: True
        Whether to show extrema with a line.

    showmedians : bool, default: False
        Whether to show the median with a line.

    side : {'both', 'low', 'high'}, default: 'both'
        'both' plots standard violins. 'low'/'high' only
        plots the side below/above the positions value.

    facecolor : :mpltype:`color` or list of :mpltype:`color`, optional
        If provided, will set the face color(s) of the violins.

        .. versionadded:: 3.11

    linecolor : :mpltype:`color` or list of :mpltype:`color`, optional
        If provided, will set the line color(s) of the violins (the
        horizontal and vertical spines and body edges).

        .. versionadded:: 3.11

    Returns
    -------
    dict
        A dictionary mapping each component of the violinplot to a
        list of the corresponding collection instances created. The
        dictionary has the following keys:

        - ``bodies``: A list of the `~.collections.PolyCollection`
          instances containing the filled area of each violin.

        - ``cmeans``: A `~.collections.LineCollection` instance that marks
          the mean values of each of the violin's distribution.

        - ``cmins``: A `~.collections.LineCollection` instance that marks
          the bottom of each violin's distribution.

        - ``cmaxes``: A `~.collections.LineCollection` instance that marks
          the top of each violin's distribution.

        - ``cbars``: A `~.collections.LineCollection` instance that marks
          the centers of each violin's distribution.

        - ``cmedians``: A `~.collections.LineCollection` instance that
          marks the median values of each of the violin's distribution.

        - ``cquantiles``: A `~.collections.LineCollection` instance created
          to identify the quantiles values of each of the violin's
          distribution.

    See Also
    --------
    violinplot :
        Draw a violin plot from data instead of pre-computed statistics.
    """

    # Statistical quantities to be plotted on the violins
    means = []
    mins = []
    maxes = []
    medians = []
    quantiles = []

    qlens = []  # Number of quantiles in each dataset.

    artists = {}  # Collections to be returned

    N = len(vpstats)
    datashape_message = ("List of violinplot statistics and `{0}` "
                         "values must have the same length")

    # vert and orientation parameters are linked until vert's
    # deprecation period expires. If both are selected,
    # vert takes precedence.
    if vert is not None:
        _api.warn_deprecated(
            "3.11",
            name="vert: bool",
            alternative="orientation: {'vertical', 'horizontal'}",
        )
        orientation = 'vertical' if vert else 'horizontal'
    _api.check_in_list(['horizontal', 'vertical'], orientation=orientation)

    # Validate positions
    if positions is None:
        positions = range(1, N + 1)
    elif len(positions) != N:
        raise ValueError(datashape_message.format("positions"))

    # Validate widths
    if np.isscalar(widths):
        widths = [widths] * N
    elif len(widths) != N:
        raise ValueError(datashape_message.format("widths"))

    # Validate side
    _api.check_in_list(["both", "low", "high"], side=side)

    # Calculate ranges for statistics lines (shape (2, N)).
    line_ends = [[-0.25 if side in ['both', 'low'] else 0],
                 [0.25 if side in ['both', 'high'] else 0]] \
                      * np.array(widths) + positions

    # Make a cycle of color to iterate through, using 'none' as fallback
    def cycle_color(color, alpha=None):
        rgba = mcolors.to_rgba_array(color, alpha=alpha)
        color_cycler = itertools.chain(itertools.cycle(rgba),
                                       itertools.repeat('none'))
        color_list = []
        for _ in range(N):
            color_list.append(next(color_cycler))
        return color_list

    # Convert colors to chain (number of colors can be different from len(vpstats))
    if facecolor is None or linecolor is None:
        if not mpl.rcParams['_internal.classic_mode']:
            next_color = self._get_lines.get_next_color()

    if facecolor is not None:
        facecolor = cycle_color(facecolor)
    else:
        default_facealpha = 0.3
        # Use default colors if user doesn't provide them
        if mpl.rcParams['_internal.classic_mode']:
            facecolor = cycle_color('y', alpha=default_facealpha)
        else:
            facecolor = cycle_color(next_color, alpha=default_facealpha)

    if mpl.rcParams['_internal.classic_mode']:
        # Classic mode uses patch.force_edgecolor=True, so we need to
        # set the edgecolor to make sure it has an alpha.
        body_edgecolor = ("k", 0.3)
    else:
        body_edgecolor = None

    if linecolor is not None:
        linecolor = cycle_color(linecolor)
    else:
        if mpl.rcParams['_internal.classic_mode']:
            linecolor = cycle_color('r')
        else:
            linecolor = cycle_color(next_color)

    # Check whether we are rendering vertically or horizontally
    if orientation == 'vertical':
        fill = self.fill_betweenx
        if side in ['low', 'high']:
            perp_lines = functools.partial(self.hlines, colors=linecolor,
                                            capstyle='projecting')
            par_lines = functools.partial(self.vlines, colors=linecolor,
                                            capstyle='projecting')
        else:
            perp_lines = functools.partial(self.hlines, colors=linecolor)
            par_lines = functools.partial(self.vlines, colors=linecolor)
    else:
        fill = self.fill_between
        if side in ['low', 'high']:
            perp_lines = functools.partial(self.vlines, colors=linecolor,
                                            capstyle='projecting')
            par_lines = functools.partial(self.hlines, colors=linecolor,
                                            capstyle='projecting')
        else:
            perp_lines = functools.partial(self.vlines, colors=linecolor)
            par_lines = functools.partial(self.hlines, colors=linecolor)

    # Render violins
    bodies = []
    bodies_zip = zip(vpstats, positions, widths, facecolor)
    for stats, pos, width, facecolor in bodies_zip:
        # The 0.5 factor reflects the fact that we plot from v-p to v+p.
        vals = np.array(stats['vals'])
        vals = 0.5 * width * vals / vals.max()
        bodies += [fill(stats['coords'],
                        -vals + pos if side in ['both', 'low'] else pos,
                        vals + pos if side in ['both', 'high'] else pos,
                        facecolor=facecolor, edgecolor=body_edgecolor)]
        means.append(stats['mean'])
        mins.append(stats['min'])
        maxes.append(stats['max'])
        medians.append(stats['median'])
        q = stats.get('quantiles')  # a list of floats, or None
        if q is None:
            q = []
        quantiles.extend(q)
        qlens.append(len(q))
    artists['bodies'] = bodies

    if showmeans:  # Render means
        artists['cmeans'] = perp_lines(means, *line_ends)
    if showextrema:  # Render extrema
        artists['cmaxes'] = perp_lines(maxes, *line_ends)
        artists['cmins'] = perp_lines(mins, *line_ends)
        artists['cbars'] = par_lines(positions, mins, maxes)
    if showmedians:  # Render medians
        artists['cmedians'] = perp_lines(medians, *line_ends)
    if quantiles:  # Render quantiles: each width is repeated qlen times.
        artists['cquantiles'] = perp_lines(
            quantiles, *np.repeat(line_ends, qlens, axis=1))

    return artists


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/legend.py
# Line: 355

def __init__(
    self, parent, handles, labels,
    *,
    loc=None,
    numpoints=None,      # number of points in the legend line
    markerscale=None,    # relative size of legend markers vs. original
    markerfirst=True,    # left/right ordering of legend marker and label
    reverse=False,       # reverse ordering of legend marker and label
    scatterpoints=None,  # number of scatter points
    scatteryoffsets=None,
    prop=None,           # properties for the legend texts
    fontsize=None,       # keyword to set font size directly
    labelcolor=None,     # keyword to set the text color

    # spacing & pad defined as a fraction of the font-size
    borderpad=None,      # whitespace inside the legend border
    labelspacing=None,   # vertical space between the legend entries
    handlelength=None,   # length of the legend handles
    handleheight=None,   # height of the legend handles
    handletextpad=None,  # pad between the legend handle and text
    borderaxespad=None,  # pad between the Axes and legend border
    columnspacing=None,  # spacing between columns

    ncols=1,     # number of columns
    mode=None,  # horizontal distribution of columns: None or "expand"

    fancybox=None,  # True: fancy box, False: rounded box, None: rcParam
    shadow=None,
    title=None,           # legend title
    title_fontsize=None,  # legend title font size
    framealpha=None,      # set frame alpha
    edgecolor=None,       # frame patch edgecolor
    facecolor=None,       # frame patch facecolor

    bbox_to_anchor=None,  # bbox to which the legend will be anchored
    bbox_transform=None,  # transform for the bbox
    frameon=None,         # draw frame
    handler_map=None,
    title_fontproperties=None,  # properties for the legend title
    alignment="center",       # control the alignment within the legend box
    ncol=1,  # synonym for ncols (backward compatibility)
    draggable=False  # whether the legend can be dragged with the mouse

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/bezier.py
# Line: 32

def get_intersection(cx1, cy1, cos_t1, sin_t1,
                     cx2, cy2, cos_t2, sin_t2):
    """
    Return the intersection between the line through (*cx1*, *cy1*) at angle
    *t1* and the line through (*cx2*, *cy2*) at angle *t2*.
    """

    # line1 => sin_t1 * (x - cx1) - cos_t1 * (y - cy1) = 0.
    # line1 => sin_t1 * x + cos_t1 * y = sin_t1*cx1 - cos_t1*cy1

    line1_rhs = sin_t1 * cx1 - cos_t1 * cy1
    line2_rhs = sin_t2 * cx2 - cos_t2 * cy2

    # rhs matrix
    a, b = sin_t1, -cos_t1
    c, d = sin_t2, -cos_t2

    ad_bc = a * d - b * c
    if abs(ad_bc) < 1e-12:
        raise ValueError("Given lines do not intersect. Please verify that "
                         "the angles are not equal or differ by 180 degrees.")

    # rhs_inverse
    a_, b_ = d, -b
    c_, d_ = -c, a
    a_, b_, c_, d_ = (k / ad_bc for k in [a_, b_, c_, d_])

    x = a_ * line1_rhs + b_ * line2_rhs
    y = c_ * line1_rhs + d_ * line2_rhs

    return x, y



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_cm.py
# Line: 56

def _ch_helper(gamma, s, r, h, p0, p1, x):
    """Helper function for generating picklable cubehelix colormaps."""
    # Apply gamma factor to emphasise low or high intensity values
    xg = x ** gamma
    # Calculate amplitude and angle of deviation from the black to white
    # diagonal in the plane of constant perceived intensity.
    a = h * xg * (1 - xg) / 2
    phi = 2 * np.pi * (s / 3 + r * x)
    return xg + a * (p0 * np.cos(phi) + p1 * np.sin(phi))


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/legend_handler.py
# Line: 94

def adjust_drawing_area(self, legend, orig_handle,
                        xdescent, ydescent, width, height, fontsize,
                        ):
    xdescent = xdescent - self._xpad * fontsize
    ydescent = ydescent - self._ypad * fontsize
    width = width - self._xpad * fontsize
    height = height - self._ypad * fontsize
    return xdescent, ydescent, width, height


# ==================================================
# Line: 140

def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize,
                   trans):
    """
    Return the legend artists generated.

    Parameters
    ----------
    legend : `~matplotlib.legend.Legend`
        The legend for which these legend artists are being created.
    orig_handle : `~matplotlib.artist.Artist` or similar
        The object for which these legend artists are being created.
    xdescent, ydescent, width, height : int
        The rectangle (*xdescent*, *ydescent*, *width*, *height*) that the
        legend artists being created should fit within.
    fontsize : int
        The fontsize in pixels. The legend artists being created should
        be scaled according to the given fontsize.
    trans : `~matplotlib.transforms.Transform`
        The transform that is applied to the legend artists being created.
        Typically from unit coordinates in the handler box to screen
        coordinates.
    """
    raise NotImplementedError('Derived must override')



# ==================================================
# Line: 193

def get_xdata(self, legend, xdescent, ydescent, width, height, fontsize):
    numpoints = self.get_numpoints(legend)
    if numpoints > 1:
        # we put some pad here to compensate the size of the marker
        pad = self._marker_pad * fontsize
        xdata = np.linspace(-xdescent + pad,
                            -xdescent + width - pad,
                            numpoints)
        xdata_marker = xdata
    else:
        xdata = [-xdescent, -xdescent + width]
        xdata_marker = [-xdescent + 0.5 * width]
    return xdata, xdata_marker



# ==================================================
# Line: 229

def get_ydata(self, legend, xdescent, ydescent, width, height, fontsize):
    if self._yoffsets is None:
        ydata = height * legend._scatteryoffsets
    else:
        ydata = height * np.asarray(self._yoffsets)

    return ydata



# ==================================================
# Line: 244

def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize,
                   trans):
    # docstring inherited
    xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                         width, height, fontsize)

    ydata = np.full_like(xdata, ((height - ydescent) / 2))
    legline = Line2D(xdata, ydata)

    self.update_prop(legline, orig_handle, legend)
    legline.set_drawstyle('default')
    legline.set_marker("")

    legline_marker = Line2D(xdata_marker, ydata[:len(xdata_marker)])
    self.update_prop(legline_marker, orig_handle, legend)
    legline_marker.set_linestyle('None')
    if legend.markerscale != 1:
        newsz = legline_marker.get_markersize() * legend.markerscale
        legline_marker.set_markersize(newsz)
    # we don't want to add this to the return list because
    # the texts and handles are assumed to be in one-to-one
    # correspondence.
    legline._legmarker = legline_marker

    legline.set_transform(trans)
    legline_marker.set_transform(trans)

    return [legline, legline_marker]



# ==================================================
# Line: 285

def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize,
                   trans):
    # docstring inherited
    xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                         width, height, fontsize)

    markevery = None
    if self.get_numpoints(legend) == 1:
        # Special case: one wants a single marker in the center
        # and a line that extends on both sides. One will use a
        # 3 points line, but only mark the #1 (i.e. middle) point.
        xdata = np.linspace(xdata[0], xdata[-1], 3)
        markevery = [1]

    ydata = np.full_like(xdata, (height - ydescent) / 2)
    legline = Line2D(xdata, ydata, markevery=markevery)

    self.update_prop(legline, orig_handle, legend)

    if legend.markerscale != 1:
        newsz = legline.get_markersize() * legend.markerscale
        legline.set_markersize(newsz)

    legline.set_transform(trans)

    return [legline]



# ==================================================
# Line: 340

def _create_patch(self, legend, orig_handle,
                  xdescent, ydescent, width, height, fontsize):
    if self._patch_func is None:
        p = Rectangle(xy=(-xdescent, -ydescent),
                      width=width, height=height)
    else:
        p = self._patch_func(legend=legend, orig_handle=orig_handle,
                             xdescent=xdescent, ydescent=ydescent,
                             width=width, height=height, fontsize=fontsize)
    return p


# ==================================================
# Line: 351

def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize, trans):
    # docstring inherited
    p = self._create_patch(legend, orig_handle,
                           xdescent, ydescent, width, height, fontsize)
    self.update_prop(p, orig_handle, legend)
    p.set_transform(trans)
    return [p]



# ==================================================
# Line: 385

def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize, trans):
    # docstring inherited
    if orig_handle.get_fill() or (orig_handle.get_hatch() is not None):
        p = self._create_patch(orig_handle, xdescent, ydescent, width,
                               height)
        self.update_prop(p, orig_handle, legend)
    else:
        p = self._create_line(orig_handle, width, height)
    p.set_transform(trans)
    return [p]



# ==================================================
# Line: 416

def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize, trans):
    # docstring inherited
    xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                         width, height, fontsize)
    ydata = np.full_like(xdata, (height - ydescent) / 2)
    legline = Line2D(xdata, ydata)

    self.update_prop(legline, orig_handle, legend)
    legline.set_transform(trans)

    return [legline]



# ==================================================
# Line: 444

def get_sizes(self, legend, orig_handle,
              xdescent, ydescent, width, height, fontsize):
    if self._sizes is None:
        handle_sizes = orig_handle.get_sizes()
        if not len(handle_sizes):
            handle_sizes = [1]
        size_max = max(handle_sizes) * legend.markerscale ** 2
        size_min = min(handle_sizes) * legend.markerscale ** 2

        numpoints = self.get_numpoints(legend)
        if numpoints < 4:
            sizes = [.5 * (size_max + size_min), size_max,
                     size_min][:numpoints]
        else:
            rng = (size_max - size_min)
            sizes = rng * np.linspace(0, 1, numpoints) + size_min
    else:
        sizes = self._sizes

    return sizes


# ==================================================
# Line: 481

def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize,
                   trans):
    # docstring inherited
    xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                         width, height, fontsize)

    ydata = self.get_ydata(legend, xdescent, ydescent,
                           width, height, fontsize)

    sizes = self.get_sizes(legend, orig_handle, xdescent, ydescent,
                           width, height, fontsize)

    p = self.create_collection(
        orig_handle, sizes,
        offsets=list(zip(xdata_marker, ydata)), offset_transform=trans)

    self.update_prop(p, orig_handle, legend)
    p.set_offset_transform(trans)
    return [p]



# ==================================================
# Line: 532

def get_err_size(self, legend, xdescent, ydescent,
                 width, height, fontsize):
    xerr_size = self._xerr_size * fontsize

    if self._yerr_size is None:
        yerr_size = xerr_size
    else:
        yerr_size = self._yerr_size * fontsize

    return xerr_size, yerr_size


# ==================================================
# Line: 543

def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize,
                   trans):
    # docstring inherited
    plotlines, caplines, barlinecols = orig_handle

    xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                         width, height, fontsize)

    ydata = np.full_like(xdata, (height - ydescent) / 2)
    legline = Line2D(xdata, ydata)

    xdata_marker = np.asarray(xdata_marker)
    ydata_marker = np.asarray(ydata[:len(xdata_marker)])

    xerr_size, yerr_size = self.get_err_size(legend, xdescent, ydescent,
                                             width, height, fontsize)

    legline_marker = Line2D(xdata_marker, ydata_marker)

    # when plotlines are None (only errorbars are drawn), we just
    # make legline invisible.
    if plotlines is None:
        legline.set_visible(False)
        legline_marker.set_visible(False)
    else:
        self.update_prop(legline, plotlines, legend)

        legline.set_drawstyle('default')
        legline.set_marker('none')

        self.update_prop(legline_marker, plotlines, legend)
        legline_marker.set_linestyle('None')

        if legend.markerscale != 1:
            newsz = legline_marker.get_markersize() * legend.markerscale
            legline_marker.set_markersize(newsz)

    handle_barlinecols = []
    handle_caplines = []

    if orig_handle.has_xerr:
        verts = [((x - xerr_size, y), (x + xerr_size, y))
                 for x, y in zip(xdata_marker, ydata_marker)]
        coll = mcoll.LineCollection(verts)
        self.update_prop(coll, barlinecols[0], legend)
        handle_barlinecols.append(coll)

        if caplines:
            capline_left = Line2D(xdata_marker - xerr_size, ydata_marker)
            capline_right = Line2D(xdata_marker + xerr_size, ydata_marker)
            self.update_prop(capline_left, caplines[0], legend)
            self.update_prop(capline_right, caplines[0], legend)
            capline_left.set_marker("|")
            capline_right.set_marker("|")

            handle_caplines.append(capline_left)
            handle_caplines.append(capline_right)

    if orig_handle.has_yerr:
        verts = [((x, y - yerr_size), (x, y + yerr_size))
                 for x, y in zip(xdata_marker, ydata_marker)]
        coll = mcoll.LineCollection(verts)
        self.update_prop(coll, barlinecols[0], legend)
        handle_barlinecols.append(coll)

        if caplines:
            capline_left = Line2D(xdata_marker, ydata_marker - yerr_size)
            capline_right = Line2D(xdata_marker, ydata_marker + yerr_size)
            self.update_prop(capline_left, caplines[0], legend)
            self.update_prop(capline_right, caplines[0], legend)
            capline_left.set_marker("_")
            capline_right.set_marker("_")

            handle_caplines.append(capline_left)
            handle_caplines.append(capline_right)

    artists = [
        *handle_barlinecols, *handle_caplines, legline, legline_marker,
    ]
    for artist in artists:
        artist.set_transform(trans)
    return artists



# ==================================================
# Line: 654

def get_ydata(self, legend, xdescent, ydescent, width, height, fontsize):
    if self._yoffsets is None:
        ydata = height * (0.5 * legend._scatteryoffsets + 0.5)
    else:
        ydata = height * np.asarray(self._yoffsets)

    return ydata


# ==================================================
# Line: 662

def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize,
                   trans):
    # docstring inherited
    markerline, stemlines, baseline = orig_handle
    # Check to see if the stemcontainer is storing lines as a list or a
    # LineCollection. Eventually using a list will be removed, and this
    # logic can also be removed.
    using_linecoll = isinstance(stemlines, mcoll.LineCollection)

    xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                         width, height, fontsize)

    ydata = self.get_ydata(legend, xdescent, ydescent,
                           width, height, fontsize)

    if self._bottom is None:
        bottom = 0.
    else:
        bottom = self._bottom

    leg_markerline = Line2D(xdata_marker, ydata[:len(xdata_marker)])
    self.update_prop(leg_markerline, markerline, legend)

    leg_stemlines = [Line2D([x, x], [bottom, y])
                     for x, y in zip(xdata_marker, ydata)]

    if using_linecoll:
        # change the function used by update_prop() from the default
        # to one that handles LineCollection
        with cbook._setattr_cm(
                self, _update_prop_func=self._copy_collection_props):
            for line in leg_stemlines:
                self.update_prop(line, stemlines, legend)

    else:
        for lm, m in zip(leg_stemlines, stemlines):
            self.update_prop(lm, m, legend)

    leg_baseline = Line2D([np.min(xdata), np.max(xdata)],
                          [bottom, bottom])
    self.update_prop(leg_baseline, baseline, legend)

    artists = [*leg_stemlines, leg_baseline, leg_markerline]
    for artist in artists:
        artist.set_transform(trans)
    return artists


# ==================================================
# Line: 740

def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize,
                   trans):
    # docstring inherited
    handler_map = legend.get_legend_handler_map()

    if self._ndivide is None:
        ndivide = len(orig_handle)
    else:
        ndivide = self._ndivide

    if self._pad is None:
        pad = legend.borderpad * fontsize
    else:
        pad = self._pad * fontsize

    if ndivide > 1:
        width = (width - pad * (ndivide - 1)) / ndivide

    xds_cycle = cycle(xdescent - (width + pad) * np.arange(ndivide))

    a_list = []
    for handle1 in orig_handle:
        handler = legend.get_legend_handler(handler_map, handle1)
        _a_list = handler.create_artists(
            legend, handle1,
            next(xds_cycle), ydescent, width, height, fontsize, trans)
        a_list.extend(_a_list)

    return a_list



# ==================================================
# Line: 805

def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize, trans):
    # docstring inherited
    p = Rectangle(xy=(-xdescent, -ydescent),
                  width=width, height=height)
    self.update_prop(p, orig_handle, legend)
    p.set_transform(trans)
    return [p]

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_mathtext.py
# Line: 243

def get_kern(self, font1: str, fontclass1: str, sym1: str, fontsize1: float,
             font2: str, fontclass2: str, sym2: str, fontsize2: float,
             dpi: float) -> float:
    """
    Get the kerning distance for font between *sym1* and *sym2*.

    See `~.Fonts.get_metrics` for a detailed description of the parameters.
    """
    return 0.


# ==================================================
# Line: 288

def render_glyph(self, output: Output, ox: float, oy: float, font: str,
                 font_class: str, sym: str, fontsize: float, dpi: float) -> None:
    """
    At position (*ox*, *oy*), draw the glyph specified by the remaining
    parameters (see `get_metrics` for their detailed description).
    """
    info = self._get_info(font, font_class, sym, fontsize, dpi)
    output.glyphs.append((ox, oy, info))


# ==================================================
# Line: 421

def get_kern(self, font1: str, fontclass1: str, sym1: str, fontsize1: float,
             font2: str, fontclass2: str, sym2: str, fontsize2: float,
             dpi: float) -> float:
    if font1 == font2 and fontsize1 == fontsize2:
        info1 = self._get_info(font1, fontclass1, sym1, fontsize1, dpi)
        info2 = self._get_info(font2, fontclass2, sym2, fontsize2, dpi)
        font = info1.font
        return font.get_kerning(info1.num, info2.num, Kerning.DEFAULT) / 64
    return super().get_kern(font1, fontclass1, sym1, fontsize1,
                            font2, fontclass2, sym2, fontsize2, dpi)



# ==================================================
# Line: 1535

def __init__(self, c: str, height: float, depth: float, state: ParserState,
             always: bool = False, factor: float | None = None):
    alternatives = state.fontset.get_sized_alternatives_for_symbol(
        state.font, c)

    xHeight = state.fontset.get_xheight(
        state.font, state.fontsize, state.dpi)

    state = state.copy()
    target_total = height + depth
    for fontname, sym in alternatives:
        state.font = fontname
        char = Char(sym, state)
        # Ensure that size 0 is chosen when the text is regular sized but
        # with descender glyphs by subtracting 0.2 * xHeight
        if char.height + char.depth >= target_total - 0.2 * xHeight:
            break

    shift = 0.0
    if state.font != 0 or len(alternatives) == 1:
        if factor is None:
            factor = target_total / (char.height + char.depth)
        state.fontsize *= factor
        char = Char(sym, state)

        shift = (depth - char.depth)

    super().__init__([char])
    self.shift_amount = shift



# ==================================================
# Line: 2614

def _genfrac(self, ldelim: str, rdelim: str, rule: float | None, style: _MathStyle,
             num: Hlist, den: Hlist) -> T.Any:
    state = self.get_state()
    thickness = state.get_current_underline_thickness()

    for _ in range(style.value):
        num.shrink()
        den.shrink()
    cnum = HCentered([num])
    cden = HCentered([den])
    width = max(num.width, den.width)
    cnum.hpack(width, 'exactly')
    cden.hpack(width, 'exactly')
    vlist = Vlist([cnum,                      # numerator
                   Vbox(0, thickness * 2.0),  # space
                   Hrule(state, rule),        # rule
                   Vbox(0, thickness * 2.0),  # space
                   cden                       # denominator
                   ])

    # Shift so the fraction line sits in the middle of the
    # equals sign
    metrics = state.fontset.get_metrics(
        state.font, mpl.rcParams['mathtext.default'],
        '=', state.fontsize, state.dpi)
    shift = (cden.height -
             ((metrics.ymax + metrics.ymin) / 2 -
              thickness * 3.0))
    vlist.shift_amount = shift

    result = [Hlist([vlist, Hbox(thickness * 2.)])]
    if ldelim or rdelim:
        if ldelim == '':
            ldelim = '.'
        if rdelim == '':
            rdelim = '.'
        return self._auto_sized_delimiter(ldelim,
                                          T.cast(list[Box | Char | str],
                                                 result),
                                          rdelim)
    return result


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/text.py
# Line: 104

def __init__(self,
             x=0, y=0, text='', *,
             color=None,           # defaults to rc params
             verticalalignment='baseline',
             horizontalalignment='left',
             multialignment=None,
             fontproperties=None,  # defaults to FontProperties()
             rotation=None,
             linespacing=None,
             rotation_mode=None,
             usetex=None,          # defaults to rcParams['text.usetex']
             wrap=False,
             transform_rotates_text=False,
             parse_math=None,    # defaults to rcParams['text.parse_math']
             antialiased=None,  # defaults to rcParams['text.antialiased']
             **kwargs
             ):
    """
    Create a `.Text` instance at *x*, *y* with string *text*.

    The text is aligned relative to the anchor point (*x*, *y*) according
    to ``horizontalalignment`` (default: 'left') and ``verticalalignment``
    (default: 'baseline'). See also
    :doc:`/gallery/text_labels_and_annotations/text_alignment`.

    While Text accepts the 'label' keyword argument, by default it is not
    added to the handles of a legend.

    Valid keyword arguments are:

    %(Text:kwdoc)s
    """
    super().__init__()
    self._x, self._y = x, y
    self._text = ''
    self._reset_visual_defaults(
        text=text,
        color=color,
        fontproperties=fontproperties,
        usetex=usetex,
        parse_math=parse_math,
        wrap=wrap,
        verticalalignment=verticalalignment,
        horizontalalignment=horizontalalignment,
        multialignment=multialignment,
        rotation=rotation,
        transform_rotates_text=transform_rotates_text,
        linespacing=linespacing,
        rotation_mode=rotation_mode,
        antialiased=antialiased
    )
    self.update(kwargs)


# ==================================================
# Line: 157

def _reset_visual_defaults(
    self,
    text='',
    color=None,
    fontproperties=None,
    usetex=None,
    parse_math=None,
    wrap=False,
    verticalalignment='baseline',
    horizontalalignment='left',
    multialignment=None,
    rotation=None,
    transform_rotates_text=False,
    linespacing=None,
    rotation_mode=None,
    antialiased=None

# ==================================================
# Line: 1689

def __init__(self, text, xy,
             xytext=None,
             xycoords='data',
             textcoords=None,
             arrowprops=None,
             annotation_clip=None,
             **kwargs):
    """
    Annotate the point *xy* with text *text*.

    In the simplest form, the text is placed at *xy*.

    Optionally, the text can be displayed in another position *xytext*.
    An arrow pointing from the text to the annotated point *xy* can then
    be added by defining *arrowprops*.

    Parameters
    ----------
    text : str
        The text of the annotation.

    xy : (float, float)
        The point *(x, y)* to annotate. The coordinate system is determined
        by *xycoords*.

    xytext : (float, float), default: *xy*
        The position *(x, y)* to place the text at. The coordinate system
        is determined by *textcoords*.

    xycoords : single or two-tuple of str or `.Artist` or `.Transform` or \

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/pyplot.py
# Line: 875

def figure(
    # autoincrement if None, else integer from 1-N
    num: int | str | Figure | SubFigure | None = None,
    # defaults to rc figure.figsize
    figsize: ArrayLike  # a 2-element ndarray is accepted as well
             | tuple[float, float, Literal["in", "cm", "px"]]
             | None = None,
    # defaults to rc figure.dpi
    dpi: float | None = None,
    *,
    # defaults to rc figure.facecolor
    facecolor: ColorType | None = None,
    # defaults to rc figure.edgecolor
    edgecolor: ColorType | None = None,
    frameon: bool = True,
    FigureClass: type[Figure] = Figure,
    clear: bool = False,
    **kwargs

# ==================================================
# Line: 1579

def subplots(
    nrows: Literal[1] = ...,
    ncols: Literal[1] = ...,
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[True] = ...,
    width_ratios: Sequence[float] | None = ...,
    height_ratios: Sequence[float] | None = ...,
    subplot_kw: dict[str, Any] | None = ...,
    gridspec_kw: dict[str, Any] | None = ...,
    **fig_kw

# ==================================================
# Line: 1596

def subplots(
    nrows: int = ...,
    ncols: int = ...,
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: Literal[False],
    width_ratios: Sequence[float] | None = ...,
    height_ratios: Sequence[float] | None = ...,
    subplot_kw: dict[str, Any] | None = ...,
    gridspec_kw: dict[str, Any] | None = ...,
    **fig_kw

# ==================================================
# Line: 1613

def subplots(
    nrows: int = ...,
    ncols: int = ...,
    *,
    sharex: bool | Literal["none", "all", "row", "col"] = ...,
    sharey: bool | Literal["none", "all", "row", "col"] = ...,
    squeeze: bool = ...,
    width_ratios: Sequence[float] | None = ...,
    height_ratios: Sequence[float] | None = ...,
    subplot_kw: dict[str, Any] | None = ...,
    gridspec_kw: dict[str, Any] | None = ...,
    **fig_kw

# ==================================================
# Line: 1629

def subplots(
    nrows: int = 1, ncols: int = 1, *,
    sharex: bool | Literal["none", "all", "row", "col"] = False,
    sharey: bool | Literal["none", "all", "row", "col"] = False,
    squeeze: bool = True,
    width_ratios: Sequence[float] | None = None,
    height_ratios: Sequence[float] | None = None,
    subplot_kw: dict[str, Any] | None = None,
    gridspec_kw: dict[str, Any] | None = None,
    **fig_kw

# ==================================================
# Line: 1793

def subplot_mosaic(
    mosaic: str,
    *,
    sharex: bool = ...,
    sharey: bool = ...,
    width_ratios: ArrayLike | None = ...,
    height_ratios: ArrayLike | None = ...,
    empty_sentinel: str = ...,
    subplot_kw: dict[str, Any] | None = ...,
    gridspec_kw: dict[str, Any] | None = ...,
    per_subplot_kw: dict[str | tuple[str, ...], dict[str, Any]] | None = ...,
    **fig_kw: Any

# ==================================================
# Line: 1809

def subplot_mosaic(
    mosaic: list[HashableList[_T]],
    *,
    sharex: bool = ...,
    sharey: bool = ...,
    width_ratios: ArrayLike | None = ...,
    height_ratios: ArrayLike | None = ...,
    empty_sentinel: _T = ...,
    subplot_kw: dict[str, Any] | None = ...,
    gridspec_kw: dict[str, Any] | None = ...,
    per_subplot_kw: dict[_T | tuple[_T, ...], dict[str, Any]] | None = ...,
    **fig_kw: Any

# ==================================================
# Line: 1825

def subplot_mosaic(
    mosaic: list[HashableList[Hashable]],
    *,
    sharex: bool = ...,
    sharey: bool = ...,
    width_ratios: ArrayLike | None = ...,
    height_ratios: ArrayLike | None = ...,
    empty_sentinel: Any = ...,
    subplot_kw: dict[str, Any] | None = ...,
    gridspec_kw: dict[str, Any] | None = ...,
    per_subplot_kw: dict[Hashable | tuple[Hashable, ...], dict[str, Any]] | None = ...,
    **fig_kw: Any

# ==================================================
# Line: 1840

def subplot_mosaic(
    mosaic: str | list[HashableList[_T]] | list[HashableList[Hashable]],
    *,
    sharex: bool = False,
    sharey: bool = False,
    width_ratios: ArrayLike | None = None,
    height_ratios: ArrayLike | None = None,
    empty_sentinel: Any = '.',
    subplot_kw: dict[str, Any] | None = None,
    gridspec_kw: dict[str, Any] | None = None,
    per_subplot_kw: dict[str | tuple[str, ...], dict[str, Any]] |
                    dict[_T | tuple[_T, ...], dict[str, Any]] |
                    dict[Hashable | tuple[Hashable, ...], dict[str, Any]] | None = None,
    **fig_kw: Any

# ==================================================
# Line: 2750

def figimage(
    X: ArrayLike,
    xo: int = 0,
    yo: int = 0,
    alpha: float | None = None,
    norm: str | Normalize | None = None,
    cmap: str | Colormap | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    origin: Literal["upper", "lower"] | None = None,
    resize: bool = False,
    *,
    colorizer: Colorizer | None = None,
    **kwargs,

# ==================================================
# Line: 2870

def angle_spectrum(
    x: ArrayLike,
    Fs: float | None = None,
    Fc: int | None = None,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = None,
    pad_to: int | None = None,
    sides: Literal["default", "onesided", "twosided"] | None = None,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 2895

def annotate(
    text: str,
    xy: tuple[float, float],
    xytext: tuple[float, float] | None = None,
    xycoords: CoordsType = "data",
    textcoords: CoordsType | None = None,
    arrowprops: dict[str, Any] | None = None,
    annotation_clip: bool | None = None,
    **kwargs,

# ==================================================
# Line: 3060

def boxplot(
    x: ArrayLike | Sequence[ArrayLike],
    notch: bool | None = None,
    sym: str | None = None,
    vert: bool | None = None,
    orientation: Literal["vertical", "horizontal"] = "vertical",
    whis: float | tuple[float, float] | None = None,
    positions: ArrayLike | None = None,
    widths: float | ArrayLike | None = None,
    patch_artist: bool | None = None,
    bootstrap: int | None = None,
    usermedians: ArrayLike | None = None,
    conf_intervals: ArrayLike | None = None,
    meanline: bool | None = None,
    showmeans: bool | None = None,
    showcaps: bool | None = None,
    showbox: bool | None = None,
    showfliers: bool | None = None,
    boxprops: dict[str, Any] | None = None,
    tick_labels: Sequence[str] | None = None,
    flierprops: dict[str, Any] | None = None,
    medianprops: dict[str, Any] | None = None,
    meanprops: dict[str, Any] | None = None,
    capprops: dict[str, Any] | None = None,
    whiskerprops: dict[str, Any] | None = None,
    manage_ticks: bool = True,
    autorange: bool = False,
    zorder: float | None = None,
    capwidths: float | ArrayLike | None = None,
    label: Sequence[str] | None = None,
    *,
    data=None,

# ==================================================
# Line: 3149

def cohere(
    x: ArrayLike,
    y: ArrayLike,
    NFFT: int = 256,
    Fs: float = 2,
    Fc: int = 0,
    detrend: Literal["none", "mean", "linear"]
    | Callable[[ArrayLike], ArrayLike] = mlab.detrend_none,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike = mlab.window_hanning,
    noverlap: int = 0,
    pad_to: int | None = None,
    sides: Literal["default", "onesided", "twosided"] = "default",
    scale_by_freq: bool | None = None,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3207

def csd(
    x: ArrayLike,
    y: ArrayLike,
    NFFT: int | None = None,
    Fs: float | None = None,
    Fc: int | None = None,
    detrend: Literal["none", "mean", "linear"]
    | Callable[[ArrayLike], ArrayLike]
    | None = None,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = None,
    noverlap: int | None = None,
    pad_to: int | None = None,
    sides: Literal["default", "onesided", "twosided"] | None = None,
    scale_by_freq: bool | None = None,
    return_line: bool | None = None,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3269

def errorbar(
    x: float | ArrayLike,
    y: float | ArrayLike,
    yerr: float | ArrayLike | None = None,
    xerr: float | ArrayLike | None = None,
    fmt: str = "",
    ecolor: ColorType | None = None,
    elinewidth: float | None = None,
    capsize: float | None = None,
    barsabove: bool = False,
    lolims: bool | ArrayLike = False,
    uplims: bool | ArrayLike = False,
    xlolims: bool | ArrayLike = False,
    xuplims: bool | ArrayLike = False,
    errorevery: int | tuple[int, int] = 1,
    capthick: float | None = None,
    elinestyle: LineStyleType | None = None,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3314

def eventplot(
    positions: ArrayLike | Sequence[ArrayLike],
    orientation: Literal["horizontal", "vertical"] = "horizontal",
    lineoffsets: float | Sequence[float] = 1,
    linelengths: float | Sequence[float] = 1,
    linewidths: float | Sequence[float] | None = None,
    colors: ColorType | Sequence[ColorType] | None = None,
    alpha: float | Sequence[float] | None = None,
    linestyles: LineStyleType | Sequence[LineStyleType] = "solid",
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3349

def fill_between(
    x: ArrayLike,
    y1: ArrayLike | float,
    y2: ArrayLike | float = 0,
    where: Sequence[bool] | None = None,
    interpolate: bool = False,
    step: Literal["pre", "post", "mid"] | None = None,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3374

def fill_betweenx(
    y: ArrayLike,
    x1: ArrayLike | float,
    x2: ArrayLike | float = 0,
    where: Sequence[bool] | None = None,
    step: Literal["pre", "post", "mid"] | None = None,
    interpolate: bool = False,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3410

def grouped_bar(
    heights: Sequence[ArrayLike] | dict[str, ArrayLike] | np.ndarray | pd.DataFrame,
    *,
    positions: ArrayLike | None = None,
    group_spacing: float | None = 1.5,
    bar_spacing: float | None = 0,
    tick_labels: Sequence[str] | None = None,
    labels: Sequence[str] | None = None,
    orientation: Literal["vertical", "horizontal"] = "vertical",
    colors: Iterable[ColorType] | None = None,
    **kwargs,

# ==================================================
# Line: 3437

def hexbin(
    x: ArrayLike,
    y: ArrayLike,
    C: ArrayLike | None = None,
    gridsize: int | tuple[int, int] = 100,
    bins: Literal["log"] | int | Sequence[float] | None = None,
    xscale: Literal["linear", "log"] = "linear",
    yscale: Literal["linear", "log"] = "linear",
    extent: tuple[float, float, float, float] | None = None,
    cmap: str | Colormap | None = None,
    norm: str | Normalize | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    alpha: float | None = None,
    linewidths: float | None = None,
    edgecolors: Literal["face", "none"] | ColorType = "face",
    reduce_C_function: Callable[[np.ndarray | list[float]], float] = np.mean,
    mincnt: int | None = None,
    marginals: bool = False,
    colorizer: Colorizer | None = None,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3490

def hist(
    x: ArrayLike | Sequence[ArrayLike],
    bins: int | Sequence[float] | str | None = None,
    range: tuple[float, float] | None = None,
    density: bool = False,
    weights: ArrayLike | None = None,
    cumulative: bool | float = False,
    bottom: ArrayLike | float | None = None,
    histtype: Literal["bar", "barstacked", "step", "stepfilled"] = "bar",
    align: Literal["left", "mid", "right"] = "mid",
    orientation: Literal["vertical", "horizontal"] = "vertical",
    rwidth: float | None = None,
    log: bool = False,
    color: ColorType | Sequence[ColorType] | None = None,
    label: str | Sequence[str] | None = None,
    stacked: bool = False,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3560

def hist2d(
    x: ArrayLike,
    y: ArrayLike,
    bins: None | int | tuple[int, int] | ArrayLike | tuple[ArrayLike, ArrayLike] = 10,
    range: ArrayLike | None = None,
    density: bool = False,
    weights: ArrayLike | None = None,
    cmin: float | None = None,
    cmax: float | None = None,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3591

def hlines(
    y: float | ArrayLike,
    xmin: float | ArrayLike,
    xmax: float | ArrayLike,
    colors: ColorType | Sequence[ColorType] | None = None,
    linestyles: LineStyleType = "solid",
    label: str = "",
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3616

def imshow(
    X: ArrayLike | PIL.Image.Image,
    cmap: str | Colormap | None = None,
    norm: str | Normalize | None = None,
    *,
    aspect: Literal["equal", "auto"] | float | None = None,
    interpolation: str | None = None,
    alpha: float | ArrayLike | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    colorizer: Colorizer | None = None,
    origin: Literal["upper", "lower"] | None = None,
    extent: tuple[float, float, float, float] | None = None,
    interpolation_stage: Literal["data", "rgba", "auto"] | None = None,
    filternorm: bool = True,
    filterrad: float = 4.0,
    resample: bool | None = None,
    url: str | None = None,
    data=None,
    **kwargs,

# ==================================================
# Line: 3683

def magnitude_spectrum(
    x: ArrayLike,
    Fs: float | None = None,
    Fc: int | None = None,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = None,
    pad_to: int | None = None,
    sides: Literal["default", "onesided", "twosided"] | None = None,
    scale: Literal["default", "linear", "dB"] | None = None,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3733

def pcolor(
    *args: ArrayLike,
    shading: Literal["flat", "nearest", "auto"] | None = None,
    alpha: float | None = None,
    norm: str | Normalize | None = None,
    cmap: str | Colormap | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    colorizer: Colorizer | None = None,
    data=None,
    **kwargs,

# ==================================================
# Line: 3763

def pcolormesh(
    *args: ArrayLike,
    alpha: float | None = None,
    norm: str | Normalize | None = None,
    cmap: str | Colormap | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    colorizer: Colorizer | None = None,
    shading: Literal["flat", "nearest", "gouraud", "auto"] | None = None,
    antialiased: bool = False,
    data=None,
    **kwargs,

# ==================================================
# Line: 3795

def phase_spectrum(
    x: ArrayLike,
    Fs: float | None = None,
    Fc: int | None = None,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = None,
    pad_to: int | None = None,
    sides: Literal["default", "onesided", "twosided"] | None = None,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3820

def pie(
    x: ArrayLike,
    explode: ArrayLike | None = None,
    labels: Sequence[str] | None = None,
    colors: ColorType | Sequence[ColorType] | None = None,
    autopct: str | Callable[[float], str] | None = None,
    pctdistance: float = 0.6,
    shadow: bool = False,
    labeldistance: float | None = 1.1,
    startangle: float = 0,
    radius: float = 1,
    counterclock: bool = True,
    wedgeprops: dict[str, Any] | None = None,
    textprops: dict[str, Any] | None = None,
    center: tuple[float, float] = (0, 0),
    frame: bool = False,
    rotatelabels: bool = False,
    *,
    normalize: bool = True,
    hatch: str | Sequence[str] | None = None,
    data=None,

# ==================================================
# Line: 3885

def psd(
    x: ArrayLike,
    NFFT: int | None = None,
    Fs: float | None = None,
    Fc: int | None = None,
    detrend: Literal["none", "mean", "linear"]
    | Callable[[ArrayLike], ArrayLike]
    | None = None,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = None,
    noverlap: int | None = None,
    pad_to: int | None = None,
    sides: Literal["default", "onesided", "twosided"] | None = None,
    scale_by_freq: bool | None = None,
    return_line: bool | None = None,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 3940

def scatter(
    x: float | ArrayLike,
    y: float | ArrayLike,
    s: float | ArrayLike | None = None,
    c: ArrayLike | Sequence[ColorType] | ColorType | None = None,
    marker: MarkerType | None = None,
    cmap: str | Colormap | None = None,
    norm: str | Normalize | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    alpha: float | None = None,
    linewidths: float | Sequence[float] | None = None,
    *,
    edgecolors: Literal["face", "none"] | ColorType | Sequence[ColorType] | None = None,
    colorizer: Colorizer | None = None,
    plotnonfinite: bool = False,
    data=None,
    **kwargs,

# ==================================================
# Line: 3995

def specgram(
    x: ArrayLike,
    NFFT: int | None = None,
    Fs: float | None = None,
    Fc: int | None = None,
    detrend: Literal["none", "mean", "linear"]
    | Callable[[ArrayLike], ArrayLike]
    | None = None,
    window: Callable[[ArrayLike], ArrayLike] | ArrayLike | None = None,
    noverlap: int | None = None,
    cmap: str | Colormap | None = None,
    xextent: tuple[float, float] | None = None,
    pad_to: int | None = None,
    sides: Literal["default", "onesided", "twosided"] | None = None,
    scale_by_freq: bool | None = None,
    mode: Literal["default", "psd", "magnitude", "angle", "phase"] | None = None,
    scale: Literal["default", "linear", "dB"] | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 4086

def stem(
    *args: ArrayLike | str,
    linefmt: str | None = None,
    markerfmt: str | None = None,
    basefmt: str | None = None,
    bottom: float = 0,
    label: str | None = None,
    orientation: Literal["vertical", "horizontal"] = "vertical",
    data=None,

# ==================================================
# Line: 4130

def streamplot(
    x,
    y,
    u,
    v,
    density=1,
    linewidth=None,
    color=None,
    cmap=None,
    norm=None,
    arrowsize=1,
    arrowstyle="-|>",
    minlength=0.1,
    transform=None,
    zorder=None,
    start_points=None,
    maxlength=4.0,
    integration_direction="both",
    broken_streamlines=True,
    *,
    integration_max_step_scale=1.0,
    integration_max_error_scale=1.0,
    num_arrows=1,
    data=None,

# ==================================================
# Line: 4185

def table(
    cellText=None,
    cellColours=None,
    cellLoc="right",
    colWidths=None,
    rowLabels=None,
    rowColours=None,
    rowLoc="left",
    colLabels=None,
    colColours=None,
    colLoc="center",
    loc="bottom",
    bbox=None,
    edges="closed",
    **kwargs,

# ==================================================
# Line: 4274

def tripcolor(
    *args,
    alpha=1.0,
    norm=None,
    cmap=None,
    vmin=None,
    vmax=None,
    shading="flat",
    facecolors=None,
    **kwargs,

# ==================================================
# Line: 4308

def violinplot(
    dataset: ArrayLike | Sequence[ArrayLike],
    positions: ArrayLike | None = None,
    vert: bool | None = None,
    orientation: Literal["vertical", "horizontal"] = "vertical",
    widths: float | ArrayLike = 0.5,
    showmeans: bool = False,
    showextrema: bool = True,
    showmedians: bool = False,
    quantiles: Sequence[float | Sequence[float]] | None = None,
    points: int = 100,
    bw_method: Literal["scott", "silverman"]
    | float
    | Callable[[GaussianKDE], float]
    | None = None,
    side: Literal["both", "low", "high"] = "both",
    facecolor: Sequence[ColorType] | ColorType | None = None,
    linecolor: Sequence[ColorType] | ColorType | None = None,
    *,
    data=None,

# ==================================================
# Line: 4350

def vlines(
    x: float | ArrayLike,
    ymin: float | ArrayLike,
    ymax: float | ArrayLike,
    colors: ColorType | Sequence[ColorType] | None = None,
    linestyles: LineStyleType = "solid",
    label: str = "",
    *,
    data=None,
    **kwargs,

# ==================================================
# Line: 4375

def xcorr(
    x: ArrayLike,
    y: ArrayLike,
    normed: bool = True,
    detrend: Callable[[ArrayLike], ArrayLike] = mlab.detrend_none,
    usevlines: bool = True,
    maxlags: int = 10,
    *,
    data=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/quiver.py
# Line: 283

def __init__(self, Q, X, Y, U, label,
             *, angle=0, coordinates='axes', color=None, labelsep=0.1,
             labelpos='N', labelcolor=None, fontproperties=None,
             zorder=None, **kwargs):
    """
    Add a key to a quiver plot.

    The positioning of the key depends on *X*, *Y*, *coordinates*, and
    *labelpos*.  If *labelpos* is 'N' or 'S', *X*, *Y* give the position of
    the middle of the key arrow.  If *labelpos* is 'E', *X*, *Y* positions
    the head, and if *labelpos* is 'W', *X*, *Y* positions the tail; in
    either of these two cases, *X*, *Y* is somewhere in the middle of the
    arrow+label key object.

    Parameters
    ----------
    Q : `~matplotlib.quiver.Quiver`
        A `.Quiver` object as returned by a call to `~.Axes.quiver()`.
    X, Y : float
        The location of the key.
    U : float
        The length of the key.
    label : str
        The key label (e.g., length and units of the key).
    angle : float, default: 0
        The angle of the key arrow, in degrees anti-clockwise from the
        horizontal axis.
    coordinates : {'axes', 'figure', 'data', 'inches'}, default: 'axes'
        Coordinate system and units for *X*, *Y*: 'axes' and 'figure' are
        normalized coordinate systems with (0, 0) in the lower left and
        (1, 1) in the upper right; 'data' are the axes data coordinates
        (used for the locations of the vectors in the quiver plot itself);
        'inches' is position in the figure in inches, with (0, 0) at the
        lower left corner.
    color : :mpltype:`color`
        Overrides face and edge colors from *Q*.
    labelpos : {'N', 'S', 'E', 'W'}
        Position the label above, below, to the right, to the left of the
        arrow, respectively.
    labelsep : float, default: 0.1
        Distance in inches between the arrow and the label.
    labelcolor : :mpltype:`color`, default: :rc:`text.color`
        Label color.
    fontproperties : dict, optional
        A dictionary with keyword arguments accepted by the
        `~matplotlib.font_manager.FontProperties` initializer:
        *family*, *style*, *variant*, *size*, *weight*.
    zorder : float
        The zorder of the key. The default is 0.1 above *Q*.
    **kwargs
        Any additional keyword arguments are used to override vector
        properties taken from *Q*.
    """
    super().__init__()
    self.Q = Q
    self.X = X
    self.Y = Y
    self.U = U
    self.angle = angle
    self.coord = coordinates
    self.color = color
    self.label = label
    self._labelsep_inches = labelsep

    self.labelpos = labelpos
    self.labelcolor = labelcolor
    self.fontproperties = fontproperties or dict()
    self.kw = kwargs
    self.text = mtext.Text(
        text=label,
        horizontalalignment=self.halign[self.labelpos],
        verticalalignment=self.valign[self.labelpos],
        fontproperties=self.fontproperties)
    if self.labelcolor is not None:
        self.text.set_color(self.labelcolor)
    self._dpi_at_last_init = None
    self.zorder = zorder if zorder is not None else Q.zorder + 0.1


# ==================================================
# Line: 510

def __init__(self, ax, *args,
             scale=None, headwidth=3, headlength=5, headaxislength=4.5,
             minshaft=1, minlength=1, units='width', scale_units=None,
             angles='uv', width=None, color='k', pivot='tail', **kwargs):
    """
    The constructor takes one required argument, an Axes
    instance, followed by the args and kwargs described
    by the following pyplot interface documentation:
    %s
    """
    self._axes = ax  # The attr actually set by the Artist.axes property.
    X, Y, U, V, C = _parse_args(*args, caller_name='quiver')
    self.X = X
    self.Y = Y
    self.XY = np.column_stack((X, Y))
    self.N = len(X)
    self.scale = scale
    self.headwidth = headwidth
    self.headlength = float(headlength)
    self.headaxislength = headaxislength
    self.minshaft = minshaft
    self.minlength = minlength
    self.units = units
    self.scale_units = scale_units
    self.angles = angles
    self.width = width

    if pivot.lower() == 'mid':
        pivot = 'middle'
    self.pivot = pivot.lower()
    _api.check_in_list(self._PIVOT_VALS, pivot=self.pivot)

    self.transform = kwargs.pop('transform', ax.transData)
    kwargs.setdefault('facecolors', color)
    kwargs.setdefault('linewidths', (0,))
    super().__init__([], offsets=self.XY, offset_transform=self.transform,
                     closed=False, **kwargs)
    self.polykw = kwargs
    self.set_UVC(U, V, C)
    self._dpi_at_last_init = None


# ==================================================
# Line: 935

def __init__(self, ax, *args,
             pivot='tip', length=7, barbcolor=None, flagcolor=None,
             sizes=None, fill_empty=False, barb_increments=None,
             rounding=True, flip_barb=False, **kwargs):
    """
    The constructor takes one required argument, an Axes
    instance, followed by the args and kwargs described
    by the following pyplot interface documentation:
    %(barbs_doc)s
    """
    self.sizes = sizes or dict()
    self.fill_empty = fill_empty
    self.barb_increments = barb_increments or dict()
    self.rounding = rounding
    self.flip = np.atleast_1d(flip_barb)
    transform = kwargs.pop('transform', ax.transData)
    self._pivot = pivot
    self._length = length

    # Flagcolor and barbcolor provide convenience parameters for
    # setting the facecolor and edgecolor, respectively, of the barb
    # polygon.  We also work here to make the flag the same color as the
    # rest of the barb by default

    if None in (barbcolor, flagcolor):
        kwargs['edgecolors'] = 'face'
        if flagcolor:
            kwargs['facecolors'] = flagcolor
        elif barbcolor:
            kwargs['facecolors'] = barbcolor
        else:
            # Set to facecolor passed in or default to black
            kwargs.setdefault('facecolors', 'k')
    else:
        kwargs['edgecolors'] = barbcolor
        kwargs['facecolors'] = flagcolor

    # Explicitly set a line width if we're not given one, otherwise
    # polygons are not outlined and we get no barbs
    if 'linewidth' not in kwargs and 'lw' not in kwargs:
        kwargs['linewidth'] = 1

    # Parse out the data arrays from the various configurations supported
    x, y, u, v, c = _parse_args(*args, caller_name='barbs')
    self.x = x
    self.y = y
    xy = np.column_stack((x, y))

    # Make a collection
    barb_size = self._length ** 2 / 4  # Empirically determined
    super().__init__(
        [], (barb_size,), offsets=xy, offset_transform=transform, **kwargs)
    self.set_transform(transforms.IdentityTransform())

    self.set_UVC(u, v, c)


# ==================================================
# Line: 1023

def _make_barbs(self, u, v, nflags, nbarbs, half_barb, empty_flag, length,
                pivot, sizes, fill_empty, flip):
    """
    Create the wind barbs.

    Parameters
    ----------
    u, v
        Components of the vector in the x and y directions, respectively.

    nflags, nbarbs, half_barb, empty_flag
        Respectively, the number of flags, number of barbs, flag for
        half a barb, and flag for empty barb, ostensibly obtained from
        :meth:`_find_tails`.

    length
        The length of the barb staff in points.

    pivot : {"tip", "middle"} or number
        The point on the barb around which the entire barb should be
        rotated.  If a number, the start of the barb is shifted by that
        many points from the origin.

    sizes : dict
        Coefficients specifying the ratio of a given feature to the length
        of the barb. These features include:

        - *spacing*: space between features (flags, full/half barbs).
        - *height*: distance from shaft of top of a flag or full barb.
        - *width*: width of a flag, twice the width of a full barb.
        - *emptybarb*: radius of the circle used for low magnitudes.

    fill_empty : bool
        Whether the circle representing an empty barb should be filled or
        not (this changes the drawing of the polygon).

    flip : list of bool
        Whether the features should be flipped to the other side of the
        barb (useful for winds in the southern hemisphere).

    Returns
    -------
    list of arrays of vertices
        Polygon vertices for each of the wind barbs.  These polygons have
        been rotated to properly align with the vector direction.
    """

    # These control the spacing and size of barb elements relative to the
    # length of the shaft
    spacing = length * sizes.get('spacing', 0.125)
    full_height = length * sizes.get('height', 0.4)
    full_width = length * sizes.get('width', 0.25)
    empty_rad = length * sizes.get('emptybarb', 0.15)

    # Controls y point where to pivot the barb.
    pivot_points = dict(tip=0.0, middle=-length / 2.)

    endx = 0.0
    try:
        endy = float(pivot)
    except ValueError:
        endy = pivot_points[pivot.lower()]

    # Get the appropriate angle for the vector components.  The offset is
    # due to the way the barb is initially drawn, going down the y-axis.
    # This makes sense in a meteorological mode of thinking since there 0
    # degrees corresponds to north (the y-axis traditionally)
    angles = -(ma.arctan2(v, u) + np.pi / 2)

    # Used for low magnitude.  We just get the vertices, so if we make it
    # out here, it can be reused.  The center set here should put the
    # center of the circle at the location(offset), rather than at the
    # same point as the barb pivot; this seems more sensible.
    circ = CirclePolygon((0, 0), radius=empty_rad).get_verts()
    if fill_empty:
        empty_barb = circ
    else:
        # If we don't want the empty one filled, we make a degenerate
        # polygon that wraps back over itself
        empty_barb = np.concatenate((circ, circ[::-1]))

    barb_list = []
    for index, angle in np.ndenumerate(angles):
        # If the vector magnitude is too weak to draw anything, plot an
        # empty circle instead
        if empty_flag[index]:
            # We can skip the transform since the circle has no preferred
            # orientation
            barb_list.append(empty_barb)
            continue

        poly_verts = [(endx, endy)]
        offset = length

        # Handle if this barb should be flipped
        barb_height = -full_height if flip[index] else full_height

        # Add vertices for each flag
        for i in range(nflags[index]):
            # The spacing that works for the barbs is a little to much for
            # the flags, but this only occurs when we have more than 1
            # flag.
            if offset != length:
                offset += spacing / 2.
            poly_verts.extend(
                [[endx, endy + offset],
                 [endx + barb_height, endy - full_width / 2 + offset],
                 [endx, endy - full_width + offset]])

            offset -= full_width + spacing

        # Add vertices for each barb.  These really are lines, but works
        # great adding 3 vertices that basically pull the polygon out and
        # back down the line
        for i in range(nbarbs[index]):
            poly_verts.extend(
                [(endx, endy + offset),
                 (endx + barb_height, endy + offset + full_width / 2),
                 (endx, endy + offset)])

            offset -= spacing

        # Add the vertices for half a barb, if needed
        if half_barb[index]:
            # If the half barb is the first on the staff, traditionally it
            # is offset from the end to make it easy to distinguish from a
            # barb with a full one
            if offset == length:
                poly_verts.append((endx, endy + offset))
                offset -= 1.5 * spacing
            poly_verts.extend(
                [(endx, endy + offset),
                 (endx + barb_height / 2, endy + offset + full_width / 4),
                 (endx, endy + offset)])

        # Rotate the barb according the angle. Making the barb first and
        # then rotating it made the math for drawing the barb really easy.
        # Also, the transform framework makes doing the rotation simple.
        poly_verts = transforms.Affine2D().rotate(-angle).transform(
            poly_verts)
        barb_list.append(poly_verts)

    return barb_list


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/figure.py
# Line: 785

def subplots(self, nrows=1, ncols=1, *, sharex=False, sharey=False,
             squeeze=True, width_ratios=None, height_ratios=None,
             subplot_kw=None, gridspec_kw=None):
    """
    Add a set of subplots to this figure.

    This utility wrapper makes it convenient to create common layouts of
    subplots in a single call.

    Parameters
    ----------
    nrows, ncols : int, default: 1
        Number of rows/columns of the subplot grid.

    sharex, sharey : bool or {'none', 'all', 'row', 'col'}, default: False
        Controls sharing of x-axis (*sharex*) or y-axis (*sharey*):

        - True or 'all': x- or y-axis will be shared among all subplots.
        - False or 'none': each subplot x- or y-axis will be independent.
        - 'row': each subplot row will share an x- or y-axis.
        - 'col': each subplot column will share an x- or y-axis.

        When subplots have a shared x-axis along a column, only the x tick
        labels of the bottom subplot are created. Similarly, when subplots
        have a shared y-axis along a row, only the y tick labels of the
        first column subplot are created. To later turn other subplots'
        ticklabels on, use `~matplotlib.axes.Axes.tick_params`.

        When subplots have a shared axis that has units, calling
        `.Axis.set_units` will update each axis with the new units.

        Note that it is not possible to unshare axes.

    squeeze : bool, default: True
        - If True, extra dimensions are squeezed out from the returned
          array of Axes:

          - if only one subplot is constructed (nrows=ncols=1), the
            resulting single Axes object is returned as a scalar.
          - for Nx1 or 1xM subplots, the returned object is a 1D numpy
            object array of Axes objects.
          - for NxM, subplots with N>1 and M>1 are returned as a 2D array.

        - If False, no squeezing at all is done: the returned Axes object
          is always a 2D array containing Axes instances, even if it ends
          up being 1x1.

    width_ratios : array-like of length *ncols*, optional
        Defines the relative widths of the columns. Each column gets a
        relative width of ``width_ratios[i] / sum(width_ratios)``.
        If not given, all columns will have the same width.  Equivalent
        to ``gridspec_kw={'width_ratios': [...]}``.

    height_ratios : array-like of length *nrows*, optional
        Defines the relative heights of the rows. Each row gets a
        relative height of ``height_ratios[i] / sum(height_ratios)``.
        If not given, all rows will have the same height. Equivalent
        to ``gridspec_kw={'height_ratios': [...]}``.

    subplot_kw : dict, optional
        Dict with keywords passed to the `.Figure.add_subplot` call used to
        create each subplot.

    gridspec_kw : dict, optional
        Dict with keywords passed to the
        `~matplotlib.gridspec.GridSpec` constructor used to create
        the grid the subplots are placed on.

    Returns
    -------
    `~.axes.Axes` or array of Axes
        Either a single `~matplotlib.axes.Axes` object or an array of Axes
        objects if more than one subplot was created. The dimensions of the
        resulting array can be controlled with the *squeeze* keyword, see
        above.

    See Also
    --------
    .pyplot.subplots
    .Figure.add_subplot
    .pyplot.subplot

    Examples
    --------
    ::

        # First create some toy data:
        x = np.linspace(0, 2*np.pi, 400)
        y = np.sin(x**2)

        # Create a figure
        fig = plt.figure()

        # Create a subplot
        ax = fig.subplots()
        ax.plot(x, y)
        ax.set_title('Simple plot')

        # Create two subplots and unpack the output array immediately
        ax1, ax2 = fig.subplots(1, 2, sharey=True)
        ax1.plot(x, y)
        ax1.set_title('Sharing Y axis')
        ax2.scatter(x, y)

        # Create four polar Axes and access them through the returned array
        axes = fig.subplots(2, 2, subplot_kw=dict(projection='polar'))
        axes[0, 0].plot(x, y)
        axes[1, 1].scatter(x, y)

        # Share an X-axis with each column of subplots
        fig.subplots(2, 2, sharex='col')

        # Share a Y-axis with each row of subplots
        fig.subplots(2, 2, sharey='row')

        # Share both X- and Y-axes with all subplots
        fig.subplots(2, 2, sharex='all', sharey='all')

        # Note that this is the same as
        fig.subplots(2, 2, sharex=True, sharey=True)
    """
    gridspec_kw = dict(gridspec_kw or {})
    if height_ratios is not None:
        if 'height_ratios' in gridspec_kw:
            raise ValueError("'height_ratios' must not be defined both as "
                             "parameter and as key in 'gridspec_kw'")
        gridspec_kw['height_ratios'] = height_ratios
    if width_ratios is not None:
        if 'width_ratios' in gridspec_kw:
            raise ValueError("'width_ratios' must not be defined both as "
                             "parameter and as key in 'gridspec_kw'")
        gridspec_kw['width_ratios'] = width_ratios

    gs = self.add_gridspec(nrows, ncols, figure=self, **gridspec_kw)
    axs = gs.subplots(sharex=sharex, sharey=sharey, squeeze=squeeze,
                      subplot_kw=subplot_kw)
    return axs


# ==================================================
# Line: 1315

def subplots_adjust(self, left=None, bottom=None, right=None, top=None,
                    wspace=None, hspace=None):
    """
    Adjust the subplot layout parameters.

    Unset parameters are left unmodified; initial values are given by
    :rc:`figure.subplot.[name]`.

    .. plot:: _embedded_plots/figure_subplots_adjust.py

    Parameters
    ----------
    left : float, optional
        The position of the left edge of the subplots,
        as a fraction of the figure width.
    right : float, optional
        The position of the right edge of the subplots,
        as a fraction of the figure width.
    bottom : float, optional
        The position of the bottom edge of the subplots,
        as a fraction of the figure height.
    top : float, optional
        The position of the top edge of the subplots,
        as a fraction of the figure height.
    wspace : float, optional
        The width of the padding between subplots,
        as a fraction of the average Axes width.
    hspace : float, optional
        The height of the padding between subplots,
        as a fraction of the average Axes height.
    """
    if (self.get_layout_engine() is not None and
            not self.get_layout_engine().adjust_compatible):
        _api.warn_external(
            "This figure was using a layout engine that is "
            "incompatible with subplots_adjust and/or tight_layout; "
            "not calling subplots_adjust.")
        return
    self.subplotpars.update(left, bottom, right, top, wspace, hspace)
    for ax in self.axes:
        if ax.get_subplotspec() is not None:
            ax._set_position(ax.get_subplotspec().get_position(self))
    self.stale = True


# ==================================================
# Line: 1604

def subfigures(self, nrows=1, ncols=1, squeeze=True,
               wspace=None, hspace=None,
               width_ratios=None, height_ratios=None,
               **kwargs):
    """
    Add a set of subfigures to this figure or subfigure.

    A subfigure has the same artist methods as a figure, and is logically
    the same as a figure, but cannot print itself.
    See :doc:`/gallery/subplots_axes_and_figures/subfigures`.

    .. versionchanged:: 3.10
        subfigures are now added in row-major order.

    Parameters
    ----------
    nrows, ncols : int, default: 1
        Number of rows/columns of the subfigure grid.

    squeeze : bool, default: True
        If True, extra dimensions are squeezed out from the returned
        array of subfigures.

    wspace, hspace : float, default: None
        The amount of width/height reserved for space between subfigures,
        expressed as a fraction of the average subfigure width/height.
        If not given, the values will be inferred from rcParams if using
        constrained layout (see `~.ConstrainedLayoutEngine`), or zero if
        not using a layout engine.

    width_ratios : array-like of length *ncols*, optional
        Defines the relative widths of the columns. Each column gets a
        relative width of ``width_ratios[i] / sum(width_ratios)``.
        If not given, all columns will have the same width.

    height_ratios : array-like of length *nrows*, optional
        Defines the relative heights of the rows. Each row gets a
        relative height of ``height_ratios[i] / sum(height_ratios)``.
        If not given, all rows will have the same height.
    """
    gs = GridSpec(nrows=nrows, ncols=ncols, figure=self,
                  wspace=wspace, hspace=hspace,
                  width_ratios=width_ratios,
                  height_ratios=height_ratios,
                  left=0, right=1, bottom=0, top=1)

    sfarr = np.empty((nrows, ncols), dtype=object)
    for i in range(nrows):
        for j in range(ncols):
            sfarr[i, j] = self.add_subfigure(gs[i, j], **kwargs)

    if self.get_layout_engine() is None and (wspace is not None or
                                             hspace is not None):
        # Gridspec wspace and hspace is ignored on subfigure instantiation,
        # and no space is left.  So need to account for it here if required.
        bottoms, tops, lefts, rights = gs.get_grid_positions(self)
        for sfrow, bottom, top in zip(sfarr, bottoms, tops):
            for sf, left, right in zip(sfrow, lefts, rights):
                bbox = Bbox.from_extents(left, bottom, right, top)
                sf._redo_transform_rel_fig(bbox=bbox)

    if squeeze:
        # Discarding unneeded dimensions that equal 1.  If we only have one
        # subfigure, just return it instead of a 1-element array.
        return sfarr.item() if sfarr.size == 1 else sfarr.squeeze()
    else:
        # Returned axis array will be always 2-d, even if nrows=ncols=1.
        return sfarr


# ==================================================
# Line: 1899

def subplot_mosaic(self, mosaic, *, sharex=False, sharey=False,
                   width_ratios=None, height_ratios=None,
                   empty_sentinel='.',
                   subplot_kw=None, per_subplot_kw=None, gridspec_kw=None):
    """
    Build a layout of Axes based on ASCII art or nested lists.

    This is a helper function to build complex GridSpec layouts visually.

    See :ref:`mosaic`
    for an example and full API documentation

    Parameters
    ----------
    mosaic : list of list of {hashable or nested} or str

        A visual layout of how you want your Axes to be arranged
        labeled as strings.  For example ::

           x = [['A panel', 'A panel', 'edge'],
                ['C panel', '.',       'edge']]

        produces 4 Axes:

        - 'A panel' which is 1 row high and spans the first two columns
        - 'edge' which is 2 rows high and is on the right edge
        - 'C panel' which in 1 row and 1 column wide in the bottom left
        - a blank space 1 row and 1 column wide in the bottom center

        Any of the entries in the layout can be a list of lists
        of the same form to create nested layouts.

        If input is a str, then it can either be a multi-line string of
        the form ::

          '''
          AAE
          C.E
          '''

        where each character is a column and each line is a row. Or it
        can be a single-line string where rows are separated by ``;``::

          'AB;CC'

        The string notation allows only single character Axes labels and
        does not support nesting but is very terse.

        The Axes identifiers may be `str` or a non-iterable hashable
        object (e.g. `tuple` s may not be used).

    sharex, sharey : bool, default: False
        If True, the x-axis (*sharex*) or y-axis (*sharey*) will be shared
        among all subplots.  In that case, tick label visibility and axis
        units behave as for `subplots`.  If False, each subplot's x- or
        y-axis will be independent.

    width_ratios : array-like of length *ncols*, optional
        Defines the relative widths of the columns. Each column gets a
        relative width of ``width_ratios[i] / sum(width_ratios)``.
        If not given, all columns will have the same width.  Equivalent
        to ``gridspec_kw={'width_ratios': [...]}``. In the case of nested
        layouts, this argument applies only to the outer layout.

    height_ratios : array-like of length *nrows*, optional
        Defines the relative heights of the rows. Each row gets a
        relative height of ``height_ratios[i] / sum(height_ratios)``.
        If not given, all rows will have the same height. Equivalent
        to ``gridspec_kw={'height_ratios': [...]}``. In the case of nested
        layouts, this argument applies only to the outer layout.

    subplot_kw : dict, optional
        Dictionary with keywords passed to the `.Figure.add_subplot` call
        used to create each subplot.  These values may be overridden by
        values in *per_subplot_kw*.

    per_subplot_kw : dict, optional
        A dictionary mapping the Axes identifiers or tuples of identifiers
        to a dictionary of keyword arguments to be passed to the
        `.Figure.add_subplot` call used to create each subplot.  The values
        in these dictionaries have precedence over the values in
        *subplot_kw*.

        If *mosaic* is a string, and thus all keys are single characters,
        it is possible to use a single string instead of a tuple as keys;
        i.e. ``"AB"`` is equivalent to ``("A", "B")``.

        .. versionadded:: 3.7

    gridspec_kw : dict, optional
        Dictionary with keywords passed to the `.GridSpec` constructor used
        to create the grid the subplots are placed on. In the case of
        nested layouts, this argument applies only to the outer layout.
        For more complex layouts, users should use `.Figure.subfigures`
        to create the nesting.

    empty_sentinel : object, optional
        Entry in the layout to mean "leave this space empty".  Defaults
        to ``'.'``. Note, if *layout* is a string, it is processed via
        `inspect.cleandoc` to remove leading white space, which may
        interfere with using white-space as the empty sentinel.

    Returns
    -------
    dict[label, Axes]
       A dictionary mapping the labels to the Axes objects.  The order of
       the Axes is left-to-right and top-to-bottom of their position in the
       total layout.

    """
    subplot_kw = subplot_kw or {}
    gridspec_kw = dict(gridspec_kw or {})
    per_subplot_kw = per_subplot_kw or {}

    if height_ratios is not None:
        if 'height_ratios' in gridspec_kw:
            raise ValueError("'height_ratios' must not be defined both as "
                             "parameter and as key in 'gridspec_kw'")
        gridspec_kw['height_ratios'] = height_ratios
    if width_ratios is not None:
        if 'width_ratios' in gridspec_kw:
            raise ValueError("'width_ratios' must not be defined both as "
                             "parameter and as key in 'gridspec_kw'")
        gridspec_kw['width_ratios'] = width_ratios

    # special-case string input
    if isinstance(mosaic, str):
        mosaic = self._normalize_grid_string(mosaic)
        per_subplot_kw = {
            tuple(k): v for k, v in per_subplot_kw.items()
        }

    per_subplot_kw = self._norm_per_subplot_kw(per_subplot_kw)

    # Only accept strict bools to allow a possible future API expansion.
    _api.check_isinstance(bool, sharex=sharex, sharey=sharey)

    def _make_array(inp):
        """
        Convert input into 2D array

        We need to have this internal function rather than
        ``np.asarray(..., dtype=object)`` so that a list of lists
        of lists does not get converted to an array of dimension > 2.

        Returns
        -------
        2D object array
        """
        r0, *rest = inp
        if isinstance(r0, str):
            raise ValueError('List mosaic specification must be 2D')
        for j, r in enumerate(rest, start=1):
            if isinstance(r, str):
                raise ValueError('List mosaic specification must be 2D')
            if len(r0) != len(r):
                raise ValueError(
                    "All of the rows must be the same length, however "
                    f"the first row ({r0!r}) has length {len(r0)} "
                    f"and row {j} ({r!r}) has length {len(r)}."
                )
        out = np.zeros((len(inp), len(r0)), dtype=object)
        for j, r in enumerate(inp):
            for k, v in enumerate(r):
                out[j, k] = v
        return out

    def _identify_keys_and_nested(mosaic):
        """
        Given a 2D object array, identify unique IDs and nested mosaics

        Parameters
        ----------
        mosaic : 2D object array

        Returns
        -------
        unique_ids : tuple
            The unique non-sub mosaic entries in this mosaic
        nested : dict[tuple[int, int], 2D object array]
        """
        # make sure we preserve the user supplied order
        unique_ids = cbook._OrderedSet()
        nested = {}
        for j, row in enumerate(mosaic):
            for k, v in enumerate(row):
                if v == empty_sentinel:
                    continue
                elif not cbook.is_scalar_or_string(v):
                    nested[(j, k)] = _make_array(v)
                else:
                    unique_ids.add(v)

        return tuple(unique_ids), nested

    def _do_layout(gs, mosaic, unique_ids, nested):
        """
        Recursively do the mosaic.

        Parameters
        ----------
        gs : GridSpec
        mosaic : 2D object array
            The input converted to a 2D array for this level.
        unique_ids : tuple
            The identified scalar labels at this level of nesting.
        nested : dict[tuple[int, int]], 2D object array
            The identified nested mosaics, if any.

        Returns
        -------
        dict[label, Axes]
            A flat dict of all of the Axes created.
        """
        output = dict()

        # we need to merge together the Axes at this level and the Axes
        # in the (recursively) nested sub-mosaics so that we can add
        # them to the figure in the "natural" order if you were to
        # ravel in c-order all of the Axes that will be created
        #
        # This will stash the upper left index of each object (axes or
        # nested mosaic) at this level
        this_level = dict()

        # go through the unique keys,
        for name in unique_ids:
            # sort out where each axes starts/ends
            index = np.argwhere(mosaic == name)
            start_row, start_col = np.min(index, axis=0)
            end_row, end_col = np.max(index, axis=0) + 1
            # and construct the slice object
            slc = (slice(start_row, end_row), slice(start_col, end_col))
            # some light error checking
            if (mosaic[slc] != name).any():
                raise ValueError(
                    f"While trying to layout\n{mosaic!r}\n"
                    f"we found that the label {name!r} specifies a "
                    "non-rectangular or non-contiguous area.")
            # and stash this slice for later
            this_level[(start_row, start_col)] = (name, slc, 'axes')

        # do the same thing for the nested mosaics (simpler because these
        # cannot be spans yet!)
        for (j, k), nested_mosaic in nested.items():
            this_level[(j, k)] = (None, nested_mosaic, 'nested')

        # now go through the things in this level and add them
        # in order left-to-right top-to-bottom
        for key in sorted(this_level):
            name, arg, method = this_level[key]
            # we are doing some hokey function dispatch here based
            # on the 'method' string stashed above to sort out if this
            # element is an Axes or a nested mosaic.
            if method == 'axes':
                slc = arg
                # add a single Axes
                if name in output:
                    raise ValueError(f"There are duplicate keys {name} "
                                     f"in the layout\n{mosaic!r}")
                ax = self.add_subplot(
                    gs[slc], **{
                        'label': str(name),
                        **subplot_kw,
                        **per_subplot_kw.get(name, {})
                    }
                )
                output[name] = ax
            elif method == 'nested':
                nested_mosaic = arg
                j, k = key
                # recursively add the nested mosaic
                rows, cols = nested_mosaic.shape
                nested_output = _do_layout(
                    gs[j, k].subgridspec(rows, cols),
                    nested_mosaic,
                    *_identify_keys_and_nested(nested_mosaic)
                )
                overlap = set(output) & set(nested_output)
                if overlap:
                    raise ValueError(
                        f"There are duplicate keys {overlap} "
                        f"between the outer layout\n{mosaic!r}\n"
                        f"and the nested layout\n{nested_mosaic}"
                    )
                output.update(nested_output)
            else:
                raise RuntimeError("This should never happen")
        return output

    mosaic = _make_array(mosaic)
    rows, cols = mosaic.shape
    gs = self.add_gridspec(rows, cols, **gridspec_kw)
    ret = _do_layout(gs, mosaic, *_identify_keys_and_nested(mosaic))
    ax0 = next(iter(ret.values()))
    for ax in ret.values():
        if sharex:
            ax.sharex(ax0)
            ax._label_outer_xaxis(skip_non_rectangular_axes=True)
        if sharey:
            ax.sharey(ax0)
            ax._label_outer_yaxis(skip_non_rectangular_axes=True)
    if extra := set(per_subplot_kw) - set(ret):
        raise ValueError(
            f"The keys {extra} are in *per_subplot_kw* "
            "but not in the mosaic."
        )
    return ret


# ==================================================
# Line: 2235

def __init__(self, parent, subplotspec, *,
             facecolor=None,
             edgecolor=None,
             linewidth=0.0,
             frameon=None,
             **kwargs):
    """
    Parameters
    ----------
    parent : `.Figure` or `.SubFigure`
        Figure or subfigure that contains the SubFigure.  SubFigures
        can be nested.

    subplotspec : `.gridspec.SubplotSpec`
        Defines the region in a parent gridspec where the subfigure will
        be placed.

    facecolor : default: ``"none"``
        The figure patch face color; transparent by default.

    edgecolor : default: :rc:`figure.edgecolor`
        The figure patch edge color.

    linewidth : float
        The linewidth of the frame (i.e. the edge linewidth of the figure
        patch).

    frameon : bool, default: :rc:`figure.frameon`
        If ``False``, suppress drawing the figure background patch.

    Other Parameters
    ----------------
    **kwargs : `.SubFigure` properties, optional

        %(SubFigure:kwdoc)s
    """
    super().__init__(**kwargs)
    if facecolor is None:
        facecolor = "none"
    edgecolor = mpl._val_or_rc(edgecolor, 'figure.edgecolor')
    frameon = mpl._val_or_rc(frameon, 'figure.frameon')

    self._subplotspec = subplotspec
    self._parent = parent
    self._root_figure = parent._root_figure

    # subfigures use the parent axstack
    self._axstack = parent._axstack
    self.subplotpars = parent.subplotpars
    self.dpi_scale_trans = parent.dpi_scale_trans
    self._axobservers = parent._axobservers
    self.transFigure = parent.transFigure
    self.bbox_relative = Bbox.null()
    self._redo_transform_rel_fig()
    self.figbbox = self._parent.figbbox
    self.bbox = TransformedBbox(self.bbox_relative,
                                self._parent.transSubfigure)
    self.transSubfigure = BboxTransformTo(self.bbox)

    self.patch = Rectangle(
        xy=(0, 0), width=1, height=1, visible=frameon,
        facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth,
        # Don't let the figure patch influence bbox calculation.
        in_layout=False, transform=self.transSubfigure)
    self._set_artist_props(self.patch)
    self.patch.set_antialiased(False)


# ==================================================
# Line: 2463

def __init__(self,
             figsize=None,
             dpi=None,
             *,
             facecolor=None,
             edgecolor=None,
             linewidth=0.0,
             frameon=None,
             subplotpars=None,  # rc figure.subplot.*
             tight_layout=None,  # rc figure.autolayout
             constrained_layout=None,  # rc figure.constrained_layout.use
             layout=None,
             **kwargs
             ):
    """
    Parameters
    ----------
    figsize : (float, float) or (float, float, str), default: :rc:`figure.figsize`
        The figure dimensions. This can be

        - a tuple ``(width, height, unit)``, where *unit* is one of "in" (inch),
          "cm" (centimenter), "px" (pixel).
        - a tuple ``(width, height)``, which is interpreted in inches, i.e. as
          ``(width, height, "in")``.

    dpi : float, default: :rc:`figure.dpi`
        Dots per inch.

    facecolor : default: :rc:`figure.facecolor`
        The figure patch facecolor.

    edgecolor : default: :rc:`figure.edgecolor`
        The figure patch edge color.

    linewidth : float
        The linewidth of the frame (i.e. the edge linewidth of the figure
        patch).

    frameon : bool, default: :rc:`figure.frameon`
        If ``False``, suppress drawing the figure background patch.

    subplotpars : `~matplotlib.gridspec.SubplotParams`
        Subplot parameters. If not given, the default subplot
        parameters :rc:`figure.subplot.*` are used.

    tight_layout : bool or dict, default: :rc:`figure.autolayout`
        Whether to use the tight layout mechanism. See `.set_tight_layout`.

        .. admonition:: Discouraged

            The use of this parameter is discouraged. Please use
            ``layout='tight'`` instead for the common case of
            ``tight_layout=True`` and use `.set_tight_layout` otherwise.

    constrained_layout : bool, default: :rc:`figure.constrained_layout.use`
        This is equal to ``layout='constrained'``.

        .. admonition:: Discouraged

            The use of this parameter is discouraged. Please use
            ``layout='constrained'`` instead.

    layout : {'constrained', 'compressed', 'tight', 'none', `.LayoutEngine`, \

# ==================================================
# Line: 3010

def figimage(self, X, xo=0, yo=0, alpha=None, norm=None, cmap=None,
             vmin=None, vmax=None, origin=None, resize=False, *,
             colorizer=None, **kwargs):
    """
    Add a non-resampled image to the figure.

    The image is attached to the lower or upper left corner depending on
    *origin*.

    Parameters
    ----------
    X
        The image data. This is an array of one of the following shapes:

        - (M, N): an image with scalar data.  Color-mapping is controlled
          by *cmap*, *norm*, *vmin*, and *vmax*.
        - (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
        - (M, N, 4): an image with RGBA values (0-1 float or 0-255 int),
          i.e. including transparency.

    xo, yo : int
        The *x*/*y* image offset in pixels.

    alpha : None or float
        The alpha blending value.

    %(cmap_doc)s

        This parameter is ignored if *X* is RGB(A).

    %(norm_doc)s

        This parameter is ignored if *X* is RGB(A).

    %(vmin_vmax_doc)s

        This parameter is ignored if *X* is RGB(A).

    origin : {'upper', 'lower'}, default: :rc:`image.origin`
        Indicates where the [0, 0] index of the array is in the upper left
        or lower left corner of the Axes.

    resize : bool
        If *True*, resize the figure to match the given image size.

    %(colorizer_doc)s

        This parameter is ignored if *X* is RGB(A).

    Returns
    -------
    `matplotlib.image.FigureImage`

    Other Parameters
    ----------------
    **kwargs
        Additional kwargs are `.Artist` kwargs passed on to `.FigureImage`.

    Notes
    -----
    figimage complements the Axes image (`~matplotlib.axes.Axes.imshow`)
    which will be resampled to fit the current Axes.  If you want
    a resampled image to fill the entire figure, you can define an
    `~matplotlib.axes.Axes` with extent [0, 0, 1, 1].

    Examples
    --------
    ::

        f = plt.figure()
        nx = int(f.get_figwidth() * f.dpi)
        ny = int(f.get_figheight() * f.dpi)
        data = np.random.random((ny, nx))
        f.figimage(data)
        plt.show()
    """
    if resize:
        dpi = self.get_dpi()
        figsize = [x / dpi for x in (X.shape[1], X.shape[0])]
        self.set_size_inches(figsize, forward=True)

    im = mimage.FigureImage(self, cmap=cmap, norm=norm,
                            colorizer=colorizer,
                            offsetx=xo, offsety=yo,
                            origin=origin, **kwargs)
    im.stale_callback = _stale_figure_callback

    im.set_array(X)
    im.set_alpha(alpha)
    if norm is None:
        im._check_exclusionary_keywords(colorizer, vmin=vmin, vmax=vmax)
        im.set_clim(vmin, vmax)
    self.images.append(im)
    im._remove_method = self.images.remove
    self.stale = True
    return im


# ==================================================
# Line: 3490

def ginput(self, n=1, timeout=30, show_clicks=True,
           mouse_add=MouseButton.LEFT,
           mouse_pop=MouseButton.RIGHT,
           mouse_stop=MouseButton.MIDDLE):
    """
    Blocking call to interact with a figure.

    Wait until the user clicks *n* times on the figure, and return the
    coordinates of each click in a list.

    There are three possible interactions:

    - Add a point.
    - Remove the most recently added point.
    - Stop the interaction and return the points added so far.

    The actions are assigned to mouse buttons via the arguments
    *mouse_add*, *mouse_pop* and *mouse_stop*.

    Parameters
    ----------
    n : int, default: 1
        Number of mouse clicks to accumulate. If negative, accumulate
        clicks until the input is terminated manually.
    timeout : float, default: 30 seconds
        Number of seconds to wait before timing out. If zero or negative
        will never time out.
    show_clicks : bool, default: True
        If True, show a red cross at the location of each click.
    mouse_add : `.MouseButton` or None, default: `.MouseButton.LEFT`
        Mouse button used to add points.
    mouse_pop : `.MouseButton` or None, default: `.MouseButton.RIGHT`
        Mouse button used to remove the most recently added point.
    mouse_stop : `.MouseButton` or None, default: `.MouseButton.MIDDLE`
        Mouse button used to stop input.

    Returns
    -------
    list of tuples
        A list of the clicked (x, y) coordinates.

    Notes
    -----
    The keyboard can also be used to select points in case your mouse
    does not have one or more of the buttons.  The delete and backspace
    keys act like right-clicking (i.e., remove last point), the enter key
    terminates input and any other key (not already used by the window
    manager) selects a point.
    """
    clicks = []
    marks = []

    def handler(event):
        is_button = event.name == "button_press_event"
        is_key = event.name == "key_press_event"
        # Quit (even if not in infinite mode; this is consistent with
        # MATLAB and sometimes quite useful, but will require the user to
        # test how many points were actually returned before using data).
        if (is_button and event.button == mouse_stop
                or is_key and event.key in ["escape", "enter"]):
            self.canvas.stop_event_loop()
        # Pop last click.
        elif (is_button and event.button == mouse_pop
              or is_key and event.key in ["backspace", "delete"]):
            if clicks:
                clicks.pop()
                if show_clicks:
                    marks.pop().remove()
                    self.canvas.draw()
        # Add new click.
        elif (is_button and event.button == mouse_add
              # On macOS/gtk, some keys return None.
              or is_key and event.key is not None):
            if event.inaxes:
                clicks.append((event.xdata, event.ydata))
                _log.info("input %i: %f, %f",
                          len(clicks), event.xdata, event.ydata)
                if show_clicks:
                    line = mpl.lines.Line2D([event.xdata], [event.ydata],
                                            marker="+", color="r")
                    event.inaxes.add_line(line)
                    marks.append(line)
                    self.canvas.draw()
        if len(clicks) == n and n > 0:
            self.canvas.stop_event_loop()

    _blocking_input.blocking_input_loop(
        self, ["button_press_event", "key_press_event"], timeout, handler)

    # Cleanup.
    for mark in marks:
        mark.remove()
    self.canvas.draw()

    return clicks


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/animation.py
# Line: 746

def __init__(self, fps=30, codec=None, bitrate=None, extra_args=None,
             metadata=None, embed_frames=False, default_mode='loop',
             embed_limit=None):

    if extra_args:
        _log.warning("HTMLWriter ignores 'extra_args'")
    extra_args = ()  # Don't lookup nonexistent rcParam[args_key].
    self.embed_frames = embed_frames
    self.default_mode = default_mode.lower()
    _api.check_in_list(['loop', 'once', 'reflect'],
                       default_mode=self.default_mode)

    # Save embed limit, which is given in MB
    self._bytes_limit = mpl._val_or_rc(embed_limit, 'animation.embed_limit')
    # Convert from MB to bytes
    self._bytes_limit *= 1024 * 1024

    super().__init__(fps, codec, bitrate, extra_args, metadata)


# ==================================================
# Line: 940

def save(self, filename, writer=None, fps=None, dpi=None, codec=None,
         bitrate=None, extra_args=None, metadata=None, extra_anim=None,
         savefig_kwargs=None, *, progress_callback=None):
    """
    Save the animation as a movie file by drawing every frame.

    Parameters
    ----------
    filename : str
        The output filename, e.g., :file:`mymovie.mp4`.

    writer : `MovieWriter` or str, default: :rc:`animation.writer`
        A `MovieWriter` instance to use or a key that identifies a
        class to use, such as 'ffmpeg'.

    fps : int, optional
        Movie frame rate (per second).  If not set, the frame rate from the
        animation's frame interval.

    dpi : float, default: :rc:`savefig.dpi`
        Controls the dots per inch for the movie frames.  Together with
        the figure's size in inches, this controls the size of the movie.

    codec : str, default: :rc:`animation.codec`.
        The video codec to use.  Not all codecs are supported by a given
        `MovieWriter`.

    bitrate : int, default: :rc:`animation.bitrate`
        The bitrate of the movie, in kilobits per second.  Higher values
        means higher quality movies, but increase the file size.  A value
        of -1 lets the underlying movie encoder select the bitrate.

    extra_args : list of str or None, optional
        Extra command-line arguments passed to the underlying movie encoder. These
        arguments are passed last to the encoder, just before the output filename.
        The default, None, means to use :rc:`animation.[name-of-encoder]_args` for
        the builtin writers.

    metadata : dict[str, str], default: {}
        Dictionary of keys and values for metadata to include in
        the output file. Some keys that may be of use include:
        title, artist, genre, subject, copyright, srcform, comment.

    extra_anim : list, default: []
        Additional `Animation` objects that should be included
        in the saved movie file. These need to be from the same
        `.Figure` instance. Also, animation frames will
        just be simply combined, so there should be a 1:1 correspondence
        between the frames from the different animations.

    savefig_kwargs : dict, default: {}
        Keyword arguments passed to each `~.Figure.savefig` call used to
        save the individual frames.

    progress_callback : function, optional
        A callback function that will be called for every frame to notify
        the saving progress. It must have the signature ::

            def func(current_frame: int, total_frames: int) -> Any

        where *current_frame* is the current frame number and *total_frames* is the
        total number of frames to be saved. *total_frames* is set to None, if the
        total number of frames cannot be determined. Return values may exist but are
        ignored.

        Example code to write the progress to stdout::

            progress_callback = lambda i, n: print(f'Saving frame {i}/{n}')

    Notes
    -----
    *fps*, *codec*, *bitrate*, *extra_args* and *metadata* are used to
    construct a `.MovieWriter` instance and can only be passed if
    *writer* is a string.  If they are passed as non-*None* and *writer*
    is a `.MovieWriter`, a `RuntimeError` will be raised.
    """

    all_anim = [self]
    if extra_anim is not None:
        all_anim.extend(anim for anim in extra_anim
                        if anim._fig is self._fig)

    # Disable "Animation was deleted without rendering" warning.
    for anim in all_anim:
        anim._draw_was_started = True

    if writer is None:
        writer = mpl.rcParams['animation.writer']
    elif (not isinstance(writer, str) and
          any(arg is not None
              for arg in (fps, codec, bitrate, extra_args, metadata))):
        raise RuntimeError('Passing in values for arguments '
                           'fps, codec, bitrate, extra_args, or metadata '
                           'is not supported when writer is an existing '
                           'MovieWriter instance. These should instead be '
                           'passed as arguments when creating the '
                           'MovieWriter instance.')

    if savefig_kwargs is None:
        savefig_kwargs = {}
    else:
        # we are going to mutate this below
        savefig_kwargs = dict(savefig_kwargs)

    if fps is None and hasattr(self, '_interval'):
        # Convert interval in ms to frames per second
        fps = 1000. / self._interval

    # Reuse the savefig DPI for ours if none is given.
    dpi = mpl._val_or_rc(dpi, 'savefig.dpi')
    if dpi == 'figure':
        dpi = self._fig.dpi

    writer_kwargs = {}
    if codec is not None:
        writer_kwargs['codec'] = codec
    if bitrate is not None:
        writer_kwargs['bitrate'] = bitrate
    if extra_args is not None:
        writer_kwargs['extra_args'] = extra_args
    if metadata is not None:
        writer_kwargs['metadata'] = metadata

    # If we have the name of a writer, instantiate an instance of the
    # registered class.
    if isinstance(writer, str):
        try:
            writer_cls = writers[writer]
        except RuntimeError:  # Raised if not available.
            writer_cls = PillowWriter  # Always available.
            _log.warning("MovieWriter %s unavailable; using Pillow "
                         "instead.", writer)
        writer = writer_cls(fps, **writer_kwargs)
    _log.info('Animation.save using %s', type(writer))

    if 'bbox_inches' in savefig_kwargs:
        _log.warning("Warning: discarding the 'bbox_inches' argument in "
                     "'savefig_kwargs' as it may cause frame size "
                     "to vary, which is inappropriate for animation.")
        savefig_kwargs.pop('bbox_inches')

    # Create a new sequence of frames for saved data. This is different
    # from new_frame_seq() to give the ability to save 'live' generated
    # frame information to be saved later.
    # TODO: Right now, after closing the figure, saving a movie won't work
    # since GUI widgets are gone. Either need to remove extra code to
    # allow for this non-existent use case or find a way to make it work.

    def _pre_composite_to_white(color):
        r, g, b, a = mcolors.to_rgba(color)
        return a * np.array([r, g, b]) + 1 - a

    # canvas._is_saving = True makes the draw_event animation-starting
    # callback a no-op; canvas.manager = None prevents resizing the GUI
    # widget (both are likewise done in savefig()).
    with (writer.saving(self._fig, filename, dpi),
          cbook._setattr_cm(self._fig.canvas, _is_saving=True, manager=None)):
        if not writer._supports_transparency():
            facecolor = savefig_kwargs.get('facecolor',
                                           mpl.rcParams['savefig.facecolor'])
            if facecolor == 'auto':
                facecolor = self._fig.get_facecolor()
            savefig_kwargs['facecolor'] = _pre_composite_to_white(facecolor)
            savefig_kwargs['transparent'] = False   # just to be safe!

        for anim in all_anim:
            anim._init_draw()  # Clear the initial frame
        frame_number = 0
        # TODO: Currently only FuncAnimation has a save_count
        #       attribute. Can we generalize this to all Animations?
        save_count_list = [getattr(a, '_save_count', None)
                           for a in all_anim]
        if None in save_count_list:
            total_frames = None
        else:
            total_frames = sum(save_count_list)
        for data in zip(*[a.new_saved_frame_seq() for a in all_anim]):
            for anim, d in zip(all_anim, data):
                # TODO: See if turning off blit is really necessary
                anim._draw_next_frame(d, blit=False)
                if progress_callback is not None:
                    progress_callback(frame_number, total_frames)
                    frame_number += 1
            writer.grab_frame(**savefig_kwargs)


# ==================================================
# Line: 1650

def __init__(self, fig, func, frames=None, init_func=None, fargs=None,
             save_count=None, *, cache_frame_data=True, **kwargs):
    if fargs:
        self._args = fargs
    else:
        self._args = ()
    self._func = func
    self._init_func = init_func

    # Amount of framedata to keep around for saving movies. This is only
    # used if we don't know how many frames there will be: in the case
    # of no generator or in the case of a callable.
    self._save_count = save_count
    # Set up a function that creates a new iterable when needed. If nothing
    # is passed in for frames, just use itertools.count, which will just
    # keep counting from 0. A callable passed in for frames is assumed to
    # be a generator. An iterable will be used as is, and anything else
    # will be treated as a number of frames.
    if frames is None:
        self._iter_gen = itertools.count
    elif callable(frames):
        self._iter_gen = frames
    elif np.iterable(frames):
        if kwargs.get('repeat', True):
            self._tee_from = frames
            def iter_frames(frames=frames):
                this, self._tee_from = itertools.tee(self._tee_from, 2)
                yield from this
            self._iter_gen = iter_frames
        else:
            self._iter_gen = lambda: iter(frames)
        if hasattr(frames, '__len__'):
            self._save_count = len(frames)
            if save_count is not None:
                _api.warn_external(
                    f"You passed in an explicit {save_count=} "
                    "which is being ignored in favor of "
                    f"{len(frames)=}."
                )
    else:
        self._iter_gen = lambda: iter(range(frames))
        self._save_count = frames
        if save_count is not None:
            _api.warn_external(
                f"You passed in an explicit {save_count=} which is being "
                f"ignored in favor of {frames=}."
            )
    if self._save_count is None and cache_frame_data:
        _api.warn_external(
            f"{frames=!r} which we can infer the length of, "
            "did not pass an explicit *save_count* "
            f"and passed {cache_frame_data=}.  To avoid a possibly "
            "unbounded cache, frame data caching has been disabled. "
            "To suppress this warning either pass "
            "`cache_frame_data=False` or `save_count=MAX_FRAMES`."
        )
        cache_frame_data = False

    self._cache_frame_data = cache_frame_data

    # Needs to be initialized so the draw functions work without checking
    self._save_seq = []

    super().__init__(fig, **kwargs)

    # Need to reset the saved seq, since right now it will contain data
    # for a single frame from init, which is not what we want.
    self._save_seq = []


# ==================================================
