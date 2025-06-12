# cached-repeated-calls snippets for numpy

# File: /root/ecooptimizer/numpy/numpy/distutils/from_template.py
# Line: 137

thelist = conv(mobj.group(1).replace(r'\,', '@comma@'))

# ==================================================
# Line: 179

name = mobj.group(1)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/fcompiler/__init__.py
# Occurrences: Lines 815-815 (2 instances)

v = c.get_version()

# ==================================================
# Occurrences: Lines 826-826 (2 instances)

v = c.get_version()

# ==================================================
# Line: 990

line = f.readline()

# ==================================================
# Line: 1004

line = f.readline()

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/fcompiler/gnu.py
# Occurrences: Lines 49-63 (4 instances)

return ('g77', m.group(1))

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/ccompiler.py
# Occurrences: Lines 597-597 (2 instances)

pos = m.end()

# ==================================================
# Occurrences: Lines 603-603 (2 instances)

pos = m.end()

# ==================================================
# Line: 776

msg = str(e)

# ==================================================
# Line: 783

msg = str(e)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/system_info.py
# Occurrences: Lines 811-813 (2 instances)

if sum(found) == 1:

# ==================================================
# Line: 1813

atlas_version = m.group('version')

# ==================================================
# Line: 1832

atlas_version = m.group('version')

# ==================================================
# Occurrences: Lines 2760-2763 (2 instances)

include_dirs.append(sysconfig.get_path('include'))

# ==================================================
# Occurrences: Lines 2836-2846 (3 instances)

msg1 = str(e)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/misc_util.py
# Occurrences: Lines 209-214 (2 instances)

config_file = os.path.join(path, '_numpyconfig.h')

# ==================================================
# Occurrences: Lines 274-274 (2 instances)

p2 = sorted_glob(njoin(local_path, n))

# ==================================================
# Occurrences: Lines 285-285 (2 instances)

n2 = njoin(local_path, n)

# ==================================================
# Occurrences: Lines 625-634 (4 instances)

rpath = rel_path(dpath, top_path)

# ==================================================
# Occurrences: Lines 795-796 (2 instances)

elif os.path.isdir(njoin(self.local_path, package_path)):

# ==================================================
# Occurrences: Lines 1764-1767 (2 instances)

a = getattr(self, key)

# ==================================================
# Line: 1780

% (key, getattr(self, key), dict[key]))

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/command/build_ext.py
# Occurrences: Lines 108-112 (2 instances)

build_clib = self.distribution.get_command_obj(
    'build_clib')

# ==================================================
# Line: 135

self.compiler = new_compiler(compiler=compiler_type,
                             verbose=self.verbose,
                             dry_run=self.dry_run,
                             force=self.force)

# ==================================================
# Line: 273

self._cxx_compiler = new_compiler(compiler=compiler_type,
                                  verbose=self.verbose,
                                  dry_run=self.dry_run,
                                  force=self.force)

# ==================================================
# Line: 546

existing_modules = glob('*.mod')

# ==================================================
# Line: 558

for f in glob('*.mod'):

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/command/config_compiler.py
# Occurrences: Lines 69-69 (2 instances)

v = getattr(c, a)

# ==================================================
# Occurrences: Lines 80-80 (2 instances)

if getattr(c, a) is None: setattr(c, a, v1)

# ==================================================
# Occurrences: Lines 110-110 (2 instances)

v = getattr(c, a)

# ==================================================
# Occurrences: Lines 121-121 (2 instances)

if getattr(c, a) is None: setattr(c, a, v1)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/command/config.py
# Occurrences: Lines 140-140 (2 instances)

libfile = os.path.join(libdir, '%s.lib' % (libname))

# ==================================================
# Occurrences: Lines 152-152 (2 instances)

libfile2 = os.path.join(libdir, '%s.lib' % (libname))

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/command/build_clib.py
# Line: 396

existing_modules = glob('*.mod')

# ==================================================
# Line: 411

for f in glob('*.mod'):

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/command/build_src.py
# Line: 209

generated_dir = os.path.join(template_dir, install_dir)

# ==================================================
# Line: 221

full_install_dir = os.path.join(template_dir, install_dir)

# ==================================================
# Occurrences: Lines 419-421 (4 instances)

target_dir = os.path.dirname(base)

# ==================================================
# Occurrences: Lines 479-481 (4 instances)

target_dir = os.path.dirname(base)

# ==================================================
# Occurrences: Lines 488-488 (2 instances)

target_file = os.path.join(target_dir, name+'module.c')

# ==================================================
# Occurrences: Lines 494-494 (2 instances)

