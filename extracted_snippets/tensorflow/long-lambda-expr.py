# long-lambda-expr snippets for tensorflow

# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/convert.py
# Line: 1059

lambda index: BufferIndex(  # pylint: disable=g-long-lambda
    index,
    model.buffers[index].data.size,
    hashlib.md5(model.buffers[index].data.data.tobytes()).hexdigest(),
),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/python_api_parameter_converter_test.py
# Line: 328

inputs=lambda: [
    [1, 2, constant_op.constant(3.0)],  # x
    [constant_op.constant(4.0), 5, 6],  # y
    [7, constant_op.constant(8), 9],  # z
],

# ==================================================
# Line: 344

outputs=lambda: [[
    constant_op.constant(1, dtypes.int32),
    constant_op.constant(2, dtypes.float32),
    constant_op.constant(3.0, dtypes.float32)
], [dtypes.int32, dtypes.float32, dtypes.float32]],

# ==================================================
# Line: 380

outputs=lambda: [
    constant_op.constant(1, dtypes.int32),
    constant_op.constant(2, dtypes.float32), {
        "foo": ["bar", "baz"]
    }
],

# ==================================================
# Line: 411

inputs=lambda: [
    [[1, 2, 3], [4, 5, 6]],  # a
    [[1, 2], [3, 4, 5], [6]],  # b
    [1, 2, 3],  # c
    "Foo",  # d
    [[1, 2], [["three"]], [4], "five"],  # e
    [1, "two", [[3, 4], [5, 6]], [["7"]]],  # f
],

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/extension_type_test.py
# Line: 1432

lambda: extension_type.AnonymousExtensionType(
    values=constant_op.constant([1, 2, 3]),
    mask=constant_op.constant([True, False]),
),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/composite_tensor_test.py
# Occurrences: Lines 388-395 (3 instances)

('IndexedSlicesNoDenseShape', lambda: indexed_slices.IndexedSlices(
    constant_op.constant([1, 2, 3]), constant_op.constant([2, 8, 4]))),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/type_spec.py
# Line: 881

get_spec_tensor_list = lambda spec, v: (  # pylint: disable=g-long-lambda
    batchable_to_tensor_list(spec, v, minimum_rank=1)
    if isinstance(spec, BatchableTypeSpec) else spec._to_tensor_list(v))  # pylint: disable=protected-access

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3_additional_test.py
# Line: 61

