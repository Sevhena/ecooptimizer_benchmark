# cached-repeated-calls snippets for matplotlib

# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/axis_artist.py
# Line: 476

pad = max(w for w, h, d in whd_list)

# ==================================================
# Line: 482

pad = max(w for w, h, d in whd_list)

# ==================================================
# Line: 488

pad = max(h for w, h, d in whd_list)

# ==================================================
# Occurrences: Lines 494-499 (3 instances)

max_ascent = max(h - d for w, h, d in whd_list)

# ==================================================
# Occurrences: Lines 505-506 (2 instances)

max_ascent = max(h - d for w, h, d in whd_list)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/angle_helper.py
# Line: 112

n = len(levs)

# ==================================================
# Line: 124

n = len(levs)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/mplot3d/axis3d.py
# Occurrences: Lines 281-282 (2 instances)

means_z0 = np.zeros(3)

# ==================================================
# Occurrences: Lines 465-467 (4 instances)

x1, y1, z1 = proj3d.proj_transform(*pos, self.axes.M)

# ==================================================
# Occurrences: Lines 474-474 (2 instances)

lx, ly, lz = proj3d.proj_transform(*pos, self.axes.M)

# ==================================================
# Occurrences: Lines 593-594 (2 instances)

pep = proj3d._proj_trans_points([edgep1, edgep2], self.axes.M)

# ==================================================
# Occurrences: Lines 621-622 (2 instances)

pep = proj3d._proj_trans_points([edgep1, edgep2], self.axes.M)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/mplot3d/art3d.py
# Occurrences: Lines 583-587 (3 instances)

mask = _viewlim_mask(*zip(*s), self.axes)

# ==================================================
# Occurrences: Lines 645-649 (3 instances)

mask = _viewlim_mask(*zip(*s), self.axes)

# ==================================================
# Line: 1035

PathCollection.set_offsets(self, np.ma.column_stack((vxs, vys)))

# ==================================================
# Line: 1043

self._offset_zordered = np.ma.column_stack((vxs, vys))

# ==================================================
# Occurrences: Lines 1624-1625 (2 instances)

v1 = np.empty((len(polygons), 3))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/mplot3d/axes3d.py
# Occurrences: Lines 132-138 (3 instances)

self.xy_viewLim = Bbox.unit()

# ==================================================
# Line: 2427

rii = np.array([], dtype=int)

# ==================================================
# Line: 2437

cii = np.array([], dtype=int)

# ==================================================
# Line: 4154

nk = np.linalg.norm(k)

# ==================================================
# Line: 4163

k = k / np.linalg.norm(k)  # unit vector normal to r1-r2

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/mplot3d/proj3d.py
# Occurrences: Lines 103-104 (2 instances)

Mr = np.eye(4)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axes_grid1/axes_rgb.py
# Line: 41

