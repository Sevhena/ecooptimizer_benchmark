# no-self-use snippets for numpy

# File: /root/ecooptimizer/numpy/numpy/distutils/ccompiler_opt.py
# Line: 885

def cache_hash(self, *factors):
    # is there a built-in non-crypto hash?
    # sdbm
    chash = 0
    for f in factors:
        for char in str(f):
            chash  = ord(char) + (chash << 6) + (chash << 16) - chash
            chash &= 0xFFFFFFFF
    return chash


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/cpuinfo.py
# Line: 69

def _try_call(self, func):
    try:
        return func()
    except Exception:
        pass


# ==================================================
# Occurrences: Lines 85-88 (2 instances)

def _getNCPUs(self):
    return 1


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/fcompiler/arm.py
# Occurrences: Lines 47-62 (6 instances)

def get_flags(self):
    return []


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/fcompiler/__init__.py
# Line: 391

def get_flags_free(self):
    """List of Fortran 90 free format specific flags."""
    return []

# ==================================================
# Occurrences: Lines 406-412 (3 instances)

def get_flags_opt(self):
    """List of architecture independent compiler flags."""
    return []

# ==================================================
# Line: 719

def can_ccompiler_link(self, ccompiler):
    """
    Check if the given C compiler can link objects produced by
    this compiler.
    """
    return True


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/fcompiler/nv.py
# Occurrences: Lines 37-46 (4 instances)

def get_flags_opt(self):
    return ['-fast']


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/fcompiler/g95.py
# Occurrences: Lines 31-35 (3 instances)

def get_flags(self):
    return ['-fno-second-underscore']

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/fcompiler/mips.py
# Line: 36

def get_flags_arch_f77(self):
    r = None
    if cpu.is_r10000(): r = 10000
    elif cpu.is_r12000(): r = 12000
    elif cpu.is_r8000(): r = 8000
    elif cpu.is_r5000(): r = 5000
    elif cpu.is_r4000(): r = 4000
    if r is not None:
        return ['r%s' % (r)]
    return []

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/fcompiler/sun.py
# Occurrences: Lines 35-37 (2 instances)

def get_opt(self):
    return ['-fast', '-dalign']

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/fcompiler/gnu.py
# Line: 31

def gnu_version_match(self, version_string):
    """Handle the different versions of GNU fortran compilers"""
    # Strip warning(s) that may be emitted by gfortran
    while version_string.startswith('gfortran: warning'):
        version_string =\
            version_string[version_string.find('\n') + 1:].strip()

    # Gfortran versions from after 2010 will output a simple string
    # (usually "x.y", "x.y.z" or "x.y.z-q") for ``-dumpversion``; older
    # gfortrans may still return long version strings (``-dumpversion`` was
    # an alias for ``--version``)
    if len(version_string) <= 20:
        # Try to find a valid version string
        m = re.search(r'([0-9.]+)', version_string)
        if m:
            # g77 provides a longer version string that starts with GNU
            # Fortran
            if version_string.startswith('GNU Fortran'):
                return ('g77', m.group(1))

            # gfortran only outputs a version string such as #.#.#, so check
            # if the match is at the start of the string
            elif m.start() == 0:
                return ('gfortran', m.group(1))
    else:
        # Output probably from --version, try harder:
        m = re.search(r'GNU Fortran\s+95.*?([0-9-.]+)', version_string)
        if m:
            return ('gfortran', m.group(1))
        m = re.search(
            r'GNU Fortran.*?\-?([0-9-.]+\.[0-9-.]+)', version_string)
        if m:
            v = m.group(1)
            if v.startswith(('0', '2', '3')):
                # the '0' is for early g77's
                return ('g77', v)
            else:
                # at some point in the 4.x series, the ' 95' was dropped
                # from the version string
                return ('gfortran', v)

    # If still nothing, raise an error to make the problem easy to find.
    err = 'A valid Fortran version was not found in this string:\n'
    raise ValueError(err + version_string)


