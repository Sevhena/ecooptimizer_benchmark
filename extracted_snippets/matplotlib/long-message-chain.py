# long-message-chain snippets for matplotlib

# File: /root/ecooptimizer/matplotlib/lib/mpl_toolkits/axisartist/axis_artist.py
# Line: 267

bbox = super().get_window_extent(renderer).frozen()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/collections.py
# Line: 1657

transforms.Affine2D(x).rotate(-self._rotation).get_matrix()

# ==================================================
# Line: 2135

m = ax.transData.get_affine().get_matrix().copy()

# ==================================================
# Line: 2377

return super().get_edgecolor().reshape(-1, 4)

# ==================================================
# Line: 2383

return super().get_facecolor().reshape(-1, 4)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_agg.py
# Line: 266

return np.asarray(self._renderer).take([3, 0, 1, 2], axis=2).tobytes()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_cairo.py
# Line: 127

+ Affine2D().scale(1, -1).translate(0, self.height))

# ==================================================
# Line: 142

Affine2D().scale(dpi, -dpi).translate(0, dpi),

# ==================================================
# Line: 176

+ Affine2D().scale(1, -1).translate(0, self.height))

# ==================================================
# Line: 364

+ Affine2D().scale(1, -1).translate(0, self.renderer.height))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_wx.py
# Line: 201

Affine2D().scale(1.0, -1.0).translate(0.0, self.height)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/qt_editor/_formlayout.py
# Line: 463

icon = QtWidgets.QWidget().style().standardIcon(
    QtWidgets.QStyle.SP_MessageBoxQuestion)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_gtk4.py
# Line: 108

self.get_display().get_default_seat().get_pointer())

# ==================================================
# Line: 193

self.get_display().get_default_seat().get_pointer())

# ==================================================
# Line: 212

self.get_display().get_default_seat().get_pointer())

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_pdf.py
# Line: 337

obj.decode('latin-1').translate(_str_escapes).encode('latin-1')

# ==================================================
# Line: 2319

mytrans = Affine2D().rotate_deg(angle).translate(x, y)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_gtk3.py
# Line: 115

window.get_display().get_device_manager().get_client_pointer())

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_qt.py
# Line: 738

if self.palette().color(self.backgroundRole()).value() < 128:

# ==================================================
# Line: 925

QtGui.QFontMetrics(text.document().defaultFont())
.size(0, text.toPlainText()).height() + 20)

# ==================================================
# Line: 1062

QtWidgets.QApplication.instance().clipboard().setPixmap(pixmap)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_svg.py
# Line: 492

return transform + Affine2D().scale(1, -1).translate(0, self.height)

# ==================================================
# Line: 528

Affine2D()
.scale(HATCH_SIZE).scale(1.0, -1.0).translate(0, HATCH_SIZE),

# ==================================================
# Line: 998

Affine2D()
.translate(x, y)
.scale(1.0, -1.0)
.translate(0.0, self.height))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/image.py
# Occurrences: Lines 406-421 (3 instances)

t0 = Affine2D().translate(0, -A.shape[0]).scale(1, -1)

# ==================================================
# Line: 1083

np.ascontiguousarray(A).view(np.uint32).ravel()[

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/contour.py
# Line: 328

pos = self.get_transform().inverted().transform(screen_pos)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/artist.py
# Line: 1649

names = [self.aliased_name_rest(prop, target)
         .replace('_base._AxesBase', 'Axes')
         .replace('_axes.Axes', 'Axes')

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/patches.py
# Line: 837

+ transforms.Affine2D() \
.translate(-rotation_point[0], -rotation_point[1]) \
.scale(1, self._aspect_ratio_correction) \
.rotate_deg(self.angle) \
.scale(1, 1 / self._aspect_ratio_correction) \
.translate(*rotation_point)

# ==================================================
# Line: 1007

return self._patch_transform.clear() \
    .scale(self.radius) \
    .rotate(self.orientation) \
    .translate(*self.xy)

# ==================================================
# Line: 1412

transforms.Affine2D()
.scale(np.hypot(self._dx, self._dy), self._width)
.rotate(np.arctan2(self._dy, self._dx))
.translate(self._x, self._y)
.frozen())

# ==================================================
# Line: 1675

self._patch_transform = transforms.Affine2D() \
    .scale(width * 0.5, height * 0.5 * self._aspect_ratio_correction) \
    .rotate_deg(self.angle) \
    .scale(1, 1 / self._aspect_ratio_correction) \
    .translate(*center)

# ==================================================
# Line: 1958

return transforms.Affine2D() \
    .scale(*self._convert_xy_units((a, b))) \
    .rotate_deg(self.angle) \
    .translate(*self._convert_xy_units(self.center)) \
    .transform(verts)

# ==================================================
# Line: 2503

trans = Affine2D().scale(a, b).translate(x0 + width / 2,
                                         y0 + height / 2)

# ==================================================
# Line: 4491

return self.get_transform().inverted().transform_path(_path)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/textpath.py
# Line: 366

tr = (Affine2D()
      .scale(self._size / text_to_path.FONT_SCALE)
      .translate(*self._xy))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/offsetbox.py
# Line: 1018

return self.get_child().get_bbox(renderer).padded(pad)

# ==================================================
# Line: 1612

ann.xyann = ann.get_transform().inverted().transform(
    (self.ox + dx, self.oy + dy))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backend_bases.py
# Occurrences: Lines 555-563 (2 instances)

transform = (Affine2D()
             .scale(fontsize / text2path.FONT_SCALE)
             .rotate_deg(angle)
             .translate(x, height - y))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/markers.py
# Line: 481

self._transform = Affine2D().scale(0.5).rotate_deg(rotation)

# ==================================================
# Line: 501

Affine2D()
.translate(-bbox.xmin + 0.5 * -bbox.width, -bbox.ymin + 0.5 * -bbox.height)
.scale(1.0 / max_dim))