ax1 = axes_class(ax.get_figure(), ax.get_position(original=True),

# ==================================================
# Line: 55

fig = ax.get_figure()

# ==================================================
# Occurrences: Lines 147-151 (3 instances)

R = np.zeros_like(RGB)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backend_tools.py
# Occurrences: Lines 476-477 (2 instances)

self.views[figure] = cbook._Stack()

# ==================================================
# Occurrences: Lines 695-700 (2 instances)

if (time.time()-self.lastscroll) < self.scrollthresh:

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/lines.py
# Occurrences: Lines 416-417 (2 instances)

self._xorig = np.asarray([])

# ==================================================
# Line: 775

gc = renderer.new_gc()

# ==================================================
# Line: 813

gc = renderer.new_gc()

# ==================================================
# Occurrences: Lines 845-849 (2 instances)

tpath, affine = (self._get_transformed_path()
                 .get_transformed_points_and_affine())

# ==================================================
# Line: 862

snap = renderer.points_to_pixels(self._markersize) >= snap

# ==================================================
# Line: 868

w = renderer.points_to_pixels(self._markersize)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/table.py
# Occurrences: Lines 133-137 (2 instances)

required = self.get_required_width(renderer)

# ==================================================
# Line: 741

rows = len(cellColours)

# ==================================================
# Line: 768

if len(cellColours) != rows:

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/collections.py
# Occurrences: Lines 270-275 (2 instances)

return transforms.Bbox.null()

# ==================================================
# Occurrences: Lines 311-314 (2 instances)

bbox = transforms.Bbox.null()

# ==================================================
# Occurrences: Lines 327-331 (2 instances)

paths = self.get_paths()

# ==================================================
# Occurrences: Lines 388-390 (3 instances)

trans = self.get_transforms()

# ==================================================
# Occurrences: Lines 433-435 (4 instances)

gc, transform.frozen(), [],

# ==================================================
# Occurrences: Lines 460-469 (6 instances)

renderer.draw_path_collection(gc, transform.frozen(), ipaths,

# ==================================================
# Occurrences: Lines 476-494 (9 instances)

transform = transform.frozen()

# ==================================================
# Line: 500

transform = transform.frozen()

# ==================================================
# Occurrences: Lines 771-773 (4 instances)

if len(dashes) != len(linewidths):

# ==================================================
# Occurrences: Lines 854-855 (2 instances)

if isinstance(c, str) and c.lower() in ("none", "face"):

# ==================================================
# Occurrences: Lines 908-909 (2 instances)

if isinstance(c, str) and c.lower() in ("none", "face"):

# ==================================================
# Line: 1200

hasarray = self.get_array() is not None

# ==================================================
# Occurrences: Lines 1213-1216 (2 instances)

u = np.unique(self.get_array())

# ==================================================
# Occurrences: Lines 1234-1236 (2 instances)

arr = self.get_array()

# ==================================================
# Occurrences: Lines 2665-2669 (2 instances)

prev_unmask = self._get_unmasked_polys()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/__init__.py
# Occurrences: Lines 757-761 (2 instances)

val = self._get(key)

# ==================================================
# Occurrences: Lines 1495-1498 (6 instances)

v[k1] = _replacer(data, v1)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/registry.py
# Line: 352

self._backend_to_gui_framework.get(backend))

# ==================================================
# Line: 361

gui = self._backend_to_gui_framework.get(backend)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_gtk3agg.py
# Occurrences: Lines 37-39 (4 instances)

x = int(bbox.x0)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/_backend_tk.py
# Line: 149

self._timer = self.parent.after(self._interval, self._on_timer)

# ==================================================
# Line: 156

lambda: self.parent.after(self._interval, self._on_timer)

# ==================================================
# Occurrences: Lines 208-210 (2 instances)

self = weakself()

# ==================================================
# Occurrences: Lines 220-222 (2 instances)

self = weakself()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/qt_compat.py
# Line: 77

_to_int = operator.attrgetter('value')

# ==================================================
# Line: 83

_to_int = operator.attrgetter('value')

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_wx.py
# Occurrences: Lines 656-661 (2 instances)

size = self.GetMinSize()

# ==================================================
# Line: 1098

fg = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT)

# ==================================================
# Line: 1116

fg = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/qt_editor/_formlayout.py
# Occurrences: Lines 301-301 (2 instances)

field = QtWidgets.QLineEdit(repr(value), self)

# ==================================================
# Occurrences: Lines 315-315 (2 instances)

field = QtWidgets.QLineEdit(repr(value), self)

# ==================================================
# Occurrences: Lines 329-329 (2 instances)

value = str(field.text())

# ==================================================
# Occurrences: Lines 341-341 (2 instances)

value = float(str(field.text()))

# ==================================================
# Occurrences: Lines 355-355 (2 instances)

value = literal_eval(str(field.text()))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/qt_editor/figureoptions.py
# Occurrences: Lines 190-192 (6 instances)

general = data.pop(0)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_gtk4.py
# Line: 346

label = Gtk.Label()

# ==================================================
# Line: 352

self.message = Gtk.Label()

# ==================================================
# Line: 366

ff = Gtk.FileFilter()

# ==================================================
# Line: 376

ff = Gtk.FileFilter()

# ==================================================
# Line: 440

label = Gtk.Label()

# ==================================================
# Line: 446

self._message = Gtk.Label()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_ps.py
# Line: 1144

width, height = self.figure.get_size_inches()

# ==================================================
# Line: 1198

self.figure.get_size_inches())

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_pdf.py
# Line: 682

self._object_seq = itertools.count(1)  # consumed by reserveObject

# ==================================================
# Line: 722

self._internal_font_seq = (Name(f'F{i}') for i in itertools.count(1))

