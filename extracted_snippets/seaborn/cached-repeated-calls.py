# cached-repeated-calls snippets for seaborn

# File: /root/ecooptimizer/seaborn/seaborn/_base.py
# Occurrences: Lines 260-261 (2 instances)

levels = list(sorted(palette))

# ==================================================
# Occurrences: Lines 503-506 (2 instances)

norm(levels)

# ==================================================
# Occurrences: Lines 919-919 (2 instances)

levels[axis] = converter.convert_units(levels[axis])

# ==================================================
# Occurrences: Lines 926-926 (2 instances)

levels[axis] = transform(converter.convert_units(levels[axis]))

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/regression.py
# Occurrences: Lines 58-62 (2 instances)

vals = [getattr(self, var) for var in vars]

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/utils.py
# Line: 85

color = desaturate(color, saturation)

# ==================================================
# Line: 128

color = to_rgb(scout.get_facecolor())

# ==================================================
# Occurrences: Lines 137-142 (2 instances)

facecolor = scout.get_facecolor()

# ==================================================
# Occurrences: Lines 363-363 (2 instances)

newticks = newticks.compress(newticks >= firsttick)

# ==================================================
# Occurrences: Lines 375-375 (2 instances)

newticks = newticks.compress(newticks >= firsttick)

# ==================================================
# Occurrences: Lines 624-627 (2 instances)

df["Date"] = pd.to_datetime(df["Date"])

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/external/appdirs.py
# Line: 114

path = os.path.join(path, appname)

# ==================================================
# Occurrences: Lines 120-124 (2 instances)

path = os.path.join(path, appname)

# ==================================================
# Line: 189

buf = ctypes.create_unicode_buffer(1024)

# ==================================================
# Line: 200

buf2 = ctypes.create_unicode_buffer(1024)

# ==================================================
# Occurrences: Lines 212-215 (2 instances)

buf = array.zeros('c', buf_size)

# ==================================================
# Occurrences: Lines 225-228 (2 instances)

buf = array.zeros('c', buf_size)

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/external/docscrape.py
# Line: 220

section = self._doc.read_to_next_empty_line()

# ==================================================
# Line: 226

section += self._doc.read_to_next_empty_line()

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/external/kde.py
# Line: 255

energy = sum(diff * diff, axis=0) / 2.0

# ==================================================
# Line: 261

energy = sum(diff * diff, axis=0) / 2.0

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_stats/order.py
# Occurrences: Lines 66-70 (2 instances)

values = data[var].dropna()

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/palettes.py
# Occurrences: Lines 177-182 (2 instances)

n_colors = len(palette)

# ==================================================
# Occurrences: Lines 212-213 (2 instances)

_, color = palette.split(":")

# ==================================================
# Occurrences: Lines 220-221 (2 instances)

_, color = palette.split(":")

# ==================================================
# Line: 228

_, colors = palette.split(":")

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/categorical.py
# Occurrences: Lines 828-834 (6 instances)

center = pos_data[self.orient].item()

# ==================================================
# Occurrences: Lines 886-886 (2 instances)

pos = np.full(len(vals), inv_ori(pos_data[self.orient].item()))

# ==================================================
# Line: 968

norm_keys = [vars_to_key(violin["sub_vars"]) for violin in violin_data]

# ==================================================
# Line: 1010

norm_key = vars_to_key(violin["sub_vars"])

# ==================================================
# Occurrences: Lines 1091-1091 (2 instances)

pos_pts = np.stack([inv_pos(pos0), inv_pos(pos1)])

# ==================================================
# Occurrences: Lines 1108-1108 (2 instances)

pos_pts = np.stack([inv_pos(pos0), inv_pos(pos1)])

# ==================================================
# Line: 2887

plot_kws = kwargs.copy()

# ==================================================
# Line: 2903

plot_kws = kwargs.copy()

# ==================================================
# Occurrences: Lines 2920-2927 (5 instances)

plot_kws = kwargs.copy()

# ==================================================
# Occurrences: Lines 2945-2947 (3 instances)

plot_kws = kwargs.copy()

# ==================================================
# Occurrences: Lines 2970-2972 (3 instances)

linewidth = plot_kws.pop("linewidth", None)

# ==================================================
# Occurrences: Lines 2993-2997 (5 instances)

plot_kws = kwargs.copy()

# ==================================================
# Line: 3010

linecolor = p._complement_color(linecolor, color, p._hue_map)

# ==================================================
# Line: 3033

aggregator = agg_cls(estimator, errorbar, n_boot=n_boot, seed=seed)

# ==================================================
# Line: 3067

aggregator = agg_cls(estimator, errorbar, n_boot=n_boot, seed=seed)

