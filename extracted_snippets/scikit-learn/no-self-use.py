# no-self-use snippets for scikit-learn

# File: /root/ecooptimizer/scikit-learn/sklearn/_loss/link.py
# Line: 259

def symmetrize_raw_prediction(self, raw_prediction):
    return raw_prediction - np.mean(raw_prediction, axis=1)[:, np.newaxis]


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/_loss/loss.py
# Line: 456

def constant_to_optimal_zero(self, y_true, sample_weight=None):
    """Calculate term dropped in loss.

    With this term added, the loss of perfect predictions is zero.
    """
    return np.zeros_like(y_true)


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/estimator_checks.py
# Line: 946

def __array_function__(self, func, types, args, kwargs):
    if func.__name__ == "may_share_memory":
        return True
    raise TypeError("Don't want to call array_function {}!".format(func.__name__))



# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_metadata_requests.py
# Line: 1577

def get(self, name, default=None):
    return Bunch(**{method: dict() for method in METHODS})


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_testing.py
# Line: 1207

def __sklearn_tags__(self):
    return Tags(
        estimator_type="classifier",
        classifier_tags=ClassifierTags(),
        regressor_tags=None,
        transformer_tags=None,
        target_tags=TargetTags(required=True),
    )



# ==================================================
# Line: 1254

def __sklearn_tags__(self):
    return Tags(
        estimator_type="regressor",
        classifier_tags=None,
        regressor_tags=RegressorTags(),
        transformer_tags=None,
        target_tags=TargetTags(required=True),
    )



# ==================================================
# Line: 1299

def __sklearn_tags__(self):
    return Tags(
        estimator_type="transformer",
        classifier_tags=None,
        regressor_tags=None,
        transformer_tags=TransformerTags(),
        target_tags=TargetTags(required=False),
    )



# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_set_output.py
# Occurrences: Lines 140-144 (2 instances)

def is_supported_container(self, X):
    pd = check_library_installed("pandas")
    return isinstance(X, pd.DataFrame)


# ==================================================
# Line: 150

def hstack(self, Xs):
    pd = check_library_installed("pandas")
    return pd.concat(Xs, axis=1)



# ==================================================
# Occurrences: Lines 171-175 (2 instances)

def is_supported_container(self, X):
    pl = check_library_installed("polars")
    return isinstance(X, pl.DataFrame)


# ==================================================
# Line: 181

def hstack(self, Xs):
    pl = check_library_installed("polars")
    return pl.concat(Xs, how="horizontal")



# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_mocking.py
# Occurrences: Lines 410-418 (3 instances)

def predict(self, X):
    return "predict"


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/isotonic.py
# Line: 294

def _check_input_data_shape(self, X):
    if not (X.ndim == 1 or (X.ndim == 2 and X.shape[1] == 1)):
        msg = (
            "Isotonic regression input X should be a 1d array or "
            "2d array with 1 feature"
        )
        raise ValueError(msg)


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/base.py
# Line: 452

def __sklearn_tags__(self):
    return Tags(
        estimator_type=None,
        target_tags=TargetTags(required=False),
        transformer_tags=None,
        regressor_tags=None,
        classifier_tags=None,
    )


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/array_api_compat/numpy/_info.py
# Line: 67

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
# Line: 111

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
    device : Device
        The default device used for new NumPy arrays.

    Examples
    --------
    >>> info = np.__array_namespace_info__()
    >>> info.default_device()
    'cpu'

    """
    return "cpu"


# ==================================================
# Line: 138

def default_dtypes(
    self,
    *,
    device: Device | None = None,

# ==================================================
# Line: 334

def devices(self) -> list[Device]:
    """
    The devices supported by NumPy.

    For NumPy, this always returns ``['cpu']``.

    Returns
    -------
    devices : list[Device]
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
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/array_api_compat/dask/array/_info.py
# Line: 90