# ==================================================
# Occurrences: Lines 728-737 (4 instances)

self._alpha_state_seq = (Name(f'A{i}') for i in itertools.count(1))

# ==================================================
# Line: 1178

fontdescObject = self.reserveObject('font descriptor')

# ==================================================
# Line: 1227

gind = font.get_char_index(ccode)

# ==================================================
# Occurrences: Lines 1244-1246 (2 instances)

rawcharprocs = _get_pdf_charprocs(filename, glyph_ids)

# ==================================================
# Line: 1262

charprocObject = self.reserveObject('charProc')

# ==================================================
# Line: 1268

name = self._get_xobject_glyph_name(filename, charname)

# ==================================================
# Line: 1283

fontdescObject = self.reserveObject('font descriptor')

# ==================================================
# Line: 1343

gind = font.get_char_index(ccode)

# ==================================================
# Occurrences: Lines 1390-1391 (2 instances)

rawcharprocs = _get_pdf_charprocs(filename, glyph_ids)

# ==================================================
# Occurrences: Lines 1403-1406 (2 instances)

charprocObject = self.reserveObject('charProc')

# ==================================================
# Line: 1786

png_data, bit_depth, palette = self._writePng(img)

# ==================================================
# Line: 1796

png_data, _, _ = self._writePng(img)

# ==================================================
# Occurrences: Lines 2627-2627 (2 instances)

theirs = getattr(other, p)

# ==================================================
# Occurrences: Lines 2651-2654 (4 instances)

theirs = [getattr(other, p) for p in params]

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_gtk3.py
# Occurrences: Lines 334-336 (2 instances)

toolitem = Gtk.ToolItem()

# ==================================================
# Occurrences: Lines 342-344 (2 instances)

toolitem = Gtk.ToolItem()

# ==================================================
# Line: 372

name = dialog.get_filter().get_name()

# ==================================================
# Occurrences: Lines 381-383 (2 instances)

response = dialog.run()

# ==================================================
# Line: 398

dialog.run()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_pgf.py
# Line: 517

strokeopacity = gc.get_rgb()[3]

# ==================================================
# Line: 530

stroke_rgba = gc.get_rgb()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_svg.py
# Line: 420

mid = ensure_metadata(mid)

# ==================================================
# Occurrences: Lines 426-428 (2 instances)

info = metadata.pop(key, None)

# ==================================================
# Line: 434

agents = metadata.pop(key, None)

# ==================================================
# Line: 443

mid = ensure_metadata(mid)

# ==================================================
# Line: 458

mid = ensure_metadata(mid)

# ==================================================
# Line: 567

attrib['fill-opacity'] = _short_float_fmt(rgbFace[3])

# ==================================================
# Line: 576

attrib['fill-opacity'] = _short_float_fmt(rgbFace[3])

# ==================================================
# Occurrences: Lines 595-596 (2 instances)

if gc.get_joinstyle() != 'round':

# ==================================================
# Occurrences: Lines 1133-1136 (4 instances)

if prop.get_style() != 'normal':

# ==================================================
# Occurrences: Lines 1168-1170 (3 instances)

if prop.get_stretch() != 'normal':

# ==================================================
# Occurrences: Lines 1196-1203 (2 instances)

attrib['style'] = _generate_css({**font_style, **color_style})

# ==================================================
# Occurrences: Lines 1216-1219 (2 instances)

style=_generate_css({**font_style, **color_style}),

# ==================================================
# Line: 1240

style = _generate_css({**font_style, **color_style})

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/ticker.py
# Line: 671

axis_inv_trf = axis_trf.inverted()

# ==================================================
# Line: 677

axis_inv_trf = axis_trf.inverted()

# ==================================================
# Occurrences: Lines 984-989 (2 instances)

math.floor(math.log(vmax, b))

# ==================================================
# Line: 1103

exponent = round(fx) if is_x_decade else np.floor(fx)

# ==================================================
# Line: 1112

fx = round(fx)

# ==================================================
# Line: 1522

pow10 = np.clip(pow10, min(self.ENG_PREFIXES), max(self.ENG_PREFIXES))

# ==================================================
# Line: 1529

and pow10 < max(self.ENG_PREFIXES)):

# ==================================================
# Line: 2441

return np.array([])  # no minor or major ticks

