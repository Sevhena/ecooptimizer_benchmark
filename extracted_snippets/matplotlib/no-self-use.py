# no-self-use snippets for matplotlib

# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/axis_artist.py
# Line: 94

def get_ref_artist(self):
    """
    Return the underlying artist that actually defines some properties
    (e.g., color) of this artist.
    """
    raise RuntimeError("get_ref_artist must overridden")


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/axisline_style.py
# Line: 41

def _extend_path(self, path, mutation_size=10):
    """
    Extend the path to make a room for drawing arrow.
    """
    (x0, y0), (x1, y1) = path.vertices[-2:]
    theta = math.atan2(y1 - y0, x1 - x0)
    x2 = x1 + math.cos(theta) * mutation_size
    y2 = y1 + math.sin(theta) * mutation_size
    if path.codes is None:
        return Path(np.concatenate([path.vertices, [[x2, y2]]]))
    else:
        return Path(np.concatenate([path.vertices, [[x2, y2]]]),
                    np.concatenate([path.codes, [Path.LINETO]]))


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/grid_helper_curvelinear.py
# Line: 200

def get_axislabel_transform(self, axes):
    return Affine2D()  # axes.transData


# ==================================================
# Line: 223

def get_tick_transform(self, axes):
    return IdentityTransform()  # axes.transData


# ==================================================
# Line: 268

def get_line_transform(self, axes):
    return axes.transData


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/axislines.py
# Occurrences: Lines 137-142 (2 instances)

def get_line_transform(self, axes):
    return axes.transAxes


# ==================================================
# Line: 167

def get_line(self, axes):
    raise RuntimeError("get_line method should be defined by the derived class")



# ==================================================
# Occurrences: Lines 218-221 (2 instances)

def get_line_transform(self, axes):
    return axes.transAxes


# ==================================================
# Line: 237

def get_tick_transform(self, axes):
    return axes.transData


# ==================================================
# Line: 290

def get_gridlines(self, which, axis):
    """
    Return list of grid lines as a list of paths (list of points).

    Parameters
    ----------
    which : {"both", "major", "minor"}
    axis : {"both", "x", "y"}
    """
    return []



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/angle_helper.py
# Line: 203

def _get_number_fraction(self, factor):
    ## check for fractional numbers
    number_fraction = None
    # check for 60

    for threshold in [1, 60, 3600]:
        if factor <= threshold:
            break

        d = factor // threshold
        int_log_d = int(np.floor(np.log10(d)))
        if 10**int_log_d == d and d != 1:
            number_fraction = int_log_d
            factor = factor // 10**int_log_d
            return factor, number_fraction

    return factor, number_fraction


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/mplot3d/axis3d.py
# Occurrences: Lines 54-58 (2 instances)

def _old_init(self, adir, v_intervalx, d_intervalx, axes, *args,
              rotate_label=None, **kwargs):
    return locals()


# ==================================================
# Line: 301

def _calc_centers_deltas(self, maxs, mins):
    centers = 0.5 * (maxs + mins)
    # In mpl3.8, the scale factor was 1/12. mpl3.9 changes this to
    # 1/12 * 24/25 = 0.08 to compensate for the change in automargin
    # behavior and keep appearance the same. The 24/25 factor is from the
    # 1/48 padding added to each side of the axis in mpl3.8.
    scale = 0.08
    deltas = (maxs - mins) * scale
    return centers, deltas


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/mplot3d/art3d.py
# Line: 200

def get_tightbbox(self, renderer=None):
    # Overwriting the 2d Text behavior which is not valid for 3d.
    # For now, just return None to exclude from layout calculation.
    return None



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/mplot3d/axes3d.py
# Line: 333

def _equal_aspect_axis_indices(self, aspect):
    """
    Get the indices for which of the x, y, z axes are constrained to have
    equal aspect ratios.

    Parameters
    ----------
    aspect : {'auto', 'equal', 'equalxy', 'equalxz', 'equalyz'}
        See descriptions in docstring for `.set_aspect()`.
    """
    ax_indices = []  # aspect == 'auto'
    if aspect == 'equal':
        ax_indices = [0, 1, 2]
    elif aspect == 'equalxy':
        ax_indices = [0, 1]
    elif aspect == 'equalxz':
        ax_indices = [0, 2]
    elif aspect == 'equalyz':
        ax_indices = [1, 2]
    return ax_indices


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
# Line: 1091

def clabel(self, *args, **kwargs):
    """Currently not implemented for 3D Axes, and returns *None*."""
    return None


# ==================================================
# Occurrences: Lines 1302-1306 (2 instances)

def can_zoom(self):
    # doc-string inherited
    return True


# ==================================================
# Line: 1511

def _arcball(self, x: float, y: float) -> np.ndarray:
    """
    Convert a point (x, y) to a point on a virtual trackball.

    This is Ken Shoemake's arcball (a sphere), modified
    to soften the abrupt edge (optionally).
    See: Ken Shoemake, "ARCBALL: A user interface for specifying
    three-dimensional rotation using a mouse." in
    Proceedings of Graphics Interface '92, 1992, pp. 151-156,
    https://doi.org/10.20380/GI1992.18
    The smoothing of the edge is inspired by Gavin Bell's arcball
    (a sphere combined with a hyperbola), but here, the sphere
    is combined with a section of a cylinder, so it has finite support.
    """
    s = mpl.rcParams['axes3d.trackballsize'] / 2
    b = mpl.rcParams['axes3d.trackballborder'] / s
    x /= s
    y /= s
    r2 = x*x + y*y
    r = np.sqrt(r2)
    ra = 1 + b
    a = b * (1 + b/2)
    ri = 2/(ra + 1/ra)
    if r < ri:
        p = np.array([np.sqrt(1 - r2), x, y])
    elif r < ra:
        dr = ra - r
        p = np.array([a - np.sqrt((a + dr) * (a - dr)), x, y])
        p /= np.linalg.norm(p)
    else:
        p = np.array([0, x/r, y/r])
    return p


# ==================================================
# Line: 2610

def _add_contourf_set(self, cset, zdir='z', offset=None, axlim_clip=False):
    """
    Returns
    -------
    levels : `numpy.ndarray`
        Levels at which the filled contours are added.
    """
    zdir = '-' + zdir

    midpoints = cset.levels[:-1] + np.diff(cset.levels) / 2
    # Linearly interpolate to get levels for any extensions
    if cset._extend_min:
        min_level = cset.levels[0] - np.diff(cset.levels[:2]) / 2
        midpoints = np.insert(midpoints, 0, min_level)
    if cset._extend_max:
        max_level = cset.levels[-1] + np.diff(cset.levels[-2:]) / 2
        midpoints = np.append(midpoints, max_level)

    art3d.collection_2d_to_3d(
        cset, zs=offset if offset is not None else midpoints, zdir=zdir,
        axlim_clip=axlim_clip)
    return midpoints


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axes_grid1/inset_locator.py
# Line: 24