target_file = os.path.join(target_dir, name+'module.c')

# ==================================================
# Occurrences: Lines 500-501 (4 instances)

target_dir = os.path.dirname(base)

# ==================================================
# Occurrences: Lines 633-636 (4 instances)

target_dir = os.path.dirname(base)

# ==================================================
# Occurrences: Lines 645-648 (4 instances)

typ = get_swig_target(source)

# ==================================================
# Occurrences: Lines 669-669 (2 instances)

target_file = _find_swig_target(target_dir, name)

# ==================================================
# Occurrences: Lines 675-676 (4 instances)

target_dir = os.path.dirname(base)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_build_utils/tempita/_tempita.py
# Line: 250

expr = self._eval(expr, ns, pos)

# ==================================================
# Occurrences: Lines 265-269 (2 instances)

result = self._eval(expr, ns, pos)

# ==================================================
# Line: 358

value = value.encode(self.default_encoding)

# ==================================================
# Line: 385

value = value.encode(self.default_encoding)

# ==================================================
# Occurrences: Lines 498-500 (4 instances)

sig_args.pop(0)

# ==================================================
# Occurrences: Lines 605-605 (2 instances)

pos = find_position(s, match.end(), last, last_pos)

# ==================================================
# Occurrences: Lines 622-622 (2 instances)

last = match.end()

# ==================================================
# Occurrences: Lines 673-673 (2 instances)

prev_ok = not prev or trail_whitespace_re.search(prev)

# ==================================================
# Occurrences: Lines 680-680 (2 instances)

or lead_whitespace_re.search(next_chunk)

# ==================================================
# Occurrences: Lines 687-687 (2 instances)

m = trail_whitespace_re.search(prev)

# ==================================================
# Occurrences: Lines 696-696 (2 instances)

m = lead_whitespace_re.search(next_chunk)

# ==================================================
# Occurrences: Lines 971-976 (4 instances)

tok_type, tok_string = get_token()

# ==================================================
# Occurrences: Lines 982-982 (2 instances)

tok_type, tok_string = get_token()

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/linalg/_linalg.py
# Occurrences: Lines 1153-1158 (2 instances)

r = r.astype(result_t, copy=False)

# ==================================================
# Occurrences: Lines 1183-1184 (2 instances)

q = q.astype(result_t, copy=False)

# ==================================================
# Line: 1835

s = abs(s)

# ==================================================
# Line: 1845

s = abs(s)

# ==================================================
# Line: 1864

s = s.astype(_realType(result_t), copy=False)

# ==================================================
# Line: 1873

s = s.astype(_realType(result_t), copy=False)

# ==================================================
# Occurrences: Lines 2812-2814 (2 instances)

return abs(x).max(axis=axis, keepdims=keepdims, initial=0)

# ==================================================
# Line: 2824

return add.reduce(abs(x), axis=axis, keepdims=keepdims)

# ==================================================
# Line: 2834

absx = abs(x)

# ==================================================
# Occurrences: Lines 2852-2864 (4 instances)

ret = add.reduce(abs(x), axis=row_axis).max(axis=col_axis, initial=0)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/ctypeslib/_ctypeslib.py
# Occurrences: Lines 302-305 (2 instances)

flags = _flags_fromnum(num)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/ma/extras.py
# Occurrences: Lines 311-315 (2 instances)

_m = func(getmaskarray(x), *args, **params)

# ==================================================
# Occurrences: Lines 419-422 (2 instances)

i[axis] = slice(None, None)

# ==================================================
# Occurrences: Lines 436-438 (2 instances)

outarr = zeros(outshape, object)

# ==================================================
# Line: 449

res = func1d(arr[tuple(i.tolist())], *args, **kwargs)

# ==================================================
# Occurrences: Lines 456-458 (2 instances)

j[axis] = ([slice(None, None)] * res.ndim)

# ==================================================
# Line: 464

outarr = zeros(outshape, object)

# ==================================================
# Line: 477

res = func1d(arr[tuple(i.tolist())], *args, **kwargs)

# ==================================================
# Line: 852

s = np.lib._utils_impl._median_nancheck(asorted, s, axis)

# ==================================================
# Line: 860

return np.ma.minimum_fill_value(asorted)

# ==================================================
# Line: 882

s.data[rep] = np.ma.minimum_fill_value(asorted)

# ==================================================
# Line: 892

s = np.lib._utils_impl._median_nancheck(asorted, s, axis)

# ==================================================
# Occurrences: Lines 1721-1730 (4 instances)

mask = np.less_equal(fact, 0, dtype=bool)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/ma/mrecords.py
# Occurrences: Lines 366-368 (2 instances)