# ==================================================
# Line: 233

def _c_arch_flags(self):
    """ Return detected arch flags from CFLAGS """
    import sysconfig
    try:
        cflags = sysconfig.get_config_vars()['CFLAGS']
    except KeyError:
        return []
    arch_re = re.compile(r"-arch\s+(\w+)")
    arch_flags = []
    for arch in arch_re.findall(cflags):
        arch_flags += ['-arch', arch]
    return arch_flags


# ==================================================
# Line: 401

def _hash_files(self, filenames):
    h = hashlib.sha1()
    for fn in filenames:
        with open(fn, 'rb') as f:
            while True:
                block = f.read(131072)
                if not block:
                    break
                h.update(block)
    text = base64.b32encode(h.digest())
    text = text.decode('ascii')
    return text.rstrip('=')


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/system_info.py
# Line: 1075

def combine_paths(self, *args):
    """Return a list of existing paths composed by all combinations
    of items from the arguments.
    """
    return combine_paths(*args)



# ==================================================
# Line: 1263

def get_mkl_rootdir(self):
    mklroot = os.environ.get('MKLROOT', None)
    if mklroot is not None:
        return mklroot
    paths = os.environ.get('LD_LIBRARY_PATH', '').split(os.pathsep)
    ld_so_conf = '/etc/ld.so.conf'
    if os.path.isfile(ld_so_conf):
        with open(ld_so_conf) as f:
            for d in f:
                d = d.strip()
                if d:
                    paths.append(d)
    intel_mkl_dirs = []
    for path in paths:
        path_atoms = path.split(os.sep)
        for m in path_atoms:
            if m.startswith('mkl'):
                d = os.sep.join(path_atoms[:path_atoms.index(m) + 2])
                intel_mkl_dirs.append(d)
                break
    for d in paths:
        dirs = glob(os.path.join(d, 'mkl', '*'))
        dirs += glob(os.path.join(d, 'mkl*'))
        for sub_dir in dirs:
            if os.path.isdir(os.path.join(sub_dir, 'lib')):
                return sub_dir
    return None


# ==================================================
# Line: 1343

def get_tcsds_rootdir(self):
    tcsdsroot = os.environ.get('TCSDS_PATH', None)
    if tcsdsroot is not None:
        return tcsdsroot
    return None


# ==================================================
# Line: 1929

def _get_info_blas(self):
    # Default to get the optimized BLAS implementation
    info = get_info('blas_opt')
    if not info:
        warnings.warn(BlasNotFoundError.__doc__ or '', stacklevel=3)
        info_src = get_info('blas_src')
        if not info_src:
            warnings.warn(BlasSrcNotFoundError.__doc__ or '', stacklevel=3)
            return {}
        dict_append(info, libraries=[('fblas_src', info_src)])
    return info


# ==================================================
# Line: 1941

def _get_info_lapack(self):
    info = get_info('lapack')
    if not info:
        warnings.warn(LapackNotFoundError.__doc__ or '', stacklevel=3)
        info_src = get_info('lapack_src')
        if not info_src:
            warnings.warn(LapackSrcNotFoundError.__doc__ or '', stacklevel=3)
            return {}
        dict_append(info, libraries=[('flapack_src', info_src)])
    return info


# ==================================================
# Line: 2523

def check_embedded_lapack(self, info):
    """ libflame does not necessarily have a wrapper for fortran LAPACK, we need to check """
    c = customized_ccompiler()

    tmpdir = tempfile.mkdtemp()
    s = textwrap.dedent("""\
        void zungqr_();
        int main(int argc, const char *argv[])
        {
            zungqr_();
            return 0;
        }""")
    src = os.path.join(tmpdir, 'source.c')
    out = os.path.join(tmpdir, 'a.out')
    # Add the additional "extra" arguments
    extra_args = info.get('extra_link_args', [])
    try:
        with open(src, 'w') as f:
            f.write(s)
        obj = c.compile([src], output_dir=tmpdir)
        try:
            c.link_executable(obj, out, libraries=info['libraries'],
                              library_dirs=info['library_dirs'],
                              extra_postargs=extra_args)
            return True
        except distutils.ccompiler.LinkError:
            return False
    finally:
        shutil.rmtree(tmpdir)


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/misc_util.py
# Line: 880

