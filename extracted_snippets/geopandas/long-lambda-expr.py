# long-lambda-expr snippets for geopandas

# File: /root/ecooptimizer/geopandas/geopandas/base.py
# Line: 6499

lambda x: (
    points_from_xy(
        *sample_function(x, size=size, **kwargs).T
    ).union_all()
    if not (x.is_empty or x is None or "Polygon" not in x.geom_type)
    else MultiPoint()
),

# ==================================================
