# cached-repeated-calls snippets for scipy

# File: /root/ecooptimizer/scipy/scipy/sparse/_sputils.py
# Occurrences: Lines 227-236 (4 instances)

if max(*A.shape) > max_value:

# ==================================================
# Line: 242

if max(*A.shape) > max_value:

# ==================================================
# Occurrences: Lines 252-256 (3 instances)

if max(*A.shape) > max_value:

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_base.py
# Line: 634

csr_self = (self if self.ndim < 3 else self.reshape(1, -1)).tocsr()

# ==================================================
# Occurrences: Lines 646-648 (2 instances)

csr_self = (self if self.ndim < 3 else self.reshape(1, -1)).tocsr()

# ==================================================
# Line: 664

csr_self = (self if self.ndim < 3 else self.reshape(1, -1)).tocsr()

# ==================================================
# Line: 675

all_true = csr_self.__class__(np.ones(csr_self.shape, dtype=np.bool_))

# ==================================================
# Line: 794

return result.reshape(1)

# ==================================================
# Occurrences: Lines 834-839 (2 instances)

result = self._ascontainer(result)

# ==================================================
# Line: 857

result = self._ascontainer(result)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_coo.py
# Line: 38

idx_dtype = self._get_index_dtype(maxval=max(self._shape))

# ==================================================
# Line: 56

self._shape = check_shape(shape, allow_nd=self._allow_nd)

# ==================================================
# Occurrences: Lines 87-91 (2 instances)

if check_shape(shape, allow_nd=self._allow_nd) != self._shape:

# ==================================================
# Line: 494

new_col = np.arange(max_index, dtype=idx_dtype)

# ==================================================
# Line: 500

new_row = np.arange(max_index, dtype=idx_dtype)

# ==================================================
# Occurrences: Lines 671-673 (3 instances)

perm = range(ret.ndim)

# ==================================================
# Line: 784

result = np.zeros(result_shape, dtype=result_dtype)

# ==================================================
# Line: 799

result = np.zeros(result_shape, dtype=result_dtype)

# ==================================================
# Line: 1164

new_data = np.tile(new_data, repeat_count)

# ==================================================
# Line: 1175

new_data = np.tile(new_data, repeat_count)

# ==================================================
# Occurrences: Lines 1314-1318 (2 instances)

idx_dtype = get_index_dtype(maxval=maxval)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_compressed.py
# Line: 58

arrays = coo._coo_to_compressed(self._swap)

# ==================================================
# Line: 96

arrays = coo._coo_to_compressed(self._swap)

# ==================================================
# Occurrences: Lines 293-307 (4 instances)

new_other = _make_diagonal_csr(other.toarray().ravel(), is_array)

# ==================================================
# Occurrences: Lines 322-326 (2 instances)

bshape = broadcast_shapes(self.shape, other.shape)

# ==================================================
# Line: 333

ret.data = data.view(np.ndarray).ravel()

# ==================================================
# Line: 351

(data.view(np.ndarray).ravel(), (row, col)),

# ==================================================
# Line: 368

(data.view(np.ndarray).ravel(), (row, col)),

# ==================================================
# Line: 380

ret.data = data.view(np.ndarray).ravel()

# ==================================================
# Occurrences: Lines 439-442 (4 instances)

s_indptr = np.asarray(s.indptr, dtype=idx_dtype)

# ==================================================
# Occurrences: Lines 453-456 (4 instances)

s_indptr = np.asarray(s.indptr, dtype=idx_dtype)

# ==================================================
# Line: 772

j = np.arange(max_index, dtype=self.indices.dtype)

# ==================================================
# Line: 779

i = np.arange(max_index, dtype=self.indices.dtype)

# ==================================================
# Occurrences: Lines 795-801 (2 instances)

ret = csr_sample_offsets(M, N, self.indptr, self.indices, n_samples,
                         i, j, offsets)

# ==================================================
# Occurrences: Lines 853-859 (2 instances)

ret = csr_sample_offsets(M, N, self.indptr, self.indices, n_samples,
                         i, j, offsets)

# ==================================================
# Occurrences: Lines 890-896 (2 instances)

ret = csr_sample_offsets(M, N, self.indptr, self.indices, n_samples,
                         i, j, offsets)

# ==================================================
# Occurrences: Lines 941-941 (2 instances)

if len(uj) == je - js:

# ==================================================
# Occurrences: Lines 947-947 (2 instances)

new_nnzs[c] = len(uj)

# ==================================================
# Line: 1252

if len(self.shape) == 1 and len(shape) == 1:

# ==================================================
# Occurrences: Lines 1266-1267 (2 instances)

if len(shape) != 2:

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_csr.py
# Line: 209

idx = np.asarray(idx, dtype=idx_dtype)

# ==================================================
# Line: 215

col = np.asarray(idx, dtype=idx_dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_dia.py
# Line: 29

arg1 = arg1.copy()

# ==================================================
# Occurrences: Lines 35-40 (2 instances)

A = arg1.copy()

# ==================================================
# Line: 79

self._shape = check_shape(A.shape)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_dsolve/linsolve.py
# Line: 216

is_pydata_sparse = is_pydata_spmatrix(b)

# ==================================================
# Line: 256

b_vec = b.toarray()

# ==================================================
# Line: 274

b = b.toarray()

# ==================================================
# Line: 297

if not (b.format == "csc" or is_pydata_spmatrix(b)):

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_eigen/lobpcg/lobpcg.py
# Occurrences: Lines 494-498 (2 instances)

lambdaHistory = np.zeros((maxiter + 3, sizeX),
                         dtype=blockVectorX.dtype)

# ==================================================
# Occurrences: Lines 652-657 (2 instances)

ii = _get_indx(_lambda, sizeX, largest)

# ==================================================
# Occurrences: Lines 699-700 (2 instances)

aux = np.sum(blockVectorR.conj() * blockVectorR, 0)

# ==================================================
# Occurrences: Lines 841-843 (2 instances)

gramXAX = np.dot(blockVectorX.T.conj(), blockVectorAX)

# ==================================================
# Occurrences: Lines 849-849 (2 instances)

gramRBR = np.eye(currentBlockSize, dtype=gramDtype)

# ==================================================
# Occurrences: Lines 863-863 (2 instances)

gramPBP = np.eye(currentBlockSize, dtype=gramDtype)

# ==================================================
# Occurrences: Lines 883-885 (2 instances)

_lambda, eigBlockVector = eigh(gramA,
                               gramB,
                               check_finite=False)

# ==================================================
# Occurrences: Lines 904-906 (2 instances)

_lambda, eigBlockVector = eigh(gramA,
                               gramB,
                               check_finite=False)

# ==================================================
# Line: 916

ii = _get_indx(_lambda, sizeX, largest)

# ==================================================
# Occurrences: Lines 930-936 (6 instances)

pp = np.dot(activeBlockVectorR, eigBlockVectorR)

# ==================================================
# Occurrences: Lines 942-944 (6 instances)

pp = np.dot(activeBlockVectorR, eigBlockVectorR)

# ==================================================
# Occurrences: Lines 959-962 (4 instances)

pp = np.dot(activeBlockVectorR, eigBlockVectorR)

# ==================================================
# Occurrences: Lines 968-969 (4 instances)

pp = np.dot(activeBlockVectorR, eigBlockVectorR)

# ==================================================
# Occurrences: Lines 983-984 (2 instances)

aux = np.sum(blockVectorR.conj() * blockVectorR, 0)

# ==================================================
# Line: 1027

gramXAX = np.dot(blockVectorX.T.conj(), blockVectorAX)

# ==================================================
# Line: 1040

gramXBX = np.dot(blockVectorX.T.conj(), blockVectorBX)

# ==================================================
# Occurrences: Lines 1051-1053 (2 instances)

ii = _get_indx(_lambda, sizeX, largest)

# ==================================================
# Occurrences: Lines 1066-1067 (2 instances)

aux = np.sum(blockVectorR.conj() * blockVectorR, 0)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_eigen/_svds.py
# Occurrences: Lines 41-53 (7 instances)

kmax = min(A.shape) if solver == 'propack' else min(A.shape) - 1

# ==================================================
# Line: 76

shape = (A.shape[0],) if solver == 'propack' else (min(A.shape),)

# ==================================================
# Occurrences: Lines 466-466 (2 instances)

shape=(min(A.shape), min(A.shape)))

# ==================================================
# Line: 475

X = rng.standard_normal(size=(min(A.shape), k))

# ==================================================
# Line: 508

v0 = rng.standard_normal(size=(min(A.shape),))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_eigen/arpack/arpack.py
# Occurrences: Lines 553-567 (4 instances)

self.workd[yslice] = self.OP(self.workd[xslice])

# ==================================================
# Occurrences: Lines 749-753 (2 instances)

self.workd[yslice] = self.OP(self.workd[xslice])

# ==================================================
# Occurrences: Lines 782-783 (2 instances)

dr = np.zeros(k + 1, self.tp)

# ==================================================
# Line: 817

z[:, i + 1] = z[:, i].conjugate()

# ==================================================
# Occurrences: Lines 834-840 (5 instances)

d[i] = np.dot(zr[:, i], self.matvec(zr[:, i]))

# ==================================================
# Line: 1625

A = aslinearoperator(A)

# ==================================================
# Line: 1647

M_matvec = aslinearoperator(M).matvec

# ==================================================
# Occurrences: Lines 1658-1666 (3 instances)

Minv_matvec = get_OPinv_matvec(A, M, sigma,
                               hermitian=True, tol=tol)

# ==================================================
# Occurrences: Lines 1673-1677 (3 instances)

Minv_matvec = get_OPinv_matvec(A, M, sigma,
                               hermitian=True, tol=tol)

# ==================================================
# Occurrences: Lines 1683-1692 (4 instances)

matvec = aslinearoperator(A).matvec

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_special_sparse_arrays.py
# Occurrences: Lines 384-385 (2 instances)

L_i = np.empty_like(L)

# ==================================================
# Occurrences: Lines 639-640 (2 instances)

