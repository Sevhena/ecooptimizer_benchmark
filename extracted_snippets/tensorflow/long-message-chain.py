# long-message-chain snippets for tensorflow

# File: /root/ecooptimizer/tensorflow/tensorflow/lite/ios/extract_object_files.py
# Line: 168

name = archive_file.read(filename_size).decode('utf-8').strip(' \x00')

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/lite.py
# Line: 2056

_jit(self._serving_funcs[0])
.trace(*ordered_inputs)
.lower(lowering_platforms=("cpu",))
.compiler_ir("hlo")
.as_serialized_hlo_module_proto()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/dtensor/python/save_restore.py
# Line: 134

if api.fetch_layout(tensor).mesh.device_type().upper() != 'CPU':

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor_shape_test.py
# Line: 321

tensor_shape.TensorShape([3, 4, 7]).merge_with(
    tensor_shape.TensorShape([3, 4, 7])).as_list())

# ==================================================
# Line: 342

tensor_shape.TensorShape([3, 4, 7]).merge_with(
    tensor_shape.TensorShape(None)).as_list())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/test_util_test.py
# Occurrences: Lines 1207-1208 (2 instances)

self.assertTrue(LeakedObjectTest("test_has_leak").run().wasSuccessful())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/op_callbacks_test.py
# Line: 661

dataset = dataset_ops.Dataset.from_tensor_slices(tensor).batch(2).map(
    map_fn)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor_util.py
# Line: 47

return numpy_compat.np_asarray(x, np.float16).view(np.uint16).item()

# ==================================================
# Line: 64

return numpy_compat.np_asarray(
    x, dtype=dtypes.bfloat16.as_numpy_dtype).view(np.uint16).item()

# ==================================================
# Line: 82

numpy_compat.np_asarray(
    proto_values, dtype=dtypes.float8_e5m2.as_numpy_dtype)
.view(np.uint8)
.tobytes()

# ==================================================
# Line: 98

numpy_compat.np_asarray(
    proto_values, dtype=dtypes.float8_e4m3fn.as_numpy_dtype)
.view(np.uint8)
.tobytes()

# ==================================================
# Line: 115

numpy_compat.np_asarray(
    proto_values, dtype=dtypes.float8_e4m3fnuz.as_numpy_dtype
)
.view(np.uint8)
.tobytes()

# ==================================================
# Line: 134

numpy_compat.np_asarray(
    proto_values, dtype=dtypes.float8_e4m3b11fnuz.as_numpy_dtype
)
.view(np.uint8)
.tobytes()

# ==================================================
# Line: 153

numpy_compat.np_asarray(
    proto_values, dtype=dtypes.float8_e5m2fnuz.as_numpy_dtype
)
.view(np.uint8)
.tobytes()

# ==================================================
# Line: 762

return (np.frombuffer(tensor.tensor_content,
                      dtype=dtype).copy().reshape(shape))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3.py
# Line: 664

tf_device.DeviceSpec.from_string(tpu_devices[rid][cid])
.replace(device_type="CPU", device_index=0)
.to_string()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/datasets.py
# Line: 194

output_dataset = dataset_ops.Dataset.range(2).repeat().map(
    MapFn, num_parallel_calls=4 if sloppy else None)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
# Occurrences: Lines 224-225 (2 instances)

val0 = np.arange(6).reshape((2, 3)).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3_test.py
# Line: 190

dataset.unbatch()
.repeat()
.batch(16 * strategy.num_replicas_in_sync, drop_remainder=True)

# ==================================================
# Line: 254

dataset.unbatch()
.repeat()
.batch(16 * strategy.num_replicas_in_sync, drop_remainder=True)

# ==================================================
# Line: 318

dataset.unbatch()
.repeat()
.batch(16 * strategy.num_replicas_in_sync, drop_remainder=True)

# ==================================================
# Line: 419

dataset.unbatch()
.repeat()
.batch(16 * strategy.num_replicas_in_sync, drop_remainder=True)

# ==================================================
# Line: 528

dataset.unbatch()
.repeat()
.batch(16 * strategy.num_replicas_in_sync, drop_remainder=True)

# ==================================================
# Line: 603

dataset.unbatch()
.repeat()
.batch(16 * strategy.num_replicas_in_sync, drop_remainder=True)

# ==================================================
# Line: 683

dataset.unbatch()
.repeat()
.batch(16 * strategy.num_replicas_in_sync, drop_remainder=True)

# ==================================================
# Line: 767

dataset.unbatch()
.repeat()
.batch(16 * strategy.num_replicas_in_sync, drop_remainder=True)

# ==================================================
# Line: 884