def draw(self, renderer):
    raise RuntimeError("No draw method should be called")


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axes_grid1/axes_divider.py
# Line: 104

def get_subplotspec(self):
    return None


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backend_tools.py
# Line: 438

def set_scale(self, ax, scale):
    ax.set_yscale(scale)



# ==================================================
# Line: 448

def set_scale(self, ax, scale):
    ax.set_xscale(scale)



# ==================================================
# Line: 537

def _axes_pos(self, ax):
    """
    Return the original and modified positions for the specified Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The `.Axes` to get the positions for.

    Returns
    -------
    original_position, modified_position
        A tuple of the original and modified positions.
    """

    return (ax.get_position(True).frozen(),
            ax.get_position().frozen())


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/collections.py
# Line: 645

def _get_default_linewidth(self):
    # This may be overridden in a subclass.
    return mpl.rcParams['patch.linewidth']  # validated as float


# ==================================================
# Line: 807

def _get_default_antialiased(self):
    # This may be overridden in a subclass.
    return mpl.rcParams['patch.antialiased']


# ==================================================
# Line: 831

def _get_default_facecolor(self):
    # This may be overridden in a subclass.
    return mpl.rcParams['patch.facecolor']


# ==================================================
# Line: 868

def _get_default_edgecolor(self):
    # This may be overridden in a subclass.
    return mpl.rcParams['patch.edgecolor']


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/_backend_pdf_ps.py
# Occurrences: Lines 130-138 (3 instances)

def flipy(self):
    # docstring inherited
    return False  # y increases from bottom to top.


# ==================================================
# Line: 178

def _get_font_ttf(self, prop):
    fnames = font_manager.fontManager._find_fonts_by_props(prop)
    try:
        font = font_manager.get_font(fnames)
        font.clear()
        font.set_size(prop.get_size_in_points(), 72)
        return font
    except RuntimeError:
        logging.getLogger(__name__).warning(
            "The PostScript/PDF backend does not currently "
            "support the selected font (%s).", fnames)
        raise

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/registry.py
# Line: 128

def _read_entry_points(self):
    # Read entry points of modules that self-advertise as Matplotlib backends.
    # Expects entry points like this one from matplotlib-inline (in pyproject.toml
    # format):
    #   [project.entry-points."matplotlib.backend"]
    #   inline = "matplotlib_inline.backend_inline"
    import importlib.metadata as im

    entry_points = im.entry_points(group="matplotlib.backend")
    entries = [(entry.name, entry.value) for entry in entry_points]

    # For backward compatibility, if matplotlib-inline and/or ipympl are installed
    # but too old to include entry points, create them. Do not import ipympl
    # directly as this calls matplotlib.use() whilst in this function.
    def backward_compatible_entry_points(
            entries, module_name, threshold_version, names, target):
        from matplotlib import _parse_to_version_info
        try:
            module_version = im.version(module_name)
            if _parse_to_version_info(module_version) < threshold_version:
                for name in names:
                    entries.append((name, target))
        except im.PackageNotFoundError:
            pass

    names = [entry[0] for entry in entries]
    if "inline" not in names:
        backward_compatible_entry_points(
            entries, "matplotlib_inline", (0, 1, 7), ["inline"],
            "matplotlib_inline.backend_inline")
    if "ipympl" not in names:
        backward_compatible_entry_points(
            entries, "ipympl", (0, 9, 4), ["ipympl", "widget"],
            "ipympl.backend_nbagg")

    return entries


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_wx.py
# Line: 140

def flipy(self):
    # docstring inherited
    return True


# ==================================================
# Line: 551

def flush_events(self):
    # docstring inherited
    wx.Yield()


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_gtk4.py
# Line: 223

def _get_key(self, keyval, keycode, state):
    unikey = chr(Gdk.keyval_to_unicode(keyval))
    key = cbook._unikey_or_keysym_to_mplkey(
        unikey,
        Gdk.keyval_name(keyval))
    modifiers = [
        ("ctrl", Gdk.ModifierType.CONTROL_MASK, "control"),
        ("alt", Gdk.ModifierType.ALT_MASK, "alt"),
        ("shift", Gdk.ModifierType.SHIFT_MASK, "shift"),
        ("super", Gdk.ModifierType.SUPER_MASK, "super"),
    ]
    mods = [
        mod for mod, mask, mod_key in modifiers
        if (mod_key != key and state & mask
            and not (mod == "shift" and unikey.isprintable()))]
    return "+".join([*mods, key])


# ==================================================
# Line: 308

def flush_events(self):
    # docstring inherited
    context = GLib.MainContext.default()
    while context.pending():
        context.iteration(True)



# ==================================================
# Line: 527

def _normalize_shortcut(self, key):
    """
    Convert Matplotlib key presses to GTK+ accelerator identifiers.

    Related to `FigureCanvasGTK4._get_key`.
    """
    special = {
        'backspace': 'BackSpace',
        'pagedown': 'Page_Down',
        'pageup': 'Page_Up',
        'scroll_lock': 'Scroll_Lock',
    }

    parts = key.split('+')
    mods = ['<' + mod + '>' for mod in parts[:-1]]
    key = parts[-1]

    if key in special:
        key = special[key]
    elif len(key) > 1:
        key = key.capitalize()
    elif key.isupper():
        mods += ['<shift>']

    return ''.join(mods) + key


# ==================================================
# Line: 553

def _is_valid_shortcut(self, key):
    """
    Check for a valid shortcut to be displayed.

    - GTK will never send 'cmd+' (see `FigureCanvasGTK4._get_key`).
    - The shortcut window only shows keyboard shortcuts, not mouse buttons.
    """
    return 'cmd+' not in key and not key.startswith('MouseButton.')


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_webagg_core.py
# Line: 181

def show(self):
    # show the figure window
    from matplotlib.pyplot import show
    show()


# ==================================================
# Line: 266

def handle_unknown_event(self, event):
    _log.warning('Unhandled message type %s. %s', event["type"], event)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_pdf.py
# Line: 1045

def _generate_encoding(self, encoding):
    prev = -2
    result = []
    for code, name in sorted(encoding.items()):
        if code != prev + 1:
            result.append(code)
        prev = code
        result.append(Name(name))
    return {
        'Type': Name('Encoding'),
        'Differences': result
    }



# ==================================================
# Line: 1696

def _unpack(self, im):
    """
    Unpack image array *im* into ``(data, alpha)``, which have shape
    ``(height, width, 3)`` (RGB) or ``(height, width, 1)`` (grayscale or
    alpha), except that alpha is None if the image is fully opaque.
    """
    im = im[::-1]
    if im.ndim == 2:
        return im, None
    else:
        rgb = im[:, :, :3]
        rgb = np.array(rgb, order='C')
        # PDF needs a separate alpha image
        if im.shape[2] == 4:
            alpha = im[:, :, 3][..., None]
            if np.all(alpha == 255):
                alpha = None
            else:
                alpha = np.array(alpha, order='C')
        else:
            alpha = None
        return rgb, alpha