output = np.ndarray.view(self, dtype)

# ==================================================
# Line: 380

output = np.ndarray.view(self, dtype)

# ==================================================
# Line: 717

vartypes = _guessvartypes(_variables[0])

# ==================================================
# Line: 724

vartypes = _guessvartypes(_variables[0])

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/ma/core.py
# Line: 493

fill_value = np.asarray(fill_value, dtype=ndtype)

# ==================================================
# Line: 509

fill_value = np.asarray(fill_value, dtype=ndtype)

# ==================================================
# Occurrences: Lines 991-1001 (4 instances)

result = self.f(d, *args, **kwargs)

# ==================================================
# Line: 2928

_data._mask = np.zeros(_data.shape, dtype=mdtype)

# ==================================================
# Line: 2968

mask = np.zeros(_data.shape, dtype=mdtype)

# ==================================================
# Occurrences: Lines 3268-3273 (3 instances)

output = ndarray.view(self, dtype)

# ==================================================
# Line: 3439

_mask[indx] = getmask(value)

# ==================================================
# Line: 3447

_mask = self._mask = make_mask_none(self.shape, _dtype)

# ==================================================
# Line: 3458

mval = getmask(value)

# ==================================================
# Line: 3465

_mask = self._mask = make_mask_none(self.shape, _dtype)

# ==================================================
# Occurrences: Lines 3926-3931 (2 instances)

result = self._data.copy('K')

# ==================================================
# Occurrences: Lines 4077-4079 (4 instances)

data = np.concatenate((arr[0], arr[2]), axis=axis)

# ==================================================
# Line: 4109

'fill': str(self.fill_value),

# ==================================================
# Line: 4174

fill_repr = str(self.fill_value)

# ==================================================
# Occurrences: Lines 6159-6165 (2 instances)

result -= self.min(axis=axis, fill_value=fill_value,
                   keepdims=keepdims)

# ==================================================
# Occurrences: Lines 6601-6603 (2 instances)

self._mask[indx] |= getattr(value, "_mask", False)

# ==================================================
# Occurrences: Lines 6978-6982 (2 instances)

t = self.f.reduce(target, **kwargs)

# ==================================================
# Occurrences: Lines 8232-8235 (2 instances)

a = _mask_propagate(a, a.ndim - 1)

# ==================================================
# Occurrences: Lines 8450-8457 (6 instances)

x = getdata(a)

# ==================================================
# Line: 8558

d = filled(less_equal(absolute(x - y), atol + rtol * absolute(y)),
           masked_equal)

# ==================================================
# Line: 8567

d = filled(less_equal(absolute(x - y), atol + rtol * absolute(y)),
           masked_equal)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/code_generators/generate_umath.py
# Occurrences: Lines 1410-1410 (3 instances)

tname = english_upper(chartoname[t.type])

# ==================================================
# Occurrences: Lines 1418-1422 (6 instances)

tname = english_upper(chartoname[t.type])

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/code_generators/genapi.py
# Occurrences: Lines 277-277 (2 instances)

line = m.group(1)

# ==================================================
# Occurrences: Lines 284-284 (2 instances)

function_name = m.group(1)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/arrayprint.py
# Occurrences: Lines 895-897 (4 instances)

word = recurser(index + (i,), next_hanging_indent, next_width)

# ==================================================
# Occurrences: Lines 910-912 (4 instances)

word = recurser(index + (-i,), next_hanging_indent, next_width)

# ==================================================
# Occurrences: Lines 918-920 (4 instances)

word = recurser(index + (-1,), next_hanging_indent, next_width)

# ==================================================
# Occurrences: Lines 930-932 (2 instances)

nested = recurser(
    index + (i,), next_hanging_indent, next_width
)

# ==================================================
# Occurrences: Lines 944-948 (4 instances)

nested = recurser(index + (-i,), next_hanging_indent,
                  next_width)

# ==================================================
# Line: 1040

self.precision = max(len(s) for s in frac_part)

# ==================================================
# Line: 1049

self.pad_left = max(len(s) for s in int_part)

# ==================================================
# Occurrences: Lines 1065-1066 (2 instances)

self.pad_left = max(len(s) for s in int_part)

# ==================================================
# Occurrences: Lines 1497-1502 (2 instances)

return StructuredVoidFormat.from_data(array(x), **options)(x)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/_internal.py
# Occurrences: Lines 157-157 (2 instances)

while startindex < len(astr):

# ==================================================
# Occurrences: Lines 165-169 (6 instances)

startindex = mo.end()

# ==================================================
# Occurrences: Lines 176-176 (2 instances)