dataset.unbatch()
.repeat()
.batch(16 * strategy.num_replicas_in_sync, drop_remainder=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/client/client.py
# Line: 278

r = service.projects().locations().nodes().get(name=self._full_name())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/image_grad_test_base.py
# Line: 46

x = np.arange(0, 4).reshape(in_shape).astype(nptype)

# ==================================================
# Line: 61

x = np.arange(0, 6).reshape(in_shape).astype(nptype)

# ==================================================
# Line: 78

x = np.arange(0, 24).reshape(in_shape).astype(nptype)

# ==================================================
# Line: 95

x = np.arange(0, np.prod(in_shape)).reshape(in_shape).astype(nptype)

# ==================================================
# Line: 141

x = np.arange(np.prod(in_shape)).reshape(in_shape).astype(dtype)

# ==================================================
# Line: 164

x = np.arange(np.prod(in_shape)).reshape(in_shape).astype(np.float32)

# ==================================================
# Line: 227

x = np.arange(0, 24).reshape(in_shape).astype(np.uint8)

# ==================================================
# Line: 285

x = np.arange(0, 4).reshape(in_shape).astype(np.float32)

# ==================================================
# Line: 300

x = np.arange(0, 6).reshape(in_shape).astype(np.float32)

# ==================================================
# Line: 319

x = np.arange(0, 24).reshape(in_shape).astype(np.float32)

# ==================================================
# Line: 340

x = np.arange(0, 24).reshape(in_shape).astype(np.uint8)

# ==================================================
# Line: 357

x = np.arange(0, 6).reshape(in_shape).astype(np.float32)

# ==================================================
# Line: 397

x = np.arange(0, 6).reshape(in_shape).astype(np.float32)

# ==================================================
# Line: 435

image = np.arange(0, batch * image_height * image_width *
                  depth).reshape(image_shape).astype(np.float32)

# ==================================================
# Line: 508

image = np.arange(0, batch * image_height * image_width *
                  depth).reshape(image_shape).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
# Occurrences: Lines 455-459 (5 instances)

run_test(np.arange(9).reshape((3, 3)).tolist())

# ==================================================
# Occurrences: Lines 502-506 (4 instances)

run_test(np.arange(4).reshape((2, 2)).tolist())

# ==================================================
# Line: 633

run_test(np.arange(9).reshape((3, 3)).tolist())

# ==================================================
# Occurrences: Lines 710-715 (4 instances)

run_test(np.arange(8).reshape((2, 2, 2)).tolist(), axis=(0, 2))

# ==================================================
# Occurrences: Lines 739-744 (4 instances)

run_test(np.arange(8).reshape((2, 2, 2)).tolist(), axis=(0, 2))

# ==================================================
# Occurrences: Lines 767-772 (4 instances)

run_test(np.arange(8).reshape((2, 2, 2)).tolist(), axis=(0, 2))

# ==================================================
# Occurrences: Lines 795-800 (4 instances)

run_test(np.arange(8).reshape((2, 2, 2)).tolist(), axis=(0, 2))

# ==================================================
# Occurrences: Lines 820-825 (4 instances)

run_test(np.arange(8).reshape((2, 2, 2)).tolist(), axis=(0, 2))

# ==================================================
# Line: 908

run_test(np.arange(8).reshape((2, 2, 2)).tolist())

# ==================================================
# Occurrences: Lines 1031-1037 (7 instances)

run_test(np.arange(30).reshape(2, 3, 5).tolist())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
# Occurrences: Lines 87-88 (2 instances)

(np.arange(2 * 3 * 5).reshape([2, 3, 5]).tolist(),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/weak_tensor_np_array_ops_test.py
# Occurrences: Lines 475-479 (5 instances)

run_test(np.arange(9).reshape((3, 3)).tolist())

# ==================================================
# Occurrences: Lines 527-531 (4 instances)

run_test(np.arange(4).reshape((2, 2)).tolist())

# ==================================================
# Line: 607

run_test(np.arange(9).reshape((3, 3)).tolist())

# ==================================================
# Occurrences: Lines 724-729 (4 instances)

run_test(np.arange(8).reshape((2, 2, 2)).tolist(), axis=(0, 2))

# ==================================================
# Occurrences: Lines 766-774 (4 instances)

run_test(np.arange(8).reshape((2, 2, 2)).tolist(), axis=(0, 2))

# ==================================================
# Occurrences: Lines 805-808 (2 instances)

np.arange(8).reshape((2, 2, 2)).tolist(), res_dtype=None, axis=(0, 2)

# ==================================================
# Occurrences: Lines 814-817 (2 instances)

np.arange(8).reshape((2, 2, 2)).tolist(), res_dtype=None, axis=(2, 0)

# ==================================================
# Occurrences: Lines 853-856 (2 instances)

np.arange(8).reshape((2, 2, 2)).tolist(), res_dtype=None, axis=(0, 2)

# ==================================================
# Occurrences: Lines 862-865 (2 instances)

np.arange(8).reshape((2, 2, 2)).tolist(), res_dtype=None, axis=(2, 0)

# ==================================================
# Occurrences: Lines 902-910 (4 instances)

run_test(np.arange(8).reshape((2, 2, 2)).tolist(), axis=(0, 2))

# ==================================================
# Line: 1007

run_test(np.arange(8).reshape((2, 2, 2)).tolist())

# ==================================================
# Occurrences: Lines 1172-1178 (7 instances)

run_test(np.arange(30).reshape(2, 3, 5).tolist())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/distribution.py
# Line: 1299

shape = tensor_shape.TensorShape([None]*sample_ndims).concatenate(
    self.batch_shape).concatenate([None]*event_ndims)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/image_ops_impl.py
# Line: 123

static_shape = image.get_shape().with_rank(rank).as_list()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/array_ops.py
# Line: 1437

ops.convert_to_tensor(
    axis, name="concat_dim",
    dtype=dtypes.int32).get_shape().assert_has_rank(0)

# ==================================================
# Line: 1531

tensor_shape.as_shape(shape_tensor[:axis]).concatenate(
    [first_dim]).concatenate(shape_tensor[axis + ndims_mask:]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/random_ops_util.py
# Line: 76

canon_alg = alg.strip().lower().replace("-", "").replace("_", "")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/tensor_array_ops_test.py
# Line: 40

values = (values.write(0, a).write(
    1, constant_op.constant([], dtypes.string))).write(2, b).write(
        3, constant_op.constant([], dtypes.string))

# ==================================================
# Line: 54

values = (values.write(0, a).write(
    1, constant_op.constant([], dtypes.string))).write(2, b).write(
        3, constant_op.constant([], dtypes.string))

# ==================================================
# Line: 65

values = (values.write(0, a).write(
    1, constant_op.constant([], dtypes.string))).write(2, b).write(
        3, constant_op.constant([], dtypes.string))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/resource_variable_ops.py
# Line: 745

op_device = pydev.DeviceSpec.from_string(self.device).replace(
    device_type="CPU", device_index=0).to_string()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
# Line: 1008

ta = tensor_array_ops.TensorArray(
    dtypes.int32, 2, clear_after_read=False).write(0, 0).write(1, 1)

# ==================================================
# Line: 1019

ta = tensor_array_ops.TensorArray(
    dtypes.int32, 2, clear_after_read=False).write(0, 0).write(1, 1)

# ==================================================
# Line: 1054

ta1 = tensor_array_ops.TensorArray(dtypes.int32, 2).write(0,
                                                          i).write(1, 1)

# ==================================================
# Occurrences: Lines 1066-1071 (2 instances)

ta1 = tensor_array_ops.TensorArray(dtypes.int32,
                                   2).scatter([0],
                                              [[i, 2]]).scatter([1],
                                                                [[1, 2]])

# ==================================================
# Occurrences: Lines 1080-1083 (2 instances)

ta1 = tensor_array_ops.TensorArray(
    dtypes.int32, 2, clear_after_read=False).write(0, i).write(1, 1)

# ==================================================
# Occurrences: Lines 1093-1096 (2 instances)

ta1 = tensor_array_ops.TensorArray(
    dtypes.int32, 2, clear_after_read=False).write(0, i).write(1, 1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/save_test.py
# Occurrences: Lines 1511-1515 (2 instances)

self.assertEqual(label, model.fn().numpy().decode("utf-8"))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/saved_model_test.py
# Line: 1284

ops.get_default_graph().get_tensor_by_name(
    "scope_name/constant_tensor_name:0").eval())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
# Occurrences: Lines 257-259 (2 instances)

util.Checkpoint(s=restore_s).read(ckpt_path).expect_partial()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
# Line: 2965

checkpoint.restore(save_path).assert_consumed().run_restore_ops()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
# Occurrences: Lines 268-281 (3 instances)

np_input = np.arange(
    1.0, 49.0,
    dtype=dtype.as_numpy_dtype).reshape([2, 3, 4, 2]).astype(np.float32)

# ==================================================
# Line: 291

np_input = np.arange(
    1.0, 49.0,
    dtype=dtype.as_numpy_dtype).reshape([1, 2, 3, 4,
                                         2]).astype(np.float32)

# ==================================================
# Line: 300

np_input = np.arange(1.0, 129.0).reshape([4, 1, 1, 32]).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
# Line: 322

x = np.arange(np.prod(input_sizes)).reshape(input_sizes).astype(dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/trace_op_test.py
# Line: 38

x = np.random.rand(np.prod(shape)).astype(dtype).reshape(shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
# Line: 189

x = np.arange(-3, 3).reshape(1, 3, 2).astype(np.float32)

# ==================================================
# Occurrences: Lines 244-246 (2 instances)

x = np.arange(40, 40 + 6).reshape(6).astype(np.float32)

# ==================================================
# Occurrences: Lines 299-304 (2 instances)

x = np.arange(-3, 3).reshape(1, 3, 2).astype(np.float64)

# ==================================================
# Line: 353

x = np.arange(-3, 3).reshape(1, 3, 2).astype(np.float16)

# ==================================================
# Line: 412

x = np.arange(-6, 6,
              2).reshape(1, 3, 2).astype(bfloat16)

# ==================================================
# Line: 449

x = np.arange(-6, 6, 2).reshape(1, 3, 2).astype(np.int8)

# ==================================================
# Occurrences: Lines 457-461 (2 instances)

x = np.arange(6).reshape(1, 3, 2).astype(np.uint8)

# ==================================================
# Occurrences: Lines 469-473 (2 instances)

x = np.arange(6).reshape(1, 3, 2).astype(np.uint16)

# ==================================================
# Occurrences: Lines 487-491 (2 instances)

x = np.arange(6).reshape(1, 3, 2).astype(np.uint32)

# ==================================================
# Occurrences: Lines 503-513 (3 instances)

x = np.arange(-6 << 20, 6 << 20, 2 << 20).reshape(1, 3, 2).astype(np.int64)

# ==================================================
# Line: 559

x = (1 + 1j) * np.arange(-3, 3).reshape(1, 3, 2).astype(np.complex128)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
# Occurrences: Lines 149-150 (2 instances)

x = np.linspace(-15, 15, np.prod(xs)).astype(dtype).reshape(xs)

# ==================================================
# Occurrences: Lines 260-261 (2 instances)

x = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 284-285 (2 instances)

x = np.random.randint(0, 2, np.prod(xs)).astype(np.bool_).reshape(xs)

# ==================================================
# Occurrences: Lines 296-297 (2 instances)

x = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args

# ==================================================
# Line: 459

c = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 490-493 (4 instances)

c0 = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args

# ==================================================
# Line: 527

c = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args

# ==================================================
# Line: 553

c = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args

# ==================================================
# Line: 580

c = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args

# ==================================================
# Line: 599

c = np.random.randint(0, 3, 0).astype(np.bool_).reshape(1, 3, 0)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 1244-1248 (2 instances)

data = np.arange(1, 2, 0.10).reshape([5, 2]).astype(np.float32)

# ==================================================
# Line: 1279

data = np.arange(1, 2, 0.125).reshape([2, 4]).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
# Occurrences: Lines 264-271 (4 instances)

a_np = np.random.normal(-5, 5, m * k).astype(dtype).reshape([m, k])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/tensordot_op_test.py
# Occurrences: Lines 155-160 (2 instances)

a = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(a_shape)).reshape(a_shape).astype(dtype_)

# ==================================================
# Occurrences: Lines 209-212 (2 instances)

a_np = np.random.uniform(
    low=-1.0, high=1.0, size=np.prod(shape)).reshape(shape).astype(dtype_)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
# Occurrences: Lines 53-54 (2 instances)

x = np.linspace(-5, 20, 15).reshape(1, 3, 5).astype(np.float32)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 63-64 (2 instances)

x = np.linspace(-5, 20, 15).reshape(3, 5).astype(np.float32)

# ==================================================
# Occurrences: Lines 71-72 (2 instances)

x = np.linspace(-5, 20, 15).reshape(1, 3, 5).astype(np.float64)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 79-80 (2 instances)

x = np.linspace(-5, 20, 15).reshape(3, 5).astype(np.float64)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
# Occurrences: Lines 202-203 (2 instances)

x = np.linspace(-5, 20, 15).reshape(1, 3, 5).astype(np.float32)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 223-224 (2 instances)

a_pos_small = np.linspace(0.1, 2, 15).reshape(1, 3, 5).astype(np.float32)  # pylint: disable=too-many-function-args

# ==================================================
# Line: 232

n_small = np.arange(0, 15).reshape(1, 3, 5).astype(np.float32)

# ==================================================
# Occurrences: Lines 240-241 (2 instances)

x = np.array([1, 2, 3, 4]).reshape(2, 2).astype(np.float32)

# ==================================================
# Occurrences: Lines 250-256 (4 instances)

np.array([1, 1, 2, 2]).reshape(2, 2).astype(np.float32))

# ==================================================
# Occurrences: Lines 270-272 (2 instances)

x = np.linspace(-20, 20, 10).reshape(1, 2, 5).astype(bfloat16)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 279-280 (2 instances)

x = np.linspace(-5, 20, 15).reshape(1, 3, 5).astype(np.float64)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 300-301 (2 instances)

a_pos_small = np.linspace(0.1, 2, 15).reshape(1, 3, 5).astype(np.float32)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 311-312 (2 instances)

x = np.linspace(-5, 20, 15).reshape(1, 3, 5).astype(bf16_np)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 327-328 (2 instances)

x = np.arange(1, 13, 2).reshape(1, 3, 2).astype(np.uint8)

# ==================================================
# Occurrences: Lines 334-335 (2 instances)

x = np.arange(1, 13, 2).reshape(1, 3, 2).astype(np.int8)

# ==================================================
# Occurrences: Lines 346-347 (2 instances)

x = np.arange(1, 13, 2).reshape(1, 3, 2).astype(np.int16)

# ==================================================
# Occurrences: Lines 354-355 (2 instances)

x = np.arange(1, 13, 2).reshape(1, 3, 2).astype(np.uint16)

# ==================================================
# Occurrences: Lines 366-367 (2 instances)

x = np.arange(1, 13, 2).reshape(1, 3, 2).astype(np.int32)

# ==================================================
# Occurrences: Lines 385-386 (2 instances)

x = np.arange(1, 13, 2).reshape(1, 3, 2).astype(np.uint32)

# ==================================================
# Occurrences: Lines 394-395 (2 instances)

x = np.arange(1 << 40, 13 << 40, 2 << 40).reshape(1, 3, 2).astype(np.int64)

# ==================================================
# Occurrences: Lines 408-409 (2 instances)

x = np.arange(1, 13, 2).reshape(1, 3, 2).astype(np.uint32)

# ==================================================
# Occurrences: Lines 417-420 (2 instances)

x = (1 + 1j) * np.linspace(-10, 10, 6).reshape(1, 3, 2).astype(  # pylint: disable=too-many-function-args
    np.complex64)

# ==================================================
# Occurrences: Lines 432-435 (2 instances)

x = (1 + 1j) * np.linspace(-10, 10, 6).reshape(1, 3, 2).astype(  # pylint: disable=too-many-function-args
    np.complex128)

# ==================================================
# Occurrences: Lines 973-974 (2 instances)

x = np.linspace(-15, 15, np.prod(xs)).astype(dtype).reshape(xs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Line: 143

data = np.arange(np.prod(shape)).reshape(shape).astype(dtype.as_numpy_dtype)

# ==================================================
# Line: 372

np_arr = np.arange(0, 10).reshape([2, 5]).astype(np.float32)

# ==================================================
# Line: 843

np_arr = np.arange(1, 31).reshape([2, 3, 5]).astype(np.float32)

# ==================================================
# Line: 857

np_arr = np.arange(1, 31).reshape([2, 3, 5]).astype(np.float64)

# ==================================================
# Line: 871

x = np.arange(1.0, 49.0).reshape(s).astype(np.float64)

# ==================================================
# Line: 882

x = np.arange(1.0, 49.0).reshape(s).astype(np.float64)

# ==================================================
# Line: 893

x = np.arange(1.0, 49.0).reshape(s).astype(np.float64)

# ==================================================
# Line: 904

x = np.arange(1.0, 49.0).reshape(s).astype(np.float64)

# ==================================================
# Line: 960

np_arr = np.arange(-31, -1).reshape([2, 3, 5]).astype(np.int64)

# ==================================================
# Line: 974

np_arr = np.arange(-31, -1).reshape([2, 3, 5]).astype(np.float32)

# ==================================================
# Line: 988

np_arr = np.arange(-31, -1).reshape([2, 3, 5]).astype(np.float64)

# ==================================================
# Line: 1002

np_arr = np.arange(-31,
                   -1).reshape([2, 3,
                                5]).astype(dtypes.bfloat16.as_numpy_dtype)

# ==================================================
# Line: 1018

x = np.arange(-49.0, -1.0).reshape(s).astype(np.float64)

# ==================================================
# Line: 1029

x = np.arange(-49.0, -1.0).reshape(s).astype(np.float64)

# ==================================================
# Line: 1040

x = np.arange(-49.0, -1.0).reshape(s).astype(np.float64)

# ==================================================
# Line: 1051

x = np.arange(-49.0, -1.0).reshape(s).astype(np.float64)

# ==================================================
# Line: 1210

np_arr = np.floor(np.arange(0.0, 210.0) / 100.0).reshape([2, 3, 5,
                                                          7]).astype(
                                                              np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
# Occurrences: Lines 339-343 (2 instances)

self._compareCpu(np.arange(0, 6).reshape([3, 2]).astype(np.float32), [0, 1])

# ==================================================
# Line: 349

x = np.arange(0, 8).reshape([2, 4]).astype(np.float32)

# ==================================================
# Occurrences: Lines 361-388 (12 instances)

self._compare(np.arange(0, 21).reshape([3, 7]).astype(np.float16))

# ==================================================
# Occurrences: Lines 394-399 (3 instances)

(1 + 2j) * np.arange(0, 21).reshape([3, 7]).astype(np.complex64))

# ==================================================
# Occurrences: Lines 405-435 (15 instances)

(1 + 2j) * np.arange(0, 21).reshape([3, 7]).astype(np.complex128))

# ==================================================
# Line: 458

np.arange(np.prod(shape)).reshape(shape).astype(np.float32))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
# Line: 250

np.mod(np.arange(np.power(4, dims)), 10).reshape(
    (4,) * dims).astype(np_type), rank, rtol=tol, atol=tol)

# ==================================================
# Line: 262

np.mod(np.arange(np.power(4, dims)), 10)
.reshape((4,) * dims)
.astype(np_type),

# ==================================================
# Line: 286

np.mod(np.arange(np.power(4, dims)), 10)
.reshape((4,) * dims)
.astype(np_type),

# ==================================================
# Line: 310

np.mod(np.arange(np.power(4, dims)), 10)
.reshape((4,) * dims)
.astype(np_type),

# ==================================================
# Line: 363

np.mod(np.arange(np.power(4, 4)), 10).reshape((4,) * 4).astype(np_type),

# ==================================================
# Line: 376

np.mod(np.arange(np.power(128, dims)), 10).reshape(
    (128,) * dims).astype(np_type), rank, rtol=tol, atol=tol)