# ==================================================
# Line: 1719

def _writePng(self, img):
    """
    Write the image *img* into the pdf file using png
    predictors with Flate compression.
    """
    buffer = BytesIO()
    img.save(buffer, format="png")
    buffer.seek(8)
    png_data = b''
    bit_depth = palette = None
    while True:
        length, type = struct.unpack(b'!L4s', buffer.read(8))
        if type in [b'IHDR', b'PLTE', b'IDAT']:
            data = buffer.read(length)
            if len(data) != length:
                raise RuntimeError("truncated data")
            if type == b'IHDR':
                bit_depth = int(data[8])
            elif type == b'PLTE':
                palette = data
            elif type == b'IDAT':
                png_data += data
        elif type == b'IEND':
            break
        else:
            buffer.seek(length, 1)
        buffer.seek(4, 1)   # skip CRC
    return png_data, bit_depth, palette


# ==================================================
# Line: 2352

def encode_string(self, s, fonttype):
    if fonttype in (1, 3):
        return s.encode('cp1252', 'replace')
    return s.encode('utf-16be', 'replace')


# ==================================================
# Occurrences: Lines 2527-2530 (2 instances)

def linewidth_cmd(self, width):
    return [width, Op.setlinewidth]


# ==================================================
# Line: 2553

def rgb_cmd(self, rgb):
    if mpl.rcParams['pdf.inheritcolor']:
        return []
    if rgb[0] == rgb[1] == rgb[2]:
        return [rgb[0], Op.setgray_stroke]
    else:
        return [*rgb[:3], Op.setrgb_stroke]


# ==================================================
# Line: 2561

def fillcolor_cmd(self, rgb):
    if rgb is None or mpl.rcParams['pdf.inheritcolor']:
        return []
    elif rgb[0] == rgb[1] == rgb[2]:
        return [rgb[0], Op.setgray_nonstroke]
    else:
        return [*rgb[:3], Op.setrgb_nonstroke]


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_gtk3.py
# Line: 296

def flush_events(self):
    # docstring inherited
    context = GLib.MainContext.default()
    while context.pending():
        context.iteration(True)



# ==================================================
# Line: 487

def _normalize_shortcut(self, key):
    """
    Convert Matplotlib key presses to GTK+ accelerator identifiers.

    Related to `FigureCanvasGTK3._get_key`.
    """
    special = {
        'backspace': 'BackSpace',
        'pagedown': 'Page_Down',
        'pageup': 'Page_Up',
        'scroll_lock': 'Scroll_Lock',
    }

    parts = key.split('+')
    mods = ['<' + mod + '>' for mod in parts[:-1]]
    key = parts[-1]

    if key in special:
        key = special[key]
    elif len(key) > 1:
        key = key.capitalize()
    elif key.isupper():
        mods += ['<shift>']

    return ''.join(mods) + key


# ==================================================
# Line: 513

def _is_valid_shortcut(self, key):
    """
    Check for a valid shortcut to be displayed.

    - GTK will never send 'cmd+' (see `FigureCanvasGTK3._get_key`).
    - The shortcut window only shows keyboard shortcuts, not mouse buttons.
    """
    return 'cmd+' not in key and not key.startswith('MouseButton.')


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_pgf.py
# Occurrences: Lines 623-627 (2 instances)

def option_scale_image(self):
    # docstring inherited
    return True


# ==================================================
# Line: 735

def flipy(self):
    # docstring inherited
    return False


# ==================================================
# Line: 754

def get_default_filetype(self):
    return 'pdf'


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_qt.py
# Line: 399

def minimumSizeHint(self):
    return QtCore.QSize(10, 10)


# ==================================================
# Line: 449

def flush_events(self):
    # docstring inherited
    QtWidgets.QApplication.instance().processEvents()


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_nbagg.py
# Line: 86

def display_js(self):
    # XXX How to do this just once? It has to deal with multiple
    # browser instances using the same kernel (require.js - but the
    # file isn't static?).
    display(Javascript(FigureManagerNbAgg.get_javascript()))


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_svg.py
# Line: 482

def _make_id(self, type, content):
    salt = mpl.rcParams['svg.hashsalt']
    if salt is None:
        salt = str(uuid.uuid4())
    m = hashlib.sha256()
    m.update(salt.encode('utf8'))
    m.update(str(content).encode('utf8'))
    return f'{type}{m.hexdigest()[:10]}'


# ==================================================
# Line: 1037

def _adjust_char_id(self, char_id):
    return char_id.replace("%20", "_")


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/ticker.py
# Line: 183

def get_tick_space(self):
    # Just use the long-standing default of nbins==9
    return 9



# ==================================================
# Line: 234

def get_offset(self):
    return ''


# ==================================================
# Line: 1044

def _pprint_val(self, x, d):
    # If the number is not too big and it's an int, format it as an int.
    if abs(x) < 1e4 and x == int(x):
        return '%d' % x
    fmt = ('%1.3e' if d < 1e-2 else
           '%1.3f' if d <= 1 else
           '%1.2f' if d <= 10 else
           '%1.1f' if d <= 1e5 else
           '%1.1e')
    s = fmt % x
    tup = s.split('e')
    if len(tup) == 2:
        mantissa = tup[0].rstrip('0').rstrip('.')
        exponent = int(tup[1])
        if exponent:
            s = '%se%d' % (mantissa, exponent)
        else:
            s = mantissa
    else:
        s = s.rstrip('0').rstrip('.')
    return s



# ==================================================
# Line: 1087

def _non_decade_format(self, sign_string, base, fx, usetex):
    """Return string for non-decade locations."""
    return r'$\mathdefault{%s%s^{%.2f}}$' % (sign_string, base, fx)


# ==================================================
# Line: 1278

def _format_value(self, x, locs, sci_notation=True):
    if sci_notation:
        exponent = math.floor(np.log10(x))
        min_precision = 0
    else:
        exponent = 0
        min_precision = 1
    value = x * 10 ** (-exponent)
    if len(locs) < 2:
        precision = min_precision
    else:
        diff = np.sort(np.abs(locs - x))[1]
        precision = -np.log10(diff) + exponent
        precision = (
            int(np.round(precision))
            if _is_close_to_int(precision)
            else math.ceil(precision)
        )
        if precision < min_precision:
            precision = min_precision
    mantissa = r"%.*f" % (precision, value)
    if not sci_notation:
        return mantissa
    s = r"%s\cdot10^{%d}" % (mantissa, exponent)
    return s


# ==================================================
# Line: 1719