startindex = mo.end()

# ==================================================
# Occurrences: Lines 268-272 (2 instances)

self._data = self._ctypes.c_void_p(ptr)

# ==================================================
# Occurrences: Lines 652-655 (2 instances)

return self.advance(i)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/numeric.py
# Occurrences: Lines 2132-2134 (2 instances)

binwidth = len(binary)

# ==================================================
# Occurrences: Lines 2151-2153 (2 instances)

binwidth = len(binary)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/shape_base.py
# Line: 65

result = result.reshape(1)

# ==================================================
# Line: 71

result = result.reshape(1)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/getlimits.py
# Line: 232

tiny_f128 = exp2(ld(-16382))

# ==================================================
# Line: 257

tiny_f80 = exp2(ld(-16382))

# ==================================================
# Line: 496

obj = cls._finfo_cache.get(dtype)  # most common path

# ==================================================
# Line: 517

obj = cls._finfo_cache.get(dtype)

# ==================================================
# Line: 527

obj = cls._finfo_cache.get(dtype)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/records.py
# Occurrences: Lines 829-832 (2 instances)

pos = fd.tell()

# ==================================================
# Line: 917

shapeprod = sb.array(shape).prod(dtype=nt.intp)

# ==================================================
# Line: 923

shapeprod = sb.array(shape).prod(dtype=nt.intp)

# ==================================================
# Occurrences: Lines 1063-1067 (2 instances)

new = obj.view(dtype)

# ==================================================
# Occurrences: Lines 1075-1079 (2 instances)

new = obj.view(dtype)

# ==================================================
# Line: 1088

obj = obj.view(dtype)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/einsumfunc.py
# Line: 211

path = min(full_results, key=lambda x: x[0])[1]

# ==================================================
# Line: 219

path = min(full_results, key=lambda x: x[0])[1]

# ==================================================
# Line: 379

comb_iter = itertools.combinations(range(len(input_sets)), 2)

# ==================================================
# Occurrences: Lines 395-398 (2 instances)

result = _parse_possible_contraction(
    positions, input_sets, output_set, idx_dict,
    memory_limit, path_cost, naive_cost
)

# ==================================================
# Occurrences: Lines 407-413 (3 instances)

for positions in itertools.combinations(
    range(len(input_sets)), 2
):

# ==================================================
# Line: 487

if len(idx_removed) == 0:

# ==================================================
# Line: 513

rs = len(idx_removed)

# ==================================================
# Line: 612

s = operator.index(s)

# ==================================================
# Line: 629

s = operator.index(s)

# ==================================================
# Line: 650

input_tmp, output_sub = subscripts.split("->")

# ==================================================
# Occurrences: Lines 691-692 (2 instances)

tmp_subscripts = subscripts.replace(",", "")

# ==================================================
# Occurrences: Lines 704-710 (3 instances)

input_subscripts, output_subscript = subscripts.split("->")

# ==================================================
# Line: 927

max_size = max(size_list)

# ==================================================
# Line: 1026

max_i = max(size_list)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/_methods.py
# Occurrences: Lines 228-230 (2 instances)

ret = ret.dtype.type(um.sqrt(ret))

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/defchararray.py
# Occurrences: Lines 1306-1307 (2 instances)

itemsize = len(obj)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/conftest.py
# Occurrences: Lines 131-133 (2 instances)

old_mode = get_fpu_mode()

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/polynomial/polyutils.py
# Occurrences: Lines 616-621 (2 instances)

van = vander_f(x, lmax)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/polynomial/legendre.py
# Occurrences: Lines 516-526 (4 instances)

if len(c) == 1:

# ==================================================
# Occurrences: Lines 895-905 (4 instances)

if len(c) == 1:

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/polynomial/hermite.py
# Occurrences: Lines 495-505 (4 instances)

if len(c) == 1:

# ==================================================
# Occurrences: Lines 875-885 (4 instances)

if len(c) == 1:

# ==================================================
# Occurrences: Lines 1643-1648 (2 instances)

df = _normed_hermite_n(x, ideg - 1) * np.sqrt(2 * ideg)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/polynomial/laguerre.py
# Occurrences: Lines 491-501 (4 instances)

if len(c) == 1:

# ==================================================
# Occurrences: Lines 873-883 (4 instances)

if len(c) == 1:

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/polynomial/hermite_e.py
# Occurrences: Lines 495-505 (4 instances)

if len(c) == 1:

# ==================================================
# Occurrences: Lines 872-882 (4 instances)

if len(c) == 1:

# ==================================================
# Occurrences: Lines 1555-1560 (2 instances)