# ==================================================
# Line: 397

np.mod(np.arange(np.power(4, dims)), 10).reshape(
    (4,) * dims).astype(np_type),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
# Line: 229

value = np.arange(np.prod(shape)).reshape(shape).astype(dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
# Line: 79

ls = array_ops.concat(tensors, axis=0).numpy().tolist()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
# Occurrences: Lines 193-198 (2 instances)

x_np = np.random.uniform(
    low=-1.0, high=1.0, size=np.prod(shape_)).reshape(shape_).astype(dtype_)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
# Occurrences: Lines 72-75 (2 instances)

matrix = (np.random.normal(-5, 5,
                           m * n).astype(np.complex128).reshape([m, n]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/conjugate_gradient_test.py
# Line: 38

np.random.uniform(low=-1.0, high=1.0, size=np.prod(shape))
.reshape(shape)
.astype(dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
# Occurrences: Lines 128-133 (2 instances)

x_np = np.random.uniform(
    low=-1.0, high=1.0, size=np.prod(shape_)).reshape(shape_).astype(dtype_)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/self_adjoint_eig_op_test.py
# Occurrences: Lines 143-147 (2 instances)

a = np.random.uniform(
    low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)

# ==================================================
# Occurrences: Lines 190-194 (2 instances)

a = np.random.uniform(
    low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/eig_op_test.py
# Occurrences: Lines 162-166 (2 instances)

a = np.random.uniform(
    low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)

# ==================================================
# Occurrences: Lines 214-218 (2 instances)

a = np.random.uniform(
    low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
# Line: 234

matrix = np.random.uniform(
    low=-1.0, high=1.0, size=np.prod(shape)).reshape(shape).astype(dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
# Line: 111

matrix = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(shape)).reshape(shape).astype(np.complex64)

# ==================================================
# Line: 122

matrix = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(shape)).reshape(shape).astype(np.complex128)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_ls_op_test.py
# Line: 47

matrix = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(matrix_shape)).reshape(matrix_shape).astype(np.float32)

# ==================================================
# Line: 236

matrix = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(matrix_shape)).reshape(matrix_shape).astype(np.float32)

# ==================================================
# Line: 253

matrix = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(matrix_shape)).reshape(matrix_shape).astype(np.float32)

# ==================================================
# Line: 270

matrix = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(matrix_shape)).reshape(matrix_shape).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
# Line: 143

matrix = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(shape)).reshape(shape).astype(dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_grad_test.py
# Line: 118

return np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(shape_)).reshape(shape_).astype(dtype_)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
# Occurrences: Lines 77-79 (2 instances)

return [b"".join(c).decode("utf-32-be").encode(encoding) for c in chars]

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
# Line: 329

inp = np.random.rand(num_inputs).astype("f").reshape(input_shape)

# ==================================================
# Line: 335

grads = np.random.rand(num_grads).astype("f").reshape(slice_size)

# ==================================================
# Line: 354

inp = np.random.rand(num_inputs).astype("f").reshape(input_shape)

# ==================================================
# Line: 360

grads = np.random.rand(num_grads).astype("f").reshape(slice_size)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
# Line: 270

x = np.random.normal(0, 1, b * h * w * d *
                     block_size_sq).astype(np.float32).reshape(
                         [b * block_size * block_size, h, w, d])

# ==================================================
# Line: 330

