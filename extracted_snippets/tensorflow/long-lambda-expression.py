# long-lambda-expression snippets for tensorflow

# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/python_api_parameter_converter_test.py
# Line: 419

outputs=lambda: [
    Const([[1, 2, 3], [4, 5, 6]]),
    [Const([1, 2]), Const([3, 4, 5]),
     Const([6])],
    [1, 2, 3],
    "Foo",
    [Const([1, 2]),
     Const([["three"]]),
     Const([4]),
     Const("five")],
    [Const(1),
     Const("two"),
     Const([[3, 4], [5, 6]]),
     Const([["7"]])],
],

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/composite_tensor_test.py
# Line: 402

('Nested structure', lambda: {
    'a':
        indexed_slices.IndexedSlices(
            constant_op.constant([1, 2, 3]),
            constant_op.constant([2, 8, 4])),
    'b': [
        ragged_factory_ops.constant([[1, 2], [3]]),
        sparse_tensor.SparseTensor([[3], [7]], ['a', 'b'], [10])
    ]
}),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
# Line: 249

return lambda: {
    'a':
        np.ones([1, 2, 3, 1]),
    'b':
        np.ones([1, 2, 3, 1, 5]),
    'c':
        ragged_factory_ops.constant(
            np.zeros([1, 2, 3, 1], dtype=np.uint8), dtype=dtypes.uint8),
    'd':
        ragged_factory_ops.constant(
            np.zeros([1, 2, 3, 1, 3]).tolist(), ragged_rank=1),
    'e':
        ragged_factory_ops.constant(
            np.zeros([1, 2, 3, 1, 2, 2]).tolist(), ragged_rank=2),
    'f':
        ragged_factory_ops.constant(
            np.zeros([1, 2, 3, 1, 3]), dtype=dtypes.float32),
    'g':
        StructuredTensor.from_pyval([[
            [  # pylint: disable=g-complex-comprehension
                [{
                    'x': j,
                    'y': k
                }] for k in range(3)
            ] for j in range(2)
        ]]),
    'h':
        StructuredTensor.from_pyval([[
            [  # pylint: disable=g-complex-comprehension
                [[
                    {
                        'x': j,
                        'y': k,
                        'z': z
                    } for z in range(j)
                ]] for k in range(3)
            ] for j in range(2)
        ]]),
}

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
# Line: 296

"fields": lambda: {
    "a": np.ones([1, 2, 3, 1]),
    "b": np.ones([1, 2, 3, 1, 5]),
    "c": ragged_factory_ops.constant(np.zeros([1, 2, 3, 1])),
    "d": ragged_factory_ops.constant(
        np.zeros([1, 2, 3, 1, 3]).tolist(), ragged_rank=1),
    "e": ragged_factory_ops.constant(
        np.zeros([1, 2, 3, 1, 2, 2]).tolist(), ragged_rank=2),
    "f": ragged_factory_ops.constant(np.zeros([1, 2, 3, 1, 3])),
    "g": StructuredTensor.from_pyval(
        [[[[{"x": j, "y": k}] for k in range(3)]
          for j in range(2)]]),
    "h": StructuredTensor.from_pyval(
        [[[[[{"x": j, "y": k, "z": z} for z in range(j)]]
           for k in range(3)]
          for j in range(2)]]),
},

# ==================================================
# Line: 548

"fields": lambda: {
    "a": np.ones([1, 2, 3, 1]),
    "b": np.ones([1, 2, 3, 1, 5]),
    "c": ragged_factory_ops.constant(np.zeros([1, 2, 3, 1])),
    "d": ragged_factory_ops.constant(
        np.zeros([1, 2, 3, 1, 3]).tolist(), ragged_rank=1),
    "e": ragged_factory_ops.constant(
        np.zeros([1, 2, 3, 1, 2, 2]).tolist(), ragged_rank=2),
    "f": ragged_factory_ops.constant(np.zeros([1, 2, 3, 1, 3])),
    "g": StructuredTensor.from_pyval(
        [[[[{"x": j, "y": k}] for k in range(3)]
          for j in range(2)]]),
    "h": StructuredTensor.from_pyval(
        [[[[[{"x": j, "y": k, "z": z} for z in range(j)]]
           for k in range(3)]
          for j in range(2)]]),
},

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
# Line: 70

lambda: np_utils.cond(  # pylint: disable=g-long-lambda
    math_ops.equal(array_ops.rank(b), 1),
    lambda: math_ops.tensordot(a, b, axes=[[-1], [-1]]),
    lambda: math_ops.tensordot(a, b, axes=[[-1], [-2]]),
),

# ==================================================
# Line: 247

lambda: np_utils.cond(  # pylint: disable=g-long-lambda
    math_ops.equal(np_utils.tf_rank(x1), 1),
    lambda: math_ops.tensordot(  # pylint: disable=g-long-lambda
        x1, x2, axes=[[0], [-2]]
    ),
    lambda: math_ops.matmul(x1, x2),
),

# ==================================================
# Line: 368

lambda: np_utils.cond(  # pylint: disable=g-long-lambda
    axis_c == np_utils.subtract(array_ops.rank(c), 1),
    lambda: c,
    lambda: move_last_to_axis(c, axis_c),
),

# ==================================================
# Line: 1161

lambda: np_utils.cond(  # pylint: disable=g-long-lambda
    np_utils.reduce_all(
        math_ops.equal(array_ops.shape(x1), array_ops.shape(x2))
    ),
    lambda: math_ops.reduce_all(math_ops.equal(x1, x2)),
    lambda: constant_op.constant(False),
),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Occurrences: Lines 3432-3443 (2 instances)

lambda i, y: (
    i + 1,
    y + tf_cond.cond(
        constant_op.constant(True),
        # True branch
        lambda: while_loop_tf.while_loop(
            # Inner loop condition
            lambda j, z: j < 3,
            # Inner loop body
            lambda j, z: (j + 1, z + math_ops.square(var)),
            # Inner initial loop value
            [0, y])[1],
        # False branch
        lambda: (0.0))),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/util/structure_test.py
# Line: 160

}], lambda: [{
    "a": constant_op.constant(15.0),
    "b": constant_op.constant([4, 5, 6, 7])
}, {
    "a": constant_op.constant(15),
    "b": constant_op.constant([4, 5, 6])
}, {
    "a":
        constant_op.constant(15),
    "b":
        sparse_tensor.SparseTensor(
            indices=[[0], [1], [2]], values=[4, 5, 6], dense_shape=[3])
}, (constant_op.constant(15.0), constant_op.constant([4, 5, 6]))]),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/fingerprint_test.py
# Line: 56

lambda: (
    dataset.range(10).flat_map(dataset.range),
    dataset.range(10).flat_map(lambda x: dataset.range(x + 1)),
),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/cardinality_test.py
# Occurrences: Lines 62-75 (4 instances)

lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).concatenate(
    dataset_ops.Dataset.range(5).filter(lambda _: True)),

# ==================================================
# Line: 158

("Zip4", lambda: dataset_ops.Dataset.zip(
    (dataset_ops.Dataset.range(5).repeat(), dataset_ops.Dataset.range(3).
     repeat())), dataset_ops.INFINITE),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/saver_test.py
# Line: 2381

self._testGradientSerDes(lambda x: cond.cond(
    x > 0,
    lambda: cond.cond(x > 3,
                      lambda: array_ops.identity(x),
                      lambda: math_ops.multiply(x, 2.0)),
    lambda: cond.cond(x < -3,
                      lambda: constant_op.constant(1.0),
                      lambda: math_ops.multiply(x, -1.0))))

# ==================================================