df = _normed_hermite_e_n(x, ideg - 1) * np.sqrt(ideg)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/polynomial/chebyshev.py
# Occurrences: Lines 1658-1661 (2 instances)

scl = np.array([1.] + [np.sqrt(.5)] * (n - 1))

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_polynomial_impl.py
# Occurrences: Lines 237-240 (2 instances)

return NX.array([])

# ==================================================
# Line: 249

N = len(p)

# ==================================================
# Line: 256

roots = NX.array([])

# ==================================================
# Occurrences: Lines 1304-1308 (4 instances)

coefstr = fmt_float(real(coeff))

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_npyio_impl.py
# Line: 1043

data = iter(data)

# ==================================================
# Line: 1062

data = iter(data)  # cannot chunk when reading from file

# ==================================================
# Line: 1382

delimiter.decode("latin1")

# ==================================================
# Line: 1395

delimiter = delimiter.decode('latin1')

# ==================================================
# Line: 1599

format = delimiter.join(fmt)

# ==================================================
# Line: 1608

format = delimiter.join(fmt)

# ==================================================
# Line: 2106

key = names.index(key)

# ==================================================
# Line: 2113

key = usecols.index(key)

# ==================================================
# Line: 2157

key = names.index(key)

# ==================================================
# Line: 2165

key = usecols.index(key)

# ==================================================
# Line: 2187

for (miss, fill) in zip(missing_values, filling_values)

# ==================================================
# Line: 2202

zipit = zip(missing_values, filling_values)

# ==================================================
# Line: 2302

current_column = map(itemgetter(i), rows)

# ==================================================
# Occurrences: Lines 2349-2353 (2 instances)