d1 = -4 * np.ones(self.n, dtype=self.dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_svdp.py
# Occurrences: Lines 222-224 (2 instances)

u[:, 0] = rng.uniform(size=m)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_expm_multiply.py
# Occurrences: Lines 292-296 (4 instances)

c1 = _exact_inf_norm(B)

# ==================================================
# Occurrences: Lines 768-768 (3 instances)

c1 = _exact_inf_norm(F)

# ==================================================
# Occurrences: Lines 776-776 (3 instances)

if c1 + c2 <= tol * _exact_inf_norm(F):

# ==================================================
# Occurrences: Lines 803-803 (3 instances)

c1 = _exact_inf_norm(F)

# ==================================================
# Occurrences: Lines 812-812 (3 instances)

if c1 + c2 <= tol * _exact_inf_norm(F):

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_funm_multiply_krylov.py
# Occurrences: Lines 130-132 (4 instances)

V[:, k + 1] = A.dot(V[:, k]) - H[k, k - 1] * V[:, k - 1]

# ==================================================
# Occurrences: Lines 339-343 (4 instances)

fH = f(t * H[:end, :end])

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_isolve/_gcrotmk.py
# Occurrences: Lines 111-111 (2 instances)

w_norm = nrm2(w)

# ==================================================
# Occurrences: Lines 126-126 (2 instances)

hcur[i+1] = nrm2(w)

# ==================================================
# Occurrences: Lines 376-376 (2 instances)

beta = nrm2(r)

# ==================================================
# Occurrences: Lines 384-384 (2 instances)

beta = nrm2(r)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_isolve/lsmr.py
# Occurrences: Lines 240-252 (5 instances)

x = zeros(n, dtype)

# ==================================================
# Line: 269

hbar = zeros(n, dtype)

# ==================================================
# Line: 286

normA = sqrt(normA2)

# ==================================================
# Occurrences: Lines 330-336 (3 instances)

beta = norm(u)

# ==================================================
# Line: 400

normA = sqrt(normA2)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_isolve/minres.py
# Line: 166

z = abs(s - t)

# ==================================================
# Line: 175

z = abs(s - t)

# ==================================================
# Occurrences: Lines 194-195 (2 instances)

w = zeros(n, dtype=xtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_isolve/lgmres.py
# Occurrences: Lines 162-162 (2 instances)

r_norm = nrm2(r_outer)

# ==================================================
# Occurrences: Lines 171-171 (2 instances)

rnorm = nrm2(r_outer)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_isolve/lsqr.py
# Line: 332

var = np.zeros(n)

# ==================================================
# Occurrences: Lines 377-387 (4 instances)

x = np.zeros(n)

# ==================================================
# Occurrences: Lines 431-437 (3 instances)

beta = np.linalg.norm(u)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_isolve/tfqmr.py
# Line: 104

x = b.copy()

# ==================================================
# Line: 112

r = b.copy()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_isolve/iterative.py
# Line: 256

rtilde = r.copy()

# ==================================================
# Line: 276

p = r.copy()

# ==================================================
# Line: 500

bnrm2 = np.linalg.norm(b)

# ==================================================
# Occurrences: Lines 521-522 (2 instances)

rtilde = r.copy()

# ==================================================
# Occurrences: Lines 552-553 (4 instances)

p = r.copy()

# ==================================================
# Occurrences: Lines 744-744 (2 instances)

if np.linalg.norm(r) < atol:  # Are we done?

# ==================================================
# Occurrences: Lines 760-760 (3 instances)

h0 = np.linalg.norm(w)

# ==================================================
# Occurrences: Lines 766-766 (3 instances)

h1 = np.linalg.norm(w)

# ==================================================
# Occurrences: Lines 822-822 (2 instances)

rnorm = np.linalg.norm(r)

# ==================================================
# Occurrences: Lines 958-963 (6 instances)

vtilde = r.copy()

# ==================================================
# Occurrences: Lines 1013-1021 (4 instances)

y = M1.matvec(vtilde)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_matfuncs.py
# Occurrences: Lines 98-100 (2 instances)

if int(p) != p or p < 0:

# ==================================================
# Occurrences: Lines 165-167 (2 instances)

out = A.dot(B)

# ==================================================
# Line: 643

return _solve_P_Q(U, V, structure=structure)

# ==================================================
# Line: 649

return _solve_P_Q(U, V, structure=structure)

# ==================================================
# Occurrences: Lines 655-658 (2 instances)

return _solve_P_Q(U, V, structure=structure)

# ==================================================
# Line: 673

X = _solve_P_Q(U, V, structure=structure)

# ==================================================
# Line: 792

exp_diag = np.exp(scale * diag_T)

# ==================================================
# Line: 801

exp_diag = np.exp(scale * diag_T)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/linalg/_onenormest.py
# Line: 85

A = aslinearoperator(A)

# ==================================================
# Line: 94

A_explicit = np.asarray(aslinearoperator(A).matmat(np.identity(n)))

# ==================================================
# Line: 275

ind = range(t)

# ==================================================
# Line: 299

for j in range(t):

# ==================================================
# Line: 311

for j in range(t):

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_bsr.py
# Line: 119

self._shape = check_shape(shape)

# ==================================================
# Line: 137

self._shape = check_shape(shape)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/csgraph/_laplacian.py
# Line: 431

m = _linearoperator(md, shape=graph.shape, dtype=dtype)

# ==================================================
# Line: 443

m = _linearoperator(md, shape=graph.shape, dtype=dtype)

# ==================================================
# Line: 469

m = m.tocoo(copy=needs_copy)

# ==================================================
# Line: 480

m = m.tocoo(copy=needs_copy)

# ==================================================
# Line: 514

m = _linearoperator(md, shape=graph.shape, dtype=dtype)

# ==================================================
# Line: 526

m = _linearoperator(md, shape=graph.shape, dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_index.py
# Occurrences: Lines 66-68 (2 instances)

res = self._get_intXarray(row, col)

# ==================================================
# Line: 134

x = np.asarray(x, dtype=self.dtype)

# ==================================================
# Line: 165

x = np.asarray(x, dtype=self.dtype)

# ==================================================
# Line: 204

x = np.asarray(x, dtype=self.dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_lil.py
# Line: 38

self._shape = check_shape(A.shape)

# ==================================================
# Occurrences: Lines 48-49 (2 instances)

self.rows = np.empty((M,), dtype=object)

# ==================================================
# Line: 65

self._shape = check_shape(A.shape)

# ==================================================
# Line: 411

indptr = np.empty(M + 1, dtype=idx_dtype)

# ==================================================
# Line: 422

indptr = np.empty(M + 1, dtype=idx_dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_construct.py
# Occurrences: Lines 435-446 (7 instances)

idx_dtype = get_index_dtype(maxval=n)

# ==================================================
# Line: 963

blocks = np.asarray(blocks, dtype='object')

# ==================================================
# Occurrences: Lines 977-982 (2 instances)

blocks = np.asarray(blocks, dtype='object')

# ==================================================
# Occurrences: Lines 990-995 (2 instances)

blocks = np.asarray(blocks, dtype='object')

# ==================================================
# Occurrences: Lines 1040-1041 (2 instances)

row = np.empty(nnz, dtype=idx_dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/sparse/_dok.py
# Occurrences: Lines 38-39 (2 instances)

self._shape = check_shape(arg1.shape, allow_nd=self._allow_nd)

# ==================================================
# Occurrences: Lines 53-58 (2 instances)

self.dtype = getdtype(arg1.dtype)

# ==================================================
# Line: 290

new = self._dok_container(self.shape, dtype=res_dtype)

# ==================================================
# Line: 300

new = self._dok_container(self.shape, dtype=res_dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/ndimage/_measurements.py
# Line: 199

output = np.empty(input.shape, np.intp if need_64bits else np.int32)

# ==================================================
# Line: 222

tmp_output = np.empty(input.shape, np.intp if need_64bits else np.int32)

# ==================================================
# Occurrences: Lines 526-530 (2 instances)

if np.any(index.astype(labels.dtype).astype(index.dtype) != index):

# ==================================================
# Occurrences: Lines 997-1016 (6 instances)

mins = np.zeros(labels.max() + 2, input.dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/ndimage/_morphology.py
# Line: 244

structure = structure.copy()

# ==================================================
# Line: 281

structure = structure.copy()

# ==================================================
# Line: 2143

ft_inplace = isinstance(indices, np.ndarray)

# ==================================================
# Line: 2193

if isinstance(indices, np.ndarray):

# ==================================================
# Occurrences: Lines 2387-2389 (2 instances)

dt[...] = np.where(input, -1, 0).astype(np.int32)

# ==================================================
# Line: 2595

dt = np.add.reduce(dt, axis=0)

# ==================================================
# Line: 2602

dt = np.add.reduce(dt, axis=0)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/ndimage/_ni_support.py
# Occurrences: Lines 89-99 (4 instances)

if complex_output and np.dtype(output).kind != 'c':

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/ndimage/_filters.py
# Occurrences: Lines 173-173 (2 instances)

return footprinted_function(xp.asarray(view), **kwargs)

# ==================================================
# Occurrences: Lines 183-185 (4 instances)

return footprinted_function(xp.asarray(view), **kwargs)

# ==================================================
# Occurrences: Lines 193-198 (6 instances)

temp = footprinted_function(xp.asarray(view[i:i2]), **kwargs)

# ==================================================
# Line: 844

num_axes = len(axes)

# ==================================================
# Line: 851

if len(axes) > 0:

# ==================================================
# Line: 1603

num_axes = len(axes)

# ==================================================
# Line: 1609

if len(axes) > 0:

# ==================================================
# Line: 1744

footprint = np.asarray(footprint, dtype=bool)

# ==================================================
# Line: 1759

footprint = np.asarray(footprint, dtype=bool)

# ==================================================
# Line: 1770

num_axes = len(axes)

# ==================================================
# Occurrences: Lines 1776-1781 (2 instances)

for ii in range(len(axes)) if sizes[ii] > 1]

# ==================================================
# Line: 1795

f"len(axes) ({len(axes)})")

# ==================================================
# Line: 1933

num_axes = len(axes)

# ==================================================
# Line: 1949

f"len(axes) ({len(axes)})")

# ==================================================
# Occurrences: Lines 1998-2003 (4 instances)

x = input.astype('int64')

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_build_utils/tempita/_tempita.py
# Line: 239

expr = self._eval(expr, ns, pos)

# ==================================================
# Occurrences: Lines 254-258 (2 instances)

result = self._eval(expr, ns, pos)

# ==================================================
# Line: 347

value = value.encode(self.default_encoding)

# ==================================================
# Line: 371

value = value.encode(self.default_encoding)

# ==================================================
# Occurrences: Lines 477-479 (4 instances)

sig_args.pop(0)

# ==================================================
# Occurrences: Lines 584-584 (2 instances)

pos = find_position(s, match.end(), last, last_pos)

# ==================================================
# Occurrences: Lines 601-601 (2 instances)

last = match.end()

# ==================================================
# Occurrences: Lines 649-649 (2 instances)

prev_ok = not prev or trail_whitespace_re.search(prev)

# ==================================================
# Occurrences: Lines 655-655 (2 instances)

and (not next_chunk or lead_whitespace_re.search(next_chunk)

# ==================================================
# Occurrences: Lines 662-662 (2 instances)

m = trail_whitespace_re.search(prev)

# ==================================================
# Occurrences: Lines 671-671 (2 instances)

m = lead_whitespace_re.search(next_chunk)

# ==================================================
# Occurrences: Lines 957-967 (6 instances)

tok_type, tok_string = get_token()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_build_utils/_generate_blas_wrapper.py
# Occurrences: Lines 94-96 (2 instances)

blas_sigs = f.readlines()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/signal/_fir_filter_design.py
# Line: 835

bands = np.asarray(bands)

# ==================================================
# Line: 854

bands = np.asarray(bands).copy()

# ==================================================
# Occurrences: Lines 971-972 (2 instances)

bands = np.asarray(bands)

# ==================================================
# Line: 987

bands = np.asarray(bands).flatten() / nyq

# ==================================================
# Line: 995

desired = np.asarray(desired).flatten()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/signal/_spectral_py.py
# Occurrences: Lines 887-889 (3 instances)

nperseg = len(win)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/signal/_short_time_fft.py
# Occurrences: Lines 2067-2069 (2 instances)

return fft_lib.rfft(x, n=self.mfft, axis=-1)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/signal/_filter_design.py
# Occurrences: Lines 1401-1402 (2 instances)

b = xp.asarray([1], dtype=result_type)

# ==================================================
# Occurrences: Lines 1442-1443 (2 instances)

z = xp.zeros(n_sections*2, dtype=xp.complex128)

# ==================================================
# Occurrences: Lines 1734-1741 (8 instances)

z1_idx = _nearest_real_complex_idx(z, p1, 'real')

# ==================================================
# Occurrences: Lines 1757-1758 (4 instances)

z = np.delete(z, z1_idx)

# ==================================================
# Occurrences: Lines 1767-1767 (2 instances)

p2 = p1.conj()

# ==================================================
# Occurrences: Lines 1773-1773 (2 instances)

z = np.delete(z, z1_idx)

# ==================================================
# Occurrences: Lines 1779-1779 (2 instances)

z2_idx = _nearest_real_complex_idx(z, p1, 'real')

# ==================================================
# Occurrences: Lines 2123-2125 (2 instances)

pwo = wo ** xp.arange(max((d, n)), dtype=b.dtype)

# ==================================================
# Line: 4276

WN = xp.sort(xp.abs(WN))

# ==================================================
# Line: 4283

WN = xp.sort(xp.abs(WN))

# ==================================================
# Line: 4495

nat = xp.asarray([float(nat0), float(nat1)])

# ==================================================
# Line: 4501

nat = xp.asarray([float(nat0), float(nat1)])

# ==================================================
# Occurrences: Lines 4681-4683 (3 instances)

xp.asarray([], device=device), xp.asarray([], device=device), 10**(-rp/20)

# ==================================================
# Occurrences: Lines 4749-4754 (2 instances)

m = xp.arange(-N+1, N, 2, dtype=xp_default_dtype(xp), device=device)

# ==================================================
# Occurrences: Lines 4944-4949 (2 instances)

p = -math.sqrt(1.0 / _pow10m1(0.1 * rp))

# ==================================================
# Occurrences: Lines 5049-5052 (2 instances)

if abs(int(n)) != n:

# ==================================================
# Occurrences: Lines 5277-5280 (2 instances)

if abs(int(N)) != N:

# ==================================================
# Occurrences: Lines 5307-5309 (2 instances)

z = xp.asarray([], device=device)

# ==================================================
# Line: 5738

b = np.zeros(N + 1)

# ==================================================
# Line: 5748

a = np.zeros(N + 1)

# ==================================================
# Occurrences: Lines 5913-5917 (2 instances)

g1 = -2 * np.exp(2j * fr) * T

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/signal/_ltisys.py
# Line: 1902

yout = squeeze(xout @ C.T)

# ==================================================
# Line: 1917

yout = squeeze(xout @ C.T)

# ==================================================
# Line: 1944

expMT = linalg.expm(M.T)

# ==================================================
# Line: 1965

expMT = linalg.expm(M.T)

# ==================================================
# Line: 1972

yout = squeeze(xout @ C.T) + squeeze(U @ D.T)

# ==================================================
# Line: 2580

r_j = np.arange(2, hnb+nb_real % 2)

# ==================================================
# Line: 2592

r_j = np.arange(2, hnb+nb_real % 2)

# ==================================================
# Occurrences: Lines 2621-2621 (2 instances)

det_transfer_matrixb = np.abs(np.linalg.det(transfer_matrix))

# ==================================================
# Occurrences: Lines 2647-2647 (2 instances)

np.abs(np.linalg.det(transfer_matrix))))

# ==================================================
# Occurrences: Lines 2669-2674 (4 instances)

det_transfer_matrixb = np.abs(np.linalg.det(transfer_matrix))

# ==================================================
# Occurrences: Lines 2907-2911 (8 instances)

diag_poles[idx, idx] = np.real(p)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/signal/_spline_filters.py
# Occurrences: Lines 198-199 (2 instances)

zi = lfiltic(cs, r_[1, -2 * rho * cos(omega), rho * rho], r_[zi_1, zi_2])

# ==================================================
# Occurrences: Lines 217-218 (2 instances)

zi = lfiltic(cs, r_[1, -2 * rho * cos(omega), rho * rho], r_[zi_1, zi_2])

# ==================================================
# Line: 585

res = zeros_like(newx, dtype=cj.dtype)

# ==================================================
# Line: 598

result = zeros_like(newx, dtype=cj.dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/signal/_signaltools.py
# Occurrences: Lines 288-289 (2 instances)

a_in1 = np.asarray(in1)

# ==================================================
# Occurrences: Lines 304-309 (3 instances)

a_in1 = np.asarray(in1)

# ==================================================
# Line: 322

out = np.empty(ps, a_in1.dtype)

# ==================================================
# Occurrences: Lines 407-412 (2 instances)

lags = np.arange(-in2_len + 1, in1_len)

# ==================================================
# Line: 2237

zi = np.asarray(zi)

# ==================================================
# Line: 2252

zi = np.asarray(zi)

# ==================================================
# Occurrences: Lines 3135-3152 (6 instances)

current = np.array([1])

# ==================================================
# Occurrences: Lines 3935-3940 (4 instances)

if up != int(up):

# ==================================================
# Occurrences: Lines 3970-3973 (2 instances)

h = firwin(2 * half_len + 1, f_c, window=window)

# ==================================================
# Line: 4579

M = np.zeros((2*m, 2*order))

# ==================================================
# Line: 4617

W = np.zeros((2*m, 2*order))

# ==================================================
# Occurrences: Lines 4843-4846 (2 instances)

(y, zf) = lfilter(b, a, axis_reverse(y, axis=axis), axis=axis, zi=zi * y0)

# ==================================================
# Occurrences: Lines 5025-5027 (2 instances)

out = (xp.asarray(x), xp.asarray(zi))

# ==================================================
# Occurrences: Lines 5139-5140 (2 instances)

(y, zf) = sosfilt(sos, axis_reverse(y, axis=axis), axis=axis, zi=zi * y_0)

# ==================================================
# Occurrences: Lines 5260-5265 (2 instances)

sos = np.asarray(sos, dtype=result_type)

# ==================================================
# Occurrences: Lines 5273-5278 (2 instances)

system = ftype._as_tf()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/signal/windows/_windows.py
# Occurrences: Lines 197-200 (2 instances)

return xp.ones(M, dtype=xp.float64, device=device)

# ==================================================
# Line: 1643

k = xp.arange(M, dtype=xp.float64, device=device)

# ==================================================
# Occurrences: Lines 1656-1662 (3 instances)

w = xp.real(sp_fft.fft(p))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_precompute/gammainc_data.py
# Line: 90

t0 = time()

# ==================================================
# Line: 120

print(f"{(time() - t0)/60} minutes elapsed")

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_precompute/wright_bessel_data.py
# Line: 44

t0 = time()

# ==================================================
# Line: 148

print(f"{(time() - t0)/60:.1f} minutes elapsed")

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_precompute/hyp2f1_data.py
# Occurrences: Lines 117-118 (2 instances)

relative_error = float("inf")

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_precompute/wright_bessel.py
# Line: 319

t0 = time()

# ==================================================
# Line: 338

print(f"\n{(time() - t0)/60:.1f} minutes elapsed.\n")

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_mptestutils.py
# Line: 69

right = np.log10(linpts[1])

# ==================================================
# Line: 86

right = np.log10(linpts[1])

# ==================================================
# Occurrences: Lines 389-392 (6 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_testutils.py
# Occurrences: Lines 249-252 (8 instances)

pinf_x = np.isinf(x)

# ==================================================
# Occurrences: Lines 262-267 (4 instances)

abs_y = np.absolute(y)

# ==================================================
# Occurrences: Lines 286-287 (4 instances)

inf_x = np.isinf(x)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_generate_pyx.py
# Line: 541

if len(inp) != inarg_num or len(outp) != outarg_num:

# ==================================================
# Occurrences: Lines 552-555 (2 instances)

ret = ret.replace('*', '')

# ==================================================
# Line: 563

ret = ret.replace('*', '')

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_basic.py
# Line: 2953

result = np.array(result)

# ==================================================
# Line: 2967

result = np.array(result)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/_decomp_qr.py
# Occurrences: Lines 19-21 (2 instances)

ret = f(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/_matfuncs_inv_ssq.py
# Occurrences: Lines 193-203 (4 instances)

return np.sqrt(a) - 1

# ==================================================
# Line: 377

T = _sqrtm_triu(T)

# ==================================================
# Occurrences: Lines 404-404 (2 instances)

T = _sqrtm_triu(T)

# ==================================================
# Occurrences: Lines 416-416 (2 instances)

T = _sqrtm_triu(T)

# ==================================================
# Line: 560

T0_diag = np.diag(T0)

# ==================================================
# Line: 576

eivals = np.diag(T0)

# ==================================================
# Line: 695

a = int(np.floor(p))

# ==================================================
# Line: 702

Q = np.linalg.matrix_power(A, a)

# ==================================================
# Occurrences: Lines 714-717 (2 instances)

a = int(np.floor(p))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/interpolative.py
# Line: 504

k = int(eps_or_k)

# ==================================================
# Line: 526

k = int(eps_or_k)

# ==================================================
# Occurrences: Lines 845-853 (5 instances)

V = V.T.conj()

# ==================================================
# Occurrences: Lines 862-865 (2 instances)

V = V.T.conj()

# ==================================================
# Line: 874

k = int(eps_or_k)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/_solvers.py
# Occurrences: Lines 537-541 (2 instances)

n_u_sym = norm(u_sym, 1)

# ==================================================
# Occurrences: Lines 747-751 (2 instances)

n_u_sym = norm(u_sym, 1)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/_testutils.py
# Line: 28

x = np.zeros(shape, dtype=dtype)

# ==================================================
# Line: 34

x = np.zeros(shape, dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/_decomp.py
# Occurrences: Lines 79-87 (4 instances)

alpha, beta, vl, vr, work, info = ggev(a1, b1, cvl, cvr, lwork,
                                       overwrite_a, overwrite_b)

# ==================================================
# Occurrences: Lines 221-223 (3 instances)

w = _make_eigvals(w, None, homogeneous_eigvals)

# ==================================================
# Occurrences: Lines 251-262 (4 instances)

w, vl, vr, info = geev(a1, lwork=lwork,
                       compute_vl=compute_vl,
                       compute_vr=compute_vr,
                       overwrite_a=overwrite_a)

# ==================================================
# Occurrences: Lines 609-614 (2 instances)

msg = drv_err['ev'].format(info)

# ==================================================
# Line: 809

bevd, = get_lapack_funcs((internal_name,), (a1,))

# ==================================================
# Line: 825

bevx, = get_lapack_funcs((internal_name,), (a1,))

# ==================================================
# Occurrences: Lines 1348-1358 (5 instances)

m = len(w)

# ==================================================
# Line: 1460

h = np.empty(a1.shape, dtype=h3.dtype)

# ==================================================
# Line: 1466

h = np.empty(a1.shape, dtype=h3.dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/_generate_pyx.py
# Occurrences: Lines 566-569 (2 instances)

blas_sigs = f.readlines()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/_decomp_lu.py
# Occurrences: Lines 321-328 (4 instances)

PL = np.empty(shape=[*nd, m, k], dtype=a1.dtype)

# ==================================================
# Line: 344

a1 = a1.copy(order='C')

# ==================================================
# Line: 352

a1 = a1.copy(order='C')

# ==================================================
# Line: 367

U = np.zeros([*nd, k, k], dtype=a1.dtype)

# ==================================================
# Line: 373

L = np.zeros([*nd, k, k], dtype=a1.dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/_matfuncs.py
# Occurrences: Lines 338-338 (2 instances)

eA[ind] = np.diag(np.exp(np.diag(aw)))

# ==================================================
# Occurrences: Lines 370-370 (2 instances)

diag_aw = np.diag(aw)

# ==================================================
# Line: 520

a = a.astype(np.float64)

# ==================================================
# Line: 526

a = a.astype(np.float64)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/linalg/_basic.py
# Line: 1319

a1 = a1.copy(order='C')

# ==================================================
# Line: 1326

a1 = a1.copy(order='C')

# ==================================================
# Occurrences: Lines 1475-1476 (2 instances)

residues = np.empty((0,))

# ==================================================
# Line: 1508

lwork = _compute_lwork(lapack_lwork, m, n, nrhs, cond)

# ==================================================
# Occurrences: Lines 1515-1520 (2 instances)

lwork, iwork = _compute_lwork(lapack_lwork, m, n, nrhs, cond)

# ==================================================
# Line: 1538

lwork = _compute_lwork(lapack_lwork, m, n, nrhs, cond)

# ==================================================
# Line: 1901

perm = np.arange(n)

# ==================================================
# Line: 1921

iperm[perm] = np.arange(n)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/fft/_fftlog_backend.py
# Occurrences: Lines 80-81 (2 instances)

u = np.empty(n//2+1, dtype=complex)

# ==================================================
# Occurrences: Lines 110-115 (2 instances)

u = np.copy(u)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/fft/_basic_backend.py
# Line: 31

x = np.asarray(x)

# ==================================================
# Occurrences: Lines 40-47 (4 instances)

res = xp_func(x, n=n, axis=axis, norm=norm)

# ==================================================
# Line: 56

x = np.asarray(x)

# ==================================================
# Occurrences: Lines 65-72 (4 instances)

res = xp_func(x, s=s, axes=axes, norm=norm)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/decorator.py
# Occurrences: Lines 223-228 (2 instances)

args, kw = fix(args, kw, sig)

# ==================================================
# Line: 234

args, kw = fix(args, kw, sig)

# ==================================================
# Occurrences: Lines 389-389 (2 instances)

if issubclass(t, type_) and type_ not in t.mro():

# ==================================================
# Occurrences: Lines 408-408 (2 instances)

mro = t.mro()

# ==================================================
# Occurrences: Lines 430-430 (2 instances)

for ancs in itertools.product(*ancestors(*types)):

# ==================================================
# Occurrences: Lines 442-442 (2 instances)

combinations = itertools.product(*ancestors(*types))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/_bunch.py
# Occurrences: Lines 206-211 (2 instances)

class_namespace[name] = property(_get)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/deprecation.py
# Occurrences: Lines 266-267 (4 instances)

doc = str(doc).split("\n", 1)[1]  # remove signature

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/_elementwise_iterative_method.py
# Occurrences: Lines 212-222 (4 instances)

res_dict['nit'] = xp.zeros(n_elements, dtype=xp.int32)

# ==================================================
# Occurrences: Lines 253-258 (2 instances)

active = _check_termination(work, res, res_work_pairs, active,
                            check_termination, preserve_shape, xp)

# ==================================================
# Line: 268

return _prepare_result(work, res, res_work_pairs, active, shape,
                       customize_result, preserve_shape, xp)

# ==================================================
# Occurrences: Lines 317-322 (2 instances)

res[key] = xpx.at(res[key])[active_mask].set(val)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/pyprima/pyprima/src/pyprima/__init__.py
# Line: 149

newx = np.zeros(lenx0)

# ==================================================
# Occurrences: Lines 173-178 (2 instances)

f = fun(x, *args)

# ==================================================
# Line: 208

newx = np.zeros(lenx0)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/pyprima/pyprima/src/pyprima/common/selectx.py
# Line: 135

if sum(keep) == maxfilt:  # In this case, NFILT = SIZE(KEEP) = COUNT(KEEP) = MAXFILT > 0.

# ==================================================
# Line: 164

nfilt = sum(keep)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/pyprima/pyprima/src/pyprima/common/linalg.py
# Line: 150

B = np.zeros((n, n))

# ==================================================
# Line: 156

B = np.zeros((n, n))

# ==================================================
# Line: 164

B = np.zeros((n, n))

# ==================================================
# Occurrences: Lines 262-263 (2 instances)

c = 1 / np.sqrt(2) * np.sign(x[0])

# ==================================================
# Line: 273

c = np.sign(x[0])

# ==================================================
# Line: 280

s = np.sign(x[1])

# ==================================================
# Line: 295

u *= np.sign(x[0]) ##MATLAB: u = sign(x(1))*sqrt(1 + t**2)

# ==================================================
# Line: 301

u *= np.sign(x[1]) ##MATLAB: u = sign(x(2))*sqrt(1 + t**2)

# ==================================================
# Occurrences: Lines 353-359 (3 instances)

n = np.size(A, 0)

# ==================================================
# Line: 367

tol = tol if present(tol) else np.minimum(1e-3, 1e2 * EPS * np.maximum(np.size(A, 0), np.size(A, 1)))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/pyprima/pyprima/src/pyprima/common/_bounds.py
# Occurrences: Lines 23-24 (2 instances)

lb = np.concatenate((lb, -np.inf*np.ones(lenx0 - len(lb))))

# ==================================================
# Occurrences: Lines 31-32 (2 instances)

lb = np.concatenate((lb, -np.inf*np.ones(lenx0 - len(lb))))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/pyprima/pyprima/src/pyprima/common/message.py
# Occurrences: Lines 86-89 (2 instances)

is_constrained = present(cstrv)

# ==================================================
# Occurrences: Lines 149-152 (2 instances)

is_constrained = present(cstrv)

# ==================================================
# Occurrences: Lines 250-253 (2 instances)

is_constrained = present(cstrv)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/pyprima/pyprima/src/pyprima/common/_nonlinear_constraints.py
# Occurrences: Lines 19-19 (2 instances)

_ = len(lb)

# ==================================================
# Occurrences: Lines 25-25 (2 instances)

_ = len(ub)

# ==================================================
# Occurrences: Lines 31-33 (4 instances)

if len(values) != len(lb):

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/pyprima/pyprima/src/pyprima/cobyla/cobyla.py
# Occurrences: Lines 504-506 (2 instances)

num_vars = len(xl)

# ==================================================
# Occurrences: Lines 514-514 (2 instances)

assert (xl is None or xu is None) or len(xl) == len(xu) == num_vars

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/pyprima/pyprima/src/pyprima/cobyla/cobylb.py
# Occurrences: Lines 43-44 (3 instances)

A = np.zeros((np.size(x), np.size(constr))) # A contains the approximate gradient for the constraints

# ==================================================
# Occurrences: Lines 62-64 (2 instances)

num_constraints = np.size(constr)

# ==================================================
# Occurrences: Lines 103-105 (2 instances)

confilt = np.zeros((np.size(constr), np.size(cfilt)))

# ==================================================
# Line: 124

assert np.size(x) == num_vars and not any(np.isnan(x))

# ==================================================
# Occurrences: Lines 195-196 (2 instances)

conmat, cval, fval, sim, simi, subinfo = updatepole(cpen, conmat, cval, fval,
                                                    sim, simi)

# ==================================================
# Occurrences: Lines 204-204 (2 instances)

adequate_geo = all(primasum(primapow2(sim[:, :num_vars]), axis=0) <= 4 * primapow2(delta))

# ==================================================
# Occurrences: Lines 269-272 (6 instances)

distsq[num_vars] = primasum(primapow2(x - sim[:, num_vars]))

# ==================================================
# Occurrences: Lines 280-288 (6 instances)

f, constr = evaluate(calcfc, x, m_nlcon, amat, bvec)

# ==================================================
# Occurrences: Lines 349-349 (2 instances)

subinfo = checkbreak_con(maxfun, nf, cstrv, ctol, f, ftarget, x)

# ==================================================
# Occurrences: Lines 423-423 (2 instances)

if improve_geo and not all(primasum(primapow2(sim[:, :num_vars]), axis=0) <= 4 * primapow2(delta)):

# ==================================================
# Occurrences: Lines 467-470 (6 instances)

distsq[num_vars] = primasum(primapow2(x - sim[:, num_vars]))

# ==================================================
# Occurrences: Lines 478-486 (6 instances)

f, constr = evaluate(calcfc, x, m_nlcon, amat, bvec)

# ==================================================
# Occurrences: Lines 498-498 (2 instances)

subinfo = checkbreak_con(maxfun, nf, cstrv, ctol, f, ftarget, x)

# ==================================================
# Occurrences: Lines 510-511 (4 instances)

delta = max(0.5 * rho, redrho(rho, rhoend))

# ==================================================
# Occurrences: Lines 517-517 (2 instances)

conmat, cval, fval, sim, simi, subinfo = updatepole(cpen, conmat, cval, fval, sim, simi)

# ==================================================
# Occurrences: Lines 540-544 (3 instances)

f, constr = evaluate(calcfc, x, m_nlcon, amat, bvec)

# ==================================================
# Occurrences: Lines 580-586 (4 instances)

A = np.zeros((np.size(sim, 0), np.size(conmat, 0)))

# ==================================================
# Occurrences: Lines 593-598 (2 instances)

assert np.size(conmat, 0) == num_constraints and np.size(conmat, 1) == num_vars + 1

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/pyprima/pyprima/src/pyprima/cobyla/update.py
# Line: 27

num_vars = np.size(sim, 0)

# ==================================================
# Line: 42

assert np.size(sim, 0) == num_vars and np.size(sim, 1) == num_vars + 1

# ==================================================
# Occurrences: Lines 63-68 (2 instances)

simi -= outprod(matprod(simi, d), simi_jdrop)

# ==================================================
# Line: 106

assert np.size(sim, 0) == num_vars and np.size(sim, 1) == num_vars + 1

# ==================================================
# Line: 214

jopt = findpole(cpen, cval, fval)

# ==================================================
# Line: 276

assert findpole(cpen, cval, fval) == num_vars or info == DAMAGING_ROUNDING

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/pyprima/pyprima/src/pyprima/cobyla/geometry.py
# Line: 32

num_vars = np.size(sim, 0)

# ==================================================
# Line: 39

assert np.size(sim, 0) == num_vars and np.size(sim, 1) == num_vars + 1

# ==================================================
# Occurrences: Lines 173-174 (2 instances)

num_constraints = np.size(conmat, 0)

# ==================================================
# Occurrences: Lines 182-185 (2 instances)

assert np.size(simi, 0) == num_vars and np.size(simi, 1) == num_vars

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/_docscrape.py
# Line: 202

section = self._doc.read_to_next_empty_line()

# ==================================================
# Line: 208

section += self._doc.read_to_next_empty_line()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/_util.py
# Occurrences: Lines 364-365 (4 instances)

doc = str(doc).split("\n", 1)[1]  # remove signature

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_root_scalar.py
# Line: 304

kwargs['tol'] = kwargs.pop('xtol')

# ==================================================
# Line: 326

kwargs['tol'] = kwargs.pop('xtol')

# ==================================================
# Line: 337

kwargs['tol'] = kwargs.pop('xtol')

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_linprog_rs.py
# Line: 53

residual = c.dot(x)

# ==================================================
# Line: 67

residual = c.dot(x)

# ==================================================
# Line: 166

x = np.zeros(n)

# ==================================================
# Occurrences: Lines 187-192 (3 instances)

c = np.zeros(n)

# ==================================================
# Line: 234

basis = _get_more_basis_columns(A, basis)  # add columns as needed

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_lbfgsb_py.py
# Occurrences: Lines 406-407 (2 instances)

low_bnd = zeros(n, float64)

# ==================================================
# Occurrences: Lines 432-433 (2 instances)

task = zeros(2, dtype=np.int32)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_spectral.py
# Line: 94

F_0_norm = fnorm(F_k)

# ==================================================
# Line: 107

F_k_norm = fnorm(F_k)

# ==================================================
# Line: 224

f = fmerit(F)

# ==================================================
# Occurrences: Lines 236-239 (2 instances)

f = fmerit(F)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_tnc.py
# Line: 373

n = len(x0)

# ==================================================
# Occurrences: Lines 400-401 (2 instances)

low = zeros(n)

# ==================================================
# Occurrences: Lines 417-423 (3 instances)

scale = array([])

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_shgo.py
# Occurrences: Lines 1462-1464 (2 instances)

self.C = self.sampling_function(n, dim)

# ==================================================
# Line: 1507

self.Tri = spatial.Delaunay(self.C,
                            incremental=self.qhull_incremental,
                            )

# ==================================================
# Line: 1520

self.Tri = spatial.Delaunay(self.C,
                            incremental=
                            self.qhull_incremental)

# ==================================================
# Line: 1589

self.f_maps = np.array(self.f_maps)

# ==================================================
# Line: 1596

self.f_maps = np.array(self.f_maps)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_numdiff.py
# Line: 559

rel_step = _eps_for_method(x0.dtype, f0.dtype, method)

# ==================================================
# Line: 576

_eps_for_method(x0.dtype, f0.dtype, method) *

# ==================================================
# Line: 631

df = fun(x) - f0

# ==================================================
# Line: 654

f1 = fun(x)

# ==================================================
# Line: 678

x1 = np.copy(x0)

# ==================================================
# Occurrences: Lines 693-694 (6 instances)

x1 = np.copy(x0)

# ==================================================
# Occurrences: Lines 706-715 (10 instances)

f_evals = iter(workers(fun, x_generator3(x0, h, use_one_sided)))

# ==================================================
# Line: 763

e_gen = e_generator()

# ==================================================
# Occurrences: Lines 770-774 (7 instances)

e_gen = e_generator()

# ==================================================
# Line: 787

e_gen = e_generator()

# ==================================================
# Occurrences: Lines 794-802 (5 instances)

f_evals = iter(workers(fun, x_generator2()))

# ==================================================
# Occurrences: Lines 812-819 (8 instances)

dx = next(xs) - x0

# ==================================================
# Occurrences: Lines 828-829 (4 instances)

f1 = next(f_evals)

# ==================================================
# Occurrences: Lines 841-841 (2 instances)

f1 = next(f_evals)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_trustregion_constr/equality_constrained_sqp.py
# Occurrences: Lines 78-81 (2 instances)

S = scaling(x)

# ==================================================
# Occurrences: Lines 98-101 (2 instances)

H = lagr_hess(x, v)

# ==================================================
# Occurrences: Lines 215-225 (4 instances)

S = scaling(x)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_trustregion_constr/projections.py
# Line: 69

v = factor(A.dot(x))

# ==================================================
# Line: 87

return factor(A.dot(x))

# ==================================================
# Occurrences: Lines 121-124 (2 instances)

v = np.hstack([x, np.zeros(m)])

# ==================================================
# Occurrences: Lines 155-158 (2 instances)

v = np.hstack([x, np.zeros(m)])

# ==================================================
# Line: 172

lu_sol = solve(v)

# ==================================================
# Occurrences: Lines 197-199 (4 instances)

aux1 = Q.T.dot(x)

# ==================================================
# Occurrences: Lines 211-211 (2 instances)

aux2 = scipy.linalg.solve_triangular(R, aux1, lower=False)

# ==================================================
# Occurrences: Lines 222-224 (3 instances)

aux1 = Q.T.dot(x)

# ==================================================
# Occurrences: Lines 255-257 (3 instances)

aux1 = Vt.dot(x)

# ==================================================
# Occurrences: Lines 269-269 (2 instances)

v = U.dot(aux2)

# ==================================================
# Occurrences: Lines 279-281 (2 instances)

aux1 = Vt.dot(x)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_trustregion_constr/canonical_constraint.py
# Line: 153

empty_fun = np.empty(0)

# ==================================================
# Occurrences: Lines 161-163 (2 instances)

empty_jac = sps.csr_array((0, n))

# ==================================================
# Occurrences: Lines 174-179 (3 instances)

empty_fun = np.empty(0)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_trustregion_constr/qp_subproblem.py
# Line: 383

_, alpha, intersect = box_sphere_intersections(z, p, lb, ub,
                                               trust_radius)

# ==================================================
# Line: 392

_, alpha, _ = box_sphere_intersections(z, p, lb, ub,
                                       trust_radius)

# ==================================================
# Line: 400

_, alpha, _ = box_sphere_intersections(z, p, lb, ub,
                                       trust_radius)

# ==================================================
# Line: 506

H_p = H.dot(p)

# ==================================================
# Occurrences: Lines 566-566 (2 instances)

x = reinforce_box_boundaries(x, lb, ub)

# ==================================================
# Occurrences: Lines 579-580 (2 instances)

_, theta, intersect = box_sphere_intersections(x, alpha*p, lb, ub,
                                               trust_radius)

# ==================================================
# Occurrences: Lines 586-586 (2 instances)

x = reinforce_box_boundaries(x, lb, ub)

# ==================================================
# Occurrences: Lines 599-600 (2 instances)

_, theta, intersect = box_sphere_intersections(x, alpha*p, lb, ub,
                                               trust_radius)

# ==================================================
# Line: 628

H_p = H.dot(p)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_trustregion_constr/minimize_trustregion_constr.py
# Line: 455

callback_stop = callback(state)

# ==================================================
# Line: 500

callback_stop = callback(state)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_trustregion_constr/tr_interior_point.py
# Occurrences: Lines 198-199 (2 instances)

new_indices = np.empty(size)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_shgo_lib/_complex.py
# Occurrences: Lines 277-277 (2 instances)

ab_Cc = copy.copy(ab_C)

# ==================================================
# Occurrences: Lines 319-319 (2 instances)

ab_Cc = copy.copy(ab_C)

# ==================================================
# Line: 435

self.cp = self.cyclic_product(cbounds, origin, supremum, centroid)

# ==================================================
# Line: 451

self.cp = self.cyclic_product(cbounds, origin, supremum,
                              centroid)

# ==================================================
# Occurrences: Lines 558-561 (2 instances)

vco = self.split_edge(vo.x, vs.x)  # Split in case not centroid arg

# ==================================================
# Line: 571

a_vl = copy.copy(list(vot))

# ==================================================
# Occurrences: Lines 577-581 (3 instances)

vco = self.split_edge(vo.x, vs.x)  # Split in case not centroid arg

# ==================================================
# Occurrences: Lines 649-649 (3 instances)

d_bc_vc = self.split_edge(vectors[0].x, bc_vc.x)

# ==================================================
# Occurrences: Lines 673-674 (4 instances)

os_v = self.split_edge(vectors[1].x, ba_vu.x)  # o-s

# ==================================================
# Occurrences: Lines 682-689 (7 instances)

d_bc_vc = self.split_edge(vectors[0].x, bc_vc.x)

# ==================================================
# Occurrences: Lines 702-702 (2 instances)

comb_iter = itertools.combinations(comb, 2)

# ==================================================
# Occurrences: Lines 725-725 (3 instances)

d_bc_vc = self.split_edge(vectors[0].x, bc_vc.x)

# ==================================================
# Occurrences: Lines 749-750 (4 instances)

os_v = self.split_edge(vectors[1].x, ba_vu.x)  # o-s

# ==================================================
# Occurrences: Lines 756-771 (11 instances)

d_bc_vc = self.split_edge(vectors[0].x, bc_vc.x)

# ==================================================
# Occurrences: Lines 779-779 (2 instances)

comb_iter = itertools.combinations(comb, 2)

# ==================================================
# Occurrences: Lines 800-800 (2 instances)

c_vc = self.split_edge(vl.x, a_vu.x)

# ==================================================
# Occurrences: Lines 815-815 (2 instances)

c_vu = self.split_edge(vu.x, a_vu.x)

# ==================================================
# Occurrences: Lines 858-858 (2 instances)

d_bc_vc = self.split_edge(vectors[1].x, ba_vu.x)  # o-s

# ==================================================
# Occurrences: Lines 867-868 (4 instances)

d_ba_vl = self.split_edge(vectors[3].x, ba_vl.x)

# ==================================================
# Occurrences: Lines 877-877 (2 instances)

comb_iter = itertools.combinations(comb, 2)

# ==================================================
# Occurrences: Lines 896-896 (2 instances)

c_vc = self.split_edge(vl.x, a_vu.x)

# ==================================================
# Occurrences: Lines 904-905 (2 instances)

c_vu = self.split_edge(vu.x,
                       a_vu.x)  # yield at end of loop

# ==================================================
# Occurrences: Lines 1111-1112 (2 instances)

S_rows = np.array(S_rows)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_minpack_py.py
# Occurrences: Lines 516-516 (2 instances)

return f(params)

# ==================================================
# Occurrences: Lines 523-523 (2 instances)

val = f(params)

# ==================================================
# Line: 976

sigma = np.asarray(sigma)

# ==================================================
# Line: 985

sigma = np.asarray(sigma)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_lsq/bvls.py
# Occurrences: Lines 33-38 (2 instances)

free_set, = np.nonzero(free_set)

# ==================================================
# Line: 58

optimality = compute_kkt_optimality(g, on_bound)

# ==================================================
# Line: 92

g = A.T.dot(r)

# ==================================================
# Line: 108

optimality = compute_kkt_optimality(g, on_bound)

# ==================================================
# Line: 127

free_set, = np.nonzero(free_set)

# ==================================================
# Occurrences: Lines 174-175 (2 instances)

g = A.T.dot(r)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_lsq/trf.py
# Line: 132

p_value = evaluate_quadratic(J_h, g_h, p_h, diag=diag_h)

# ==================================================
# Line: 181

p_value = evaluate_quadratic(J_h, g_h, p_h, diag=diag_h)

# ==================================================
# Line: 212

f_true = f.copy()

# ==================================================
# Occurrences: Lines 220-226 (3 instances)

rho = loss_function(f)

# ==================================================
# Line: 240

g_norm = norm(g * v, ord=np.inf)

# ==================================================
# Line: 265

g_norm = norm(g * v, ord=np.inf)

# ==================================================
# Line: 372

f_true = f.copy()

# ==================================================
# Occurrences: Lines 380-383 (3 instances)

rho = loss_function(f)

# ==================================================
# Line: 421

f_true = f.copy()

# ==================================================
# Occurrences: Lines 429-435 (3 instances)

rho = loss_function(f)

# ==================================================
# Line: 547

f_true = f.copy()

# ==================================================
# Occurrences: Lines 555-558 (3 instances)

rho = loss_function(f)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_lsq/least_squares.py
# Line: 1021

tr_options.copy(), verbose, callback=callback_wrapped)

# ==================================================
# Line: 1028

tr_options = tr_options.copy()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_lsq/dogbox.py
# Line: 154

f_true = f.copy()

# ==================================================
# Occurrences: Lines 161-167 (3 instances)

rho = loss_function(f)

# ==================================================
# Line: 307

f_true = f.copy()

# ==================================================
# Occurrences: Lines 315-318 (3 instances)

rho = loss_function(f)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_lsq/trf_linear.py
# Line: 166

g = compute_grad(A, r)

# ==================================================
# Line: 234

g = compute_grad(A, r)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_lsq/common.py
# Line: 514

return y, np.ones_like(y)

# ==================================================
# Line: 536

g = np.ones_like(y)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_slsqp_py.py
# Occurrences: Lines 394-395 (2 instances)

xl = np.empty(n, dtype=float)

# ==================================================
# Line: 571

temp = np.atleast_1d(con['fun'](x, *con['args'])).ravel()

# ==================================================
# Line: 578

temp = np.atleast_1d(con['fun'](x, *con['args'])).ravel()

# ==================================================
# Line: 592

temp = np.atleast_2d(con['jac'](x, *con['args']))

# ==================================================
# Line: 599

temp = np.atleast_2d(con['jac'](x, *con['args']))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_nonlin.py
# Occurrences: Lines 180-181 (2 instances)

Fx = func(x)

# ==================================================
# Occurrences: Lines 227-228 (2 instances)

Fx = func(x)

# ==================================================
# Line: 277

tmp_phi = [norm(Fx)**2]

# ==================================================
# Line: 313

Fx_norm = norm(Fx)

# ==================================================
# Occurrences: Lines 929-933 (2 instances)

r = self.Gm.matvec(f)

# ==================================================
# Occurrences: Lines 1152-1156 (2 instances)

while len(self.dx) > self.M:

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_dual_annealing.py
# Line: 278

self.xmin = np.copy(self.energy_state.current_location)

# ==================================================
# Line: 284

self.xmin = np.copy(self.energy_state.current_location)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_remove_redundancy.py
# Line: 400

U, s, Vh = svd(A)

# ==================================================
# Line: 447

U, s, Vh = svd(A)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_tstutils.py
# Occurrences: Lines 130-132 (2 instances)

v = random()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_linprog_util.py
# Line: 617

and rr_method.lower() not in {"svd", "pivot", "id"}):

# ==================================================
# Occurrences: Lines 819-820 (2 instances)

b_eq = np.array([])

# ==================================================
# Occurrences: Lines 886-898 (5 instances)

rr_res = _remove_redundancy_svd(A_eq, b_eq)

# ==================================================
# Occurrences: Lines 1146-1149 (4 instances)

lb_none = np.equal(lbs, -np.inf)

# ==================================================
# Occurrences: Lines 1157-1160 (4 instances)

lb_none = np.equal(lbs, -np.inf)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_trustregion_exact.py
# Occurrences: Lines 300-302 (2 instances)

U, info = self.cholesky(H, lower=False,
                        overwrite_a=False,
                        clean=True)

# ==================================================
# Occurrences: Lines 331-331 (2 instances)

s_min, z_min = estimate_smallest_singular_value(U)

# ==================================================
# Occurrences: Lines 358-360 (2 instances)

c, info = self.cholesky(H, lower=False,
                        overwrite_a=False,
                        clean=True)

# ==================================================
# Occurrences: Lines 399-399 (2 instances)

s_min, z_min = estimate_smallest_singular_value(U)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_trustregion_ncg.py
# Occurrences: Lines 96-96 (2 instances)

ta, tb = self.get_boundaries_intersections(z, d, trust_radius)

# ==================================================
# Occurrences: Lines 111-111 (2 instances)

ta, tb = self.get_boundaries_intersections(z, d, trust_radius)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_hessian_update_strategy.py
# Occurrences: Lines 146-148 (2 instances)

self.B = np.eye(n, dtype=float)

# ==================================================
# Occurrences: Lines 388-390 (2 instances)

wz = np.dot(w, z)

# ==================================================
# Line: 403

wMw = Mw.dot(w)

# ==================================================
# Line: 417

wz = np.dot(w, z)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_constraints.py
# Line: 510

y = np.array(fun(x)).flatten()

# ==================================================
# Line: 516

dy = jac(x)

# ==================================================
# Line: 529

y_all = np.array(fun(x)).flatten()

# ==================================================
# Line: 538

dy_all = jac(x)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_linesearch.py
# Line: 405

phi_a1 = phi(alpha1)

# ==================================================
# Line: 463

phi_a1 = phi(alpha1)

# ==================================================
# Occurrences: Lines 795-795 (2 instances)

fp, Fp = f(xp)

# ==================================================
# Occurrences: Lines 804-804 (2 instances)

fp, Fp = f(xp)

# ==================================================
# Occurrences: Lines 871-871 (2 instances)

fp, Fp = f(xp)

# ==================================================
# Occurrences: Lines 880-880 (2 instances)

fp, Fp = f(xp)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_zeros_py.py
# Line: 308

fval = func(p0, *args)

# ==================================================
# Occurrences: Lines 357-359 (2 instances)

q0 = func(p0, *args)

# ==================================================
# Line: 387

q1 = func(p1, *args)

# ==================================================
# Line: 408

failures = np.ones_like(p, dtype=bool)

# ==================================================
# Line: 414

fval = np.asarray(func(p, *args))

# ==================================================
# Occurrences: Lines 440-442 (3 instances)

q0 = np.asarray(func(p, *args))

# ==================================================
# Line: 463

q1 = np.asarray(func(p1, *args))

# ==================================================
# Occurrences: Lines 1033-1036 (2 instances)

xvals = np.asarray(xvals)

# ==================================================
# Occurrences: Lines 1045-1050 (4 instances)

xvals = np.asarray(xvals)

# ==================================================
# Occurrences: Lines 1064-1065 (2 instances)

Q = np.zeros([N, N])

# ==================================================
# Occurrences: Lines 1211-1214 (3 instances)

return _ECONVERGED, sum(self.ab) / 2.0

# ==================================================
# Line: 1239

fc = self._callf(c)

# ==================================================
# Line: 1245

d, fd = self._update_bracket(c, fc)

# ==================================================
# Line: 1255

c = sum(self.ab) / 2.0

# ==================================================
# Occurrences: Lines 1272-1284 (4 instances)

c = sum(self.ab) / 2.0

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_differentialevolution.py
# Occurrences: Lines 1596-1601 (4 instances)

energy = self.func(parameters)

# ==================================================
# Line: 1887

x = np.asarray(x)

# ==================================================
# Line: 1910

return np.asarray(x)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_linprog_ip.py
# Line: 233

solve = _get_solver(M, sparse, lstsq, sym_pos, cholesky, permc_spec)

# ==================================================
# Line: 324

solve = _get_solver(M, sparse, lstsq, sym_pos,
                    cholesky, permc_spec)

# ==================================================
# Occurrences: Lines 464-466 (2 instances)

x0 = np.ones(n)

# ==================================================
# Line: 723

rho_p, rho_d, rho_A, rho_g, rho_mu, obj = _indicators(
    A, b, c, c0, x, y, z, tau, kappa)

# ==================================================
# Line: 730

x_o, fun, slack, con = _postsolve(x/tau, postsolve_args)

# ==================================================
# Occurrences: Lines 774-776 (2 instances)

x, y, z, tau, kappa = _do_step(
    x, y, z, tau, kappa, d_x, d_y,
    d_z, d_tau, d_kappa, alpha)

# ==================================================
# Occurrences: Lines 787-788 (2 instances)

x, y, z, tau, kappa = _do_step(
    x, y, z, tau, kappa, d_x, d_y, d_z, d_tau, d_kappa, alpha)

# ==================================================
# Occurrences: Lines 796-801 (3 instances)

message = _get_message(status)

# ==================================================
# Line: 807

x_o, fun, slack, con = _postsolve(x/tau, postsolve_args)

# ==================================================
# Occurrences: Lines 824-828 (4 instances)

message = _get_message(status)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_dcsrch.py
# Occurrences: Lines 469-472 (2 instances)

if abs(self.sty - self.stx) >= p66 * self.width1:

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_qap.py
# Line: 680

N = len(A)

# ==================================================
# Line: 701

elif (partial_guess >= len(A)).any():

# ==================================================
# Occurrences: Lines 713-716 (4 instances)

guess_rows = np.zeros(N, dtype=bool)

# ==================================================
# Occurrences: Lines 732-738 (4 instances)

perm[random_rows] = rng.permutation(np.arange(N)[random_cols])

# ==================================================
# Line: 750

score = _calc_score(A, B, perm)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_direct_py.py
# Line: 248

x = np.asarray(x)

# ==================================================
# Line: 278

return OptimizeResult(x=np.asarray(x), fun=fun, status=ret_code,

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_differentiable_functions.py
# Occurrences: Lines 336-337 (2 instances)

_x = xpx.atleast_nd(self.xp.asarray(x), ndim=1, xp=self.xp)

# ==================================================
# Occurrences: Lines 345-346 (2 instances)

_x = xpx.atleast_nd(self.xp.asarray(x), ndim=1, xp=self.xp)

# ==================================================
# Line: 588

self.x_diff = np.copy(self.x)

# ==================================================
# Line: 597

self.x_diff = np.copy(self.x)

# ==================================================
# Occurrences: Lines 683-684 (2 instances)

_x = xpx.atleast_nd(self.xp.asarray(x), ndim=1, xp=self.xp)

# ==================================================
# Occurrences: Lines 690-691 (2 instances)

_x = xpx.atleast_nd(self.xp.asarray(x), ndim=1, xp=self.xp)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_optimize.py
# Line: 763

dim = float(len(x0))

# ==================================================
# Line: 791

N = len(x0)

# ==================================================
# Line: 808

if len(x0) != sim.shape[1]:

# ==================================================
# Occurrences: Lines 855-862 (6 instances)

ind = np.argsort(fsim)

# ==================================================
# Occurrences: Lines 931-933 (3 instances)

ind = np.argsort(fsim)

# ==================================================
# Line: 1121

_grad = np.asanyarray(grad(x0, *args))

# ==================================================
# Line: 1135

analytical_grad = grad(x0, *args)

# ==================================================
# Line: 1414

maxiter = len(x0) * 200

# ==================================================
# Line: 1427

N = len(x0)

# ==================================================
# Line: 1438

gnorm = vecnorm(gfk, ord=norm)

# ==================================================
# Line: 1466

gnorm = vecnorm(gfk, ord=norm)

# ==================================================
# Occurrences: Lines 1799-1799 (2 instances)

deltak = np.dot(gfk, gfk)

# ==================================================
# Occurrences: Lines 1828-1828 (2 instances)

return np.dot(pk, gfk) <= -sigma_3 * np.dot(gfk, gfk)

# ==================================================
# Occurrences: Lines 2120-2120 (2 instances)

dri0 = np.dot(ri, ri)

# ==================================================
# Occurrences: Lines 2154-2154 (2 instances)

dri1 = np.dot(ri, ri)

# ==================================================
# Line: 2336

fx = func(x, *args)

# ==================================================
# Line: 2389

fu = func(x, *args)

# ==================================================
# Occurrences: Lines 2893-2894 (2 instances)

f1 = func(*((x1,) + args))

# ==================================================
# Line: 2910

f2 = func(*((x2,) + args))

# ==================================================
# Line: 2916

f1 = func(*((x1,) + args))

# ==================================================
# Occurrences: Lines 3058-3058 (2 instances)

fw = func(*((w,) + args))

# ==================================================
# Occurrences: Lines 3071-3078 (6 instances)

fw = func(*((w,) + args))

# ==================================================
# Occurrences: Lines 3086-3090 (4 instances)

fw = func(*((w,) + args))

# ==================================================
# Line: 3557

x1 = x.copy()

# ==================================================
# Occurrences: Lines 3567-3571 (2 instances)

fval, x, direc1 = _linesearch_powell(func, x, direc1,
                                     tol=xtol * 100,
                                     lower_bound=lower_bound,
                                     upper_bound=upper_bound,
                                     fval=fval)

# ==================================================
# Line: 3594

x1 = x.copy()

# ==================================================
# Occurrences: Lines 3610-3616 (2 instances)

fval, x, direc1 = _linesearch_powell(
    func, x, direc1,
    tol=xtol * 100,
    lower_bound=lower_bound,
    upper_bound=upper_bound,
    fval=fval
)

# ==================================================
# Line: 4133

text = "".join(text)

# ==================================================
# Line: 4144

text = "".join(text)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/optimize/_highspy/_highs_wrapper.py
# Occurrences: Lines 187-188 (2 instances)

"status": highs.getModelStatus(),

# ==================================================
# Occurrences: Lines 210-211 (2 instances)

"status": highs.getModelStatus(),

# ==================================================
# Line: 217

model_status = highs.getModelStatus()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_stats_py.py
# Line: 118

a = xp.reshape(a, (-1,))

# ==================================================
# Line: 125

a = xp.reshape(a, (-1,))

# ==================================================
# Occurrences: Lines 1554-1560 (4 instances)

pvalue = distribution.cdf(statistic)

# ==================================================
# Line: 2051

if int(idx) != idx:

# ==================================================
# Line: 2063

i = int(idx)

# ==================================================
# Occurrences: Lines 2207-2217 (6 instances)

left = count(a < score)

# ==================================================
# Occurrences: Lines 3602-3605 (2 instances)

uppercut = nobs - int(proportiontocut * nobs)

# ==================================================
# Occurrences: Lines 3884-3889 (3 instances)

if len(samples) < 2:

# ==================================================
# Line: 3973

k = len(samples)

# ==================================================
# Occurrences: Lines 3981-3985 (2 instances)

s_w_t = np.sum(w_t, axis=0)

# ==================================================
# Occurrences: Lines 4220-4231 (6 instances)

rlo = xp.tanh(zlo)

# ==================================================
# Occurrences: Lines 4693-4697 (2 instances)

statistic, _ = pearsonr(x, y, axis=axis, alternative=alternative)

# ==================================================
# Occurrences: Lines 4703-4708 (2 instances)

statistic, _ = pearsonr(x, y, axis=axis, alternative=alternative)

# ==================================================
# Line: 5031

pvalue = hypergeom.cdf(c[0, 0], n1 + n2, n1, n)

# ==================================================
# Line: 5047

plower = hypergeom.cdf(c[0, 0], n1 + n2, n1, n)

# ==================================================
# Line: 5644

NaN = _get_nan(x, y)

# ==================================================
# Line: 5653

return (int((cnt * (cnt - 1) // 2).sum()),

# ==================================================
# Line: 5672

ntie = int((cnt * (cnt - 1) // 2).sum())  # joint ties

# ==================================================
# Line: 5679

NaN = _get_nan(x, y)

# ==================================================
# Occurrences: Lines 5886-5899 (6 instances)

x = _toint64(x)

# ==================================================
# Occurrences: Lines 6232-6235 (2 instances)

low, high = xp.broadcast_arrays(-inf, special.stdtrit(df, p))

# ==================================================
# Line: 6241

ci = special.stdtrit(df, p)

# ==================================================
# Line: 7562

Dplus, d_location = _compute_dplus(cdfvals, x)

# ==================================================
# Line: 7568

Dminus, d_location = _compute_dminus(cdfvals, x)

# ==================================================
# Occurrences: Lines 7574-7575 (2 instances)

Dplus, dplus_location = _compute_dplus(cdfvals, x)

# ==================================================
# Occurrences: Lines 8833-8838 (2 instances)

chi2 = _SimpleChi2(2*n)

# ==================================================
# Line: 8958

high_index = int(bd.isf(p))

# ==================================================
# Line: 8969

high_index = int(bd.isf(p))

# ==================================================
# Line: 9297

pvalue = Y.sf(T2-1)  # Y.pmf(T2) + Y.sf(T2)

# ==================================================
# Line: 9304

pvalue = Y.cdf(T1)

# ==================================================
# Occurrences: Lines 9315-9315 (2 instances)

pvalues = [Y.cdf(T1), Y.sf(T2 - 1)]  # [greater, less]

# ==================================================
# Occurrences: Lines 10220-10223 (2 instances)

x0 = np.average(a, weights=weights)

# ==================================================
# Occurrences: Lines 10509-10513 (2 instances)

if np.amax(x) == np.amin(x) and len(x) > 1:

# ==================================================
# Line: 10662

res = xp.mean(x, axis=axis, keepdims=keepdims)

# ==================================================
# Line: 10691

return xp.mean(x, axis=axis, keepdims=keepdims)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_mstats_basic.py
# Occurrences: Lines 160-165 (2 instances)

if len(args) == 1 and not isinstance(args[0], ndarray):

# ==================================================
# Occurrences: Lines 382-384 (2 instances)

modes = output[tuple(slices)].reshape(newshape)

# ==================================================
# Line: 705

res = scipy.stats._stats_py.SignificanceResult(rs, prob)

# ==================================================
# Line: 725

res = scipy.stats._stats_py.SignificanceResult(rs, prob)

# ==================================================
# Occurrences: Lines 766-781 (6 instances)

new = np.zeros(c+1)

# ==================================================
# Occurrences: Lines 873-874 (2 instances)

corr_x = np.sum([v*k*(k-1) for (k,v) in xties.items()], dtype=float)

# ==================================================
# Occurrences: Lines 897-898 (2 instances)

v1 = (np.sum([v*k*(k-1) for (k, v) in xties.items()], dtype=float) *

# ==================================================
# Line: 1151

x = ma.array(x)

# ==================================================
# Line: 1161

x = ma.array(x)

# ==================================================
# Line: 3401

m = data.mean(0)

# ==================================================
# Line: 3409

if not ma.allclose(v,data.mean(0)):

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_mannwhitneyu.py
# Occurrences: Lines 77-80 (2 instances)

cdfs = np.asarray(self.cdf(kc))

# ==================================================
# Line: 95

indices = np.arange(d, a + 1, d)

# ==================================================
# Line: 101

indices = np.arange(d, a + 1, d)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_continuous_distns.py
# Line: 873

args=(b, len(data), np.log(data).sum()),

# ==================================================
# Line: 890

s1 = np.log(data).sum()

# ==================================================
# Occurrences: Lines 1901-1902 (2 instances)

E1 = random_state.standard_exponential(size=size)

# ==================================================
# Occurrences: Lines 2801-2802 (2 instances)

gamma1 = sc.gamma(1+1/c)

# ==================================================
# Occurrences: Lines 2840-2840 (2 instances)

scale = np.sqrt(v / (sc.gamma(1+2/c) - sc.gamma(1+1/c)**2))

# ==================================================
# Line: 2846

loc = m - scale*sc.gamma(1 + 1/c)

# ==================================================
# Line: 4339

loc = get_loc_from_scale(scale)

# ==================================================
# Line: 4384

loc = floc if floc is not None else get_loc_from_scale(scale)

# ==================================================
# Line: 5323

lm = self._logquasipdf(m, p, b)

# ==================================================
# Line: 5339

umax = np.exp(0.5*self._logquasipdf(m, p, b))

# ==================================================
# Occurrences: Lines 5358-5359 (4 instances)

u = umax * random_state.uniform(size=k)

# ==================================================
# Line: 5379

k1 = np.exp(self._logquasipdf(m, p, b))

# ==================================================
# Occurrences: Lines 5398-5399 (4 instances)

u = random_state.uniform(size=k)

# ==================================================
# Line: 6925

shape, scale = get_shape_scale(loc)

# ==================================================
# Line: 6931

shape, scale = get_shape_scale(loc)

# ==================================================
# Occurrences: Lines 6944-6949 (2 instances)

dL_dLoc_rbrack = dL_dLoc(rbrack)

# ==================================================
# Occurrences: Lines 6965-6970 (2 instances)

dL_dLoc_lbrack = dL_dLoc(lbrack)

# ==================================================
# Line: 6993

shape, scale = get_shape_scale(loc)

# ==================================================
# Line: 7312

a = np.empty(np.shape(h))

# ==================================================
# Line: 7328

a = np.empty(np.shape(h))

# ==================================================
# Line: 8042

mu2 = _lazyselect(condlist, choicelist, (df,), np.nan)

# ==================================================
# Line: 8052

g2 = _lazyselect(condlist, choicelist, (df,), np.nan)

# ==================================================
# Occurrences: Lines 8199-8216 (8 instances)

bt = np.extract(mask, b)

# ==================================================
# Line: 8736

loc_lt1 = np.nextafter(data.min(), -np.inf)

# ==================================================
# Occurrences: Lines 8761-8764 (2 instances)

loc = np.nextafter(data.min(), -np.inf)

# ==================================================
# Line: 8788

scale = np.nextafter(get_scale(data, loc), -np.inf)

# ==================================================
# Line: 8795

scale = np.nextafter(get_scale(data, loc), -np.inf)

# ==================================================
# Line: 8803

rbrack = np.nextafter(data.min(), -np.inf)

# ==================================================
# Line: 8831

scale = np.nextafter(get_scale(data, loc), np.inf)

# ==================================================
# Occurrences: Lines 8837-8845 (4 instances)

return fit_loc_scale_w_shape_lt_1()

# ==================================================
# Occurrences: Lines 9124-9126 (2 instances)

s1 = xm.sum()

# ==================================================
# Occurrences: Lines 9133-9133 (2 instances)

return xm.sum() - scale**2 * (1/xm).sum()

# ==================================================
# Occurrences: Lines 9731-9732 (2 instances)

u0 = random_state.normal(size=size)

# ==================================================
# Line: 10544

return (1 - (quot-1) / (quot - (1 - 1/c)*harm_m/np.log(c)))/log_m

# ==================================================
# Occurrences: Lines 10566-10569 (4 instances)

scale = get_scale(loc)

# ==================================================
# Line: 10585

mn_inf = np.nextafter(mn, -np.inf)

# ==================================================
# Occurrences: Lines 10597-10604 (5 instances)

scale = get_scale(loc)

# ==================================================
# Occurrences: Lines 10613-10616 (2 instances)

return fallback(data, *args, **kwds)

# ==================================================
# Occurrences: Lines 10628-10642 (7 instances)

return fallback(data, *args, **kwds)

# ==================================================
# Occurrences: Lines 10656-10663 (4 instances)

return fallback(data, *args, **kwds)

# ==================================================
# Occurrences: Lines 10672-10673 (2 instances)

scale = fscale or get_scale(loc)

# ==================================================
# Line: 10689

upper=get_c(loc, scale))

# ==================================================
# Occurrences: Lines 10698-10702 (3 instances)

logm = log_mean(std_data)

# ==================================================
# Line: 10711

return fallback(data, *args, **kwds)

# ==================================================
# Occurrences: Lines 10726-10733 (3 instances)

scale = get_scale(loc)

# ==================================================
# Line: 10741

params_super = fallback(data, *args, **kwds)

# ==================================================
# Occurrences: Lines 10985-10995 (4 instances)

loc = data.min()

# ==================================================
# Line: 11001

loc = data.min() - 0.5*(fscale - ptp)

# ==================================================
# Occurrences: Lines 11682-11685 (2 instances)

pbeta = N * (m/beta) * np.exp(-beta**2/2) / (m - 1)

# ==================================================
# Line: 11692

eb2 = np.exp(-beta**2/2)

# ==================================================
# Occurrences: Lines 11888-11893 (5 instances)

u = random_state.uniform(size=k)

# ==================================================
# Occurrences: Lines 11903-11909 (5 instances)

u = random_state.uniform(size=k)

# ==================================================
# Line: 11920

num_accept = np.sum(accept)

# ==================================================
# Occurrences: Lines 12278-12278 (2 instances)

usr_data = np.array(arg, float).ctypes.data_as(ctypes.c_void_p)

# ==================================================
# Occurrences: Lines 12284-12284 (2 instances)

usr_data = np.array(arg, float).ctypes.data_as(ctypes.c_void_p)

# ==================================================
# Occurrences: Lines 12305-12305 (2 instances)

usr_data = np.array(arg, float).ctypes.data_as(ctypes.c_void_p)

# ==================================================
# Occurrences: Lines 12311-12311 (2 instances)

usr_data = np.array(arg, float).ctypes.data_as(ctypes.c_void_p)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_correlation.py
# Line: 197

xi, r, l = _xi_statistic(x, y, y_continuous)

# ==================================================
# Line: 204

data=(y,), statistic=lambda y, axis: _xi_statistic(x, y, y_continuous)[0],

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_quantile.py
# Line: 28

elif np.iterable(axis) or int(axis) != axis:

# ==================================================
# Line: 34

axis = int(axis)

# ==================================================
# Occurrences: Lines 87-90 (2 instances)

y = xp.asarray(y, copy=True)  # ensure writable

# ==================================================
# Occurrences: Lines 305-307 (2 instances)

g = xp.astype((g > 0), jg.dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_continued_fraction.py
# Occurrences: Lines 288-292 (2 instances)

n = int(xp.real(xp_ravel(n))[0])

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_binned_statistic.py
# Occurrences: Lines 598-608 (6 instances)

flatcount = _bincount(binnumbers, None)

# ==================================================
# Line: 618

flatcount = _bincount(binnumbers, None)

# ==================================================
# Line: 624

flatsum = _bincount(binnumbers, values[vv])

# ==================================================
# Occurrences: Lines 641-646 (2 instances)

i = np.argsort(values[vv])[::-1]  # Reversed so the min is last

# ==================================================
# Line: 656

result = result.astype(np.complex128)

# ==================================================
# Line: 663

result = result.astype(np.complex128)

# ==================================================
# Occurrences: Lines 731-732 (2 instances)

smin = np.empty(Ndim)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_morestats.py
# Occurrences: Lines 387-389 (2 instances)

return kstat(data, n=2, axis=axis, _no_deco=True) * 1.0/N

# ==================================================
# Occurrences: Lines 1668-1671 (2 instances)

out[pos] = np.log1p(x[pos])

# ==================================================
# Occurrences: Lines 2269-2274 (2 instances)

s = np.std(x, ddof=1, axis=0)

# ==================================================
# Line: 2281

sig = array([15, 10, 5, 2.5, 1])

# ==================================================
# Line: 2292

sol0 = array([xbar, np.std(x, ddof=1, axis=0)])

# ==================================================
# Occurrences: Lines 2306-2307 (2 instances)

sig = array([25, 10, 5, 2.5, 1])

# ==================================================
# Occurrences: Lines 2314-2315 (2 instances)

sig = array([25, 10, 5, 2.5, 1])

# ==================================================
# Occurrences: Lines 2824-2831 (4 instances)

pval = 2.0 * np.minimum(_abw_state.a.cdf(AB, n, m),

# ==================================================
# Line: 3071

Yci = np.empty(k, 'd')

# ==================================================
# Line: 3101

Zbari = np.empty(k, 'd')

# ==================================================
# Line: 3290

diffs_prep = np.concatenate(([1], diffs))

# ==================================================
# Line: 3297

t = np.bincount(np.cumsum(np.asarray(diffs_prep != 0, dtype=int)))[1:]

# ==================================================
# Occurrences: Lines 3306-3307 (2 instances)

diffs_prep = np.concatenate(([1], diffs))

# ==================================================
# Occurrences: Lines 4599-4602 (2 instances)

if method.lower() not in methods:

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_distn_infrastructure.py
# Occurrences: Lines 1184-1185 (2 instances)

mu = self._munp(1, *goodargs)

# ==================================================
# Occurrences: Lines 1191-1197 (3 instances)

mu2p = self._munp(2, *goodargs)

# ==================================================
# Occurrences: Lines 1203-1207 (3 instances)

mu3p = self._munp(3, *goodargs)

# ==================================================
# Line: 1213

out0 = default.copy()

# ==================================================
# Occurrences: Lines 1221-1223 (2 instances)

mu = self._munp(1, *goodargs)

# ==================================================
# Line: 1232

mu3p = self._munp(3, *goodargs)

# ==================================================
# Occurrences: Lines 1238-1242 (2 instances)

out0 = default.copy()

# ==================================================
# Line: 3113

qa = self._cdf(a, *args)

# ==================================================
# Line: 3120

qa = self._cdf(a, *args)

# ==================================================
# Line: 3946

delta = np.sum(fun(x))

# ==================================================
# Line: 3958

delta = np.sum(fun(x))

# ==================================================
# Occurrences: Lines 4115-4117 (2 instances)

Y = self._ppf(U)[0]

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_stats_mstats_common.py
# Occurrences: Lines 139-142 (2 instances)

x = np.arange(len(y), dtype=float)

# ==================================================
# Occurrences: Lines 168-169 (2 instances)

nt = len(slopes)       # N in Sen (1968)

# ==================================================
# Line: 177

Ru = min(int(np.round((nt - z*sigma)/2.)), len(slopes)-1)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_discrete_distns.py
# Occurrences: Lines 1558-1559 (2 instances)

x = random_state.geometric(probOfSuccess, size=size)

# ==================================================
# Occurrences: Lines 1805-1806 (2 instances)

E1 = random_state.standard_exponential(size)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_multivariate.py
# Line: 177

if len(d) < len(s) and not allow_singular:

# ==================================================
# Line: 189

self.rank = len(d)

# ==================================================
# Line: 449

cov = np.asarray(cov, dtype=float)

# ==================================================
# Line: 455

mean = np.asarray(mean, dtype=float)

# ==================================================
# Occurrences: Lines 466-470 (2 instances)

mean = np.asarray(mean, dtype=float)

# ==================================================
# Occurrences: Lines 2130-2132 (2 instances)

log_det_x = np.empty(x.shape[-1])

# ==================================================
# Occurrences: Lines 2730-2731 (2 instances)

log_det_x = np.empty(x.shape[-1])

# ==================================================
# Line: 4726

shape = np.asarray(shape, dtype=float)

# ==================================================
# Occurrences: Lines 4733-4738 (4 instances)

loc = np.asarray(loc, dtype=float)

# ==================================================
# Line: 4748

shape = shape * np.eye(dim)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_binomtest.py
# Occurrences: Lines 140-144 (2 instances)

plow = _findp(lambda p: binom.sf(k-1, n, p) - alpha)

# ==================================================
# Line: 151

phigh = _findp(lambda p: binom.cdf(k, n, p) - alpha)

# ==================================================
# Line: 157

plow = _findp(lambda p: binom.sf(k-1, n, p) - alpha)

# ==================================================
# Occurrences: Lines 299-301 (2 instances)

pval = binom.cdf(k, n, p)

# ==================================================
# Line: 318

pval = binom.cdf(k, n, p) + binom.sf(n - y, n, p)

# ==================================================
# Line: 327

pval = binom.cdf(y-1, n, p) + binom.sf(k-1, n, p)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_distribution_infrastructure.py
# Line: 645

a, b = np.broadcast_arrays(a, b)

# ==================================================
# Occurrences: Lines 687-688 (2 instances)

min = np.asarray(a.squeeze())

# ==================================================
# Occurrences: Lines 694-696 (3 instances)

a, b = np.broadcast_arrays(a, b)

# ==================================================
# Occurrences: Lines 760-764 (2 instances)

arr = np.asarray(arr, dtype=np.float64)

# ==================================================
# Occurrences: Lines 977-977 (2 instances)

low, high = endpoints.get(method_name, self.support())

# ==================================================
# Occurrences: Lines 1046-1046 (2 instances)

a, b = self.support()

# ==================================================
# Occurrences: Lines 1086-1088 (4 instances)

return f(self, *args, **kwargs)

# ==================================================
# Line: 1642

parameters = self._process_parameters(**parameters)

# ==================================================
# Line: 1672

parameters = self._process_parameters(**parameters)

# ==================================================
# Occurrences: Lines 3230-3236 (2 instances)

mean = self._moment_raw_dispatch(self._one, **params,
                                 methods=self._moment_methods)

# ==================================================
# Occurrences: Lines 3630-3632 (2 instances)

nan_result = np.isnan(x) | np.isnan(p)

# ==================================================
# Occurrences: Lines 3638-3640 (2 instances)

nan_result = np.isnan(x) | np.isnan(p)

# ==================================================
# Occurrences: Lines 4125-4129 (2 instances)

a, _ = dist._get_support(**parameter_values)

# ==================================================
# Line: 4252

domain = _RealInterval(**domain_info)

# ==================================================
# Line: 4258

_x_support = _RealInterval(**domain_info)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_fit.py
# Line: 200

y = self.pxf(x, *fit_params)

# ==================================================
# Line: 209

y = self.pxf(x, *fit_params)

# ==================================================
# Line: 589

user_bounds_array = np.empty((n_params, 2))

# ==================================================
# Line: 627

user_bounds_array = np.empty((n_params, 2))

# ==================================================
# Occurrences: Lines 1203-1206 (2 instances)

loc = np.mean(data, axis=-1)

# ==================================================
# Occurrences: Lines 1321-1325 (2 instances)

fixed_nhd_params = known_params_f.copy()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_axis_nan_policy.py
# Occurrences: Lines 530-532 (6 instances)

n_axes = len(axis)

# ==================================================
# Occurrences: Lines 559-560 (6 instances)

res = np.full(n_out, NaN)

# ==================================================
# Occurrences: Lines 567-581 (21 instances)

samples = _remove_nans(samples, paired)

# ==================================================
# Occurrences: Lines 595-595 (3 instances)

res = _add_reduced_axes(res, reduced_axes, keepdims)

# ==================================================
# Occurrences: Lines 612-613 (6 instances)

res = result_to_tuple(res, n_out)

# ==================================================
# Occurrences: Lines 620-627 (12 instances)

samples = _remove_nans(samples, paired)

# ==================================================
# Occurrences: Lines 634-641 (12 instances)

return np.full(n_out, NaN)

# ==================================================
# Occurrences: Lines 647-654 (12 instances)

samples = _remove_sentinel(samples, paired, sentinel)

# ==================================================
# Occurrences: Lines 676-677 (4 instances)

doc = str(doc).split("\n", 1)[1]  # remove signature

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_qmc.py
# Occurrences: Lines 572-576 (2 instances)

- 2. / n * np.prod(1. + 0.5 * abs(z_ij[i1, :])
                   - 0.5 * z_ij[i1, :] ** 2))

# ==================================================
# Occurrences: Lines 595-596 (2 instances)

h_i1 = np.prod(1. + 0.5 * abs(z_ij[i1, :]) - 0.5 * (z_ij[i1, :] ** 2))

# ==================================================
# Line: 2191

indices = ((candidate - self.l_bounds) / self.cell_size).astype(int)

# ==================================================
# Line: 2216

indices = ((candidate - self.l_bounds) / self.cell_size).astype(int)

# ==================================================
# Line: 2880

l1_old = _l1_norm(sample=sample)

# ==================================================
# Line: 2887

l1_new = _l1_norm(sample=sample)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_odds_ratio.py
# Line: 34

value = func(nc)

# ==================================================
# Line: 44

while func(nc) > 0:

# ==================================================
# Line: 50

while func(nc) < 0:

# ==================================================
# Occurrences: Lines 158-162 (2 instances)

z = ndtri(confidence_level)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_sampling.py
# Occurrences: Lines 1041-1046 (2 instances)

x = self.ppf(u)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_hypotests.py
# Occurrences: Lines 1127-1132 (2 instances)

if 0 in table.sum(axis=0):

# ==================================================
# Occurrences: Lines 1341-1346 (2 instances)

if 0 in table.sum(axis=0):

# ==================================================
# Occurrences: Lines 1526-1529 (2 instances)

+ [np.empty((2, 0), dtype=dtype) for _ in range(m)])

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_ksstats.py
# Occurrences: Lines 232-234 (3 instances)

gpower = np.empty(npwrs)  # gpower = (g/n)^m/m!

# ==================================================
# Occurrences: Lines 247-248 (2 instances)

V0 = np.zeros([npwrs])

# ==================================================
# Line: 408

prob = _kolmogn_DMTW(n, x, cdf=True)

# ==================================================
# Line: 428

cdfprob = _kolmogn_DMTW(n, x, cdf=True)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_wilcoxon.py
# Line: 207

r_plus, r_minus, se, z, count, has_ties = _wilcoxon_statistic(
    d, method, zero_method
)

# ==================================================
# Occurrences: Lines 245-254 (5 instances)

p = dist.cdf(np.ceil(r_plus))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_resampling.py
# Line: 955

cmps = xp.asarray(cmps, dtype=dtype)

# ==================================================
# Line: 961

cmps = xp.asarray(cmps, dtype=dtype)

# ==================================================
# Occurrences: Lines 1532-1537 (2 instances)

data = np.swapaxes(data, 0, -1)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/differentiate/_differentiate.py
# Occurrences: Lines 559-559 (2 instances)

stop = xpx.at(stop)[i].set(True)

# ==================================================
# Occurrences: Lines 565-565 (2 instances)

stop = xpx.at(stop)[i].set(True)

# ==================================================
# Occurrences: Lines 576-576 (2 instances)

stop = xpx.at(stop)[i].set(True)

# ==================================================
# Occurrences: Lines 676-682 (3 instances)

s = np.sign(i)

# ==================================================
# Occurrences: Lines 698-704 (3 instances)

s = np.sign(i)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_rbfinterp.py
# Line: 450

out[i:i + chunksize, :] = np.dot(vec, coeffs)

# ==================================================
# Line: 460

out = np.dot(vec, coeffs)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_cubic.py
# Line: 288

dk = np.zeros_like(y)

# ==================================================
# Line: 304

dk = np.zeros_like(y)

# ==================================================
# Line: 797

b = np.empty((n,) + y.shape[1:], dtype=y.dtype)

# ==================================================
# Line: 862

s = np.empty((n,) + y.shape[1:], dtype=y.dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_rgi.py
# Line: 416

indices, norm_distances = self._find_indices(xi.T)

# ==================================================
# Line: 433

indices, norm_distances = self._find_indices(xi.T)

# ==================================================
# Occurrences: Lines 452-454 (2 instances)

ndim = len(self.grid)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_ndbspline.py
# Line: 262

ndim = len(t_tpl)

# ==================================================
# Occurrences: Lines 272-275 (2 instances)

raise ValueError(f"len(t) = {len(t_tpl)} != {len(k) = }.")

# ==================================================
# Line: 310

ndim = len(t_tpl)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_fitpack_impl.py
# Line: 186

n = len(t)

# ==================================================
# Line: 193

_iermess[ier][0] + f"\tk={k} n={len(t)} m={m} fp={fp} s={s}"

# ==================================================
# Line: 255

numknots = len(t)

# ==================================================
# Line: 286

_mess = (_iermess[ier][0] + f"\tk={k} n={len(t)} m={m} fp={fp} s={s}")

# ==================================================
# Occurrences: Lines 538-543 (2 instances)

_surfit_cache['tx'] = atleast_1d(tx)

# ==================================================
# Occurrences: Lines 564-565 (2 instances)

_surfit_cache['tx'] = atleast_1d(tx)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_polyint.py
# Occurrences: Lines 368-369 (2 instances)

pi = np.zeros((n, len(x)))

# ==================================================
# Line: 904

return np.zeros((der, len(x), self.r), dtype=self.dtype)

# ==================================================
# Line: 939

cn = np.zeros((der, len(x), self.r), dtype=self.dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_rbf.py
# Occurrences: Lines 230-233 (2 instances)

self.di = np.asarray(args[-1]).flatten()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_bary_rational.py
# Occurrences: Lines 446-451 (4 instances)

zj = np.empty(max_terms, dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_fitpack_repro.py
# Occurrences: Lines 265-265 (2 instances)

residuals, fp = _get_residuals(x, y, t, k, w=w)

# ==================================================
# Occurrences: Lines 306-306 (2 instances)

residuals, _ = _get_residuals(x, y, t, k, w=w)

# ==================================================
# Line: 681

_, _, c = _lsq_solve_qr(x, y, t, k, w)

# ==================================================
# Line: 688

R, Y, _ = _lsq_solve_qr(x, y, t, k, w)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_fitpack2.py
# Occurrences: Lines 1525-1526 (2 instances)

tx1 = zeros((nmax,), float)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_interpolate.py
# Occurrences: Lines 621-622 (2 instances)

self.c = np.moveaxis(self.c, axis+1, 0)

# ==================================================
# Line: 1985

extrapolate = bool(extrapolate)

# ==================================================
# Line: 2013

bool(extrapolate),

# ==================================================
# Line: 2034

sl = [slice(None)]*ndim

# ==================================================
# Line: 2047

sl[axis] = slice(None)

# ==================================================
# Occurrences: Lines 2081-2086 (2 instances)

c2 = c2.transpose(perm2)

# ==================================================
# Occurrences: Lines 2214-2216 (2 instances)

return out.reshape(c.shape[2:])

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/interpolate/_bsplines.py
# Line: 711

out = _dierckx.evaluate_spline(ta, ca.reshape(ca.shape[0], -1),
                      ka, x, 0, False)

# ==================================================
# Occurrences: Lines 726-742 (5 instances)

x = np.asarray([a, b], dtype=np.float64)

# ==================================================
# Occurrences: Lines 1157-1159 (2 instances)

dx = np.diff(xc)

# ==================================================
# Line: 1326

c = np.ascontiguousarray(c.reshape((n + k - 1,) + y.shape[1:]))

# ==================================================
# Line: 1365

c = np.ascontiguousarray(c.reshape((n + k - 1,) + y.shape[1:]))

# ==================================================
# Line: 1512

y = np.asarray(y)

# ==================================================
# Occurrences: Lines 1538-1539 (2 instances)

c = np.asarray(y)

# ==================================================
# Occurrences: Lines 1547-1548 (2 instances)

c = np.asarray(y)

# ==================================================
# Occurrences: Lines 1798-1814 (8 instances)

yy = y.view(float)

# ==================================================
# Line: 2323

X = np.zeros((5, n))

# ==================================================
# Line: 2340

wE = np.zeros((5, n))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/conftest.py
# Occurrences: Lines 119-121 (2 instances)

old_mode = get_fpu_mode()

# ==================================================
# Occurrences: Lines 444-448 (2 instances)

devices = xp.__array_namespace_info__().devices()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_tanhsinh.py
# Line: 367

aerr = xp_ravel(xp.full(shape, xp.nan, dtype=dtype))  # absolute error

# ==================================================
# Occurrences: Lines 376-381 (5 instances)

fr0 = xp_ravel(xp.full(shape, xp.nan, dtype=dtype))

# ==================================================
# Occurrences: Lines 565-566 (2 instances)

work.pair_cache.xjc = xp.empty(0)

# ==================================================
# Line: 717

nan = xp.full_like(work.Sn, xp.nan)

# ==================================================
# Line: 742

nan = xp.full_like(work.Sn, xp.nan)

# ==================================================
# Line: 778

aerr = xp.clip(xp.max(ds, axis=0), d5, d1)

# ==================================================
# Line: 789

aerr = xp.clip(xp.max(ds, axis=0), d5, d1)

# ==================================================
# Occurrences: Lines 809-815 (4 instances)

abinf = xp.isinf(a) & xp.isinf(b)

# ==================================================
# Occurrences: Lines 876-881 (2 instances)

and np.all(params.astype(np.int64) == params)):

# ==================================================
# Occurrences: Lines 1176-1177 (2 instances)

S = xp.empty_like(a)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_lebedev.py
# Occurrences: Lines 96-99 (4 instances)

leb_tmp.x = zeros(degree)

# ==================================================
# Occurrences: Lines 110-4706 (1287 instances)

leb_tmp, start = get_lebedev_recurrence_points(1, start, a, b, v, leb_tmp)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_quadrature.py
# Occurrences: Lines 129-130 (2 instances)

slice1 = [slice(None)]*nd

# ==================================================
# Line: 141

slice3[axis] = slice(None)

# ==================================================
# Occurrences: Lines 148-159 (2 instances)

ret = xp.sum(
    d * (y[tuple(slice1)] + y[tuple(slice2)]) / 2.0,
    axis=axis, dtype=result_dtype
)

# ==================================================
# Line: 315

elif len(x.shape) != len(y.shape):

# ==================================================
# Line: 325

nd = len(y.shape)

# ==================================================
# Occurrences: Lines 350-351 (2 instances)

slice0 = tupleset(slice_all, axis, slice(start, stop, step))

# ==================================================
# Occurrences: Lines 361-362 (2 instances)

sl0 = tupleset(slice_all, axis, slice(start, stop, step))

# ==================================================
# Line: 444

nd = len(y.shape)

# ==================================================
# Line: 456

elif len(x.shape) != len(y.shape):

# ==================================================
# Occurrences: Lines 472-473 (2 instances)

slice1 = tupleset(slice_all, axis, -1)

# ==================================================
# Occurrences: Lines 481-482 (2 instances)

slice1 = tupleset(slice_all, axis, -1)

# ==================================================
# Occurrences: Lines 507-530 (3 instances)

alpha = np.true_divide(
    num,
    den,
    out=np.zeros_like(den),
    where=den != 0
)

# ==================================================
# Line: 768

alt_input_dx_shape = tupleset(original_shape, axis, 1)

# ==================================================
# Line: 781

alt_initial_input_shape = tupleset(original_shape, axis, 1)

# ==================================================
# Occurrences: Lines 1040-1045 (2 instances)

rn = np.arange(N+1)

# ==================================================
# Line: 1058

nvec = np.arange(N+1)

# ==================================================
# Line: 1284

m = m or mean(estimates, log)

# ==================================================
# Line: 1295

m = m or mean(estimates, log)

# ==================================================
# Line: 1333

integral = mean(estimates, log)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_rules/_genz_malik.py
# Occurrences: Lines 81-82 (2 instances)

l_3 = math.sqrt(9/10)

# ==================================================
# Occurrences: Lines 140-141 (2 instances)

l_3 = math.sqrt(9/10)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_bvp.py
# Line: 81

dbc_dya = np.empty((n, n + k), dtype=dtype)

# ==================================================
# Line: 92

dbc_dyb = np.empty((n, n + k), dtype=dtype)

# ==================================================
# Occurrences: Lines 248-249 (2 instances)

dPhi_dy_0 = np.empty((m - 1, n, n), dtype=dtype)

# ==================================================
# Occurrences: Lines 255-256 (2 instances)

dPhi_dy_1 = np.empty((m - 1, n, n), dtype=dtype)

# ==================================================
# Line: 442

res = np.hstack((col_res.ravel(order='F'), bc_res))

# ==================================================
# Occurrences: Lines 457-457 (2 instances)

step = LU.solve(res)

# ==================================================
# Occurrences: Lines 472-474 (3 instances)

res = np.hstack((col_res.ravel(order='F'), bc_res))

# ==================================================
# Line: 1007

h = np.diff(x)

# ==================================================
# Line: 1073

bc_res = bc_wrapped(y[:, 0], y[:, -1], p)

# ==================================================
# Line: 1094

bc_res = bc_wrapped(y[:, 0], y[:, -1], p)

# ==================================================
# Line: 1126

h = np.diff(x)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_ivp/radau.py
# Occurrences: Lines 481-481 (2 instances)

error_norm = norm(error / scale)

# ==================================================
# Occurrences: Lines 487-491 (3 instances)

error_norm = norm(error / scale)

# ==================================================
# Line: 502

factor = predict_factor(h_abs, h_abs_old, error_norm, error_norm_old)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_ivp/ivp.py
# Occurrences: Lines 33-34 (2 instances)

max_events = np.empty(len(events))

# ==================================================
# Occurrences: Lines 668-668 (2 instances)

sol = solver.dense_output()

# ==================================================
# Occurrences: Lines 678-678 (2 instances)

sol = solver.dense_output()

# ==================================================
# Occurrences: Lines 720-720 (2 instances)

sol = solver.dense_output()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_ivp/bdf.py
# Occurrences: Lines 20-21 (2 instances)

I = np.arange(1, order + 1)[:, None]

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_ivp/common.py
# Line: 351

scale = np.maximum(np.abs(f[max_ind]), np.abs(f_new[max_ind, r]))

# ==================================================
# Line: 364

scale_new = np.maximum(np.abs(f[max_ind]), np.abs(f_new[max_ind, r]))

# ==================================================
# Occurrences: Lines 390-394 (2 instances)

e = np.equal(group, groups)

# ==================================================
# Occurrences: Lines 417-422 (2 instances)

e = np.equal(group, groups)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_quad_vec.py
# Occurrences: Lines 268-273 (2 instances)

return quad_vec(f2, 0, 1, **kwargs)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_cubature.py
# Line: 330

if xp_size(a) == 0 or xp_size(b) == 0:

# ==================================================
# Line: 338

ndim = xp_size(a)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/integrate/_ode.py
# Occurrences: Lines 371-376 (2 instances)

n_prev = len(self._y)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/cluster/hierarchy.py
# Line: 1362

cols_idx = xp.arange(nobs)

# ==================================================
# Line: 1369

cols_idx = nobs - xp.searchsorted(xp.arange(nobs), n_clusters)

# ==================================================
# Line: 1378

last_group = xp.arange(nobs)

# ==================================================
# Line: 3457

color_threshold = xp.max(Z[:, 2]) * 0.7

# ==================================================
# Line: 3491

mh = xp.max(Z[:, 2])

# ==================================================
# Occurrences: Lines 4338-4339 (4 instances)

L = np.zeros(n_clusters, dtype=np.int32)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/cluster/vq.py
# Line: 477

return _kmeans(obs, guess, thresh=thresh, xp=xp)

# ==================================================
# Line: 493

book, dist = _kmeans(obs, guess, thresh=thresh, xp=xp)

# ==================================================
# Line: 555

x = xp.asarray(x)

# ==================================================
# Line: 561

x = xp.asarray(x)

# ==================================================
# Line: 570

x = xp.asarray(x)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/_idl.py
# Occurrences: Lines 171-173 (2 instances)

length = _read_long(f)

# ==================================================
# Occurrences: Lines 192-197 (4 instances)

return _read_float32(f)

# ==================================================
# Occurrences: Lines 204-205 (2 instances)

real = _read_float64(f)

# ==================================================
# Occurrences: Lines 318-321 (3 instances)

record = {'rectype': _read_long(f)}

# ==================================================
# Occurrences: Lines 333-335 (2 instances)

record['varname'] = _read_string(f)

# ==================================================
# Line: 349

varstart = _read_long(f)

# ==================================================
# Occurrences: Lines 366-385 (11 instances)

record['date'] = _read_string(f)

# ==================================================
# Occurrences: Lines 393-400 (5 instances)

record['nvalues'] = _read_long(f)

# ==================================================
# Occurrences: Lines 435-438 (2 instances)

typedesc['array_desc'] = _read_arraydesc(f)

# ==================================================
# Line: 446

arraydesc = {'arrstart': _read_long(f)}

# ==================================================
# Occurrences: Lines 452-460 (5 instances)

arraydesc['nbytes'] = _read_long(f)

# ==================================================
# Occurrences: Lines 468-470 (3 instances)

arraydesc['nbytes'] = _read_uint64(f)

# ==================================================
# Occurrences: Lines 478-481 (4 instances)

v = _read_long(f)

# ==================================================
# Occurrences: Lines 494-501 (5 instances)

structstart = _read_long(f)

# ==================================================
# Line: 513

tag['name'] = _read_string(f)

# ==================================================
# Occurrences: Lines 524-527 (3 instances)

structdesc['classname'] = _read_string(f)

# ==================================================
# Occurrences: Lines 546-552 (3 instances)

tagdesc = {'offset': _read_long(f)}

# ==================================================
# Line: 757

signature = _read_bytes(f, 2)

# ==================================================
# Line: 763

recfmt = _read_bytes(f, 2)

# ==================================================
# Occurrences: Lines 792-793 (4 instances)

nextrec = _read_uint32(f)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/wavfile.py
# Line: 506

start = fid.tell()

# ==================================================
# Occurrences: Lines 521-527 (3 instances)

a[:, :bytes_per_sample] = data.reshape((-1, bytes_per_sample))

# ==================================================
# Line: 560

str1 = fid.read(4)  # File signature

# ==================================================
# Occurrences: Lines 579-589 (6 instances)

file_size = struct.unpack(fmt, fid.read(4))[0] + 8

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/_netcdf.py
# Occurrences: Lines 428-429 (4 instances)

if var.isrec and len(var.data) > self._recs:

# ==================================================
# Line: 520

the_beguine = self.fp.tell()

# ==================================================
# Line: 542

pos0 = pos = self.fp.tell()

# ==================================================
# Occurrences: Lines 624-628 (2 instances)

count = self._unpack_int()

# ==================================================
# Line: 701

pos = self.fp.tell()

# ==================================================
# Line: 725

pos = self.fp.tell()

# ==================================================
# Occurrences: Lines 739-742 (2 instances)

dims = self._unpack_int()

# ==================================================
# Line: 752

vsize = self._unpack_int()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/_harwell_boeing/_fortran_format_parser.py
# Occurrences: Lines 256-259 (2 instances)

next = tokens.pop(0)

# ==================================================
# Occurrences: Lines 278-285 (4 instances)

repeat = int(tokens.pop(0).value)

# ==================================================
# Occurrences: Lines 292-304 (6 instances)

next = self._next(tokens, "INT")

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/_harwell_boeing/hb.py
# Line: 138

line = fid.readline().strip("\n")

# ==================================================
# Occurrences: Lines 146-153 (4 instances)

line = fid.readline().strip("\n")

# ==================================================
# Line: 165

line = fid.readline().strip("\n")

# ==================================================
# Occurrences: Lines 187-189 (3 instances)

nrows = _expect_int(line[14:28])

# ==================================================
# Line: 197

line = fid.readline().strip("\n")

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/_fast_matrix_market/__init__.py
# Occurrences: Lines 145-146 (2 instances)

i = np.zeros(cursor.header.nnz, dtype=index_dtype)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/_mmio.py
# Occurrences: Lines 375-377 (2 instances)

line = stream.readline()

# ==================================================
# Line: 393

line = stream.readline()

# ==================================================
# Occurrences: Lines 399-406 (3 instances)

line = stream.readline()

# ==================================================
# Line: 412

rows, cols, entries = map(int, split_line)

# ==================================================
# Line: 474

stream = open(filespec, mode)

# ==================================================
# Line: 480

stream = open(filespec, mode)

# ==================================================
# Occurrences: Lines 686-690 (5 instances)

aij = int(line)

# ==================================================
# Occurrences: Lines 728-729 (2 instances)

I = zeros(entries, dtype='intc')

# ==================================================
# Occurrences: Lines 750-757 (5 instances)

l = line.split()

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/arff/_arffread.py
# Occurrences: Lines 552-555 (2 instances)

next_item = next(iterable)

# ==================================================
# Occurrences: Lines 618-620 (2 instances)

i = next(ofile)

# ==================================================
# Occurrences: Lines 626-630 (2 instances)

i = next(ofile)

# ==================================================
# Occurrences: Lines 648-650 (4 instances)

i = next(ofile)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/matlab/_mio4.py
# Occurrences: Lines 216-217 (2 instances)

res = self.read_sub_array(hdr, copy=False)

# ==================================================
# Occurrences: Lines 301-305 (2 instances)

rows = np.ndarray(shape=(), dtype=dt,
                  buffer=self.mat_stream.read(dt.itemsize))

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/spatial/distance.py
# Occurrences: Lines 1602-1605 (2 instances)

n = float(len(u))

# ==================================================
# Occurrences: Lines 2326-2335 (3 instances)

metric_info = _METRIC_ALIAS.get(mstr, None)

# ==================================================
# Line: 2344

X, typ, kwargs = _validate_pdist_input(
    X, m, n, metric_info, **kwargs)

# ==================================================
# Line: 2474

X = _copy_array_if_base_present(X)

# ==================================================
# Line: 2498

X = _copy_array_if_base_present(X)

# ==================================================
# Occurrences: Lines 3125-3132 (3 instances)

metric_info = _METRIC_ALIAS.get(mstr, None)

# ==================================================
# Line: 3140

XA, XB, typ, kwargs = _validate_cdist_input(
    XA, XB, mA, mB, n, metric_info, **kwargs)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/spatial/transform/_rotation_spline.py
# Occurrences: Lines 84-85 (2 instances)

k1 = np.empty_like(norm)

# ==================================================
# Occurrences: Lines 130-132 (3 instances)

k1 = np.empty_like(norm)

# ==================================================
# Occurrences: Lines 223-235 (4 instances)

A_i = np.empty_like(A, dtype=int)

# ==================================================
# Line: 347

rotvecs_dot = _matrix_vector_product_of_stacks(A, angular_rates)

# ==================================================
# Line: 359

rotvecs_dot = _matrix_vector_product_of_stacks(A, angular_rates)

# ==================================================
# Occurrences: Lines 447-450 (2 instances)

rotvecs_dot = self.interpolator(times, 1)

# ==================================================