def nonsingular(self, v0, v1):
    """
    Adjust a range as needed to avoid singularities.

    This method gets called during autoscaling, with ``(v0, v1)`` set to
    the data limits on the Axes if the Axes contains any data, or
    ``(-inf, +inf)`` if not.

    - If ``v0 == v1`` (possibly up to some floating point slop), this
      method returns an expanded interval around this value.
    - If ``(v0, v1) == (-inf, +inf)``, this method returns appropriate
      default view limits.
    - Otherwise, ``(v0, v1)`` is returned without modification.
    """
    return mtransforms.nonsingular(v0, v1, expander=.05)


# ==================================================
# Line: 1735

def view_limits(self, vmin, vmax):
    """
    Select a scale for the range from vmin to vmax.

    Subclasses should override this method to change locator behaviour.
    """
    return mtransforms.nonsingular(vmin, vmax)



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/image.py
# Line: 585

def _check_unsampled_image(self):
    """
    Return whether the image is better to be drawn unsampled.

    The derived class needs to override it.
    """
    return False


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/contour.py
# Line: 217

def print_label(self, linecontour, labelwidth):
    """Return whether a contour is long enough to hold a label."""
    return (len(linecontour) > 10 * labelwidth
            or (len(linecontour)
                and (np.ptp(linecontour, axis=0) > 1.2 * labelwidth).any()))


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/artist.py
# Line: 322

def get_window_extent(self, renderer=None):
    """
    Get the artist's bounding box in display space.

    The bounding box's width and height are non-negative.

    Subclasses should override for inclusion in the bounding box
    "tight" calculation. Default is to return an empty bounding
    box at 0, 0.

    .. warning::

      The extent can change due to any changes in the transform stack, such
      as changing the Axes limits, the figure size, the canvas used (as is
      done when saving a figure), or the DPI.

      Relying on a once-retrieved window extent can lead to unexpected
      behavior in various cases such as interactive figures being resized or
      moved to a screen with different dpi, or figures that look fine on
      screen render incorrectly when saved to file.

      To get accurate results you may need to manually call
      `matplotlib.figure.Figure.savefig` or
      `matplotlib.figure.Figure.draw_without_rendering` to have Matplotlib
      compute the rendered size.

    """
    return Bbox([[0, 0], [0, 0]])


# ==================================================
# Line: 460

def get_children(self):
    r"""Return a list of the child `.Artist`\s of this `.Artist`."""
    return []


# ==================================================
# Line: 1302

def get_cursor_data(self, event):
    """
    Return the cursor data for a given event.

    .. note::
        This method is intended to be overridden by artist subclasses.
        As an end-user of Matplotlib you will most likely not call this
        method yourself.

    Cursor data can be used by Artists to provide additional context
    information for a given event. The default implementation just returns
    *None*.

    Subclasses can override the method and return arbitrary data. However,
    when doing so, they must ensure that `.format_cursor_data` can convert
    the data to a string representation.

    The only current use case is displaying the z-value of an `.AxesImage`
    in the status bar of a plot window, while moving the mouse.

    Parameters
    ----------
    event : `~matplotlib.backend_bases.MouseEvent`

    See Also
    --------
    format_cursor_data

    """
    return None


# ==================================================
# Line: 1503

def _replace_path(self, source_class):
    """
    Changes the full path to the public API path that is used
    in sphinx. This is needed for links to work.
    """
    replace_dict = {'_base._AxesBase': 'Axes',
                    '_axes.Axes': 'Axes'}
    for key, value in replace_dict.items():
        source_class = source_class.replace(key, value)
    return source_class


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/patches.py
# Line: 320

def get_patch_transform(self):
    """
    Return the `~.transforms.Transform` instance mapping patch coordinates
    to data coordinates.

    For example, one may define a patch of a circle which represents a
    radius of 5 by providing coordinates for a unit circle, and a
    transform which scales the coordinates (the patch coordinate) by 5.
    """
    return transforms.IdentityTransform()


# ==================================================
# Line: 2820

def _in_patch(self, patch):
    """
    Return a predicate function testing whether a point *xy* is
    contained in *patch*.
    """
    return lambda xy: patch.contains(
        SimpleNamespace(x=xy[0], y=xy[1]))[0]


# ==================================================
# Line: 2828

def _clip(self, path, in_start, in_stop):
    """
    Clip *path* at its start by the region where *in_start* returns
    True, and at its stop by the region where *in_stop* returns True.

    The original path is assumed to start in the *in_start* region and
    to stop in the *in_stop* region.
    """
    if in_start:
        try:
            _, path = split_path_inout(path, in_start)
        except ValueError:
            pass
    if in_stop:
        try:
            path, _ = split_path_inout(path, in_stop)
        except ValueError:
            pass
    return path


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
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/textpath.py
# Occurrences: Lines 39-42 (2 instances)

def _get_hinting_flag(self):
    return LoadFlags.NO_HINTING


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/colorbar.py
# Line: 1265

def _get_extension_lengths(self, frac, automin, automax, default=0.05):
    """
    Return the lengths of colorbar extensions.

    This is a helper method for _uniform_y and _proportional_y.
    """
    # Set the default value.
    extendlength = np.array([default, default])
    if isinstance(frac, str):
        _api.check_in_list(['auto'], extendfrac=frac.lower())
        # Use the provided values when 'auto' is required.
        extendlength[:] = [automin, automax]
    elif frac is not None:
        try:
            # Try to set min and max extension fractions directly.
            extendlength[:] = frac
            # If frac is a sequence containing None then NaN may
            # be encountered. This is an error.
            if np.isnan(extendlength).any():
                raise ValueError()
        except (TypeError, ValueError) as err:
            # Raise an error on encountering an invalid value for frac.
            raise ValueError('invalid value for extendfrac') from err
    return extendlength


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backend_bases.py
# Line: 298

def _iter_collection_raw_paths(self, master_transform, paths,
                               all_transforms):
    """
    Helper method (along with `_iter_collection`) to implement
    `draw_path_collection` in a memory-efficient manner.

    This method yields all of the base path/transform combinations, given a
    master transform, a list of paths and list of transforms.

    The arguments should be exactly what is passed in to
    `draw_path_collection`.

    The backend should take each yielded path and transform and create an
    object that can be referenced (reused) later.
    """
    Npaths = len(paths)
    Ntransforms = len(all_transforms)
    N = max(Npaths, Ntransforms)

    if Npaths == 0:
        return

    transform = transforms.IdentityTransform()
    for i in range(N):
        path = paths[i % Npaths]
        if Ntransforms:
            transform = Affine2D(all_transforms[i % Ntransforms])
        yield path, transform + master_transform


# ==================================================
# Line: 327

def _iter_collection_uses_per_path(self, paths, all_transforms,
                                   offsets, facecolors, edgecolors):
    """
    Compute how many times each raw path object returned by
    `_iter_collection_raw_paths` would be used when calling
    `_iter_collection`. This is intended for the backend to decide
    on the tradeoff between using the paths in-line and storing
    them once and reusing. Rounds up in case the number of uses
    is not the same for every path.
    """
    Npaths = len(paths)
    if Npaths == 0 or len(facecolors) == len(edgecolors) == 0:
        return 0
    Npath_ids = max(Npaths, len(all_transforms))
    N = max(Npath_ids, len(offsets))
    return (N + Npath_ids - 1) // Npath_ids


