# long-lambda-expression snippets for matplotlib

# File: /root/ecooptimizer/matplotlib/lib/matplotlib/axes/_base.py
# Line: 1484

self._type_check = lambda artist: (
    (not valid_types or isinstance(artist, valid_types)) and
    (not invalid_types or not isinstance(artist, invalid_types))
)

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/axes/_axes.py
# Line: 2916

lambda r, b=bar:
    mtransforms.Bbox.intersection(
        b.get_window_extent(r), b.get_clip_box()
    ) or mtransforms.Bbox.null()

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/transforms.py
# Line: 74

return lambda self: (
    type(self).__name__ + "("
    + ",".join([*(indent("\n" + strrepr(getattr(self, arg)))
                  for arg in args),
                *(indent("\n" + k + "=" + strrepr(getattr(self, arg)))
                  for k, arg in kwargs.items())])
    + ")")

# ==================================================
