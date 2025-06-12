# no-self-use snippets for scipy

# File: /root/ecooptimizer/scipy/scipy/sparse/_base.py
# Line: 991

def __rdiv__(self, other):
    # Implementing this as the inverse would be too magical -- bail out
    return NotImplemented


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_index.py
# Line: 313

def _asindices(self, idx, length):
    """Convert `idx` to a valid index for an axis with a given length.

    Subclasses that need special validation can override this method.
    """
    try:
        x = np.asarray(idx)
    except (ValueError, TypeError, MemoryError) as e:
        raise IndexError('invalid index') from e

    if x.ndim not in (1, 2):
        raise IndexError('Index dimension must be 1 or 2')

    if x.size == 0:
        return x

    # Check bounds
    max_indx = x.max()
    if max_indx >= length:
        raise IndexError(f'index ({max_indx}) out of range')

    min_indx = x.min()
    if min_indx < 0:
        if min_indx < -length:
            raise IndexError(f'index ({min_indx}) out of range')
        if x is idx or not x.flags.owndata:
            x = x.copy()
        x[x < 0] += length
    return x


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_build_utils/tempita/_looper.py
# Line: 142

def _compare_group(self, item, other, getter):
    if getter is None:
        return item != other
    elif (isinstance(getter, basestring_)
          and getter.startswith('.')):
        getter = getter[1:]
        if getter.endswith('()'):
            getter = getter[:-2]
            return getattr(item, getter)() != getattr(other, getter)()
        else:
            return getattr(item, getter) != getattr(other, getter)
    elif hasattr(getter, '__call__'):
        return getter(item) != getter(other)
    else:
        return item[getter] != other[getter]

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/signal/_ltisys.py
# Line: 1356

def _check_binop_other(self, other):
    return isinstance(other, StateSpace | np.ndarray | float | complex |
                              np.number | int)


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_mptestutils.py
# Line: 39

def _positive_values(self, a, b, n):
    if a < 0:
        raise ValueError("a should be positive")

    # Try to put half of the points into a linspace between a and
    # 10 the other half in a logspace.
    if n % 2 == 0:
        nlogpts = n//2
        nlinpts = nlogpts
    else:
        nlogpts = n//2
        nlinpts = nlogpts + 1

    if a >= 10:
        # Outside of linspace range; just return a logspace.
        pts = np.logspace(np.log10(a), np.log10(b), n)
    elif a > 0 and b < 10:
        # Outside of logspace range; just return a linspace
        pts = np.linspace(a, b, n)
    elif a > 0:
        # Linspace between a and 10 and a logspace between 10 and
        # b.
        linpts = np.linspace(a, 10, nlinpts, endpoint=False)
        logpts = np.logspace(1, np.log10(b), nlogpts)
        pts = np.hstack((linpts, logpts))
    elif a == 0 and b <= 10:
        # Linspace between 0 and b and a logspace between 0 and
        # the smallest positive point of the linspace
        linpts = np.linspace(0, b, nlinpts)
        if linpts.size > 1:
            right = np.log10(linpts[1])
        else:
            right = -30
        logpts = np.logspace(-30, right, nlogpts, endpoint=False)
        pts = np.hstack((logpts, linpts))
    else:
        # Linspace between 0 and 10, logspace between 0 and the
        # smallest positive point of the linspace, and a logspace
        # between 10 and b.
        if nlogpts % 2 == 0:
            nlogpts1 = nlogpts//2
            nlogpts2 = nlogpts1
        else:
            nlogpts1 = nlogpts//2
            nlogpts2 = nlogpts1 + 1
        linpts = np.linspace(0, 10, nlinpts, endpoint=False)
        if linpts.size > 1:
            right = np.log10(linpts[1])
        else:
            right = -30
        logpts1 = np.logspace(-30, right, nlogpts1, endpoint=False)
        logpts2 = np.logspace(1, np.log10(b), nlogpts2)
        pts = np.hstack((logpts1, linpts, logpts2))

    return np.sort(pts)


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/_testutils.py
# Line: 160

def get_optional_args(self, func):
    # get optional arguments with its default value,
    # used for testing keywords
    signature = inspect.signature(func)
    optional_args = {}
    for k, v in signature.parameters.items():
        if v.default is not inspect.Parameter.empty:
            optional_args[k] = v.default
    return optional_args


# ==================================================
# Line: 179

def get_dtype(self, dtype_list, dtype_idx):
    # get the dtype from dtype_list via index
    # if the index is out of range, then return the last dtype
    if dtype_idx > len(dtype_list)-1:
        return dtype_list[-1]
    else:
        return dtype_list[dtype_idx]


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/_docscrape.py
# Line: 188

def _strip(self, doc):
    i = 0
    j = 0
    for i, line in enumerate(doc):
        if line.strip():
            break

    for j, line in enumerate(doc[::-1]):
        if line.strip():
            break

    return doc[i : len(doc) - j]


# ==================================================
# Line: 224

def _parse_param_list(self, content, single_element_is_type=False):
    content = dedent_lines(content)
    r = Reader(content)
    params = []
    while not r.eof():
        header = r.read().strip()
        if " : " in header:
            arg_name, arg_type = header.split(" : ", maxsplit=1)
        else:
            # NOTE: param line with single element should never have a
            # a " :" before the description line, so this should probably
            # warn.
            if header.endswith(" :"):
                header = header[:-2]
            if single_element_is_type:
                arg_name, arg_type = "", header
            else:
                arg_name, arg_type = header, ""

        desc = r.read_to_next_unindented_line()
        desc = dedent_lines(desc)
        desc = strip_blank_lines(desc)

        params.append(Parameter(arg_name, arg_type, desc))

    return params


# ==================================================
# Line: 346

def _parse_index(self, section, content):
    """
    .. index:: default
       :refguide: something, else, and more

    """

    def strip_each_in(lst):
        return [s.strip() for s in lst]

    out = {}
    section = section.split("::")
    if len(section) > 1:
        out["default"] = strip_each_in(section[1].split(","))[0]
    for line in content:
        line = line.split(":")
        if len(line) > 2:
            out[line[1]] = strip_each_in(line[2].split(","))
    return out


# ==================================================
# Occurrences: Lines 454-457 (2 instances)

def _str_header(self, name, symbol="-"):
    return [name, len(name) * symbol]


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_trustregion_constr/tr_interior_point.py
# Line: 111

def _compute_constr(self, c_ineq, c_eq, s):
    # Compute barrier constraint
    return np.hstack((c_eq,
                      c_ineq + s))


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_shgo_lib/_complex.py
# Line: 1200

def deg_simplex(self, S, proj=None):
    """Test a simplex S for degeneracy (linear dependence in R^dim).

    Parameters
    ----------
    S : np.array
        Simplex with rows as vertex vectors
    proj : array, optional,
        If the projection S[1:] - S[0] is already
        computed it can be added as an optional argument.
    """
    # Strategy: we test all combination of faces, if any of the
    # determinants are zero then the vectors lie on the same face and is
    # therefore linearly dependent in the space of R^dim
    if proj is None:
        proj = S[1:] - S[0]

    # TODO: Is checking the projection of one vertex against faces of other
    #       vertices sufficient? Or do we need to check more vertices in
    #       dimensions higher than 2?
    # TODO: Literature seems to suggest using proj.T, but why is this
    #       needed?
    if np.linalg.det(proj) == 0.0:  # TODO: Replace with tolerance?
        return True  # Simplex is degenerate
    else:
        return False  # Simplex is not degenerate

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_trustregion.py
# Line: 90

def get_boundaries_intersections(self, z, d, trust_radius):
    """
    Solve the scalar quadratic equation ``||z + t d|| == trust_radius``.
    This is like a line-sphere intersection.
    Return the two values of t, sorted from low to high.
    """
    a = np.dot(d, d)
    b = 2 * np.dot(z, d)
    c = np.dot(z, z) - trust_radius**2
    sqrt_discriminant = math.sqrt(b*b - 4*a*c)

    # The following calculation is mathematically
    # equivalent to:
    # ta = (-b - sqrt_discriminant) / (2*a)
    # tb = (-b + sqrt_discriminant) / (2*a)
    # but produce smaller round off errors.
    # Look at Matrix Computation p.97
    # for a better justification.
    aux = b + math.copysign(sqrt_discriminant, b)
    ta = -aux / (2*a)
    tb = -2*c / aux
    return sorted([ta, tb])


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_differentialevolution.py
# Line: 1499

def _accept_trial(self, energy_trial, feasible_trial, cv_trial,
                  energy_orig, feasible_orig, cv_orig):
    """
    Trial is accepted if:
    * it satisfies all constraints and provides a lower or equal objective
      function value, while both the compared solutions are feasible
    - or -
    * it is feasible while the original solution is infeasible,
    - or -
    * it is infeasible, but provides a lower or equal constraint violation
      for all constraint functions.

    This test corresponds to section III of Lampinen [1]_.

    Parameters
    ----------
    energy_trial : float
        Energy of the trial solution
    feasible_trial : float
        Feasibility of trial solution
    cv_trial : array-like
        Excess constraint violation for the trial solution
    energy_orig : float
        Energy of the original solution
    feasible_orig : float
        Feasibility of original solution
    cv_orig : array-like
        Excess constraint violation for the original solution

    Returns
    -------
    accepted : bool

    """
    if feasible_orig and feasible_trial:
        return energy_trial <= energy_orig
    elif feasible_trial and not feasible_orig:
        return True
    elif not feasible_trial and (cv_trial <= cv_orig).all():
        # cv_trial < cv_orig would imply that both trial and orig are not
        # feasible
        return True

    return False


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_stats_py.py
# Occurrences: Lines 10762-10768 (3 instances)

def cdf(self, x):
    return special.ndtr(x)


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_continuous_distns.py
# Line: 174

def _shape_info(self):
    return [_ShapeInfo("n", True, (1, np.inf), (True, False))]


# ==================================================
# Line: 266

def _shape_info(self):
    return [_ShapeInfo("n", True, (1, np.inf), (True, False))]


# ==================================================
# Line: 330

def _shape_info(self):
    return []


# ==================================================
# Line: 416

def _shape_info(self):
    return []


# ==================================================
# Line: 542