# ==================================================
# Occurrences: Lines 3075-3076 (2 instances)

gap = kwargs.pop("gap", 0)

# ==================================================
# Occurrences: Lines 3104-3105 (2 instances)

gap = kwargs.pop("gap", 0)

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/plot.py
# Occurrences: Lines 1203-1207 (4 instances)

title_text = ax.set_title(title)

# ==================================================
# Occurrences: Lines 1541-1548 (8 instances)

out_df = data.frames[(x, y)].copy()

# ==================================================
# Occurrences: Lines 1606-1606 (3 instances)

axes_df_inf_as_nan = axes_df.copy()

# ==================================================
# Occurrences: Lines 1632-1632 (3 instances)

yield subplot_keys, axes_df.copy(), view["ax"]

# ==================================================
# Occurrences: Lines 1785-1789 (6 instances)

axis_obj = getattr(ax, f"{axis}axis")

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/scales.py
# Occurrences: Lines 447-448 (2 instances)

a = forward(vmin)

# ==================================================
# Occurrences: Lines 906-907 (2 instances)

self.major = mpl.axis.Ticker()

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/matrix.py
# Occurrences: Lines 121-123 (2 instances)

xticklabels = _index_to_ticklabels(data.columns)

# ==================================================
# Occurrences: Lines 130-132 (2 instances)

yticklabels = _index_to_ticklabels(data.index)

# ==================================================
# Line: 141

self.xticklabels = _index_to_ticklabels(data.columns)

# ==================================================
# Line: 151

self.yticklabels = _index_to_ticklabels(data.index)

# ==================================================
# Line: 512

self.ylabel = _index_to_label(self.data.index)

# ==================================================
# Line: 520

self.xlabel = _index_to_label(self.data.index)

# ==================================================
# Occurrences: Lines 891-893 (2 instances)

subtract = standardized.min()

# ==================================================
# Occurrences: Lines 1097-1102 (2 instances)

ytl = self.ax_heatmap.get_yticklabels()

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/widgets.py
# Occurrences: Lines 102-106 (2 instances)

colors = color_palette(name, 256, desat)

# ==================================================
# Occurrences: Lines 121-125 (2 instances)

colors = color_palette(name, 256, desat)

# ==================================================
# Line: 135

pal[:] = color_palette(name, n, desat)

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/distributions.py
# Line: 175

kws.setdefault("facecolor", to_rgba(color, alpha))

# ==================================================
# Occurrences: Lines 188-190 (2 instances)

kws["edgecolor"] = to_rgba(color, alpha)

# ==================================================
# Occurrences: Lines 486-489 (5 instances)

ax = self._get_axes(sub_vars)

# ==================================================
# Line: 554

ax = self._get_axes(sub_vars)

# ==================================================
# Line: 679

ax = self._get_axes(sub_vars)

# ==================================================
# Occurrences: Lines 722-724 (2 instances)

default_y = estimator.stat.capitalize()

# ==================================================
# Occurrences: Lines 826-826 (2 instances)

cmap = self._cmap_from_color(color)

# ==================================================
# Occurrences: Lines 833-833 (2 instances)

cmap = self._cmap_from_color(color)

# ==================================================
# Line: 1089

ax = self._get_axes(sub_vars)

# ==================================================
# Line: 1135

cmap = self._cmap_from_color(color)

# ==================================================
# Occurrences: Lines 1153-1157 (2 instances)

contour_kws["cmap"] = self._cmap_from_color(color)

# ==================================================
# Line: 2172

hist_kws = kwargs.copy()

# ==================================================
# Line: 2202

kde_kws = kwargs.copy()

# ==================================================
# Line: 2227

ecdf_kws = kwargs.copy()

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/axisgrid.py
# Line: 419

ncol = 1 if col is None else len(col_names)

# ==================================================
# Line: 429

nrow = int(np.ceil(len(col_names) / col_wrap))

# ==================================================
# Line: 480

n_axes = len(col_names)

# ==================================================
# Occurrences: Lines 919-924 (4 instances)

curr_ticks = ax.get_xticks()

# ==================================================
# Occurrences: Lines 1020-1030 (3 instances)

title = template.format(**args)

# ==================================================
# Line: 1621

kwargs = kwargs.copy()

# ==================================================
# Line: 1635

kws = kwargs.copy()

# ==================================================
# Line: 2107

diag_kws = {} if diag_kws is None else diag_kws.copy()

# ==================================================
# Line: 2146

diag_kws = diag_kws.copy()

# ==================================================
# Line: 2203

marginal_kws = {} if marginal_kws is None else marginal_kws.copy()

# ==================================================
# Occurrences: Lines 2280-2281 (2 instances)

marg_x_kws = marginal_kws.copy()

# ==================================================