return lambda shape, dtype: array_ops.pad(
    init_mat,
    [
        [0, shape[0] - init_mat.shape[0]],
        [0, shape[1] - init_mat.shape[1]],
    ],
    'CONSTANT',
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/metrics_impl.py
# Line: 188

lambda: sparse_ops.sparse_reshape(  # pylint: disable=g-long-lambda
    labels,
    shape=array_ops.concat((labels.dense_shape, (1,)), 0),
    name=scope),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
# Line: 165

'unbatched': lambda: [
    StructuredTensor.from_fields({'a': 1, 'b': [5, 6]}),
    StructuredTensor.from_fields({'a': 2, 'b': [7, 8]})],

# ==================================================
# Occurrences: Lines 174-216 (6 instances)

'unbatched': lambda: [
    StructuredTensor.from_fields(shape=[3], fields={
        'a': [1, 2, 3],
        'b': [[5, 6], [6, 7], [7, 8]]}),
    StructuredTensor.from_fields(shape=[3], fields={
        'a': [2, 3, 4],
        'b': [[2, 2], [3, 3], [4, 4]]})],

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
# Line: 135

"fields": lambda: {
    "foo": StructuredTensor.from_pyval({"a": 1, "b": [1, 2, 3]}),
    "bar": StructuredTensor.from_pyval(
        [[{"x": 12}], [{"x": 13}, {"x": 14}]]),
    },

# ==================================================
# Line: 145

"fields": lambda: {
    # TODO(martinz): should handle this, but can't.
    "f1": 5,
    "f2": [1, 2, 3],
    "f3": ragged_factory_ops.constant_value([[1, 2], [3]]),
    "f4": StructuredTensor.from_pyval({"a": 1, "b": [1, 2, 3]}),
},

# ==================================================
# Line: 186

"fields": lambda: {
    "foo": StructuredTensor.from_pyval(
        [{"a": 1, "b": [1, 2, 3]}, {"a": 2, "b": []}]),
    "bar": StructuredTensor.from_pyval(
        [[{"x": 12}], [{"x": 13}, {"x": 14}]]),
},

# ==================================================
# Line: 197

"fields": lambda: {
    "x": [1, 2],
    "y": [[1, 2], [3, 4]],
    "r": ragged_factory_ops.constant_value([[1, 2], [3]]),
    "s": StructuredTensor.from_pyval(
        [[{"x": 12}], [{"x": 13}, {"x": 14}]]),
},

# ==================================================
# Line: 209

"fields": lambda: {
    "x": [],
    "y": np.zeros([0, 8]),
    "r": ragged_factory_ops.constant([], ragged_rank=1),
    "s": StructuredTensor.from_pyval([]),
},

# ==================================================
# Line: 220

"fields": lambda: {
    "x": [1, 2],
    "y": [[1, 2], [3, 4]],
    "r": ragged_factory_ops.constant_value([[1, 2], [3]]),
    "p": ragged_factory_ops.constant_value([[4], [5, 6, 7]]),
    "foo": StructuredTensor.from_pyval(
        [{"a": 1, "b": [1, 2, 3]}, {"a": 2, "b": []}]),
    "bar": StructuredTensor.from_pyval(
        [[{"x": 12}], [{"x": 13}, {"x": 14}]]),
},

# ==================================================
# Line: 258

"fields": lambda: {
    # Note: fields must have identical row_splits.
    "a": StructuredTensor.from_pyval(
        [[{"x": 1}], [{"x": 2}, {"x": 3}]]),
    "b": StructuredTensor.from_pyval(
        [[[{"y": 1}]], [[], [{"y": 2}, {"y": 3}]]]),
},

# ==================================================
# Line: 270

"fields": lambda: {
    # Note: fields must have identical row_splits.
    "a": ragged_factory_ops.constant_value(
        [[1], [2, 3]], row_splits_dtype=dtypes.int32),
    "b": ragged_factory_ops.constant_value(
        [["a"], ["b", "c"]], row_splits_dtype=dtypes.int64),
},

# ==================================================
# Line: 282

"fields": lambda: {
    "a": [[1, 2], [3, 4]],
    "b": ragged_factory_ops.constant_value([[1, 2], [3, 4]]),
    "c": StructuredTensor.from_pyval(
        [[[{"y": 1}], []], [[], [{"y": 2}, {"y": 3}]]]),
    "d": ragged_factory_ops.constant_value(
        [[[1, 2], []], [[3], [4]]]),
},

# ==================================================
# Occurrences: Lines 382-396 (2 instances)

"fields": lambda: {
    "foo": StructuredTensor.from_pyval({"a": 1, "b": [1, 2, 3]}),
    "bar": StructuredTensor.from_pyval(
        [[{"x": 12}], [{"x": 13}, {"x": 14}]]),
    },

# ==================================================
# Occurrences: Lines 433-473 (4 instances)

"fields": lambda: {
    "foo": StructuredTensor.from_pyval(
        [{"a": 1, "b": [1, 2, 3]}, {"a": 2, "b": []}]),
    "bar": StructuredTensor.from_pyval(
        [[{"x": 12}], [{"x": 13}, {"x": 14}]]),
},

# ==================================================
# Occurrences: Lines 513-531 (2 instances)

"fields": lambda: {
    # Note: fields must have identical row_splits.
    "a": StructuredTensor.from_pyval(
        [[{"x": 1}], [{"x": 2}, {"x": 3}]]),
    "b": StructuredTensor.from_pyval(
        [[[{"y": 1}]], [[], [{"y": 2}, {"y": 3}]]]),
},

# ==================================================
# Line: 539

"row_partitions": lambda: [
    row_partition.RowPartition.from_row_lengths([3]),
    row_partition.RowPartition.from_row_lengths([2, 0, 1]),
    row_partition.RowPartition.from_uniform_row_length(3, nvals=9)
]

# ==================================================
# Line: 578

"fields": (lambda: {
    "a": ragged_factory_ops.constant(
        [[1]], row_splits_dtype=dtypes.int32),
    "b": ragged_factory_ops.constant(
        [[1]], row_splits_dtype=dtypes.int64)}),

# ==================================================
# Line: 848

"expected": lambda: StructuredTensor.from_fields(shape=[], fields={
    "a": 12,
    "b": [1, 2, 3],
    "c": ragged_factory_ops.constant([[1, 2], [3]])})

# ==================================================
# Occurrences: Lines 863-876 (2 instances)

"expected": lambda: StructuredTensor.from_fields(shape=[], fields={
    "a": 12,
    "b": [1, 2, 3],
    "c": ragged_factory_ops.constant([[1, 2], [3]])})

# ==================================================
# Line: 928

"expected": lambda: StructuredTensor.from_fields(shape=[2], fields={
    "a": [1, 2],
    "b": StructuredTensor.from_fields(shape=[2], fields={
        "x": ragged_factory_ops.constant([[1, 2], [3]])})}),

# ==================================================
# Line: 937

"expected": lambda: StructuredTensor.from_fields(shape=[2], fields={
    "a": [1, 2],
    "b": StructuredTensor.from_fields(shape=[2, None], fields={
        "x": ragged_factory_ops.constant([[[1, 2], [5]], [[3]]])})}),

# ==================================================
# Line: 946

"expected": lambda: StructuredTensor.from_fields(
    shape=[2, None],
    fields={
        "a": ragged_factory_ops.constant([[1, 2, 3], [4, 5]])})

# ==================================================
# Line: 956

"expected": lambda: StructuredTensor.from_fields(
    shape=[2, None], fields={
        "a": ragged_factory_ops.constant([[1, 2, 3], [4, 5, 6]])})

# ==================================================
# Occurrences: Lines 996-1029 (4 instances)

st=lambda: StructuredTensor.from_fields(
    {}, (2, None),
    row_partitions=[
        row_partition.RowPartition.from_row_lengths([3, 2])]),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
# Line: 1314

lambda: np_utils.cond(
    math_ops.equal(ndim_, 1),
    lambda: array_ops.pad(old_shape, [[1, 1]], constant_values=1),
    lambda: array_ops.pad(old_shape, [[0, 1]], constant_values=1),
),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/check_ops.py
# Line: 1954

diff = lambda: compare_op(
    array_ops.strided_slice(x, [1], [1] + s_len),
    array_ops.strided_slice(x, [0], s_len),
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg_ops.py
# Line: 750

lambda i: math_ops.cast(
    array_ops.squeeze(
        array_ops.where_v2(math_ops.equal(perm_before, i))),
    dtype=dtypes.int32), axes)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
# Line: 1065

kwargs=lambda: {
    'tensor': ragged_factory_ops.constant([[1, 2], [3]]),
    'shape': DynamicRaggedShape.from_lengths([3, (1, 0, 2)]),
},

# ==================================================
# Line: 1107

kwargs=lambda: {
    'shape_x': DynamicRaggedShape.from_lengths([2, (2, 3), 1]),
    'shape_y': DynamicRaggedShape.from_lengths([5])
},

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_print_op_test.py
# Line: 61

inputs=lambda: [
    ragged_factory_ops.constant([[1, 2], [3]]),
    ragged_factory_ops.constant([[5], [], [6, 7, 8]])
],

# ==================================================
# Line: 90

inputs=lambda: [
    ragged_factory_ops.constant([[1, 2, 3, 4, 5, 6, 7, 8, 9], [10], [
    ], [], [], [], [11, 12]])
],

# ==================================================
# Occurrences: Lines 99-110 (2 instances)

inputs=lambda: [
    ragged_factory_ops.constant([[1, 2, 3, 4, 5, 6, 7, 8, 9], [10], [
    ], [], [], [], [11, 12]])
],

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_matmul_op_test.py
# Line: 89

b=lambda: ragged_factory_ops.constant([[[1, 2], [3, 4], [5, 6],
                                        [7, 8]], [[9, 10], [11, 12]]],
                                      ragged_rank=1),

# ==================================================
# Line: 105

a=lambda: ragged_factory_ops.constant(
    [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [8, 7, 6], [5, 4, 3]]],
    ragged_rank=1),

