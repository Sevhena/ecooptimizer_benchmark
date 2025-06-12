# long-message-chain snippets for numpy

# File: /root/ecooptimizer/numpy/numpy/__init__.py
# Line: 927

return [str(Path(__file__).with_name("_pyinstaller").resolve())]

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/cpuinfo.py
# Line: 90

nbits = re.compile(r'(\d+)bit').search(abits).group(1)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_build_utils/gitversion.py
# Line: 42

out.decode('utf-8')
.strip()
.replace('"', '')
.split('T')[0]

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/ma/core.py
# Line: 5017

d = self.filled(True).all(axis=axis, **kwargs).view(type(self))

# ==================================================
# Line: 5047

d = self.filled(False).any(axis=axis, **kwargs).view(type(self))

# ==================================================
# Line: 5170

return D.astype(dtype).filled(0).sum(axis=-1, out=out)

# ==================================================
# Line: 5948

result = self.filled(fill_value).min(
    axis=axis, out=out, **kwargs).view(type(self))

# ==================================================
# Line: 6053

result = self.filled(fill_value).max(
    axis=axis, out=out, **kwargs).view(type(self))

# ==================================================
# Line: 7645

return np.asarray(a).transpose(axes).view(MaskedArray)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/matlib.py
# Line: 379

c = a.reshape(1, a.size).repeat(m, 0).reshape(rows, origcols).repeat(n, 0)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/einsumfunc.py
# Line: 644

used = subscripts.replace(".", "").replace(",", "").replace("->", "")

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/_backends/_meson.py
# Line: 226

values = match_result.group(2).strip().split()

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/crackfortran.py
# Line: 1326

initexpr = initexpr[1:].lower().replace('d', 'e').\
    replace(',', '+1j*(')

# ==================================================
# Line: 1344

if m.group('after').strip().lower() == 'none':

# ==================================================
# Line: 2497

v = ''.join(v_[:-1]).lower().replace(v_[-1].lower(), '')

# ==================================================