# ==================================================
# Line: 2519

ticklocs = np.array([])

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_constrained_layout.py
# Line: 178

layoutgrids = make_layoutgrids_gs(layoutgrids, gs)

# ==================================================
# Line: 196

layoutgrids = make_layoutgrids_gs(layoutgrids, gs)

# ==================================================
# Occurrences: Lines 270-273 (4 instances)

if ax.get_subplotspec() is None:

# ==================================================
# Line: 366

gs = ss.get_gridspec()

# ==================================================
# Occurrences: Lines 377-381 (5 instances)

if not ax.get_subplotspec() or not ax.get_in_layout():

# ==================================================
# Occurrences: Lines 550-550 (2 instances)

ss2 = ax2.get_subplotspec()

# ==================================================
# Occurrences: Lines 580-580 (2 instances)

ss2 = ax2.get_subplotspec()

# ==================================================
# Occurrences: Lines 668-673 (4 instances)

if ax.get_subplotspec() is None or not ax.get_in_layout():

# ==================================================
# Line: 743

pbcb = pbcb.translated(dx, 0)

# ==================================================
# Line: 749

pbcb = pbcb.translated(dx, 0)

# ==================================================
# Line: 757

pbcb = pbcb.translated(0, dy)

# ==================================================
# Line: 763

pbcb = pbcb.translated(0, dy)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/image.py
# Line: 496

alpha = self.get_alpha()

# ==================================================
# Line: 509

alpha = self.get_alpha()

# ==================================================
# Line: 1084

np.add.outer(y_int * A.shape[1], x_int)]

# ==================================================
# Line: 1092

idx_int = np.add.outer(y_int * A.shape[1], x_int)

# ==================================================
# Occurrences: Lines 1484-1486 (2 instances)

bbox_in = self.get_window_extent(renderer).frozen()

# ==================================================
# Line: 1537

parsed = parse.urlparse(fname)

# ==================================================
# Line: 1559

if isinstance(fname, str) and len(parse.urlparse(fname).scheme) > 1:

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/contour.py
# Occurrences: Lines 1378-1382 (2 instances)

self.zmin = z.min().astype(float)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/artist.py
# Occurrences: Lines 1449-1452 (2 instances)

and callable(getattr(self.o, name))]

# ==================================================
# Occurrences: Lines 1610-1615 (2 instances)

accepts = self.get_valid_values(prop)

# ==================================================
# Line: 1634

accepts = self.get_valid_values(prop)

# ==================================================
# Line: 1653

accepts = [self.get_valid_values(prop)

# ==================================================
# Occurrences: Lines 1679-1683 (2 instances)

if name.startswith('get_') and callable(getattr(o, name))]

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/patches.py
# Occurrences: Lines 1195-1197 (2 instances)

if self._closed == bool(closed):

# ==================================================
# Line: 3810

path_out, path_in = split_bezier_intersecting_with_closedpath(
    arrow_path, in_f)

# ==================================================
# Line: 3824

path_out, path_in = split_bezier_intersecting_with_closedpath(
    arrow_path, in_f)

# ==================================================
# Line: 3842

path_in, path_out = split_bezier_intersecting_with_closedpath(
    arrow_path, in_f)

# ==================================================
# Line: 4661

fig = self.get_figure(root=False)

# ==================================================
# Line: 4692

bb = self.get_figure(root=False).figbbox

# ==================================================
# Line: 4698

bb = self.get_figure(root=False).bbox

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backend_managers.py
# Occurrences: Lines 56-57 (2 instances)

self.keypresslock = widgets.LockDraw()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/rcsetup.py
# Occurrences: Lines 441-444 (2 instances)

s = s.lower()

# ==================================================
# Line: 856

norm_prop = _prop_aliases.get(prop, prop)

# ==================================================
# Line: 871

norm_prop = _prop_aliases.get(prop, prop)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/stackplot.py
# Line: 106

first_line = -np.sum(y, 0) * 0.5

# ==================================================
# Line: 116

total = np.sum(y, 0)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/path.py
# Line: 1006

codes = np.full(length, cls.CURVE4, dtype=cls.code_type)

# ==================================================
# Line: 1015

codes = np.full(length, cls.CURVE4, dtype=cls.code_type)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/colorbar.py
# Line: 763