# ==================================================
# Occurrences: Lines 165-189 (5 instances)

b=lambda: ragged_factory_ops.constant([[[3, 1], [4, 1], [5, 9], [
    1, 2
], [3, 4]], [[2, 4, 6], [1, 3, 5], [7, 8, 9], [1, 2, 3], [3, 2, 1]]]),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Line: 1023

row_partitions=lambda: [  # pylint: disable=g-long-lambda
    RowPartition.from_value_rowids([0, 2, 4], nrows=5),
    RowPartition.from_value_rowids([0, 2, 5], nrows=6)
],

# ==================================================
# Line: 2898

row_partitions=lambda: [  # pylint: disable=g-long-lambda
    RowPartition.from_uniform_row_length(1, 3, nrows=3),
    RowPartition.from_uniform_row_length(1, 4, nrows=4)
],

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/variables.py
# Line: 1754

assign_fn = lambda var, r_value: var.assign_add(
    r_value, use_locking=use_locking, name=name, read_value=read_value)

# ==================================================
# Line: 1762

assign_fn = lambda var, r_value: var.assign_sub(
    r_value, use_locking=use_locking, name=name, read_value=read_value)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/data_flow_ops.py
# Line: 2034

fn = lambda: gen_data_flow_ops.unstage(dtypes=self._dtypes,
                shared_name=self._name, name=name,
                capacity=self._capacity,
                memory_limit=self._memory_limit)