def _shape_info(self):
    return [_ShapeInfo("a", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 585

def _shape_info(self):
    return []


# ==================================================
# Line: 631

def _shape_info(self):
    return []


# ==================================================
# Line: 739

def _shape_info(self):
    ia = _ShapeInfo("a", False, (0, np.inf), (False, False))
    ib = _ShapeInfo("b", False, (0, np.inf), (False, False))
    return [ia, ib]


# ==================================================
# Line: 1010

def _shape_info(self):
    ia = _ShapeInfo("a", False, (0, np.inf), (False, False))
    ib = _ShapeInfo("b", False, (0, np.inf), (False, False))
    return [ia, ib]


# ==================================================
# Line: 1096

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 1181

def _shape_info(self):
    ic = _ShapeInfo("c", False, (0, np.inf), (False, False))
    id = _ShapeInfo("d", False, (0, np.inf), (False, False))
    return [ic, id]


# ==================================================
# Line: 1302

def _shape_info(self):
    ic = _ShapeInfo("c", False, (0, np.inf), (False, False))
    id = _ShapeInfo("d", False, (0, np.inf), (False, False))
    return [ic, id]


# ==================================================
# Line: 1459

def _shape_info(self):
    return []


# ==================================================
# Line: 1542

def _shape_info(self):
    return [_ShapeInfo("df", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 1629

def _shape_info(self):
    return [_ShapeInfo("df", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 1707

def _shape_info(self):
    return []


# ==================================================
# Line: 1776

def _shape_info(self):
    return [_ShapeInfo("a", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 1887

def _shape_info(self):
    return [_ShapeInfo("u", False, (-np.inf, np.inf), (False, False)),
            _ShapeInfo("s", False, (0, np.inf), (False, False)),
            _ShapeInfo("a", False, (0, np.inf), (False, False)),
            _ShapeInfo("b", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 1984

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 2064

def _shape_info(self):
    return []


# ==================================================
# Line: 2191

def _shape_info(self):
    return [_ShapeInfo("K", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 2290

def _shape_info(self):
    ia = _ShapeInfo("a", False, (0, np.inf), (False, False))
    ic = _ShapeInfo("c", False, (0, np.inf), (False, False))
    return [ia, ic]


# ==================================================
# Line: 2352

def _shape_info(self):
    return [_ShapeInfo("b", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 2409

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 2483

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (True, False))]


# ==================================================
# Line: 2548

def _shape_info(self):
    idfn = _ShapeInfo("dfn", False, (0, np.inf), (False, False))
    idfd = _ShapeInfo("dfd", False, (0, np.inf), (False, False))
    return [idfn, idfd]


# ==================================================
# Line: 2657

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (True, False))]


# ==================================================
# Line: 2742

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 2909

def _shape_info(self):
    ic = _ShapeInfo("c", False, (0, np.inf), (False, False))
    ia = _ShapeInfo("a", False, (0, np.inf), (True, False))
    ib = _ShapeInfo("b", False, (0, np.inf), (False, False))
    return [ic, ia, ib]


# ==================================================
# Line: 3009

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 3079

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 3173

def _shape_info(self):
    return [_ShapeInfo("c", False, (-np.inf, np.inf), (False, False))]


# ==================================================
# Line: 3286

def _shape_info(self):
    ia = _ShapeInfo("a", False, (0, np.inf), (False, False))
    ib = _ShapeInfo("b", False, (0, np.inf), (False, False))
    ic = _ShapeInfo("c", False, (0, np.inf), (False, False))
    return [ia, ib, ic]


# ==================================================
# Line: 3363

def _shape_info(self):
    return [_ShapeInfo("c", False, (-np.inf, np.inf), (False, False))]


# ==================================================
# Line: 3371

def _loglogcdf(self, x, c):
    # Returns log(-log(cdf(x, c)))
    return xpx.apply_where(
        (x == x) & (c != 0), (x, c),
        lambda x, c: sc.log1p(-c*x)/c, 
        fill_value=-x)


# ==================================================
# Line: 3586

def _shape_info(self):
    return [_ShapeInfo("a", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 3851

def _shape_info(self):
    ia = _ShapeInfo("a", False, (0, np.inf), (False, False))
    ic = _ShapeInfo("c", False, (-np.inf, np.inf), (False, False))
    return [ia, ic]


# ==================================================
# Line: 3937

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 4062

def _shape_info(self):
    ip = _ShapeInfo("p", False, (-np.inf, np.inf), (False, False))
    ia = _ShapeInfo("a", False, (0, np.inf), (True, False))
    ib = _ShapeInfo("b", False, (-np.inf, np.inf), (False, False))
    return [ip, ia, ib]


# ==================================================
# Line: 4222

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 4287

def _shape_info(self):
    return []


# ==================================================
# Line: 4420

def _shape_info(self):
    return []


# ==================================================
# Line: 4492

def _shape_info(self):
    return []


# ==================================================
# Line: 4591

def _shape_info(self):
    return []


# ==================================================
# Line: 4716

def _shape_info(self):
    return []


# ==================================================
# Line: 4800

def _shape_info(self):
    return []


# ==================================================
# Line: 4866

def _shape_info(self):
    ia = _ShapeInfo("a", False, (0, np.inf), (False, False))
    ib = _ShapeInfo("b", False, (0, np.inf), (False, False))
    ic = _ShapeInfo("c", False, (-np.inf, np.inf), (False, False))
    iz = _ShapeInfo("z", False, (-1, np.inf), (False, False))
    return [ia, ib, ic, iz]


# ==================================================
# Line: 4920

def _shape_info(self):
    return [_ShapeInfo("a", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 5025

def _shape_info(self):
    return [_ShapeInfo("mu", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 5175

def _shape_info(self):
    ip = _ShapeInfo("p", False, (-np.inf, np.inf), (False, False))
    ib = _ShapeInfo("b", False, (0, np.inf), (False, False))
    return [ip, ib]


# ==================================================
# Line: 5214

def _logquasipdf(self, x, p, b):
    # log of the quasi-density (w/o normalizing constant) used in _rvs
    return xpx.apply_where(x > 0, (x, p, b),
                           lambda x, p, b: (p - 1)*np.log(x) - b*(x + 1/x)/2,
                           fill_value=-np.inf)


# ==================================================
# Line: 5428

def _mode(self, p, b):
    # distinguish cases to avoid catastrophic cancellation (see [2])
    if p < 1:
        return b / (np.sqrt((p - 1)**2 + b**2) + 1 - p)
    else:
        return (np.sqrt((1 - p)**2 + b**2) - (1 - p)) / b


# ==================================================
# Line: 5513

def _shape_info(self):
    ia = _ShapeInfo("a", False, (0, np.inf), (False, False))
    ib = _ShapeInfo("b", False, (-np.inf, np.inf), (False, False))
    return [ia, ib]


# ==================================================
# Line: 5636

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 5711

def _shape_info(self):
    ia = _ShapeInfo("a", False, (0, np.inf), (False, False))
    ib = _ShapeInfo("b", False, (0, np.inf), (False, False))
    return [ia, ib]


# ==================================================
# Line: 5810

def _shape_info(self):
    ia = _ShapeInfo("a", False, (-np.inf, np.inf), (False, False))
    ib = _ShapeInfo("b", False, (0, np.inf), (False, False))
    return [ia, ib]


# ==================================================
# Line: 5875

def _shape_info(self):
    ia = _ShapeInfo("a", False, (-np.inf, np.inf), (False, False))
    ib = _ShapeInfo("b", False, (0, np.inf), (False, False))
    return [ia, ib]


# ==================================================
# Line: 5976

def _shape_info(self):
    return []


# ==================================================
# Line: 6044

def _shape_info(self):
    return []


# ==================================================
# Line: 6143

def _shape_info(self):
    return [_ShapeInfo("kappa", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 6322

def _shape_info(self):
    return []


# ==================================================
# Line: 6425

def _shape_info(self):
    return []


# ==================================================
# Line: 6479

def _shape_info(self):
    return []


# ==================================================
# Line: 6599

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 6727

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 6847

def _shape_info(self):
    return [_ShapeInfo("s", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 7026

def _shape_info(self):
    return []


# ==================================================
# Line: 7093

def _shape_info(self):
    return []


# ==================================================
# Line: 7168

def _shape_info(self):
    ik = _ShapeInfo("k", False, (0, np.inf), (False, False))
    i_s = _ShapeInfo("s", False, (0, np.inf), (False, False))
    return [ik, i_s]


# ==================================================
# Line: 7292

def _shape_info(self):
    ih = _ShapeInfo("h", False, (-np.inf, np.inf), (False, False))
    ik = _ShapeInfo("k", False, (-np.inf, np.inf), (False, False))
    return [ih, ik]


# ==================================================
# Line: 7444

def _get_stats_info(self, h, k):
    condlist = [
        np.logical_and(h < 0, k >= 0),
        k < 0,
    ]

    def f0(h, k):
        return (-1.0/h*k).astype(int)

    def f1(h, k):
        return (-1.0/k).astype(int)

    return _lazyselect(condlist, [f0, f1], [h, k], default=5)


# ==================================================
# Line: 7506

def _shape_info(self):
    return [_ShapeInfo("a", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 7596

def _shape_info(self):
    return []


# ==================================================
# Line: 7683

def _shape_info(self):
    return [_ShapeInfo("nu", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 7807

def _shape_info(self):
    idf = _ShapeInfo("df", False, (0, np.inf), (False, False))
    inc = _ShapeInfo("nc", False, (0, np.inf), (True, False))
    return [idf, inc]


# ==================================================
# Line: 7916

def _shape_info(self):
    idf1 = _ShapeInfo("dfn", False, (0, np.inf), (False, False))
    idf2 = _ShapeInfo("dfd", False, (0, np.inf), (False, False))
    inc = _ShapeInfo("nc", False, (0, np.inf), (True, False))
    return [idf1, idf2, inc]


# ==================================================
# Line: 7994

def _shape_info(self):
    return [_ShapeInfo("df", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 8116

def _shape_info(self):
    idf = _ShapeInfo("df", False, (0, np.inf), (False, False))
    inc = _ShapeInfo("nc", False, (-np.inf, np.inf), (False, False))
    return [idf, inc]


# ==================================================
# Line: 8176

def _shape_info(self):
    return [_ShapeInfo("b", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 8339

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 8421

def _preprocess(self, x, skew):
    # The real 'loc' and 'scale' are handled in the calling pdf(...). The
    # local variables 'loc' and 'scale' within pearson3._pdf are set to
    # the defaults just to keep them as part of the equations for
    # documentation.
    loc = 0.0
    scale = 1.0

    # If skew is small, return _norm_pdf. The divide between pearson3
    # and norm was found by brute force and is approximately a skew of
    # 0.000016.  No one, I hope, would actually use a skew value even
    # close to this small.
    norm2pearson_transition = 0.000016

    ans, x, skew = np.broadcast_arrays(1.0, x, skew)
    ans = ans.copy()

    # mask is True where skew is small enough to use the normal approx.
    mask = np.absolute(skew) < norm2pearson_transition
    invmask = ~mask

    beta = 2.0 / (skew[invmask] * scale)
    alpha = (scale * beta)**2
    zeta = loc - alpha / beta

    transx = beta * (x[invmask] - zeta)
    return ans, x, transx, mask, invmask, beta, alpha, zeta


# ==================================================
# Line: 8456

def _shape_info(self):
    return [_ShapeInfo("skew", False, (-np.inf, np.inf), (False, False))]


# ==================================================
# Line: 8607

def _shape_info(self):
    return [_ShapeInfo("a", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 8885

def _shape_info(self):
    ic = _ShapeInfo("c", False, (0, np.inf), (False, False))
    i_s = _ShapeInfo("s", False, (0, np.inf), (False, False))
    return [ic, i_s]


# ==================================================
# Line: 8945

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 9008

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 9062

def _shape_info(self):
    return []


# ==================================================
# Line: 9217

def _shape_info(self):
    ia = _ShapeInfo("a", False, (0, np.inf), (False, False))
    ib = _ShapeInfo("b", False, (0, np.inf), (False, False))
    return [ia, ib]


# ==================================================
# Line: 9306

def _shape_info(self):
    return [_ShapeInfo("b", False, (0, np.inf), (True, False))]


# ==================================================
# Line: 9411

def _shape_info(self):
    return [_ShapeInfo("n", True, (1, np.inf), (True, False))]


# ==================================================
# Line: 9494

def _shape_info(self):
    return [_ShapeInfo("mu", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 9559

def _shape_info(self):
    return []


# ==================================================
# Line: 9628

def _shape_info(self):
    return [_ShapeInfo("a", False, (-1.0, 1.0), (False, False))]


# ==================================================
# Line: 9694

def _shape_info(self):
    return [_ShapeInfo("a", False, (-np.inf, np.inf), (False, False))]


# ==================================================
# Line: 9926

def _shape_info(self):
    ic = _ShapeInfo("c", False, (0, 1.0), (True, True))
    id = _ShapeInfo("d", False, (0, 1.0), (True, True))
    return [ic, id]


# ==================================================
# Line: 10026

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, 1.0), (True, True))]


# ==================================================
# Line: 10096

def _shape_info(self):
    return [_ShapeInfo("b", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 10259

def _shape_info(self):
    ia = _ShapeInfo("a", False, (-np.inf, np.inf), (True, False))
    ib = _ShapeInfo("b", False, (-np.inf, np.inf), (False, True))
    return [ia, ib]


# ==================================================
# Line: 10475

def _shape_info(self):
    ib = _ShapeInfo("b", False, (0.0, np.inf), (False, False))
    ic = _ShapeInfo("c", False, (1.0, np.inf), (False, False))
    return [ib, ic]


# ==================================================
# Line: 10782

def _shape_info(self):
    return [_ShapeInfo("lam", False, (-np.inf, np.inf), (False, False))]


# ==================================================
# Line: 10838

def _shape_info(self):
    return []


# ==================================================
# Line: 11108

def _shape_info(self):
    return [_ShapeInfo("kappa", False, (0, np.inf), (True, False))]


# ==================================================
# Line: 11136

def _stats_skip(self, kappa):
    return 0, None, 0, None


# ==================================================
# Line: 11347

def _shape_info(self):
    return [_ShapeInfo("c", False, (0, 1), (False, False))]


# ==================================================
# Line: 11435

def _shape_info(self):
    return [_ShapeInfo("beta", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 11527

def _shape_info(self):
    return [_ShapeInfo("beta", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 11600

def _shape_info(self):
    ibeta = _ShapeInfo("beta", False, (0, np.inf), (False, False))
    im = _ShapeInfo("m", False, (1, np.inf), (False, False))
    return [ibeta, im]


# ==================================================
# Line: 11784

def _shape_info(self):
    return [_ShapeInfo("chi", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 11827

def _rvs_scalar(self, chi, numsamples=None, random_state=None):
    # if chi <= 1.8:
    # use rejection method, see Devroye:
    # Non-Uniform Random Variate Generation, 1986, section II.3.2.
    # write: PDF f(x) = c * g(x) * h(x), where
    # h is [0,1]-valued and g is a density
    # we use two ways to write f
    #
    # Case 1:
    # write g(x) = 3*x*sqrt(1-x**2), h(x) = exp(-chi**2 (1-x**2) / 2)
    # If X has a distribution with density g its ppf G_inv is given by:
    # G_inv(u) = np.sqrt(1 - u**(2/3))
    #
    # Case 2:
    # g(x) = chi**2 * x * exp(-chi**2 * (1-x**2)/2) / (1 - exp(-chi**2 /2))
    # h(x) = sqrt(1 - x**2), 0 <= x <= 1
    # one can show that
    # G_inv(u) = np.sqrt(2*np.log(u*(np.exp(chi**2/2)-1)+1))/chi
    #          = np.sqrt(1 + 2*np.log(np.exp(-chi**2/2)*(1-u)+u)/chi**2)
    # the latter expression is used for precision with small chi
    #
    # In both cases, the inverse cdf of g can be written analytically, and
    # we can apply the rejection method:
    #
    # REPEAT
    #    Generate U uniformly distributed on [0, 1]
    #    Generate X with density g (e.g. via inverse transform sampling:
    #    X = G_inv(V) with V uniformly distributed on [0, 1])
    # UNTIL X <= h(X)
    # RETURN X
    #
    # We use case 1 for chi <= 0.5 as it maintains precision for small chi
    # and case 2 for 0.5 < chi <= 1.8 due to its speed for moderate chi.
    #
    # if chi > 1.8:
    # use relation to the Gamma distribution: if X is ARGUS with parameter
    # chi), then Y = chi**2 * (1 - X**2) / 2 has density proportional to
    # sqrt(u) * exp(-u) on [0, chi**2 / 2], i.e. a Gamma(3/2) distribution
    # conditioned on [0, chi**2 / 2]). Therefore, to sample X from the
    # ARGUS distribution, we sample Y from the gamma distribution, keeping
    # only samples on [0, chi**2 / 2], and apply the inverse
    # transformation X = (1 - 2*Y/chi**2)**(1/2). Since we only
    # look at chi > 1.8, gamma(1.5).cdf(chi**2/2) is large enough such
    # Y falls in the interval [0, chi**2 / 2] with a high probability:
    # stats.gamma(1.5).cdf(1.8**2/2) = 0.644...
    #
    # The points to switch between the different methods are determined
    # by a comparison of the runtime of the different methods. However,
    # the runtime is platform-dependent. The implemented values should
    # ensure a good overall performance and are supported by an analysis
    # of the rejection constants of different methods.

    size1d = tuple(np.atleast_1d(numsamples))
    N = int(np.prod(size1d))
    x = np.zeros(N)
    simulated = 0
    chi2 = chi * chi
    if chi <= 0.5:
        d = -chi2 / 2
        while simulated < N:
            k = N - simulated
            u = random_state.uniform(size=k)
            v = random_state.uniform(size=k)
            z = v**(2/3)
            # acceptance condition: u <= h(G_inv(v)). This simplifies to
            accept = (np.log(u) <= d * z)
            num_accept = np.sum(accept)
            if num_accept > 0:
                # we still need to transform z=v**(2/3) to X = G_inv(v)
                rvs = np.sqrt(1 - z[accept])
                x[simulated:(simulated + num_accept)] = rvs
                simulated += num_accept
    elif chi <= 1.8:
        echi = np.exp(-chi2 / 2)
        while simulated < N:
            k = N - simulated
            u = random_state.uniform(size=k)
            v = random_state.uniform(size=k)
            z = 2 * np.log(echi * (1 - v) + v) / chi2
            # as in case one, simplify u <= h(G_inv(v)) and then transform
            # z to the target distribution X = G_inv(v)
            accept = (u**2 + z <= 0)
            num_accept = np.sum(accept)
            if num_accept > 0:
                rvs = np.sqrt(1 + z[accept])
                x[simulated:(simulated + num_accept)] = rvs
                simulated += num_accept
    else:
        # conditional Gamma for chi > 1.8
        while simulated < N:
            k = N - simulated
            g = random_state.standard_gamma(1.5, size=k)
            accept = (g <= chi2 / 2)
            num_accept = np.sum(accept)
            if num_accept > 0:
                x[simulated:(simulated + num_accept)] = g[accept]
                simulated += num_accept
        x = np.sqrt(1 - 2 * x / chi2)

    return np.reshape(x, size1d)


# ==================================================
# Line: 12239

def _shape_info(self):
    ik = _ShapeInfo("k", False, (1, np.inf), (False, False))
    idf = _ShapeInfo("df", False, (0, np.inf), (False, False))
    return [ik, idf]


# ==================================================
# Line: 12393

def _shape_info(self):
    return [_ShapeInfo("rho", False, (0, np.inf), (False, False))]


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_distn_infrastructure.py
# Line: 908

def _stats(self, *args, **kwds):
    return None, None, None, None


# ==================================================
# Line: 920

def _argcheck_rvs(self, *args, **kwargs):
    # Handle broadcasting and size validation of the rvs method.
    # Subclasses should not have to override this method.
    # The rule is that if `size` is not None, then `size` gives the
    # shape of the result (integer values of `size` are treated as
    # tuples with length 1; i.e. `size=3` is the same as `size=(3,)`.)
    #
    # `args` is expected to contain the shape parameters (if any), the
    # location and the scale in a flat tuple (e.g. if there are two
    # shape parameters `a` and `b`, `args` will be `(a, b, loc, scale)`).
    # The only keyword argument expected is 'size'.
    size = kwargs.get('size', None)
    all_bcast = np.broadcast_arrays(*args)

    def squeeze_left(a):
        while a.ndim > 0 and a.shape[0] == 1:
            a = a[0]
        return a

    # Eliminate trivial leading dimensions.  In the convention
    # used by numpy's random variate generators, trivial leading
    # dimensions are effectively ignored.  In other words, when `size`
    # is given, trivial leading dimensions of the broadcast parameters
    # in excess of the number of dimensions  in size are ignored, e.g.
    #   >>> np.random.normal([[1, 3, 5]], [[[[0.01]]]], size=3)
    #   array([ 1.00104267,  3.00422496,  4.99799278])
    # If `size` is not given, the exact broadcast shape is preserved:
    #   >>> np.random.normal([[1, 3, 5]], [[[[0.01]]]])
    #   array([[[[ 1.00862899,  3.00061431,  4.99867122]]]])
    #
    all_bcast = [squeeze_left(a) for a in all_bcast]
    bcast_shape = all_bcast[0].shape
    bcast_ndim = all_bcast[0].ndim

    if size is None:
        size_ = bcast_shape
    else:
        size_ = tuple(np.atleast_1d(size))

    # Check compatibility of size_ with the broadcast shape of all
    # the parameters.  This check is intended to be consistent with
    # how the numpy random variate generators (e.g. np.random.normal,
    # np.random.beta) handle their arguments.   The rule is that, if size
    # is given, it determines the shape of the output.  Broadcasting
    # can't change the output size.

    # This is the standard broadcasting convention of extending the
    # shape with fewer dimensions with enough dimensions of length 1
    # so that the two shapes have the same number of dimensions.
    ndiff = bcast_ndim - len(size_)
    if ndiff < 0:
        bcast_shape = (1,)*(-ndiff) + bcast_shape
    elif ndiff > 0:
        size_ = (1,)*ndiff + size_

    # This compatibility test is not standard.  In "regular" broadcasting,
    # two shapes are compatible if for each dimension, the lengths are the
    # same or one of the lengths is 1.  Here, the length of a dimension in
    # size_ must not be less than the corresponding length in bcast_shape.
    ok = all([bcdim == 1 or bcdim == szdim
              for (bcdim, szdim) in zip(bcast_shape, size_)])
    if not ok:
        raise ValueError("size does not match the broadcast shape of "
                         f"the parameters. {size}, {size_}, {bcast_shape}")

    param_bcast = all_bcast[:-2]
    loc_bcast = all_bcast[-2]
    scale_bcast = all_bcast[-1]

    return param_bcast, loc_bcast, scale_bcast, size_


# ==================================================
# Line: 994

def _argcheck(self, *args):
    """Default check for correct values on args and keywords.

    Returns condition array of 1's where arguments are correct and
     0's where they are not.

    """
    cond = 1
    for arg in args:
        cond = logical_and(cond, (asarray(arg) > 0))
    return cond


# ==================================================
# Line: 2381

def _unpack_loc_scale(self, theta):
    try:
        loc = theta[-2]
        scale = theta[-1]
        args = tuple(theta[:-2])
    except IndexError as e:
        raise ValueError("Not enough input arguments.") from e
    return loc, scale, args


# ==================================================
# Line: 3424

def _nonzero(self, k, *args):
    return floor(k) == k


# ==================================================
# Line: 3440

def _unpack_loc_scale(self, theta):
    try:
        loc = theta[-1]
        scale = 1
        args = tuple(theta[:-1])
    except IndexError as e:
        raise ValueError("Not enough input arguments.") from e
    return loc, scale, args


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_discrete_distns.py
# Line: 66

def _shape_info(self):
    return [_ShapeInfo("n", True, (0, np.inf), (True, False)),
            _ShapeInfo("p", False, (0, 1), (True, True))]


# ==================================================
# Line: 233

def _shape_info(self):
    return [_ShapeInfo("n", True, (0, np.inf), (True, False)),
            _ShapeInfo("a", False, (0, np.inf), (False, False)),
            _ShapeInfo("b", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 341

def _shape_info(self):
    return [_ShapeInfo("n", True, (0, np.inf), (True, False)),
            _ShapeInfo("p", False, (0, 1), (True, True))]


# ==================================================
# Line: 439

def _shape_info(self):
    return [_ShapeInfo("n", True, (0, np.inf), (True, False)),
            _ShapeInfo("a", False, (0, np.inf), (False, False)),
            _ShapeInfo("b", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 532

def _shape_info(self):
    return [_ShapeInfo("p", False, (0, 1), (True, True))]


# ==================================================
# Line: 656

def _shape_info(self):
    return [_ShapeInfo("M", True, (0, np.inf), (True, False)),
            _ShapeInfo("n", True, (0, np.inf), (True, False)),
            _ShapeInfo("N", True, (0, np.inf), (True, False))]


# ==================================================
# Line: 841

def _shape_info(self):
    return [_ShapeInfo("M", True, (0, np.inf), (True, False)),
            _ShapeInfo("n", True, (0, np.inf), (True, False)),
            _ShapeInfo("r", True, (0, np.inf), (True, False))]


# ==================================================
# Line: 927

def _shape_info(self):
    return [_ShapeInfo("p", False, (0, 1), (True, True))]


# ==================================================
# Line: 986

def _shape_info(self):
    return [_ShapeInfo("mu", False, (0, np.inf), (True, False))]


# ==================================================
# Line: 1058

def _shape_info(self):
    return [_ShapeInfo("lambda_", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 1126

def _shape_info(self):
    return [_ShapeInfo("lambda_", False, (0, np.inf), (False, False)),
            _ShapeInfo("N", True, (0, np.inf), (False, False))]


# ==================================================
# Line: 1235

def _shape_info(self):
    return [_ShapeInfo("low", True, (-np.inf, np.inf), (False, False)),
            _ShapeInfo("high", True, (-np.inf, np.inf), (False, False))]


# ==================================================
# Line: 1339

def _shape_info(self):
    return [_ShapeInfo("a", False, (1, np.inf), (False, False))]


# ==================================================
# Line: 1437

def _shape_info(self):
    return [_ShapeInfo("a", False, (0, np.inf), (True, False)),
            _ShapeInfo("n", True, (0, np.inf), (False, False))]


# ==================================================
# Line: 1506

def _shape_info(self):
    return [_ShapeInfo("a", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 1608

def _shape_info(self):
    # message = 'Fitting is not implemented for this distribution."
    # raise NotImplementedError(message)
    return []


# ==================================================
# Line: 1731

def _shape_info(self):
    return [_ShapeInfo("mu1", False, (0, np.inf), (False, False)),
            _ShapeInfo("mu2", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 1801

def _shape_info(self):
    return [_ShapeInfo("alpha", False, (0, np.inf), (False, False))]


# ==================================================
# Line: 1859

def _shape_info(self):
    return [_ShapeInfo("M", True, (0, np.inf), (True, False)),
            _ShapeInfo("n", True, (0, np.inf), (True, False)),
            _ShapeInfo("N", True, (0, np.inf), (True, False)),
            _ShapeInfo("odds", False, (0, np.inf), (False, False))]


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_multivariate.py
# Line: 431

def _process_parameters_Covariance(self, mean, cov):
    dim = cov.shape[-1]
    mean = np.array([0.]) if mean is None else mean
    message = (f"`cov` represents a covariance matrix in {dim} dimensions,"
               f"and so `mean` must be broadcastable to shape {(dim,)}")
    try:
        mean = np.broadcast_to(mean, dim)
    except ValueError as e:
        raise ValueError(message) from e
    return dim, mean, cov


# ==================================================
# Line: 442

def _process_parameters_psd(self, dim, mean, cov):
    # Try to infer dimensionality
    if dim is None:
        if mean is None:
            if cov is None:
                dim = 1
            else:
                cov = np.asarray(cov, dtype=float)
                if cov.ndim < 2:
                    dim = 1
                else:
                    dim = cov.shape[0]
        else:
            mean = np.asarray(mean, dtype=float)
            dim = mean.size
    else:
        if not np.isscalar(dim):
            raise ValueError("Dimension of random variable must be "
                             "a scalar.")

    # Check input sizes and return full arrays for mean and cov if
    # necessary
    if mean is None:
        mean = np.zeros(dim)
    mean = np.asarray(mean, dtype=float)

    if cov is None:
        cov = 1.0
    cov = np.asarray(cov, dtype=float)

    if dim == 1:
        mean = mean.reshape(1)
        cov = cov.reshape(1, 1)

    if mean.ndim != 1 or mean.shape[0] != dim:
        raise ValueError(f"Array 'mean' must be a vector of length {dim}.")
    if cov.ndim == 0:
        cov = cov * np.eye(dim)
    elif cov.ndim == 1:
        cov = np.diag(cov)
    elif cov.ndim == 2 and cov.shape != (dim, dim):
        rows, cols = cov.shape
        if rows != cols:
            msg = ("Array 'cov' must be square if it is two dimensional,"
                   f" but cov.shape = {str(cov.shape)}.")
        else:
            msg = (f"Dimension mismatch: array 'cov' is of shape {cov.shape}, "
                   f"but 'mean' is a vector of length {len(mean)}.")
        raise ValueError(msg)
    elif cov.ndim > 2:
        raise ValueError(f"Array 'cov' must be at most two-dimensional, "
                         f"but cov.ndim = {cov.ndim}")

    return dim, mean, cov


# ==================================================
# Line: 497

def _process_quantiles(self, x, dim):
    """
    Adjust quantiles array so that last axis labels the components of
    each data point.
    """
    x = np.asarray(x, dtype=float)

    if x.ndim == 0:
        x = x[np.newaxis]
    elif x.ndim == 1:
        if dim == 1:
            x = x[:, np.newaxis]
        else:
            x = x[np.newaxis, :]

    return x


# ==================================================
# Line: 514

def _logpdf(self, x, mean, cov_object):
    """Log of the multivariate normal probability density function.

    Parameters
    ----------
    x : ndarray
        Points at which to evaluate the log of the probability
        density function
    mean : ndarray
        Mean of the distribution
    cov_object : Covariance
        An object representing the Covariance matrix

    Notes
    -----
    As this function does no argument checking, it should not be
    called directly; use 'logpdf' instead.

    """
    log_det_cov, rank = cov_object.log_pdet, cov_object.rank
    dev = x - mean
    if dev.ndim > 1:
        log_det_cov = log_det_cov[..., np.newaxis]
        rank = rank[..., np.newaxis]
    maha = np.sum(np.square(cov_object.whiten(dev)), axis=-1)
    return -0.5 * (rank * _LOG_2PI + log_det_cov + maha)


# ==================================================
# Line: 597

def _cdf(self, x, mean, cov, maxpts, abseps, releps, lower_limit, rng):
    """Multivariate normal cumulative distribution function.

    Parameters
    ----------
    x : ndarray
        Points at which to evaluate the cumulative distribution function.
    mean : ndarray
        Mean of the distribution
    cov : array_like
        Covariance matrix of the distribution
    maxpts : integer
        The maximum number of points to use for integration
    abseps : float
        Absolute error tolerance
    releps : float
        Relative error tolerance
    lower_limit : array_like, optional
        Lower limit of integration of the cumulative distribution function.
        Default is negative infinity. Must be broadcastable with `x`.
    rng : Generator
        an instance of ``np.random.Generator``, which is used internally
        for QMC integration.

    Notes
    -----
    As this function does no argument checking, it should not be
    called directly; use 'cdf' instead.


    .. versionadded:: 1.0.0

    """
    lower = (np.full(mean.shape, -np.inf)
             if lower_limit is None else lower_limit)
    # In 2d, _mvn.mvnun accepts input in which `lower` bound elements
    # are greater than `x`. Not so in other dimensions. Fix this by
    # ensuring that lower bounds are indeed lower when passed, then
    # set signs of resulting CDF manually.
    b, a = np.broadcast_arrays(x, lower)
    b, a = b - mean, a - mean  # _qmvn only accepts zero mean
    i_swap = b < a
    signs = (-1)**(i_swap.sum(axis=-1))  # odd # of swaps -> negative
    a, b = a.copy(), b.copy()
    a[i_swap], b[i_swap] = b[i_swap], a[i_swap]
    n = x.shape[-1]
    limits = np.concatenate((a, b), axis=-1)

    # qmvn expects 1-d arguments, so process points sequentially
    # XXX: if cov.ndim == 2 and limits.ndim == 1, can avoid apply_along_axis
    def func1d(limits):
        # res0 = _qmvn(maxpts, cov, limits[:n], limits[n:], rng)[0]
        res = _qauto(_qmvn, cov, limits[:n], limits[n:],
                     rng, error=abseps, limit=maxpts, n_batches=10)
        return np.squeeze(res[0])

    out = np.apply_along_axis(func1d, -1, limits) * signs
    return _squeeze_output(out)


# ==================================================
# Line: 808

def fit(self, x, fix_mean=None, fix_cov=None):
    """Fit a multivariate normal distribution to data.

    Parameters
    ----------
    x : ndarray (m, n)
        Data the distribution is fitted to. Must have two axes.
        The first axis of length `m` represents the number of vectors
        the distribution is fitted to. The second axis of length `n`
        determines the dimensionality of the fitted distribution.
    fix_mean : ndarray(n, )
        Fixed mean vector. Must have length `n`.
    fix_cov: ndarray (n, n)
        Fixed covariance matrix. Must have shape ``(n, n)``.

    Returns
    -------
    mean : ndarray (n, )
        Maximum likelihood estimate of the mean vector
    cov : ndarray (n, n)
        Maximum likelihood estimate of the covariance matrix

    """
    # input validation for data to be fitted
    x = np.asarray(x)
    if x.ndim != 2:
        raise ValueError("`x` must be two-dimensional.")

    n_vectors, dim = x.shape

    # parameter estimation
    # reference: https://home.ttic.edu/~shubhendu/Slides/Estimation.pdf
    if fix_mean is not None:
        # input validation for `fix_mean`
        fix_mean = np.atleast_1d(fix_mean)
        if fix_mean.shape != (dim, ):
            msg = ("`fix_mean` must be a one-dimensional array the same "
                   "length as the dimensionality of the vectors `x`.")
            raise ValueError(msg)
        mean = fix_mean
    else:
        mean = x.mean(axis=0)

    if fix_cov is not None:
        # input validation for `fix_cov`
        fix_cov = np.atleast_2d(fix_cov)
        # validate shape
        if fix_cov.shape != (dim, dim):
            msg = ("`fix_cov` must be a two-dimensional square array "
                   "of same side length as the dimensionality of the "
                   "vectors `x`.")
            raise ValueError(msg)
        # validate positive semidefiniteness
        # a trimmed down copy from _PSD
        s, u = scipy.linalg.eigh(fix_cov, lower=True, check_finite=True)
        eps = _eigvalsh_to_eps(s)
        if np.min(s) < -eps:
            msg = "`fix_cov` must be symmetric positive semidefinite."
            raise ValueError(msg)
        cov = fix_cov
    else:
        centered_data = x - mean
        cov = centered_data.T @ centered_data / n_vectors
    return mean, cov



# ==================================================
# Line: 1140

def _process_parameters(self, mean, rowcov, colcov):
    """
    Infer dimensionality from mean or covariance matrices. Handle
    defaults. Ensure compatible dimensions.
    """

    # Process mean
    if mean is not None:
        mean = np.asarray(mean, dtype=float)
        meanshape = mean.shape
        if len(meanshape) != 2:
            raise ValueError("Array `mean` must be two dimensional.")
        if np.any(meanshape == 0):
            raise ValueError("Array `mean` has invalid shape.")

    # Process among-row covariance
    rowcov = np.asarray(rowcov, dtype=float)
    if rowcov.ndim == 0:
        if mean is not None:
            rowcov = rowcov * np.identity(meanshape[0])
        else:
            rowcov = rowcov * np.identity(1)
    elif rowcov.ndim == 1:
        rowcov = np.diag(rowcov)
    rowshape = rowcov.shape
    if len(rowshape) != 2:
        raise ValueError("`rowcov` must be a scalar or a 2D array.")
    if rowshape[0] != rowshape[1]:
        raise ValueError("Array `rowcov` must be square.")
    if rowshape[0] == 0:
        raise ValueError("Array `rowcov` has invalid shape.")
    numrows = rowshape[0]

    # Process among-column covariance
    colcov = np.asarray(colcov, dtype=float)
    if colcov.ndim == 0:
        if mean is not None:
            colcov = colcov * np.identity(meanshape[1])
        else:
            colcov = colcov * np.identity(1)
    elif colcov.ndim == 1:
        colcov = np.diag(colcov)
    colshape = colcov.shape
    if len(colshape) != 2:
        raise ValueError("`colcov` must be a scalar or a 2D array.")
    if colshape[0] != colshape[1]:
        raise ValueError("Array `colcov` must be square.")
    if colshape[0] == 0:
        raise ValueError("Array `colcov` has invalid shape.")
    numcols = colshape[0]

    # Ensure mean and covariances compatible
    if mean is not None:
        if meanshape[0] != numrows:
            raise ValueError("Arrays `mean` and `rowcov` must have the "
                             "same number of rows.")
        if meanshape[1] != numcols:
            raise ValueError("Arrays `mean` and `colcov` must have the "
                             "same number of columns.")
    else:
        mean = np.zeros((numrows, numcols))

    dims = (numrows, numcols)

    return dims, mean, rowcov, colcov


# ==================================================
# Line: 1206

def _process_quantiles(self, X, dims):
    """
    Adjust quantiles array so that last two axes labels the components of
    each data point.
    """
    X = np.asarray(X, dtype=float)
    if X.ndim == 2:
        X = X[np.newaxis, :]
    if X.shape[-2:] != dims:
        raise ValueError("The shape of array `X` is not compatible "
                         "with the distribution parameters.")
    return X


# ==================================================
# Line: 1219

def _logpdf(self, dims, X, mean, row_prec_rt, log_det_rowcov,
            col_prec_rt, log_det_colcov):
    """Log of the matrix normal probability density function.

    Parameters
    ----------
    dims : tuple
        Dimensions of the matrix variates
    X : ndarray
        Points at which to evaluate the log of the probability
        density function
    mean : ndarray
        Mean of the distribution
    row_prec_rt : ndarray
        A decomposition such that np.dot(row_prec_rt, row_prec_rt.T)
        is the inverse of the among-row covariance matrix
    log_det_rowcov : float
        Logarithm of the determinant of the among-row covariance matrix
    col_prec_rt : ndarray
        A decomposition such that np.dot(col_prec_rt, col_prec_rt.T)
        is the inverse of the among-column covariance matrix
    log_det_colcov : float
        Logarithm of the determinant of the among-column covariance matrix

    Notes
    -----
    As this function does no argument checking, it should not be
    called directly; use 'logpdf' instead.

    """
    numrows, numcols = dims
    roll_dev = np.moveaxis(X-mean, -1, 0)
    scale_dev = np.tensordot(col_prec_rt.T,
                             np.dot(roll_dev, row_prec_rt), 1)
    maha = np.sum(np.sum(np.square(scale_dev), axis=-1), axis=0)
    return -0.5 * (numrows*numcols*_LOG_2PI + numcols*log_det_rowcov
                   + numrows*log_det_colcov + maha)


# ==================================================
# Line: 1376

def _entropy(self, dims, row_cov_logdet, col_cov_logdet):
    n, p = dims
    return (0.5 * n * p * (1 + _LOG_2PI) + 0.5 * p * row_cov_logdet +
            0.5 * n * col_cov_logdet)



# ==================================================
# Line: 1662

def _logpdf(self, x, alpha):
    """Log of the Dirichlet probability density function.

    Parameters
    ----------
    x : ndarray
        Points at which to evaluate the log of the probability
        density function
    %(_dirichlet_doc_default_callparams)s

    Notes
    -----
    As this function does no argument checking, it should not be
    called directly; use 'logpdf' instead.

    """
    lnB = _lnB(alpha)
    return - lnB + np.sum((xlogy(alpha - 1, x.T)).T, 0)


# ==================================================
# Line: 1723

def mean(self, alpha):
    """Mean of the Dirichlet distribution.

    Parameters
    ----------
    %(_dirichlet_doc_default_callparams)s

    Returns
    -------
    mu : ndarray or scalar
        Mean of the Dirichlet distribution.

    """
    alpha = _dirichlet_check_parameters(alpha)

    out = alpha / (np.sum(alpha))
    return _squeeze_output(out)


# ==================================================
# Line: 1741

def var(self, alpha):
    """Variance of the Dirichlet distribution.

    Parameters
    ----------
    %(_dirichlet_doc_default_callparams)s

    Returns
    -------
    v : ndarray or scalar
        Variance of the Dirichlet distribution.

    """

    alpha = _dirichlet_check_parameters(alpha)

    alpha0 = np.sum(alpha)
    out = (alpha * (alpha0 - alpha)) / ((alpha0 * alpha0) * (alpha0 + 1))
    return _squeeze_output(out)


# ==================================================
# Line: 1761

def cov(self, alpha):
    """Covariance matrix of the Dirichlet distribution.

    Parameters
    ----------
    %(_dirichlet_doc_default_callparams)s

    Returns
    -------
    cov : ndarray
        The covariance matrix of the distribution.
    """

    alpha = _dirichlet_check_parameters(alpha)
    alpha0 = np.sum(alpha)
    a = alpha / alpha0

    cov = (np.diag(a) - np.outer(a, a)) / (alpha0 + 1)
    return _squeeze_output(cov)


# ==================================================
# Line: 1781

def entropy(self, alpha):
    """
    Differential entropy of the Dirichlet distribution.

    Parameters
    ----------
    %(_dirichlet_doc_default_callparams)s

    Returns
    -------
    h : scalar
        Entropy of the Dirichlet distribution

    """

    alpha = _dirichlet_check_parameters(alpha)

    alpha0 = np.sum(alpha)
    lnB = _lnB(alpha)
    K = alpha.shape[0]

    out = lnB + (alpha0 - K) * scipy.special.psi(alpha0) - np.sum(
        (alpha - 1) * scipy.special.psi(alpha))
    return _squeeze_output(out)


# ==================================================
# Line: 2020

def _process_parameters(self, df, scale):
    if scale is None:
        scale = 1.0
    scale = np.asarray(scale, dtype=float)

    if scale.ndim == 0:
        scale = scale[np.newaxis, np.newaxis]
    elif scale.ndim == 1:
        scale = np.diag(scale)
    elif scale.ndim == 2 and not scale.shape[0] == scale.shape[1]:
        raise ValueError("Array 'scale' must be square if it is two dimensional,"
                         f" but scale.scale = {str(scale.shape)}.")
    elif scale.ndim > 2:
        raise ValueError(f"Array 'scale' must be at most two-dimensional, "
                         f"but scale.ndim = {scale.ndim}")

    dim = scale.shape[0]

    if df is None:
        df = dim
    elif not np.isscalar(df):
        raise ValueError("Degrees of freedom must be a scalar.")
    elif df <= dim - 1:
        raise ValueError("Degrees of freedom must be greater than the "
                         "dimension of scale matrix minus 1.")

    return dim, df, scale


# ==================================================
# Line: 2048

def _process_quantiles(self, x, dim):
    """
    Adjust quantiles array so that last axis labels the components of
    each data point.
    """
    x = np.asarray(x, dtype=float)

    if x.ndim == 0:
        x = x * np.eye(dim)[:, :, np.newaxis]
    if x.ndim == 1:
        if dim == 1:
            x = x[np.newaxis, np.newaxis, :]
        else:
            x = np.diag(x)[:, :, np.newaxis]
    elif x.ndim == 2:
        if not x.shape[0] == x.shape[1]:
            raise ValueError(
                "Quantiles must be square if they are two dimensional,"
                f" but x.shape = {str(x.shape)}.")
        x = x[:, :, np.newaxis]
    elif x.ndim == 3:
        if not x.shape[0] == x.shape[1]:
            raise ValueError(
                "Quantiles must be square in the first two dimensions "
                f"if they are three dimensional, but x.shape = {str(x.shape)}.")
    elif x.ndim > 3:
        raise ValueError(f"Quantiles must be at most two-dimensional with an "
                         f"additional dimension for multiple components, "
                         f"but x.ndim = {x.ndim}")

    # Now we have 3-dim array; should have shape [dim, dim, *]
    if not x.shape[0:2] == (dim, dim):
        raise ValueError('Quantiles have incompatible dimensions: should'
                         f' be {(dim, dim)}, got {x.shape[0:2]}.')

    return x


# ==================================================
# Line: 2085

def _process_size(self, size):
    size = np.asarray(size)

    if size.ndim == 0:
        size = size[np.newaxis]
    elif size.ndim > 1:
        raise ValueError('Size must be an integer or tuple of integers;'
             ' thus must have dimension <= 1.'
             f' Got size.ndim = {str(tuple(size))}')
    n = size.prod()
    shape = tuple(size)

    return n, shape


# ==================================================
# Line: 2196

def _mean(self, dim, df, scale):
    """Mean of the Wishart distribution.

    Parameters
    ----------
    dim : int
        Dimension of the scale matrix
    %(_doc_default_callparams)s

    Notes
    -----
    As this function does no argument checking, it should not be
    called directly; use 'mean' instead.

    """
    return df * scale


# ==================================================
# Line: 2229

def _mode(self, dim, df, scale):
    """Mode of the Wishart distribution.

    Parameters
    ----------
    dim : int
        Dimension of the scale matrix
    %(_doc_default_callparams)s

    Notes
    -----
    As this function does no argument checking, it should not be
    called directly; use 'mode' instead.

    """
    if df >= dim + 1:
        out = (df-dim-1) * scale
    else:
        out = None
    return out


# ==================================================
# Line: 2269

def _var(self, dim, df, scale):
    """Variance of the Wishart distribution.

    Parameters
    ----------
    dim : int
        Dimension of the scale matrix
    %(_doc_default_callparams)s

    Notes
    -----
    As this function does no argument checking, it should not be
    called directly; use 'var' instead.

    """
    var = scale**2
    diag = scale.diagonal()  # 1 x dim array
    var += np.outer(diag, diag)
    var *= df
    return var


# ==================================================
# Line: 2306

def _standard_rvs(self, n, shape, dim, df, random_state):
    """
    Parameters
    ----------
    n : integer
        Number of variates to generate
    shape : iterable
        Shape of the variates to generate
    dim : int
        Dimension of the scale matrix
    df : int
        Degrees of freedom
    random_state : {None, int, `numpy.random.Generator`,
                    `numpy.random.RandomState`}, optional

        If `seed` is None (or `np.random`), the `numpy.random.RandomState`
        singleton is used.
        If `seed` is an int, a new ``RandomState`` instance is used,
        seeded with `seed`.
        If `seed` is already a ``Generator`` or ``RandomState`` instance
        then that instance is used.

    Notes
    -----
    As this function does no argument checking, it should not be
    called directly; use 'rvs' instead.

    """
    # Random normal variates for off-diagonal elements
    n_tril = dim * (dim-1) // 2
    covariances = random_state.normal(
        size=n*n_tril).reshape(shape+(n_tril,))

    # Random chi-square variates for diagonal elements
    variances = (np.r_[[random_state.chisquare(df-(i+1)+1, size=n)**0.5
                        for i in range(dim)]].reshape((dim,) +
                                                      shape[::-1]).T)

    # Create the A matri(ces) - lower triangular
    A = np.zeros(shape + (dim, dim))

    # Input the covariances
    size_idx = tuple([slice(None, None, None)]*len(shape))
    tril_idx = np.tril_indices(dim, k=-1)
    A[size_idx + tril_idx] = covariances

    # Input the variances
    diag_idx = np.diag_indices(dim)
    A[size_idx + diag_idx] = variances

    return A


# ==================================================
# Line: 2434

def _entropy(self, dim, df, log_det_scale):
    """Compute the differential entropy of the Wishart.

    Parameters
    ----------
    dim : int
        Dimension of the scale matrix
    df : int
        Degrees of freedom
    log_det_scale : float
        Logarithm of the determinant of the scale matrix

    Notes
    -----
    As this function does no argument checking, it should not be
    called directly; use 'entropy' instead.

    """
    return (
        0.5 * (dim+1) * log_det_scale +
        0.5 * dim * (dim+1) * _LOG_2 +
        multigammaln(0.5*df, dim) -
        0.5 * (df - dim - 1) * np.sum(
            [psi(0.5*(df + 1 - (i+1))) for i in range(dim)]
        ) +
        0.5 * df * dim
    )


# ==================================================
# Line: 2483

def _cholesky_logdet(self, scale):
    """Compute Cholesky decomposition and determine (log(det(scale)).

    Parameters
    ----------
    scale : ndarray
        Scale matrix.

    Returns
    -------
    c_decomp : ndarray
        The Cholesky decomposition of `scale`.
    logdet : scalar
        The log of the determinant of `scale`.

    Notes
    -----
    This computation of ``logdet`` is equivalent to
    ``np.linalg.slogdet(scale)``.  It is ~2x faster though.

    """
    c_decomp = scipy.linalg.cholesky(scale, lower=True)
    logdet = 2 * np.sum(np.log(c_decomp.diagonal()))
    return c_decomp, logdet



# ==================================================
# Line: 2915

def _inv_standard_rvs(self, n, shape, dim, df, random_state):
    """
    Parameters
    ----------
    n : integer
        Number of variates to generate
    shape : iterable
        Shape of the variates to generate
    dim : int
        Dimension of the scale matrix
    df : int
        Degrees of freedom
    random_state : {None, int, `numpy.random.Generator`,
                    `numpy.random.RandomState`}, optional

        If `seed` is None (or `np.random`), the `numpy.random.RandomState`
        singleton is used.
        If `seed` is an int, a new ``RandomState`` instance is used,
        seeded with `seed`.
        If `seed` is already a ``Generator`` or ``RandomState`` instance
        then that instance is used.

    Returns
    -------
    A : ndarray
        Random variates of shape (`shape`) + (``dim``, ``dim``).
        Each slice `A[..., :, :]` is lower-triangular, and its
        inverse is the lower Cholesky factor of a draw from
        `invwishart(df, np.eye(dim))`.

    Notes
    -----
    As this function does no argument checking, it should not be
    called directly; use 'rvs' instead.

    """
    A = np.zeros(shape + (dim, dim))

    # Random normal variates for off-diagonal elements
    tri_rows, tri_cols = np.tril_indices(dim, k=-1)
    n_tril = dim * (dim-1) // 2
    A[..., tri_rows, tri_cols] = random_state.normal(
        size=(*shape, n_tril),
    )

    # Random chi variates for diagonal elements
    rows = np.arange(dim)
    chi_dfs = (df - dim + 1) + rows
    A[..., rows, rows] = random_state.chisquare(
        df=chi_dfs, size=(*shape, dim),
    )**0.5

    return A


# ==================================================
# Line: 3279

def _process_parameters(self, n, p):
    """Returns: n_, p_, npcond.

    n_ and p_ are arrays of the correct shape; npcond is a boolean array
    flagging values out of the domain.
    """
    eps = np.finfo(np.result_type(np.asarray(p), np.float32)).eps * 10
    p = np.array(p, dtype=np.float64, copy=True)
    p_adjusted = 1. - p[..., :-1].sum(axis=-1)
    # only make adjustment when it's significant
    i_adjusted = np.abs(1 - p.sum(axis=-1)) > eps
    p[i_adjusted, -1] = p_adjusted[i_adjusted]

    if np.any(i_adjusted):
        message = ("Some rows of `p` do not sum to 1.0 within tolerance of "
                   f"{eps=}. Currently, the last element of these rows is adjusted "
                   "to compensate, but this condition will produce NaNs "
                   "beginning in SciPy 1.18.0. Please ensure that rows of `p` sum "
                   "to 1.0 to avoid futher disruption.")
        warnings.warn(message, FutureWarning, stacklevel=3)

    # true for bad p
    pcond = np.any(p < 0, axis=-1)
    pcond |= np.any(p > 1, axis=-1)

    n = np.array(n, dtype=int, copy=True)

    # true for bad n
    ncond = n < 0

    return n, p, ncond | pcond


# ==================================================
# Line: 3311

def _process_quantiles(self, x, n, p):
    """Returns: x_, xcond.

    x_ is an int array; xcond is a boolean array flagging values out of the
    domain.
    """
    xx = np.asarray(x, dtype=int)

    if xx.ndim == 0:
        raise ValueError("x must be an array.")

    if xx.size != 0 and not xx.shape[-1] == p.shape[-1]:
        raise ValueError(f"Size of each quantile should be size of p: "
                         f"received {xx.shape[-1]}, but expected "
                         f"{p.shape[-1]}.")

    # true for x out of the domain
    cond = np.any(xx != x, axis=-1)
    cond |= np.any(xx < 0, axis=-1)
    cond = cond | (np.sum(xx, axis=-1) != n)

    return xx, cond


# ==================================================
# Line: 3334

def _checkresult(self, result, cond, bad_value):
    result = np.asarray(result)

    if cond.ndim != 0:
        result[cond] = bad_value
    elif cond:
        if result.ndim == 0:
            return bad_value
        result[...] = bad_value
    return result


# ==================================================
# Line: 3345

def _logpmf(self, x, n, p):
    return gammaln(n+1) + np.sum(xlogy(x, p) - gammaln(x+1), axis=-1)


# ==================================================
# Line: 3640

def _process_parameters(self, dim):
    """Dimension N must be specified; it cannot be inferred."""
    if dim is None or not np.isscalar(dim) or dim < 0 or dim != int(dim):
        raise ValueError("""Dimension of rotation must be specified,
                            and must be a scalar nonnegative integer.""")

    return dim


# ==================================================
# Line: 3783

def _process_parameters(self, dim):
    """Dimension N must be specified; it cannot be inferred."""
    if dim is None or not np.isscalar(dim) or dim < 0 or dim != int(dim):
        raise ValueError("Dimension of rotation must be specified,"
                         "and must be a scalar nonnegative integer.")

    return dim


# ==================================================
# Line: 3948

def _process_parameters(self, eigs, tol):
    eigs = np.asarray(eigs, dtype=float)
    dim = eigs.size

    if eigs.ndim != 1 or eigs.shape[0] != dim or dim <= 1:
        raise ValueError("Array 'eigs' must be a vector of length "
                         "greater than 1.")

    if np.fabs(np.sum(eigs) - dim) > tol:
        raise ValueError("Sum of eigenvalues must equal dimensionality.")

    for x in eigs:
        if x < -tol:
            raise ValueError("All eigenvalues must be non-negative.")

    return dim, eigs


# ==================================================
# Line: 3965

def _givens_to_1(self, aii, ajj, aij):
    """Computes a 2x2 Givens matrix to put 1's on the diagonal.

    The input matrix is a 2x2 symmetric matrix M = [ aii aij ; aij ajj ].

    The output matrix g is a 2x2 anti-symmetric matrix of the form
    [ c s ; -s c ];  the elements c and s are returned.

    Applying the output matrix to the input matrix (as b=g.T M g)
    results in a matrix with bii=1, provided tr(M) - det(M) >= 1
    and floating point issues do not occur. Otherwise, some other
    valid rotation is returned. When tr(M)==2, also bjj=1.

    """
    aiid = aii - 1.
    ajjd = ajj - 1.

    if ajjd == 0:
        # ajj==1, so swap aii and ajj to avoid division by zero
        return 0., 1.

    dd = math.sqrt(max(aij**2 - aiid*ajjd, 0))

    # The choice of t should be chosen to avoid cancellation [1]
    t = (aij + math.copysign(dd, aij)) / ajjd
    c = 1. / math.sqrt(1. + t*t)
    if c == 0:
        # Underflow
        s = 1.0
    else:
        s = c*t
    return c, s


# ==================================================
# Line: 4197

def _process_parameters(self, dim):
    """Dimension N must be specified; it cannot be inferred."""
    if dim is None or not np.isscalar(dim) or dim < 0 or dim != int(dim):
        raise ValueError("Dimension of rotation must be specified,"
                         "and must be a scalar nonnegative integer.")

    return dim


# ==================================================
# Line: 4482

def _logpdf(self, x, loc, prec_U, log_pdet, df, dim, rank):
    """Utility method `pdf`, `logpdf` for parameters.

    Parameters
    ----------
    x : ndarray
        Points at which to evaluate the log of the probability density
        function.
    loc : ndarray
        Location of the distribution.
    prec_U : ndarray
        A decomposition such that `np.dot(prec_U, prec_U.T)` is the inverse
        of the shape matrix.
    log_pdet : float
        Logarithm of the determinant of the shape matrix.
    df : float
        Degrees of freedom of the distribution.
    dim : int
        Dimension of the quantiles x.
    rank : int
        Rank of the shape matrix.

    Notes
    -----
    As this function does no argument checking, it should not be called
    directly; use 'logpdf' instead.

    """
    if df == np.inf:
        return multivariate_normal._logpdf(x, loc, prec_U, log_pdet, rank)

    dev = x - loc
    maha = np.square(np.dot(dev, prec_U)).sum(axis=-1)

    t = 0.5 * (df + dim)
    A = gammaln(t)
    B = gammaln(0.5 * df)
    C = dim/2. * np.log(df * np.pi)
    D = 0.5 * log_pdet
    E = -t * np.log(1 + (1./df) * maha)

    return _squeeze_output(A - B - C - D + E)


# ==================================================
# Line: 4603

def _entropy(self, dim, df=1, shape=1):
    if df == np.inf:
        return multivariate_normal(None, cov=shape).entropy()

    shape_info = _PSD(shape)
    shape_term = 0.5 * shape_info.log_pdet

    def regular(dim, df):
        halfsum = 0.5 * (dim + df)
        half_df = 0.5 * df
        return (
            -gammaln(halfsum) + gammaln(half_df)
            + 0.5 * dim * np.log(df * np.pi) + halfsum
            * (psi(halfsum) - psi(half_df))
            + shape_term
        )

    def asymptotic(dim, df):
        # Formula from Wolfram Alpha:
        # "asymptotic expansion -gammaln((m+d)/2) + gammaln(d/2) + (m*log(d*pi))/2
        #  + ((m+d)/2) * (digamma((m+d)/2) - digamma(d/2))"
        return (
            dim * norm._entropy() + dim / df
            - dim * (dim - 2) * df**-2.0 / 4
            + dim**2 * (dim - 2) * df**-3.0 / 6
            + dim * (-3 * dim**3 + 8 * dim**2 - 8) * df**-4.0 / 24
            + dim**2 * (3 * dim**3 - 10 * dim**2 + 16) * df**-5.0 / 30
            + shape_term
        )[()]

    # preserves ~12 digits accuracy up to at least `dim=1e5`. See gh-18465.
    threshold = dim * 100 * 4 / (np.log(dim) + 1)
    return xpx.apply_where(df >= threshold, (dim, df), asymptotic, regular)


# ==================================================
# Line: 4701

def _process_quantiles(self, x, dim):
    """
    Adjust quantiles array so that last axis labels the components of
    each data point.
    """
    x = np.asarray(x, dtype=float)
    if x.ndim == 0:
        x = x[np.newaxis]
    elif x.ndim == 1:
        if dim == 1:
            x = x[:, np.newaxis]
        else:
            x = x[np.newaxis, :]
    return x


# ==================================================
# Line: 4716

def _process_parameters(self, loc, shape, df):
    """
    Infer dimensionality from location array and shape matrix, handle
    defaults, and ensure compatible dimensions.
    """
    if loc is None and shape is None:
        loc = np.asarray(0, dtype=float)
        shape = np.asarray(1, dtype=float)
        dim = 1
    elif loc is None:
        shape = np.asarray(shape, dtype=float)
        if shape.ndim < 2:
            dim = 1
        else:
            dim = shape.shape[0]
        loc = np.zeros(dim)
    elif shape is None:
        loc = np.asarray(loc, dtype=float)
        dim = loc.size
        shape = np.eye(dim)
    else:
        shape = np.asarray(shape, dtype=float)
        loc = np.asarray(loc, dtype=float)
        dim = loc.size

    if dim == 1:
        loc = loc.reshape(1)
        shape = shape.reshape(1, 1)

    if loc.ndim != 1 or loc.shape[0] != dim:
        raise ValueError(f"Array 'loc' must be a vector of length {dim}.")
    if shape.ndim == 0:
        shape = shape * np.eye(dim)
    elif shape.ndim == 1:
        shape = np.diag(shape)
    elif shape.ndim == 2 and shape.shape != (dim, dim):
        rows, cols = shape.shape
        if rows != cols:
            msg = ("Array 'cov' must be square if it is two dimensional,"
                   f" but cov.shape = {str(shape.shape)}.")
        else:
            msg = ("Dimension mismatch: array 'cov' is of shape %s,"
                   " but 'loc' is a vector of length %d.")
            msg = msg % (str(shape.shape), len(loc))
        raise ValueError(msg)
    elif shape.ndim > 2:
        raise ValueError(f"Array 'cov' must be at most two-dimensional, "
                         f"but cov.ndim = {shape.ndim}")

    # Process degrees of freedom.
    if df is None:
        df = 1
    elif df <= 0:
        raise ValueError("'df' must be greater than zero.")
    elif np.isnan(df):
        raise ValueError("'df' is 'nan' but must be greater than zero or 'np.inf'.")

    return dim, loc, shape, df



# ==================================================
# Line: 5005

def _process_parameters(self, m, n):
    m = np.asarray(m)
    n = np.asarray(n)
    if m.size == 0:
        m = m.astype(int)
    if n.size == 0:
        n = n.astype(int)
    if not np.issubdtype(m.dtype, np.integer):
        raise TypeError("'m' must an array of integers.")
    if not np.issubdtype(n.dtype, np.integer):
        raise TypeError("'n' must an array of integers.")
    if m.ndim == 0:
        raise ValueError("'m' must be an array with"
                         " at least one dimension.")

    # check for empty arrays
    if m.size != 0:
        n = n[..., np.newaxis]

    m, n = np.broadcast_arrays(m, n)

    # check for empty arrays
    if m.size != 0:
        n = n[..., 0]

    mcond = m < 0

    M = m.sum(axis=-1)

    ncond = (n < 0) | (n > M)
    return M, m, n, mcond, ncond, np.any(mcond, axis=-1) | ncond


# ==================================================
# Line: 5037

def _process_quantiles(self, x, M, m, n):
    x = np.asarray(x)
    if not np.issubdtype(x.dtype, np.integer):
        raise TypeError("'x' must an array of integers.")
    if x.ndim == 0:
        raise ValueError("'x' must be an array with"
                         " at least one dimension.")
    if not x.shape[-1] == m.shape[-1]:
        raise ValueError(f"Size of each quantile must be size of 'm': "
                         f"received {x.shape[-1]}, "
                         f"but expected {m.shape[-1]}.")

    # check for empty arrays
    if m.size != 0:
        n = n[..., np.newaxis]
        M = M[..., np.newaxis]

    x, m, n, M = np.broadcast_arrays(x, m, n, M)

    # check for empty arrays
    if m.size != 0:
        n, M = n[..., 0], M[..., 0]

    xcond = (x < 0) | (x > m)
    return (x, M, m, n, xcond,
            np.any(xcond, axis=-1) | (x.sum(axis=-1) != n))


# ==================================================
# Line: 5064

def _checkresult(self, result, cond, bad_value):
    result = np.asarray(result)
    if cond.ndim != 0:
        result[cond] = bad_value
    elif cond:
        return bad_value
    if result.ndim == 0:
        return result[()]
    return result


# ==================================================
# Line: 5074

def _logpmf(self, x, M, m, n, mxcond, ncond):
    # This equation of the pmf comes from the relation,
    # n combine r = beta(n+1, 1) / beta(r+1, n-r+1)
    num = np.zeros_like(m, dtype=np.float64)
    den = np.zeros_like(n, dtype=np.float64)
    m, x = m[~mxcond], x[~mxcond]
    M, n = M[~ncond], n[~ncond]
    num[~mxcond] = (betaln(m+1, 1) - betaln(x+1, m-x+1))
    den[~ncond] = (betaln(M+1, 1) - betaln(n+1, M-n+1))
    num[mxcond] = np.nan
    den[ncond] = np.nan
    num = num.sum(axis=-1)
    return num - den


# ==================================================
# Line: 5846

def _process_parameters(self, dim):
    """Dimension N must be specified; it cannot be inferred."""
    if dim is None or not np.isscalar(dim) or dim < 1 or dim != int(dim):
        raise ValueError("Dimension of vector must be specified, "
                         "and must be an integer greater than 0.")

    return int(dim)


# ==================================================
# Line: 6116

def logpmf(self, x, alpha, n):
    """The log of the probability mass function.

    Parameters
    ----------
    x: ndarray
        Category counts (non-negative integers). Must be broadcastable
        with shape parameter ``alpha``. If multidimensional, the last axis
        must correspond with the categories.
    %(_dirichlet_mn_doc_default_callparams)s

    Returns
    -------
    out: ndarray or scalar
        Log of the probability mass function.

    """

    a, Sa, n, x = _dirichlet_multinomial_check_parameters(alpha, n, x)

    out = np.asarray(loggamma(Sa) + loggamma(n + 1) - loggamma(n + Sa))
    out += (loggamma(x + a) - (loggamma(a) + loggamma(x + 1))).sum(axis=-1)
    np.place(out, n != x.sum(axis=-1), -np.inf)
    return out[()]


# ==================================================
# Line: 6160

def mean(self, alpha, n):
    """Mean of a Dirichlet multinomial distribution.

    Parameters
    ----------
    %(_dirichlet_mn_doc_default_callparams)s

    Returns
    -------
    out: ndarray
        Mean of a Dirichlet multinomial distribution.

    """
    a, Sa, n = _dirichlet_multinomial_check_parameters(alpha, n)
    n, Sa = n[..., np.newaxis], Sa[..., np.newaxis]
    return n * a / Sa


# ==================================================
# Line: 6177

def var(self, alpha, n):
    """The variance of the Dirichlet multinomial distribution.

    Parameters
    ----------
    %(_dirichlet_mn_doc_default_callparams)s

    Returns
    -------
    out: array_like
        The variances of the components of the distribution. This is
        the diagonal of the covariance matrix of the distribution.

    """
    a, Sa, n = _dirichlet_multinomial_check_parameters(alpha, n)
    n, Sa = n[..., np.newaxis], Sa[..., np.newaxis]
    return n * a / Sa * (1 - a/Sa) * (n + Sa) / (1 + Sa)


# ==================================================
# Line: 6195

def cov(self, alpha, n):
    """Covariance matrix of a Dirichlet multinomial distribution.

    Parameters
    ----------
    %(_dirichlet_mn_doc_default_callparams)s

    Returns
    -------
    out : array_like
        The covariance matrix of the distribution.

    """
    a, Sa, n = _dirichlet_multinomial_check_parameters(alpha, n)
    var = dirichlet_multinomial.var(a, n)

    n, Sa = n[..., np.newaxis, np.newaxis], Sa[..., np.newaxis, np.newaxis]
    aiaj = a[..., :, np.newaxis] * a[..., np.newaxis, :]
    cov = -n * aiaj / Sa ** 2 * (n + Sa) / (1 + Sa)

    ii = np.arange(cov.shape[-1])
    cov[..., ii, ii] = var
    return cov



# ==================================================
# Line: 6478

def _process_parameters(self, mu, kappa):
    """
    Infer dimensionality from mu and ensure that mu is a one-dimensional
    unit vector and kappa positive.
    """
    mu = np.asarray(mu)
    if mu.ndim > 1:
        raise ValueError("'mu' must have one-dimensional shape.")
    if not np.allclose(np.linalg.norm(mu), 1.):
        raise ValueError("'mu' must be a unit vector of norm 1.")
    if not mu.size > 1:
        raise ValueError("'mu' must have at least two entries.")
    kappa_error_msg = "'kappa' must be a positive scalar."
    if not np.isscalar(kappa) or kappa < 0:
        raise ValueError(kappa_error_msg)
    if float(kappa) == 0.:
        raise ValueError("For 'kappa=0' the von Mises-Fisher distribution "
                         "becomes the uniform distribution on the sphere "
                         "surface. Consider using "
                         "'scipy.stats.uniform_direction' instead.")
    dim = mu.size

    return dim, mu, kappa


# ==================================================
# Line: 6502

def _check_data_vs_dist(self, x, dim):
    if x.shape[-1] != dim:
        raise ValueError("The dimensionality of the last axis of 'x' must "
                         "match the dimensionality of the "
                         "von Mises Fisher distribution.")
    if not np.allclose(np.linalg.norm(x, axis=-1), 1.):
        msg = "'x' must be unit vectors of norm 1 along last dimension."
        raise ValueError(msg)


# ==================================================
# Line: 6511

def _log_norm_factor(self, dim, kappa):
    # normalization factor is given by
    # c = kappa**(dim/2-1)/((2*pi)**(dim/2)*I[dim/2-1](kappa))
    #   = kappa**(dim/2-1)*exp(-kappa) /
    #     ((2*pi)**(dim/2)*I[dim/2-1](kappa)*exp(-kappa)
    #   = kappa**(dim/2-1)*exp(-kappa) /
    #     ((2*pi)**(dim/2)*ive[dim/2-1](kappa)
    # Then the log is given by
    # log c = 1/2*(dim -1)*log(kappa) - kappa - -1/2*dim*ln(2*pi) -
    #         ive[dim/2-1](kappa)
    halfdim = 0.5 * dim
    return (0.5 * (dim - 2)*np.log(kappa) - halfdim * _LOG_2PI -
            np.log(ive(halfdim - 1, kappa)) - kappa)


# ==================================================
# Line: 6585

def _rvs_2d(self, mu, kappa, size, random_state):
    """
    In 2D, the von Mises-Fisher distribution reduces to the
    von Mises distribution which can be efficiently sampled by numpy.
    This method is much faster than the general rejection
    sampling based algorithm.

    """
    mean_angle = np.arctan2(mu[1], mu[0])
    angle_samples = random_state.vonmises(mean_angle, kappa, size=size)
    samples = np.stack([np.cos(angle_samples), np.sin(angle_samples)],
                       axis=-1)
    return samples


# ==================================================
# Line: 6599

def _rvs_3d(self, kappa, size, random_state):
    """
    Generate samples from a von Mises-Fisher distribution
    with mu = [1, 0, 0] and kappa. Samples then have to be
    rotated towards the desired mean direction mu.
    This method is much faster than the general rejection
    sampling based algorithm.
    Reference: https://www.mitsuba-renderer.org/~wenzel/files/vmf.pdf

    """
    if size is None:
        sample_size = 1
    else:
        sample_size = size

    # compute x coordinate acc. to equation from section 3.1
    x = random_state.random(sample_size)
    x = 1. + np.log(x + (1. - x) * np.exp(-2 * kappa))/kappa

    # (y, z) are random 2D vectors that only have to be
    # normalized accordingly. Then (x, y z) follow a VMF distribution
    temp = np.sqrt(1. - np.square(x))
    uniformcircle = _sample_uniform_direction(2, sample_size, random_state)
    samples = np.stack([x, temp * uniformcircle[..., 0],
                        temp * uniformcircle[..., 1]],
                       axis=-1)
    if size is None:
        samples = np.squeeze(samples)
    return samples


# ==================================================
# Line: 6629

def _rejection_sampling(self, dim, kappa, size, random_state):
    """
    Generate samples from a n-dimensional von Mises-Fisher distribution
    with mu = [1, 0, ..., 0] and kappa via rejection sampling.
    Samples then have to be rotated towards the desired mean direction mu.
    Reference: https://doi.org/10.1080/03610919408813161
    """
    dim_minus_one = dim - 1
    # calculate number of requested samples
    if size is not None:
        if not np.iterable(size):
            size = (size, )
        n_samples = math.prod(size)
    else:
        n_samples = 1
    # calculate envelope for rejection sampler (eq. 4)
    sqrt = np.sqrt(4 * kappa ** 2. + dim_minus_one ** 2)
    envelop_param = (-2 * kappa + sqrt) / dim_minus_one
    if envelop_param == 0:
        # the regular formula suffers from loss of precision for high
        # kappa. This can only be detected by checking for 0 here.
        # Workaround: expansion for sqrt variable
        # https://www.wolframalpha.com/input?i=sqrt%284*x%5E2%2Bd%5E2%29
        # e = (-2 * k + sqrt(k**2 + d**2)) / d
        #   ~ (-2 * k + 2 * k + d**2/(4 * k) - d**4/(64 * k**3)) / d
        #   = d/(4 * k) - d**3/(64 * k**3)
        envelop_param = (dim_minus_one/4 * kappa**-1.
                         - dim_minus_one**3/64 * kappa**-3.)
    # reference step 0
    node = (1. - envelop_param) / (1. + envelop_param)
    # t = ln(1 - ((1-x)/(1+x))**2)
    #   = ln(4 * x / (1+x)**2)
    #   = ln(4) + ln(x) - 2*log1p(x)
    correction = (kappa * node + dim_minus_one
                  * (np.log(4) + np.log(envelop_param)
                  - 2 * np.log1p(envelop_param)))
    n_accepted = 0
    x = np.zeros((n_samples, ))
    halfdim = 0.5 * dim_minus_one
    # main loop
    while n_accepted < n_samples:
        # generate candidates acc. to reference step 1
        sym_beta = random_state.beta(halfdim, halfdim,
                                     size=n_samples - n_accepted)
        coord_x = (1 - (1 + envelop_param) * sym_beta) / (
            1 - (1 - envelop_param) * sym_beta)
        # accept or reject: reference step 2
        # reformulation for numerical stability:
        # t = ln(1 - (1-x)/(1+x) * y)
        #   = ln((1 + x - y +x*y)/(1 +x))
        accept_tol = random_state.random(n_samples - n_accepted)
        criterion = (
            kappa * coord_x
            + dim_minus_one * (np.log((1 + envelop_param - coord_x
            + coord_x * envelop_param) / (1 + envelop_param)))
            - correction) > np.log(accept_tol)
        accepted_iter = np.sum(criterion)
        x[n_accepted:n_accepted + accepted_iter] = coord_x[criterion]
        n_accepted += accepted_iter
    # concatenate x and remaining coordinates: step 3
    coord_rest = _sample_uniform_direction(dim_minus_one, n_accepted,
                                           random_state)
    coord_rest = np.einsum(
        '...,...i->...i', np.sqrt(1 - x ** 2), coord_rest)
    samples = np.concatenate([x[..., None], coord_rest], axis=1)
    # reshape output to (size, dim)
    if size is not None:
        samples = samples.reshape(size + (dim, ))
    else:
        samples = np.squeeze(samples)
    return samples


# ==================================================
# Line: 6701

def _rotate_samples(self, samples, mu, dim):
    """A QR decomposition is used to find the rotation that maps the
    north pole (1, 0,...,0) to the vector mu. This rotation is then
    applied to all samples.

    Parameters
    ----------
    samples: array_like, shape = [..., n]
    mu : array-like, shape=[n, ]
        Point to parametrise the rotation.

    Returns
    -------
    samples : rotated samples

    """
    base_point = np.zeros((dim, ))
    base_point[0] = 1.
    embedded = np.concatenate([mu[None, :], np.zeros((dim - 1, dim))])
    rotmatrix, _ = np.linalg.qr(np.transpose(embedded))
    if np.allclose(np.matmul(rotmatrix, base_point[:, None])[:, 0], mu):
        rotsign = 1
    else:
        rotsign = -1

    # apply rotation
    samples = np.einsum('ij,...j->...i', rotmatrix, samples) * rotsign
    return samples


# ==================================================
# Line: 6807

def fit(self, x):
    """Fit the von Mises-Fisher distribution to data.

    Parameters
    ----------
    x : array-like
        Data the distribution is fitted to. Must be two dimensional.
        The second axis of `x` must be unit vectors of norm 1 and
        determine the dimensionality of the fitted
        von Mises-Fisher distribution.

    Returns
    -------
    mu : ndarray
        Estimated mean direction.
    kappa : float
        Estimated concentration parameter.

    """
    # validate input data
    x = np.asarray(x)
    if x.ndim != 2:
        raise ValueError("'x' must be two dimensional.")
    if not np.allclose(np.linalg.norm(x, axis=-1), 1.):
        msg = "'x' must be unit vectors of norm 1 along last dimension."
        raise ValueError(msg)
    dim = x.shape[-1]

    # mu is simply the directional mean
    dirstats = directional_stats(x)
    mu = dirstats.mean_direction
    r = dirstats.mean_resultant_length

    # kappa is the solution to the equation:
    # r = I[dim/2](kappa) / I[dim/2 -1](kappa)
    #   = I[dim/2](kappa) * exp(-kappa) / I[dim/2 -1](kappa) * exp(-kappa)
    #   = ive(dim/2, kappa) / ive(dim/2 -1, kappa)

    halfdim = 0.5 * dim

    def solve_for_kappa(kappa):
        bessel_vals = ive([halfdim, halfdim - 1], kappa)
        return bessel_vals[0]/bessel_vals[1] - r

    root_res = root_scalar(solve_for_kappa, method="brentq",
                           bracket=(1e-8, 1e9))
    kappa = root_res.root
    return mu, kappa



# ==================================================
# Line: 7113

def _logpdf(self, x, s2, mu, lmbda, a, b):
    t1 = 0.5 * (np.log(lmbda) - np.log(2 * np.pi * s2))
    t2 = a*np.log(b) - special.gammaln(a).astype(a.dtype)
    t3 = -(a + 1) * np.log(s2)
    t4 = -(2*b + lmbda*(x - mu)**2) / (2*s2)
    return t1 + t2 + t3 + t4


# ==================================================
# Line: 7146

def _pdf(self, x, s2, mu, lmbda, a, b):
    t1 = np.sqrt(lmbda / (2 * np.pi * s2))
    t2 = b**a / special.gamma(a).astype(a.dtype)
    t3 = (1 / s2)**(a + 1)
    t4 = np.exp(-(2*b + lmbda*(x - mu)**2) / (2*s2))
    return t1 * t2 * t3 * t4


# ==================================================
# Line: 7229

def _process_parameters_pdf(self, x, s2, mu, lmbda, a, b):
    args = np.broadcast_arrays(x, s2, mu, lmbda, a, b)
    dtype = np.result_type(1.0, *(arg.dtype for arg in args))
    args = [arg.astype(dtype, copy=False) for arg in args]
    x, s2, mu, lmbda, a, b = args
    invalid = ~((lmbda > 0) & (a > 0) & (b > 0))
    return invalid, args


# ==================================================
# Line: 7237

def _process_shapes(self, mu, lmbda, a, b):
    args = np.broadcast_arrays(mu, lmbda, a, b)
    dtype = np.result_type(1.0, *(arg.dtype for arg in args))
    args = [arg.astype(dtype, copy=False) for arg in args]
    mu, lmbda, a, b = args
    invalid = ~((lmbda > 0) & (a > 0) & (b > 0))
    return invalid, args


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_distribution_infrastructure.py
# Line: 1779

def _validate(self, parameterization, parameters):
    # Broadcasts distribution parameter arrays and converts them to a
    # consistent dtype. Replaces invalid parameters with `np.nan`.
    # Returns the validated parameters, a boolean mask indicated *which*
    # elements are invalid, a boolean scalar indicating whether *any*
    # are invalid (to skip special treatments if none are invalid), and
    # the common dtype.
    valid, dtype = parameterization.validation(parameters)
    invalid = ~valid
    any_invalid = invalid if invalid.shape == () else np.any(invalid)
    # If necessary, make the arrays contiguous and replace invalid with NaN
    if any_invalid:
        for parameter_name in parameters:
            parameters[parameter_name] = np.copy(
                parameters[parameter_name])
            parameters[parameter_name][invalid] = np.nan

    return parameters, invalid, any_invalid, dtype


# ==================================================
# Line: 1798

def _process_parameters(self, **params):
    r""" Process and cache distribution parameters for reuse.

    This is intended to be overridden by subclasses. It allows distribution
    authors to pre-process parameters for re-use. For instance, when a user
    parameterizes a LogUniform distribution with `a` and `b`, it makes
    sense to calculate `log(a)` and `log(b)` because these values will be
    used in almost all distribution methods. The dictionary returned by
    this method is passed to all private methods that calculate functions
    of the distribution.
    """
    return params


# ==================================================
# Line: 1811

def _get_parameter_str(self, parameters):
    # Get a string representation of the parameters like "{a, b, c}".
    return f"{{{', '.join(parameters.keys())}}}"


# ==================================================
# Line: 3179

def _moment_raw_formula(self, order, **params):
    return None


# ==================================================
# Line: 3244

def _moment_central_formula(self, order, **params):
    return None


# ==================================================
# Line: 3305

def _moment_standardized_formula(self, order, **params):
    return None


# ==================================================
# Occurrences: Lines 4613-4616 (2 instances)

def _transform(self, x, loc, scale, **kwargs):
    return (x - loc)/scale


# ==================================================
# Line: 5127

def _input_validation(self, components, weights):
    if len(components) == 0:
        message = ("`components` must contain at least one random variable.")
        raise ValueError(message)

    for var in components:
        # will generalize to other kinds of distributions when there
        # *are* other kinds of distributions
        if not isinstance(var, ContinuousDistribution):
            message = ("Each element of `components` must be an instance of "
                       "`ContinuousDistribution`.")
            raise ValueError(message)
        if not var._shape == ():
            message = "All elements of `components` must have scalar shapes."
            raise ValueError(message)

    if weights is None:
        return components, weights

    weights = np.asarray(weights)
    if weights.shape != (len(components),):
        message = "`components` and `weights` must have the same length."
        raise ValueError(message)

    if not np.issubdtype(weights.dtype, np.inexact):
        message = "`weights` must have floating point dtype."
        raise ValueError(message)

    if not np.isclose(np.sum(weights), 1.0):
        message = "`weights` must sum to 1.0."
        raise ValueError(message)

    if not np.all(weights >= 0):
        message = "All `weights` must be non-negative."
        raise ValueError(message)

    return components, weights


# ==================================================
# Line: 5208

def _raise_if_method(self, method):
    if method is not None:
        raise NotImplementedError("`method` not implemented for this distribution.")


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_fit.py
# Line: 289

def _plotting_positions(self, n, a=.5):
    # See https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot#Plotting_positions
    k = np.arange(1, n+1)
    return (k-a) / (n + 1 - 2*a)


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_levy_stable/__init__.py
# Line: 819

def _shape_info(self):
    ialpha = _ShapeInfo("alpha", False, (0, 2), (False, True))
    ibeta = _ShapeInfo("beta", False, (-1, 1), (True, True))
    return [ialpha, ibeta]


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_covariance.py
# Line: 443

def _validate_matrix(self, A, name):
    A = np.atleast_2d(A)
    m, n = A.shape[-2:]
    if m != n or A.ndim != 2 or not (np.issubdtype(A.dtype, np.integer) or
                                     np.issubdtype(A.dtype, np.floating)):
        message = (f"The input `{name}` must be a square, "
                   "two-dimensional array of real numbers.")
        raise ValueError(message)
    return A


# ==================================================
# Line: 453

def _validate_vector(self, A, name):
    A = np.atleast_1d(A)
    if A.ndim != 1 or not (np.issubdtype(A.dtype, np.integer) or
                           np.issubdtype(A.dtype, np.floating)):
        message = (f"The input `{name}` must be a one-dimensional array "
                   "of real numbers.")
        raise ValueError(message)
    return A



# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_rgi.py
# Occurrences: Lines 315-321 (3 instances)

def _check_dimensionality(self, grid, values):
    _check_dimensionality(grid, values)


# ==================================================
# Line: 332

def _check_fill_value(self, values, fill_value):
    if fill_value is not None:
        fill_value_dtype = np.asarray(fill_value).dtype
        if (hasattr(values, 'dtype') and not
                np.can_cast(fill_value_dtype, values.dtype,
                            casting='same_kind')):
            raise ValueError("fill_value must be either 'None' or "
                             "of a type compatible with values")
    return fill_value


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_polyint.py
# Line: 91

def _prepare_x(self, x):
    """Reshape input x array to 1-D"""
    x = _asarray_validated(x, check_finite=False, as_inexact=True)
    x_shape = x.shape
    return x.ravel(), x_shape


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_rbf.py
# Occurrences: Lines 160-169 (4 instances)

def _h_linear(self, r):
    return r


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_bary_rational.py
# Line: 65

def _input_validation(self, x, y, **kwargs):
    if x.ndim != 1:
        raise ValueError("`x` must be 1-D.")

    if not y.ndim >= 1:
        raise ValueError("`y` must be at least 1-D.")

    if x.size != y.shape[0]:
        raise ValueError("`x` be the same size as the first dimension of `y`.")

    if not np.all(np.isfinite(x)):
        raise ValueError("`x` must be finite.")


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_fitpack2.py
# Line: 331

def _reset_nest(self, data, nest=None):
    n = data[10]
    if nest is None:
        k, m = data[5], len(data[0])
        nest = m+k+1  # this is the maximum bound for nest
    else:
        if not n <= nest:
            raise ValueError("`nest` can only be increased")
    t, c, fpint, nrdata = (np.resize(data[j], nest) for j in
                           [8, 9, 11, 12])

    args = data[:8] + (t, c, n, fpint, nrdata, data[13])
    with FITPACK_LOCK:
        data = dfitpack.fpcurf1(*args)
    return data


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_quad_vec.py
# Line: 67

def get_t(self, x):
    s = -1 if x < 0 else 1
    return s / (abs(x) + 1)


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/wavfile.py
# Line: 68

def flush(self):
    raise io.UnsupportedOperation("SeekEmulatingReader can't flush.")



# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/_harwell_boeing/_fortran_format_parser.py
# Line: 255

def _get_min(self, tokens):
    next = tokens.pop(0)
    if not next.type == "DOT":
        raise SyntaxError()
    next = tokens.pop(0)
    return next.value


# ==================================================
# Line: 262

def _expect(self, token, tp):
    if not token.type == tp:
        raise SyntaxError()


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/_fast_matrix_market/__init__.py
# Occurrences: Lines 59-67 (3 instances)

def get_num_threads(self):
    global PARALLELISM
    return PARALLELISM


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/arff/_arffread.py
# Line: 82

def parse_data(self, data_str):
    """
    Parse a value of this type.
    """
    return None


# ==================================================
# Line: 226

def _basic_stats(self, data):
    nbfac = data.size * 1. / (data.size - 1)
    return (np.nanmin(data), np.nanmax(data),
            np.mean(data), np.std(data) * nbfac)



# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/matlab/_miobase.py
# Line: 405

def guess_byte_order(self):
    ''' As we do not know what file type we have, assume native '''
    return boc.native_code


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/odr/_odrpack.py
# Line: 390

def _sd2wt(self, sd):
    """ Convert standard deviation to weights.
    """

    return 1./np.power(sd, 2)


# ==================================================
# Line: 396

def _cov2wt(self, cov):
    """ Convert covariance matrix(-ices) to weights.
    """

    from scipy.linalg import inv

    if len(cov.shape) == 2:
        return inv(cov)
    else:
        weights = np.zeros(cov.shape, float)

        for i in range(cov.shape[-1]):  # n
            weights[:,:,i] = inv(cov[:,:,i])

        return weights


# ==================================================