zip(*[[conv._loose_call(_r) for _r in map(itemgetter(i), rows)]

# ==================================================
# Line: 2391

n_chars = max(len(row[i]) for row in data)

# ==================================================
# Line: 2414

outputmask = np.array(masks, dtype=mdtype)

# ==================================================
# Line: 2452

ttype = (ttype, max(len(row[i]) for row in data))

# ==================================================
# Line: 2471

outputmask = np.array(masks, dtype=mdtype)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_histograms_impl.py
# Line: 392

first_edge, last_edge = _get_outer_edges(a, range)

# ==================================================
# Line: 425

first_edge, last_edge = _get_outer_edges(a, range)

# ==================================================
# Line: 880

cum_n += _search_sorted_inclusive(sa, bin_edges)

# ==================================================
# Line: 890

bin_index = _search_sorted_inclusive(sa, bin_edges)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_nanfunctions_impl.py
# Occurrences: Lines 1085-1087 (2 instances)

return _nanmedian1d(part, overwrite_input)

# ==================================================
# Occurrences: Lines 1116-1118 (2 instances)

out[...] = m.filled(fill_value)

# ==================================================
# Occurrences: Lines 2021-2023 (2 instances)

std = var.dtype.type(np.sqrt(var))

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_twodim_base_impl.py
# Occurrences: Lines 636-638 (2 instances)

N = len(x)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_arraysetops_impl.py
# Occurrences: Lines 928-930 (2 instances)

return np.ones_like(ar1, dtype=bool)

# ==================================================
# Occurrences: Lines 963-965 (2 instances)

outgoing_array = np.ones_like(ar1, dtype=bool)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_index_tricks_impl.py
# Line: 162

step = abs(step)

# ==================================================
# Line: 182

step = int(abs(step))

# ==================================================
# Line: 202

step_float = abs(step)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_shape_base_impl.py
# Occurrences: Lines 739-741 (4 instances)

sub_arys[i] = _nx.empty(0, dtype=sub_arys[i].dtype)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_utils_impl.py
# Occurrences: Lines 529-559 (7 instances)

arguments = str(inspect.signature(object))

# ==================================================
# Line: 575

print(inspect.getdoc(object), file=output)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_datasource.py
# Occurrences: Lines 355-362 (4 instances)

filelist = self._possible_names(path)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_function_base_impl.py
# Occurrences: Lines 1264-1267 (4 instances)

slice1 = [slice(None)] * N

# ==================================================
# Occurrences: Lines 1299-1301 (4 instances)

slice1[axis] = slice(1, -1)

# ==================================================
# Occurrences: Lines 1377-1380 (8 instances)

slice1[axis] = slice(None)

# ==================================================
# Line: 2562

nin = len(args)

# ==================================================
# Line: 2610

ufunc = frompyfunc(_func, len(args), nout)

# ==================================================
# Occurrences: Lines 4846-4850 (2 instances)

slices_having_nans = np.isnan(arr[-1, ...])

# ==================================================
# Line: 4864

slices_having_nans = np.isnan(arr[-1, ...])

# ==================================================
# Occurrences: Lines 4898-4901 (2 instances)

slices_having_nans = np.isnan(arr[-1, ...])

# ==================================================
# Line: 5386

new = empty(newshape, arr.dtype, arrorder)

# ==================================================
# Line: 5441

new = empty(newshape, arr.dtype, arrorder)

# ==================================================
# Line: 5619

new = empty(newshape, arr.dtype, arrorder)

# ==================================================
# Line: 5645

new = empty(newshape, arr.dtype, arrorder)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_format_impl.py
# Occurrences: Lines 348-351 (4 instances)

dt = descr_to_dtype(descr_str)

# ==================================================
# Occurrences: Lines 658-663 (2 instances)

d = ast.literal_eval(header)

# ==================================================
# Line: 968

offset = fp.tell()

# ==================================================
# Line: 980

offset = fp.tell()

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/recfunctions.py
# Occurrences: Lines 453-457 (2 instances)

data = a.ravel().__array__()

# ==================================================
# Line: 463

fval = np.array(fval, dtype=a.dtype, ndmin=1)

# ==================================================
# Occurrences: Lines 481-488 (3 instances)

data = a.ravel().__array__()

# ==================================================
# Line: 1039

new_shape = arr.shape + (sum(counts), out_dtype.itemsize)

# ==================================================
# Line: 1067

return arr.view((out_dtype, (sum(counts),)))

# ==================================================
# Line: 1143

dts, counts, offsets = zip(*fields)

# ==================================================
# Line: 1154

dts, counts, offsets = zip(*fields)

# ==================================================
# Occurrences: Lines 1587-1592 (2 instances)

idx_1 = np.concatenate((idx_1, idx_out[(idx_out < nb1)]))

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_iotools.py
# Occurrences: Lines 867-871 (3 instances)

nbfields = len(ndtype)

# ==================================================
# Line: 879

names = names.split(",")

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_arraypad_impl.py
# Line: 349

left_slice = _slice_at_axis(slice(start, stop, -1), axis)

# ==================================================
# Line: 360

pad_area = _slice_at_axis(slice(start, stop), axis)

# ==================================================
# Line: 372

right_slice = _slice_at_axis(slice(start, stop, -1), axis)

# ==================================================
# Line: 384

pad_area = _slice_at_axis(slice(start, stop), axis)

# ==================================================
# Line: 434

right_slice = _slice_at_axis(slice(slice_start, slice_end), axis)

# ==================================================
# Line: 453

left_slice = _slice_at_axis(slice(slice_start, slice_end), axis)

# ==================================================
# Line: 513

x = x.ravel()  # Ensure x[0] works for x.ndim == 0, 1, 2

# ==================================================
# Line: 523

x = x.ravel()  # Ensure x[0], x[1] works

# ==================================================
# Line: 765

for axis in range(padded.ndim):

# ==================================================
# Line: 809

axes = range(padded.ndim)

# ==================================================
# Line: 815

roi = _view_roi(padded, original_area_slice, axis)

# ==================================================
# Line: 836

roi = _view_roi(padded, original_area_slice, axis)

# ==================================================
# Line: 844

roi = _view_roi(padded, original_area_slice, axis)

# ==================================================
# Line: 853

roi = _view_roi(padded, original_area_slice, axis)

# ==================================================
# Line: 869

roi = _view_roi(padded, original_area_slice, axis)

# ==================================================
# Line: 881

roi = _view_roi(padded, original_area_slice, axis)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/matrixlib/defmatrix.py
# Occurrences: Lines 29-30 (4 instances)

Ncols = len(newrow)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/symbolic.py
# Line: 286

r = ', '.join(item.tostring(Precedence.TUPLE, language=language)
              for item in self.data)

# ==================================================
# Occurrences: Lines 299-305 (2 instances)

r = ', '.join(item.tostring(Precedence.TUPLE, language=language)
              for item in self.data)

# ==================================================
# Occurrences: Lines 328-340 (7 instances)

for base, exp in sorted(self.data.items()):

# ==================================================
# Line: 813

(t, c), = d.items()

# ==================================================
# Line: 849

(b, e), = d.items()

# ==================================================
# Line: 886

for b, e in d.items():

# ==================================================
# Line: 1357

oper, expr1, expr2 = restore(m.groups())

# ==================================================
# Line: 1371

left, rop, right = m.groups()

# ==================================================
# Line: 1381

keyname, value = m.groups()

# ==================================================
# Line: 1391

op = op.strip()

# ==================================================
# Occurrences: Lines 1415-1418 (3 instances)

result = self.process(operands[0])

# ==================================================
# Occurrences: Lines 1435-1437 (2 instances)

result = self.process(operands[0])

# ==================================================
# Occurrences: Lines 1446-1448 (2 instances)

value, _, kind = m.groups()

# ==================================================
# Occurrences: Lines 1458-1460 (2 instances)

value, _, _, kind = m.groups()

# ==================================================
# Line: 1490

target, args, paren = m.groups()

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/f90mod_rules.py
# Occurrences: Lines 144-144 (2 instances)

note = '\n'.join(note)

# ==================================================
# Occurrences: Lines 167-167 (2 instances)

note = '\n'.join(note)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/capi_maps.py
# Occurrences: Lines 209-210 (2 instances)

elif 'typespec' in var and var['typespec'].lower() in f2cmap_all:

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/cfuncs.py
# Occurrences: Lines 1536-1536 (2 instances)

saveout = copy.copy(outneeds[n])

# ==================================================
# Occurrences: Lines 1559-1559 (2 instances)

saveout = copy.copy(outneeds[n])

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/cb_rules.py
# Line: 555

rd = dictappend(rd, ar)

# ==================================================
# Occurrences: Lines 566-567 (2 instances)

ar = applyrules(r, vrd, var[a])

# ==================================================
# Occurrences: Lines 578-579 (2 instances)

ar = applyrules(r, vrd, var[a])

# ==================================================
# Occurrences: Lines 590-591 (2 instances)

ar = applyrules(r, vrd, var[a])

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/crackfortran.py
# Line: 338

line = fhandle.readline()

# ==================================================
# Line: 351

line = fhandle.readline()

# ==================================================
# Occurrences: Lines 390-393 (4 instances)

l = fin.readline()

# ==================================================
# Occurrences: Lines 401-401 (2 instances)

currentfilename = fin.filename()

# ==================================================
# Occurrences: Lines 472-474 (4 instances)

r = cont1.match(l)

# ==================================================
# Occurrences: Lines 484-484 (2 instances)

finalline = ll.lower()

# ==================================================
# Occurrences: Lines 494-494 (2 instances)

lc = fin.readline()

# ==================================================
# Occurrences: Lines 503-505 (4 instances)

r = cont1.match(l)

# ==================================================
# Occurrences: Lines 514-514 (2 instances)

finalline = ll.lower() if not (is_f2py_directive and iscstyledirective(ll)) else ll

# ==================================================
# Occurrences: Lines 525-527 (2 instances)

m = includeline.match(origfinalline)

# ==================================================
# Line: 535

fn1 = os.path.join(inc_dir, fn)

# ==================================================
# Line: 548

finalline = ll.lower()

# ==================================================
# Occurrences: Lines 554-556 (2 instances)

m = includeline.match(origfinalline)

# ==================================================
# Line: 563

fn1 = os.path.join(inc_dir, fn)

# ==================================================
# Line: 709

_, has_semicolon = split_by_unquoted(line, ";")

# ==================================================
# Line: 715

line, semicolon_line = split_by_unquoted(line, ";")

# ==================================================
# Line: 1007

block = m.group('this')

# ==================================================
# Occurrences: Lines 1036-1041 (3 instances)

name, attrs, _ = _resolvetypedefpattern(m.group('after'))

# ==================================================
# Line: 1052

args = rmbadname([x.strip()
                  for x in markoutercomma(args).split('@,@')])

# ==================================================
# Line: 1122

groupcache[groupcounter]['prefix'] = m.group('before')

# ==================================================
# Occurrences: Lines 1164-1165 (2 instances)

if bindcdat.group('lang_name'):

# ==================================================
# Occurrences: Lines 1182-1186 (2 instances)

t = typespattern[0].match(m.group('before') + ' ' + name)

# ==================================================
# Occurrences: Lines 1199-1203 (3 instances)

name, args, result, _ = _resolvenameargspattern(m.group('after'))

# ==================================================
# Occurrences: Lines 1211-1225 (7 instances)

block, m.group('after'))

# ==================================================
# Line: 1251

k = rmbadname1(m1.group('name'))

# ==================================================
# Line: 1259

ap = m.group('this') + pl

# ==================================================
# Occurrences: Lines 1298-1301 (3 instances)

[x.strip() for x in m.group('after').split(',')]

# ==================================================
# Occurrences: Lines 1344-1346 (3 instances)

if m.group('after').strip().lower() == 'none':

# ==================================================
# Line: 1352

for e in markoutercomma(m.group('after')).split('@,@'):

# ==================================================
# Line: 1400

for c in m.group('after'):

# ==================================================
# Occurrences: Lines 1416-1418 (2 instances)

dl = dl.strip()

# ==================================================
# Occurrences: Lines 1424-1426 (2 instances)

dl = dl.strip()

# ==================================================
# Occurrences: Lines 1483-1483 (2 instances)

line = m.group('after').strip()

# ==================================================
# Occurrences: Lines 1506-1511 (2 instances)

r'\A\s*(?P<name>\b\w+\b)\s*((,(\s*\bonly\b\s*:|(?P<notonly>))\s*(?P<list>.*))|)\s*\Z', m.group('after'), re.I)