# ==================================================
# Line: 2064

fn = lambda: gen_data_flow_ops.stage_peek(index,
                dtypes=self._dtypes, shared_name=self._name,
                name=name, capacity=self._capacity,
                memory_limit=self._memory_limit)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
# Line: 407

lambda: [array_ops.concat([x, y], axis=0)  # pylint: disable=g-long-lambda
         for x, y in zip(remaining_output_tensors,
                         tiled_output_tensors)])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/cudnn_deterministic_base.py
# Line: 106

self._assert_reproducible(lambda: nn_ops.conv3d(
    in_op,
    filter_op,
    strides=[1, 1, 1, 1, 1],
    padding='VALID',
    data_format='NCDHW',
    dilations=[1, 1, 2, 2, 2]))

# ==================================================
# Line: 126

self._assert_reproducible(lambda: nn_ops.conv3d(
    in_op,
    filter_op,
    strides=[1, 1, 1, 1, 1],
    padding='VALID',
    data_format='NCDHW',
    dilations=[1, 1, 2, 2, 2]))

# ==================================================
# Line: 145

self._assert_reproducible(lambda: nn_ops.conv2d_backprop_filter(
    in_op,
    filter_shape,
    out_op,
    strides=strides,
    padding=padding,
    dilations=dilations))

# ==================================================
# Line: 170

self._assert_reproducible(lambda: nn_ops.conv2d_backprop_input(
    in_shape,
    filter_op,
    out_op,
    strides=strides,
    padding=padding,
    dilations=dilations))

# ==================================================
# Line: 199