x = np.random.normal(
    0, 1, np.prod(input_shape)).astype(np.float32).reshape(input_shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
# Occurrences: Lines 61-63 (2 instances)

self._testAll(np.arange(-15, 15).reshape([2, 3, 5]).astype(np.float32))

# ==================================================
# Occurrences: Lines 89-91 (2 instances)

self._testAll(np.arange(-15, 15).reshape([2, 3, 5]).astype(np.float64))

# ==================================================
# Line: 109

self._testAll(np.arange(-15, 15).reshape([2, 3, 5]).astype(np.int32))

# ==================================================
# Line: 116

self._testAll(np.arange(-15, 15).reshape([2, 3, 5]).astype(np.int64))

# ==================================================
# Occurrences: Lines 132-143 (4 instances)

(1 + 2j) * np.arange(-15, 15).reshape([2, 3, 5]).astype(np.complex64))

# ==================================================
# Line: 183

np.arange(-15, 15).reshape([2, 3, 5]).astype(np.float32),

# ==================================================
# Line: 189

np.arange(-15, 15).reshape([2, 3, 5]).astype(np.float32))

# ==================================================
# Line: 203

np.arange(-15, 15).reshape([2, 3, 5]).astype(np.float32),

# ==================================================
# Line: 451

x = np.arange(15).astype(in_type).reshape(*shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
# Line: 570

x = np.random.normal(0, 1, b * h * w * d *
                     block_size_sq).astype(np.float32).reshape(
                         [b, h * block_size, w * block_size, d])

# ==================================================
# Line: 627

x = np.random.normal(
    0, 1, np.prod(input_shape)).astype(np.float32).reshape(input_shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
# Line: 313

state_ops.scatter_nd_update(ref, indices,
                            updates).get_shape().as_list(), shape)

# ==================================================
# Line: 566

self.scatter_nd(indices, updates, shape).get_shape().as_list(), shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
# Occurrences: Lines 69-109 (11 instances)

x = np.arange(1., 7.).reshape([1, 6]).astype(np.float32)

# ==================================================
# Line: 128

x = np.arange(1., 25.).reshape([2, 3, 4]).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
# Occurrences: Lines 74-102 (9 instances)

self._testAll(np.arange(-15, 15).reshape([2, 3, 5]).astype(bfloat16))

# ==================================================
# Line: 109

self._testAll(np.arange(-15, 15).reshape([2, 3, 5]).astype(np.int64))

# ==================================================
# Line: 120

np.arange(dtype.min, dtype.max + 1)
.reshape([2, 4, 2])
.astype(np_dtype)

# ==================================================
# Occurrences: Lines 132-135 (2 instances)

(1 + 2j) * np.arange(-15, 15).reshape([2, 3, 5]).astype(np.complex64))

# ==================================================
# Occurrences: Lines 141-144 (2 instances)

(1 + 2j) * np.arange(-15, 15).reshape([2, 3, 5]).astype(np.complex128))

# ==================================================
# Line: 207

np.arange(-15, 15).reshape([2, 3, 5]).astype(np.float32),

# ==================================================
# Line: 219

np.arange(-15, 15).reshape([2, 3, 5]).astype(np.float32))

# ==================================================
# Line: 573

x = np.arange(15).astype(in_type).reshape(*shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
# Line: 267

self.assertAllEqual((1, 2), dist.sample(1, seed=42).get_shape().as_list())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
# Line: 609

elems_ok = np.array([1] * 4).reshape((2, 2)).astype(np.int32)

# ==================================================
# Line: 624

elems_ok = np.array([1] * 8).reshape((2, 2, 2)).astype(np.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
# Line: 742

elems_ok = np.array([1] * 4).reshape((2, 2)).astype(np.int32)

# ==================================================
# Line: 754

elems_ok = np.array([1] * 8).reshape((2, 2, 2)).astype(np.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
# Line: 1365

ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, size=2).write(0, x0).write(1, x1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_matmul_op_test.py
# Occurrences: Lines 73-74 (2 instances)

x = np.arange(0., 4.).reshape([4, 1]).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_image_patches_op_test.py
# Line: 123

image = np.arange(16).reshape(1, 4, 4, 1).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
# Line: 104

x = np.arange(1, 6).reshape([5]).astype(dtype)

# ==================================================
# Line: 119

x = np.arange(1, 6).reshape([5]).astype(dtype)

# ==================================================
# Line: 127

x = np.arange(1, 6).reshape([5]).astype(dtype)

# ==================================================
# Line: 134

x = np.arange(0, 10).reshape([2, 5]).astype(dtype)

# ==================================================
# Line: 141

x = np.arange(0, 20).reshape([2, 2, 5]).astype(dtype)

# ==================================================
# Line: 148

x = np.arange(1, 145).reshape([2, 2, 3, 3, 2, 2]).astype(dtype)

# ==================================================
# Line: 167

x = np.arange(0, 10).reshape([2, 5]).astype(np.float32)

# ==================================================
# Line: 184

x = np.arange(0, 50).reshape(shape).astype(np.float64)

# ==================================================
# Line: 258

x = np.arange(1, 6).reshape([5]).astype(dtype)

# ==================================================
# Line: 268

x = np.arange(1, 6).reshape([5]).astype(dtype)

# ==================================================
# Line: 276

x = np.arange(1, 6).reshape([5]).astype(dtype)

# ==================================================
# Line: 283

x = np.arange(1, 11).reshape([2, 5]).astype(dtype)

# ==================================================
# Line: 290

x = np.arange(1, 21).reshape([2, 2, 5]).astype(dtype)

# ==================================================
# Occurrences: Lines 297-302 (2 instances)

x = np.arange(1, 145).reshape([2, 2, 3, 3, 2, 2]).astype(dtype)

# ==================================================
# Line: 319

x = np.arange(1, 9).reshape(shape).astype(np.float64)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
# Line: 1229

var.scatter_nd_update([[1]], [4.]).scatter_nd_add([[0]], [2.])
.scatter_nd_sub([[1]], [3]),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/dataset_ops.py
# Line: 5066

class_values_ds.batch(dist_estimation_batch_size, name=name).scan(
    initial_examples_per_class_seen, update_estimate_and_tile,
    name=name).unbatch(name=name))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/counter_op.py
# Line: 25

return (dataset_ops.Dataset.from_tensors(0, name=name).repeat(None).scan(
    start, lambda state, _: (state + step, state)))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
# Line: 170

dataset_ops.Dataset.from_tensor_slices(components).shuffle(5).repeat()

# ==================================================
# Line: 227

dataset_ops.Dataset.from_tensor_slices(components)
.shuffle(dataset_ops.UNKNOWN)
.repeat()

# ==================================================
# Line: 278

dataset = dataset_ops.Dataset.range(10).shuffle(10, seed=1).shuffle(1)

# ==================================================
# Line: 294

dataset = dataset_ops.Dataset.range(10).shuffle(
    10, seed=op_seed, reshuffle_each_iteration=reshuffle).repeat(3)

# ==================================================
# Line: 317

dataset = dataset_ops.Dataset.range(100).shuffle(
    10, reshuffle_each_iteration=reshuffle).repeat(3)

# ==================================================
# Line: 353

dataset = dataset.shuffle(10).repeat(len(sizes)).take(3)

# ==================================================
# Line: 366

dataset = dataset.shuffle(10).repeat().take(3)

# ==================================================
# Line: 374

dataset = dataset_ops.Dataset.range(10).shuffle(
    10, seed=seed, reshuffle_each_iteration=reshuffle).repeat(2)

# ==================================================
# Line: 547

dataset_ops.Dataset.range(range_limit)
.shuffle(
    buffer_size,
    seed=seed,
    reshuffle_each_iteration=reshuffle_each_iteration,
)
.repeat(num_repeats)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/ignore_errors_test.py
# Line: 45

dataset_ops.Dataset.from_tensor_slices(components).map(
    lambda x: array_ops.check_numerics(x, "message")).ignore_errors())

# ==================================================
# Line: 58

dataset_ops.Dataset.from_tensor_slices(components).map(
    lambda x: array_ops.check_numerics(x, "message")).ignore_errors(
        log_warning=True))

# ==================================================
# Line: 76

dataset_ops.Dataset.from_tensor_slices(components).map(
    lambda x: array_ops.check_numerics(x, "message"),
    num_parallel_calls=2).prefetch(2).ignore_errors())

# ==================================================
# Line: 100

dataset_ops.Dataset.from_tensor_slices(filenames).map(
    io_ops.read_file, num_parallel_calls=2).prefetch(2).ignore_errors())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
# Line: 116

dataset_ops.Dataset.range(10)
.map(lambda x: {"foo": x * 2, "bar": x**2})
.flat_map(
    lambda d: dataset_ops.Dataset.from_tensors(d["foo"]).repeat(
        d["bar"]
    )
)

# ==================================================
# Line: 143

dataset = dataset_ops.Dataset.range(10).map(_map_fn).flat_map(_flat_map_fn)

# ==================================================
# Line: 162

dataset = dataset_ops.Dataset.range(10).map(_map_fn).flat_map(_flat_map_fn)

# ==================================================
# Line: 181

dataset = dataset_ops.Dataset.range(10).map(_map_fn).flat_map(_flat_map_fn)

# ==================================================
# Line: 424

return dataset_ops.Dataset.range(10).map(_map_fn).flat_map(_flat_map_fn)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
# Line: 67

dataset = dataset_ops.Dataset.from_tensors(components).repeat(
    inner_count).repeat(outer_count)

# ==================================================
# Line: 202

