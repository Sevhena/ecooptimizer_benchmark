# use-a-generator snippets for scipy

# File: /root/ecooptimizer/scipy/scipy/ndimage/_interpolation.py
# Line: 974

if not all([float(ax).is_integer() for ax in axes]):

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/signal/_signaltools.py
# Line: 1400

if any([_numeric_arrays([x], kinds='ui', xp=xp) for x in [volume, kernel]]):

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_mptestutils.py
# Line: 212

self.is_complex = any(
    [isinstance(arg, ComplexArg) for arg in self.arg_spec]
)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/_decomp_cossin.py
# Line: 171

cplx = any([np.iscomplexobj(x) for x in [x11, x12, x21, x22]])

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/pyprima/pyprima/src/pyprima/common/selectx.py
# Occurrences: Lines 197-198 (2 instances)

assert not any([isbetter(ffilt_i, cfilt_i, f, cstrv, ctol) for ffilt_i, cfilt_i in zip(ffilt[:nfilt], cfilt[:nfilt])])

# ==================================================
# Line: 294

assert not any([isbetter(fhisti, chisti, fhist[kopt], chist[kopt], ctol) for fhisti, chisti in zip(fhist[:nhist], chist[:nhist])])

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_distn_infrastructure.py
# Line: 979

ok = all([bcdim == 1 or bcdim == szdim
          for (bcdim, szdim) in zip(bcast_shape, size_)])

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_rbf.py
# Line: 238

if not all([x.size == self.di.shape[0] for x in self.xi]):

# ==================================================
# Line: 282

if not all([x.shape == y.shape for x in args for y in args]):

# ==================================================