# ==================================================
# Line: 426

def get_image_magnification(self):
    """
    Get the factor by which to magnify images passed to `draw_image`.
    Allows a backend to have images at a different resolution to other
    artists.
    """
    return 1.0


# ==================================================
# Line: 467

def option_image_nocomposite(self):
    """
    Return whether image composition by Matplotlib should be skipped.

    Raster backends should usually return False (letting the C-level
    rasterizer take care of image composition); vector backends should
    usually return ``not rcParams["image.composite_image"]``.
    """
    return False


# ==================================================
# Line: 477

def option_scale_image(self):
    """
    Return whether arbitrary affine transformations in
    `~.RendererBase.draw_image` are supported (True for most vector backends).
    """
    return False


# ==================================================
# Line: 599

def flipy(self):
    """
    Return whether y values increase from top to bottom.

    Note that this only affects drawing of texts.
    """
    return True


# ==================================================
# Line: 607

def get_canvas_width_height(self):
    """Return the canvas width and height in display coords."""
    return 1, 1


# ==================================================
# Occurrences: Lines 617-621 (2 instances)

def new_gc(self):
    """Return an instance of a `.GraphicsContextBase`."""
    return GraphicsContextBase()


# ==================================================
# Line: 3588

def mainloop(self):
    return cls.mainloop()


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/tri/_triinterpolate.py
# Line: 881

def get_Hrot_from_J(self, J, return_area=False):
    """
    Parameters
    ----------
    *J* is a (N x 2 x 2) array of jacobian matrices (jacobian matrix at
    triangle first apex)

    Returns
    -------
    Returns H_rot used to rotate Hessian from local basis of first apex,
    to global coordinates.
    if *return_area* is True, returns also the triangle area (0.5*det(J))
    """
    # Here we try to deal with the simplest colinear cases; a null
    # energy and area is imposed.
    J_inv = _safe_inv22_vectorized(J)
    Ji00 = J_inv[:, 0, 0]
    Ji11 = J_inv[:, 1, 1]
    Ji10 = J_inv[:, 1, 0]
    Ji01 = J_inv[:, 0, 1]
    H_rot = _to_matrix_vectorized([
        [Ji00*Ji00, Ji10*Ji10, Ji00*Ji10],
        [Ji01*Ji01, Ji11*Ji11, Ji01*Ji11],
        [2*Ji00*Ji01, 2*Ji11*Ji10, Ji00*Ji11+Ji10*Ji01]])
    if not return_area:
        return H_rot
    else:
        area = 0.5 * (J[:, 0, 0]*J[:, 1, 1] - J[:, 0, 1]*J[:, 1, 0])
        return H_rot, area


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/axis.py
# Line: 1594

def _copy_tick_props(self, src, dest):
    """Copy the properties from *src* tick to *dest* tick."""
    if src is None or dest is None:
        return
    dest.label1.update_from(src.label1)
    dest.label2.update_from(src.label2)
    dest.tick1line.update_from(src.tick1line)
    dest.tick2line.update_from(src.tick2line)
    dest.gridline.update_from(src.gridline)
    dest.update_from(src)
    dest._loc = src._loc
    dest._size = src._size
    dest._width = src._width
    dest._base_pad = src._base_pad
    dest._labelrotation = src._labelrotation
    dest._zorder = src._zorder
    dest._tickdir = src._tickdir


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/dviread.py
# Line: 555

def _malformed(self, offset):
    raise ValueError(f"unknown command: byte {250 + offset}")



# ==================================================
# Line: 1095