dataset = dataset_ops.Dataset.range(elements).repeat(count_1).repeat(
    count_2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
# Line: 156

input_dataset = dataset_ops.Dataset.from_tensor_slices(math_ops.range(
    128)).map(_map_fn).filter(lambda d: math_ops.equal(d["x"] % 2, 0))

# ==================================================
# Line: 338

dataset = dataset_ops.Dataset.range(1).repeat().group_by_window(
    key_func=lambda x: x % 2,
    reduce_func=lambda key, window: dataset_ops.Dataset.from_tensors(key),
    window_size=4)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
# Line: 70

dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    _map_fn).repeat(count)

# ==================================================
# Line: 205

return dataset_ops.Dataset.range(10).map(lambda x: {
    "foo": x * 2,
    "bar": x**2
}).filter(lambda d: math_ops.equal(d["bar"] % 2, 0)).map(
    lambda d: d["foo"] + d["bar"])

# ==================================================
# Line: 227

return dataset_ops.Dataset.range(10).map(_map_fn).filter(_filter_fn).map(
    lambda x, i: x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
# Line: 62

dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    _map_fn).repeat(count).window(
        size=size,
        shift=shift,
        stride=stride,
        drop_remainder=drop_remainder).flat_map(_flat_map_fn)

# ==================================================
# Line: 107

ds = dataset_ops.Dataset.range(10).map(lambda x: x).repeat(count).window(
    size=size, shift=shift,
    stride=stride).flat_map(lambda x: x.batch(batch_size=size))

# ==================================================
# Line: 126

dataset = dataset_ops.Dataset.range(10).map(_sparse).window(
    size=5, shift=3,
    drop_remainder=True).flat_map(lambda x: x.batch(batch_size=5))

# ==================================================
# Line: 149

dataset = dataset_ops.Dataset.range(10).map(_sparse).window(
    size=5, shift=3,
    drop_remainder=True).flat_map(lambda x: x.batch(batch_size=5))

# ==================================================
# Line: 176

dataset = dataset_ops.Dataset.range(10).map(_sparse).window(
    size=4, shift=2,
    drop_remainder=True).flat_map(lambda x: x.batch(batch_size=4)).window(
        size=3, shift=1,
        drop_remainder=True).flat_map(lambda x: x.batch(batch_size=3))

# ==================================================
# Line: 206

dataset = dataset_ops.Dataset.from_generator(
    generator, dtypes.float32, output_shapes=[None]).window(
        size=3, shift=1).flat_map(lambda x: x.batch(batch_size=3))

# ==================================================
# Line: 219

dataset = dataset_ops.Dataset.from_tensor_slices(input_values).map(
    lambda x: array_ops.check_numerics(x, "message")).window(
        size=2, shift=2, stride=2,
        drop_remainder=True).flat_map(lambda x: x.batch(batch_size=2))

# ==================================================
# Line: 250

dataset = dataset_ops.Dataset.from_tensors(42).window(
    1, name="window").flat_map(lambda x: x)

# ==================================================
# Line: 259

dataset = dataset_ops.Dataset.range(42).window(6).interleave(
    lambda x: x, cycle_length=2, num_parallel_calls=2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/take_while_test.py
# Line: 110

dataset = dataset_ops.Dataset.range(10).take_while(
    predicate=lambda x: x < 2).repeat(5)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
# Line: 50

dataset = dataset_ops.Dataset.from_tensor_slices(seq_lens).map(
    lambda x: array_ops.fill([x], x)).padded_batch(
        batch_size=batch_size,
        drop_remainder=drop_remainder,
        padded_shapes=padded_shapes)

# ==================================================
# Line: 88

dataset_ops.Dataset.from_tensor_slices(
    [6, 5, 5, 5, 5]).map(lambda x: array_ops.fill([x], x)).padded_batch(
        batch_size=4, padded_shapes=[5]))

# ==================================================
# Line: 97

dataset_ops.Dataset.from_tensor_slices(
    [0, 0, 0, 0]).map(lambda x: array_ops.fill([x], x)).padded_batch(
        batch_size=4, padded_shapes=[-1]))

# ==================================================
# Line: 129

dataset_ops.Dataset.from_tensor_slices(
    [1, 2, 3, 4]).map(fill).padded_batch(batch_size=2))

# ==================================================
# Line: 142

dataset_ops.Dataset.from_tensor_slices(
    [1, 2, 3, 4]).map(fill_tuple).padded_batch(batch_size=2))

# ==================================================
# Line: 165

dataset_ops.Dataset.from_tensor_slices(random_seq_lens).map(fill_tuple)
.padded_batch(
    4, padded_shapes=([-1], [-1], {'structure': [-1]}),
    padding_values=padding_values))

# ==================================================
# Line: 255

_ = dataset_ops.Dataset.from_tensors(st).repeat(10).padded_batch(10)

# ==================================================
# Line: 268

_ = dataset_ops.Dataset.from_tensors(rt).repeat(10).padded_batch(10)

# ==================================================
# Line: 378

dataset = dataset_ops.Dataset.from_tensor_slices(seq_lens).map(
    lambda x: array_ops.fill([x], x)).padded_batch(
        batch_size=4, padded_shapes=[-1])

# ==================================================
# Line: 401

return dataset_ops.Dataset.from_tensor_slices(seq_lens).map(
    fill_tuple).padded_batch(
        batch_size=4,
        padded_shapes=(padded_shape, padded_shape),
        padding_values=(-1, '<end>'))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
# Line: 46

ds = dataset_ops.Dataset.range(0).with_options(options).cache()

# ==================================================
# Line: 53

ds = dataset_ops.Dataset.range(0).with_options(options).with_options(
    options)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
# Line: 221

dataset = dataset_ops.Dataset.from_tensors(
    (list(range(10)), None)).unbatch().map(lambda x, y: x)

# ==================================================
# Line: 243

dataset = dataset_ops.Dataset.from_tensor_slices(components).batch(
    batch_size).unbatch()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py
# Line: 268

dataset = dataset_ops.Dataset.range(16).batch(
    2, drop_remainder=True).batch(
        4, drop_remainder=True)

# ==================================================
# Line: 286

dataset = dataset_ops.Dataset.range(8).map(map_fn).batch(
    4, drop_remainder=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/prefetch_test.py
# Line: 98

dataset = dataset_ops.Dataset.range(10).map(map_py_fn).prefetch(3)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/unique_test.py
# Line: 101

return dataset_ops.Dataset.range(num_elements).map(
    lambda x: x % unique_elem_range).unique()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
# Line: 181

dataset = dataset.map(lambda a: a).batch(4).repeat(2)

# ==================================================
# Line: 189

return dataset_ops.Dataset.range(100).shuffle(100).cache(cache_path)

# ==================================================
# Line: 300

dataset = dataset_ops.Dataset.range(10).cache().take(5).repeat(2)

# ==================================================
# Line: 314

dataset = dataset_ops.Dataset.range(10).map(increment_fn).cache().repeat(2)

# ==================================================
# Line: 340

dataset = dataset_ops.Dataset.range(10).map(increment_fn).cache()

# ==================================================
# Line: 449

return dataset_ops.Dataset.range(self.range_size).cache(filename).repeat(
    self.num_repeats)

# ==================================================
# Line: 682

dataset = dataset_ops.Dataset.range(20).filter(
    lambda x: math_ops.equal(x % 2, 0)).cache()

# ==================================================
# Line: 689

dataset = dataset_ops.Dataset.range(20).filter(
    lambda x: math_ops.equal(x % 2, 0)).repeat(-1).cache()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/rejection_resample_test.py
# Line: 41

dataset = dataset_ops.Dataset.from_tensor_slices(classes).shuffle(
    200, seed=21).map(lambda c: (c, string_ops.as_string(c))).repeat()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/get_single_element_test.py
# Line: 52

dataset = dataset_ops.Dataset.range(100).skip(skip).map(
    lambda x: (x * x, make_sparse(x))).take(take)

# ==================================================
# Line: 73

dataset = dataset_ops.Dataset.range(10).window(2).flat_map(flat_map_func)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
# Line: 138

dataset = dataset_ops.Dataset.random(
    seed=42, name="random").take(1).map(lambda _: 42)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
# Line: 193

dataset = dataset_ops.Dataset.from_tensor_slices(input_values).repeat(
    count).interleave(
        lambda x: dataset_ops.Dataset.from_tensors(x).repeat(x),
        cycle_length, block_length, num_parallel_calls)

# ==================================================
# Line: 222

dataset = dataset_ops.Dataset.from_tensor_slices(input_values).map(
    lambda x: array_ops.check_numerics(x, "message")).interleave(
        dataset_ops.Dataset.from_tensors, cycle_length, block_length,
        num_parallel_calls)

# ==================================================
# Line: 248

dataset = dataset_ops.Dataset.range(10).map(_map_fn).interleave(
    _interleave_fn, cycle_length=1)

# ==================================================
# Line: 287

dataset = dataset_ops.Dataset.from_tensor_slices(input_values).repeat(
    count).interleave(
        lambda x: dataset_ops.Dataset.from_tensors(x).repeat(x),
        cycle_length, block_length, num_parallel_calls)

# ==================================================
# Line: 650

return dataset_ops.Dataset.range(10).map(_map_fn).interleave(
    _interleave_fn, cycle_length=1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
# Line: 91

dataset_ops.Dataset.from_tensor_slices(components).map(_map_fn)
.repeat(14))

# ==================================================
# Line: 118

dataset_ops.Dataset.from_tensor_slices(tensor_components)
.map(_map_fn).repeat(14))

