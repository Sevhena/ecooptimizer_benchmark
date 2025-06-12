# long-message-chain snippets for seaborn

# File: /root/ecooptimizer/seaborn/seaborn/regression.py
# Line: 289

yhat = model(_y, _x, **kwargs).fit().predict(grid)

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_marks/line.py
# Line: 257

data = data.groupby(orient).agg(**agg).reset_index()

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_marks/area.py
# Line: 169

data = data.groupby(orient).agg(**agg).reset_index()

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_stats/aggregation.py
# Line: 47

groupby
.agg(data, {var: self.func})
.dropna(subset=[var])
.reset_index(drop=True)

# ==================================================
# Line: 114

groupby
.apply(data, self._process, var, engine)
.dropna(subset=[var])
.reset_index(drop=True)

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_stats/counting.py
# Line: 40

groupby
.agg(data.assign(**{var: data[orient]}), {var: len})
.dropna(subset=["x", "y"])
.reset_index(drop=True)

# ==================================================
# Line: 125

vals = vals.replace(-np.inf, np.nan).replace(np.inf, np.nan).dropna()

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/categorical.py
# Line: 1217

sub_data
.groupby(self.orient)
.apply(aggregator, agg_var, **groupby_apply_include_groups(False))
.reindex(pd.Index(positions, name=self.orient))
.reset_index()

# ==================================================
# Line: 1288

sub_data
.groupby(self.orient)
.apply(aggregator, agg_var, **groupby_apply_include_groups(False))
.reset_index()

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/plot.py
# Line: 1503

df
.drop(coord_cols, axis=1)
.reindex(df.columns, axis=1)  # So unscaled columns retain their place
.copy(deep=False)

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/moves.py
# Line: 131

return w.shift(1).fillna(0).cumsum() + (w - w.sum()) / 2

# ==================================================
# Line: 143

data
.drop("width", axis=1)
.merge(groups, on=grouping_vars, how="left")
.drop(orient, axis=1)
.rename(columns={"_dodged": orient})

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/_core/groupby.py
# Line: 95

data
.groupby(grouper, sort=False, observed=False)
.agg(*args, **kwargs)
.reindex(groups)
.reset_index()
.pipe(self._reorder_columns, data)

# ==================================================
# File: /root/ecooptimizer/seaborn/seaborn/distributions.py
# Line: 1060

min_variance = observations.var().fillna(0).min()

# ==================================================