def warn(self, message):
    sys.stderr.write('Warning: %s\n' % (message,))


# ==================================================
# Line: 900

def get_distribution(self):
    """Return the distutils distribution object for self."""
    from numpy.distutils.core import get_distribution
    return get_distribution()


# ==================================================
# Line: 1800

def get_config_cmd(self):
    """
    Returns the numpy.distutils config command instance.
    """
    cmd = get_cmd('config')
    cmd.ensure_finalized()
    cmd.dump_source = 0
    cmd.noisy = 0
    old_path = os.environ.get('PATH')
    if old_path:
        path = os.pathsep.join(['.', old_path])
        os.environ['PATH'] = path
    return cmd


# ==================================================
# Line: 1814

def get_build_temp_dir(self):
    """
    Return a path to a temporary directory where temporary files should be
    placed.
    """
    cmd = get_cmd('build')
    cmd.ensure_finalized()
    return cmd.build_temp


# ==================================================
# Line: 1875

def _get_svn_revision(self, path):
    """Return path's SVN revision number.
    """
    try:
        output = subprocess.check_output(['svnversion'], cwd=path)
    except (subprocess.CalledProcessError, OSError):
        pass
    else:
        m = re.match(rb'(?P<revision>\d+)', output)
        if m:
            return int(m.group('revision'))

    if sys.platform=='win32' and os.environ.get('SVN_ASP_DOT_NET_HACK', None):
        entries = njoin(path, '_svn', 'entries')
    else:
        entries = njoin(path, '.svn', 'entries')
    if os.path.isfile(entries):
        with open(entries) as f:
            fstr = f.read()
        if fstr[:5] == '<?xml':  # pre 1.4
            m = re.search(r'revision="(?P<revision>\d+)"', fstr)
            if m:
                return int(m.group('revision'))
        else:  # non-xml entries file --- check to be sure that
            m = re.search(r'dir[\n\r]+(?P<revision>\d+)', fstr)
            if m:
                return int(m.group('revision'))
    return None


# ==================================================
# Line: 1904

def _get_hg_revision(self, path):
    """Return path's Mercurial revision number.
    """
    try:
        output = subprocess.check_output(
            ['hg', 'identify', '--num'], cwd=path)
    except (subprocess.CalledProcessError, OSError):
        pass
    else:
        m = re.match(rb'(?P<revision>\d+)', output)
        if m:
            return int(m.group('revision'))

    branch_fn = njoin(path, '.hg', 'branch')
    branch_cache_fn = njoin(path, '.hg', 'branch.cache')

    if os.path.isfile(branch_fn):
        branch0 = None
        with open(branch_fn) as f:
            revision0 = f.read().strip()

        branch_map = {}
        with open(branch_cache_fn) as f:
            for line in f:
                branch1, revision1  = line.split()[:2]
                if revision1==revision0:
                    branch0 = branch1
                try:
                    revision1 = int(revision1)
                except ValueError:
                    continue
                branch_map[branch1] = revision1

        return branch_map.get(branch0)

    return None



# ==================================================
# Line: 2109

def get_info(self,*names):
    """Get resources information.

    Return information (from system_info.get_info) for all of the names in
    the argument list in a single dictionary.
    """
    from .system_info import get_info, dict_append
    info_dict = {}
    for a in names:
        dict_append(info_dict,**get_info(a))
    return info_dict



# ==================================================
# File: /root/ecooptimizer/numpy/numpy/distutils/command/build_src.py
# Line: 396