# ==================================================
# Line: 146

dataset_ops.Dataset.from_tensor_slices(components)
.map(_map_fn).repeat(14))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
# Line: 565

dataset = apply_map(dataset, fn).repeat(1000).batch(10)

# ==================================================
# Occurrences: Lines 1178-1183 (2 instances)

_ = dataset_ops.Dataset.range(10).batch(2).map(random_func_seeded)

# ==================================================
# Line: 1606

dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    _map_fn, num_parallel_calls=num_parallel_calls).repeat(num_epochs)

# ==================================================
# Line: 1638

return (dataset_ops.Dataset.from_tensors(0).repeat(10).map(
    lambda _: counter_var.assign_add(1),
    num_parallel_calls=num_parallel_calls))

# ==================================================
# Line: 1653

return (dataset_ops.Dataset.from_tensors(0).repeat(10).map(
    lambda x: x + constant_var, num_parallel_calls=num_parallel_calls))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/iterator_cluster_test.py
# Line: 166

dataset_ops.Dataset.from_tensor_slices(components).map(_map_fn)
.repeat(None).prefetch(10000))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
# Line: 41

dataset = dataset_ops.Dataset.from_generator(
    generator, output_types=dtypes.int64).repeat(num_repeats).prefetch(5)

# ==================================================
# Line: 132

return (dataset_ops.Dataset.from_generator(
    generator, output_types=(dtypes.int64, dtypes.int64),
    output_shapes=([None], [3]))
        .repeat(num_inner_repeats).prefetch(5))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
# Line: 161

readers.TextLineDataset(filename).repeat().batch(16))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
# Line: 47

return dataset_ops.Dataset.from_tensors(0).repeat().scan(
    initial_state=start, scan_func=scan_fn)

# ==================================================
# Line: 71

data = dataset_ops.Dataset.from_tensors(1).repeat(None).scan(
    initial_state=[0, 1],
    scan_func=lambda a, _: ([a[1], a[0] + a[1]], a[1]))

# ==================================================
# Line: 203

dataset = dataset_ops.Dataset.from_tensors(0).repeat(5).scan(
    initial_state=([0], 1), scan_func=_scan_fn)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/sparse_batch_test.py
# Line: 33

dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    lambda x: array_ops.fill([x], x)).sparse_batch(4, [12])

# ==================================================
# Line: 55

dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    lambda x: array_ops.fill([x, x], x)).sparse_batch(4, [5, None])

# ==================================================
# Line: 109

return dataset_ops.Dataset.from_tensor_slices(components).map(
    lambda x: array_ops.fill([x], x)).sparse_batch(4, [12])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/cardinality_test.py
# Occurrences: Lines 45-47 (2 instances)

lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).batch(2),

# ==================================================
# Occurrences: Lines 54-75 (6 instances)

lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).concatenate(
    dataset_ops.Dataset.range(5)), dataset_ops.UNKNOWN),

# ==================================================
# Occurrences: Lines 93-104 (3 instances)

("Interleave3", lambda: dataset_ops.Dataset.range(5).repeat().interleave(
    lambda _: dataset_ops.Dataset.from_tensors(0),
    cycle_length=1,
    num_parallel_calls=1), dataset_ops.INFINITE),

# ==================================================
# Occurrences: Lines 131-147 (6 instances)

lambda: dataset_ops.Dataset.range(5).filter(lambda _: True).shard(2, 0),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
# Line: 78

dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    _map_fn).repeat(count).batch(batch_size, drop_remainder,
                                 num_parallel_calls)

# ==================================================
# Line: 121

dataset = dataset_ops.Dataset.range(10).map(map_fn).batch(5)

# ==================================================
# Line: 132

dataset = dataset_ops.Dataset.range(10).map(_sparse).batch(5)

# ==================================================
# Line: 151

dataset = dataset_ops.Dataset.range(10).map(_sparse).batch(5)

# ==================================================
# Line: 174

dataset = dataset_ops.Dataset.range(10).map(_sparse).batch(5).batch(2)

# ==================================================
# Line: 208

dataset = dataset_ops.Dataset.range(10).map(_ragged).batch(5)

# ==================================================
# Line: 217

dataset = dataset_ops.Dataset.range(10).map(ragged_math_ops.range).batch(5)

# ==================================================
# Line: 231

dataset = dataset_ops.Dataset.range(10).map(_ragged).batch(5).batch(2)

# ==================================================
# Line: 240

dataset = dataset_ops.Dataset.range(10).map(lambda x: (x, None)).batch(
    10).map(lambda x, y: x)

# ==================================================
# Line: 349

return dataset_ops.Dataset.range(10).map(self._sparse).batch(batch_size)

# ==================================================
# Line: 358

return dataset_ops.Dataset.range(10).map(self._sparse).batch(5).batch(2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
# Line: 303

dataset = dataset_ops.Dataset.from_tensor_slices([1, 2, 3, 4, 5, 6]).map(
    math_ops.square).batch(2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
# Line: 100

dataset = dataset_ops.Dataset.range(2 * i).map(_sparse).apply(
    grouping.group_by_reducer(lambda x: x.values[0] % 2, reducer))

# ==================================================
# Line: 123

dataset = dataset_ops.Dataset.from_tensors(np.int64(0)).repeat(i).apply(
    grouping.group_by_reducer(lambda x: x, reducer))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
# Line: 78

return dataset_ops.Dataset.from_tensor_slices(input_values).repeat(
    self.repeat_count).apply(
        interleave_ops.parallel_interleave(
            interleave_fn, cycle_length, block_length, sloppy,
            buffer_output_elements, prefetch_input_elements))

# ==================================================
# Line: 238

dataset = dataset_ops.Dataset.range(10).map(_map_fn).apply(
    interleave_ops.parallel_interleave(_interleave_fn, cycle_length=1))

# ==================================================
# Line: 267

return dataset_ops.Dataset.from_tensor_slices(input_values).map(
    map_fn).repeat(self.repeat_count).apply(
        interleave_ops.parallel_interleave(
            interleave_fn, cycle_length, block_length, sloppy,
            buffer_output_elements, prefetch_input_elements))

# ==================================================
# Line: 311

return dataset_ops.Dataset.from_tensor_slices(input_values).repeat(
    self.repeat_count).apply(
        interleave_ops.parallel_interleave(
            interleave_fn, cycle_length, block_length, sloppy,
            buffer_output_elements, prefetch_input_elements))

# ==================================================
# Line: 409

return (dataset_ops.Dataset.from_tensor_slices(self.input_values).repeat(
    self.num_repeats).apply(
        interleave_ops.parallel_interleave(
            lambda x: dataset_ops.Dataset.range(10 * x, 11 * x),
            cycle_length, block_length, sloppy)))

# ==================================================
# Line: 453

return dataset_ops.Dataset.range(10).map(_map_fn).apply(
    interleave_ops.parallel_interleave(_interleave_fn, 1))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_batched_features_dataset_test.py
# Line: 94

core_readers.TFRecordDataset(self._filenames)
.map(lambda x: parsing_ops.parse_single_example(x, features))
.repeat(10).batch(2))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
# Line: 75

dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    _map_fn).repeat(count)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_and_batch_fusion_test.py
# Line: 30

dataset = dataset_ops.Dataset.range(10).apply(
    testing.assert_next(
        ["MapAndBatch"])).map(lambda x: x * x).batch(10)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
# Line: 74

return dataset_ops.Dataset.from_tensors(0).repeat(10).apply(
    grouping.group_by_window(lambda _: 0, reduce_fn, 10))

# ==================================================
# Line: 106

dataset = dataset_ops.Dataset.range(
    10).map(lambda _: random_ops.random_uniform([])).batch(10)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_and_filter_fusion_test.py
# Line: 92

dataset = dataset_ops.Dataset.range(10).apply(
    testing.assert_next(["Map", "Filter",
                         "Map"])).map(function).filter(predicate)

# ==================================================
# Line: 112

dataset = dataset_ops.Dataset.range(10).apply(
    testing.assert_next(["Map", "Filter"])).map(function).filter(predicate)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_fusion_test.py
# Line: 65

dataset = dataset_ops.Dataset.range(5).apply(
    testing.assert_next(["Map", "Filter", "MemoryCacheImpl"])).map(function)

# ==================================================
# Line: 102

