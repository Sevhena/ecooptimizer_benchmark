# long-message-chain snippets for scipy

# File: /root/ecooptimizer/scipy/scipy/sparse/_base.py
# Line: 247

return self.tocsr().astype(
    dtype, casting=casting, copy=copy).asformat(self.format)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_norm.py
# Occurrences: Lines 153-159 (4 instances)

return abs(x).sum(axis=row_axis).max()

# ==================================================
# Line: 181

M = sqrt(abs(x).power(2).sum(axis=a))

# ==================================================
# Line: 187

M = np.power(abs(x).power(ord).sum(axis=a), 1 / ord)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_bsr.py
# Line: 424

col = ((C * self.indices).astype(idx_dtype, copy=False)
       .repeat(R*C).reshape(-1,R,C))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_lil.py
# Line: 390

return self.tocsr(copy=copy).transpose(axes=axes, copy=False).tolil(copy=False)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_precompute/wright_bessel.py
# Line: 35

term = expression.diff(a, n).subs(a, 0).simplify().doit()

# ==================================================
# Line: 98

term = expression.diff(a, n).subs(a, 0).simplify().doit()

# ==================================================
# Line: 110

pg_part = (pg_part.series(b, 0, n=order+1-n)
           .removeO()
           .subs(polygamma(2, 1), -2*zeta(3))
           .simplify()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_mptestutils.py
# Line: 159

v1 = Arg(self.a, self.b).values(max(1 + n//2, n-5)).astype(int)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_generate_pyx.py
# Line: 600

self.doc.replace("\\", "\\\\").replace('"', '\\"')
.replace('\n', '\\n\"\n    "')

# ==================================================
# Line: 636

var_name = c_name.replace('[', '_').replace(']', '_').replace(' ', '_')

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/_solvers.py
# Line: 525

x = solve_triangular(ul.conj().T,
                     solve_triangular(uu.conj().T,
                                      u10.conj().T,
                                      lower=True),
                     unit_diagonal=True,
                     ).conj().T.dot(up.conj().T)

# ==================================================
# Line: 735

x = solve_triangular(ul.conj().T,
                     solve_triangular(uu.conj().T,
                                      u10.conj().T,
                                      lower=True),
                     unit_diagonal=True,
                     ).conj().T.dot(up.conj().T)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_mstats_basic.py
# Occurrences: Lines 1667-1668 (2 instances)

x = ma.asarray(x).compressed().view(ndarray)

# ==================================================
# Line: 3540

ranked = ranked.compressed().reshape(k,-1).view(ndarray)

# ==================================================
# Occurrences: Lines 3612-3613 (2 instances)

x = ma.asarray(x).compressed().view(ndarray)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_continuous_distns.py
# Line: 12480

pairs = list(globals().copy().items())

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_censored_data.py
# Line: 26

if np.isinf(interval).all(axis=1).any():

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_discrete_distns.py
# Line: 2095

pairs = list(globals().copy().items())

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_levy_stable/__init__.py
# Line: 887

super()
.pdf(_x, _alpha, _beta, loc=_delta, scale=gamma)
.reshape(len(_x), 1)

# ==================================================
# Line: 1034

super()
.cdf(_x, _alpha, _beta, loc=_delta, scale=gamma)
.reshape(len(_x), 1)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/arff/_arffread.py
# Line: 327

date_str = data_str.strip().strip("'").strip('"')

# ==================================================
