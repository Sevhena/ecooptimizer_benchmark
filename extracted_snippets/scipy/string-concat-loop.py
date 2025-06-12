# string-concat-loop snippets for scipy

# File: /root/ecooptimizer/scipy/scipy/sparse/_generate_sparsetools.py
# Line: 237

for I_typenum, I_type in I_TYPES:
    piece = """
    else if (I_typenum == %(I_typenum)s) {
        if (T_typenum == -1) { return %(j)s; }"""
    getter_code += piece % dict(I_typenum=I_typenum, j=j)

    i_types.append((j, I_typenum, None, I_type, None))
    j += 1

    for T_typenum, T_type in T_TYPES:
        piece = """
        else if (T_typenum == %(T_typenum)s) { return %(j)s; }"""
        getter_code += piece % dict(T_typenum=T_typenum, j=j)

        it_types.append((j, I_typenum, T_typenum, I_type, T_type))
        j += 1

    getter_code += """
    }"""


# ==================================================
# Occurrences: Lines 245-251 (2 instances)

for T_typenum, T_type in T_TYPES:
    piece = """
    else if (T_typenum == %(T_typenum)s) { return %(j)s; }"""
    getter_code += piece % dict(T_typenum=T_typenum, j=j)

    it_types.append((j, I_typenum, T_typenum, I_type, T_type))
    j += 1


# ==================================================
# Line: 326

for j, I_typenum, T_typenum, I_type, T_type in types:
    arglist = get_arglist(I_type, T_type)

    piece = """
    case %(j)s:"""
    if ret_spec == 'v':
        piece += """
        (void)%(name)s(%(arglist)s);
        return 0;"""
    else:
        piece += """
        return %(name)s(%(arglist)s);"""
    thunk_content += piece % dict(j=j, I_type=I_type, T_type=T_type,
                                  I_typenum=I_typenum, T_typenum=T_typenum,
                                  arglist=arglist, name=name)


# ==================================================
# Occurrences: Lines 414-422 (2 instances)

for name in names:
    method_defs += (f"PyObject *{name}"
                    f"_method(PyObject *, PyObject *);\n")


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_precompute/wright_bessel.py
# Line: 50

for i in range(len(c)):
    s += f"\n{name}[{i}] = " + str(c[i])

# ==================================================
# Occurrences: Lines 135-143 (6 instances)

for i in range(len(c)):
    s += f"\n{name}[{i}] = "
    s += str(c[i])

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/special/_generate_pyx.py
# Occurrences: Lines 300-302 (2 instances)

for j in range(len(ufunc_inputs)):
    body += f"    cdef char *ip{j} = args[{j}]\n"

# ==================================================
# Line: 319

for j, outtype in enumerate(func_outputs):
    body += f"    cdef {CY_TYPES[outtype]} ov{j+func_joff}\n"
    ftypes.append(f"{CY_TYPES[outtype]} *")
    fvars.append(f"&ov{j+func_joff}")
    outtypecodes.append(outtype)


# ==================================================
# Line: 351

for j, outtype in enumerate(outtypecodes):
    body += f"            ov{j} = <{CY_TYPES[outtype]}>{NAN_VALUE[outtype]}\n"

# ==================================================
# Occurrences: Lines 358-372 (8 instances)

for j, (outtype, fouttype) in enumerate(zip(ufunc_outputs, outtypecodes)):
    if (fouttype, outtype) in DANGEROUS_DOWNCAST:
        body += f"        if ov{j} == <{CY_TYPES[outtype]}>ov{j}:\n"
        body += (f"            (<{CY_TYPES[outtype]} *>op{j})[0] = "
                f"<{CY_TYPES[outtype]}>ov{j}\n")
        body += "        else:\n"
        body += ("            sf_error.error(func_name, sf_error.DOMAIN, "
                 "\"invalid output\")\n")
        body += (f"            (<{CY_TYPES[outtype]} *>op{j})[0] = "
                f"<{CY_TYPES[outtype]}>{NAN_VALUE[outtype]}\n")
    else:
        body += (f"        (<{CY_TYPES[outtype]} *>op{j})[0] = "
                f"<{CY_TYPES[outtype]}>ov{j}\n")

# ==================================================
# Occurrences: Lines 605-615 (5 instances)

for j, function in enumerate(loops):
    toplevel += (f"ufunc_{self.name}_loops[{j}] = "
                f"<np.PyUFuncGenericFunction>{function}\n")

# ==================================================
# Line: 721

for c_name, c_proto, cy_proto, header in cfuncs:
    if header.endswith('++'):
        header = header[:-2]

        # for the CXX module
        item_defs, item_defs_h, var_name = get_declaration(
            ufunc, c_name, c_proto, cy_proto, header, cxx_proto_h_filename
        )
        cxx_defs.extend(item_defs)
        cxx_defs_h.extend(item_defs_h)

        func_name = ufunc.cython_func_name(
            c_name, specialized=True, override=False
        )
        cxx_defs.append(f"cdef void *_export_{var_name} = <void*>{func_name}")
        cxx_pxd_defs.append(f"cdef void *_export_{var_name}")

        # let cython grab the function pointer from the c++ shared library
        ufunc.function_name_overrides[c_name] = (
            "scipy.special._ufuncs_cxx._export_" + var_name
        )
    else:
        # usual case
        item_defs, item_defs_h, _ = get_declaration(
            ufunc, c_name, c_proto, cy_proto, header, proto_h_filename
        )
        defs.extend(item_defs)
        defs_h.extend(item_defs_h)


# ==================================================
# File: /root/ecooptimizer/scipy/scipy/_lib/_ccallback.py
# Occurrences: Lines 199-201 (2 instances)

for j, arg in enumerate(func.argtypes):
    if j == 0:
        signature += _typename_from_ctypes(arg)
    else:
        signature += ", " + _typename_from_ctypes(arg)

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/stats/_distribution_infrastructure.py
# Line: 5364

for component in self.components:
    result += f"        {repr(component)},\n"

# ==================================================
# Line: 5375

for component in self.components:
    result += f"        {str(component)},\n"

# ==================================================
# File: /root/ecooptimizer/scipy/scipy/io/arff/_arffread.py
# Line: 164

for i in range(len(self.values)-1):
    msg += self.values[i] + ","

# ==================================================
# Occurrences: Lines 692-695 (3 instances)

for i in self._attributes:
    msg += f"\t{i}'s type is {self._attributes[i].type_name}"
    if self._attributes[i].range:
        msg += f", range is {str(self._attributes[i].range)}"
    msg += '\n'

# ==================================================