# ==================================================
# Line: 548

self._transform = Affine2D().scale(0.5).rotate_deg(rot)

# ==================================================
# Line: 608

self._transform = Affine2D().translate(-0.5, -0.5).rotate_deg(45)

# ==================================================
# Line: 695

self._transform = Affine2D().scale(0.5).rotate_deg(30)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_text_helpers.py
# Line: 25

f"({chr(codepoint).encode('ascii', 'namereplace').decode('ascii')}) "

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/spines.py
# Line: 131

self._patch_transform = mtransforms.Affine2D() \
    .scale(width * 0.5, height * 0.5) \
    .translate(*center)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/cbook.py
# Line: 1094

inputs = [np.ma.array(k, mask=mask, dtype=float).filled(np.nan).ravel()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/colors.py
# Line: 2198

transform = mpl.transforms.Affine2D().translate(-0.5, -0.5)\
                        .scale(self.N / (s[1] - 1), self.N / (s[0] - 1))

# ==================================================
# Line: 2844

value = (self._trf
         .inverted()
         .transform(rescaled)
         .reshape(np.shape(value)))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/projections/polar.py
# Line: 170

affine = mtransforms.Affine2D() \
    .scale(0.5 / yscale) \
    .translate(0.5, 0.5)

# ==================================================
# Occurrences: Lines 340-342 (2 instances)

trans = mtransforms.Affine2D().scale(1, 1).rotate(angle)

# ==================================================
# Occurrences: Lines 350-352 (2 instances)

trans = mtransforms.Affine2D().scale(1, 1).rotate(angle)

# ==================================================
# Line: 628

trans = mtransforms.Affine2D().scale(-1, 1).rotate(tick_angle)

# ==================================================
# Line: 660

trans = mtransforms.Affine2D().scale(-1, 1).rotate(tick_angle)

# ==================================================
# Line: 900

flipr_transform = mtransforms.Affine2D() \
    .translate(0.0, -0.5) \
    .scale(1.0, -1.0) \
    .translate(0.0, 0.5)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/projections/geo.py
# Line: 74

Affine2D() \
.scale(1, self._longitude_cap * 2) \
.translate(0, -self._longitude_cap)

# ==================================================
# Line: 90

yaxis_stretch = Affine2D().scale(np.pi * 2, 1).translate(-np.pi, 0)

# ==================================================
# Line: 112

return Affine2D() \
    .scale(0.5 / xscale, 0.5 / yscale) \
    .translate(0.5, 0.5)

# ==================================================
# Line: 195

self._xaxis_pretransform \
    .clear() \
    .scale(1.0, self._longitude_cap * 2.0) \
    .translate(0.0, -self._longitude_cap)

# ==================================================
# Line: 509

return Affine2D() \
    .scale(0.25) \
    .translate(0.5, 0.5)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/sphinxext/figmpl_directive.py
# Line: 145

rel = relpath(docsource, srctop).replace('.', '').replace(os.sep, '-')

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_type1font.py
# Line: 735

float(x) for x in (self.prop['FontMatrix']
                   .lstrip('[').rstrip(']').split())

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/widgets.py
# Line: 3463

return Affine2D().translate(-self.center[0], -self.center[1]) \
        .scale(1, aspect_ratio) \
        .rotate(self._rotation) \
        .scale(1, 1 / aspect_ratio) \
        .translate(*self.center)

# ==================================================
# Line: 3896

t = (transforms.Affine2D()
     .translate(-old_bbox.x0, -old_bbox.y0)
     .scale(1 / old_bbox.width, 1 / old_bbox.height)
     .scale(w1, h1)
     .translate(x1, y1))

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/font_manager.py
# Occurrences: Lines 371-374 (4 instances)

sfnt2 = (sfnt.get((*mac_key, 2), b'').decode('latin-1').lower() or

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/text.py
# Line: 60

x_box, y_box = Affine2D().rotate(theta).transform((xt_box, yt_box))

# ==================================================
# Line: 286

return self.get_transform().transform_angles(
    [self._rotation], [self.get_unitless_position()]).item(0)

# ==================================================
# Line: 590

Affine2D()
.rotate_deg(self.get_rotation())
.translate(posx + x_box, posy + y_box))

# ==================================================
# Line: 1497

return Affine2D().scale(scale).translate(x, y)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/transforms.py
# Line: 636

corners_rotated = Affine2D().rotate(radians).transform(corners)

# ==================================================
# Line: 2036

return self.translate(-x, -y).rotate(theta).translate(x, y)

# ==================================================
# Line: 2048

return self.translate(-x, -y).rotate_deg(degrees).translate(x, y)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/pyplot.py
# Line: 1269

figlegend.__doc__ = Figure.legend.__doc__ \
    .replace(" legend(", " figlegend(") \
    .replace("fig.legend(", "plt.figlegend(") \
    .replace("ax.plot(", "plt.plot(")

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/quiver.py
# Line: 1161

poly_verts = transforms.Affine2D().rotate(-angle).transform(
    poly_verts)

# ==================================================
