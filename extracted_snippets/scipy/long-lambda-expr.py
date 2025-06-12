# long-lambda-expr snippets for scipy

# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_eigen/arpack/arpack.py
# Line: 509

self.OP = lambda x: Minv_matvec(matvec(x)
                                + sigma * M_matvec(x))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/csgraph/_laplacian.py
# Line: 392

lambda v: v * d[:, np.newaxis]
- m @ v
- np.transpose(np.conjugate(np.transpose(np.conjugate(v)) @ m))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_precompute/wright_bessel_data.py
# Line: 35

res = mp.nsum(lambda k: x**k / mp.fac(k)
              * rgamma_cached(a * k + b, dps=dps),

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_orthogonal.py
# Line: 2041

wfunc=lambda x: 1.0 / sqrt(1 - x * x / 4.0),

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_continuous_distns.py
# Line: 1067

lambda a, b: np.prod([(a+i-1)/(b-i) for i in range(1, int(n)+1)], axis=0),

# ==================================================
# Occurrences: Lines 1190-1192 (2 instances)

lambda x_, c_, d_: c_ * d_ * (x_**(c_*d_-1)) / (1 + x_**c_),

# ==================================================
# Occurrences: Lines 1198-1202 (2 instances)

lambda x_, c_, d_: (np.log(c_) + np.log(d_) + sc.xlogy(c_*d_ - 1, x_)
                    - (d_+1) * sc.log1p(x_**(c_))),

# ==================================================
# Occurrences: Lines 1233-1239 (2 instances)

lambda e1, e2, e3, mu2_if_c: ((e3 - 3*e2*e1 + 2*e1**3)
                               / np.sqrt((mu2_if_c)**3)),

# ==================================================
# Line: 1480

lambda absx: (-_LOG_PI - (2*np.log(absx) + np.log1p((1/absx)**2))))

# ==================================================
# Occurrences: Lines 2589-2596 (2 instances)

lambda v1, v2, v2_2, v2_4:
2 * v2 * v2 * (v1 + v2_2) / (v1 * v2_2**2 * v2_4),

# ==================================================
# Line: 3122

lambda c: -np.log(c) + sc.psi(c + 1) + _EULER + 1,

# ==================================================
# Line: 3219

lambda xi: 1 / (1 - xi)**2 / (1 - 2 * xi),

# ==================================================
# Line: 3225

lambda xi: 2 * (1 + xi) * np.sqrt(1 - 2*xi) / (1 - 3*xi),

# ==================================================
# Line: 3231

lambda xi: 3 * (1 - 2*xi) * (2*xi**2 + xi + 3) 
           / (1 - 3*xi) / (1 - 4*xi) - 3,

# ==================================================
# Line: 3862

lambda x, c: (np.log(abs(c)) + sc.xlogy(c*a - 1, x) - x**c - sc.gammaln(a)),

# ==================================================
# Line: 4947

lambda x: 1. / (x - 1.)**2 / (x - 2.),

# ==================================================
# Occurrences: Lines 4953-4957 (2 instances)

lambda x: 4. * np.sqrt(x - 2.) / (x - 3.),

# ==================================================
# Line: 5217

lambda x, p, b: (p - 1)*np.log(x) - b*(x + 1/x)/2,

# ==================================================
# Line: 6640

lambda x, c: np.exp(c*x - sc.gammaln(c+1)),

# ==================================================
# Line: 6649

lambda g, q, c: (np.log(q) + sc.gammaln(c+1))/c,

# ==================================================
# Line: 6656

lambda x, c: -np.expm1(c*x - sc.gammaln(c+1)),

# ==================================================
# Line: 6665

lambda g, q, c: (np.log1p(-q) + sc.gammaln(c+1))/c,

# ==================================================
# Line: 6796

lambda x, s: (-np.log(x)**2 / (2 * s**2)
              - np.log(s * x * np.sqrt(2 * np.pi))),

# ==================================================
# Line: 9505

lambda x, mu: (-(1 - mu*x)**2.0 / (2*x*mu**2.0)
               - 0.5*np.log(2*np.pi*x)),

# ==================================================
# Line: 9701

lambda x, a: 2.*_norm_pdf(x)*_norm_cdf(a*x))

# ==================================================
# Line: 9707

lambda x, a: np.log(2)+_norm_logpdf(x)+_norm_logcdf(a*x))

# ==================================================
# Occurrences: Lines 9946-9949 (3 instances)

[lambda x, c, d: x**2 / c / (d-c+1),

# ==================================================
# Line: 9979

lambda d: np.expm1((n+2) * np.log(d)) / (d-1.0),

# ==================================================
# Line: 10053

lambda x, c: (x*x - 2*x + c) / (c-1),

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_discrete_distns.py
# Line: 873

lambda k, M, n, r:
    (-betaln(k+1, r) + betaln(k+r, 1)
     - betaln(n-k+1, M-r-n+1) + betaln(M-r-k+1, 1)
     + betaln(n+1, M-n+1) - betaln(M+1, 1)),

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_distribution_infrastructure.py
# Occurrences: Lines 1946-1947 (2 instances)

h=lambda u: np.sign(u) * np.abs(u)**(1 / other),

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_sampling.py
# Line: 219

"center": lambda a: 0.25 * (math.sqrt(a * a + 8.0) - a),

# ==================================================
# Occurrences: Lines 254-260 (4 instances)

"center": lambda a, b: (2 ** (1 / b) - 1) ** (-1 / a),

# ==================================================
# Occurrences: Lines 338-342 (2 instances)

"pdf": lambda x: math.exp(-x) / (1 + math.exp(-x)) ** 2,

# ==================================================
# Line: 364

"pdf": lambda x, df: (1 + x * x / df) ** (-0.5 * (df + 1)),

# ==================================================