dataset = dataset_ops.Dataset.range(10).apply(
    testing.assert_next(["Filter", "Filter"
                        ])).filter(predicate).filter(lambda x: True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_parallelization_test.py
# Line: 62

dataset = dataset_ops.Dataset.range(5).apply(
    testing.assert_next(next_nodes)).map(function)

# ==================================================
# Line: 74

dataset_ops.Dataset.range(5)
.apply(testing.assert_next(["Map"]))
.map(lambda x: x + 1, synchronous=True)

# ==================================================
# Line: 91

dataset = dataset_ops.Dataset.range(5).apply(
    testing.assert_next(["ParallelMap"])).map(fn)

# ==================================================
# Line: 105

dataset = dataset_ops.Dataset.range(5).apply(
    testing.assert_next(["Map"])).map(fn)

# ==================================================
# Line: 123

dataset = dataset_ops.Dataset.range(4).apply(
    testing.assert_next(next_nodes)).map(lambda x: x + 2)

# ==================================================
# Line: 138

ds = dataset_ops.Dataset.range(i).apply(testing.assert_next(
    ["Map"])).map(lambda x: x + 1)

# ==================================================
# Line: 155

ds = dataset_ops.Dataset.range(i).apply(testing.assert_next(
    ["Map"])).map(lambda x: x + 1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/shuffle_and_repeat_fusion_test.py
# Line: 33

dataset = dataset_ops.Dataset.range(10).apply(
    testing.assert_next([expected])).shuffle(10).repeat(2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
# Line: 181

ds = dataset_ops.Dataset.range(num_elements).shuffle(num_elements).repeat(
    num_repeats)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/metadata_test.py
# Line: 55

return (dataset_ops.Dataset.range(10).shard(distribute.SHARD_HINT,
                                            distribute.SHARD_HINT).repeat())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
# Line: 191

dataset = dataset_ops.Dataset.range(10000000).repeat().shuffle(
    buffer_size=100)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/dense_to_sparse_batch_test.py
# Line: 34

dataset = dataset_ops.Dataset.from_tensor_slices(
    components).map(lambda x: array_ops.fill([x], x)).apply(
        batching.dense_to_sparse_batch(4, [12]))

# ==================================================
# Line: 57

dataset = dataset_ops.Dataset.from_tensor_slices(
    components).map(lambda x: array_ops.fill([x, x], x)).apply(
        batching.dense_to_sparse_batch(4, [5, None]))

# ==================================================
# Line: 113

return dataset_ops.Dataset.from_tensor_slices(components).map(
    lambda x: array_ops.fill([x], x)).apply(
        batching.dense_to_sparse_batch(4, [12]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
# Line: 65

dataset = dataset_ops.Dataset.from_tensor_slices(components).repeat(
    count).apply(
        batching.map_and_batch(
            map_func=_map_fn,
            batch_size=batch_size,
            num_parallel_calls=num_parallel_calls,
            num_parallel_batches=num_parallel_batches))

# ==================================================
# Line: 270

dataset = dataset_ops.Dataset.from_tensor_slices(components).repeat(
    1000).apply(batching.map_and_batch(_map_fn, batch_size=100))

# ==================================================
# Line: 321

dataset = dataset_ops.Dataset.from_generator(gen, dtype).repeat(100).apply(
    batching.map_and_batch(lambda x: x, batch_size=10))

# ==================================================
# Line: 332

dataset = self.structuredDataset(None).repeat().apply(
    batching.map_and_batch(map_fn, batch_size=10))

# ==================================================
# Line: 341

dataset = self.structuredDataset(None).repeat().apply(
    batching.map_and_batch(map_fn, batch_size=10))

# ==================================================
# Line: 350

dataset = self.structuredDataset(
    (None,
     None)).repeat().apply(batching.map_and_batch(map_fn, batch_size=10))

# ==================================================
# Line: 361

dataset = self.structuredDataset(
    (None,
     None)).repeat().apply(batching.map_and_batch(map_fn, batch_size=10))

# ==================================================
# Line: 372

dataset = self.structuredDataset(None).repeat().apply(
    batching.map_and_batch(lambda x: captured_t, batch_size=10))

# ==================================================
# Line: 487

return dataset_ops.Dataset.range(
    range_start, range_start + range_size).shard(
        num_shards=num_shards, index=0).repeat(num_repeats).apply(
            batching.map_and_batch(
                map_func=_map_fn,
                batch_size=batch_size,
                num_parallel_batches=num_parallel_batches,
                drop_remainder=drop_remainder))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
# Line: 225

dataset = dataset_ops.Dataset.range(1024).map(lambda x: (x, x)).batch(32)

# ==================================================
# Line: 235

dataset = dataset_ops.Dataset.range(8).map(
    lambda x: {"a": x, "b": {"c": x + 1}}).batch(4)

# ==================================================
# Line: 279

dataset = dataset_ops.Dataset.range(16).batch(2).batch(4)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_next_test.py
# Line: 31

dataset = dataset_ops.Dataset.from_tensors(0).apply(
    testing.assert_next(["Map"])).map(lambda x: x)

# ==================================================
# Line: 42

dataset = dataset_ops.Dataset.from_tensors(0).apply(
    testing.assert_next(["Map", "Batch"])).map(lambda x: x).batch(1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_prev_test.py
# Line: 31

dataset = dataset_ops.Dataset.from_tensors(0).map(
    lambda x: x, deterministic=True, num_parallel_calls=8).apply(
        testing.assert_prev([("ParallelMapDataset",
                              {"deterministic", "true"})]))

# ==================================================
# Line: 44

dataset = dataset_ops.Dataset.from_tensors(0).map(
    lambda x: x, deterministic=True, num_parallel_calls=8).batch(1).apply(
        testing.assert_prev([("BatchDataset", {}),
                             ("ParallelMapDataset", {
                                 "deterministic": "true"
                             })]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
# Line: 123

ds = dataset_ops.Dataset.range(500).batch(100).apply(
    shuffle_ops.shuffle_and_repeat(
        buffer_size=5 * num_epochs, count=num_epochs))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_saveable_from_iterator_test.py
# Line: 33

ds = dataset_ops.Dataset.range(num_outputs).shuffle(
    10, reshuffle_each_iteration=False).prefetch(10)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/saveable_compat_test.py
# Line: 152

checkpoint.Checkpoint(dep).read(checkpoint_path).assert_consumed()

# ==================================================
# Line: 163

checkpoint.Checkpoint(dep).read(checkpoint_path).assert_consumed()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint_view_test.py
# Line: 35

checkpoint_view.CheckpointView(root_save_path).children(0).items()))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/benchmarks_test.py
# Line: 101

all_names, all_dtypes = zip(*py_checkpoint_reader.NewCheckpointReader(
    checkpoint_path).get_variable_to_dtype_map().items())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/graph_view.py
# Line: 75

for name, ref in super(ObjectGraphView,
                       self).children(obj, save_type, **kwargs).items():

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# Line: 228

checkpoint.restore(save_path).assert_consumed().initialize_or_restore()

# ==================================================
# Line: 237

checkpoint.restore(save_path).assert_consumed().initialize_or_restore()

# ==================================================
# Line: 617

status = load_root.restore(
    save_path).assert_consumed().assert_existing_objects_matched()

# ==================================================
# Line: 1400

ckpt.restore(save_path).assert_consumed().run_restore_ops()

# ==================================================
# Line: 1421

ckpt.read(ckpt_path).assert_consumed().run_restore_ops()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/sharding/sharding_policies_test.py
# Line: 702

ckpt_key, tensor = list(super()._serialize_to_tensors().items())[0]

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/trackable/base_delegate_test.py
# Line: 82

ckpt2.restore(prefix_tensor).assert_consumed().run_restore_ops()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
# Line: 321

tfconfig_cluster_resolver.TFConfigClusterResolver()
.cluster_spec()
.as_dict()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
# Line: 567

dataset = get_dataset_from_tensor_slices(
    [5]).map(lambda x: math_ops.cast(x, dtypes.int64)).batch(2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/values_test.py
# Line: 326

dataset = dataset_ops.DatasetV2.from_tensors([0, 1, 2]).repeat().batch(
    2, drop_remainder=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/values.py
# Line: 1095

op_device = pydev.DeviceSpec.from_string(self.device).replace(
    device_type="CPU", device_index=0).to_string()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/input_lib_test.py
# Line: 376

local_list = array_ops.concat(local, axis=0).numpy().tolist()

# ==================================================
# Line: 387

local_list = array_ops.concat(local, axis=0).numpy().tolist()

# ==================================================
# Line: 891

dataset = dataset_ops.Dataset.range(16).shuffle(16).cache().batch(4)

# ==================================================
# Line: 919

dataset = dataset_ops.Dataset.range(12).shuffle(
    12, reshuffle_each_iteration=reshuffle).batch(4)

# ==================================================
# Line: 996

data = iter(dist_dataset).get_next_as_optional().get_value()

# ==================================================
# Line: 1136

dataset = dataset_ops.Dataset.range(10).map(lambda x: {  # pylint: disable=g-long-lambda
    "y": math_ops.cast(x, dtypes.float32) ** 2,
}).batch(4)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distributed_table_test.py
# Line: 95

dataset = dataset_ops.DatasetV2.from_tensors(tensor).repeat().batch(
    batch_size, drop_remainder=True)

# ==================================================
# Line: 250

dataset = dataset.repeat().batch(24, drop_remainder=True).prefetch(2)

# ==================================================
# Line: 346

dataset = dataset.repeat().batch(24, drop_remainder=True).prefetch(2)

# ==================================================
# Line: 424

dataset_ops.DatasetV2.from_tensors(
    constant_op.constant([0, 1, 3], dtype=dtypes.int64)).repeat().batch(
        24, drop_remainder=True).prefetch(2))

# ==================================================
# Line: 599

dataset_ops.DatasetV2.from_tensors(
    constant_op.constant([0, 1, 3], dtype=dtypes.int64)).repeat().batch(
        24, drop_remainder=True).prefetch(2))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/ps_values_test.py
# Line: 45

checkpoint.restore(save_path).assert_consumed().run_restore_ops()

# ==================================================
# Line: 54

checkpoint.restore(save_path).assert_consumed().run_restore_ops()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
# Occurrences: Lines 598-600 (2 instances)

self._num_ps = len(cluster_resolver.cluster_spec().as_dict().get("ps", []))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/tpu_replicated_variable_test.py
# Line: 120

ckpt.restore(save_path).assert_consumed().run_restore_ops()

# ==================================================
# Line: 142

ckpt.restore(save_path).assert_consumed().run_restore_ops()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/experimental/multi_worker_mirrored_strategy_test.py
# Line: 548

return dataset_ops.Dataset.from_tensors(
    (self.images, self.labels)).repeat().batch(
        local_batch_size, drop_remainder=True).prefetch(2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
# Line: 634

return dataset_ops.Dataset.from_tensors(
    (self.images, self.labels)).repeat().batch(
        local_batch_size, drop_remainder=True).prefetch(2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
# Line: 101

checkpoint.restore(save_path).assert_consumed().run_restore_ops()

# ==================================================
# Line: 118

checkpoint.restore(save_path).assert_consumed().run_restore_ops()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
# Line: 34

return dataset_ops.Dataset.range(1000).map(
    lambda x: {"labels": x % 5, "predictions": x % 3}).batch(
        4, drop_remainder=True)

# ==================================================
# Line: 46

return dataset_ops.Dataset.from_tensor_slices({
    "labels": [True, False, True, False],
    "predictions": [True, True, False, False]}).repeat().batch(
        3, drop_remainder=True)

# ==================================================
# Line: 59

return dataset_ops.Dataset.from_tensor_slices({
    "labels": [True, False, True, False],
    "predictions": [1.0, 0.75, 0.25, 0.]}).repeat().batch(
        3, drop_remainder=True)

# ==================================================
# Line: 139

return dataset_ops.Dataset.range(1000).map(math_ops.to_float).batch(
    4, drop_remainder=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
# Line: 239

ds1 = dataset_ops.DatasetV2.range(10).batch(2).batch(5)

# ==================================================
# Line: 288

return readers.TextLineDatasetV2(dataset).map(
    string_ops.string_to_number).batch(
        input_context.get_per_replica_batch_size(4))

# ==================================================
# Line: 402

list(dataset_ops.DatasetV2.range(10).batch(1).as_numpy_iterator()))

# ==================================================
# Line: 539

return readers.TextLineDatasetV2(dataset).map(
    string_ops.string_to_number).batch(
        input_context.get_per_replica_batch_size(4))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
# Line: 322

dataset = dataset_ops.Dataset.from_tensors(tensor).repeat().batch(
    batch_size, drop_remainder=True)

# ==================================================
# Line: 458

dataset = dataset_ops.Dataset.from_tensors(("string", 1.0)).repeat().batch(
    2, drop_remainder=False)

# ==================================================
# Line: 620

sum_val = train_step().numpy().astype(float)

# ==================================================
# Line: 1148

dataset_ops.Dataset.from_tensors(y).repeat(num_replicas).batch(
    num_replicas))

# ==================================================
# Line: 1169

dataset_ops.Dataset.from_tensors(y).repeat(num_replicas).batch(
    num_replicas))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/zero_batch_test.py
# Line: 173

dataset = dataset_ops.Dataset.from_tensor_slices((inputs, targets)).batch(
    10, drop_remainder=False).repeat()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/strategy_common_test.py
# Line: 628

d = dataset_ops.DatasetV2.range(100).repeat().batch(batch_size)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
# Line: 714

dataset = dataset_ops.DatasetV2.range(0, 100).shuffle(100).batch(1)

# ==================================================
# Line: 1564

dataset = dataset_ops.DatasetV2.from_tensor_slices([2.]).repeat().batch(
    self.strategy.num_replicas_in_sync)

# ==================================================
# Line: 1619

dataset = dataset_ops.DatasetV2.range(0, 10).batch(
    self.strategy.num_replicas_in_sync).map(map_fn)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
# Line: 381

key = next(line_iter).strip().replace(":", "")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
# Line: 1536

attr_val_str = repr(attrs[attr_key]).strip().replace("\n", " ")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
# Line: 92

dataset = dataset_ops.Dataset.from_tensor_slices(tensor).batch(2).map(
    map_fn)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/profile_context_test.py
# Line: 39

opts = builder(builder.time_and_memory()).with_file_output(outfile).build()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
# Line: 58

opts = builder(builder.trainable_variables_parameter()).with_file_output(
    outfile).build()

# ==================================================
# Line: 79

builder(builder.trainable_variables_parameter()).with_file_output(
    outfile).with_accounted_types(['.*']).select([
        'micros', 'bytes', 'params', 'float_ops', 'occurrence',
        'device', 'op_types', 'input_shapes'
    ]).build())

# ==================================================
# Line: 152

builder(builder.trainable_variables_parameter()).with_file_output(
    outfile).with_accounted_types(['.*']).select([
        'params', 'float_ops', 'occurrence', 'device', 'op_types',
        'input_shapes'
    ]).build())

# ==================================================
# Line: 178

builder(builder.trainable_variables_parameter()).with_file_output(
    outfile).with_accounted_types(['.*']).with_node_names(
        show_name_regexes=['.*model_analyzer_testlib.*'
                          ]).account_displayed_op_only(False).select([
                              'bytes', 'params', 'float_ops',
                              'num_hidden_ops', 'device', 'input_shapes'
                          ]).build())

# ==================================================
# Line: 211

builder(builder.trainable_variables_parameter()).with_file_output(
    outfile).with_accounted_types(['.*']).with_node_names(
        show_name_regexes=['.*model_analyzer_testlib.py.*'
                          ]).account_displayed_op_only(False).select(
                              ['params', 'float_ops']).build())

# ==================================================
# Line: 270

builder(builder.trainable_variables_parameter()).with_empty_output()
.with_accounted_types(['.*']).account_displayed_op_only(False).select(
    ['bytes', 'params', 'float_ops', 'device']).build())

# ==================================================
# Line: 298

builder(builder.trainable_variables_parameter()).with_max_depth(100000)
.with_step(0).with_timeline_output(outfile).with_accounted_types(
    ['.*']).build())