def capabilities(self) -> Capabilities:
    """
    Return a dictionary of array API library capabilities.

    The resulting dictionary has the following keys:

    - **"boolean indexing"**: boolean indicating whether an array library
      supports boolean indexing.

      Dask support boolean indexing as long as both the index
      and the indexed arrays have known shapes.
      Note however that the output .shape and .size properties
      will contain a non-compliant math.nan instead of None.

    - **"data-dependent shapes"**: boolean indicating whether an array
      library supports data-dependent output shapes.

      Dask implements unique_values et.al.
      Note however that the output .shape and .size properties
      will contain a non-compliant math.nan instead of None.

    - **"max dimensions"**: integer indicating the maximum number of
      dimensions supported by the array library.

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
    >>> info = xp.__array_namespace_info__()
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
# Line: 145

def default_device(self) -> L["cpu"]:
    """
    The default device used for new Dask arrays.

    For Dask, this always returns ``'cpu'``.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_dtypes,
    __array_namespace_info__.dtypes,
    __array_namespace_info__.devices

    Returns
    -------
    device : Device
        The default device used for new Dask arrays.

    Examples
    --------
    >>> info = xp.__array_namespace_info__()
    >>> info.default_device()
    'cpu'

    """
    return "cpu"


# ==================================================
# Line: 172

def default_dtypes(self, /, *, device: _Device | None = None) -> DefaultDTypes:
    """
    The default data types used for new Dask arrays.

    For Dask, this always returns the following dictionary:

    - **"real floating"**: ``numpy.float64``
    - **"complex floating"**: ``numpy.complex128``
    - **"integral"**: ``numpy.intp``
    - **"indexing"**: ``numpy.intp``

    Parameters
    ----------
    device : str, optional
        The device to get the default data types for.

    Returns
    -------
    dtypes : dict
        A dictionary describing the default data types used for new Dask
        arrays.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_device,
    __array_namespace_info__.dtypes,
    __array_namespace_info__.devices

    Examples
    --------
    >>> info = xp.__array_namespace_info__()
    >>> info.default_dtypes()
    {'real floating': dask.float64,
     'complex floating': dask.complex128,
     'integral': dask.int64,
     'indexing': dask.int64}

    """
    if device not in ["cpu", _DASK_DEVICE, None]:
        raise ValueError(
            f'Device not understood. Only "cpu" or _DASK_DEVICE is allowed, '
            f"but received: {device!r}"
        )
    return {
        "real floating": dtype(float64),
        "complex floating": dtype(complex128),
        "integral": dtype(intp),
        "indexing": dtype(intp),
    }


# ==================================================
# Line: 391

def devices(self) -> list[_Device]:
    """
    The devices supported by Dask.

    For Dask, this always returns ``['cpu', DASK_DEVICE]``.

    Returns
    -------
    devices : list[Device]
        The devices supported by Dask.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_device,
    __array_namespace_info__.default_dtypes,
    __array_namespace_info__.dtypes

    Examples
    --------
    >>> info = xp.__array_namespace_info__()
    >>> info.devices()
    ['cpu', DASK_DEVICE]

    """
    return ["cpu", _DASK_DEVICE]

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/array_api_compat/cupy/_info.py
# Line: 64

def capabilities(self):
    """
    Return a dictionary of array API library capabilities.

    The resulting dictionary has the following keys:

    - **"boolean indexing"**: boolean indicating whether an array library
      supports boolean indexing. Always ``True`` for CuPy.

    - **"data-dependent shapes"**: boolean indicating whether an array
      library supports data-dependent output shapes. Always ``True`` for
      CuPy.

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
    >>> info = xp.__array_namespace_info__()
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
# Line: 108

def default_device(self):
    """
    The default device used for new CuPy arrays.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_dtypes,
    __array_namespace_info__.dtypes,
    __array_namespace_info__.devices

    Returns
    -------
    device : Device
        The default device used for new CuPy arrays.

    Examples
    --------
    >>> info = xp.__array_namespace_info__()
    >>> info.default_device()
    Device(0)

    Notes
    -----
    This method returns the static default device when CuPy is initialized.
    However, the *current* device used by creation functions (``empty`` etc.)
    can be changed globally or with a context manager.

    See Also
    --------
    https://github.com/data-apis/array-api/issues/835
    """
    return cuda.Device(0)


# ==================================================
# Line: 142

def default_dtypes(self, *, device=None):
    """
    The default data types used for new CuPy arrays.

    For CuPy, this always returns the following dictionary:

    - **"real floating"**: ``cupy.float64``
    - **"complex floating"**: ``cupy.complex128``
    - **"integral"**: ``cupy.intp``
    - **"indexing"**: ``cupy.intp``

    Parameters
    ----------
    device : str, optional
        The device to get the default data types for.

    Returns
    -------
    dtypes : dict
        A dictionary describing the default data types used for new CuPy
        arrays.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_device,
    __array_namespace_info__.dtypes,
    __array_namespace_info__.devices

    Examples
    --------
    >>> info = xp.__array_namespace_info__()
    >>> info.default_dtypes()
    {'real floating': cupy.float64,
     'complex floating': cupy.complex128,
     'integral': cupy.int64,
     'indexing': cupy.int64}

    """
    # TODO: Does this depend on device?
    return {
        "real floating": dtype(float64),
        "complex floating": dtype(complex128),
        "integral": dtype(intp),
        "indexing": dtype(intp),
    }