# ==================================================
# Occurrences: Lines 1540-1545 (4 instances)

if m.group('this') == 'usercode' and 'usercode' in d:

# ==================================================
# Line: 1554

m.group('this'))

# ==================================================
# Occurrences: Lines 1711-1711 (2 instances)

edecl['kindselector'] = copy.copy(kindselect)

# ==================================================
# Occurrences: Lines 1738-1738 (2 instances)

edecl['attrspec'] = copy.copy(attrspec)

# ==================================================
# Occurrences: Lines 1745-1748 (4 instances)

edecl['kindselector'] = copy.copy(kindselect)

# ==================================================
# Line: 1849

kindselect[k] = rmbadname1(i)

# ==================================================
# Line: 1876

charselect[k] = rmbadname1(i)

# ==================================================
# Line: 2137

n = len(dep)

# ==================================================
# Line: 2158

n = len(dep)

# ==================================================
# Occurrences: Lines 2316-2339 (26 instances)

m = re_1.match(e)

# ==================================================
# Occurrences: Lines 2445-2446 (2 instances)

params = copy.copy(global_params)

# ==================================================
# Occurrences: Lines 2486-2490 (4 instances)

orig_v_len = len(v)

# ==================================================
# Occurrences: Lines 2637-2637 (2 instances)