# ==================================================
# Line: 330

builder(builder.trainable_variables_parameter()).with_file_output(
    outfile).with_accounted_types(
        ['.*']).with_min_occurrence(10).order_by('occurrence').select([
            'params', 'micros', 'bytes', 'peak_bytes', 'residual_bytes',
            'output_bytes', 'occurrence', 'input_shapes'
        ]).build())

# ==================================================
# Line: 355

lib.CheckAndRemoveDoc(f.read()).replace('\t',
                                        '').replace(' ', '')[0:170])

# ==================================================
# Line: 412

builder(builder.time_and_memory()).select([
    attribute
]).with_max_depth(100000).with_node_names(
    trim_name_regexes=['ops.py.*']).with_pprof_output(outfile).build())

# ==================================================
# Occurrences: Lines 493-530 (7 instances)

opts = builder(builder.time_and_memory(
    min_micros=min_val)).with_empty_output().build()

# ==================================================
# Occurrences: Lines 557-573 (3 instances)

opts = builder(
    builder.time_and_memory()).with_file_output(outfile).select(
        ['micros']).build()

# ==================================================
# Line: 589

gfile.Open(os.path.join(time_dir, ret[0]), 'r').read().find(
    'execution time') > 0)

# ==================================================
# Line: 598

gfile.Open(os.path.join(memory_dir, ret[0]), 'r').read().find(
    'requested bytes') > 0)

# ==================================================
# Occurrences: Lines 624-628 (2 instances)

builder(builder.time_and_memory()).with_file_output(
    os.path.join(time_dir, 'profile')).select(['micros']).build())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/profiler_test.py
# Line: 39

opts = (builder(builder.trainable_variables_parameter())
        .with_file_output(outfile)
        .with_accounted_types(['.*'])
        .select(['params', 'float_ops', 'micros', 'bytes',
                 'device', 'op_types', 'occurrence']).build())

# ==================================================
# Line: 175

opts = (builder(builder.trainable_variables_parameter())
        .with_empty_output()
        .with_accounted_types(['.*'])
        .select(['micros', 'bytes', 'peak_bytes',
                 'residual_bytes', 'output_bytes']).build())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/pprof_profiler.py
# Line: 434

device_name = str(device).strip('/').translate(
    maketrans('/:', '__'))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/utils/io_utils.py
# Occurrences: Lines 51-55 (2 instances)

overwrite = input('[WARNING] %s already exists - overwrite? '
                  '[y/n]' % (filepath)).strip().lower()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
# Line: 1405

self._deferred_slot_restorations.setdefault(
    slot_name, {}).setdefault(variable_key, []).append(
        slot_variable_position)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/saving/saveable_object_util_test.py
# Occurrences: Lines 216-221 (2 instances)

checkpoint.Checkpoint(a=converted_saveable_state).read(
    ckpt_path).assert_existing_objects_matched().expect_partial()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/optimizer.py
# Line: 1400

self._deferred_slot_restorations.setdefault(
    slot_name, {}).setdefault(variable_key, []).append(
        slot_variable_position)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
# Line: 136

dataset = dataset_ops.DatasetV2.range(5).repeat().batch(2)

# ==================================================
# Line: 143

dataset = dataset_ops.DatasetV2.range(5).repeat().batch(2)

# ==================================================
# Line: 150

dataset = dataset_ops.DatasetV2.range(5).filter(lambda _: True).batch(2)

# ==================================================
# Line: 157

dataset = dataset_ops.DatasetV2.range(5).filter(lambda _: True).batch(2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/transform/transform_test.py
# Line: 188

f.get_concrete_function(
    *args).pretty_printed_signature().split("\n")[1:],

# ==================================================