# ==================================================
# Line: 319

def devices(self):
    """
    The devices supported by CuPy.

    Returns
    -------
    devices : list[Device]
        The devices supported by CuPy.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_device,
    __array_namespace_info__.default_dtypes,
    __array_namespace_info__.dtypes

    """
    return [cuda.Device(i) for i in range(cuda.runtime.getDeviceCount())]

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/array_api_compat/torch/_info.py
# Line: 48

def capabilities(self):
    """
    Return a dictionary of array API library capabilities.

    The resulting dictionary has the following keys:

    - **"boolean indexing"**: boolean indicating whether an array library
      supports boolean indexing. Always ``True`` for PyTorch.

    - **"data-dependent shapes"**: boolean indicating whether an array
      library supports data-dependent output shapes. Always ``True`` for
      PyTorch.

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
    >>> info = xp.__array_namespace_info__()
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
# Line: 92

def default_device(self):
    """
    The default device used for new PyTorch arrays.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_dtypes,
    __array_namespace_info__.dtypes,
    __array_namespace_info__.devices

    Returns
    -------
    device : Device
        The default device used for new PyTorch arrays.

    Examples
    --------
    >>> info = xp.__array_namespace_info__()
    >>> info.default_device()
    device(type='cpu')

    Notes
    -----
    This method returns the static default device when PyTorch is initialized.
    However, the *current* device used by creation functions (``empty`` etc.)
    can be changed at runtime.

    See Also
    --------
    https://github.com/data-apis/array-api/issues/835
    """
    return torch.device("cpu")


# ==================================================
# Line: 126

def default_dtypes(self, *, device=None):
    """
    The default data types used for new PyTorch arrays.

    Parameters
    ----------
    device : Device, optional
        The device to get the default data types for.
        Unused for PyTorch, as all devices use the same default dtypes.

    Returns
    -------
    dtypes : dict
        A dictionary describing the default data types used for new PyTorch
        arrays.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_device,
    __array_namespace_info__.dtypes,
    __array_namespace_info__.devices

    Examples
    --------
    >>> info = xp.__array_namespace_info__()
    >>> info.default_dtypes()
    {'real floating': torch.float32,
     'complex floating': torch.complex64,
     'integral': torch.int64,
     'indexing': torch.int64}

    """
    # Note: if the default is set to float64, the devices like MPS that
    # don't support float64 will error. We still return the default_dtype
    # value here because this error doesn't represent a different default
    # per-device.
    default_floating = torch.get_default_dtype()
    default_complex = torch.complex64 if default_floating == torch.float32 else torch.complex128
    default_integral = torch.int64
    return {
        "real floating": default_floating,
        "complex floating": default_complex,
        "integral": default_integral,
        "indexing": default_integral,
    }



# ==================================================
# Line: 317

def devices(self):
    """
    The devices supported by PyTorch.

    Returns
    -------
    devices : list[Device]
        The devices supported by PyTorch.

    See Also
    --------
    __array_namespace_info__.capabilities,
    __array_namespace_info__.default_device,
    __array_namespace_info__.default_dtypes,
    __array_namespace_info__.dtypes

    Examples
    --------
    >>> info = xp.__array_namespace_info__()
    >>> info.devices()
    [device(type='cpu'), device(type='mps', index=0), device(type='meta')]

    """
    # Torch doesn't have a straightforward way to get the list of all
    # currently supported devices. To do this, we first parse the error
    # message of torch.device to get the list of all possible types of
    # device:
    try:
        torch.device('notadevice')
        raise AssertionError("unreachable")  # pragma: nocover
    except RuntimeError as e:
        # The error message is something like:
        # "Expected one of cpu, cuda, ipu, xpu, mkldnn, opengl, opencl, ideep, hip, ve, fpga, ort, xla, lazy, vulkan, mps, meta, hpu, mtia, privateuseone device type at start of device string: notadevice"
        devices_names = e.args[0].split('Expected one of ')[1].split(' device type')[0].split(', ')

    # Next we need to check for different indices for different devices.
    # device(device_name, index=index) doesn't actually check if the
    # device name or index is valid. We have to try to create a tensor
    # with it (which is why this function is cached).
    devices = []
    for device_name in devices_names:
        i = 0
        while True:
            try:
                a = torch.empty((0,), device=torch.device(device_name, index=i))
                if a.device in devices:
                    break
                devices.append(a.device)
            except:
                break
            i += 1

    return devices

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/_arff.py
# Line: 487

def encode_data(self, data, attributes):
    '''(INTERNAL) Encodes a line of data.

    Data instances follow the csv format, i.e, attribute values are
    delimited by commas. After converted from csv.

    :param data: a list of values.
    :param attributes: a list of attributes. Used to check if data is valid.
    :return: a string with the encoded data line.
    '''
    current_row = 0

    for inst in data:
        if len(inst) != len(attributes):
            raise BadObject(
                'Instance %d has %d attributes, expected %d' %
                 (current_row, len(inst), len(attributes))
            )

        new_data = []
        for value in inst:
            if value is None or value == '' or value != value:
                s = '?'
            else:
                s = encode_string(str(value))
            new_data.append(s)

        current_row += 1
        yield ','.join(new_data)



# ==================================================
# Line: 529

def decode_rows(self, stream, conversors):
    data, rows, cols = [], [], []
    for i, row in enumerate(stream):
        values = _parse_values(row)
        if not isinstance(values, dict):
            raise BadLayout()
        if not values:
            continue
        row_cols, values = zip(*sorted(values.items()))
        try:
            values = [value if value is None else conversors[key](value)
                      for key, value in zip(row_cols, values)]
        except ValueError as exc:
            if 'float: ' in str(exc):
                raise BadNumericalValue()
            raise
        except IndexError:
            # conversor out of range
            raise BadDataFormat(row)

        data.extend(values)
        rows.extend([i] * len(values))
        cols.extend(row_cols)

    return data, rows, cols


# ==================================================
# Line: 555

def encode_data(self, data, attributes):
    num_attributes = len(attributes)
    new_data = []
    current_row = 0

    row = data.row
    col = data.col
    data = data.data

    # Check if the rows are sorted
    if not all(row[i] <= row[i + 1] for i in range(len(row) - 1)):
        raise ValueError("liac-arff can only output COO matrices with "
                         "sorted rows.")

    for v, col, row in zip(data, col, row):
        if row > current_row:
            # Add empty rows if necessary
            while current_row < row:
                yield " ".join(["{", ','.join(new_data), "}"])
                new_data = []
                current_row += 1

        if col >= num_attributes:
            raise BadObject(
                'Instance %d has at least %d attributes, expected %d' %
                (current_row, col + 1, num_attributes)
            )

        if v is None or v == '' or v != v:
            s = '?'
        else:
            s = encode_string(str(v))
        new_data.append("%d %s" % (col, s))

    yield " ".join(["{", ','.join(new_data), "}"])


# ==================================================
# Line: 592

def decode_rows(self, stream, conversors):
    for row in stream:
        values = _parse_values(row)

        if not isinstance(values, dict):
            raise BadLayout()
        try:
            yield {key: None if value is None else conversors[key](value)
                   for key, value in values.items()}
        except ValueError as exc:
            if 'float: ' in str(exc):
                raise BadNumericalValue()
            raise
        except IndexError:
            # conversor out of range
            raise BadDataFormat(row)


# ==================================================
# Line: 609

def encode_data(self, data, attributes):
    current_row = 0

    num_attributes = len(attributes)
    for row in data:
        new_data = []

        if len(row) > 0 and max(row) >= num_attributes:
            raise BadObject(
                'Instance %d has %d attributes, expected %d' %
                (current_row, max(row) + 1, num_attributes)
            )

        for col in sorted(row):
            v = row[col]
            if v is None or v == '' or v != v:
                s = '?'
            else:
                s = encode_string(str(v))
            new_data.append("%d %s" % (col, s))

        current_row += 1
        yield " ".join(["{", ','.join(new_data), "}"])


# ==================================================
# Line: 674

def _decode_comment(self, s):
    '''(INTERNAL) Decodes a comment line.

    Comments are single line strings starting, obligatorily, with the ``%``
    character, and can have any symbol, including whitespaces or special
    characters.

    This method must receive a normalized string, i.e., a string without
    padding, including the "\r\n" characters.

    :param s: a normalized string.
    :return: a string with the decoded comment.
    '''
    res = re.sub(r'^\%( )?', '', s)
    return res


# ==================================================
# Line: 690

def _decode_relation(self, s):
    '''(INTERNAL) Decodes a relation line.

    The relation declaration is a line with the format ``@RELATION
    <relation-name>``, where ``relation-name`` is a string. The string must
    start with alphabetic character and must be quoted if the name includes
    spaces, otherwise this method will raise a `BadRelationFormat` exception.

    This method must receive a normalized string, i.e., a string without
    padding, including the "\r\n" characters.

    :param s: a normalized string.
    :return: a string with the decoded relation name.
    '''
    _, v = s.split(' ', 1)
    v = v.strip()

    if not _RE_RELATION.match(v):
        raise BadRelationFormat()

    res = str(v.strip('"\''))
    return res


# ==================================================
# Line: 713

def _decode_attribute(self, s):
    '''(INTERNAL) Decodes an attribute line.

    The attribute is the most complex declaration in an arff file. All
    attributes must follow the template::

         @attribute <attribute-name> <datatype>

    where ``attribute-name`` is a string, quoted if the name contains any
    whitespace, and ``datatype`` can be:

    - Numerical attributes as ``NUMERIC``, ``INTEGER`` or ``REAL``.
    - Strings as ``STRING``.
    - Dates (NOT IMPLEMENTED).
    - Nominal attributes with format:

        {<nominal-name1>, <nominal-name2>, <nominal-name3>, ...}

    The nominal names follow the rules for the attribute names, i.e., they
    must be quoted if the name contains whitespaces.

    This method must receive a normalized string, i.e., a string without
    padding, including the "\r\n" characters.

    :param s: a normalized string.
    :return: a tuple (ATTRIBUTE_NAME, TYPE_OR_VALUES).
    '''
    _, v = s.split(' ', 1)
    v = v.strip()

    # Verify the general structure of declaration
    m = _RE_ATTRIBUTE.match(v)
    if not m:
        raise BadAttributeFormat()

    # Extracts the raw name and type
    name, type_ = m.groups()

    # Extracts the final name
    name = str(name.strip('"\''))

    # Extracts the final type
    if type_[:1] == "{" and type_[-1:] == "}":
        try:
            type_ = _parse_values(type_.strip('{} '))
        except Exception:
            raise BadAttributeType()
        if isinstance(type_, dict):
            raise BadAttributeType()

    else:
        # If not nominal, verify the type name
        type_ = str(type_).upper()
        if type_ not in ['NUMERIC', 'REAL', 'INTEGER', 'STRING']:
            raise BadAttributeType()

    return (name, type_)


# ==================================================
# Line: 904

def _encode_comment(self, s=''):
    '''(INTERNAL) Encodes a comment line.

    Comments are single line strings starting, obligatorily, with the ``%``
    character, and can have any symbol, including whitespaces or special
    characters.

    If ``s`` is None, this method will simply return an empty comment.

    :param s: (OPTIONAL) string.
    :return: a string with the encoded comment line.
    '''
    if s:
        return '%s %s'%(_TK_COMMENT, s)
    else:
        return '%s' % _TK_COMMENT


# ==================================================
# Line: 921

def _encode_relation(self, name):
    '''(INTERNAL) Decodes a relation line.

    The relation declaration is a line with the format ``@RELATION
    <relation-name>``, where ``relation-name`` is a string.

    :param name: a string.
    :return: a string with the encoded relation declaration.
    '''
    for char in ' %{},':
        if char in name:
            name = '"%s"'%name
            break

    return '%s %s'%(_TK_RELATION, name)


# ==================================================
# Line: 937

def _encode_attribute(self, name, type_):
    '''(INTERNAL) Encodes an attribute line.

    The attribute follow the template::

         @attribute <attribute-name> <datatype>

    where ``attribute-name`` is a string, and ``datatype`` can be:

    - Numerical attributes as ``NUMERIC``, ``INTEGER`` or ``REAL``.
    - Strings as ``STRING``.
    - Dates (NOT IMPLEMENTED).
    - Nominal attributes with format:

        {<nominal-name1>, <nominal-name2>, <nominal-name3>, ...}

    This method must receive a the name of the attribute and its type, if
    the attribute type is nominal, ``type`` must be a list of values.

    :param name: a string.
    :param type_: a string or a list of string.
    :return: a string with the encoded attribute declaration.
    '''
    for char in ' %{},':
        if char in name:
            name = '"%s"'%name
            break

    if isinstance(type_, (tuple, list)):
        type_tmp = ['%s' % encode_string(type_k) for type_k in type_]
        type_ = '{%s}'%(', '.join(type_tmp))

    return '%s %s %s'%(_TK_ATTRIBUTE, name, type_)


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/neural_network/_stochastic_optimizers.py
# Line: 51

def trigger_stopping(self, msg, verbose):
    """Decides whether it is time to stop training

    Parameters
    ----------
    msg : str
        Message passed in for verbose output

    verbose : bool
        Print message to stdin if True

    Returns
    -------
    is_stopping : bool
        True if training needs to stop
    """
    if verbose:
        print(msg + " Stopping.")
    return True



# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/tree/_export.py
# Line: 402

def str_escape(self, string):
    return string



# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/preprocessing/_function_transformer.py
# Line: 383

def _transform(self, X, func=None, kw_args=None):
    if func is None:
        func = _identity

    return func(X, **(kw_args if kw_args else {}))


# ==================================================
# Line: 389

def __sklearn_is_fitted__(self):
    """Return True since FunctionTransfomer is stateless."""
    return True


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/preprocessing/_encoders.py
# Line: 35

def _check_X(self, X, ensure_all_finite=True):
    """
    Perform custom check_array:
    - convert list of strings to object dtype
    - check for missing values for object dtype data (check_array does
      not do that)
    - return list of features (arrays): this list of features is
      constructed feature by feature to preserve the data types
      of pandas DataFrame columns, as otherwise information is lost
      and cannot be used, e.g. for the `categories_` attribute.

    """
    if not (hasattr(X, "iloc") and getattr(X, "ndim", 0) == 2):
        # if not a dataframe, do normal check_array validation
        X_temp = check_array(X, dtype=None, ensure_all_finite=ensure_all_finite)
        if not hasattr(X, "dtype") and np.issubdtype(X_temp.dtype, np.str_):
            X = check_array(X, dtype=object, ensure_all_finite=ensure_all_finite)
        else:
            X = X_temp
        needs_validation = False
    else:
        # pandas dataframe, do validation later column by column, in order
        # to keep the dtype information to be used in the encoder.
        needs_validation = ensure_all_finite

    n_samples, n_features = X.shape
    X_columns = []

    for i in range(n_features):
        Xi = _safe_indexing(X, indices=i, axis=1)
        Xi = check_array(
            Xi, ensure_2d=False, dtype=None, ensure_all_finite=needs_validation
        )
        X_columns.append(Xi)

    return X_columns, n_samples, n_features


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/preprocessing/_data.py
# Line: 3459

def _yeo_johnson_inverse_transform(self, x, lmbda):
    """Return inverse-transformed input x following Yeo-Johnson inverse
    transform with parameter lambda.
    """
    x_inv = np.zeros_like(x)
    pos = x >= 0

    # when x >= 0
    if abs(lmbda) < np.spacing(1.0):
        x_inv[pos] = np.exp(x[pos]) - 1
    else:  # lmbda != 0
        x_inv[pos] = np.power(x[pos] * lmbda + 1, 1 / lmbda) - 1

    # when x < 0
    if abs(lmbda - 2) > np.spacing(1.0):
        x_inv[~pos] = 1 - np.power(-(2 - lmbda) * x[~pos] + 1, 1 / (2 - lmbda))
    else:  # lmbda == 2
        x_inv[~pos] = 1 - np.exp(-x[~pos])

    return x_inv


# ==================================================
# Line: 3480

def _yeo_johnson_transform(self, x, lmbda):
    """Return transformed input x following Yeo-Johnson transform with
    parameter lambda.
    """

    out = np.zeros_like(x)
    pos = x >= 0  # binary mask

    # when x >= 0
    if abs(lmbda) < np.spacing(1.0):
        out[pos] = np.log1p(x[pos])
    else:  # lmbda != 0
        out[pos] = (np.power(x[pos] + 1, lmbda) - 1) / lmbda

    # when x < 0
    if abs(lmbda - 2) > np.spacing(1.0):
        out[~pos] = -(np.power(-x[~pos] + 1, 2 - lmbda) - 1) / (2 - lmbda)
    else:  # lmbda == 2
        out[~pos] = -np.log1p(-x[~pos])

    return out


# ==================================================
# Line: 3502

def _box_cox_optimize(self, x):
    """Find and return optimal lambda parameter of the Box-Cox transform by
    MLE, for observed data x.

    We here use scipy builtins which uses the brent optimizer.
    """
    mask = np.isnan(x)
    if np.all(mask):
        raise ValueError("Column must not be all nan.")

    # the computation of lambda is influenced by NaNs so we need to
    # get rid of them
    _, lmbda = stats.boxcox(x[~mask], lmbda=None)

    return lmbda


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/preprocessing/_label.py
# Line: 878

def _transform(self, y, class_mapping):
    """Transforms the label sets with a given mapping.

    Parameters
    ----------
    y : iterable of iterables
        A set of labels (any orderable and hashable object) for each
        sample. If the `classes` parameter is set, `y` will not be
        iterated.

    class_mapping : Mapping
        Maps from label to column index in label indicator matrix.

    Returns
    -------
    y_indicator : sparse matrix of shape (n_samples, n_classes)
        Label indicator matrix. Will be of CSR format.
    """
    indices = array.array("i")
    indptr = array.array("i", [0])
    unknown = set()
    for labels in y:
        index = set()
        for label in labels:
            try:
                index.add(class_mapping[label])
            except KeyError:
                unknown.add(label)
        indices.extend(index)
        indptr.append(len(indices))
    if unknown:
        warnings.warn(
            "unknown class(es) {0} will be ignored".format(sorted(unknown, key=str))
        )
    data = np.ones(len(indices), dtype=int)

    return sp.csr_matrix(
        (data, indices, indptr), shape=(len(indptr) - 1, len(class_mapping))
    )


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/neighbors/_kde.py
# Line: 174

def _choose_algorithm(self, algorithm, metric):
    # given the algorithm string + metric string, choose the optimal
    # algorithm to compute the result.
    if algorithm == "auto":
        # use KD Tree if possible
        if metric in KDTree.valid_metrics:
            return "kd_tree"
        elif metric in BallTree.valid_metrics:
            return "ball_tree"
    else:  # kd_tree or ball_tree
        if metric not in TREE_DICT[algorithm].valid_metrics:
            raise ValueError(
                "invalid metric for {0}: '{1}'".format(TREE_DICT[algorithm], metric)
            )
        return algorithm


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/mixture/_gaussian_mixture.py
# Line: 846

def _compute_lower_bound(self, _, log_prob_norm):
    return log_prob_norm


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/ensemble/_bagging.py
# Line: 397

def _parallel_args(self):
    return {}


# ==================================================
# Line: 581

def _validate_y(self, y):
    if len(y.shape) == 1 or y.shape[1] == 1:
        return column_or_1d(y, warn=True)
    return y


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py
# Line: 232

def _finalize_sample_weight(self, sample_weight, y):
    """Finalize sample weight.

    Used by subclasses to adjust sample_weights. This is useful for implementing
    class weights.
    """
    return sample_weight


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/ensemble/_hist_gradient_boosting/grower.py
# Line: 358

def _validate_parameters(
    self,
    X_binned,
    min_gain_to_split,
    min_hessian_to_split,

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/ensemble/_forest.py
# Line: 624

def _validate_y_class_weight(self, y):
    # Default implementation
    return y, None


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/svm/_base.py
# Line: 295

def _validate_targets(self, y):
    """Validation of y and class_weight.

    Default implementation for SVR and one-class; overridden in BaseSVC.
    """
    return column_or_1d(y, warn=True).astype(np.float64, copy=False)


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_glm/glm.py
# Line: 460

def _get_loss(self):
    """This is only necessary because of the link and power arguments of the
    TweedieRegressor.

    Note that we do not need to pass sample_weight to the loss class as this is
    only needed to set loss.constant_hessian on which GLMs do not rely.
    """
    return HalfSquaredError()



# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_bayes.py
# Line: 406

def _update_coef_(
    self, X, y, n_samples, n_features, XT_y, U, Vh, eigen_vals_, alpha_, lambda_

# ==================================================
# Line: 766

def _update_sigma_woodbury(self, X, alpha_, lambda_, keep_lambda):
    # See slides as referenced in the docstring note
    # this function is used when n_samples < n_features and will invert
    # a matrix of shape (n_samples, n_samples) making use of the
    # woodbury formula:
    # https://en.wikipedia.org/wiki/Woodbury_matrix_identity
    n_samples = X.shape[0]
    X_keep = X[:, keep_lambda]
    inv_lambda = 1 / lambda_[keep_lambda].reshape(1, -1)
    sigma_ = pinvh(
        np.eye(n_samples, dtype=X.dtype) / alpha_
        + np.dot(X_keep * inv_lambda, X_keep.T)
    )
    sigma_ = np.dot(sigma_, X_keep * inv_lambda)
    sigma_ = -np.dot(inv_lambda.reshape(-1, 1) * X_keep.T, sigma_)
    sigma_[np.diag_indices(sigma_.shape[1])] += 1.0 / lambda_[keep_lambda]
    return sigma_


# ==================================================
# Line: 784

def _update_sigma(self, X, alpha_, lambda_, keep_lambda):
    # See slides as referenced in the docstring note
    # this function is used when n_samples >= n_features and will
    # invert a matrix of shape (n_features, n_features)
    X_keep = X[:, keep_lambda]
    gram = np.dot(X_keep.T, X_keep)
    eye = np.eye(gram.shape[0], dtype=X.dtype)
    sigma_inv = lambda_[keep_lambda] * eye + alpha_ * gram
    sigma_ = pinvh(sigma_inv)
    return sigma_


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_stochastic_gradient.py
# Occurrences: Lines 179-182 (2 instances)

def _get_learning_rate_type(self, learning_rate):
    return LEARNING_RATE_TYPES[learning_rate]


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_ridge.py
# Occurrences: Lines 1679-1682 (2 instances)

def decision_function(self, y_predict):
    return y_predict


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_linear_loss.py
# Line: 207

def l2_penalty(self, weights, l2_reg_strength):
    """Compute L2 penalty term l2_reg_strength/2 *||w||_2^2."""
    norm2_w = weights @ weights if weights.ndim == 1 else squared_norm(weights)
    return 0.5 * l2_reg_strength * norm2_w


# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/gaussian_process/kernels.py
# Line: 468

def diag(self, X):
    """Returns the diagonal of the kernel k(X, X).

    The result of this method is identical to np.diag(self(X)); however,
    it can be evaluated more efficiently since only the diagonal is
    evaluated.

    Parameters
    ----------
    X : ndarray of shape (n_samples_X, n_features)
        Left argument of the returned kernel k(X, Y)

    Returns
    -------
    K_diag : ndarray of shape (n_samples_X,)
        Diagonal of kernel k(X, X)
    """
    return np.ones(X.shape[0])



# ==================================================
# Line: 494

def is_stationary(self):
    """Returns whether the kernel is stationary."""
    return True



# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/feature_extraction/text.py
# Line: 1193

def _sort_features(self, X, vocabulary):
    """Sort features by name

    Returns a reordered matrix and modifies the vocabulary in place
    """
    sorted_features = sorted(vocabulary.items())
    map_index = np.empty(len(sorted_features), dtype=X.indices.dtype)
    for new_val, (term, old_val) in enumerate(sorted_features):
        vocabulary[term] = new_val
        map_index[old_val] = new_val

    X.indices = map_index.take(X.indices, mode="clip")
    return X


# ==================================================
# Line: 1207

def _limit_features(self, X, vocabulary, high=None, low=None, limit=None):
    """Remove too rare or too common features.

    Prune features that are non zero in more samples than high or less
    documents than low, modifying the vocabulary, and restricting it to
    at most the limit most frequent.

    This does not prune samples with zero features.
    """
    if high is None and low is None and limit is None:
        return X, set()

    # Calculate a mask based on document frequencies
    dfs = _document_frequency(X)
    mask = np.ones(len(dfs), dtype=bool)
    if high is not None:
        mask &= dfs <= high
    if low is not None:
        mask &= dfs >= low
    if limit is not None and mask.sum() > limit:
        tfs = np.asarray(X.sum(axis=0)).ravel()
        mask_inds = (-tfs[mask]).argsort()[:limit]
        new_mask = np.zeros(len(dfs), dtype=bool)
        new_mask[np.where(mask)[0][mask_inds]] = True
        mask = new_mask

    new_indices = np.cumsum(mask) - 1  # maps old indices to new
    for term, old_index in list(vocabulary.items()):
        if mask[old_index]:
            vocabulary[term] = new_indices[old_index]
        else:
            del vocabulary[term]
    kept_indices = np.where(mask)[0]
    if len(kept_indices) == 0:
        raise ValueError(
            "After pruning, no terms remain. Try a lower min_df or a higher max_df."
        )
    return X[:, kept_indices]


# ==================================================