l = str(eval(l, {}, params))

# ==================================================
# Occurrences: Lines 2646-2646 (2 instances)

l = str(eval(l, {}, params))

# ==================================================
# Occurrences: Lines 2835-2835 (3 instances)

v_attr = vars[v].get('attrspec', [])

# ==================================================
# Occurrences: Lines 2846-2846 (3 instances)

for aa in vars[v].get('attrspec', []):

# ==================================================
# Occurrences: Lines 3001-3004 (2 instances)

bound = param_parse(dimrange[0], params)

# ==================================================
# Occurrences: Lines 3098-3102 (4 instances)

m = re_1.match(d)

# ==================================================
# Line: 3195

if 'name' in m.groupdict() and m.group('name'):

# ==================================================
# Line: 3201

if 'name' in m.groupdict() and m.group('name'):

# ==================================================
# Occurrences: Lines 3215-3216 (2 instances)

rn = m.group('name')

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/_src_pyf.py
# Line: 136

thelist = conv(mobj.group(1).replace(r'\,', '@comma@'))

# ==================================================
# Line: 180

name = mobj.group(1)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/f2py2e.py
# Occurrences: Lines 684-688 (2 instances)

i = flib_flags.index(s)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/func2subr.py
# Occurrences: Lines 298-302 (2 instances)

fortranname = getfortranname(rout)

# ==================================================
# Occurrences: Lines 323-327 (2 instances)

fortranname = getfortranname(rout)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/rules.py
# Line: 1362

rd = dictappend(rd, ar)

# ==================================================
# Line: 1369

rd = dictappend(rd, ar)

# ==================================================
# Occurrences: Lines 1376-1380 (2 instances)

rd = dictappend(rd, ar)

# ==================================================
# Line: 1419

rd = dictappend(rd, ar)

# ==================================================
# Line: 1472

lines = ''.join(lines).replace('\n     &\n', '\n')

# ==================================================
# Line: 1499

lines = ''.join(lines).replace('\n     &\n', '\n')

# ==================================================
# Line: 1528

rd = dictappend(rd, ar)

# ==================================================
# Occurrences: Lines 1553-1554 (2 instances)

ar = applyrules(r, vrd, var[a])

# ==================================================
# Occurrences: Lines 1567-1568 (3 instances)

ar = applyrules(r, vrd, var[a])

# ==================================================
# Occurrences: Lines 1575-1575 (2 instances)

rd = dictappend(rd, ar)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/auxfuncs.py
# Occurrences: Lines 895-895 (3 instances)

i = res.get('supertext', '')

# ==================================================
# Occurrences: Lines 901-901 (3 instances)

i = res.get('supertext', '')

# ==================================================
