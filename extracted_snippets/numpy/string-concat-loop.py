# string-concat-loop snippets for numpy

# File: /root/ecooptimizer/numpy/numpy/distutils/from_template.py
# Line: 184

for k in range(numsubs):
    newstr += template_re.sub(namerepl, substr) + '\n\n'


# ==================================================
# Occurrences: Lines 201-203 (2 instances)

for sub in struct:
    cleanedstr, defs = find_and_remove_repl_patterns(newstr[oldend:sub[0]])
    writestr += cleanedstr
    names.update(defs)
    writestr += expand_sub(newstr[sub[0]:sub[1]], names)
    oldend =  sub[1]

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/ccompiler_opt.py
# Occurrences: Lines 2416-2427 (2 instances)

for name in baseline_names:
    baseline_pre += self.feature_c_preprocessor(name, tabs=1) + '\n'


# ==================================================
# Line: 2506

for tar in self.feature_sorted(target_sources):
    sources = target_sources[tar]
    name = tar if isinstance(tar, str) else '(%s)' % ' '.join(tar)
    generated += name + "[%d] " % len(sources)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/lib2def.py
# Occurrences: Lines 101-104 (2 instances)

for data_sym in dlist:
    header = header + '\t%s DATA\n' % data_sym

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/einsumfunc.py
# Line: 609

for s in sub:
    if s is Ellipsis:
        subscripts += "..."
    else:
        try:
            s = operator.index(s)
        except TypeError as e:
            raise TypeError(
                "For this input type lists must contain "
                "either int or Ellipsis"
            ) from e
        subscripts += einsum_symbols[s]

# ==================================================
# Occurrences: Lines 618-620 (2 instances)

for s in sub:
    if s is Ellipsis:
        subscripts += "..."
    else:
        try:
            s = operator.index(s)
        except TypeError as e:
            raise TypeError(
                "For this input type lists must contain "
                "either int or Ellipsis"
            ) from e
        subscripts += einsum_symbols[s]

# ==================================================
# Line: 626

for s in output_list:
    if s is Ellipsis:
        subscripts += "..."
    else:
        try:
            s = operator.index(s)
        except TypeError as e:
            raise TypeError(
                "For this input type lists must contain "
                "either int or Ellipsis"
            ) from e
        subscripts += einsum_symbols[s]

# ==================================================
# Line: 635

for s in output_list:
    if s is Ellipsis:
        subscripts += "..."
    else:
        try:
            s = operator.index(s)
        except TypeError as e:
            raise TypeError(
                "For this input type lists must contain "
                "either int or Ellipsis"
            ) from e
        subscripts += einsum_symbols[s]

# ==================================================
# Line: 696

for s in sorted(set(tmp_subscripts)):
    if s not in (einsum_symbols):
        raise ValueError(f"Character {s} is not a valid symbol.")
    if tmp_subscripts.count(s) == 1:
        output_subscript += s

# ==================================================
# Line: 1043

for n, contraction in enumerate(contraction_list):
    inds, idx_rm, einsum_str, remaining, blas = contraction
    remaining_str = ",".join(remaining) + "->" + output_subscript
    path_run = (scale_list[n], einsum_str, remaining_str)
    path_print += "\n%4d    %24s %40s" % path_run


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/core/_multiarray_umath.py
# Line: 39

for line in traceback.format_stack()[:-1]:
    if "frozen importlib" in line:
        continue
    tb_msg += line


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_polynomial_impl.py
# Line: 1083

while True:
    mat = _poly_mat.search(astr, n)
    if mat is None:
        break
    span = mat.span()
    power = mat.groups()[0]
    partstr = astr[n:span[0]]
    n = span[1]
    toadd2 = partstr + ' ' * (len(power) - 1)
    toadd1 = ' ' * (len(partstr) - 1) + power
    if ((len(line2) + len(toadd2) > wrap) or
            (len(line1) + len(toadd1) > wrap)):
        output += line1 + "\n" + line2 + "\n "
        line1 = toadd1
        line2 = toadd2
    else:
        line2 += partstr + ' ' * (len(power) - 1)
        line1 += ' ' * (len(partstr) - 1) + power

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_utils_impl.py
# Occurrences: Lines 331-333 (2 instances)

for argument in arglist:
    if k == firstwidth:
        addstr = ""
    else:
        addstr = sepstr
    k = k + len(argument) + len(addstr)
    if k > width:
        k = firstwidth + 1 + len(argument)
        newstr = newstr + ",\n" + " " * (firstwidth + 2) + argument
    else:
        newstr = newstr + addstr + argument

# ==================================================
# Occurrences: Lines 713-715 (2 instances)

for feature in __cpu_dispatch__:
    if __cpu_features__[feature]:
        enabled_features += f" {feature}*"
    else:
        enabled_features += f" {feature}?"


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/crackfortran.py
# Line: 1647

for c in line:
    if escaped == '\\' and c in ['\\', '\'', '"']:
        fragment += c
        escaped = c
        continue
    if not inside and c in ['\'', '"']:
        current_quote = c
    if c == current_quote:
        inside = not inside
    elif c == ' ' and inside:
        fragment += '@_@'
        continue
    fragment += c
    escaped = c  # reset to non-backslash

# ==================================================
# Occurrences: Lines 1655-1657 (2 instances)

for c in line:
    if escaped == '\\' and c in ['\\', '\'', '"']:
        fragment += c
        escaped = c
        continue
    if not inside and c in ['\'', '"']:
        current_quote = c
    if c == current_quote:
        inside = not inside
    elif c == ' ' and inside:
        fragment += '@_@'
        continue
    fragment += c
    escaped = c  # reset to non-backslash

# ==================================================
# Line: 3117

for c in a:
    c = c.lower()
    if c not in string.ascii_lowercase + string.digits:
        c = '_'
    na = na + c

# ==================================================
# Line: 3244

for g in block:
    if g and g['block'] in ['function', 'subroutine']:
        if g['name'] in skipfuncs:
            continue
        if onlyfuncs and g['name'] not in onlyfuncs:
            continue
    ret = ret + crack2fortrangen(g, tab, as_interface=as_interface)

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/_src_pyf.py
# Line: 185

for k in range(numsubs):
    newstr += template_re.sub(namerepl, substr) + '\n\n'


# ==================================================
# Occurrences: Lines 202-204 (2 instances)

for sub in struct:
    cleanedstr, defs = find_and_remove_repl_patterns(newstr[oldend:sub[0]])
    writestr += cleanedstr
    names.update(defs)
    writestr += expand_sub(newstr[sub[0]:sub[1]], names)
    oldend = sub[1]

# ==================================================