self._assert_reproducible(lambda: nn_ops.conv2d_transpose_v2(
    in_op,
    filter_op,
    out_shape,
    strides=1,
    padding='SAME',
    data_format='NHWC',
    dilations=[1, rate, rate, 1]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Line: 2615

b = lambda x: tf_cond.cond(
    constant_op.constant(True),
    lambda: math_ops.add(x, one), lambda: math_ops.subtract(x, one))

# ==================================================
# Line: 2639

b = lambda x: tf_cond.cond(math_ops.less(0, 1),
                           lambda: math_ops.add(x, 1),
                           lambda: math_ops.subtract(x, 1))

# ==================================================
# Line: 3770

b = lambda x: tf_cond.cond(constant_op.constant(True),
                           lambda: math_ops.square(x),
                           lambda: math_ops.subtract(x, one))

# ==================================================
# Line: 3792

b = lambda x: tf_cond.cond(constant_op.constant(True),
                           lambda: math_ops.square(x),
                           lambda: math_ops.subtract(x, one))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/session.py
# Line: 119

(sparse_tensor.SparseTensor, lambda fetch: ([
    fetch.indices, fetch.values, fetch.dense_shape
], lambda fetched_vals: sparse_tensor.SparseTensorValue(*fetched_vals)),

# ==================================================
# Occurrences: Lines 128-133 (2 instances)

lambda fetch: ([fetch.values, fetch.indices] if fetch.dense_shape is None
               else [fetch.values, fetch.indices, fetch.dense_shape
                    ], _get_indexed_slices_value_from_fetches),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/dataset_ops.py
# Line: 5018

lambda: logging_ops.Print(  # pylint: disable=g-long-lambda
    accept_dist, [proportion_rejected, initial_dist, accept_dist],
    message="Proportion of examples rejected by sampler is high: ",
    summarize=100,
    first_n=10))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/load_op.py
# Line: 55

reader_func = lambda datasets: datasets.interleave(  # pylint:disable=g-long-lambda
    lambda x: x,
    cycle_length=multiprocessing.cpu_count(),
    num_parallel_calls=dataset_ops.AUTOTUNE)

# ==================================================
# Line: 134

lambda chunk_file: _SnapshotChunkDataset(  # pylint:disable=g-long-lambda
    chunk_file,
    element_spec=_parse_element_spec(metadata.element_spec),
    compression=metadata.compression))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/snapshot_op.py
# Line: 73

reader_func = lambda datasets: datasets.interleave(  # pylint:disable=g-long-lambda
    lambda x: x,
    cycle_length=multiprocessing.cpu_count(),
    num_parallel_calls=dataset_ops.AUTOTUNE)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/util/structure_test.py
# Line: 74

("Nested_2", lambda: {
    "a":
        constant_op.constant(37.0),
    "b": (sparse_tensor.SparseTensor(
        indices=[[0, 0]], values=[1], dense_shape=[1, 1]),
          sparse_tensor.SparseTensor(
              indices=[[3, 4]], values=[-1], dense_shape=[4, 5]))
}, lambda: dict, lambda: [dtypes.float32, dtypes.variant, dtypes.variant],

# ==================================================
# Line: 103

("Tensor", lambda: constant_op.constant(37.0), lambda: [
    constant_op.constant(38.0),
    array_ops.placeholder(dtypes.float32), 42.0,
    np.array(42.0, dtype=np.float32)
], lambda: [constant_op.constant([1.0, 2.0]),

# ==================================================
# Occurrences: Lines 115-153 (6 instances)

dtype=dtypes.float32, element_shape=(3,), size=0), lambda: [
    tensor_array_ops.TensorArray(
        dtype=dtypes.float32, element_shape=(3,), size=0),
    tensor_array_ops.TensorArray(
        dtype=dtypes.float32, element_shape=(3,), size=10)
], lambda: [

# ==================================================
# Line: 318

lambda: {
    "a":
        constant_op.constant(37.0),
    "b": (sparse_tensor.SparseTensor(
        indices=[[0, 0]], values=[1], dense_shape=[1, 1]),
          sparse_tensor.SparseTensor(
              indices=[[3, 4]], values=[-1], dense_shape=[4, 5]))
},

# ==================================================
# Occurrences: Lines 476-482 (2 instances)

("Nest", lambda:
 (constant_op.constant([[1.0, 2.0], [3.0, 4.0]]),
  sparse_tensor.SparseTensor(
      indices=[[0, 0], [1, 1]], values=[13, 27], dense_shape=[2, 2])),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/util/sparse_test.py
# Line: 185

("TestCase_9", lambda:
 (sparse_tensor.SparseTensor(indices=[[0]], values=[1], dense_shape=[1]),
  (), constant_op.constant([1])), lambda: (sparse_tensor.SparseTensor,

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
# Line: 513

lambda seed: stateless_random_ops.stateless_random_uniform(
    (128, 1024, 1024), seed, dtype=dtypes.float32
)

# ==================================================
# Line: 588

lambda: self._build_shuffle_dataset(
    range_limit=range_limit,
    num_repeats=num_repeats,
    buffer_size=buffer_size,
    seed=seed,
    reshuffle_each_iteration=reshuffle_each_iteration,
    symbolic_checkpoint=symbolic_checkpoint,
),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
# Occurrences: Lines 47-55 (2 instances)

("Sparse", lambda: sparse_tensor.SparseTensor(
    indices=[[0, 1]],
    values=constant_op.constant([0], dtype=dtypes.int32),
    dense_shape=[10, 10]),

# ==================================================
# Line: 86

lambda: sparse_tensor.SparseTensor(
    indices=[[0, 1], [1, 0]], values=[37.0, 42.0], dense_shape=[2, 2]),

# ==================================================
# Line: 97

}, lambda: {
    "a":
        constant_op.constant([4, 5, 6], dtype=dtypes.int32),
    "b":
        sparse_tensor.SparseTensor(
            indices=[[0, 1], [1, 0]],
            values=[37.0, 42.0],
            dense_shape=[2, 2])
}, False),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
# Line: 68

lambda x: dataset_ops.Dataset.from_tensor_slices(x).flat_map(
    lambda y: dataset_ops.Dataset.from_tensors(y).repeat(y)
)

# ==================================================
# Line: 84

lambda x: dataset_ops.Dataset.from_tensor_slices(x).flat_map(
    lambda y: dataset_ops.Dataset.from_tensors(y).repeat(y)
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
# Line: 142

lambda: self._build_repeat_dataset(
    num_elements, num_epochs, num_outputs=num_outputs, options=options),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/fingerprint_test.py
# Occurrences: Lines 63-73 (2 instances)

lambda: (
    readers.TFRecordDataset(["f1.txt", "f2.txt"]),
    readers.TFRecordDataset(["f1.txt", "f3.txt"]),
),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
# Line: 171

lambda: self._build_random_dataset(
    seed=seed,
    num_elements=num_elements,
    rerandomize_each_iteration=rerandomize_each_iteration),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
# Line: 1526

lambda seed: stateless_random_ops.stateless_random_uniform(
    (128, 1024, 1024), seed, dtype=dtypes.float32
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/cardinality_test.py
# Occurrences: Lines 54-59 (2 instances)

lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).concatenate(
    dataset_ops.Dataset.range(5)), dataset_ops.UNKNOWN),

# ==================================================
# Occurrences: Lines 86-96 (3 instances)

("Interleave1", lambda: dataset_ops.Dataset.range(5).interleave(
    lambda _: dataset_ops.Dataset.from_tensors(0), cycle_length=1),

# ==================================================
# Occurrences: Lines 156-163 (2 instances)

("Zip3", lambda: dataset_ops.Dataset.zip((dataset_ops.Dataset.range(
    5), dataset_ops.Dataset.range(3).repeat())), 5),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/distributed_save_load_test.py
# Line: 169

lambda _: dataset_ops.Dataset.load(
    snapshot_dir.full_path,
    reader_func=_interleave_shuffled_chunks,
    wait=True))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
# Line: 220

self, lambda: self._build_dataset(
    num_elements_per_file=num_elements_per_file,
    num_files=num_files,
    num_epochs=num_epochs,
    seed=seed,
    reshuffle_each_iteration=reshuffle_each_iteration,
    symbolic_checkpoint=symbolic_checkpoint), num_outputs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
# Line: 228

dataset = dataset.map(lambda n: string_ops.string_join(  # pylint:disable=g-long-lambda
    [self.get_temp_dir(),
     string_ops.string_format("/tf_record.{}.txt", [n])]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
# Line: 71

lambda: collective_all_reduce_strategy.
CollectiveAllReduceStrategy._from_local_devices((
    "/device:CPU:0", "/device:CPU:1")),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
# Line: 1268

lambda: mirrored_strategy.MirroredStrategy(
    devices=mirrored_strategy.all_local_devices(),
    cross_device_ops=cross_device_ops_lib.ReductionToOneDevice(
    ),
),

# ==================================================
# Line: 1369

lambda: mirrored_strategy.MirroredStrategy(
    devices=["/job:worker/task:0/gpu:{}".format(
        i) for i in range(context.num_gpus())]),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
# Occurrences: Lines 439-467 (7 instances)

lambda: check_ops.assert_equal_v2(
    w.scatter_add(_make_index_slices(values=[1., 2.], indices=[0, 2])),
    [1., 0., 2.]), w)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compilation_test.py
# Line: 211

f = lambda: tracing_compilation.call_function(  # pylint: disable=g-long-lambda
    tracing_options=tracing_compilation.TracingOptions(f_py, 'f')
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
# Line: 935

lambda: tracing_compilation.call_function(  # pylint: disable=g-long-lambda
    inner_args, inner_kwds, self._no_variable_creation_config
),

# ==================================================