self, cs, erase = params.values()

# ==================================================
# Line: 774

self, levels, colors, linewidths, erase = params.values()

# ==================================================
# Line: 839

locator = ticker.FixedLocator(b, nbins=10)

# ==================================================
# Line: 851

locator = ticker.FixedLocator(b, nbins=10)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/mlab.py
# Occurrences: Lines 268-274 (4 instances)

if len(x) < NFFT:

# ==================================================
# Line: 359

t = np.arange(NFFT/2, len(x) - NFFT/2 + 1, NFFT - noverlap)/Fs

# ==================================================
# Occurrences: Lines 385-387 (2 instances)

pad_to = len(x)

# ==================================================
# Line: 898

tdiff = np.dot(self.inv_cov, diff)

# ==================================================
# Line: 905

tdiff = np.dot(self.inv_cov, diff)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/offsetbox.py
# Line: 119

offsets_ = np.cumsum([0] + [w + sep for w in widths])

# ==================================================
# Line: 134

offsets_ = np.cumsum([0] + [w + sep for w in widths])

# ==================================================
# Occurrences: Lines 622-623 (2 instances)

self.offset_transform = mtransforms.Affine2D()

# ==================================================
# Occurrences: Lines 740-741 (2 instances)

self.offset_transform = mtransforms.Affine2D()

# ==================================================
# Occurrences: Lines 844-847 (2 instances)

self.offset_transform = mtransforms.Affine2D()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backend_bases.py
# Line: 2021

canvas = canvas_class(self.figure)

# ==================================================
# Line: 2032

canvas = canvas_class(self.figure)

# ==================================================
# Occurrences: Lines 2459-2462 (4 instances)