def filter_files(self, sources, exts = []):
    new_sources = []
    files = []
    for source in sources:
        (base, ext) = os.path.splitext(source)
        if ext in exts:
            files.append(source)
        else:
            new_sources.append(source)
    return new_sources, files


# ==================================================
# Line: 458

def generate_a_pyrex_source(self, base, ext_name, source, extension):
    """Pyrex is not supported, but some projects monkeypatch this method.

    That allows compiling Cython code, see gh-6955.
    This method will remain here for compatibility reasons.
    """
    return []


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_build_utils/tempita/_looper.py
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
    elif callable(getter):
        return getter(item) != getter(other)
    else:
        return item[getter] != other[getter]

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/typing/mypy_plugin.py
# Line: 148

def get_type_analyze_hook(self, fullname: str) -> _HookFunc | None:
    """Set the precision of platform-specific `numpy.number`
    subclasses.

    For example: `numpy.int_`, `numpy.longlong` and `numpy.longdouble`.
    """
    if fullname in _PRECISION_DICT:
        return _hook
    return None


# ==================================================
# Line: 158

def get_additional_deps(
    self, file: MypyFile

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/linalg/lapack_lite/make_lite.py
# Line: 118

def _newFortranRoutine(self, rname, filename):
    return FortranRoutine(rname, filename)


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/ma/core.py
# Line: 4829

def resize(self, newshape, refcheck=True, order=False):
    """
    .. warning::

        This method does nothing, except raise a ValueError exception. A
        masked array does not own its data and therefore cannot safely be
        resized in place. Use the `numpy.ma.resize` function instead.

    This method is difficult to implement safely and may be deprecated in
    future releases of NumPy.

    """
    # Note : the 'order' keyword looks broken, let's just drop it
    errmsg = "A masked array does not own its data "\
             "and therefore cannot be resized.\n" \
             "Use the numpy.ma.resize function instead."
    raise ValueError(errmsg)


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/code_generators/genapi.py
# Line: 147

def _format_arg(self, typename, name):
    if typename.endswith('*'):
        return typename + name
    else:
        return typename + ' ' + name


# ==================================================
# Line: 403

def internal_define(self):
    astr = """\

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_core/_internal.py
# Line: 254

def cast(self, num, obj):
    return num.value


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/_array_api_info.py
# Line: 63

def capabilities(self):
    """
    Return a dictionary of array API library capabilities.

    The resulting dictionary has the following keys:

    - **"boolean indexing"**: boolean indicating whether an array library
      supports boolean indexing. Always ``True`` for NumPy.

    - **"data-dependent shapes"**: boolean indicating whether an array
      library supports data-dependent output shapes. Always ``True`` for
      NumPy.

    See
    https://data-apis.org/array-api/latest/API_specification/generated/array_api.info.capabilities.html
    for more details.

    See Also
    --------
    __array_namespace_info__.default_device,
    __array_namespace_info__.default_dtypes,
    __array_namespace_info__.dtypes,
    __array_namespace_info__.devices

    Returns
    -------
    capabilities : dict
        A dictionary of array API library capabilities.

    Examples
    --------
    >>> info = np.__array_namespace_info__()
    >>> info.capabilities()
    {'boolean indexing': True,
     'data-dependent shapes': True,
     'max dimensions': 64}

    """
    return {
        "boolean indexing": True,
        "data-dependent shapes": True,
        "max dimensions": 64,
    }


# ==================================================
# Line: 107

def default_device(self):
    """
    The default device used for new NumPy arrays.

    For NumPy, this always returns ``'cpu'``.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_dtypes,
    __array_namespace_info__.dtypes,
    __array_namespace_info__.devices

    Returns
    -------
    device : str
        The default device used for new NumPy arrays.

    Examples
    --------
    >>> info = np.__array_namespace_info__()
    >>> info.default_device()
    'cpu'

    """
    return "cpu"


# ==================================================
# Line: 134

def default_dtypes(self, *, device=None):
    """
    The default data types used for new NumPy arrays.

    For NumPy, this always returns the following dictionary:

    - **"real floating"**: ``numpy.float64``
    - **"complex floating"**: ``numpy.complex128``
    - **"integral"**: ``numpy.intp``
    - **"indexing"**: ``numpy.intp``

    Parameters
    ----------
    device : str, optional
        The device to get the default data types for. For NumPy, only
        ``'cpu'`` is allowed.

    Returns
    -------
    dtypes : dict
        A dictionary describing the default data types used for new NumPy
        arrays.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_device,
    __array_namespace_info__.dtypes,
    __array_namespace_info__.devices

    Examples
    --------
    >>> info = np.__array_namespace_info__()
    >>> info.default_dtypes()
    {'real floating': numpy.float64,
     'complex floating': numpy.complex128,
     'integral': numpy.int64,
     'indexing': numpy.int64}

    """
    if device not in ["cpu", None]:
        raise ValueError(
            'Device not understood. Only "cpu" is allowed, but received:'
            f' {device}'
        )
    return {
        "real floating": dtype(float64),
        "complex floating": dtype(complex128),
        "integral": dtype(intp),
        "indexing": dtype(intp),
    }


# ==================================================
# Line: 321

def devices(self):
    """
    The devices supported by NumPy.

    For NumPy, this always returns ``['cpu']``.

    Returns
    -------
    devices : list of str
        The devices supported by NumPy.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_device,
    __array_namespace_info__.default_dtypes,
    __array_namespace_info__.dtypes

    Examples
    --------
    >>> info = np.__array_namespace_info__()
    >>> info.devices()
    ['cpu']

    """
    return ["cpu"]

# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_datasource.py
# Line: 262

def _iszip(self, filename):
    """Test if the filename is a zip file by looking at the file extension.

    """
    fname, ext = os.path.splitext(filename)
    return ext in _file_openers.keys()


# ==================================================
# Line: 269

def _iswritemode(self, mode):
    """Test if the given mode will open a file for writing."""

    # Currently only used to test the bz2 files.
    _writemodes = ("w", "+")
    return any(c in _writemodes for c in mode)


# ==================================================
# Line: 299

def _isurl(self, path):
    """Test if path is a net location.  Tests the scheme and netloc."""

    # We do this here to reduce the 'import numpy' initial import time.
    from urllib.parse import urlparse

    # BUG : URLs require a scheme string ('http://') to be used.
    #       www.google.com will fail.
    #       Should we prepend the scheme for those that don't have it and
    #       test that also?  Similar to the way we append .gz and test for
    #       for compressed versions of files.

    scheme, netloc, upath, uparams, uquery, ufrag = urlparse(path)
    return bool(scheme and netloc)


# ==================================================
# Line: 413

def _sanitize_relative_path(self, path):
    """Return a sanitised relative path for which
    os.path.abspath(os.path.join(base, path)).startswith(base)
    """
    last = None
    path = os.path.normpath(path)
    while path != last:
        last = path
        # Note: os.path.join treats '/' as os.sep on Windows
        path = path.lstrip(os.sep).lstrip('/')
        path = path.lstrip(os.pardir).removeprefix('..')
        drive, path = os.path.splitdrive(path)  # for Windows
    return path


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/lib/_iotools.py
# Line: 149

def autostrip(self, method):
    """
    Wrapper to strip each member of the output of `method`.

    Parameters
    ----------
    method : function
        Function that takes a single argument and returns a sequence of
        strings.

    Returns
    -------
    wrapped : function
        The result of wrapping `method`. `wrapped` takes a single input
        argument and returns a list of strings that are stripped of
        white-space.

    """
    return lambda input: [_.strip() for _ in method(input)]


# ==================================================
# File: /root/ecooptimizer/numpy/numpy/f2py/_backends/_meson.py
# Line: 178

def _run_subprocess_command(self, command, cwd):
    subprocess.run(command, cwd=cwd, check=True)


# ==================================================