def _new_proc(self):
    return subprocess.Popen(
        ["luatex", "--luaonly",
         str(cbook._get_data_path("kpsewhich.lua"))],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/dates.py
# Line: 1000

def _attach_tzinfo(self, dt, tzinfo):
    # pytz zones are attached by "localizing" the datetime
    if hasattr(tzinfo, 'localize'):
        return tzinfo.localize(dt, is_dst=True)

    return dt.replace(tzinfo=tzinfo)


# ==================================================
# Line: 1106

def _get_unit(self):
    """
    Return how many days a unit of the locator is; used for
    intelligent autoscaling.
    """
    return 1


# ==================================================
# Line: 1113

def _get_interval(self):
    """
    Return the number of units for each tick.
    """
    return 1


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/colors.py
# Line: 3769

def blend_soft_light(self, rgb, intensity):
    """
    Combine an RGB image with an intensity map using "soft light" blending,
    using the "pegtop" formula.

    Parameters
    ----------
    rgb : `~numpy.ndarray`
        An (M, N, 3) RGB array of floats ranging from 0 to 1 (color image).
    intensity : `~numpy.ndarray`
        An (M, N, 1) array of floats ranging from 0 to 1 (grayscale image).

    Returns
    -------
    `~numpy.ndarray`
        An (M, N, 3) RGB array representing the combined images.
    """
    return 2 * intensity * rgb + (1 - 2 * intensity) * rgb**2


# ==================================================
# Line: 3788

def blend_overlay(self, rgb, intensity):
    """
    Combine an RGB image with an intensity map using "overlay" blending.

    Parameters
    ----------
    rgb : `~numpy.ndarray`
        An (M, N, 3) RGB array of floats ranging from 0 to 1 (color image).
    intensity : `~numpy.ndarray`
        An (M, N, 1) array of floats ranging from 0 to 1 (grayscale image).

    Returns
    -------
    ndarray
        An (M, N, 3) RGB array representing the combined images.
    """
    low = 2 * intensity * rgb
    high = 1 - 2 * (1 - intensity) * (1 - rgb)
    return np.where(rgb <= 0.5, low, high)



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/projections/polar.py
# Line: 532

def _determine_anchor(self, mode, angle, start):
    # Note: angle is the (spine angle - 90) because it's used for the tick
    # & text setup, so all numbers below are -90 from (normed) spine angle.
    if mode == 'auto':
        if start:
            if -90 <= angle <= 90:
                return 'left', 'center'
            else:
                return 'right', 'center'
        else:
            if -90 <= angle <= 90:
                return 'right', 'center'
            else:
                return 'left', 'center'
    else:
        if start:
            if angle < -68.5:
                return 'center', 'top'
            elif angle < -23.5:
                return 'left', 'top'
            elif angle < 22.5:
                return 'left', 'center'
            elif angle < 67.5:
                return 'left', 'bottom'
            elif angle < 112.5:
                return 'center', 'bottom'
            elif angle < 157.5:
                return 'right', 'bottom'
            elif angle < 202.5:
                return 'right', 'center'
            elif angle < 247.5:
                return 'right', 'top'
            else:
                return 'center', 'top'
        else:
            if angle < -68.5:
                return 'center', 'bottom'
            elif angle < -23.5:
                return 'right', 'bottom'
            elif angle < 22.5:
                return 'right', 'center'
            elif angle < 67.5:
                return 'right', 'top'
            elif angle < 112.5:
                return 'center', 'top'
            elif angle < 157.5:
                return 'left', 'top'
            elif angle < 202.5:
                return 'left', 'center'
            elif angle < 247.5:
                return 'left', 'bottom'
            else:
                return 'center', 'bottom'


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/projections/geo.py
# Line: 142

def set_yscale(self, *args, **kwargs):
    if args[0] != 'linear':
        raise NotImplementedError


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/patheffects.py
# Line: 39

def _update_gc(self, gc, new_gc_dict):
    """
    Update the given GraphicsContext with the given dict of properties.

    The keys in the dictionary are used to identify the appropriate
    ``set_`` method on the *gc*.
    """
    new_gc_dict = new_gc_dict.copy()

    dashes = new_gc_dict.pop("dashes", None)
    if dashes:
        gc.set_dashes(**dashes)

    for k, v in new_gc_dict.items():
        set_method = getattr(gc, 'set_' + k, None)
        if not callable(set_method):
            raise AttributeError(f'Unknown property {k}')
        set_method(v)
    return gc


# ==================================================
# Line: 59

def draw_path(self, renderer, gc, tpath, affine, rgbFace=None):
    """
    Derived should override this method. The arguments are the same
    as :meth:`matplotlib.backend_bases.RendererBase.draw_path`
    except the first argument is a renderer.
    """
    # Get the real renderer, not a PathEffectRenderer.
    if isinstance(renderer, PathEffectRenderer):
        renderer = renderer._renderer
    return renderer.draw_path(gc, tpath, affine, rgbFace)



# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/sankey.py
# Line: 169

def _arc(self, quadrant=0, cw=True, radius=1, center=(0, 0)):
    """
    Return the codes and vertices for a rotated, scaled, and translated
    90 degree arc.

    Other Parameters
    ----------------
    quadrant : {0, 1, 2, 3}, default: 0
        Uses 0-based indexing (0, 1, 2, or 3).
    cw : bool, default: True
        If True, the arc vertices are produced clockwise; counter-clockwise
        otherwise.
    radius : float, default: 1
        The radius of the arc.
    center : (float, float), default: (0, 0)
        (x, y) tuple of the arc's center.
    """
    # Note:  It would be possible to use matplotlib's transforms to rotate,
    # scale, and translate the arc, but since the angles are discrete,
    # it's just as easy and maybe more efficient to do it here.
    ARC_CODES = [Path.LINETO,
                 Path.CURVE4,
                 Path.CURVE4,
                 Path.CURVE4,
                 Path.CURVE4,
                 Path.CURVE4,
                 Path.CURVE4]
    # Vertices of a cubic Bezier curve approximating a 90 deg arc
    # These can be determined by Path.arc(0, 90).
    ARC_VERTICES = np.array([[1.00000000e+00, 0.00000000e+00],
                             [1.00000000e+00, 2.65114773e-01],
                             [8.94571235e-01, 5.19642327e-01],
                             [7.07106781e-01, 7.07106781e-01],
                             [5.19642327e-01, 8.94571235e-01],
                             [2.65114773e-01, 1.00000000e+00],
                             # Insignificant
                             # [6.12303177e-17, 1.00000000e+00]])
                             [0.00000000e+00, 1.00000000e+00]])
    if quadrant in (0, 2):
        if cw:
            vertices = ARC_VERTICES
        else:
            vertices = ARC_VERTICES[:, ::-1]  # Swap x and y.
    else:  # 1, 3
        # Negate x.
        if cw:
            # Swap x and y.
            vertices = np.column_stack((-ARC_VERTICES[:, 1],
                                         ARC_VERTICES[:, 0]))
        else:
            vertices = np.column_stack((-ARC_VERTICES[:, 0],
                                         ARC_VERTICES[:, 1]))
    if quadrant > 1:
        radius = -radius  # Rotate 180 deg.
    return list(zip(ARC_CODES, radius * vertices +
                    np.tile(center, (ARC_VERTICES.shape[0], 1))))


# ==================================================
# Line: 332

def _revert(self, path, first_action=Path.LINETO):
    """
    A path is not simply reversible by path[::-1] since the code
    specifies an action to take from the **previous** point.
    """
    reverse_path = []
    next_code = first_action
    for code, position in path[::-1]:
        reverse_path.append((next_code, position))
        next_code = code
    return reverse_path
    # This might be more efficient, but it fails because 'tuple' object
    # doesn't support item assignment:
    # path[1] = path[1][-1:0:-1]
    # path[1][0] = first_action
    # path[2] = path[2][::-1]
    # return path


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_type1font.py
# Occurrences: Lines 72-84 (4 instances)

def is_keyword(self, *names):
    """Is this a name token with one of the names?"""
    return False


# ==================================================
# Line: 380

def _read(self, file):
    """Read the font from a file, decoding into usable parts."""
    rawdata = file.read()
    if not rawdata.startswith(b'\x80'):
        return rawdata

    data = b''
    while rawdata:
        if not rawdata.startswith(b'\x80'):
            raise RuntimeError('Broken pfb file (expected byte 128, '
                               'got %d)' % rawdata[0])
        type = rawdata[1]
        if type in (1, 2):
            length, = struct.unpack('<i', rawdata[2:6])
            segment = rawdata[6:6 + length]
            rawdata = rawdata[6 + length:]

        if type == 1:       # ASCII text: include verbatim
            data += segment
        elif type == 2:     # binary data: encode in hexadecimal
            data += binascii.hexlify(segment)
        elif type == 3:     # end of file
            break
        else:
            raise RuntimeError('Unknown segment type %d in pfb file' % type)

    return data


# ==================================================
# Line: 408

def _split(self, data):
    """
    Split the Type 1 font into its three main parts.

    The three parts are: (1) the cleartext part, which ends in a
    eexec operator; (2) the encrypted part; (3) the fixed part,
    which contains 512 ASCII zeros possibly divided on various
    lines, a cleartomark operator, and possibly something else.
    """

    # Cleartext part: just find the eexec and skip whitespace
    idx = data.index(b'eexec')
    idx += len(b'eexec')
    while data[idx] in b' \t\r\n':
        idx += 1
    len1 = idx

    # Encrypted part: find the cleartomark operator and count
    # zeros backward
    idx = data.rindex(b'cleartomark') - 1
    zeros = 512
    while zeros and data[idx] in b'0' or data[idx] in b'\r\n':
        if data[idx] in b'0':
            zeros -= 1
        idx -= 1
    if zeros:
        # this may have been a problem on old implementations that
        # used the zeros as necessary padding
        _log.info('Insufficiently many zeros in Type 1 font')

    # Convert encrypted part to binary (if we read a pfb file, we may end
    # up converting binary to hexadecimal to binary again; but if we read
    # a pfa file, this part is already in hex, and I am not quite sure if
    # even the pfb format guarantees that it will be in binary).
    idx1 = len1 + ((idx - len1 + 2) & ~1)  # ensure an even number of bytes
    binary = binascii.unhexlify(data[len1:idx1])

    return data[:len1], binary, data[idx+1:]


# ==================================================
# Line: 949

def _postscript_encoding(self, encoding):
    """Return a PostScript encoding array for the encoding."""
    return '\n'.join([
        '/Encoding 256 array\n0 1 255 { 1 index exch /.notdef put} for',
        *(
            f'dup {i} /{glyph} put'
            for i, glyph in sorted(encoding.items())
            if glyph != '.notdef'
        ),
        'readonly def\n',
    ])


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/widgets.py
# Line: 3226

def _init_shape(self, **props):
    return Rectangle((0, 0), 0, 1, visible=False,
                     rotation_point='center', **props)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/font_manager.py
# Line: 1199

def score_style(self, style1, style2):
    """
    Return a match score between *style1* and *style2*.

    An exact match returns 0.0.

    A match between 'italic' and 'oblique' returns 0.1.

    No match returns 1.0.
    """
    if style1 == style2:
        return 0.0
    elif (style1 in ('italic', 'oblique')
          and style2 in ('italic', 'oblique')):
        return 0.1
    return 1.0


# ==================================================
# Line: 1216

def score_variant(self, variant1, variant2):
    """
    Return a match score between *variant1* and *variant2*.

    An exact match returns 0.0, otherwise 1.0.
    """
    if variant1 == variant2:
        return 0.0
    else:
        return 1.0


# ==================================================
# Line: 1227

def score_stretch(self, stretch1, stretch2):
    """
    Return a match score between *stretch1* and *stretch2*.

    The result is the absolute value of the difference between the
    CSS numeric values of *stretch1* and *stretch2*, normalized
    between 0.0 and 1.0.
    """
    try:
        stretchval1 = int(stretch1)
    except ValueError:
        stretchval1 = stretch_dict.get(stretch1, 500)
    try:
        stretchval2 = int(stretch2)
    except ValueError:
        stretchval2 = stretch_dict.get(stretch2, 500)
    return abs(stretchval1 - stretchval2) / 1000.0


# ==================================================
# Line: 1245

def score_weight(self, weight1, weight2):
    """
    Return a match score between *weight1* and *weight2*.

    The result is 0.0 if both weight1 and weight 2 are given as strings
    and have the same value.

    Otherwise, the result is the absolute value of the difference between
    the CSS numeric values of *weight1* and *weight2*, normalized between
    0.05 and 1.0.
    """
    # exact match of the weight names, e.g. weight1 == weight2 == "regular"
    if cbook._str_equal(weight1, weight2):
        return 0.0
    w1 = weight1 if isinstance(weight1, Number) else weight_dict[weight1]
    w2 = weight2 if isinstance(weight2, Number) else weight_dict[weight2]
    return 0.95 * (abs(w1 - w2) / 1000) + 0.05


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/axes/_base.py
# Line: 325

def _setdefaults(self, defaults, kw):
    """
    Add to the dict *kw* the entries in the dict *default* that are absent
    or set to None in *kw*.
    """
    for k in defaults:
        if kw.get(k, None) is None:
            kw[k] = defaults[k]


# ==================================================
# Line: 1228

def _gen_axes_patch(self):
    """
    Returns
    -------
    Patch
        The patch used to draw the background of the Axes.  It is also used
        as the clipping path for any data elements on the Axes.

        In the standard Axes, this is a rectangle, but in other projections
        it may not be.

    Notes
    -----
    Intended to be overridden by new projection types.
    """
    return mpatches.Rectangle((0.0, 0.0), 1.0, 1.0)


# ==================================================
# Line: 3728

def _validate_converted_limits(self, limit, convert):
    """
    Raise ValueError if converted limits are non-finite.

    Note that this function also accepts None as a limit argument.

    Returns
    -------
    The limit value after call to convert(), or None if limit is None.
    """
    if limit is not None:
        converted_limit = convert(limit)
        if isinstance(converted_limit, np.ndarray):
            converted_limit = converted_limit.squeeze()
        if (isinstance(converted_limit, Real)
                and not np.isfinite(converted_limit)):
            raise ValueError("Axis limits cannot be NaN or Inf")
        return converted_limit


# ==================================================
# Line: 4143

def can_zoom(self):
    """
    Return whether this Axes supports the zoom box button functionality.
    """
    return True


# ==================================================
# Line: 4149

def can_pan(self):
    """
    Return whether this Axes supports any pan/zoom button functionality.
    """
    return True


# ==================================================
# Occurrences: Lines 4871-4874 (2 instances)

def get_rasterized(self):
    return True


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/axes/_axes.py
# Line: 7049

def clabel(self, CS, levels=None, **kwargs):
    """
    Label a contour plot.

    Adds labels to line contours in given `.ContourSet`.

    Parameters
    ----------
    CS : `.ContourSet` instance
        Line contours to label.

    levels : array-like, optional
        A list of level values, that should be labeled. The list must be
        a subset of ``CS.levels``. If not given, all levels are labeled.

    **kwargs
        All other parameters are documented in `~.ContourLabeler.clabel`.
    """
    return CS.clabel(levels, **kwargs)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/scale.py
# Line: 95

def limit_range_for_scale(self, vmin, vmax, minpos):
    """
    Return the range *vmin*, *vmax*, restricted to the
    domain supported by this scale (if any).

    *minpos* should be the minimum positive value in the data.
    This is used by log scales to determine a minimum value.
    """
    return vmin, vmax



# ==================================================
# Line: 628

def transform_non_affine(self, values):
    """logistic transform (base 10)"""
    return 1.0 / (1 + 10**(-values))


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/legend_handler.py
# Line: 83

def _default_update_prop(self, legend_handle, orig_handle):
    legend_handle.update_from(orig_handle)


# ==================================================
# Line: 474

def create_collection(self, orig_handle, sizes, offsets, offset_transform):
    return type(orig_handle)(
        orig_handle.get_numsides(),
        rotation=orig_handle.get_rotation(), sizes=sizes,
        offsets=offsets, offset_transform=offset_transform,
    )


# ==================================================
# Line: 710

def _copy_collection_props(self, legend_handle, orig_handle):
    """
    Copy properties from the `.LineCollection` *orig_handle* to the
    `.Line2D` *legend_handle*.
    """
    legend_handle.set_color(orig_handle.get_color()[0])
    legend_handle.set_linestyle(orig_handle.get_linestyle()[0])



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
# Line: 297

def render_rect_filled(self, output: Output,
                       x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Draw a filled rectangle from (*x1*, *y1*) to (*x2*, *y2*).
    """
    output.rects.append((x1, y1, x2, y2))


# ==================================================
# Line: 317

def get_sized_alternatives_for_symbol(self, fontname: str,
                                      sym: str) -> list[tuple[str, str]]:
    """
    Override if your font provides multiple sizes of the same
    symbol.  Should return a list of symbols matching *sym* in
    various sizes.  The expression renderer will select the most
    appropriate size for a given situation from this list.
    """
    return [(fontname, sym)]



# ==================================================
# Line: 361

def _get_offset(self, font: FT2Font, glyph: Glyph, fontsize: float,
                dpi: float) -> float:
    if font.postscript_name == 'Cmex10':
        return (glyph.height / 64 / 2) + (fontsize/3 * dpi/72)
    return 0.


# ==================================================
# Line: 596

def _map_virtual_font(self, fontname: str, font_class: str,
                      uniindex: int) -> tuple[str, int]:
    return fontname, uniindex


# ==================================================
# Line: 1018

def get_kerning(self, next: Node | None) -> float:
    return 0.0


# ==================================================
# Line: 2196

def main(self, toks: ParseResults) -> list[Hlist]:
    return [Hlist(toks.as_list())]


# ==================================================
# Line: 2314

def unknown_symbol(self, s: str, loc: int, toks: ParseResults) -> T.Any:
    raise ParseFatalException(s, loc, f"Unknown symbol: {toks['name']}")


# ==================================================
# Occurrences: Lines 2411-2415 (2 instances)

def group(self, toks: ParseResults) -> T.Any:
    grp = Hlist(toks.get("group", []))
    return [grp]


# ==================================================
# Line: 2424

def unclosed_group(self, s: str, loc: int, toks: ParseResults) -> T.Any:
    raise ParseFatalException(s, len(s), "Expected '}'")


# ==================================================
# Line: 2443

def is_slanted(self, nucleus: Node) -> bool:
    if isinstance(nucleus, Char):
        return nucleus.is_slanted()
    return False


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/text.py
# Line: 669

def _get_dist_to_box(self, rotation, x0, y0, figure_box):
    """
    Return the distance from the given points to the boundaries of a
    rotated box, in pixels.
    """
    if rotation > 270:
        quad = rotation - 270
        h1 = (y0 - figure_box.y0) / math.cos(math.radians(quad))
        h2 = (figure_box.x1 - x0) / math.cos(math.radians(90 - quad))
    elif rotation > 180:
        quad = rotation - 180
        h1 = (x0 - figure_box.x0) / math.cos(math.radians(quad))
        h2 = (y0 - figure_box.y0) / math.cos(math.radians(90 - quad))
    elif rotation > 90:
        quad = rotation - 90
        h1 = (figure_box.y1 - y0) / math.cos(math.radians(quad))
        h2 = (x0 - figure_box.x0) / math.cos(math.radians(90 - quad))
    else:
        h1 = (figure_box.x1 - x0) / math.cos(math.radians(rotation))
        h2 = (figure_box.y1 - y0) / math.cos(math.radians(90 - rotation))

    return min(h1, h2)


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/transforms.py
# Line: 1555

def transform_non_affine(self, values):
    """
    Apply only the non-affine part of this transformation.

    ``transform(values)`` is always equivalent to
    ``transform_affine(transform_non_affine(values))``.

    In non-affine transformations, this is generally equivalent to
    ``transform(values)``.  In affine transformations, this is
    always a no-op.

    Parameters
    ----------
    values : array
        The input values as an array of length
        :attr:`~matplotlib.transforms.Transform.input_dims` or
        shape (N, :attr:`~matplotlib.transforms.Transform.input_dims`).

    Returns
    -------
    array
        The output values as an array of length
        :attr:`~matplotlib.transforms.Transform.output_dims` or shape
        (N, :attr:`~matplotlib.transforms.Transform.output_dims`),
        depending on the input.
    """
    return values


# ==================================================
# Line: 1592

def get_affine(self):
    """Get the affine part of this transform."""
    return IdentityTransform()


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/quiver.py
# Line: 991

def _find_tails(self, mag, rounding=True, half=5, full=10, flag=50):
    """
    Find how many of each of the tail pieces is necessary.

    Parameters
    ----------
    mag : `~numpy.ndarray`
        Vector magnitudes; must be non-negative (and an actual ndarray).
    rounding : bool, default: True
        Whether to round or to truncate to the nearest half-barb.
    half, full, flag : float, defaults: 5, 10, 50
        Increments for a half-barb, a barb, and a flag.

    Returns
    -------
    n_flags, n_barbs : int array
        For each entry in *mag*, the number of flags and barbs.
    half_flag : bool array
        For each entry in *mag*, whether a half-barb is needed.
    empty_flag : bool array
        For each entry in *mag*, whether nothing is drawn.
    """
    # If rounding, round to the nearest multiple of half, the smallest
    # increment
    if rounding:
        mag = half * np.around(mag / half)
    n_flags, mag = divmod(mag, flag)
    n_barb, mag = divmod(mag, full)
    half_flag = mag >= half
    empty_flag = ~(half_flag | (n_flags > 0) | (n_barb > 0))
    return n_flags.astype(int), n_barb.astype(int), half_flag, empty_flag


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
# Line: 1755

def _process_projection_requirements(self, *, axes_class=None, polar=False,
                                     projection=None, **kwargs):
    """
    Handle the args/kwargs to add_axes/add_subplot/gca, returning::

        (axes_proj_class, proj_class_kwargs)

    which can be used for new Axes initialization/identification.
    """
    if axes_class is not None:
        if polar or projection is not None:
            raise ValueError(
                "Cannot combine 'axes_class' and 'projection' or 'polar'")
        projection_class = axes_class
    else:

        if polar:
            if projection is not None and projection != 'polar':
                raise ValueError(
                    f"polar={polar}, yet projection={projection!r}. "
                    "Only one of these arguments should be supplied."
                )
            projection = 'polar'

        if isinstance(projection, str) or projection is None:
            projection_class = projections.get_projection_class(projection)
        elif hasattr(projection, '_as_mpl_axes'):
            projection_class, extra_kwargs = projection._as_mpl_axes()
            kwargs.update(**extra_kwargs)
        else:
            raise TypeError(
                f"projection must be a string, None or implement a "
                f"_as_mpl_axes method, not {projection!r}")
    return projection_class, kwargs


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/animation.py
# Line: 181

def _supports_transparency(self):
    """
    Whether this writer supports transparency.

    Writers may consult output file type and codec to determine this at runtime.
    """
    return False


# ==================================================
# Line: 355

def _args(self):
    """Assemble list of encoder-specific command-line arguments."""
    return NotImplementedError("args needs to be implemented by subclass.")


# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_afm.py
# Line: 393

def get_char_index(self, c):  # For consistency with FT2Font.
    """
    Return the glyph index corresponding to a character code point.

    Note, for AFM fonts, we treat the glyph index the same as the codepoint.
    """
    return c


# ==================================================