and None not in [_get_uniform_gridstate(ax.xaxis.minorTicks),

# ==================================================
# Occurrences: Lines 2478-2481 (4 instances)

and None not in [_get_uniform_gridstate(ax.xaxis.majorTicks),

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/tri/_trirefine.py
# Occurrences: Lines 216-217 (2 instances)

refi_x = np.zeros(refi_npts)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/tri/_triinterpolate.py
# Line: 851

DOF_rot = np.zeros([n, 9, 9], dtype=np.float64)

# ==================================================
# Line: 864

K = np.zeros([n, 9, 9], dtype=np.float64)

# ==================================================
# Occurrences: Lines 1092-1093 (2 instances)

dfx_el_w = np.empty_like(el_geom_w)

# ==================================================
# Line: 1324

x = np.zeros(n)

# ==================================================
# Occurrences: Lines 1331-1333 (2 instances)

p = np.zeros(n)

# ==================================================
# Line: 1344

rho = np.dot(r, w)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_layoutgrid.py
# Occurrences: Lines 64-65 (2 instances)

self.artists = np.empty((nrows, ncols), dtype=object)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/streamplot.py
# Line: 193

t = integrate(xg, yg, broken_streamlines,
              integration_max_step_scale,
              integration_max_error_scale)

# ==================================================
# Line: 223

t = integrate(xg, yg, broken_streamlines, integration_max_step_scale,
              integration_max_error_scale)

# ==================================================
# Occurrences: Lines 244-247 (4 instances)

points = np.transpose([tx, ty]).reshape(-1, 1, 2)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/axis.py
# Occurrences: Lines 778-785 (2 instances)

old_default_lims = (self.get_major_locator()
                    .nonsingular(-np.inf, np.inf))

# ==================================================
# Line: 1210

old0, old1 = self.get_view_interval()

# ==================================================
# Line: 1219

old0, old1 = self.get_view_interval()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/inset.py
# Occurrences: Lines 181-181 (2 instances)

xyB=xy_data, coordsB=self.rectangle.get_data_transform(),

# ==================================================
# Occurrences: Lines 192-192 (2 instances)

existing.coords2 = self.rectangle.get_data_transform()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/cbook.py
# Occurrences: Lines 806-807 (2 instances)

self._ordering[x] = len(self._ordering)

# ==================================================
# Line: 1182

M = len(data)

# ==================================================
# Line: 1201

N = len(data)

# ==================================================
# Occurrences: Lines 1278-1288 (8 instances)

if len(wiskhi) == 0 or np.max(wiskhi) < q3:

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/dviread.py
# Occurrences: Lines 748-763 (18 instances)

packet_char = self._read_arg(1)

# ==================================================
# Occurrences: Lines 1030-1032 (4 instances)

effects["slant"] = float(next(words))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/dates.py
# Occurrences: Lines 398-399 (2 instances)

return np.asarray(d)

# ==================================================
# Line: 436

d = np.asarray(d)

# ==================================================
# Line: 448

d = np.asarray(d)

# ==================================================
# Occurrences: Lines 1034-1040 (4 instances)

args, kwargs = normalize_args(args, kwargs)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/colors.py
# Occurrences: Lines 532-534 (2 instances)

rgba = np.array([to_rgba(cc) for cc in c])

# ==================================================
# Line: 1426

or len(colormaps) == 1 \

# ==================================================
# Line: 1440

self.n_variates = len(colormaps)

# ==================================================
# Line: 2825

t_vmin, t_vmax = self._trf.transform([self.vmin, self.vmax])

# ==================================================
# Line: 2838

t_vmin, t_vmax = self._trf.transform([self.vmin, self.vmax])

# ==================================================
# Occurrences: Lines 3319-3321 (3 instances)

r = np.empty_like(h)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/projections/polar.py
# Occurrences: Lines 301-304 (2 instances)

self._text1_translate = mtransforms.ScaledTranslation(
    0, 0, axes.get_figure(root=False).dpi_scale_trans)

# ==================================================
# Occurrences: Lines 340-342 (2 instances)

trans = mtransforms.Affine2D().scale(1, 1).rotate(angle)

# ==================================================
# Occurrences: Lines 350-352 (2 instances)

trans = mtransforms.Affine2D().scale(1, 1).rotate(angle)

# ==================================================
# Occurrences: Lines 603-605 (2 instances)

tick_angle = np.deg2rad(angle)

# ==================================================
# Occurrences: Lines 624-628 (3 instances)

trans = mtransforms.Affine2D().rotate(tick_angle)

# ==================================================
# Occurrences: Lines 639-641 (2 instances)

tick_angle = np.deg2rad(angle)

# ==================================================
# Occurrences: Lines 656-660 (3 instances)

trans = mtransforms.Affine2D().rotate(tick_angle)

# ==================================================
# Line: 1484

(startt, startr), (t, r) = p.trans_inverse.transform(
    [(p.x, p.y), (x, y)])

# ==================================================
# Line: 1500

(startt, startr), (t, r) = p.trans_inverse.transform(
    [(p.x, p.y), (x, y)])

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/projections/geo.py
# Occurrences: Lines 369-372 (2 instances)

delta, large_delta = d(theta)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/sankey.py
# Occurrences: Lines 625-626 (2 instances)

tips = np.zeros((n, 2))

# ==================================================
# Occurrences: Lines 634-640 (2 instances)

tips[i, :], label_locations[i, :] = self._add_output(
    urpath, angle, *spec)

# ==================================================
# Line: 659

tip, label_location = self._add_input(llpath, angle, *spec)

# ==================================================
# Line: 674

tips[i, :], label_locations[i, :] = self._add_output(
    urpath, angle, *spec)

# ==================================================
# Occurrences: Lines 702-704 (3 instances)

tips = rotate(tips)

# ==================================================
# Occurrences: Lines 711-716 (3 instances)

tips = rotate(tips)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/sphinxext/plot_directive.py
# Line: 519

pwd = os.getcwd()

# ==================================================
# Line: 536

sys, argv=[code_path], path=[os.getcwd(), *sys.path]), \

# ==================================================
# Line: 778

output_base = os.path.basename(source_file_name)

# ==================================================
# Line: 784

base, ext = os.path.splitext(os.path.basename(source_file_name))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_type1font.py
# Occurrences: Lines 213-214 (4 instances)

next_binary = (yield _WhitespaceToken(pos, match.group()))

# ==================================================
# Occurrences: Lines 229-232 (6 instances)

pos = match.end()

# ==================================================
# Occurrences: Lines 261-264 (4 instances)

raw = match.group()

# ==================================================
# Occurrences: Lines 272-272 (2 instances)

pos = match.end()

# ==================================================
# Occurrences: Lines 512-512 (2 instances)

token = next(source)

# ==================================================
# Occurrences: Lines 519-519 (2 instances)

key = token.value()

# ==================================================
# Occurrences: Lines 536-536 (2 instances)

token = next(source)

# ==================================================
# Occurrences: Lines 549-549 (2 instances)

value = token.value()

# ==================================================
# Occurrences: Lines 598-601 (2 instances)

cs[key] = self._decrypt(value, 'charstring', ndiscard)

# ==================================================
# Line: 609

count_token = next(tokens)

# ==================================================
# Occurrences: Lines 619-619 (2 instances)

index_token = next(tokens)

# ==================================================
# Occurrences: Lines 625-625 (2 instances)

nbytes_token = next(tokens)

# ==================================================
# Occurrences: Lines 631-631 (2 instances)

token = next(tokens)

# ==================================================
# Occurrences: Lines 640-643 (2 instances)

return array, next(tokens).endpos()

# ==================================================
# Occurrences: Lines 658-658 (2 instances)

nbytes_token = next(tokens)

# ==================================================
# Occurrences: Lines 664-664 (2 instances)

token = next(tokens)

# ==================================================
# Occurrences: Lines 686-686 (2 instances)

index_token = next(tokens)

# ==================================================
# Occurrences: Lines 692-692 (2 instances)

name_token = next(tokens)

# ==================================================
# Occurrences: Lines 738-741 (2 instances)

oldmatrix = np.eye(3, 3)

# ==================================================
# Occurrences: Lines 827-831 (3 instances)

len0 = len(self.parts[0])

# ==================================================
# Occurrences: Lines 863-864 (2 instances)

sorted(characters),

# ==================================================
# Occurrences: Lines 908-911 (4 instances)

byte2 = next(data)

# ==================================================
# Occurrences: Lines 917-917 (2 instances)

byte1 = next(data)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/widgets.py
# Occurrences: Lines 1380-1382 (2 instances)

bb_text = self.text_disp.get_window_extent()

# ==================================================
# Line: 1417

if self.cursor_index != len(text):

# ==================================================
# Line: 1425

self.cursor_index = len(text)

# ==================================================
# Line: 1751

self.value_selected = self.labels[index].get_text()

# ==================================================
# Line: 1768

self._observers.process('clicked', self.labels[index].get_text())

# ==================================================
# Occurrences: Lines 3991-3999 (3 instances)

self._xys[idx] = self._get_data_coords(event)

# ==================================================
# Line: 4021

self._xys[-1] = self._get_data_coords(event)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/font_manager.py
# Line: 1406

cprop = prop.copy()

# ==================================================
# Line: 1432

cprop = prop.copy()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/axes/_base.py
# Occurrences: Lines 2000-2009 (4 instances)

pb = position.frozen()

# ==================================================
# Line: 2018

position = pb1.anchored(self.get_anchor(), pb)

# ==================================================
# Line: 2426

elif any(line_trf.contains_branch_seperately(self.transData)):

# ==================================================
# Line: 2449

updatex, updatey = line_trf.contains_branch_seperately(self.transData)

# ==================================================
# Line: 3107

x, _ = title.get_position()

# ==================================================
# Occurrences: Lines 3132-3135 (2 instances)

ymax = max(title.get_position()[1] for title in titles)

# ==================================================
# Line: 4414

dx, dy = format_deltas(key, dx, dy)

# ==================================================
# Line: 4420

dx, dy = format_deltas(key, dx, dy)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/axes/_axes.py
# Line: 2219

return convert(dx)

# ==================================================
# Line: 2252

dx = convert(dx)

# ==================================================
# Occurrences: Lines 2528-2531 (2 instances)

error_message = str(e)

# ==================================================
# Occurrences: Lines 3426-3430 (2 instances)

locs = np.arange(len(heads))

# ==================================================
# Occurrences: Lines 4869-4876 (4 instances)

locator = axis.get_major_locator()

# ==================================================
# Line: 7293

nx = len(x)  # number of datasets

# ==================================================
# Line: 7324

len_xi = len(xi)

# ==================================================
# Line: 7348

if len(xi):

# ==================================================
# Line: 7359

if not input_empty and len(x) > 1:

# ==================================================
# Line: 7388

tops = (tops / np.diff(bins)) / tops[-1].sum()

# ==================================================
# Line: 7394

tops = (tops * np.diff(bins))[:, slc].cumsum(axis=1)[:, slc]

# ==================================================
# Line: 7402

totwidth = np.diff(bins)

# ==================================================
# Occurrences: Lines 7455-7456 (2 instances)

x = np.zeros(4 * len(bins) - 3)

# ==================================================
# Line: 8639

Z = np.asarray(Z)

# ==================================================
# Line: 8663

Z = np.asarray(Z)

# ==================================================
# Occurrences: Lines 9098-9114 (8 instances)

perp_lines = functools.partial(self.hlines, colors=linecolor,
                                capstyle='projecting')

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/legend.py
# Occurrences: Lines 84-89 (2 instances)

bbox = self.legend.get_bbox_to_anchor()

# ==================================================
# Line: 656

if loc.split()[0] == 'outside':

# ==================================================
# Line: 663

locs = loc.split()

# ==================================================
# Occurrences: Lines 725-729 (2 instances)

self.get_bbox_to_anchor(),

# ==================================================
# Line: 1151

start_time = time.perf_counter()

# ==================================================
# Line: 1178

if self._loc_used_default and time.perf_counter() - start_time > 1:

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/bezier.py
# Line: 364

begin_inside = inside(ctl_points[-2:])  # true if begin point is inside

# ==================================================
# Line: 374

if inside(ctl_points[-2:]) != begin_inside:

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/legend_handler.py
# Line: 587

coll = mcoll.LineCollection(verts)

# ==================================================
# Line: 605

coll = mcoll.LineCollection(verts)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_mathtext.py
# Occurrences: Lines 573-576 (2 instances)

font = findfont(prop)

# ==================================================
# Line: 1583

char = char_class(sym, state)

# ==================================================
# Line: 1589

char = char_class(sym, state)

# ==================================================
# Occurrences: Lines 1671-1674 (6 instances)

cur_g = round(clamp(box.glue_set * cur_glue))

# ==================================================
# Occurrences: Lines 1727-1730 (6 instances)

cur_g = round(clamp(box.glue_set * cur_glue))

# ==================================================
# Line: 2285

prev_char = next((c for c in s[:loc][::-1] if c != ' '), '')

# ==================================================
# Line: 2299

prev_char = next((c for c in s[:loc][::-1] if c != ' '), '')

# ==================================================
# Occurrences: Lines 2407-2408 (2 instances)

if toks.get("font"):

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/text.py
# Occurrences: Lines 273-277 (2 instances)

bb = self.get_window_extent()

# ==================================================
# Line: 425

M = Affine2D().rotate_deg(self.get_rotation())

# ==================================================
# Line: 459

angle = self.get_rotation()

# ==================================================
# Occurrences: Lines 736-736 (4 instances)

line = ' '.join(sub_words[:i])

# ==================================================
# Occurrences: Lines 748-748 (4 instances)

wrapped_lines.append(' '.join(sub_words[:i]))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/transforms.py
# Occurrences: Lines 1081-1082 (2 instances)

if np.any(self._points != other.get_points()):

# ==================================================
# Occurrences: Lines 2275-2277 (2 instances)

self._affine = self._x.get_affine()

# ==================================================
# Occurrences: Lines 2328-2330 (2 instances)

self._mtx = self._x.get_matrix()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/pyplot.py
# Line: 395

current_framework = cbook._get_running_interactive_framework()

# ==================================================
# Line: 430

current_framework = cbook._get_running_interactive_framework()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/quiver.py
# Occurrences: Lines 456-462 (4 instances)

U, V = np.atleast_1d(*args)

# ==================================================
# Occurrences: Lines 537-539 (2 instances)

if pivot.lower() == 'mid':

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/figure.py
# Line: 1743

im = ax._gci()

# ==================================================
# Line: 1750

im = ax._gci()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/animation.py
# Occurrences: Lines 57-60 (8 instances)

if int(np.nextafter(x, np.inf)*dpi) % n == 0:

# ==================================================
# Line: 295

wo, ho = self.fig.get_size_inches()

# ==================================================
# Line: 302

w, h = self.fig.get_size_inches()

# ==================================================
# Occurrences: Lines 1682-1687 (2 instances)

self._save_count = len(frames)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_afm.py
# Line: 246

line = next(fh)

# ==================================================
# Line: 256

next(fh)  # EndKernData

# ==================================================
